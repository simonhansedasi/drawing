"""
Parse MEMORY.md and print YAML stubs for any project entries
not already present in graph_data.yaml. Run when new projects
are added to memory.
"""
import re
import yaml
from pathlib import Path

MEMORY = Path.home() / ".claude/projects/-home-simonhans-coding/memory/MEMORY.md"
GRAPH = Path(__file__).parent / "graph_data.yaml"

project_line = re.compile(r"\[.*?\]\(project_.*?\.md\)")

def existing_ids(data):
    ids = {p["id"] for p in data.get("projects", [])}
    ids |= {c["id"] for c in data.get("concepts", [])}
    return ids

def slug(label):
    return re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")

def main():
    with open(GRAPH) as f:
        data = yaml.safe_load(f)
    known = existing_ids(data)

    lines = MEMORY.read_text().splitlines()
    new_stubs = []
    for line in lines:
        if not project_line.search(line):
            continue
        # Extract display name from markdown link text
        m = re.search(r"\[([^\]]+)\]", line)
        if not m:
            continue
        label = m.group(1)
        node_id = slug(label)
        if node_id in known:
            continue
        stub = (
            f"  - id: {node_id}\n"
            f"    label: \"{label}\"\n"
            f"    domain: tools  # TODO: set domain\n"
            f"    connects_to: []  # TODO: add concept connections\n"
        )
        new_stubs.append(stub)

    if not new_stubs:
        print("graph_data.yaml is up to date — no new projects found.")
    else:
        print(f"Found {len(new_stubs)} new project(s). Add these under projects: in graph_data.yaml:\n")
        for s in new_stubs:
            print(s)

if __name__ == "__main__":
    main()
