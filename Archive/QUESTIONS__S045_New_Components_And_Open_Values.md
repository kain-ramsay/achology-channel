# QUESTIONS: what S045 produced that the documents do not yet hold, and how these two pages should be checked

**From:** Claude Code, S045. **Date:** 2026-08-05.
**Read with:** `SHIP__S045_Founders_Letter_And_Testimonials.md`, which describes the build.

---

## THE ONE KAIN ASKED ME TO PUT TO YOU FIRST

**How do these two pages need to be checked?**

Both are live and both are past their own machine gate as far as that gate can go. Layer 3 of the harness says a fresh evaluator grades a built page against its signed spec before Kain sees it, and that "when the rendered page travels back through TO Chat, Chat reviews it against the signed spec, chapter by chapter, before Kain views it."

Neither page has a signed spec. The letter was designed live with Kain across S044 and S045; Testimonials was corrected against DSRD 6 and his eye, under `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`, which puts it sixth on the walk. So the question is genuinely open and it is not mine to answer:

1. **What does Layer 3 grade a page against when the page had no signed spec, because Kain designed it in the session?** The evaluator's checklist starts "Every block the signed spec names is present, in the spec's order". For these two, is the record of what he approved in the session the thing to grade against, and if so, who writes it, you from this file or me?
2. **Does the DSRD 6 record for each page get filed before or after that grading?**
3. **Testimonials is on the one-page-at-a-time walk. Does this pass count as its walk, or does it still need the full chapter-by-chapter record separately?**

Until you answer, I have filed no DSRD 6 record for either page, because I do not want to invent the shape of one.

---

## 1. The lightbox shadow, DSRD 7 §5.4's open item, settled

§5.4 said: "the lightbox shadow exists in two versions. policies.css uses `0 24px 64px rgba(var(--color-dark-footer-rgb), 0.45)` and testimonials.css uses `0 24px 64px rgba(0,0,0,.4)` on the same visual idea. One will be chosen on the rendered page, tokenised, and swapped in."

Both were built as two local files showing the same lightbox on the real page, and Kain told Code to settle it rather than choose between them himself. **The brand dark version wins**, because the palette holds no pure black and every other shadow token on the site is built from brand colours.

- `--shadow-lightbox: 0 24px 64px rgba(45,57,64,0.45)`, now in base.css and in use.
- The close button's `0 4px 14px rgba(0,0,0,0.25)` became `var(--shadow-float)`, which took your expectation.
- Both hand-typed `#000` values went with them: the panel background is now `--color-dark-footer`. The remaining `#000` pair is inside a mask, where the channel is opacity rather than colour, and is annotated in place rather than recoloured.

**You said you would write the §5.4 row. It is yours.**

## 2. The Panel Heading line-height you have been waiting for since S238

Measured on the rendered About page today, both instances: **24px, weight 600, line-height 30px, a ratio of 1.25.**

Note that this is not the 28px §3.1 currently records for that row. Kain brought every section heading on About to one size at S044, which is the 24px H2. The row needs both numbers correcting, not just the line-height.

## 3. New things that need a DSRD entry

**a. A third typeface.** DSRD 7 §3 says "Font pairing: Como (headings/labels) + Source Sans 3 (body text)." Kain asked for a handwriting face in the letter's said block and approved it on the render. It is **Caveat**, loaded from Google Fonts beside Source Sans 3 in functions.php, named once in base.css as `--font-hand`, and reached only through a token. §3 needs to record it, or rule it out.

**b. The said block**, DSRD 8. Its full token set is in base.css under `--said-*`: tint, panel, radius, padding, width, font, size, weight, leading, ink, mark size, mark ink, mark alpha, mark inset, bleed. First use is the Founders' Letter. It floats at 40 percent of the reading column, steps its tint outside the column by exactly its own padding, and drops the float on phones.

**c. The closing enquiries panel**, DSRD 8. Your own addendum said "this panel is intended as a future shared site-wide closing component with a per-page message ... Do not generalise it yet." Kain overruled that at S045 and asked for it at the foot of both new pages, so it is now one renderer in shared-parts.php with a per-page message. **The page gate fails on it until DSRD 8 names it**, because check 4 reads component membership from that document.

**d. The related-questions wrapper**, same reason, same gate failure.

**e. The member card face layer**, an addition to DSRD 8 §14: the member's portrait behind their own card, governed by `--lite-face-alpha` 0.13, `--lite-face-x` 25 percent and `--lite-face-y` 12 percent, faded out under the quote by a mask.

## 4. A deviation from a LOCKED section, on Kain's word

DSRD 7 §14.1 stages the watermark pair by page height: "standard pages place the left/right pair at 45%/55%; tall pages widen to 30%/70%". On the Founders' Letter Kain asked for the pair to sit against a named passage instead, so it renders at 38 and 58 percent on that page alone. Every constant §14.1 fixes is untouched. **Either §14.1 widens to allow a page to place its own pair, or this is recorded as that page's exception.** I have not assumed which.

## 5. Two things you asked for that are not in this file

- **The list of templates carrying baked images**, for the version-stamp standard. Not done: the session went to the two pages instead. It is a short audit and it is next.
- **The live site URL export for the redirect map** (`QUESTION__Live_Site_URL_Export_For_Redirect_Map.md`). One constraint you should know now: the SSH access Code holds is to **achologytest.com**, the build site. Nothing in this session touched achology.com and I have no shell there. If the export must come from the live site, that is a Kain question about access, not something I can route around.

*No em or en dashes in this file; checked before writing.*
