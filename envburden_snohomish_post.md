Day 4 of visualizing the unseen until I'm hired. What poison are you breathing?

I took data from Washington State's Environmental Health Disparities Map and compared four individual pollution layers against the state's own combined burden score for Snohomish County's 173 census tracts. Turns out population density is NOT a predictor for how bad your air quality is overall. Rather, density predicts WHICH pollutant gets you. Live in the densely packed I-5 corridor and you're breathing exhaust from heavy traffic. Move west toward the coast and you drop into diesel and air toxics instead, likely marine shipping and rail freight along the shoreline. Move east and it's wildfire smoke territory.

Here's the part that surprised me. Two of those three trades are a wash: coastal diesel and eastern wildfire smoke score statistically identical on the county's own combined burden index (p=0.5), different poison, same total dose. But the I-5 corridor doesn't just swap one poison for another. It's the worst overall burden in the county, and it's not close, composite score of 7 out of 10 versus about 4.5 for the other two (p<0.0001). Moving onto I-5 doesn't just change what's poisoning you. It raises the dose.

Pick your poison. Just know one of the three doors leads somewhere worse.

%%%%%
NOTES
%%%%%

Data: WA DOH Environmental Health Disparities Map v3, queried live from its public ArcGIS FeatureServer. All values are decile ranks relative to the rest of Washington State, not raw pollution measurements. The composite (Environmental_Exposures_Theme) is DOH's own precomputed combination, not derived here. Density-vs-burden numbers: traffic-dominant tracts mean composite 7.05 (n=56), diesel-dominant 4.35 (n=46), wildfire-smoke-dominant 4.43 (n=30) — Kruskal-Wallis p<0.0001 across all four categories, traffic vs. either of the other two p<0.0001, diesel vs. smoke p=0.498 (not significant).

### AI usage:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude wrote the visualization code and ran the significance tests.