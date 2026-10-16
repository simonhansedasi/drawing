import requests, pathlib
key = None
for line in pathlib.Path("/home/simonhans/coding/snotrac/.env").read_text().splitlines():
    if line.startswith("CENSUS_API_KEY"):
        key = line.split("=",1)[1].strip()

YEARS = list(range(2011, 2023))
VARS = "NAME,B17001A_001E,B17001A_002E"

for year in YEARS:
    out = pathlib.Path(f"acs_zcta_{year}_racepov_raw.json")
    if out.exists():
        print(year, "already cached", flush=True)
        continue
    url = f"https://api.census.gov/data/{year}/acs/acs5"
    params = {"get": VARS, "for": "zip code tabulation area:*", "key": key}
    r = requests.get(url, params=params, timeout=180)
    r.raise_for_status()
    out.write_text(r.text)
    print(year, "saved", len(r.text), "bytes", flush=True)
print("DONE")
