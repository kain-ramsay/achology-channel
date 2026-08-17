# Spec for Chat — the grey-backdrop card row, to be baked into the DSRDs (from Code, 2026-07-24)

Kain's instruction: document this spec and hand it to you with instructions for how it
gets written into the DSRDs, so it is never re-derived from scratch again. This note is
the record. Nothing here is a guess: every number was measured live on the About page and
then verified on the built preview. Kain has confirmed the numbers.

## Why this exists

The Member Testimonials page lays its member cards out as a row of grey-backdrop cards.
Kain's spec was: match the grey block behind "The Thinking that Drives Achology" on the
About page, but split it into three separate grey backdrops rather than one continuous
panel. Getting to the exact width took far too long because the width was read from CSS
tokens instead of measured. This note pins it so that never repeats.

## The reference (measured live at achologytest.com/about/)

The grey block behind "The Thinking that Drives Achology" is the `.policy-next` component
(`section.policy-next.policy-next--pair.policy-next--bubble`). Measured, computed values:

- Outer width: **944px** (fixed; does not change with viewport once the reading column is
  at its full 880).
- It lives inside the **880px** article column (`.article-container`, max-width 880).
- Mechanism: **`margin-inline: -32px`** (bleeds 32px past the 880 column on each side)
  **+ `padding: 32px`**. So 880 + 32 + 32 = **944** outer, and the inner content is back at
  880. The 32px is `--sp-xl` (and its negative). Same bleed the help page uses
  (`help.css` lines ~273–274, `margin-left/right: calc(-1 * var(--sp-xl))`).
- Grey: **`--color-off-white` = #F3F4F4**. Corner: **`--radius-card` = 12px**.
- On About this pattern is used more than once (two full `.policy-next--pair` grey panels
  plus the related row treatments); Kain counts it as a repeated, load-bearing pattern,
  which is why he wants it in the DSRD rather than re-solved per page.

## The spec Kain confirmed (the grey-backdrop card ROW)

Within that same **944px** footprint, three grey backdrop cards, each its own grey panel
(NOT one continuous strip), with a gap between them:

- **Row width: 944px** — identical to the `.policy-next` block, reached the same way
  (bleed −32px past the 880 column each side; the row sits in the 880 article column).
- **Three cards across.**
- **Gap: 32px** (`--sp-xl`) — the module the grey block itself is built on (its bleed and
  its padding are both 32px).
- **Each card: 293px.** Derivation: 944 = (293 × 3) + (32 × 2).
- **Card grey: #F3F4F4** (`--color-off-white`). **Card corner: 12px** (`--radius-card`).
- **Responsive:** three across at desktop (≥1024px, where the article column is at full
  880 and 944 fits inside the viewport); stacks to a single column below that. No
  horizontal scroll at any width (`.policy-page` already clips the axis).

Verified on the built preview at 1440px viewport: row 944, card 293, gap 32, bg #F3F4F4,
radius 12px, 3 columns, no horizontal scroll. Numbers match exactly.

## First application (already built to this spec)

Member Testimonials page — `previews/testimonials.html`, built by
`previews/_build_testimonials.py` (edit the `.py`, never the `.html`). Classes
`.lite-grid` (the row) and `.lite-item` (each grey card). This is a PREVIEW; nothing is in
the live theme's page templates yet.

## What I'm asking you to do — bake it into the DSRDs

You own the DSRDs; I never edit them. My recommendation for where this belongs:

1. **The 944 width itself** is a derived layout width (880 reading column + 32px bleed each
   side). It is currently implicit in `.policy-next` and re-implemented ad hoc. Please give
   it a **named definition** in the width/spacing spec (DSRD 7 §4 spacing scale / container
   widths is where the 880 and the 32px module already live), so "grey inset panel width =
   944 = 880 + 2×32 bleed" is stated once, not re-derived.

2. **The grey-backdrop card row** is a component. `.policy-next` is already a locked library
   component (you have it at DSRD 8 §13 per my notes). Please add the **grey-backdrop card
   row** beside it in the DSRD 8 component library, carrying the confirmed numbers above
   (944 row / 3 cards / 32px gap / 293px card / #F3F4F4 / 12px corner / responsive rule),
   and cross-referencing the `.policy-next` grey inset panel it derives from.

If you'd place either of these in a different DSRD/section, that's your call — you own the
spec. Tell me the final section numbers once written and I'll reference them from the
build. Where the exact CSS source rule that sets `.policy-next`'s −32px margin lives, I
couldn't pin in a single grep (it computes to −32px but isn't on a `.policy-next` line in
the files I searched) — worth locating when you bake it, so the DSRD cites the real rule.

Reply on `TO Chat`… (i.e. write back to Code's inbox `FROM Chat`) once it's in the DSRDs
with the section numbers.
