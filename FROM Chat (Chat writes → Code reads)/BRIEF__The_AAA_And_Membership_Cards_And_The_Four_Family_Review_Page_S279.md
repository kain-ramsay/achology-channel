> **CODE DISPOSITION, S085: WAITS ON** Kain's Safari sitting on the four-family review page. Job one is built (commerce-cards.php) and job two exists as card-review.php; the two open items, the busy blocks and the copy, are his to rule on the real page.

# BRIEF: bring the Access All Areas and membership cards into line, and build the four-family review page

**DOCUMENT TYPE:** approved brief. Not a page spec. Kain approved the corrections in the side panel, Session 279, 17 August 2026. Type line completed by Chat at S282 on Code's S063 refusal: both halves of this brief are component work, and the four-family review surface is an internal workbench view rather than a site page. Reasoning in `ANSWER__Both_S279_Briefs_Are_Component_Work_S282.md`.
**Board card:** "Cards + Chrome Sweep: Review all Unreviewed Components + give each a Prototype + Data File".
**Reads with:** `BRIEF__Build_The_School_Bundle_Card_And_Bring_It_Into_Line_S279.md`, beside this file, which covers the school bundle card. **Build both together.** The two briefs share one review sitting.

---

## Why this exists, and what it replaces

Three of the four remaining commerce cards, the Monthly membership card, the Annual membership card and the Access All Areas Pass card, have stylesheets and no live component, exactly like the bundle card. `page-cards.php` names all three under "Registered, but with no live component". So none of them has ever been rendered, and none has ever been reviewed.

Chat rendered all three in the side panel beside the approved course card. Kain approved the corrected versions as the build baseline, with the same two items open that the bundle card carries.

**No separate panel render travels with this brief, deliberately.** The nine corrections below are given as exact values, and the review page you are asked to build in job two supersedes any panel file as the artefact Kain rules on. A second HTML in the channel would be a second copy of one truth.

## The nine corrections

**Three are the same corrections the bundle card took, applied to all three cards.**

1. **Product name size.** `.card--aaa .card__name` and `.card--membership .card__name` move from `20px/700` to `18px/600`, `line-height: 1.35`. That is the course title's ruled treatment and it is on the nine-step scale; 20px is not a step.

2. **Stats line colour.** `.card--aaa .card__stat` and `.card--membership .card__stat` move from `var(--color-dark)` to `var(--color-soft-grey)`, matching the approved course card. The stat icons stay brand orange.

3. **The academy line's house icon.** On all three cards it takes `align-self: baseline` with `position: relative; top: 1px`, and the line's `line-height` moves from `1` to `1.6` so the alignment has the same line box the course card's S060 rule was measured against. The icon colour stays brand orange on these three: they carry no school, so there is no text-safe colour to take.

**Five are colour faults, and three of them are the tint rule ruled at S279.**

4. **The Access All Areas course-count pills.** `.card--aaa .card__course-count-pill` currently takes `var(--school-accent)` on `rgba(var(--school-accent-rgb), 0.10)`, which is school-coloured text on a tint of its own colour, seven times over. Corrected: `color: var(--school-text)`, `background: transparent`, `padding: 0`. Same fix, same reason as the bundle card's hour pill.

5. **The Annual card's summary strip.** `.card--membership--annual .card__summary-strip` takes `rgba(237,105,34,0.08)` with `var(--color-orange)` text: brand orange on a tint of brand orange. Corrected: `background: transparent`, `border-top` and `border-bottom` of `1px solid var(--color-hairline)`, text `var(--color-orange-link)`.

6. **The Annual card's price pill.** `.card--membership--annual .card__price-pill` takes `var(--color-orange)` on `rgba(237,105,34,0.10)`: the same fault again. Corrected: `color: var(--color-orange-link)`, `background: rgba(138,145,153,0.10)`, which is the tint the Monthly card's pill already uses.

7. **The Annual card's Included pills.** `.card--membership--annual .card__included-pill` takes `var(--color-orange)` at 10.5px. Brand orange measures 3.16:1 on white and fails the small-text bar; DSRD 7 section 1 has reserved `--color-orange-link` #B8460F for exactly this since S248. Corrected: `color: var(--color-orange-link)`.

8. **The Monthly card's overline.** `.card--membership--monthly .card__overline` takes `var(--color-orange)` at 13px. Same failure, and 13px is not a step. Corrected: `color: var(--color-orange-link)`, `font-size: 12px`.

**One is the guarantee, matched across the family.**

9. **The Access All Areas guarantee.** `.card--aaa .card__guarantee` is a plain 13px line reading "100% Money Back Guarantee". Corrected: it takes the course card's grey pill, `Source Sans 3 11px/600`, `--color-mid-grey` on `rgba(138,145,153,0.10)`, padding `3px 10px`, radius `12px`, reading **Money Back Guarantee**, with `margin-top: 10px` on the wrapper. The same change the bundle card took.

**The two membership cards carry no guarantee, and that is correct rather than missing.** DSRD 4 section 1.4: no refunds on community subscriptions, cancellable at any time. Do not add one.

## Three things deliberately left alone, so nobody "fixes" them later

- **The three headers stay exactly as they are.** The pale Monthly gradient, the orange Annual gradient and the dark Access All Areas slab are the documented three-tier personality system (DSRD 8 sections 9.1 and 10.1), not drift. They carry no hero artwork, so the course card's picture rules do not reach them. This is the one place the bundle card's header correction does NOT generalise.
- **The remaining off-scale sizes belong to the type scale sweep.** By name: the 26px header titles, the 12.5px stats, the 13px feature and school-name lines, the 10.5px pills, the 20px price qualifiers, the 13px price sub-lines, and the product section block's 32px heading. That sweep is its own signed brief across the whole theme (`BRIEF__Type_Scale_Sweep_S270.md`) and pulling them in here would be the while-I-am-in-here problem.
- **The Annual card's 14px/700 overline** stays at 14px: it is on the scale, and its extra weight is a ruled personality signal (DSRD 8 section 10.1).

## Job one: build all four components

`.card--bundle`, `.card--aaa`, `.card--membership--monthly` and `.card--membership--annual` each need a renderer, the same shape as `achology_course_card()`, reading their facts from the documents that own them: DSRD 5 sections 2 and 3 for the bundles, DSRD 8 sections 9 and 10 for the AAA and membership content, DSRD 4 sections 1.2 to 1.4 and 13 for prices, checkout URLs and CTA labels. Nothing authored. Once they exist, the four "Registered, but with no live component" entries come off the card sheet.

Apply the seven bundle corrections from the other brief and the nine above in the same pass, then `css_gate` and `component_gate`.

## Job two: the four-family review page, which is Kain's own ask

**He wants one page where he can flip between the four card families and edit them against each other, with the course card always available as the reference.** His words: tab options so he can edit these cards alongside the school cards, with the course cards to compare both against.

The shape, so it is not guessed:

- **Four tabs, in this order: Course cards (approved reference), School bundle cards, Membership cards, Access All Areas.** One family on screen at a time, each occupying the identical screen position, switched by its tab. This is his standing instruction from S060, and `previews/variant_tabs.py` is the instrument for it.
- **Every card renders from its live component**, never re-authored, on the same rule `page-cards.php` obeys. If a card cannot render from its one home, the slot says so on the page.
- **Real content only.** Real courses, real schools, real prices, real feature lists. A card filled with invented content would have him ruling on writing nobody decided.
- **At least six cards per family where six exist**, at real card width, in the real grid, so he judges a populated row rather than a specimen. The bundle family has seven; the membership family has two and the Access All Areas family has one, which is simply what those families are.
- **Noindex and off the navigation**, like the card sheet.

**Two things he must be able to do on that page, because the editing is the point.** He needs to see the same block of a card across two families without scrolling between them, and he needs the tab switch to hold his scroll position, so flipping compares like with like rather than jumping him to the top. If either is impractical, say so through TO Chat before building around it rather than after.

## The two items Kain has left open, and they now cover all four cards

He named both on the bundle card and repeated them on these three:

- **The blocks are too busy.** Every one of these cards stacks an overline, a title, an academy line, a name, two or three stats, five to seven checklist rows with a tag on each, a summary strip, a price row with up to three parts, a guarantee and two buttons. He wants to see them on a real page before deciding what comes out.
- **The copy needs rethinking.** The academy lines alone read "Academy of Modern Applied Psychology", "Get FULL 28-Course Curriculum", "First Month for Seven Dollars" and "Twelve Months Subscription": one slot doing four different jobs. **This one is now settled, in this same session: see the addendum at the end of this brief.** The wider busy-ness question stands and is his.

**Build all four whole and do not pre-trim them.** He is judging the full cards first and cutting from them, which is the opposite job. Both items are ruled in the Safari sitting on the review page, and the export of that approved state becomes each card's signed prototype under Harness Rule 14.

## What Chat still owes, so you are not waiting on it

DSRD 8 sections 9 and 10 and DSRD 7's type and icon registers are being brought level with the nine corrections above in the same session as this brief. DSRD 8 section 8 and DSRD 7's school-colour, type, icon and artwork entries are already done for the bundle card. Build to this brief; the documents will agree with it.

*No em or en dashes in this file; checked before writing.*

---

## ADDENDUM, written later in the same session: the eyebrow is settled, build these words

Kain ruled the eyebrow slot as a standard rather than leaving it to the Safari sitting. **It is now DSRD 8 §11.0, and it governs all four commerce cards.**

**The rule: the small line above a product's name names the parent the product belongs to, and nothing else.** No price, no promise, and never a repeat of the heading below it.

| Card | Starting point, Kain rules the final wording |
|---|---|
| Course card | its school's display name. **Approved and unchanged**, ruled on the rendered card at S060 |
| School bundle card | Academy of Modern Applied Psychology |
| Access All Areas card | Academy of Modern Applied Psychology |
| Membership, monthly | The Achology Community |
| Membership, annual | The Achology Community |

**The rule binds; these words do not.** Kain ruled the rule in Chat after the research. He did not rule the wording, and he has said plainly that he writes card copy with you in Safari rather than in Chat. **So build these words as a starting point, so there is something real in the slot for him to judge, and expect him to rewrite them in the sitting.** Whatever he settles there, file it under Rule 14 as usual and Chat folds it back into DSRD 8 §11.0 as the approved wording. Do not treat the four changed lines as signed copy, and do not defend them if he wants them gone.

**Why, so it is not re-litigated.** The slot is the eyebrow, whose published job is to categorise the thing beneath it and group it with its siblings, at its most useful in exactly this situation, a row of cards. Two cautions decided the wording: it must not carry critical information, because readers skip it on a first scan, which rules out any price or promise; and it must not repeat the heading below it. The first draft of the rule had each card name its own family ("Membership" above Monthly Membership) and repeated the heading on three of four, so it was dropped. Naming the parent is non-redundant on all four and teaches the shape of the business as the reader scans.

**What this addendum does NOT touch.** The header overline inside the Access All Areas and membership headers ("All 7 Schools. All 28 Courses", "Get Started for Only $7", "12-Month Subscription"). Different slot, own job, next in the row-by-row copy pass. Build those exactly as they are.

**The method, because the rest of the copy work will run this way.** The commerce cards' copy is settled one row at a time across all five cards at once, never one card at a time: the eyebrow, then the stats, then the checklist, then the summary strip, then the price row. This is the first row settled, and it is another reason the four-family review page matters: it is the one surface where a whole row can be seen across every card in a single flip.

*No em or en dashes in this addendum; checked before writing.*
