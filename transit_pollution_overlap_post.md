%%%%%%%%
v2 draft
%%%%%%%%

Day 6 of visualizing the unseen [until I get hired]. Environmental justice work often assumes a double burden. I tested that assumption, and it doesn't hold here.

The assumption: neighborhoods locked out of transit are also the ones stuck breathing the worst air. That's not me reading a hypothesis into the data. "Double burden" is documented language in transit-equity and environmental-justice research for exactly this compounding pattern. I tested it against 173 Snohomish County census tracts, matching Day 2's transit gap score against Day 4's pollution burden composite. It doesn't hold up here, and not in the direction you'd expect.

The tool for "do two variables move together" is a correlation coefficient. I used Spearman's rho instead of the more common Pearson's r because these scores are ranks, not clean linear measurements, and rho only asks whether one variable consistently rises as the other falls — no straight-line assumption required. It came back at -0.24 (p=0.002, n=173). Weak effect, but statistically distinguishable from noise.

It reads as an urban/rural trade-off hiding under a single number. The I-5 corridor has decent bus service but takes on the traffic and diesel exposure that comes with density. Rural tracts have clean air and almost no transit. Nobody in this county is getting hit twice. Every part of the county is trading one burden for the other, not stacking both.

The double burden this research describes isn't showing up here. Worth checking before assuming it does anywhere else.

%%%%%
NOTES
%%%%%

Data: snotrac gap_score (Day 2, Community Transit GTFS + Census ACS, block-group level) population-weighted up to census-tract level to match WA DOH's Environmental_Exposures_Theme (Day 4). No new pipeline run — both composites are the tools' own outputs, aggregated by matching each block group's tract prefix, not derived here.

Spearman's rho vs. Pearson's r: Pearson fits a straight line through the raw values and measures how tightly points cluster around it — sensitive to outliers and assumes a linear relationship. Spearman converts both variables to ranks first, so it only measures whether they move in a consistent direction, and it's the better fit for scores like these that are ordinal (deciles) or heavily skewed rather than normally distributed.

"Double burden" sourcing: the term and the compounding pattern it describes (inadequate transit access co-occurring with elevated pollution exposure) are used in transit-desert and environmental-justice literature — see writing on transit deserts (energy.sustainability-directory.com/term/transit-deserts) and state cumulative-impact policy overviews (ncelenviro.org/issue/cumulative-impacts), which lists WA's own Environmental Health Disparities Map among the state tools built to screen for it. Checked via a literature-review pass before this claim shipped, not asserted from memory.

### AI usage:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude wrote the aggregation and plotting code and ran the correlation check that overturned the "compounding burden" hypothesis before it shipped. Literature review was performed by Claude using a skill designed by me, Simon-Hans Edasi.





















%%%%%%%%%%%%
working copy
%%%%%%%%%%%%

Day 6 of visualizing the unseen [until I get hired]. Environmental justice work often assums a double burden; I can show that isn't the case.

Environmental justice work often assumes a double burden: the same neighborhoods locked out of transit are also stuck breathing the worst air. I tested that assumption against 173 Snohomish County census tracts, matching Day 2's transit gap score against Day 4's pollution burden composite. It doesn't hold up, and not in the direction you'd expect.

The tool for "do two variables move together" is a correlation coefficient. I used Spearman's rho instead of the more common Pearson's r because these scores are ranks, not clean linear measurements, and rho only asks whether one variable consistently rises as the other falls — no straight-line assumption required. It came back at -0.24 (p=0.002, n=173). Weak effect, but statistically distinguishable from noise.

It reads as an urban/rural trade-off hiding under a single number. The I-5 corridor has decent bus service but takes on the traffic and diesel exposure that comes with density. Rural tracts have clean air and almost no transit. Nobody in this county is getting hit twice — every part of it is trading one burden for the other, not stacking both.

The compounding burden some environmental justice frameworks worry about isn't showing up here. Worth checking before assuming it does anywhere else.

%%%%%
NOTES
%%%%%

Data: snotrac gap_score (Day 2, Community Transit GTFS + Census ACS, block-group level) population-weighted up to census-tract level to match WA DOH's Environmental_Exposures_Theme (Day 4). No new pipeline run — both composites are the tools' own outputs, aggregated by matching each block group's tract prefix, not derived here.

Spearman's rho vs. Pearson's r: Pearson fits a straight line through the raw values and measures how tightly points cluster around it — sensitive to outliers and assumes a linear relationship. Spearman converts both variables to ranks first, so it only measures whether they move in a consistent direction, and it's the better fit for scores like these that are ordinal (deciles) or heavily skewed rather than normally distributed.

### AI usage:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude wrote the aggregation and plotting code and ran the correlation check that overturned the "compounding burden" hypothesis before it shipped. Literature review was performed by Claude using a skill designed by me, Simon-Hans Edasi.







%%%%%%%%
original -- do not delete
%%%%%%%%

Day 6 of visualizing the unseen [until I get hired]. Environmental justice work often assumes a double burden: the same neighborhoods locked out of transit are also stuck breathing the worst air. I tested that assumption against 173 Snohomish County census tracts, matching Day 2's transit gap score against Day 4's pollution burden composite. It doesn't hold up — and not in the direction you'd expect.

The tool for "do two variables move together" is a correlation coefficient. I used Spearman's rho instead of the more common Pearson's r because these scores are ranks, not clean linear measurements, and rho only asks whether one variable consistently rises as the other falls — no straight-line assumption required. It came back at -0.24 (p=0.002, n=173). The p-value is the "is this real" check: 0.002 means there's only a 0.2% chance a relationship this strong shows up by chance if there's actually nothing there — so the trend itself isn't noise. But -0.24 is a weak coefficient (0 = no relationship, 1 or -1 = perfect), which is the "how much does it explain" check: knowing a tract's transit score barely narrows down where its pollution rank falls. And the sign runs backward from the double-burden hypothesis — worse transit access leans toward less pollution, not more.

It reads as an urban/rural trade-off hiding under a single number. The I-5 corridor has decent bus service but takes on the traffic and diesel exposure that comes with density. Rural tracts have clean air and almost no transit. Nobody in this county is getting hit twice — every part of it is trading one burden for the other, not stacking both.

The compounding burden some environmental justice frameworks worry about isn't showing up here. Worth checking before assuming it does anywhere else.

%%%%%
NOTES
%%%%%

Data: snotrac gap_score (Day 2, Community Transit GTFS + Census ACS, block-group level) population-weighted up to census-tract level to match WA DOH's Environmental_Exposures_Theme (Day 4). No new pipeline run — both composites are the tools' own outputs, aggregated by matching each block group's tract prefix, not derived here.

Spearman's rho vs. Pearson's r: Pearson fits a straight line through the raw values and measures how tightly points cluster around it — sensitive to outliers and assumes a linear relationship. Spearman converts both variables to ranks first, so it only measures whether they move in a consistent direction, and it's the better fit for scores like these that are ordinal (deciles) or heavily skewed rather than normally distributed.

### AI usage:
Built with Claude Code. Ideation, framing, and review were done by me, Simon-Hans Edasi. Claude wrote the aggregation and plotting code and ran the correlation check that overturned the "compounding burden" hypothesis before it shipped.
