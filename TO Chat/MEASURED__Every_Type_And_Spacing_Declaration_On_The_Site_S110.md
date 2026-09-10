# MEASURED: every type and spacing declaration on the site, S110

**From Code, S110. Date: Thursday 10 September 2026. Read off the theme at
0.326.0, from the stylesheets themselves with comments stripped.**
**Commissioned by Kain**, live at the close of S110: "I think we need to analyse
all of those and bring them all into alignment of this higher level altitude font
and spacing plan."

**Owning documents:** DSRD 7 section 3 (the type scale) and section 4 (the
spacing scale). **This measurement scopes the commission**; Chat's own rule from
S356 is that a measurement scoping a commission is a record, which is why it is
filed rather than reported.

---

## What Kain asked for, in his words and in the trade's

He named it himself: "a standardised typography set of rules that governs every
single typography, copy, content, infrastructure, layout and design", and then
extended it to spacing: "what amount of spacing is assigned underneath every
single font size, font weight".

**The trade calls the first half semantic type styles**, sometimes a type ramp:
named roles, each defined once as a complete recipe. **The second half is
vertical rhythm**: space held as a property of the RELATIONSHIP between two
roles rather than typed onto each element.

**What the site has is a scale. What it lacks is roles.** A scale says which
values are legal; roles say what a thing IS. Nothing anywhere on this site says
what a section heading is, so every page type decides again.

## The numbers

**Type.** 417 declarations set a size or a weight, across 18 stylesheets. The
scale declares nine steps: 12, 14, 16, 18, 21, 24, 28, 33, 42. Twenty-two
distinct raw sizes are in use, and **115 declarations sit on a step the scale
does not hold**: 11, 13, 15, 17, 19, 20, 22, 26, 30, 32, 34, 36, 40, 56, 104.
More than half of all sizes are typed as a raw number rather than drawn from the
scale.

**Space.** 1,158 declarations set a margin, padding or gap. The scale declares
seven steps: 4, 8, 16, 24, 32, 48, 64. Thirty-one distinct raw values are in use,
and **255 sit on a step the scale does not hold**, including 10px used 47 times,
12px 36 times and 20px 34 times.

**Both rules already exist in writing.** DSRD 7 section 3: "Every text size on
the site sits on a step; nothing sits between steps." Section 4: "Base unit: 8px.
All spacing uses this scale." The site breaks the first 115 times and the second
255 times. **The rules are not wrong; nothing has ever checked them, and nothing
said what a heading IS for the rule to attach to.**

## One correction to a number I gave Kain in the sitting

I told him 67 size-and-weight combinations. That counted written FORMS, so
`14px` and `var(--text-14)` were two entries. Normalised to real values there
are **48**, of which **16 are used exactly once**.

**The gap between those two numbers is itself a finding.** Nineteen styles exist
twice on this site, once as a token and once hard-typed, so changing one leaves
the other behind silently. That is a defect, not an accounting artefact.

## The thing to be careful of, and it is Kain's own work

**Some one-offs are his rulings, not drift.** The feedback buttons' full pill,
approved 2026-07-29 and deliberately outside the radius tiers. The help header's
56px, where he split the difference between 48 and 64 and confirmed it at S080.
The bubble watermark's 3px radius and hand-typed glow. A sweep that flattens
these undoes decisions he made on a render.

**So the sweep has two outputs, not one:** the roles, and a named list of
carve-outs that stay. A carve-out that is written down is a decision; one that is
merely tolerated is drift waiting to be re-argued.

## What is proposed

1. **Roles.** Collapse the 48 into ten or twelve, each carrying size, weight,
   line height and the space that follows it.
2. **Kain sees them rendered**, on a real page, one at a time, which is how he
   judges.
3. **Chat writes them into DSRD 7**, replacing the bare scales with roles.
4. **A gate check**, in `css_gate.py`, that fails an off-scale size or space the
   way it already fails an unannotated radius or colour. This is the half that
   makes it hold: both existing rules failed for want of it.

## The full inventory

Every size-and-weight pair in the theme, most used first, with the stylesheets it
appears in. A pair marked NO sits on a size the scale does not contain.

| size | weight | uses | on the scale | where it is used |
|---|---|---|---|---|
| 14 | 400 | 22 | yes | knowledge-hub.css x5, help.css x4, cards.css x3, base.css x2, ... |
| 12 | 600 | 22 | yes | cards.css x8, knowledge-hub.css x4, quote.css x3, people.css x2, ... |
| 14 | 600 | 16 | yes | components.css x3, base.css x2, cards.css x2, header.css x2, ... |
| 24 | 600 | 14 | yes | help.css x2, knowledge-hub.css x2, testimonials.css x2, base.css x1, ... |
| 11 | 600 | 14 | **NO** | cards.css x6, footer.css x2, header.css x2, knowledge-hub.css x2, ... |
| 13 | 400 | 11 | **NO** | cards.css x3, components.css x2, footer.css x2, about.css x1, ... |
| 18 | 600 | 10 | yes | cards.css x4, people.css x2, about.css x1, book-note.css x1, ... |
| 12 | 500 | 9 | yes | about.css x3, knowledge-hub.css x3, cards.css x2, base.css x1 |
| 17 | 600 | 8 | **NO** | about.css x2, cards.css x2, components.css x1, header.css x1, ... |
| 13 | 600 | 8 | **NO** | people.css x3, help.css x2, footer.css x1, header.css x1, ... |
| 33 | 700 | 7 | yes | knowledge-hub.css x3, base.css x1, book-note.css x1, help.css x1, ... |
| 16 | 600 | 7 | yes | help.css x3, base.css x2, knowledge-hub.css x1, policies.css x1 |
| 21 | 600 | 6 | yes | knowledge-hub.css x3, base.css x1, people.css x1, policies.css x1 |
| 20 | 600 | 5 | **NO** | help.css x3, global-impact.css x1, testimonials.css x1 |
| 16 | 400 | 5 | yes | knowledge-hub.css x3, base.css x1, reviews.css x1 |
| 14 | 500 | 5 | yes | components.css x2, base.css x1, cards.css x1, quote.css x1 |
| 12 | 400 | 5 | yes | base.css x2, header.css x1, knowledge-hub.css x1, policies.css x1 |
| 16 | 500 | 4 | yes | header.css x2, about.css x1, book-note.css x1 |
| 32 | 700 | 3 | **NO** | cards.css x1, help.css x1, people.css x1 |
| 26 | 700 | 3 | **NO** | cards.css x3 |
| 24 | 700 | 3 | yes | cards.css x3 |
| 15 | 400 | 3 | **NO** | about.css x1, header.css x1, reviews.css x1 |
| 15 | 500 | 3 | **NO** | cards.css x2, knowledge-hub.css x1 |
| 15 | 600 | 3 | **NO** | people.css x2, help.css x1 |
| 20 | 700 | 2 | **NO** | cards.css x1, testimonials.css x1 |
| 18 | 700 | 2 | yes | cards.css x1, course.css x1 |
| 18 | 500 | 2 | yes | people.css x1, policies.css x1 |
| 15 | 700 | 2 | **NO** | about.css x1, global-impact.css x1 |
| 13 | 500 | 2 | **NO** | cards.css x1, header.css x1 |
| 12 | 700 | 2 | yes | about.css x2 |
| 11 | 700 | 2 | **NO** | about.css x2 |
| 11 | 400 | 2 | **NO** | reviews.css x2 |
| 104 | 800 | 1 | **NO** | about.css x1 |
| 42 | 700 | 1 | yes | base.css x1 |
| 40 | 800 | 1 | **NO** | about.css x1 |
| 36 | 700 | 1 | **NO** | about.css x1 |
| 34 | 800 | 1 | **NO** | about.css x1 |
| 34 | 600 | 1 | **NO** | people.css x1 |
| 30 | 700 | 1 | **NO** | components.css x1 |
| 28 | 700 | 1 | yes | base.css x1 |
| 28 | 500 | 1 | yes | quote.css x1 |
| 22 | 700 | 1 | **NO** | footer.css x1 |
| 20 | 500 | 1 | **NO** | cards.css x1 |
| 19 | 600 | 1 | **NO** | about.css x1 |
| 19 | 700 | 1 | **NO** | footer.css x1 |
| 19 | 400 | 1 | **NO** | help.css x1 |
| 14 | 700 | 1 | yes | cards.css x1 |
| 13 | 700 | 1 | **NO** | cards.css x1 |

## The 16 combinations used exactly once

| size | weight | on the scale | the one selector that uses it |
|---|---|---|---|
| 104 | 800 | **NO** | `.odo-strip span` (about.css) |
| 42 | 700 | yes | `.type-hero` (base.css) |
| 40 | 800 | **NO** | `.cons-count__num` (about.css) |
| 36 | 700 | **NO** | `.m-stat` (about.css) |
| 34 | 800 | **NO** | `.story-proof__num` (about.css) |
| 34 | 600 | **NO** | `.ap-avatar` (people.css) |
| 30 | 700 | **NO** | `.ach-rule__mark` (components.css) |
| 28 | 700 | yes | `.type-stats-large` (base.css) |
| 28 | 500 | yes | `.qp-hook p` (quote.css) |
| 22 | 700 | **NO** | `.cta-title` (footer.css) |
| 20 | 500 | **NO** | `.card--membership .card__price-qualifier` (cards.css) |
| 19 | 600 | **NO** | `.policy-body p.founders-sign` (about.css) |
| 19 | 700 | **NO** | `.cmplz-cookiebanner.achology-consent-bar .cmplz-title` (footer.css) |
| 19 | 400 | **NO** | `.help-hero__lead` (help.css) |
| 14 | 700 | yes | `.card--membership--annual .card__overline` (cards.css) |
| 13 | 700 | **NO** | `.card--aaa .card__overline` (cards.css) |

---

OWED BACK: nothing yet. This is the evidence the commission is scoped from. The
proposed roles come to Kain rendered before anything is written into DSRD 7.

*No em or en dashes in this file; checked before writing.*
