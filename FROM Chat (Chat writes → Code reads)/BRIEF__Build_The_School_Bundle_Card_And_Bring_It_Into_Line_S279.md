# BRIEF: build the school bundle card, and bring it into line with the approved course card

**DOCUMENT TYPE:** approved brief. Not a page spec. Kain approved the direction in the side panel, Session 279, 17 August 2026.
**Type line added S281**, closing Claude Code's `REFUSAL__The_Two_S279_Card_Briefs_Carry_No_PAGE_GATE_Line_S063`. His refusal was correct on its own terms: the S264 intake tripwire exempts one phrase, `not a page spec`, and this brief did not carry it, so the tripwire read it as a page spec and required a PAGE GATE line it could not have. **This brief commissions component work and specifies no page**: it corrects a stylesheet and commissions a renderer, and names no page's blocks, order or copy. The exempting phrase is now above and the waiver row can come out.
**Board card:** "Cards + Chrome Sweep: Review all Unreviewed Components + give each a Prototype + Data File".
**Reads with:** `SWEEP_SHEET__The_Four_Commerce_Cards_Measured_S279.md`, beside this file, which measured all four commerce cards against the four standards the course card settled.
**The rendered artefact:** `RENDER__Course_Card_Versus_Bundle_Card_S279.html`, beside this file. Three tabs. Tab 3 is the baseline this brief describes, and it is the thing to build against, not this prose.

---

## Why this exists

The school bundle card has a stylesheet and no live component. `page-cards.php` says so on its own face, and S061 confirmed it against the live database. So it could not be judged in Safari, because there was nothing to open. Under the two-surfaces rule that puts it on Chat's side: rendered in the side panel, ruled there, built afterwards.

Kain looked at three tabs this session: the approved course card, the bundle card as its stylesheet draws it today, and the bundle card corrected. **He approved the corrected version as the build baseline** with two things still open, named at the end of this brief.

## What the card is, and where its facts come from

Nothing in the card is authored. Every value is read from a document:

| Element | Source |
|---|---|
| School name | DSRD 8 section 8.9, the bundle-card name table |
| Students, teaching hours, average rating | DSRD 5 section 2 |
| Course checklist and per-course hours | DSRD 5 section 3, maximum five items per card whatever the bundle size (DSRD 8 section 8.5) |
| Course names on the checklist | DSRD 5 canonical names with the leading article removed (DSRD 8 section 8.5, article removal rule) |
| Bundle price, anchor price, saving | DSRD 8 section 8.7, the bundle pricing reference |
| Summary strip wording | DSRD 8 section 8.6 |
| Checkout destination | DSRD 4 section 1.2 |

## The seven corrections, each one taking the course card's already-approved answer

1. **Picture area.** The dark grey slab goes. The header becomes white with the school colour at a whisper behind the hero, exactly the course card's `.card__image-gradient`: `linear-gradient(to top, rgba(var(--school-accent-rgb), 0.13) 0%, rgba(var(--school-accent-rgb), 0.07) 35%, rgba(255,255,255,0) 100%)`. The dark base gradient and the `::before` overlay are both removed. Kain ruled the whisper on the course card at S060 after saying the coloured backgrounds did not feel like Achology, and two cards in one grid cannot answer that differently.

2. **The hero fills the frame.** `object-fit: cover`, full width and height, no crop offset and no scale, matching the course card after its S060 correction. The `max-width: 78% / max-height: 88% / object-fit: contain` float goes.

3. **The house icon.** Takes `var(--school-text)` rather than brand orange, and takes the course card's alignment: `align-self: baseline` with `position: relative; top: 1px`. The academy line's `line-height` moves from 1 to 1.6 so the baseline alignment has the same line box the course card's rule was measured against.

4. **Stats line colour.** Moves from `var(--school-text)` to `var(--color-soft-grey)`, matching the course card. The stat icons stay brand orange.

5. **School name size.** 20px to 18px at weight 600, line-height 1.35, which is the course title's ruled treatment and is on the nine-step scale. 20px is not a step.

6. **The guarantee.** The shield icon and the longer line go. It becomes the course card's grey pill: Source Sans 3 11px/600, `--color-mid-grey` on `rgba(138,145,153,0.10)`, padding 3px 10px, radius 12px, reading **Money Back Guarantee**. It sits below the price row with 10px above it. The save badge stays where it is, because only bundles carry one.

7. **Both washes go.** The hour pill loses its 10 per cent tint and its pill padding, becoming plain text in `var(--school-text)`. The summary strip loses its 8 per cent tint and takes a 1px `--color-hairline` above and below instead, with its text in `var(--school-text)`. This closes the two sites your S061 sweep measured and correctly left open: school-coloured text on a tint of its own colour lands at 4.03 to 4.26 against a bar of 4.5, and the text-safe token cannot rescue it because the tint lifts the ground at the same time. Removing the tint is what makes the token work, and all seven schools then pass.

**The rule this settles, so it never comes back per card:** school-coloured text never sits on a tint of its own colour. No second token step is added. **DSRD 8 sections 8.2, 8.4, 8.5, 8.6, 8.7 and 8.10 were all corrected in this same session**, so the document and this brief agree; DSRD 7 section 2.1 gains the same rule in Chat's next pass.

## What is asked of Code

1. **Build the component.** `.card--bundle` needs a renderer of its own, the same shape as `achology_course_card()`, reading the seven bundles from their sources above. Once it exists it renders on the card sheet page like every other card, and the "Registered, but with no live component" entry for section 8 comes off.
2. **Apply the seven corrections to `cards.css`.**
3. **Correct the stale line on the card sheet:** its section 14 entry says the review card has no CSS and no template. It has both, in `reviews.css` and `page-reviews.php`.
4. **Return the rendered page through TO Chat** for Kain's Safari sitting, with its DSRD 6 record.
5. **Then export the approved state as the prototype** and write its component data file, per Harness Rule 14. The panel render beside this brief is the baseline, not the signed record: the signed record is the Safari export, because that is where Kain will settle the two open items below.

## Two things Kain has deliberately left open, to rule in Safari

He named both himself, and both need the card on a real page before they can be answered:

- **Too many words in the blocks.** The card carries an academy line, a school name, three stats with labels, five course names with hour figures, a summary strip, a price, an anchor price, a save badge and a guarantee. He wants to see it in place before deciding what comes out.
- **The bottom of the card is overloaded.** Price, anchor, save badge, guarantee pill and two buttons stack up in a small space. Same answer: he will rule it on the page.

**Build it whole as specified above.** Do not pre-trim it, and do not offer a lighter version alongside: he is judging the full card first and cutting from it, which is the opposite job.

## Two things Code should raise rather than solve

- **The save badge wording is Claude's fill.** No wording is recorded for it anywhere. It reads "Save 24%" and so on, written as a percentage to match the Access All Areas pill in DSRD 4 section 13. Kain rules the final wording in the Safari sitting.
- **The academy line now reads "Academy of Modern Applied Psychology"**, settled and written into DSRD 8 section 8.4 in this same session. It had read "Academy of Applied Psychology", which drops a word from the academy's own name; the canonical form is the one in DSRD 2 section 2.24's locked term register. Build the full name. **If it will not sit on one line at 350px, do not trim it: report the measurement through TO Chat and Kain rules a short form, which is then recorded in DSRD 8 rather than living in the theme.**

## One dependency Kain owns

**The seven school hero images do not exist at the slot size.** Filling the frame means artwork drawn to the slot's exact shape, the same job Kain did for the 28 course heroes at S060: 1056 by 555, transparent, downscaled to 704 by 370 on placement. Until they exist the picture area renders as it can, and that is not a fault to chase. Everything else on the card is buildable today.

*No em or en dashes in this file; checked before writing.*
