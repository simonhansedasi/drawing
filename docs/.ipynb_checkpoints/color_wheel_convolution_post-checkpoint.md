Visualizing the Unseen (until I get hired): what do brown and pink have in common?

White light is made of all the colors right? So, adding the individual bands should get you back to the full spectrum white, right?

Newton described the spectrum of light with discrete colors (seven colors for seven notes of a musical scale), however, those colors don't quite line up evenly in the spectrum. Naively add all the wavelengths of light and you get a shade of pink I like to call Newtonian Pink (hex #ffb5e5).

Mixing pigments is a different story, and runs the other direction. Mixing colored pigments is a race against brown: add too different of colors and the result is a brownish mud. In fact, adding any two complementary colors and brown is the result. It is the mixing of reflectance peaks being washed out and resulting in brown I like to call Rossian Brown (hex #4f2812).

Combining colors with different mediums produces different results.

So, which is right? Is the combination of all colors white, pink, or brown?

Like everything, it depends on context. We must agree on the goal before deciding or judging methods. 



%%%%%%
Claude draft
%%%%%%


Neither one is a real color of light. Both are combinations of the color spectrum.


Brown doesn't have its own wavelength. Take a dim, low-reflectance orange-hued patch and view it completely alone, nothing brighter nearby, and it reads as dim orange, not brown. Brown only shows up once there's something brighter in the same scene for your eye to judge it against. It's not a property of the light. It's a judgment your visual system makes about context.

Pink is the stranger case. Mix all seven "rainbow" colors -- red, orange, yellow, green, blue, indigo, violet -- the naive way, one part each, and you don't get white. You get a bright rose-pink. Officially named it Newtonian Pink, hex ffb5e5, since it's really Newton's fault: he divided the spectrum into seven bands to match the seven notes of a musical scale, not because light divides evenly, so violet's sliver of spectrum counts exactly as much as red's much wider one. Check that pink's actual hue and it lands in the same family as purple: magenta. Magenta doesn't exist on the spectrum at all. There's no wavelength of light that looks magenta -- your eye invents it by firing its red-sensing and violet-sensing cones at once with green suppressed, treating two opposite ends of the spectrum as if they were adjacent. Same reason the color wheel gets drawn as a circle instead of a line: it bends the spectrum around and glues the ends together through a hue that was never really between them.

Weight those same seven colors by how much of the real spectrum each one actually represents instead of one part per name, and the sum does converge to white. Newton's naming scheme was never built to add up. Real physics still does.

Two "ordinary" colors, brown and pink, both illusions your own visual system is performing on you, for two completely different reasons. (For the record, mixed the honest way -- any two complementary colors on the wheel, multiplied instead of added -- you get a dark, muddy brown-red I'm calling Rossian Brown, hex 4f2812. Every pigment mixing you've ever done was quietly doing this the whole time.)

Reading Eugenia Cheng's Is Math Real? right now, and her whole argument is that whether a piece of math "works" depends on which world you're doing it in. Turns out the same is true of color -- whether something reads as pink, brown, orange, or white depends on what you do with it and what's around it, not on some fixed truth sitting in the light itself.

What's a color you assumed was "real" that turned out to be something your brain made up?

Notebook: color_wheel_convolution.ipynb

%%%%%
NOTES
%%%%%

Built with Claude Code. Ideation, framing, the color-theory questions, and the naming (Newtonian Pink, Rossian Brown) were all mine, Simon-Hans Edasi. Claude built the spectral reflectance model, ran the CIE color-matching pipeline, and generated the visualizations from iterative direction from me -- I caught a couple of real mistakes along the way (a naive wavelength-to-RGB bug that made red render orange, and Rossian Brown first landing on the wrong figure), both fixed on the spot.
