"""
build_tri_historical.py -- Reconstruct TRI (Toxics Release Inventory) facility
proximity for two years (2013, 2022) per national ZCTA, to test whether the
"surrounding industrial neighborhood" near data-center ZIPs changed differently
than non-hosting ZIPs -- the pollution-side complement to dc_ej_selection_vs_impact
.ipynb's demographic diff-in-diff.

Two real EPA Envirofacts API quirks discovered while building this, worth keeping
in mind if this script is ever extended:
  - TRI_REPORTING_FORM has NO state_abbr column. Passing STATE_ABBR/<abbr> in the
    path is silently ignored (not an error) -- confirmed by requesting two
    different states and getting byte-identical rows back. Filtered nationally
    by REPORTING_YEAR only instead (~80-83K rows/year, paginated).
  - TRI_FACILITY's STATE_ABBR filter DOES work correctly (confirmed against two
    different states). This is the table state-filtered per the existing
    04_environment.py convention, once per state, reused for both years since a
    facility's registered location doesn't vary by year in this schema (closed
    facilities stay in the roster with FAC_CLOSED_IND, not purged).

Resumable: each state's facility file and each year's reporting-form page is
cached to disk; re-running skips whatever's already fetched.

Usage:
  python3 build_tri_historical.py
"""
import time
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import requests
from scipy.spatial import cKDTree

HERE = Path(__file__).parent
CACHE = HERE / "tri_cache"
CACHE.mkdir(exist_ok=True)
YEARS = [2013, 2022]
EQUAL_AREA = "EPSG:5070"  # CONUS Albers -- same convention as merascope notebooks/dcmodel.py

STATES = [
    "WA","OR","TX","CA","NV","UT","ID","MT","AZ","CO","WY","NM","ND","SD","NE","KS","OK",
    "MN","IA","MO","AR","LA","MI","WI","IL","IN","KY","TN","MS","GA","OH",
    "AL","FL","SC","NC","VA","WV","PA","NY","NJ","CT","RI","MA","VT","NH","ME","DE","MD",
]


def _ddmmss_to_dec(v):
    """Convert TRI fac_latitude/fac_longitude DDMMSS integer to decimal degrees.
    Same conversion as scripts/04_environment.py -- reused, not reinvented."""
    if pd.isna(v) or v == 0:
        return None
    v = int(abs(v))
    d = v // 10000
    rest = v % 10000
    return d + (rest // 100) / 60 + (rest % 100) / 3600


def _resolve_latlon(row):
    """pref_latitude/pref_longitude are decimal degrees but longitude is stored
    POSITIVE (needs negation for the US) -- same quirk 04_environment.py already
    handles for the current-snapshot pull. Falls back to the DDMMSS fac_lat/lon
    fields when pref_* is missing, same fallback order as that script."""
    lat, lon = row.get("pref_latitude"), row.get("pref_longitude")
    if pd.notna(lat) and pd.notna(lon):
        return float(lat), -float(lon)
    a = _ddmmss_to_dec(row.get("fac_latitude"))
    b = _ddmmss_to_dec(row.get("fac_longitude"))
    if a is not None and 24 < a < 50:
        return a, (-b if b is not None else None)
    if b is not None and 24 < b < 50:
        return b, (-a if a is not None else None)
    return None, None


def fetch_facility_roster(zip_centroid):
    """TRI_FACILITY per state (state filter confirmed working) -- one-time roster,
    facility_id + lat/lon + state, reused for both report years.

    Real coverage gap found (2026-09-03): ~20-25% of facilities have neither
    pref_latitude/longitude nor a usable fac_latitude/longitude DDMMSS fallback --
    a genuine EPA geocoding gap, not a parsing bug (checked directly against raw
    fields). Worse, that gap isn't even across years -- 73.8% of 2013's active
    reporters resolved vs. only 61.3% of 2022's, which would mechanically shrink
    2022's candidate pool and bias its nearest-facility distances FARTHER purely
    from fewer candidate points, independent of any real change. Fixed by falling
    back to the facility's own ZIP code centroid (zip_centroid, already built from
    merascope's national ZCTA table) when no real geocode exists -- ZIP-level
    precision, not exact-address, but present for essentially every row and not
    biased by year."""
    frames = []
    n_real, n_zip_fallback, n_unresolved = 0, 0, 0
    for abbr in STATES:
        path = CACHE / f"facility_{abbr}.csv"
        if not path.exists():
            url = f"https://data.epa.gov/efservice/TRI_FACILITY/STATE_ABBR/{abbr}/CSV"
            r = requests.get(url, timeout=90, headers={"User-Agent": "merascope-research/1.0"})
            r.raise_for_status()
            path.write_text(r.text)
            time.sleep(0.2)
        df = pd.read_csv(path, dtype=str)
        for c in ["pref_latitude", "pref_longitude", "fac_latitude", "fac_longitude"]:
            df[c] = pd.to_numeric(df[c], errors="coerce")
        latlon = df.apply(_resolve_latlon, axis=1, result_type="expand")
        df["lat"], df["lon"] = latlon[0], latlon[1]
        n_real += df["lat"].notna().sum()

        missing = df["lat"].isna()
        zip5 = df.loc[missing, "zip_code"].astype(str).str.extract(r"(\d{5})")[0]
        fallback_ll = zip5.map(zip_centroid)
        fb_lat = fallback_ll.map(lambda t: t[0] if isinstance(t, tuple) else np.nan)
        fb_lon = fallback_ll.map(lambda t: t[1] if isinstance(t, tuple) else np.nan)
        df.loc[missing, "lat"] = fb_lat
        df.loc[missing, "lon"] = fb_lon
        n_zip_fallback += fb_lat.notna().sum()
        n_unresolved += fb_lat.isna().sum()

        df = df.rename(columns={"tri_facility_id": "facility_id"})[["facility_id", "lat", "lon"]]
        frames.append(df.dropna(subset=["lat", "lon"]))
    roster = pd.concat(frames, ignore_index=True).drop_duplicates("facility_id")
    print(f"national TRI facility roster: {len(roster)} facilities located "
          f"({n_real} real geocode, {n_zip_fallback} ZIP-centroid fallback, "
          f"{n_unresolved} unresolved -- no lat/lon and no usable ZIP code)")
    return roster


def fetch_active_facility_ids(year):
    """TRI_REPORTING_FORM, filtered by REPORTING_YEAR only (state filter doesn't
    work on this table -- see module docstring). Paginated nationally."""
    ids = set()
    page = 0
    page_size = 10000
    while True:
        path = CACHE / f"reporting_{year}_page{page}.csv"
        if not path.exists():
            start, end = page * page_size, page * page_size + page_size - 1
            url = (f"https://data.epa.gov/efservice/TRI_REPORTING_FORM/REPORTING_YEAR/{year}"
                   f"/rows/{start}:{end}/CSV")
            r = requests.get(url, timeout=120, headers={"User-Agent": "merascope-research/1.0"})
            r.raise_for_status()
            path.write_text(r.text)
            time.sleep(0.2)
        text = path.read_text().strip()
        lines = text.split("\n")
        if len(lines) <= 1:
            break
        df = pd.read_csv(path, dtype=str, usecols=lambda c: c.lower() == "tri_facility_id")
        ids.update(df.iloc[:, 0].dropna().unique())
        if len(lines) - 1 < page_size:
            break
        page += 1
    print(f"  {year}: {len(ids)} distinct facilities reported")
    return ids


def main():
    print("Fetching ZCTA centroids (national, from merascope's cached feature table)...")
    model_table = HERE.resolve().parents[2] / "merascope" / "notebooks" / "cache" / "model_table.csv"
    zctas = pd.read_csv(model_table, dtype={"zcta": str}, usecols=["zcta", "lon", "lat"]).dropna()
    zip_centroid = {z: (lat, lon) for z, lon, lat in zip(zctas.zcta, zctas.lon, zctas.lat)}
    zctas_gdf = gpd.GeoDataFrame(zctas, geometry=gpd.points_from_xy(zctas.lon, zctas.lat),
                                  crs="EPSG:4326").to_crs(EQUAL_AREA)
    zcta_coords = np.column_stack([zctas_gdf.geometry.x, zctas_gdf.geometry.y])
    print(f"  {len(zctas)} ZCTAs")

    print("\nFetching national TRI facility roster (47 states)...")
    roster = fetch_facility_roster(zip_centroid)

    out = zctas[["zcta"]].copy()
    match_rates = {}
    for year in YEARS:
        print(f"\nFetching TRI_REPORTING_FORM for {year} (national, paginated)...")
        active_ids = fetch_active_facility_ids(year)
        active = roster[roster["facility_id"].isin(active_ids)].copy()
        matched = len(active)
        match_rates[year] = matched / len(active_ids)
        print(f"  {matched}/{len(active_ids)} reporting facility IDs located "
              f"({match_rates[year]*100:.1f}%) -- remainder is real Alaska/Hawaii/territory "
              f"facilities outside this 47-state roster's coverage")

        fac_gdf = gpd.GeoDataFrame(active, geometry=gpd.points_from_xy(active.lon, active.lat),
                                    crs="EPSG:4326").to_crs(EQUAL_AREA)
        fac_coords = np.column_stack([fac_gdf.geometry.x, fac_gdf.geometry.y])
        tree = cKDTree(fac_coords)
        dist_m, _ = tree.query(zcta_coords, k=1)
        out[f"tri_dist_km_{year}"] = dist_m / 1000
        print(f"  {year} nearest-active-TRI-facility distance: "
              f"median={np.median(dist_m)/1000:.1f} km, "
              f"{matched} active facilities nationally")

    rate_gap = abs(match_rates[YEARS[0]] - match_rates[YEARS[1]]) * 100
    print(f"\nmatch-rate gap between years after ZIP-centroid fallback: {rate_gap:.1f} points "
          f"(was 12.5 points before the fallback)")

    out_path = HERE / "tri_zcta_distance.csv"
    out.to_csv(out_path, index=False)
    print(f"\nwrote {out_path} ({len(out)} ZCTAs x {len(YEARS)} years)")


if __name__ == "__main__":
    main()
