Day 13 of visualizing the unseen (until I get hired): my resume gaps. See them filled at grape-expectations.simonhansedasi.com

I have spent this job search discovering that "I will learn it on the job" is not a sentence employers accept anymore. Job postings ask for BI or GIS experience with some regularity. I have avoided both, mostly on the principle "I do not pay a subscription fee to make a chart." That principle does not survive an applicant tracking system.

So: GrapeExpectations, the most rigorous pipeline I have built. Nine years of Sentinel-2 imagery, pulled through Google Earth Engine, trained across 33,028 hex cells in PySpark MLlib. QGIS for the maps GEE cannot draw. Looker Studio for the BI layer, since Power BI does not accept a personal Gmail account.

What is your own resume quietly not showing?

%%%%%
NOTES
%%%%%


Link: grape-expectations.simonhansedasi.com (interactive map + live BI report both embedded there)


### AI Usage ###:
Built with Claude Code. Ideation, framing, iteration, design & style, were done by me Simon-Hans Edasi through the semantic layer designed and maintained also by me. Claude generated initial code for QGIS maps, iterated by me in the QGIS python editor. Claude also implemented the CSS code to align the reports and served as responsive rubber ducky (RRD).


### AI usage note (matching this campaign's established framing — credit the specification and the catches, not "AI generated it"):
Claude built the QGIS Python-console scripts (elevation basemap, NDVI-through-season attempts — grass blades, then a plain choropleth, after two rounds of Claude's own sizing/performance mistakes that Simon caught and sent back), the Leaflet interactive map (also debugged live — a bad SRI hash Claude introduced, then fixed, then verified against source), and the Looker Studio embed wiring on the site (including a report-ID typo Claude introduced and had to trace back and fix). The actual BI report content — the leaderboard-is-ranking-noise catch, the pivot to aspect-band grouping, the SUM-vs-AVERAGE aggregation bug, the CASE/END autocomplete gremlin — was Simon working in Looker Studio directly; Claude's role there was diagnosis and instructions, not hands-on-keyboard.
