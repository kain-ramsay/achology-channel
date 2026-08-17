# RULING and SHIP: the member cards go two across on tablet, and the odd card fills the row

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Filed under harness Rule 14**, which requires a ruling Kain gives in session to be
acted on and filed the same session, quoting his words, so you write it into the
owning document.
**Shipped:** v0.38.14, deployed to achologytest.com, verified at all three widths.

## The ruling, in his words

> "On the member testimonials page, at the tablet responsiveness breakpoint, the
> member testimonial card shift from three cards on a line, to one per line, which
> doesn't look great. I think this should be two per line on tablet, and 1 per line
> only on mobile device view... Also, on tablet, it'll be fine for the bottom, ninth
> member testimonial card to be full container width, but only to not leave us with
> unnecessary white space."

## What was actually wrong, measured before changing anything

`.lite-grid`, the circular member card grid, carried **one column below 1024px and
three above it, with no tablet tier at all**. So a 768px viewport showed a single
narrow column with white space either side, which is what he saw.

Worth noting for the record: `.tm-cards`, the question-filtered testimonial grid on
the same page, was already correctly tiered and is untouched. The fault was in the
member voices block only.

## What it does now

| width | columns | the nine cards |
|---|---|---|
| below 768px | 1 | nine single rows, all equal width |
| 768px to 1023px | 2 | four rows of two, then the ninth at full container width |
| 1024px and above | 3 | a clean three by three, ninth card the same width as the rest |

**The full-width last card is conditional, not hardcoded.** The rule is
`:last-child:nth-child(odd)`, so it applies only when the card count is odd. Add a
tenth member and it stops applying by itself, with nothing for anyone to remember.
That is the whole of his "only to not leave us with unnecessary white space".

The tablet range is closed at 1023px so the span cannot leak into the three-column
tier, where nine cards already fill the grid exactly.

## Where the rule lives, and why

**`components.css`, not `testimonials.css`.** `.lite-grid` is the block's one home
under DSRD 3 §2.6, and a page-local copy in the page's own stylesheet is precisely
the defect that rule forbids. `achology_member_voices()` is called only by
`page-testimonials.php` today, so the change reaches one page, but the rule sits
where the block lives so a second page using it inherits the right behaviour.

**For DSRD 8:** the member voices component's responsive tiers are now 1 / 2 / 3 at
the DSRD 7 §4.1 boundaries, with the conditional full-width last card. Please write
that into its entry.

## Verified on the rendered live page, all three widths

- **1174px:** three columns, rows of 3, 3, 3, every card 293px. Unchanged.
- **768px:** two columns, rows of 2, 2, 2, 2, 1. First card 336px, last card 704px.
- **375px:** one column, nine rows, every card the same width.

`css_gate components.css`: PASS.

*No em or en dashes in this file; checked before writing.*
