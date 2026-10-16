## Simon's draft

Visualizing the unseen (until I get hired): data centers are accelerating into rural ZIP codes. But why?

I track a public 4-source dataset of announced or built US data centers. Since 2024 the rural share of new proposals has grown by roughly 5x, compared to the urban volume growing approximately 2.5x. Something is pulling data center development hard towards rural land.

## Claude's draft (rebuilt 2026-08-31 on USDA's real rural/urban definition)



Visualizing the unseen (until I get hired): data centers are moving into rural ZIP codes faster than urban ones. But why?

I track a public 4-source dataset of every announced or built US data center. Since 2024, rural proposal volume has grown roughly 5.4x -- outpacing urban's own 3.4x growth over the same span. Rural is still the minority of the pipeline (169 of 552 dated proposals since 2021), but it's catching up. Something is pulling development toward rural land harder than toward urban land.

So I checked every suitability indicator Merascope's own siting model tracks, one at a time, instead of assuming an answer. That model is a classifier trained to tell hosting ZIPs apart from non-hosting ones, using only real infrastructure and geography -- grid proximity, terrain, contamination sites, community burden, population density -- never a ZIP's own data-center history. Every ZIP then gets ranked 1-10 by how close it sits to the "hosts a data center" side of that learned boundary, so rural and urban ZIPs are scored on the exact same scale. And "rural" itself is USDA's own federal RUCA classification, not an internal proxy -- more on that below.

Grid access: flat over time for rural proposals (p=0.63). Overall suitability tier: also flat (p=0.37). EJ/community burden: flat too (p=0.40). Even buildable-land indicators -- terrain slope, flat land fraction, parcel size -- are flat (p=0.37-0.65). Nothing is trending. Whatever's pulling this expansion, it isn't a shift on any axis this 22-indicator model measures.

Then I checked whether developers were working from a small, optimized shortlist of "known good" rural sites. They're not: 147 distinct rural ZIP codes across 169 proposals, and 89-100% of each period's new proposals still land somewhere that's never had a proposal before -- even at 5.4x the volume. That's not a tightening search, that's an expanding frontier.

One real trade-off, worth naming honestly -- and it's not where I first found it. Sites with better grid access do track worse EJ scores, and that survives controlling for population density -- but it's the **urban** proposals where it holds (p=0.02), not the rural ones (p=0.07, doesn't clear significance once density is controlled). That's the opposite of what an earlier pass of this analysis found, using a cruder rural/urban proxy. Substantively it makes sense: infrastructure siting landing disproportionately in lower-income, higher-minority urban neighborhoods is a well-documented pattern. It just isn't the story about rural land.

Put together, the only explanation left standing for the rural pull specifically is the simplest one: land availability. Grid-connected rural land is getting claimed wherever it's found, at growing volume, not according to any tightening or evolving suitability standard. So: where are the standards? Right now the honest answer looks like "connected to the grid, and not fully urban" -- and not much else. The more interesting trade-off in this data turned out to be inside cities, not between them and the countryside.

%%%%%
NOTES
%%%%%

Data: Merascope's own public risk model and 22-indicator siting pipeline (merascope.com/#/risk). Proposal-timing data from Compute Atlas's raw dated status-history records (CC BY 4.0), spatially joined to real ZCTA polygons. Rural/urban classification is USDA ERS's 2020 ZIP-code RUCA codes (RUCA 1-3 = metro, 4-10 = non-metro) -- the actual federal standard, not an internal density proxy. All trend tests are Spearman correlations on the full dated dataset (566 records, 2021-2026), not eyeballed. The EJ-vs-grid-access trade-off is checked with a partial correlation controlling for population density, not just a raw correlation.

Images: dc_rural_urban_volume.png (rural proposal volume growing ~5.4x since pre-2024, faster than urban's 3.4x) + dc_rural_urban_ej_gridaccess_profile.png (the EJ-vs-grid-access trade-off, raw vs. density-controlled -- only urban survives the check) + dc_rural_zip_frontier.png (the expanding-frontier finding: 89-100% of each period's rural proposals land in a brand-new ZIP).

### AI usage:
Built with Claude Code, Simon-Hans Edasi directing. This piece went through six real revisions, each one Simon pushing past a plausible-sounding answer to check what was actually driving the shift. A first pass found a "trade-off" between grid access and EJ score for both rural and urban proposals -- Simon asked directly whether that could just be the population-density confound showing up twice. Then Simon pushed further on the rural/urban split itself: was the internal density-based proxy actually rigorous, or were there real USDA definitions? There are -- and rebuilding the whole analysis on the real RUCA codes (69.9% concordance with the old proxy, a meaningfully different classification) reversed the grid-access-vs-EJ finding: it's urban proposals that show the real trade-off, not rural. Claude caught that reversal itself mid-rebuild, including a subtler bug where several notebook cells' significance-bound self-checks (p>0.05) still passed even after the RUCA correction, but the prose inside them still named the wrong group as the one that "survived" -- a check on the number isn't a check on the sentence describing it, and every instance had to be found and rewritten by hand, not just re-run.

Notebooks: civil/dc_rural_urban_volume.ipynb (primary, all 5 checks), civil/dc_proposal_rural_shift.ipynb, civil/dc_tier_composition.ipynb, civil/dc_rural_tier_link.ipynb, civil/dc_risk_divide.ipynb
