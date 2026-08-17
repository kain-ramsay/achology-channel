# RULING: the mobile navigation triggers at 880px, not 768px

**From:** Claude Code, S048. **Date:** 2026-08-06. **Filed under Rule 14.**
**Authority:** Kain, in session, ruled on the rendered comparison.
**Acted on and shipped:** v0.38.53, live and verified. **Document correction owed by Chat.**

## Kain's words

Shown three panels of the real Policies page at exact iPad width (the site as
it stood, and two candidate fixes) and asked "Menu button, or tightened bar?",
he answered:

> "Menu button"

## What that rules

The hamburger menu takes over the whole band the desktop header cannot fit
into, rather than the desktop header being compressed to fit. In force from
v0.38.53.

## The defect behind it

Found by the S048 DSRD 6 walk of the Policies index, §7 and §8. Measured on the
live site:

| Viewport | Page scroll width | Slides sideways |
|---|---|---|
| 640 | 640 | no |
| 768 | 880 | yes, by 112px |
| 870 | 880 | yes, by 10px |
| 900 | 900 | no |

`.site-header__inner` has a natural width of exactly 880px and cannot compress
below it. The element pushing it out is the Sign In button. The hamburger was
already hidden above 767.98px, so there was no fallback anywhere in the band.
768px is an iPad held upright. Confirmed identical on `/about/`, so it was every
page on the site.

## The document correction Chat owns

**DSRD 8 §18.15 currently reads, word for word:**

> "**Trigger:** Hamburger icon replaces nav links and Sign In button at < 768px (per DSRD 7 §4.1). Logo remains visible."

That sentence is now wrong, and it was measurably impossible on the day it was
written: the header it describes has never fitted in the tier it was pinned to.
It needs to become 880px, with the reason recorded, because the number is
measured rather than chosen and a later reader will otherwise "tidy" it back to
the tier boundary.

**Two further edits this implies:**

1. **DSRD 7 §4.1's dependants list** names "DSRD 8 §18.13 (mobile navigation
   trigger)" among the sections that depend on the breakpoint values. That
   dependency is now severed by design: the navigation trigger no longer
   follows the tier. Worth saying so explicitly in both places, so the next
   person to change a tier does not assume the nav follows it.
2. **DSRD 7 §4.1 itself is untouched.** The three tiers stand, and gutters,
   grids and type still turn at 768 and 1024. This is a navigation trigger, not
   a fourth tier, and the distinction is the whole reason the change is safe.
   `.site-header__inner`'s 32px tablet padding deliberately still turns at 768.

## One instrument finding, not yet acted on

`page_gate` samples tablet at **900**, which sits just above the top of the
broken band, so it has stepped over this defect on every page it has ever
measured, including the nine policy-family records already filed. A gate that
samples one point inside a range cannot see the range.

I have not changed the gate, because changing what the instrument measures
part-way through the walk would make the records already filed incomparable
with the ones still to come. **That sequencing needs a ruling:** change the gate
now and re-run the nine, or finish the walk on the current instrument and sweep
afterwards. Filed here rather than decided.

## Verified live, v0.38.53

| Width | Result |
|---|---|
| 375 | menu button, no sideways scroll |
| 768 | menu button, no sideways scroll, band closed |
| 800 | menu button opens, 23 links, overlay covers the screen |
| 879 | menu button, no sideways scroll |
| 880 | full bar returns and fits exactly |
| 1440 | full bar, all three mega menus present |

`css_gate` PASS on header.css and style.css.

One note on how that was verified, because it nearly went wrong. Reading the
menu's computed style straight after clicking reported it hidden, and I almost
recorded the menu as broken. The cause was the instrument: the tab was not
fronted, so CSS transitions never advanced and the computed value stayed frozen
at the start of the interpolation. Removing the transition and re-reading showed
the menu open, visible, with a menu link under the centre of the screen. The
lesson from S047 holds and needed restating in a new costume: measure the
rendered result, and when the result looks impossible, suspect the instrument
before the code.

*No em or en dashes in this file; checked before writing.*
