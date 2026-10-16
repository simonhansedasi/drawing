Visualizing the unseen (until I get hired): that land favored by data centers.

How similar is your ZIP code to a ZIP code that currently hosts a data center?

I used a classification model to rank ZIP codes by how much they look like ZIP codes that contain data centers. I dropped the classification layer, sorted by the probabilities of containing a data center, and divided into ten even bins.

The results are hosted at merascope.com/#/risk. You can even look up your ZIP and see your exposure risk tier.

But, here's the thing: Construction of new data centers is not following the standard pattern. They're moving into different ZIPs, away from the typical ZIP that has hosted a data center in the past.

The middle tiers have an outsized proportion of proposed vs built data centers: the top tier alone holds 43% of every data center built in the country, but only 28% of what's currently proposed or permitted. Already-built ZIPs average tier 8.7. Proposed ones average tier 7.9. Rural ZIPs are absorbing more too -- rural proposals have grown 5.4x since before 2024, against urban's 3.4x.

The exposure ranking still tells you where data centers already are. It's stopped telling you where they're going.

%%%%%
NOTES
%%%%%

Data: Merascope's own public risk model and 22-indicator siting pipeline (merascope.com/#/risk), 33,252 US ZCTAs. Tiers are out-of-fold predicted probabilities from a `has_dc` classifier, prediction discarded, only the probability kept, rank-cut into 10 equal-count bins -- the same method the live product uses. Built-vs-pipeline comparison uses the model's own `has_dc` (1,196 ZCTAs) and `has_dc_forward` (259 ZCTAs) labels on that same tier column. Rural growth figure (5.4x vs 3.4x) uses USDA ERS's real RUCA rural/urban classification, not a density proxy.

Images: dc_tier_built_vs_pipeline.png (share of built vs. proposed/permitted ZCTAs by tier -- built peaks hardest at tier 10, pipeline peaks earlier at tiers 8-9 and drops back at 10) + dc_tier_composition_profile.png (national mean of each indicator by tier, for readers who want the underlying grid-access/EJ trade-off tier 10 is built on).

### AI usage:
Built with Claude Code, Simon-Hans Edasi directing.
