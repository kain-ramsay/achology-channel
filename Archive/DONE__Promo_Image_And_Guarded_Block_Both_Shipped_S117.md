# DONE: the promo image fix and the guarded block wiring, both shipped

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `REPLY__Book_Notes_Import_Instruction_Promo_Image_Element_And_Block_Placement_S361.md`, the promo image and item C halves.

---

**The promo image, v0.436.0.** `.kh-foot__kyp`'s max-width dropped from `--container-rail` to none. Verified live at 768px: the element now measures 704px, the full content column, up from the old rail width. It never draws above 1200px at all, so desktop is untouched by construction, not by a rule that could drift.

**Item C, the guarded block, v0.437.0.** `achology_kh_book_articles_block()` now wires in as `reading_lead`, threaded through `achology_content_foot()` into `achology_further_reading()` as a new `lead_html` argument, printed above that block's own rows, inside the same section. Every other caller of both functions passes nothing and is unchanged. Verified live on a real book note: no lead element, no "All Articles from this Book" link, nothing on screen, exactly as expected since every published article's `source_reference` is still empty. Closes items 1 to 3 of the cross-linking card.

One thing worth naming: shipping this caught a PHP parse error of my own making before it ever reached the server, deploy.py's own check refused it and nothing went live broken. Fixed in a second commit, both pushed.

---

OWED BACK: nothing on either line.

*No em or en dashes in this file; checked before writing.*
