# RULING: Kain takes the AA-safe orange into the pricing page's last three controls, and DSRD 7 contradicts itself on link colour

**From:** Claude Code, theme session, S128, Tuesday 22 September 2026. **To:** Claude Chat.
**Board card:** Pricing page.
**Theme version:** v0.622.0, deployed and pushed.

## What Kain ruled, in his own word

Put to him in the sitting as one yes or no, with the AA-safe orange as the recommendation and no alternative offered, because the palette already held the answer. **His word: "yes".**

Acted on in the same sitting under Rule 14, filed here so it reaches the documents that own it.

## What it was ruled on

DSRD 6 §7's machine half was re-run on his instruction, expecting the S127 button contrast repair to have cleared it. **It had not.** The repair landed and did work: it took `.btn-primary`'s fill from brand orange to `--color-orange-link` and the failing node count from 13 to 10. What remained were three places a change to that one class could not reach, every one of them brand orange `#ED6922` measuring **3.16:1** against the 4.5:1 WCAG 2.2 AA asks below large text:

1. The seven outlined "Access This School" buttons on the school cards. They override `.btn-primary` entirely, under Kain's own S127 "Quiet" ruling, so the S127 fix could not touch them.
2. The bundle payment-plan menu inside his sentence above the seven cards.
3. The "Explore the Pass" button on the third choice card, whose class is not `.btn-primary`.

## What shipped

All three now take `--color-orange-link`. The seven outlined buttons take it as label and border and fill with it on hover, so white on the hover measures 5.36 rather than the 3.89 S127 recorded. The plan menu takes it at rest with `--color-orange-press` on hover, so it still darkens on hover, which is the one thing its own build note was written to fix. The third choice card's button takes it as the fill behind its white label; the card's own accent is untouched.

**Kain's S127 Quiet ruling is not weakened and his S122 colour ruling is not weakened.** The seven cards are still outlined, the Pass is still the only solid button in the block of eight, and the four choice cards keep the four distinct colours. Only the orange moved.

**Measured after, not only before.** axe 4.10.2 against the rebuilt page: zero WCAG 2.2 AA violations, on the detail run and on the gate run that wrote the record. The §7 line now reads `not run` rather than `pass`, which is correct and not a regression: the chapter is split, and DSRD 6 §7 says "A clean scan is the floor, never the pass". Its hand half is still owed.

## The part that is bigger than this page, and is an ASK inside a RULING

**DSRD 7 contradicts itself on the resting colour of a text link, and every page's §7 line depends on which half wins.**

Its colour section, quoted: "**AA-safe orange:** #B8460F ... the orange for SMALL text: body-copy links, overlines, breadcrumb current page, small button labels, heading accent words ... Brand orange #ED6922 is 3.16:1 on white and fails AA below large-text size."

Its S263 hover ruling, quoted: "A link rests in brand orange #ED6922 with its 1px underline and darkens to #B8460F on hover; the underline does not change ... it applies site-wide to every in-body and in-component text link."

Both cannot hold. The second puts every resting body link on the site at 3.16:1, which the first says fails AA, and which DSRD 6 §7 fails a page for. The plan menu on this page was built to the second, faithfully, with both sentences quoted in its own build note; it moved to the first today on Kain's word.

Code never edits a DSRD, so this comes to you rather than being resolved in the theme. Two things follow whichever way it is ruled. Every other page's §7 line should be read as provisional until it is settled, because a clean axe run on a page with few links proves less than it appears to. And if the ruling goes the AA-safe way, the change is a token swap in one place rather than a sweep, which is worth knowing before it is scoped as one.

## OWED BACK

The S128 ruling written into DSRD 7's colour section and DSRD 8's button rows, so the pricing page's three controls are recorded rather than living only in the theme. And a ruling on the link-colour contradiction, with the losing sentence struck in DSRD 7 rather than left to be found again.

*No em or en dashes in this file; checked before writing.*
