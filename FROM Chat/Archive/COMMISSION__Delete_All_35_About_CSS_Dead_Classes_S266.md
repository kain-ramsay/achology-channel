# COMMISSION: delete all 35 dead about.css classes, with render proof

**From:** Claude Chat, Session 266. **Date:** 2026-08-12.
**Authority:** Kain, ruled in Session 266 on the evidence in your `REPORT__Testimonials_Deletion_And_About_CSS_Verification_S054.md`.
**Answers:** that report's section 6 item 1. This closes the about.css question whole.

## The ruling

**All 35 unused about.css classes are cut, including the six you could not settle.** Kain ruled the four `about-accreditation` classes and the two `about-prospectus` classes as dead, on these grounds, checked from the record before the question reached him:

1. The accreditation page (PRD Pr1.22) is real and coming, but under the S257 component truth system nothing signed lives in CSS. When that page's turn comes it gets its own signed spec from Kain and you build to that spec, never to orphan classes resurrected from a file.
2. No prospectus page exists anywhere in the site architecture. The prospectus work on the board is the Canonical Document Library card, which produces documents, not a site block.
3. Nothing in either family was ever approved by Kain's eye on a rendered page, so deleting them loses nothing the system recognises as a signed record.

## The scope: all seven families from your own verification

Your S054 report's table, all 35: the 8 `fa-` classes (`fa-act`, `fa-act--dark`, `fa-act--tint`, `fa-line--dark`, `fa-meta`, `fa-photo`, `fa-photo--ph`, `fa-rail`), the 5 `facet` classes, the 8 `fam-` classes, the 2 superseded wrappers (`cons-shell`, `cons-wrap`), the 6 superseded fragments (`d5-chart`, `x5-lm`, `x5-yr`, `m-line`, `sd-note`, `pfq-title`), the 4 `about-accreditation` classes, and the 2 `about-prospectus` classes.

## The method: the same instrument that proved the testimonials deletion

Before-and-after full computed-style comparison on every page that loads about.css, at the viewport widths that fire each media query the deletion touches from both sides, with a control run of identical code against itself returning 0 first. Motion frozen, Mirror fetch, the implausibly-small-snapshot refusal: everything the testimonials run taught. Zero differences is the pass.

## The one care note, yours, carried forward

`cons-shell` and `cons-wrap` sit next to the live `.cons-stage`, which renders 5 times on /about/. Your own words: delete with care. The render proof is exactly what makes that care demonstrable.

## Definition of done

1. All 35 families gone from about.css.
2. Render proof: zero differences on every page loading about.css, control run 0 printed.
3. `css_gate.py` PASS on the surviving file and all stylesheets, pasted in the ship brief.
4. A short report back through TO Chat with the before-and-after counts, per the testimonials pattern.

## One piece of context you were waiting on

DSRD 7 section 5.3 has been corrected this session against your S054 facts: the stage-panel list now names only `.cons-stage`, `.story-proof` and the closing enquiries panel, with `.fa-act--tint`, `.fa-act--dark` and `.tm-featured` recorded as gone. Your section 5 note is consumed.

*No em or en dashes in this file; checked before writing.*
