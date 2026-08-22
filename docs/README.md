# drawing

Generative art experiments — tie-dye patterns, trigonometric drawings, and interactive canvas sketching.

## What it does

A collection of visual experiments using matplotlib and numpy. Includes parametric trig art, procedural tie-dye color fields, an event-driven listener for interactive drawing input, a synth-audio-driven visualizer (`riff_visualizer.ipynb`), score-driven (not audio-driven) visualizations of five classical passages: Beethoven's Ode to Joy as a landscape (`ode_to_joy_landscape.ipynb`), the 5th Symphony's opening as a lightning storm (`fate_motif_storm.ipynb`), Rossini's William Tell finale as an accelerating gallop (`william_tell_gallop.ipynb`), Tchaikovsky's 1812 Overture finale as fireworks and bells over Moscow (`overture_1812_finale.ipynb`), and Ravel's Bolero as a spiral of 18 closed loops, one per real orchestration statement (`bolero_spiral.ipynb`) — decorative/A statements bulge outward with small ornamented ripples, arabesque/B statements dip inward as one smooth sweep (rendered thinner and dimmer so A carries the readable repetition), both sourced from real musicological analysis (Bhogal 2020) rather than invented, with sharpened star markers riding each loop for the constant snare ostinato — and five civic-data companion pieces feeding the campaign's "A-story": `transit_gap_visible.ipynb` (snotrac's transit-vulnerability-vs-accessibility gap, Snohomish block groups), `envburden_snohomish.ipynb` (WA DOH Environmental Health Disparities data, 4 panels: individual hazard layers, DOH's composite, a per-tract dominant-hazard map, and a population-density reference), `transit_pollution_overlap.ipynb` (the two prior pieces' composites cross-checked at tract level — a real but weak trade-off, not the compounding-burden hypothesis it set out to test), `ballot_access_snohomish.ipynb` (Nov 2024 general, 858 precincts: raw ballots-cast vs. distance to nearest of 36 drop boxes shows nothing, r=-0.05; a real turnout rate at the only granularity one exists — 20 cities, via a Wayback-Machine-recovered county report — shows a moderate but statistically inconclusive relationship, r=-0.38, p=0.10), and `ballot_access_statewide.ipynb` (same question at all 39 WA counties with official turnout, no aggregation needed; a first-pass geometric county centroid was badly broken — 40-48 mi off for Jefferson/Whatcom/King — fixed with a population-weighted centroid from WA's 2024 census-block-group population estimates, corrected result r=-0.18, p=0.26), and `dc_ej_water_tradeoff.ipynb` (merascope's own `ej_score`/`water_score` pipeline indicators, matched by point-in-polygon to every confirmed active WA data-center site's real ZCTA — the water-scarce Quincy desert campuses read as *less* EJ-burdened than the well-watered Tukwila cluster, the reverse of the going-in assumption; distinct from the merascope fire-risk finding held back for a possible press tip, see `CAMPAIGN.md`). Also `heat_equation_flow.ipynb` (a real FTCS heat-equation solve, not decorative — different shapes diffusing under curvature, a moving source leaving a comet trail, three boundary conditions compared) and `vineyard_canopy_diurnal.ipynb` (a `GrapeExpectations`/DTS science companion, not a campaign piece — models a real vine's diurnal thermal cycle with per-material heat capacity over 2 spun-up, midnight-anchored days, showing the canopy-microclimate lag a real DTS fiber deployment would be there to catch; **re-run pending as of 2026-08-15, see CONTEXT.md**). See `CAMPAIGN.md` for the "Visualizing the Unseen" LinkedIn posting series these feed into, and its `*_post.md` files for the shipped captions.

Two one-off pieces outside the campaign structure, built 2026-08-17 from `dada_science/library_recommender/library.db` (Heiki's real reading engagement data, not synthetic): `heiki_reading_life.ipynb` (concentric growth-ring/vinyl-groove art — radius = times read, groove = reread demands, color = Simon's rating, a broken ring = survived a false start) and `heiki_genre_explore.ipynb` (genre-tag cleanup + a 5-series radar chart, `heiki_genre_radar.png`, comparing reread rate/follow-through/reads-per-book/rating across cleaned genre buckets). Shipped caption for both images combined: `heiki_literature_review_post.md`. See `CONTEXT.md` for the build notes, including a real scraper bug these surfaced in `library_recommender`.

## Tech

Python — `matplotlib`, `numpy`, `scipy.stats` (Pearson r + p-values in the ballot-access pieces), Jupyter notebooks

## Data

`data/` holds sourced inputs for the civic-data pieces — election results CSVs, GeoJSON boundaries, drop-box locations/coordinates, and population estimates. Not synthetic; every file traces to a public source cited in the corresponding notebook's final markdown cell and `*_post.md` caption.

## Run

Open any notebook in Jupyter:

```bash
jupyter notebook TieDyes.ipynb
jupyter notebook trig_art.ipynb
```

Or run the interactive listener:

```bash
python listener.py
```
