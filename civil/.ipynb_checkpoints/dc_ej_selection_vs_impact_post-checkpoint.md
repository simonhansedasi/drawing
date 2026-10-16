**Selection or impact? Testing which one it actually is [until I get hired]**

Follow-up to the last piece: data-center ZIP codes score worse on environmental-justice burden than non-hosting ZIPs, and that survives controlling for population density. Obvious next question -- does that mean data centers are *driving down* EJ after they arrive, or are they *favoring* areas that were already worse off? A snapshot can't tell those apart. So I went looking for a way to add time.

Neither data-center dataset in the pipeline has a usable opening date (checked before building anything), so a clean before/after study of each individual site isn't possible. But the demographic half of the EJ index (poverty + minority rate) comes from Census ACS data, which is queryable at older vintages. Pulled the 2013 5-year estimates (~2009-2013, a decade before the recent hyperscale boom) for the same ~32,000 ZIP codes and compared: was the gap already there, or did it open up more recently?

87.2% of today's gap already existed in 2013. Hosting ZIP codes were already meaningfully more vulnerable a decade ago; today's gap is only modestly larger. That points toward selection, not impact, as the dominant explanation. There is a small residual -- hosting ZIPs drifted about 0.007 points more vulnerable than density- and baseline-matched non-hosting ZIPs over those 9 years, real against a permutation test but only ~10% of today's total gap.

Not a final answer -- no site has a known opening date, so this can't fully separate "this ZIP was already like this before any data center" from "the ZIP's oldest data center already changed things before 2013 too." And only the demographic half of EJ has a historical read; the pollution/hazard half is a current snapshot only. But the honest read of what's actually testable: mostly selection, with a real but small residual that could be impact, could be something else entirely.

Notebook: civil/dc_ej_selection_vs_impact.ipynb (direct follow-up to civil/dc_ej_hosting_gap.ipynb)

%%%%% NOTES %%%%%
- Image: dc_ej_selection_vs_impact.png (2013-to-2022 trend lines by hosting status; gap decomposed into "already there" vs "opened up since").
- Data: merascope's cached current (2022 ACS5) demog_index per state + a fresh single national 2013 ACS5 pull (cached to civil/data/acs_zcta_2013_raw.json), same has_dc label as the prior piece.
- Full stats: 2013 gap +0.0601 (p=4.1e-86), 2022 gap +0.0689 (p=1.3e-108), 87.2% already present in 2013. Delta regression: has_dc coefficient +0.0070 (t=3.11), permutation p=0.005, controlling for density_axis and 2013 baseline (mean reversion).
- Real bug caught mid-build: first permutation-test pass indexed the wrong regression coefficient (intercept instead of the shuffled has_dc coefficient) -- null distribution was suspiciously tight (std=0.0001) around a nonzero mean, which is what caught it. Fixed, rerun, null now centers near zero as expected.
- AI-usage framing: Simon asked the selection-vs-impact question directly and chose the historical-ACS approach from three options after Claude explained the data-gap tradeoffs (no site dates available at all). Claude ran the pipeline, caught its own permutation-test bug, built the checks/figure.
