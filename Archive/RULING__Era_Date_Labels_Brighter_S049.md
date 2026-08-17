# RULING: the About story stage's era date labels go brighter

**From:** Claude Code, S049. **Date:** 2026-08-06. **Filed under Harness Rule 14.**
**Closes:** the one §7 fail in `RECORD__About.md`. **Shipped:** v0.38.63, deployed and verified live.

## Kain's words

Put to him as two whole rendered About pages, each scrolling itself to the dark story stage, at full width. Not as numbers: he has ruled repeatedly that he cannot judge a colour from a description, and this is a colour. His answer, verbatim:

> "B please"

**A** was the label as built. **B** was the same label brighter.

## What it settles

`.cons-stage__dates` moves from white at 55 percent to white at 65 percent on the dark stage gradient.

**Why it needed to move.** Measured on the rendered page, the labels sit about 23 percent along the stage's gradient, where the ground is roughly `#3A4852`. At 55 percent the label read **4.14:1**. DSRD 6 §7 names the bar: WCAG 2.2 AA, which is 4.5:1 for text at 11px. It failed across the whole first half of the stage.

**Why 65 rather than the smallest passing value.** 59 percent would have cleared the bar at the labels' own position and 63 percent everywhere on the stage. 65 is the value the sub-label directly beside them already uses, so taking it fixes the contrast and removes a near-duplicate in the same move, which is DSRD 6 §10's first verdict rather than its second: *"Collapse it. The value sits close enough to a named one that using the named one leaves the page looking the same... Two values a hair apart are drift, not design."* The stage now carries one white-transparency value where it carried two.

## Verified live, not asserted

```
.cons-stage__dates   rgba(255, 255, 255, 0.65)   about.css?ver=0.38.63
  at the labels' position on the gradient   5.08:1
  at the lightest point of the gradient     4.74:1
  bar                                       4.50:1
```

Clears AA everywhere on the stage, not just where the labels happen to sit.

## One thing left beside it, not swept

`about.css` carries a second white-at-55-percent, on `.fa-act--dark .m-stat span`, which is a different element in the timeline's dark act rather than the era label Kain ruled on. It may well have the same problem. I have not touched it: he ruled on the era dates, and Rule 3 does not let a ruling on one element quietly become a pass over every similar one. It is measured and raised when the timeline itself comes up.

*No em or en dashes in this file; checked before writing.*
