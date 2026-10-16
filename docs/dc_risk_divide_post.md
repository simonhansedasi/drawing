Merascope's public risk tool ranks every ZIP code in the country by how much it resembles a place that already has a data center. I pulled the numbers behind that ranking to answer a different question: are the places getting new proposals the same places that already have one?

Mostly -- but less than you'd think. The top-ranked tier holds 43% of every built data center in the country, but only 28% of what's currently proposed or permitted. New activity is still concentrated in the same kind of places, just noticeably less concentrated than the existing stock.

The sharper split shows up in 206 ZIP codes with zero built data centers and at least one proposed. 34% of those are rural (USDA's real rural/urban classification, not an internal proxy). ZIPs that already host a facility: only 16% are rural. The frontier is roughly twice as rural as the existing footprint -- still moving into places without the built infrastructure or the local precedent yet, just not the outright rural-majority split an earlier, cruder density check suggested.

One real example: King George County, Virginia. Nothing built there yet, but two real projects on the books -- Amazon's permitted Birchwood Data Campus and a proposed second project from Green Energy Ventures. A county with zero data-center history about to have two.

Two things this isn't. It isn't "proposals are rural" in an absolute sense -- the proposed rate still climbs with tier, from 0% at the bottom to 2.2% at the top, just less steeply than the built rate does. And it isn't a story about environmental-justice neglect -- I checked, and those 206 new-frontier ZIPs actually score better (less burdened) on Merascope's own EJ index than ZIPs that already host a facility, not worse.

%%%%%
NOTES
%%%%%

Data: Merascope's own public risk model (merascope.com/#/risk), rebuilt this session after a national EJ-index recompute. Facility data is a 4-source merge (OpenStreetMap, PeeringDB, the IM3 Open Source Data Center Atlas, Compute Atlas), 2,302 US facilities, cross-referenced. King George County, VA facility records independently verified against their own source articles: Birchwood Data Campus (datacenterdynamics.com), King George Technology Center (fxbgadvance.com).

Images: dc_risk_divide_tiers.png (share of national built vs. proposed data centers, by suitability tier) + dc_risk_divide_rural.png (rural share of ZIPs already hosting vs. ZIPs with something proposed and nothing built).

### AI usage:
Built with Claude Code, Simon-Hans Edasi directing. Simon caught that the live risk numbers were stale relative to a national EJ-index rescore he'd just pushed, and asked for the pipeline to be rerun before trusting anything from it -- the rerun confirmed the core 206-ZIP/rural-split finding didn't move (it doesn't depend on EJ score at all), though the tier-concentration numbers shifted slightly (43%/28% vs. the earlier 42%/26%). Building the King George example, Claude checked each cited facility's coordinates against its real source address instead of trusting the pipeline's raw count, and caught a real geocoding bug: one of the three "proposed" facilities the model had attributed to that ZIP is actually 13 km away, across the Potomac in Maryland -- excluded from the two used in the post. Separately, Simon later questioned whether the rural/urban split itself was rigorous -- the pipeline had been using an internal population-density proxy, not a real definition -- so Claude rebuilt the whole rural/urban classification on USDA ERS's actual RUCA codes. The direction held (frontier ZIPs are more rural than the built footprint) but the magnitude roughly halved (69%/29% under the proxy became 34%/16% under RUCA).

Notebook: civil/dc_risk_divide.ipynb
