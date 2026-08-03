import sys, time, json, inspect, os, warnings, matplotlib

warnings.filterwarnings('ignore', category=matplotlib.MatplotlibDeprecationWarning)

call_log = []
PROJECT_DIR = None
NOTEBOOK_PATH = None
_tracing = False
_call_depth = 0  # counts depth of YOUR code only

def safe_repr(obj):
    try:
        return repr(obj)
    except Exception:
        return f'<unreprable {type(obj).__name__}>'

def is_my_code(filename):
    """Return True if the file is in the notebook or inside the project directory."""
    if filename.startswith("<ipython-input"):
        return True
    if PROJECT_DIR:
        # Compare absolute paths to avoid partial match issues
        abs_file = os.path.abspath(filename)
        abs_project = os.path.abspath(PROJECT_DIR)
        if abs_file.startswith(abs_project):
            return True
    return False

def tracer(frame, event, arg):
    global _call_depth
    filename = frame.f_code.co_filename

    if not is_my_code(filename):
        return tracer  # skip library/internal calls

    if event == 'call':
        _call_depth += 1

        try:
            arg_info = inspect.getargvalues(frame)
            args_repr = {k: safe_repr(arg_info.locals[k]) for k in arg_info.args}
            if arg_info.varargs:
                args_repr[arg_info.varargs] = safe_repr(arg_info.locals.get(arg_info.varargs, ()))
            if arg_info.keywords:
                args_repr[arg_info.keywords] = safe_repr(arg_info.locals.get(arg_info.keywords, {}))
        except Exception:
            args_repr = "<args unavailable>"

        call_log.append({
            "function": frame.f_code.co_name,
            "file": filename,
            "line": frame.f_lineno,
            "time": time.time(),
            "args": args_repr
        })

    elif event == 'return':
        if _call_depth > 0:
            _call_depth -= 1

    return tracer

def start(notebook_path=None):
    """Start tracing. Pass the path to the notebook to restrict logging."""
    global PROJECT_DIR, NOTEBOOK_PATH, _tracing
    if _tracing:
        return
    _tracing = True
    if notebook_path:
        NOTEBOOK_PATH = os.path.abspath(notebook_path)
        PROJECT_DIR = os.path.dirname(NOTEBOOK_PATH)
    else:
        # fallback: use current working directory if notebook path not provided
        PROJECT_DIR = os.getcwd()
    sys.settrace(tracer)

def stop(save_to=None):
    global _tracing
    sys.settrace(None)
    _tracing = False
    if save_to:
        os.makedirs(os.path.dirname(save_to), exist_ok=True)
        with open(save_to, "w") as f:
            json.dump(call_log, f, indent=2)
