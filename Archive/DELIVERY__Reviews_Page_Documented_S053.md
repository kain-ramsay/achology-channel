# DELIVERY: the Reviews page is approved and documented, and here is what is now yours

**From:** Claude Code, Session 053. **Date:** 2026-08-11.
**Authority:** Kain approved the page by eye on the live site: "this page is absolutely perfect", and then asked for every decision to be captured before we move on.
**Live:** theme v0.55.1, https://achologytest.com/reviews/

## 1. What was written, and where

Four artefacts, all in the folders the system already names. **The channel carries this pointer; the documents live where they live.**

| Artefact | Where |
|---|---|
| `Reviews_Page_S053_APPROVED.html` | Verified Student Reviews Page folder, under Proof + Funnel Design Prototypes |
| `SPEC__Reviews_Page_S053.md` | beside it, same folder |
| `achology-review-card-proof-v2.html` and its updated `BUILD_SHEET__review-card.md` | Card System folder |
| `achology-filter-bar-proof-v1.html`, `BUILD_SHEET__filter-bar.md` and a folder README | a NEW **Form Controls** folder under Component Design Prototypes |

**The page prototype is frozen, not linked.** Every stylesheet the page loads was fetched and inlined, so the record cannot drift when the theme moves on. Images and fonts stay as live addresses: they are assets rather than design decisions. Opened and checked standalone before filing.

**The card is now v2.** v1 was exported earlier in the same session at v0.49.0, before the verified word, the baseline-aligned attribution row and the star drop. It is gone rather than kept beside v2, per that folder's rule 1, and it is reproducible rather than lost: the builder reads the theme and the theme at v0.49.0 is in git.

**The Form Controls folder is new and I created it.** Your S258 brief makes this bar "the site's first form-control standard ... for every filter and search field built after it", and a standard cannot live in one page's folder. If you would rather it sat somewhere else, moving three files is nothing; say so.

## 2. The one thing to read before using the filter bar sheet

**Its values are marked RULED, SPEC, CANDIDATE or GAP, and the CANDIDATE rows are not a standard yet.**

Kain approved the page as a whole. He has not ruled the bar's field height, its internal padding, its option-row spacing or its focus ring one at a time, and your brief says these become the standard once he does. I have not quietly promoted "he liked the page" into "he ruled every value in it". They are marked so nobody downstream has to guess which is which.

## 3. What is now yours to write

1. **DSRD 9 §29 needs rewriting against the page spec.** Block order changed: there is no "Where next" panel; the About gateway and the enquiries panel are there instead. So did the grid (masonry, two across, not three), the batch size (50), and the default order (striped across the star bands, not newest first).
2. **DSRD 8 §14** needs the S053 card rulings folded in as history. The card's own sheet already carries them.
3. **DSRD 7 needs a form-control section.** It currently specifies no field height, no internal padding, no focus ring and no option-row anything. The filter bar sheet is the raw material.
4. **DSRD 7 has no link-hover standard.** The Reviews card's course link is the site's first proper in-component link and therefore has no hover colour, because the only darkened orange in the palette is reserved for primary buttons. Every link built after it asks the same question.
5. **`--color-dark-footer` #2D3940 is being used as a text colour** on the card's course prefix, outside its stated role as the sub-footer's background. Either the role widens or a darker text token gets named.
6. **PLAN__Reviews_Page.md** sections 3, 7 and 8 are superseded on the points above.

## 4. What is still not built on this page, and what each waits on

| Item | Waiting on |
|---|---|
| Block 5, the standout reviews | a source carrying the Featured flags: the shipped export has that column empty on all 4,517 rows |
| The Theme dropdown | the Cowork tagging pass |
| Review card titles | the same pass |
| The schema decision | Code, next session. DSRD 9 §29.7 O4 leaves it to Code to decide and state |
| The DSRD 6 gate and its per-chapter record | Code, next session |
| Rank Math SEO and GEO metadata | Code and Chat |

**The page is not "done" until those last three are, and I have not called it done.** Kain has approved how it looks and reads; the gate has not been run.

## 5. Two process notes, recorded rather than explained away

**I measured the wrong thing and shipped it.** The card's attribution row was centre-aligned, which aligns the boxes; three pieces of text at 14px and 11px have boxes of different heights, so their letters sat at different heights. My check compared box centres, which agreed to the pixel, and I reported it as correct. Kain could see it immediately. The row is baseline-aligned now and the check reads the text baseline, with the star row's offset measured from the font's own ink metrics. **The lesson is not "measure more", it is that a measurement which cannot fail is not evidence.**

**I deployed twice under one theme version** and my own re-measurement read the cached stylesheet, which made a fixed thing look broken. Bumping on every deployable change exists for exactly that. Second time this session.

*No em or en dashes in this file; checked before writing.*
