# COMMISSION: delete testimonials.css's dead rules, and verify about.css the same way

**From:** Claude Chat, Session 265. **Date:** 2026-08-11.
**Authority:** Kain, in session, on your S054 report.
**Answers:** `REPORT__Dead_CSS_Across_The_Theme_And_A_Spec_That_Points_At_Nothing_S054.md`, items 1, 3 and 5, and `BRIEF__S054_Ships_Model_Confirmation_And_A_Dead_Stylesheet.md` item 4.1.

## 1. The deletion pass: testimonials.css only

Approved as you scoped it. Delete the six dead families (`tm-vid`, `tm-featured`, `tm-card`, `tm-header`, `tm-chapter`, `tm-close`) and keep the two live ones (`tm-lb`, `tm-answers`). The four non-system breakpoints (900, 860, 720, 719) go with their dead blocks, exactly as your report said, so no ruling on them is needed.

**The check is the one you named yourself:** render the page before and after and show it is identical, since none of the deleted rules match anything. Return the before and after evidence with the counts: rules deleted, rules kept, file size before and after. The surviving file passes the CSS gate.

**While you are in there:** the `.tm-answers` inverse fault from your item 4, the wrapper the template writes three times that no stylesheet styles. Look at whether a rule was lost in the S045 rework or the wrapper is genuinely harmless, and say which in your return. If a rule was lost, report what it was rather than reinventing it; restoring a lost style on an approved page is a change Kain sees rendered first.

## 2. about.css: verify, report, delete nothing

Run the identical verification you ran on testimonials.css over the 35 about.css candidates: rendered-page count, caller count in PHP and JS, and your judgement per family of superseded versus built-ahead-of-a-planned-block. You flagged `about-prospectus` and `about-accreditation` as possibly planned; that is exactly the distinction the report should settle or mark unsettleable. **Delete nothing in about.css in this job.** The report comes back through TO Chat and the deletion, if any, is its own commission after Kain has seen the evidence.

## 3. Two rulings from this session, recorded so you have them

**base.css's unused inventory stays.** The design-system vocabulary (`type-h1`, `type-hero`, `sp-2xl`, `btn--full-width` and the rest of the 21) is ruled deliberate inventory, not rot. No action for you; recorded so the question is closed rather than resurfacing.

**cards.css, components.css and knowledge-hub.css are untouched**, per your own item 5. Nothing built ahead of an unbuilt page is dead. Your catch that a naive dead-158 pass would have deleted the commercial card system is the reason this commission is scoped the way it is.

## 4. What Chat is doing on its side, so the order is visible

DSRD 7 section 5.3 wrongly says `.fa-act--tint`, `.fa-act--dark` and `.tm-featured` are built and approved. Chat holds that correction until your about.css report lands, then fixes the section once against the verified facts, so the document is corrected once rather than twice. Your item 2 asked for the correction in the same breath as the deletion; this is that, sequenced so the about.css families named in the same sentence are settled in the same edit.

## 5. Definition of done

testimonials.css deleted down to its live families with the before and after render evidence and counts filed to TO Chat; the `.tm-answers` question answered in the same return; the about.css verification report filed to TO Chat with per-family evidence and judgements; nothing deleted outside testimonials.css.

*No em or en dashes in this file; checked before writing.*