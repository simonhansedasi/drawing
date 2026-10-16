# Suggestions for Improving the Fiber Proximity vs. Household Access Map

## Overall assessment

The map has a strong and original analytical concept:

-   **Solid fill = fiber proximity**
-   **Stripes = household internet access**
-   Both variables use the **same 0--1 color scale**
-   Similar colors indicate agreement
-   Contrasting colors indicate disagreement

The main strength is that the map puts the comparison directly into the
geography rather than forcing readers to compare two separate
choropleths.

The main opportunity is to make the underlying analytical insight easier
to see by reducing visual complexity.

------------------------------------------------------------------------

# Priority improvements

## 1. Make the stripe overlay less visually dominant

The current stripes compete strongly with the underlying fill.

Try experimenting with:

-   Thinner stripes
-   Greater spacing between stripes
-   Partial transparency
-   Slightly reduced contrast

### Goal

The reader should ideally perceive:

1.  The underlying fiber proximity pattern
2.  The household-access overlay
3.  Areas where the two disagree

The current version sometimes makes steps 1 and 2 equally difficult to
distinguish.

------------------------------------------------------------------------

## 2. Reconsider pure white as the midpoint

The legend currently uses white to represent approximately average
values.

Potential problem: white can also look like:

-   Missing data
-   No-data areas
-   Background
-   Empty geography

### Suggested solution

Use a very light gray or neutral off-white for the midpoint instead.

For example:

-   Blue = low
-   Light gray = average
-   Red = high

This would make the midpoint look intentional rather than potentially
absent.

------------------------------------------------------------------------

## 3. Improve the title hierarchy

The current title explains both the topic and the encoding.

Consider separating those jobs.

### Possible analytical titles

**Fiber Infrastructure Does Not Always Translate into Household Internet
Access**

**Comparing Fiber Proximity and Household Internet Access**

**Close to Fiber, Still Offline?**

**The Geography of the Fiber--Access Gap**

Then use the subtitle primarily to explain:

-   Fill = fiber proximity
-   Stripes = household internet access
-   Same colors = agreement
-   Contrasting colors = disagreement

------------------------------------------------------------------------

# The most interesting scientific result: disagreement

The most interesting parts of this visualization may not be the areas
with high or low values.

They may be the places where infrastructure and household access
disagree.

Conceptually:

    Fiber proximity ≠ household connectivity

This creates two potentially important mismatch types.

## High fiber proximity + low household access

Possible interpretation:

> Infrastructure may be geographically nearby, but households are not
> translating that proximity into actual connectivity.

Possible mechanisms to investigate:

-   Affordability
-   Last-mile infrastructure
-   Subscription barriers
-   Provider competition
-   Rural service economics
-   Digital literacy
-   Housing characteristics

## Low fiber proximity + high household access

Possible interpretation:

> Households may be accessing the internet through infrastructure or
> technologies not captured by the fiber-proximity measure.

Possible mechanisms:

-   Fixed wireless
-   Cable infrastructure
-   Satellite internet
-   Municipal broadband
-   Population-density effects
-   Alternative providers

------------------------------------------------------------------------

# Recommended companion analysis: calculate the gap explicitly

Create a difference variable:

    Gap = Household Access - Fiber Proximity

Then map the result with a diverging color scale.

Suggested interpretation:

-   Blue = fiber proximity is greater than household access
-   Red = household access is greater than fiber proximity
-   Neutral = the two measures broadly agree

This would make the central analytical question much easier to see.

------------------------------------------------------------------------

# Suggested figure set

Instead of relying entirely on the dual-encoding map, consider a
four-figure sequence.

## Figure A --- Fiber Proximity

A standard choropleth showing only the infrastructure variable.

Question:

> Where is fiber geographically close?

## Figure B --- Household Internet Access

A standard choropleth showing actual household access.

Question:

> Where are households actually connected?

## Figure C --- Fiber--Access Gap

Map:

    Household Access - Fiber Proximity

Question:

> Where does infrastructure proximity fail to predict household
> connectivity?

This may be the strongest analytical figure.

## Figure D --- Agreement/Disagreement Overlay

Use the current fill + stripe visualization.

Question:

> What do the two spatial patterns look like when directly compared?

The current visualization works especially well as a diagnostic or
synthesis figure after readers have seen the individual variables.

------------------------------------------------------------------------

# Potential next-level analysis

The map naturally suggests a statistical research question:

> How well does fiber proximity predict actual household internet
> access?

Possible analyses:

## Correlation

Calculate the correlation between:

-   Fiber proximity
-   Household access

## Regression

Model:

    Household Access ~ Fiber Proximity

Then examine:

-   Coefficient strength
-   R²
-   Spatial residuals

## Residual mapping

Calculate:

    Residual = Observed Household Access - Predicted Household Access

This could be especially powerful.

Instead of simply asking where fiber and access differ, you would ask:

> Where is household access unexpectedly high or unexpectedly low given
> the local infrastructure environment?

Those places could become candidates for investigating social, economic,
geographic, or policy explanations.

------------------------------------------------------------------------

# Cartographic experiments worth trying

-   Reduce stripe thickness
-   Increase stripe spacing
-   Add transparency to stripes
-   Replace pure-white midpoint with light gray
-   Slightly simplify boundaries if very small polygons create visual
    noise
-   Test whether the legend can more explicitly explain the two
    encodings
-   Consider a small inset showing the two variables separately
-   Consider labeling a few extreme disagreement regions

------------------------------------------------------------------------

# Bottom line

The map's central idea is strong and original.

The biggest improvement would be to make the disagreement itself the
explicit analytical focus.

The strongest potential story is not simply:

> Where is fiber?

or:

> Where do households have internet?

It is:

> **Why does physical proximity to fiber infrastructure sometimes fail
> to translate into real household connectivity?**

That question could support a much larger analysis involving
affordability, geography, alternative technologies, infrastructure
deployment, and socioeconomic barriers.
