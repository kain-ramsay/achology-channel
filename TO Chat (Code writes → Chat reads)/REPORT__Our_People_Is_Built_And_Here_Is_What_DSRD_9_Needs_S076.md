# REPORT: Our People is built and approved. Here is every value the DSRD 9 layout spec needs.

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Board card:** "Our People: publish the six approved Eldership biographies and write the page's layout spec".
**Kain asked for this file directly**, so you can close the card's last to-do: *write the Our People page layout specification into DSRD 9, owed since S062 and never started.*

**The biographies half is complete.** Everything below is the other half's raw material, read from the theme this session rather than recalled, so you can write the specification without a round trip.

---

## What is now live at /about/instructors/, theme v0.81.0

Four sections, in this order. **The order changed this session**, on Kain's instruction: the Eldership moved above the Editorial Squad.

| # | Section | Heading | People | Treatment |
|---|---|---|---|---|
| 1 | Management Team | Achology Management Team | Karen A. Ramsay, Kain Ramsay | row |
| 2 | Guest instructor | *none, by S062 ruling* | Prof. Gerard Egan | grey panel |
| 3 | Community Eldership | Achology Community Eldership Team | six elders | cards |
| 4 | Editorial Squad | The Achology Editorial Squad | eight pen names | cards |

Sections are addressed in CSS **by position, not by a class of their own**, because the template builds them from a list and their order is the page's meaning. `nth-of-type(-n+2)` is the rows, `nth-of-type(2)` is the guest panel, `nth-of-type(n+3)` is the cards. **If a fifth section is ever specified, this block is what has to be revisited, deliberately.**

## The composition, and the reasoning behind it

Kain's S062 ruling, unchanged: **volume falls as the page descends.** The people who lead the academy are read, the instructors are met, the editorial team and the eldership are scanned. That is why one page carries three treatments rather than one.

## Treatment 1: the rows (sections 1 and 2)

- Grid: one column, `row-gap: 0`, separator drawn **between** rows (`li + li` border-top) so a rounded hover is not cut by a line at its foot
- Card: `padding: 24px`, `margin: 0 -24px`, `border-radius: 12px`, hover fill `--color-off-white`
- Portrait: **128px** circle
- Name: **24px**, weight 600
- Role: **16px**, `--color-orange-link`, margin-top 4px
- Biography: **16px**, line-height 1.7, `--color-dark`, shown in full

**The role line is one size across both row sections**, ruled by Kain at S062: the guest panel's subline had to match Karen's and Kain's, so theirs grew from 12 and his shrank from 18, meeting at 16, which is a step on the approved scale.

## Treatment 2: the guest panel (section 2 only)

Sits inside treatment 1 and adds a tint. **Built to DSRD 7 §4.4's full-bleed panel rule**, nothing invented:

- Background `--color-off-white`, `border-radius: 12px`, padding **32px**
- At **1040px and above**, `max-width: calc(880px + 2 * 32px)` = **944px**: the 880px article column plus a 32px bleed each side
- The row inside contributes **no padding of its own**. One set of padding, not two
- No section heading: with one person in the panel a heading repeats the line beneath it, so his name takes its size instead at **28px**
- The row's hairline is removed; the panel's own edge is the boundary

**A caution worth carrying into the spec**, because it was got wrong once and Kain caught it on the rendered page: the panel is centred by the page's auto margins, so widening its ceiling is the whole mechanism. Setting `margin-inline` instead replaces those auto margins and slides the panel 112px left while still measuring the correct width. **Measuring width alone does not catch it; position has to be checked too.**

## Treatment 3: the cards (sections 3 and 4)

**This is the part that changed today**, ruled by Kain at S296 on a rendered before-and-after comparison.

- Grid: **two columns**, `gap: 24px`, collapsing to one column at **1023px and below**
- Card: white, `1px solid --color-hairline`, `border-radius: 12px`, `--shadow-card`, `padding: 28px 24px 24px`, `height: 100%`
- Hover: `--shadow-card-hover` and `translateY(-3px)`, both withdrawn under `prefers-reduced-motion`
- The row arrow is hidden on cards

**The card's internal layout, as ruled today:**

```
grid-template-columns: auto minmax(0, 1fr)
column-gap: 16px      row-gap: 2px      align-items: start

  portrait  | name          <- 72px circle, spans rows 1 and 2
            | role
  biography (full width, row 3, margin-top 16px)
```

- Portrait **72px**, `grid-row: 1 / span 2`
- Name **21px**, row 1, `align-self: end`
- Role row 2, `align-self: start`
- Biography spans **both columns**, row 3, **no clamp**
- `.pp-card__text` takes `display: contents` so its three children become items of the card's own grid. **No markup change, and source order is untouched, so a screen reader reads it exactly as before.**

**Two across, not three.** Three cards in the 880px column give each 277px, which breaks the longer names onto two lines and the roles onto three, and the rows stop lining up. Rendered both ways before choosing.

## Why the card layout changed, since the spec should record it

The portrait used to sit **above** the name in a column, which left the biography whatever height remained and clamped it to three lines. All fourteen cards therefore stopped mid-sentence on an ellipsis. Kain saw it and asked for the name and subtitle to sit on the same line as the top of the image, as one design across all of these cards.

**It is not a new arrangement.** It is the phone layout he approved at S062, promoted to every width. So the change **deleted** the 767px block that used to hold it rather than adding a second design: the page now has one card shape where it had two and a rule to switch between them.

Measured on the rendered page at 1440px, before and after: the biography needed **105px** and was given **63px**; it now gets all 105, and the card is **247px** tall against **287px**. More words in less height.

## The one stack-point exception this page carries

`.pp-card` wraps at **640px**, which is **approved stack-point exception 4 of 5** under DSRD 7 §4.5 as amended at S252, approved by Kain. Worth naming in the spec so a later audit does not read it as an arbitrary breakpoint.

## Tokens, so the spec quotes rather than restates

12px, 14px, 16px, 18px, 21px, 24px, 28px are `--text-*`. Spacing 16 / 24 / 32 / 48 is `--sp-md` / `--sp-lg` / `--sp-xl` / `--sp-2xl`. Card grid gap is `--grid-gap` (24px). Card corner is `--radius-card` (12px). Reading column is `--container-article` (880px).

## Two things the spec should record as open, not as built

1. **§1 still fails on two bare acronyms in role lines**: CTO in Kain Ramsay's, TAYA in Isabella S. Whitmore's. Both are registry strings and both are with Kain.
2. **The links field was withdrawn.** Built, then removed the same session on his ruling that none of the six elders has a link to give. The shape reasoned through is recorded in `BRIEF__The_Six_Eldership_Biographies_S296.md` Part Two if it ever returns.

## What is complete on the card's first half

Six biographies live in Kain's own words, rewritten twice by him in session (see `RULING__Kains_Revised_Eldership_And_Book_Research_Biographies_S076.md`, and note that "community" was dropped from all six in a later pass, so they read "Achology's elders"). The unapproved-copy warning is gone from `people-setup.php`. Gabriele's name and photograph both resolve. Benjamin Lockwood's biography was revised in the same sitting.

**One small thing left open and named rather than fixed:** Benjamin's `line` field, the one-sentence form his book-note signature block renders, still reads "distilling each catalogued book" while his biography now reads "distilling each book". Kain's rewrite covered the biography only, so the line was left rather than edited on his behalf. Raised with him; not yet ruled.

*No em or en dashes in this file; checked before writing.*
