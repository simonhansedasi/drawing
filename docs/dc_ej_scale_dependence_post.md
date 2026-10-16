Visualizing the unseen: one number gets 44% of an explanation, until it doesn't. And where it doesn't is where it really matters.

Can we predict EJ burden from other data? The first principal component of 21 features explains 44% of the answer...outside cities.

Inside Seattle, Tacoma, Spokane, 





One number gets you 44% there — until it doesn't [until I get hired]

One number gets you 44% there. And where it doesn't carry information is where it really matters.

That number is simple: how close is this ZIP code to a city. Across Washington state, that single fact explains 44% of the real gap in pollution-and-poverty burden between neighborhoods -- more than any of the other seventeen physical factors I checked (water access, flood risk, seismic risk, and so on) gets you on its own. Zoom out to the whole state, and geography basically tells the story.

Then zoom into any one city and it stops telling you anything. Inside Seattle, inside Tacoma, inside Spokane, that same number that just explained 44% of the entire state now explains about 1%.

Here's why, and it's not a different mechanism, it's the same one running out of room: that number only has power because it can tell a rural ZIP code from an urban one. Every neighborhood in these three cities is already urban. There's nothing left for "how close to a city" to distinguish once you're only comparing one Seattle block to another.

So what fills the gap? A map from 1935. The neighborhoods a federal agency graded "Hazardous" for mortgage lending ninety years ago explain 18% of who's burdened in these same three cities today -- about 13 times what physical geography has left to offer at that scale. Two maps, two completely different explanations, and neither is wrong. They're just answering the question at two different zoom levels: one for the whole state, the other for the block you actually live on.

Notebook: dc_ej_scale_dependence.ipynb

%%%%%
NOTES
%%%%%

Third piece in this thread, ties the first two together. Data: merascope's own scored WA ZCTA pipeline (605 ZIP-code areas) for the physical/infrastructure side; Mapping Inequality's digitized 1930s HOLC grades (166 polygons, Seattle/Tacoma/Spokane, the only WA cities surveyed) for the historical side. "One number" is PC1 from a PCA run on 21 real physical indicators (28% of all their variance, validated against known density proxies before being trusted) -- built and explained in `dc_ej_urban_axis_pca.ipynb`. Both checked against the same real EJ index (environmental hazard exposure x demographic vulnerability, EPA's own formula, not a demographic stand-in).

The mechanism is checked, not assumed: urban-axis standard deviation is 5x smaller within HOLC-graded neighborhoods than statewide, and every one of those 159 neighborhoods sits in roughly the top third of the full statewide range. Asserted in-notebook before the piece could claim it.

Images: dc_ej_scale_dependence.png -- four panels: where HOLC's cities sit on the statewide urban-axis distribution (literally showing the restricted range), the R² comparison at both scales, Washington colored by the urban axis, and Seattle alone colored by 1930s grade.

### AI usage ###:
Built with Claude Code. Ideation, framing, and every real call were mine, Simon-Hans Edasi. This piece exists because I asked how the physical-siting finding and the redlining finding fit together -- Claude's first pass tried a joint regression (do they add up to a bigger number?) and the honest answer was no, barely; I pushed on why, and the actual mechanism -- restricted range, not competing explanations -- came out of checking the axis's own spread inside vs. outside HOLC's cities rather than assuming a story. Hook line is mine.
