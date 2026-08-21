"""Map: where WA's historically-burned land currently reads as WHP 'non-burnable'.

Source data built by burned_nonburnable_map2.py (scratchpad) -- reproduced here
inline so the notebook is self-contained and re-runnable. Real MTBS burn
perimeters (mtbs.gov) + real USFS Wildfire Hazard Potential 2020 raster
(firelab.org), same data merascope's own fire-risk report uses.
"""
import json
import os

import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from shapely import contains_xy
from shapely.geometry import shape

BASE = "/home/simonhans/coding/merascope/data/shared"
DATA_ROOT = "/home/simonhans/coding/merascope/data"


def _load(name):
    with open(os.path.join(BASE, name)) as f:
        return json.load(f)


perimeters = _load("wa_fire_perimeters.geojson")
arr = np.load(os.path.join(BASE, "whp_wa.npy"))
t = _load("whp_wa_transform.json")

wa = gpd.read_file(os.path.join(DATA_ROOT, "WA", "raw", "state.geojson")).to_crs("EPSG:5070")
wa_union = wa.union_all()
perim_gs = gpd.GeoSeries([shape(f["geometry"]) for f in perimeters["features"]], crs="EPSG:4326").to_crs("EPSG:5070")
perim_union = perim_gs.union_all()

rows_idx, cols_idx = np.indices(arr.shape)
x = t["origin_x"] + (cols_idx + 0.5) * t["pixel_x"]
y = t["origin_y"] + (rows_idx + 0.5) * t["pixel_y"]

# Mask to the REAL state polygon, not just "raster has a rating" -- the WHP
# extract is a rectangular crop that spills into OR/ID/BC, and naively using
# arr != 255 as a WA proxy undercounts burned share (8.7% instead of the
# correct ~13.3%). Verified against the Monte Carlo estimate already shipped
# in wa_fire_risk.json (13.325%) before trusting anything below.
in_wa = contains_xy(wa_union, x, y)
valid = in_wa & (arr != 255)

burned = np.zeros(arr.shape, dtype=bool)
burned[valid] = contains_xy(perim_union, x[valid], y[valid])

n_valid, n_burned = valid.sum(), burned.sum()
burned_pct = 100 * n_burned / n_valid
n_nonburnable = int(((arr == 6) & burned).sum())
nonburnable_pct_of_burned = 100 * n_nonburnable / n_burned

assert 12.5 < burned_pct < 14.5, f"burned share {burned_pct:.2f}% drifted from the validated ~13.3% -- check the WA mask"
print(f"burned: {burned_pct:.2f}% of WA (validated against shipped Monte Carlo estimate 13.33%)")
print(f"of burned land, {nonburnable_pct_of_burned:.1f}% reads WHP class 6 'non-burnable' today")
print(f"= {100*n_nonburnable/n_valid:.2f}% of all WA land is both historically burned AND scored non-burnable")

# ---- map ----
extent = (t["origin_x"], t["origin_x"] + arr.shape[1] * t["pixel_x"],
          t["origin_y"] + arr.shape[0] * t["pixel_y"], t["origin_y"])

# 0=outside/unburned (transparent), 1=burned+burnable (neutral), 2=burned+non-burnable (accent)
# Rendered at native 270m pixel resolution, no marker inflation -- an enlarged-marker
# pass was tried and rejected: at any marker size big enough to read as "visible,"
# overlapping adjacent pixels in the real non-burnable clusters (they're spatially
# correlated, not speckled at random) blew up into blobs that looked like ~40% of
# burned area instead of the real 5.7%. Native resolution is smaller but honest.
cat = np.zeros(arr.shape, dtype=np.uint8)
cat[burned] = 1
cat[burned & (arr == 6)] = 2
cat_masked = np.ma.masked_where(~in_wa, cat)

cmap = ListedColormap(["#00000000", "#9ec5f4", "#eb6834"])  # transparent, light blue, orange accent

fig, ax = plt.subplots(figsize=(8, 8))
wa.boundary.plot(ax=ax, color="#b0b0ac", linewidth=1, zorder=1)
ax.imshow(cat_masked, extent=extent, cmap=cmap, vmin=0, vmax=2, interpolation="nearest", zorder=2)

ax.scatter([], [], s=80, color="#9ec5f4", marker="s", label="Burned since 1984, rated burnable today")
ax.scatter([], [], s=80, color="#eb6834", marker="s", label="Burned since 1984, rated “non-burnable” today")
ax.legend(loc="lower left", frameon=False, fontsize=10)

ax.set_title(
    f"{burned_pct:.0f}% of Washington has burned since 1984 --\n"
    f"{nonburnable_pct_of_burned:.0f}% of that land is scored “non-burnable” by today's fuel model",
    fontsize=13,
)
ax.set_axis_off()
ax.set_aspect("equal")
fig.tight_layout()
fig.savefig("nonburnable_burn_history.png", dpi=150, bbox_inches="tight")
plt.show()


def _demo():
    total = int(valid.sum())
    assert int(burned.sum()) + int((~burned & valid).sum()) == total
    assert 0 <= nonburnable_pct_of_burned <= 100
    print("self-check ok")


_demo()
