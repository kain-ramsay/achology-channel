**DISPOSITION (S280, Chat):** folded. Kain's Safari ruling reached the record: DSRD 7 section 2.1's second clause (a school colour used as a fill still governs the contrast of any text sitting on it) was written at S279 from this finding. Archived.

# RULING: the Learn More hover fill takes the school's text-safe colour

**DOCUMENT TYPE:** ruling, given by Kain in session. Filed under Harness Rule 14.
**From:** Claude Code, Session 061. **Date:** 17 August 2026. **Theme:** v0.63.5.
**Board card:** "School Colour Text-Safe Sweep: Every School Colour Carrying Text Moves To Its AA Token".

---

## Kain's words

Shown the two fills tabbed on the rendered live page, he ruled:

> "Yes, I like it!"

## What he ruled on, and where

The live book note page for Man's Search For Meaning, its own real related-courses row, opened in Safari at his machine. The Learn More buttons were held in their hovered state in both tabs, because a hover is gone the moment the mouse moves and he cannot judge what he has to chase. That was the only departure from what a visitor sees, and it was written on the page itself rather than left for him to find. The resting state was identical in both tabs and untouched.

Two tabs, same screen position, one thing different:

- **As it is now.** White label on the school's primary colour.
- **Corrected.** The same button filled with that school's text-safe colour, the border moving with the fill.

## What it changes

`.card--course .btn--learn-more:hover` and `.card--bundle .btn--learn-more:hover` now take `var(--school-text)` for both `background` and `border-color`. The resting outline keeps `--school-accent`.

## Why it came up, since it is not where anyone was looking

The S277 sweep went hunting for school colours on text properties. This one is not on a text property at all: the colour is the fill and the label is white, and contrast does not care which of the two moved. White on the seven primaries measures **3.23 to 5.44** against a bar of **4.5** for a 14px label at weight 600, so **five of the seven schools were failing on every hover**, on live pages, today: CBP, Life Coaching, Person-Centred, Mental Health and Personal Growth. NLP and Mindfulness passed as drawn and are unchanged either way.

Darkening the fill to the text-safe token clears all seven, at 4.53 to 5.44.

**The option that was measured and deliberately not offered:** keeping the primary fill and putting a dark label on it. Brand dark on the primaries lands at **1.93 to 3.24**, worse than what was already there. Offering a failing option as a choice is how a ruling gets made on something that cannot ship, so it was measured first and dropped. Recorded here so nobody proposes it again.

## The fold-back, per Rule 14 as tightened at S258

Both writes were made in the same session as the ruling, and this file names them:

1. **`course-card/achology-course-card-proof-v2.html`**, the prototype's next version, exported from the rendered page at v0.63.5 with stylesheets inlined. It supersedes v1 for this one ruling; everything else in it is v1 unchanged. The CSS is live inside the file, so **hovering a button in the prototype shows the ruled state** rather than describing it beside itself.
2. **`course-card/COMPONENT_DATA__course-card.json`**, updated to match: record version 2, the status block naming prototype v2, and the Learn More entry rewritten to the ruled behaviour.

The Card System README is updated in the same sitting: the course card's row added to the signed records table, and the still-to-review list down from five to four.

The hover fill goes into that data file's `not_checked_and_why` block rather than into its checks, with the reason stated rather than implied: the value is bound per school, so one expected value would be wrong for six of the seven, and it exists only under `:hover`, which a computed style read on a resting specimen page cannot enter. What was proved instead is that the deployed rule and each card's resolved `--school-text` read correctly off the live page at `ver=0.63.5`.

`component_gate` on the course card after the change: **56 passed, 0 failed.** `css_gate`: **PASS on all 15 stylesheets.**

## What Chat is asked to do with it

Record the ruling in DSRD 8 section 7 as decision history.

DSRD 7 section 2.1 needs no correction and is what this was decided against: "`--school-accent` for fills, bars and decorative marks; `--school-text` for anything a reader reads." **One added clause may be worth it when Chat next has that section open**, because this ruling turned on a case the sentence does not quite reach: a school colour used as a FILL still governs the contrast of any text sitting on it, so the accent is not automatically safe merely because it is not on the text. That is Chat's to word, not mine, and it is raised rather than assumed.

*No em or en dashes in this file; checked before writing.*
