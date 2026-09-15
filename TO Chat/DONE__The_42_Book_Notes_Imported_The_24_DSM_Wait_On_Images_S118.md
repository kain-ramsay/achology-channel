# DONE: the 42 book notes are on the install; the 24 DSM records wait on their images

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** `NOTE__Import_The_42_Book_Notes_And_The_24_DSM_Records_Cowork_Is_Done_S362.md`.

---

**42 of 42 book notes imported.** 17 created as new drafts, 25 updated in place (these were already-published pages carrying the old five section headings; Kain's relabel is now live on all 25, checked by reading the rendered headings straight back off the install). All 42 covers confirmed carrying real alt text, backfilled at the same time under this session's field-mapping fix. Nothing published beyond the 25 that were already live before today; the 17 new ones are drafts.

Bringing these 42 back surfaced two real faults in `book_note_import.py`, both fixed and named in full in `REPLY__The_Sixteen_Fields_Fully_Resolved_And_Two_Bugs_Found_Fixing_Them_S118.md`: a body-extraction fault that read fifteen of the forty-two as empty, and the project's own file footer landing as a stray paragraph on forty of them, both caught before anything shipped.

**24 of 24 DSM records still refused, every one on the same ground: no featured image on disk.** Checked directly with `import_field_authority_articles.py --type instructor-article --only ...` in plan mode: `content_gate.py` passes all 24 (Cowork's paragraph rewrite holds), but the importer refuses every one for the missing hero. This is the same gap the S117 memory note named; still unresolved, still waiting on the image asset, not on anything Code can do.
