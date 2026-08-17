# REPORT: before the deletion pass is commissioned, four things

**From:** Claude Code, Session 054. **Date:** 2026-08-11. **Theme:** v0.60.12.
**Why this exists:** Kain asked what Chat needed to know before I ran the testimonials.css deletion pass. Answering it properly turned the job from "one page's dead stylesheet" into something that would have destroyed real work if it had been commissioned as first described. Nothing has been deleted.

## 1. DSRD 7 names three blocks that do not exist

Section 5.3, quoted from the canonical file this turn:

> "**Stage panels: 16px** (named S223). The large tinted or dark full-width blocks: About's `.fa-act--tint`, `.fa-act--dark`, `.cons-stage`, `.story-proof` and the closing enquiries panel (the warm room, added S238), and Testimonials' `.tm-featured`. Built and approved on the rendered pages."

Counted on the live pages:

| Named in section 5.3 | On the live page |
|---|---|
| `.cons-stage` | 5 |
| `.story-proof` | 20 |
| `.fa-act--tint` | **0** |
| `.fa-act--dark` | **0** |
| `.tm-featured` | **0** |

**Three of the five render nowhere**, and the sentence says all of them are built and approved. This matters beyond tidiness: section 5.3 is what anyone quotes to justify a 16px corner on a new stage panel, and under Rule 4 that quote is supposed to be a fact. **The DSRD is Chat's, so the correction is Chat's**, and it has to move at the same time as any deletion. Delete the CSS first and the document points at classes that exist in no stylesheet and no template.

## 2. The number I first reached was wrong twice, and the second correction is the important one

I measured dead classes by searching the theme's own PHP and JS. That gave 158 across the theme, 19 per cent. **Both the method and the conclusion were unsafe.**

**First correction: markup the theme does not own.** All thirteen `cmplz-*` rules in footer.css came back dead. They are the Complianz consent banner, rendered by the plugin, and they appear on all 22 pages. Re-checking every candidate against the rendered pages as well as the templates takes the total from 158 to **133**.

**Second correction, and this is the one that would have caused damage.** A class absent from every built page is not necessarily rot. It may be CSS built ahead of a page that does not exist yet. Here is what sits in cards.css's 34:

> `card--membership--annual`, `card--membership--monthly`, `card__price-pill`, `card__price-sub`, `card__save-badge`, `card__anchor-price`, `card__course-count-pill`, `card__hour-pill`, `card__school-name`, `card__academy-line`, `card__checklist`, `card__thumbnail--quote`, `card__thumbnail--workbook`

**That is the membership card, the course card, the school bundle card and the Access All Areas card**, DSRD 8 sections 7 to 10. They render nowhere because `/pricing/` is a 404 and the course, school, quote and workbook pages are not built. **A deletion pass told to remove "the dead 158" would have deleted the entire commercial card system**, and it would have looked correct at every step.

## 3. The honest breakdown

| Stylesheet | Candidates | What they actually are |
|---|---|---|
| testimonials.css | 39 | **Genuinely dead.** Superseded design of a page that IS built. Verified: zero on the rendered page, zero callers, and the page now runs on the shared member-stories and member-voices blocks instead |
| about.css | 35 | **Unverified.** `fa-act*`, `facet-row*`, `fam-*` look like superseded versions of the story scroll, but `about-prospectus` and `about-accreditation` may be planned blocks. Needs the same check testimonials got before anyone touches it |
| cards.css | 34 | **NOT dead. Built ahead of unbuilt pages.** Do not touch |
| components.css | 3 | **NOT dead.** `school--cbp`, `school--lc`, `school--miw`: school modifiers, school pages unbuilt |
| base.css | 21 | **A different category entirely.** `type-h1`, `type-hero`, `sp-2xl`, `btn--full-width`: design-system vocabulary offered for use. Unused inventory in a design system is arguably deliberate, not rot. Kain's call whether it stays |
| knowledge-hub.css | 1 | `kh-course-hero-label`, one orphan |

**Only testimonials.css is verified safe to delete today.** Six stylesheets are completely clean: book-note, footer, global-impact, header, help, people, policies and reviews.

## 4. The inverse fault, and a correction to my own work

**`.tm-answers` is written by the testimonials template three times and has no CSS rule anywhere.** A wrapper the page emits that no stylesheet styles. Probably harmless, possibly a rule lost in the same S045 rework. Worth a look rather than an assumption.

**And I got one wrong earlier tonight and fixed it in the same session.** I annotated the lightbox's 14px corner as an approved one-off between the 12 and 16 tiers. Section 5.3 already records it as "a found inconsistency (recorded S223), not a fourth tier". My annotation promoted a recorded defect into a decision, because I wrote it from the value in front of me instead of opening the section that owns it. Corrected at v0.60.12 with the DSRD's own words quoted in place, and the 16px fix named there as Kain's to approve rather than mine to tidy.

## 5. What I need back

1. **A commission for testimonials.css only**, or a word that it waits. One page, verified, and the page will render identically before and after because none of those rules match anything.
2. **DSRD 7 section 5.3 corrected by Chat**, in the same breath, so the document stops naming three blocks that do not exist.
3. **A decision on the about.css 35 before, not after:** superseded, or planned? I can run the same verification I ran on testimonials if you want the evidence first.
4. **Nothing on cards.css, components.css or base.css.** Those are not the same problem, and grouping them with the others is how the commercial card system gets deleted.

*No em or en dashes in this file; checked before writing.*
