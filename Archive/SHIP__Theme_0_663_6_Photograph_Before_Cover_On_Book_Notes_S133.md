**Record only; asks nothing.** Filed to the Archive per The Shared Rules section 6 (S380).

# SHIP: theme 0.663.6, the author's photograph before another of their books

**From:** Claude Code, factory session, S133, Thursday 24 September 2026.
**Board card:** Book notes. **Authority:** `RULING__Kain_Rules_Every_Book_Note_Author_Illustration_Becomes_A_Real_Photograph_S133` (TO Chat), and Kain's "Yes, please do" in the sitting to putting the photograph first.

**What changed.** `single-book_note.php` read the note's aside image field (the S120 "another of their books" cover) before the author's photograph, so the cover acted as an override. Kain's S120 words made it the fallback for when no photograph can be found. The template now draws the licensed photograph whenever one exists with its credits row, and reads the aside field only where there is none. No content was touched on the install; the 30 aside fields stay as they were and would serve again for a future author with no photograph.

**Result, read off the build site after deploy:** all 30 notes that carried a cover now show their author's photograph, each image fetched and loading: the ten from the 0.663.5 ship and twenty more, among them The Road Less Travelled, Difficult Conversations, The Advantage, Crucial Conversations, the three Judith S. Beck notes, Fierce Self-Compassion and A Liberated Mind.

**The check that missed it.** `page_gate.py`'s author-photograph check looked only for the "Illustration by Achology" plate, so it passed 30 pages showing a cover. It now also fails a book note whose author spot carries a cover ("Cover image via"). The 0.663.5 ship record's line on ten blocked pages is closed by this one.

*No em or en dashes in this file; checked before writing.*
