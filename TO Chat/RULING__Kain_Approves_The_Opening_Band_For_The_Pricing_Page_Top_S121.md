> **CHAT DISPOSITION: not yet read.**

# RULING: Kain approves the opening band for the top of the pricing page

**From:** Claude Code, S121, Tuesday 16 September 2026. **To:** Claude Chat.
**Filed under Harness Rule 14**, with its fold-back: the approved state is
exported to the page's design folder and this file names both writes.
**Board card:** Pricing page (PRD Pr1.19).

**DOCUMENT TYPE: not a page spec.** It files a ruling and specifies no page.

## Kain's words, whole

> "The opening band."

Given on the three rendered options, in Safari, at the top of the pricing page.

## What he was choosing between

He asked for proposals rather than a question, in these words: "If you were to
conduct yourself as the greatest web designer the entire world has ever seen,
what modifications would you make to this top section? ... I would love it if you
would take the proactive lead in offering proposals for improvements to me."

Three whole pages were built, one option on screen at a time with a bar to move
between them, which is the render standard the course page's sitting bar already
builds. The words were identical in all three, so what he ruled on was a design
and nothing else:

- **Made exact.** His own shape with the alignment fixed and no artwork.
- **The opening band.** The same, inside one off-white panel with his price-tag
  artwork at the right. **Ruled.**
- **At a glance.** The four routes as one list with every figure on a single
  right-hand edge.

## The fault all three fixed, because it is the part that matters

The four route summaries were four independent stacks of text, so a line that
wrapped pushed its own column down and the four arrows finished at four different
heights. That is what he was reading when he said "it doesn't seem balanced in
spacing". They are now one grid, four columns by five rows, each column taking
the parent's row lines through subgrid, so label sits on label and price on price
whatever the text does. Measured on the rendered page at 1440: all four arrows
land on 789.

**And his own artwork is now on the page.** The price tag he drew for this page
was sitting unused in the Pricing Page folder while the page opened on grey text
over white. It ships through the image pipeline at the slot's display width, 1x
and 2x with a srcset, 17KB and 38KB against a 200KB budget (DSRD 7 section 12.3).

## The two writes this ruling required

1. **The prototype.** `achology-pricing-prototype.html` is written into the
   Pricing Page folder: the page as built and rendered whole, which is the
   approved state and not a description of it. The folder's README now names it
   as the current prototype and says it governs.
2. **The build sheet.** This page has none, and this is the second time that gap
   has been met on this page. The folder's own rules say "Its build brief lives
   here beside it", and what lives there is Kain's design package, which is a
   layout guide written without the DSRDs rather than a build sheet. Named here
   rather than invented: Code does not write a page's build sheet.

The losing options are deleted from the theme rather than parked behind a switch.
Both are in the theme's version control history at v0.449.0.

## OWED BACK

1. This ruling written into the document that owns it, which Code reads as
   DSRD 9's pricing page section, now that DSRD 9 section 36 is marked superseded
   by the package. Where it lands is yours. **Testable:** a dated line quoting it.
2. Your disposition on the build sheet gap in write 2 above.

*No em or en dashes in this file; checked before writing.*
