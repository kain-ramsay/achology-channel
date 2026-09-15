# C, partial: the guarded block is built, its placement needs a ruling

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `PRIORITY__Four_Cards_Close_Today_Do_These_First_S361.md`, item C.

---

**Built and deployed, v0.434.0.** `achology_kh_book_articles_block( $book_id, $base_url )` in `knowledge-hub-parts.php`. Counts published articles carrying `source_reference` equal to the book note's ID; where the count is zero it prints nothing at all, not an empty heading. Where the count is real it prints one link, "All Articles from this Book", to the existing `/learn/{category}/book-notes/{slug}/articles/` route. Matches the query pattern and workbench-key handling `achology_further_reading()` already uses.

**Not called from `single-book_note.php`, and this is the part I would be guessing on.** That exact page carries a ruling I read in full before touching it: Kain, S088, quoted in the file itself, "we need to definitely only have three blocks at the bottom of each article page ... which I think is too much." The block removed at that ruling ("Next possible steps after this Book Note") had three rows: this book's articles, this book's quotes, other book notes in this category. This new function is, in substance, one of those three rows, rebuilt guarded.

Two rulings, two different sessions, both real: S088 caps the foot at three and named this exact content as one reason why. S350 commissions this exact link, guarded, aware that the content is not there yet. Neither reads to me as obviously overriding the other, and where a fourth block goes on a page whose block count was itself the subject of a ruling is a placement decision, not a mechanical one. Left for a ruling rather than guessed.

**One live proof already available without waiting on the ruling:** every published book note today carries zero matching articles (source_reference is empty everywhere, as the brief says), so the guard's "absent" half is already true on every live book note page, checked. The "renders" half cannot be shown live until a book-derived article publishes or the function is called with a workbench-keyed draft; happy to build a workbench-only preview of the rendering half if that helps the decision.

---

OWED BACK: where this link renders (the rail, a new small section elsewhere, or Kain overturns the three-block cap for this one case), and I will wire it in the same sitting once told.

*No em or en dashes in this file; checked before writing.*
