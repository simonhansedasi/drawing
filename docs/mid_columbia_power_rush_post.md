# Same grid, three gold rushes [until I get hired]

Every "data center" dataset I'd touched in this series -- 2,302 facilities, cited in three earlier posts -- turned out to be hiding two categories I'd never looked at: 125 crypto-mining sites and 52 power plants, all traced to one source buried in the merge. Reading through them landed me in my own backyard.

A roughly 100-mile stretch of the Columbia River in central Washington -- Chelan, Douglas, Grant, and Benton counties -- runs on some of the cheapest industrial electricity in the country. Grant County PUD's own published rate: 2.35 cents per kWh. The U.S. industrial average: 8.62 cents. That's not a rounding difference, it's a fourth of the price.

Cheap power draws whoever needs a lot of it, in order:

Bitcoin miners first. Salcido Enterprises' oldest site, a converted industrial building in Cashmere, has been mining since 2014. A competitor, Giga Watt, set up two miles away in the Pangborn Business Park in Wenatchee and went bankrupt by November 2018, owing the local PUD over $310,000. Salcido's flagship site in that same business park is still running today.

Then AI, in the same buildings. Bitfarms bought a 24MW hydro-powered Bitcoin mine at Moses Lake in 2021 for $26M. In November 2025 -- per its own SEC filing -- it signed a $128-129M deal with Vertiv to convert that exact site to AI/HPC infrastructure, NVIDIA GB300 racks, liquid cooling. It decommissioned the Bitcoin mining in April 2026. It started installing AI hardware in August. Same building, same power contract, different tenant.

Then the power itself becomes the product. Helion Energy is building a fusion pilot plant in Malaga, under a power-purchase agreement to sell 50MW to Microsoft. Amazon and Energy Northwest are studying a small modular nuclear reactor near Richland. Both arrived before the AI conversion two counties north had even finished.

And the utility that made all of this possible is now pricing the newest wave out. Grant County PUD ends this cheap rate for data centers and crypto miners on April 1, 2026 -- unbundling them onto market-priced power, an 8-11% jump this year, a projected 9.5% a year for the next decade. The resource that started the rush is being rationed to protect it.

%%%%%
NOTES
%%%%%

Data: Compute Atlas (github.com/ek33450505/compute-atlas, CC BY 4.0), read from its raw per-record file rather than the merged facilities.geojson used in earlier posts -- this file carries per-site status history and source citations. All 10 site coordinates, dates, and dollar figures matched back to that file by name in the notebook (assert fails loudly if a name goes missing). The Moses Lake conversion is sourced to Bitfarms'/Keel Infrastructure's own SEC 10-K and 8-K filings, not press paraphrase. Grant County PUD's rate (Rate Schedule No. 14, effective April 2025) is a primary document fetched directly from grantpud.org this session. Douglas PUD's average rate, the U.S. industrial average, and the 2026 rate-hike percentages are press/aggregator reporting, not independently re-derived from a primary tariff or EIA's raw tables -- flagged as secondary on purpose.

Images: mid_columbia_map.png (all 10 sites, categorized, with a locator inset) + mid_columbia_rates.png (Mid-Columbia hydropower rates vs. the national industrial average) + mid_columbia_timeline.png (twelve years of the same power grid, three waves).

### AI usage:
Built with Claude Code. I found the crypto_mining/power_generation categories while checking whether an earlier post's Texas facility count held up under a different question; picking Central Washington as the piece, and the "gold rush" framing, were mine. Claude did the verification work: confirmed the Texas headline from the earlier post wasn't contaminated by these categories (it wasn't -- 0 of 25), traced every crypto_mining/power_generation record back to a single un-corroborated source in the 4-way merge (0 of 177 have a second source), and pulled Grant PUD's actual rate schedule PDF rather than trusting a search summary before it went in a chart. The Pangborn/Giga Watt near-coincidence (0.2 miles apart) came up as a labeling problem in the map and got kept as a real fact about the site instead of being hidden.
