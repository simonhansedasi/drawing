Day 10 of visualizing the unseen [until I get hired]. Went statewide with the ballot drop box question — and building it exposed a bug that mattered more than the extra scale did.

All 39 Washington counties, Nov 2024 general: real registered-voter turnout (65.0%-87.7%, official state numbers, no aggregation needed this time) against distance from each county's population center to its nearest of 573 drop boxes. First pass used a geometric centroid — the middle of the county's boundary, same technique that worked fine at precinct scale. At county scale it's a different story: Jefferson and Whatcom counties both stretch from a populated coast into empty mountains, and that "middle" landed 45-48 miles from where anyone actually lives. The result: r = 0.03, indistinguishable from nothing.

Fixed it with Washington's own 2024 population estimates by census block group, weighted-averaged per county instead of a raw geometric mean. Same drop boxes, same turnout numbers, only the reference point changed — and the correlation moved to r = -0.18. Still doesn't clear statistical significance at n=39 (p = 0.26), so this isn't a confirmed finding. But it's a real, directionally consistent signal that the broken version of the metric couldn't have found, because the broken version wasn't measuring what it claimed to measure.

Three passes at this question now, three different granularities: no relationship in raw ballot counts at the precinct level, a suggestive-but-underpowered relationship in one county's cities, a weak-but-corrected relationship statewide. The honest read across all three: probably something small, not proven. Reporting the geometric-centroid number alongside the fixed one on purpose — it's not a rough draft to hide, it's the reason to trust the fixed number.

%%%%%
NOTES
%%%%%

Third and final piece in this sub-thread, after Day 8 (Snohomish precinct + city level).

Data: results.vote.wa.gov/results/20241105/Turnout.html (official county turnout, all 39 counties), WA Secretary of State's statewide drop box list (573 locations, current cycle — used as a stand-in for Nov 2024, disclosed in the notebook), WA DNR county boundaries, WA OFM 2024 population estimates by census block group (5,311 statewide) for the population-weighted centroid fix.

### AI usage ###:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude sourced all four datasets, built the county join (clean this time — no name-mismatch archaeology needed), computed an initial geometric-centroid version, caught that it was placing several counties' reference points in uninhabited wilderness, and rebuilt the analysis on a population-weighted centroid before reporting a result.
