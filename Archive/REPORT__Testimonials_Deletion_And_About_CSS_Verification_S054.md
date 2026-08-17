# REPORT: the testimonials deletion is done and proved, and about.css is verified

**From:** Claude Code, Session 054. **Date:** 2026-08-12. **Live at v0.60.13.**
**Answers:** `COMMISSION__Delete_Testimonials_Dead_CSS_And_Verify_About_S265.md`, all of section 5.
**Authority:** Kain in session ("go ahead"), and this commission arriving the same evening.

## 1. The deletion: counts

| | Before | After |
|---|---|---|
| Lines | 241 | 131 |
| Rules | 96 | 30 |

**Deleted:** the six families as scoped (`tm-vid`, `tm-featured`, `tm-card`, `tm-header`, `tm-chapter`, `tm-close`), the four non-system media queries that served only them (900, 860, 720, 719), and a `prefers-reduced-motion` block whose every selector belonged to a deleted family.

**Kept:** `tm-lb` (the video lightbox), `tm-heading`, `tm-intro`, `tm-filter`, `tm-tab`, `tm-panel` (the question navigator), and the closing blocks borrowed from about.css.

The surviving file passes the CSS gate, and so do all sixteen stylesheets.

## 2. The proof, and the three times the instrument was wrong before it was right

**The result: the full computed style of all 1,096 elements, hashed at 22 viewport widths, before and after. Zero differences.** The widths were chosen to fire each deleted media query from both sides (901/900/899, 861/860/859, 721/720/719), because a deletion that only showed at 861px would pass a desktop-and-phone check.

**That number only means something because the instrument now fails when it should.** It did not at first, and the sequence is worth recording:

1. **It fingerprinted the CAPTCHA.** The first run reported "10 elements" and wrote a snapshot. SiteGround's Antibot had served a challenge screen. Fixed by loading through `page_gate`'s own Mirror, which fetches through SSH from inside the server, and by refusing to write a snapshot with implausibly few elements rather than writing a small one.
2. **It hashed `getComputedStyle` in enumeration order, which is not stable between runs.** Two runs of identical code reported **24,112 differences**. A probe comparing the same elements as dictionaries found 628 properties and zero changes: the values were never different, only their order. Fixed by sorting before joining. My first guess at the cause, the mirror's port appearing in URL-bearing custom properties, was wrong, and I found the real one only by reading the bytes instead of guessing a third time.
3. **The global impact markers animate**, so their transform and opacity differ every time you look: **746 more phantom differences**. Motion is frozen before measuring now.

**A control run of identical code against itself now returns 0.** That is what makes the 0 in the real comparison mean anything.

**One residue, chased down rather than waved off.** The first real before-and-after showed 7 differences, all of them site-header logo, picture and image elements, at one width only, 767px, and nothing in the page content. It did not reproduce on a control run, nor on a second complete before-and-after cycle. Responsive image selection across a cache purge, not the deletion. Recorded because a 7 left unexplained is how a real defect hides later.

## 3. The `.tm-answers` question: no rule was lost, and the wrapper is deliberate

**Answered from the template's own comment, not inferred.** `page-testimonials.php` carries this above the wrapper:

> "One block, not four. DSRD 7 §4.3 governs 'the separators between page-level blocks', and the heading, its one intro line, the question filter and the answers grid are one block: the page gate was demanding a hairline between a heading and its own intro because each sat loose in the column as a page-level child. Wrapped at S045; nothing inside it moves."

So `.tm-answers` was added at S045 as a **structural wrapper grouping four page-level children into one block** for the hairline rule. It was never meant to carry styling, and "nothing inside it moves" is the author saying so. Its three template appearances are the class, the heading's id, and the `aria-labelledby` pointing at it.

**Nothing to restore, and nothing for Kain to see rendered.** Recommend it stays unstyled.

## 4. about.css: verified, nothing deleted

Same method: rendered-page count across 23 pages, plus caller count in every PHP and JS file in the theme. **All 35 score zero on both.** My judgement per family:

| Family | Count | Judgement |
|---|---|---|
| `fa-act`, `fa-act--dark`, `fa-act--tint`, `fa-line--dark`, `fa-meta`, `fa-photo`, `fa-photo--ph`, `fa-rail` | 8 | **Superseded.** The earlier "five acts" story scroll. The About story now runs on `cons-stage` and the timeline classes that do render |
| `facet-row`, `facet-row__body`, `facet-row__img`, `facet-row__link`, `facet-rows` | 5 | **Superseded.** An earlier row treatment inside the story |
| `fam-act`, `fam-name`, `fam-rail`, `fam-reel`, `fam-reel__strip`, `fam-srail`, `fam-swap`, `fam-wrap` | 8 | **Superseded.** An earlier milestone rail |
| `cons-shell`, `cons-wrap` | 2 | **Superseded wrappers of a LIVE block.** `cons-stage` renders 5 times on /about/; these two are its earlier scaffolding. Delete with care: they sit next to something live |
| `d5-chart`, `x5-lm`, `x5-yr`, `m-line`, `sd-note`, `pfq-title` | 6 | **Superseded fragments** of the chart, the era markers and the question selector, all with live successors |
| `about-accreditation`, `about-accreditation__badges`, `about-accreditation__link`, `about-accreditation__text` | 4 | **UNSETTLEABLE from here, and this is the one to look at.** `/accreditation/` is a DSRD 1 page that is not built. This may be a block built ahead of it, exactly like the cards.css case, or a block cut from About. Nothing in the theme decides it |
| `about-prospectus`, `about-prospectus-list` | 2 | **UNSETTLEABLE, same reason.** A prospectus block with no page and no plan I can read |

**So: 29 of the 35 are superseded and safe; 6 are the same trap cards.css was**, and they need someone who knows whether an accreditation block and a prospectus block are still coming. That is not a fact in the theme, so under Rule 5 it stops with me and comes to you.

**Nothing in about.css was touched.**

## 5. What this unblocks for Chat

Your section 4 held the DSRD 7 section 5.3 correction until this landed. The facts are now settled: **`.fa-act--tint` and `.fa-act--dark` are superseded and render nowhere, and `.tm-featured` no longer exists at all** as of v0.60.13. `.cons-stage` and `.story-proof` are live and correct. Section 5.3 can be corrected once, against those.

## 6. What I need back

1. **A ruling on the six unsettleable about.css classes** (accreditation, prospectus): planned, or cut? Then the about.css deletion can be commissioned or closed.
2. **Nothing else.** The testimonials job is complete to your definition of done.

*No em or en dashes in this file; checked before writing.*
