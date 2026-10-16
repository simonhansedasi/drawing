The richest ZIP code broke the model. So did the poorest. [until I get hired]

Built a real environmental-justice index on merascope's Washington data -- the actual EPA formula (environmental hazard exposure x demographic vulnerability), not a stand-in. Across 605 ZIP-code areas, the state's 21 physical/infrastructure siting factors (grid access, water, seismic risk, flood risk, and so on) explain 62% of the variance in that index -- real, confirmed against 200 randomized reruns so it's not a fitting artifact (p = 0.005).

The single strongest predictor: distance to the nearest internet carrier hotel. That's suspicious enough to check rather than report. It turns out fiber access isn't really the story -- it's a stand-in for one thing, how urban or industrial a place is, which happens to predict both pollution exposure and demographic vulnerability at the same time. Dropped it from the model entirely to test that: the score barely moves (62% -> 58%), because population density immediately steps in and does almost the same job. One axis, not five independent causes.

The two places the model gets most wrong are more interesting than the 62% headline number. Inchelium, on the Colville Reservation in rural Ferry County, has real elevated burden that an urban-density proxy structurally can't see -- the model predicts almost none. Madison Park, one of Seattle's wealthiest neighborhoods, is dense enough to read as burdened to the same proxy -- and isn't. A poor place invisible to the model, a rich place wrongly flagged by it. That's what "explained by density" actually breaks on.

Notebook: dc_ej_predictors.ipynb

%%%%%
NOTES
%%%%%

Data: merascope's own scored WA ZCTA pipeline (605 ZIP-code areas). Target is a real EJ index, not a stand-in: `demog_index` (poverty + minority rate, tract-level ACS) x `env_burden` (1 - mean of contamination/superfund/RCRA/air-quality proximity scores) -- the same multiplicative structure as EPA's own EJScreen. An earlier build of this piece used merascope's `ej_score` column and called it "environmental justice"; it turned out to be pure demographic composition with zero pollution/hazard data in it (merascope's own internal grading code actually labels that pillar "Community Burden," not EJ) -- caught and fixed before anything went out.

Leakage handled by construction: the four hazard scores are literally inside the target's formula, so they're excluded from the feature set by name, not by a correlation-threshold check (their linear correlation with the target tops out around 0.58, well under a naive 0.9 cutoff, even though the dependency is exact).

Ablation, not just an importance ranking: fiber_score alone gets R²=0.385; all 17 features together get 0.616; dropping fiber_score entirely only costs 0.036 (down to 0.580), and pop_exposure_score's importance jumps from minor to 0.47 to cover the gap. Residuals get slightly worse without fiber_score, not better, so it isn't causing the model's biggest misses either -- the two named ZIP codes are.

Images: dc_ej_ml_maps.png (actual EJ index / model's prediction / residual, three WA maps, Inchelium and Madison Park called out on the residual map) + dc_ej_ml_importance.png (which of the 17 honest factors matter most, two methods compared).

### AI usage ###:
Built with Claude Code. Ideation, framing, and every real judgment call were mine, Simon-Hans Edasi; Claude wrote the code and ran the numbers. Real catches worth naming: I asked why merascope's own `ej_score` was just poverty+minority rate when EJ is supposed to mean environmental justice -- Claude checked the formula, confirmed there was no environmental data in it at all, and rebuilt both this piece and its companion on a real EJScreen-style index instead of just relabeling the old one. When the rebuilt model's top feature came back as `fiber_score`, I pushed back that it looked like it might be doing all the work on its own -- Claude ran a real ablation (drop the feature, refit, compare) instead of defending the importance ranking, found it wasn't (residuals got worse without it), and surfaced what was actually driving the number instead.
