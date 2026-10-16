Visualizing the unseen (until I get hired): How does Environmental Justice vary among zip codes 

I wondered: how does the Environmental Justice index vary between zip codes that host a data center and ones that don't?

Turns out ZIPs hosting a data center score worse on EJ burden than ones that don't, across the board, even controlling for population density.

The numbers: across 33,252 US zip codes in 48 states, the 1,196 hosting a confirmed data center score 0.18 points worse on a 0-to-1 EJ index (built the way EPA's own EJScreen does: demographic vulnerability times pollution and hazard burden) than the rest. Data centers cluster near cities, same as people do, so that was my first suspicion; density explains 61% of the gap once I control for it directly, but not all of it, and the remainder survives a permutation test. Split every zip into a density quintile against others in its own state, and hosting zips score worse in every single one, least dense to most.

Found a real bug on the way in, too. The "nationally normalized" version of these scores turned out to be a stale copy of the state-level ones; worked around it by comparing each zip only to others in its own state, which turned out to be the better design anyway.

This, however, is merely a snapshot that shows lower EJ scores for ZIPs with a data center. There may be confounding factors, and there may be a treatment or selection effect underneath it. More to come.

Notebook: civil/dc_ej_hosting_gap.ipynb

%%%%% NOTES %%%%%
- Image: dc_ej_hosting_gap.png (raw bar comparison + density-quintile-matched grouped bars).
- Data: merascope notebooks/cache/model_table.csv (33,252 ZCTAs) + data/datacenters/zcta_labels.csv (has_dc = n_built > 0, real multi-source corroborated label).
- ej_score = merascope's live EPA EJScreen-style formula (demog_index x env_burden), NOT the old demographics-only placeholder the August EJ sub-series had to work around.
- Full stats: raw gap -0.177 (Mann-Whitney p=7e-172, n=33252); adjusted regression coefficient -0.069 (t=-12.2, permutation p=0.005), 61% shrink from raw; all 5 within-state density quintiles negative, range -0.068 to -0.102.
- Real pipeline catch: ej_score_nat / pop_exposure_score_nat are 100% identical to the state-relative columns -- normalize_zcta_national.py is stale relative to the last rescore_ej.py --all run. Flagged as a merascope backlog TODO, not fixed in this piece.
- AI-usage framing: same as the canopy_semantic_layer piece -- Simon specified the question and the control; Claude ran the pipeline, caught the stale-_nat bug, and built the checks/figure.
