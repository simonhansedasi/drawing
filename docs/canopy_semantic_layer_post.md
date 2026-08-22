Day TBD of Visualizing the Unseen [until I get hired]: The tool the job postings want couldn't hold my own data

Job descriptions keep naming Power BI and Tableau. So I pointed one at a real project instead of a tutorial dataset: a precision-viticulture pipeline of mine modeling vine canopy health across 32,978 hex cells of Washington State wine country. Power BI Service wouldn't take a personal email at signup; the Looker Studio fallback worked, until its map chart crashed the browser tab trying to draw one marker per row at that resolution. That's not login friction -- it's the tool telling me its native shape is a business dashboard with a few thousand rows, not a science dataset at meter resolution.

So I went back to the process I already had, but not as one-off scripts. I specified a shared module encoding the actual decisions a correct version of this needs: don't let a naive interpolator smear color across the empty gaps between disconnected vineyard blocks; use a diverging color scale for a signed delta and a sequential one for a magnitude, never the wrong one for what the number means; anchor "peak NDVI" to a single shared date, not each cell's own noisy argmax (that version was badly speckled -- caught by looking at the image, not by any test passing). Used Claude Code -- CLI, skills, the harness -- to implement each of those against my spec, including the two that were wrong on the first pass.

What came out: bud break to pre-harvest peak (mean +0.22 NDVI, one lagging block in the northeast), peak to harvest (mean -0.07, expected for wine grapes -- deficit irrigation after veraison concentrates sugar on purpose), and the two aren't independent observations -- a direct correlation check (r=-0.61 across all 32,978 cells) confirms the same block that built up least also declined least, not two maps that happen to look similar. Plus the full season, frame by frame, real satellite dates.

The actual capability isn't "AI made a chart." It's knowing which tool fits which job, specifying what a correct visualization has to encode, and catching it when a first pass gets that wrong.

Notebook: canopy_semantic_layer.ipynb
