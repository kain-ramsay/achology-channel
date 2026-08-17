# SHIP: S045, the Founders' Letter finished and the Member Testimonials pass

**From:** Claude Code, S045. **Date:** 2026-08-05.
**Live at:** v0.38.8 on achologytest.com, deployed over SSH per Rule 12 and cache purged before every gate run.
**Pages:** `/about/founders-letter/` and `/testimonials/`.

Both pages were designed with Kain at the browser under the S044 local-file method: every change was settled in a local file he opened in Safari, and the site was touched only when a piece was finished. No design iteration happened on the build site.

---

## 1. The Founders' Letter

**Copy.** Kain rewrote the letter twice during the session and replaced four further paragraphs and two single ones after that. Every version was taken verbatim. Two obvious transcription slips were corrected on the way in and reported to him at the time ("ompetence" and "yhe").

**Structure, all his.** Four section headings now break the letter into its movements: his own "Achology: Born Out Of Frustration", then "How Achology Actually Began", "What Competence Actually Takes" and "What We Offer Through Achology". The last three wordings are Code's and open to change. The closing section was expanded by four paragraphs at his request.

**A pull quote treatment was built and refused on sight.** It is deleted, not parked behind a class.

**The said block, new.** A passage lifted out of the letter and set apart: a tinted frame stepping outside the reading column, a white panel inside it landing on the column edge, the house quote glyph filled and behind the first and last words, and the passage in a handwriting face. Kain designed it on the render across several rounds and then asked for it to be tokenised, which it is: every value lives in base.css as the `--said-*` set and the block's own rules carry no raw value at all. It is named `.said`, not after this page, because it is a site block the letter uses first. **It needs a DSRD 8 entry.**

**Internal links.** Four, on words already in his sentences: the practice sessions, the Senior and Master Achologists, the ethics training, and the practitioner-level courses. Every target was requested and returned 200 before it was written, except `/courses/`, which Kain ruled in anyway; it 404s until he creates that page.

**Related questions.** Six, chosen against the letter's own argument and in its order.

**The closing panel.** The About page's panel, promoted into `shared-parts.php` as one home rather than copied, carrying About's exact heading and body. Its own spacing rules were de-scoped from `.policy-body` at the same time, because the block only looked right inside that one parent and broke the moment it was reused.

**The watermark bubbles.** All three are present again. The third was being switched off by a manifesto rule keyed on any page carrying a `.policy-doc`, and this page's portrait hero is one. The rule was narrowed at its cause; the manifesto is unchanged. The pair was then moved down to sit against the How Achology Actually Began passage, on Kain's eye. **That is a deviation from DSRD 7 §14.1's stagger and needs your ruling (see the questions file).**

**Gate:** 18 passed, 4 failed. Two are the recorded exceptions you accepted for About, now true of this page for the same two causes: the part-width hero hairline the instrument cannot see, and the phone measurement reading the decorative backdrop. Both were measured by hand on the live page and are correct at every width. The other two are the missing meta description and canonical; the paste-ready strings are with Kain.

---

## 2. Member Testimonials

**The cause of everything on this page:** the template carried `policy-page--about` and nothing else, so every rule written for About governed it silently, including the hero rule that stops the hairline short to clear About's artwork. It now carries `policy-page--testimonials` as well, so it can be spoken to on its own. About is untouched.

**Hairlines.** The hero read far more than 48 below its line, because the artwork runs deeper than the copy and the header ended at the picture's foot. Fixed the same way as the letter. Every hairline on the page now reads 48/48 at desktop and tablet and 32/32 at phone, measured by hand at both widths.

**One block, not four.** The section heading, its intro line, the question filter and the answers grid were four loose children of the reading column, so the gate was demanding a hairline between a heading and its own intro. They are one `section` now.

**Six related questions and the closing panel** added, the panel from its shared home.

**The member cards.** Each member's own portrait now sits behind their grey card, head to shoulders, faded out before the quote so the words stay readable, and the face follows the portrait through a question switch. Kain designed it on the render and then lightened it. Three named values in base.css govern the whole row. **The card is DSRD 8 §14 and this adds a layer to it, so it needs your entry.**

**The video lightbox.** Each member is now introduced as "Senior Achologist" before their country, on Kain's ruling, given for all nine; the card data holds no CPD level, so that is his word and not a value read from anywhere. The question being answered is shown above the answer, and the dialog announces whose video it is.

**Copy corrections.** The lead said nine, the heading said ten, and there are nine member records: nine is the true number, counted from the data, and the heading was wrong. One clause was added to the lead so the page says in its own copy what its title and breadcrumb call it. Kain's own closing sentence is untouched. The hero alt now describes the illustration truthfully.

**Gate:** 35 passed, 7 failed. Two are the same recorded exceptions as the letter. One is the missing canonical. **Four are one thing said twice: check 4 fails on the closing panel and the related-questions wrapper because neither is named in DSRD 8.** Their spacing measures correctly; the gate is reporting an unregistered component, not a defect.

---

## 3. Shared work that came out of these two pages

- **`components.css` passes its own gate again.** The two proof-card shadows collapsed onto the card tokens exactly as your rulings file authorised. The lightbox values are settled (see the questions file). One mask value was annotated rather than changed, because in a mask layer the channel is opacity and a brand token there would assert something untrue about the palette.
- **`--shadow-float` added to base.css**, the value DSRD 7 §5.4 already names and says Code should add.
- **The closing panel promoted to one home** in `shared-parts.php`. `page-about.php` still carries its own copy and was deliberately not touched, because that is a second page: collapsing it belongs to `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`.

## 4. Still failing, and not touched

`testimonials.css` fails its own gate on 24 values that predate this session: hand-typed colours, shadows, and two screen widths that are not system widths. None of them are Code's and none were annotated. Everything above was done without opening that file. It needs the same treatment `components.css` just had, which means Kain ruling on the values he cares about.

*No em or en dashes in this file; checked before writing.*
