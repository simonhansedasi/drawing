Day 8 of visualizing the unseen [until I get hired]. Election season question: does living far from a ballot drop box actually mean fewer people vote? The answer depends on which number you trust.

Snohomish County, WA's last completed general (Nov 2024) — 858 precincts, 36 official drop boxes, real coordinates pulled from the county's own map. At the precinct level, distance to nearest drop box (20 feet to 12.6 miles) has essentially no relationship to raw ballots cast: r = -0.05.

But raw ballot count mixes population size with actual engagement. Step up to the only place a real turnout *rate* exists — the county's own registered-voter counts by city — and a moderate relationship shows up: r = -0.38 across 20 cities and towns. It doesn't clear statistical significance at that sample size (p = 0.10), so this is "worth watching," not "proven." But it's the opposite of what the fine-grained number said, and the fine-grained number was the one hiding a confound.

Washington votes entirely by mail with prepaid return postage, so a drop box is a convenience, not the only way back — this was never going to be a disenfranchisement story. What it turned into instead: a small case study in how the metric you pick can flip the answer, even on the same underlying question.

Precinct boundaries, election results, and city-level registration figures are hosted by three different parts of the county/state election system, with three different ID schemes. Reconciling them was most of this piece.

%%%%%
NOTES
%%%%%

A-story companion to Day 2 (transit gap) and Day 6 (transit/pollution overlap) — same county, same "layer two real datasets and see what's actually there" pattern.

Data: results.vote.wa.gov (Nov 5, 2024 general, precinct-level export), Snohomish County GIS "Voter Precinct Districts" layer, county's public drop-box map (KML export, exact coordinates), Snohomish County Elections' own "2024 Counts for 2025 Validation" report (city-level registered voters + ballots cast, recovered via a Wayback Machine snapshot since the county overwrites that report's URL in place each year). City-level aggregation cross-checked against the county's own published totals before trusting it — every city landed within 1-3%.

### AI usage ###:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude sourced the data (including recovering a since-overwritten county report via the Wayback Machine), built the precinct-name join across mismatched ID schemes, ran both the precinct-level and city-level analyses, and caught its own first-draft mistake — an early version of this caption assumed both granularities would agree; they didn't, and the draft got corrected before posting.
