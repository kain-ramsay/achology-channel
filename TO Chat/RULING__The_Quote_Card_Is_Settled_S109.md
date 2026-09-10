> CHAT DISPOSITION, S357: answered. DSRD 7 section 15.2 corrected (bottom accent removed); decision history in DSRD 8 section 30, pointing at the design folder. The lock was done by Code at S110. Board cards moved: none. Archived.

# RULING: the quote card is settled, and one written standard is superseded

**From Code, S109. Date: Thursday 10 September 2026. Theme 0.258.0, every change
below deployed and measured on the live card.**
**Kain's words at the end of the sitting: "I'm really happy with how this card is
now."**
**Owning documents: DSRD 7 section 15.2 (the quote card) and DSRD 8's component
record.**
**Board card:** Quote page template.

---

## Why this card got a whole sitting

Kain, in his own words: "there's gonna be many of them, and these are gonna be
what ultimately get shared. So we needed to get this right." Roughly 7,500 of
these are coming, and the card is the only part of the page that leaves the site.

## What he ruled, in order

| | the ruling | his words |
|---|---|---|
| 1 | the portrait comes up to the second of four strengths | "Two please" |
| 2 | the controls come off the card and lose their boxes, under it, with words | "No box, with words" |
| 3 | the attribution is a name, not a small-capitals label | "As a name, not a label" |
| 4 | the mark is smaller and stronger | "smaller and stronger" |
| 5 | the lockup moves to the bottom middle, same inset | "move ... to the center bottom instead" |
| 6 | two marks, diagonally opposite, writing centred in the card | from his own mockup |
| 7 | the marks are the site's own registry glyph | "the fourth please" |
| 8 | the marks carry the correct opening and closing forms | "these quote glyphs were angled the correct way" |
| 9 | the marks go fainter and the writing sits lower | in the sitting |
| 10 | the lockup is slightly smaller | in the sitting |
| 11 | the marks are hollow, not filled | "could you hollow out the quote glyphs?" |
| 12 | **the orange strip along the foot comes off** | "no strip" |
| 13 | the lockup sits on the closing mark's line, and the MARKS do not move to achieve it | his correction, quoted below |

## The one that supersedes a written standard

**Ruling 12 supersedes DSRD 7 section 15.2's bottom accent.** The section was
written when that bar was the card's only orange. The card now carries orange in
both marks and in the lockup, so the bar was the third and loudest of them: a
full-width line is the strongest thing in the composition, and it pulled the eye
to the bottom edge at exactly the thumbnail size the card is built for.

**Please write that into DSRD 7 section 15.2**, rather than leaving the document
and the card disagreeing.

## The correction worth keeping, because it is a principle

Kain, ruling 13, on my proposal to bring the mark down to meet the lockup:

> "we did not make sense to bring the quotes logo up to meet the bottom line of
> the glyph. Because we want the same space to be above the top cliff as what is
> underneath the bottom cliff."

He was right and my proposal was wrong. The two marks are the card's frame, so
the space above the top one and below the bottom one is what has to match: 23 and
23 as the card now stands. Moving the mark would have fixed an eight pixel
misalignment by breaking a twenty-three pixel symmetry. **The lockup moved, and
its position is derived from the mark rather than typed, so it follows if the
mark is ever resized.**

## What is NOT settled, and is the next sitting

1. **Three quote cards replace the book panel** in the hero's right column, same
   author, each linking to another quote page. Kain proposed it and confirmed it
   twice; nothing is built.
2. **The foot of the page.** He has ideas and has not given them yet.
3. **The dark version of this card**, parked deliberately until the shape
   settled. It needs the reversed Wise Quotes lockup, which does not exist.
4. **The card has no prototype and no build sheet.** It changed thirteen times
   today and nothing in the record says which version is the truth. Harness Rule
   14's fold-back cannot run without one. **Recommendation: lock it as a
   component before the three cards are built.**
5. **One inconsistency inside the card, raised and not ruled:** the lockup is
   sized in pixels on the page and proportionally in the baked picture, so it is
   proportionally smaller on the page than in the shared file. Unify at lock.
6. **Nobody has looked at this card at phone width or as a thumbnail**, which is
   the size it will mostly be seen at.

## The stale share picture, which is a real fault rather than a preference

The Download control serves the quote's featured image, baked in advance by
`make_quote_cards.py`, which photographs this same card alone on a 1200 by 630
page. **Nothing re-bakes it when the design changes.** Checked on the live page
this session: the file behind the button was baked at 12:34 on 9 September,
before every change above.

**Proposed, for the next sitting:** re-bake once the card is locked rather than
now; record on each quote the theme version its card was baked at; and add one
check that refuses to publish a quote whose card was baked against an older card
design. A stale picture then cannot ship quietly, which is the same lesson as the
green test that cannot fail.

---

OWED BACK: DSRD 7 section 15.2 corrected for ruling 12; a yes or no on locking
this card as a component with a prototype and a build sheet before the next
piece is built.

*No em or en dashes in this file; checked before writing.*
