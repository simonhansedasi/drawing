## Simon's draft

Visualizing the unseen (until I get hired): data centers are accelerating into rural ZIP codes. But why?

I track a public 4-source dataset of announced or built US data centers. Since 2024 the rural share of new proposals has grown by roughly 5x, compared to the urban volume growing approximately 2.5x. Something is pulling data center development hard towards rural land.

## Claude's draft



Visualizing the unseen (until I get hired): data centers are accelerating into rural ZIP codes. But why?

I track a public 4-source dataset of every announced or built US data center. Since 2024, the rural share of new proposals has climbed from 53% to 69%, and rural proposal volume has grown roughly 5x -- faster than urban's 2.5x growth over the same span. Something is pulling development toward rural land, hard.

So I checked every suitability indicator Merascope's own siting model tracks, one at a time, instead of assuming an answer. That model ranks every ZIP code 1-10 on how much it resembles an existing data-center site, trained only on real infrastructure and geography -- grid proximity, terrain, contamination sites, community burden, population density -- and never on the ZIP's own data-center history, so rural and urban ZIPs land on the exact same scale.

Grid access: flat over time for rural proposals (p=0.69) -- not degrading as volume grows. Overall suitability tier: also flat (p=0.55). EJ/community burden: flat too (p=0.51), not getting worse as volume grows. Even buildable-land indicators -- terrain slope, flat land fraction, parcel size -- are flat (p=0.51-0.94). Nothing is trending. Whatever's driving this expansion, it isn't a shift on any axis this 22-indicator model measures.

Then I checked whether developers were working from a small, optimized shortlist of "known good" rural sites. They're not: 283 distinct rural ZIP codes across 349 proposals, and 86-100% of each period's new proposals still land somewhere that's never had a proposal before -- even at 5x the volume. That's not a tightening search, that's an expanding frontier.

One real exception, worth naming honestly: within rural proposals specifically, sites with better grid access do track modestly worse EJ scores -- a real trade-off that survives controlling for population density. The same-looking pattern in urban proposals didn't survive that check; it turned out to be entirely a density artifact. So there is one genuine, if modest, trade-off buried in here. It just isn't the driver of the shift itself.

Put together, the only explanation left standing is the simplest one: land availability. Grid-connected rural land is getting claimed wherever it's found, at growing volume, not according to any tightening or evolving suitability standard. So: where are the standards? Right now the honest answer looks like "connected to the grid, and not fully urban" -- and not much else.

%%%%%
NOTES
%%%%%

Data: Merascope's own public risk model and 22-indicator siting pipeline (merascope.com/#/risk). Proposal-timing data from Compute Atlas's raw dated status-history records (CC BY 4.0), spatially joined to real ZCTA polygons. All trend tests are Spearman correlations on the full dated dataset (566 records, 2021-2026), not eyeballed. The EJ-vs-grid-access trade-off is checked with a partial correlation controlling for population density, not just a raw correlation.

Images: dc_rural_urban_volume.png (rural proposal volume growing ~5x since pre-2024, faster than urban's 2.5x) + dc_rural_urban_ej_gridaccess_profile.png (the EJ-vs-grid-access trade-off, raw vs. density-controlled -- only rural survives the check) + dc_rural_zip_frontier.png (the expanding-frontier finding: 86-100% of each period's rural proposals land in a brand-new ZIP).

### AI usage:
Built with Claude Code, Simon-Hans Edasi directing. This piece went through five real revisions, each one Simon pushing past a plausible-sounding answer to check what was actually driving the shift. A first pass found a "trade-off" between grid access and EJ score for both rural and urban proposals -- Simon asked directly whether that could just be the population-density confound showing up twice. It was, for urban (the correlation dropped from rho=-0.18 to rho=-0.05 and lost significance once controlled), but not for rural (rho=-0.13, essentially unchanged). Then Simon pushed further: if none of the suitability indicators are moving, is this even about suitability, or just available land? That's the actual headline finding -- checked directly (buildable-land indicators flat, ZIP pool expanding not shrinking), not assumed from the absence of other explanations.

Notebooks: civil/dc_rural_urban_volume.ipynb (primary, all 5 checks), civil/dc_proposal_rural_shift.ipynb, civil/dc_tier_composition.ipynb, civil/dc_rural_tier_link.ipynb, civil/dc_risk_divide.ipynb
