Visualizing the unseen (until I get hired): How does Environmental Justice vary among zip codes 

I wondered: How does the Environmental Justice index vary between zip codes hosting or not hosting a data center?

Turns out that ZIPs hosting data centers have a worse EJ burden than zips that don't, across the board controlling for population.

This, however, is merely a snapshot that shows lower EJ score for ZIPs with a data center. There may be confounding factors, and there may be a treatment or selection happening. More to come.









**Data centers, environmental justice, and the confound I checked first [until I get hired]**

Question: does the ZIP code hosting a data center score worse on environmental-justice burden than one that doesn't? Obvious objection before I even asked it: data centers and people both cluster near cities, so of course a "data center ZIP" looks different from a random ZIP -- it's probably just a density story wearing a different costume.

So I controlled for it. Across 33,252 U.S. ZIP codes (48 states), the 1,196 that host a confirmed, corroborated built data center score 0.177 points worse on a real EPA EJScreen-style EJ index (demographic vulnerability x pollution/hazard burden, 0-1 scale) than ones that don't -- and yes, those ZIPs really are denser on average, exactly as I expected going in.

Controlling for it two independent ways: an adjusted regression shrinks the gap 61% once population density is in the model -- density really is most of the story -- but the remainder survives a 200-shuffle permutation test (p=0.005). And splitting every ZIP into a population-density quintile relative to its own state, then comparing only within the same quintile: data-center ZIPs score worse in every single one of the five bins, from the least dense to the most.

Not a claim about why -- I didn't test mechanism, just whether the gap is real. Siting economics (land, power, grid access) plausibly pulls data centers toward the same industrial/urban-adjacent land that already carries more burden, independent of any decision about data centers specifically. But "it's just density" doesn't survive the check.

Built on merascope.com's real per-ZIP indicator pipeline, not an invented composite -- and it caught a real pipeline bug on the way in: the "nationally normalized" versions of these two scores turned out to be stale byte-for-byte copies of the state-relative ones (a re-normalization pass hadn't been rerun since the underlying formula last changed). Worked around by comparing each ZIP to others in its own state instead, which turned out to be the more defensible design anyway.

Notebook: civil/dc_ej_hosting_gap.ipynb

%%%%% NOTES %%%%%
- Image: dc_ej_hosting_gap.png (raw bar comparison + density-quintile-matched grouped bars).
- Data: merascope notebooks/cache/model_table.csv (33,252 ZCTAs) + data/datacenters/zcta_labels.csv (has_dc = n_built > 0, real multi-source corroborated label).
- ej_score = merascope's live EPA EJScreen-style formula (demog_index x env_burden), NOT the old demographics-only placeholder the August EJ sub-series had to work around.
- Full stats: raw gap -0.177 (Mann-Whitney p=7e-172, n=33252); adjusted regression coefficient -0.069 (t=-12.2, permutation p=0.005), 61% shrink from raw; all 5 within-state density quintiles negative, range -0.068 to -0.102.
- Real pipeline catch: ej_score_nat / pop_exposure_score_nat are 100% identical to the state-relative columns -- normalize_zcta_national.py is stale relative to the last rescore_ej.py --all run. Flagged as a merascope backlog TODO, not fixed in this piece.
- AI-usage framing: same as the canopy_semantic_layer piece -- Simon specified the question and the control; Claude ran the pipeline, caught the stale-_nat bug, and built the checks/figure.
