## Simon's draft

Data centers require massive amounts of power to run and are building out at unprecedented scale.

Can our existing infrastructure support such a build?

Texas ties with Virginia for the most proposed data centers. It is also the interconnection queue floor.

"Interconnection queue" is a phrase tossed around, but hard to visualize at a refined scale. It's a state level number representing how much new generation capacity is already proposed relative to what's operating. A statewide number, not refinable to plot or zip code scale, but rather useful for comparing neighboring states.

So the highest volume of proposals are in the state with the worst power grid capacity.

Texas does not stand out when controlling for population and geographic area. (((Insert numbers comparing states)))

The state DOES stand out in one way: deregulation.

---

## Claude's draft

Data centers require massive amounts of power to run and are building out at unprecedented scale.

Can our existing infrastructure support such a build?

Texas ties with Virginia for the most proposed data centers of any state -- 25 apiece, out of 2,302 I mapped nationally from four independent sources. It is also the interconnection queue floor: the single worst grid-capacity score of any of the 48 contiguous states, 0.0000.

"Interconnection queue" is a phrase tossed around, but hard to visualize at a refined scale. It's a state level number representing how much new generation capacity is already proposed relative to what's operating -- from EIA's own monthly report. A statewide number, not refinable to plot or zip code scale, but rather useful for comparing neighboring states.

So the highest volume of proposals are in the state with the worst power grid capacity.

Texas does not stand out when controlling for population and geographic area. 7.06 data centers per million residents -- 19th of 48 states, well behind Wyoming's 62.84. 0.86 per 1,000 square miles -- 20th of 48, well behind New Jersey's 7.48. Texas isn't unusually dense with data centers. It's the second-biggest state in the country by both population and land area, and "most data centers" mostly just follows from that.

The state DOES stand out in one way: deregulation. ERCOT runs its own interconnection process -- "connect-and-manage" -- genuinely faster than the more cumbersome studies most other regional grids require, and its deregulated market lets developers negotiate power directly instead of going through a utility. That's the actual reason Texas leads and Texas floors at the same time, not a coincidence of size: a system built for roughly 40-50 large-load projects at a time is now processing over 1,800, about 90% of them data centers, totaling 474 gigawatts of requests. The same speed that made Texas the easiest place in the country to plug in a data center is what let the queue outrun the grid it depends on.

%%%%%
NOTES
%%%%%

Data: facility locations from merascope's public data-center atlas (merascope.com/data/datacenters/facilities.geojson), a 4-source merge of OpenStreetMap, PeeringDB, the IM3 Open Source Data Center Atlas (Battelle Memorial Institute), and Compute Atlas -- 2,302 US facilities, cross-checked against each other, 300m merge radius. Grid-capacity score from EIA Form 860M (planned vs. operating generation capacity by state), computed by merascope's own pipeline. Population and land-area figures are real U.S. Census Bureau numbers (July 2025 population estimates; official state land-area table). The ERCOT/deregulation mechanism is sourced to real reporting on Texas's "connect-and-manage" interconnection process and the 2026-08-03 Abbott administration pause on new data-center grid connections pending a state audit.

Images: dc_grid_queue_map.png (grid-capacity score, all 48 contiguous states) + dc_grid_queue_proposed_map.png (where new data centers are actually being proposed, Texas highlighted) + dc_grid_queue_marketsize_map.png (total existing data centers per state, the variable that actually predicts new proposals) + dc_grid_queue_substation.png (how close Washington's own confirmed sites sit to a real grid substation).

### AI usage:
Built with Claude Code. Ideation, framing, and every real call were mine, Simon-Hans Edasi; Claude wrote the code and ran the numbers. Real catches worth naming: I asked whether Texas still led once you control for market size, and it didn't -- 15th of 48 by share, not 1st. I asked the same for population and geographic area, and it didn't stand out there either -- solidly mid-pack on both, real Census figures, not eyeballed. When I said Texas is in this situation because of its grid, Claude checked that against actual press coverage instead of taking it on faith, and confirmed ERCOT's own "connect-and-manage" process is the documented, specific mechanism behind both halves of the finding -- not something either of us assumed going in.
