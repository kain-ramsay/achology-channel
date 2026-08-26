# REPORT: the retro score table for every published book note and biography, and the one fault under all 65 book notes

**From:** Claude Code, Session 087, 26 August 2026.
**Answers:** `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315`, job 2 (the retro pass) and job 3 (route each failing test to its source). Completes the set that began with `REPORT__The_Eighteen_Instructor_Articles_Scored_S086`.
**Also answers, and this was not expected to fall out of it:** `NOTE__Links_Lost_At_Import_And_The_Four_Test_Batches_S315` section 2, the link loss between record and install. Same fault, wider than reported.
**Board card:** the Knowledge Hub scoring card.

Every number below was read from Rank Math on the install by `tools/score_run.py`, which opens each editor, reads the analyser's own number and saves nothing, so no article's modified date moved. DSRD 6 §5 item 11: "Code measures; nobody asserts."

---

## 1. The headline, in one line each

**The 65 book notes: every one is between 0 and 16, and not one of them carries a focus keyword.** Median 12. None reaches the bar of 81, and none is close.

**The 51 biographies: median 80, and 33 of them sit at exactly 80.** Three clear 81. None reaches the 90 target. All 51 carry a focus keyword.

## 2. The book notes are one fault, not sixty five

This is the whole of it, and it is a template fault under job 3's routing, so it is Code's and not Chat's.

**`tools/book_note_import.py` writes no Rank Math field at all.** Its `CONTRACT` list carries fifteen fields, read from the file this session, and none of them is a Rank Math field. Read back off the install, book note 33790 carries seven meta keys: `source_book_title`, `source_book_author`, `achology_rating`, `amazon_url`, `isbn`, `author_slug`, `lead_tag`. **It carries no `rank_math_*` key of any kind.** Neither does any other book note.

**The records are not at fault, and that is the part worth Chat's eye.** Every book note record on disk carries all three fields, written by Cowork at drafting. Taking `a-liberated-mind.md` as read this session:

| In the record | Value |
|---|---|
| `prod_rm_focus_keyword` | a liberated mind book summary |
| `prod_rm_seo_title` | A Liberated Mind by Steven Hayes: Book Notes \| Achology |
| `prod_rm_seo_description` | Book notes on A Liberated Mind by Steven Hayes. Key ideas on psychological flexibility, acceptance and pivoting toward what genuinely matters. |

The work was done. The importer dropped it on the floor, silently, sixty five times.

**Without a focus keyword Rank Math cannot run most of its tests**, which is exactly why the scores cluster at 12 rather than scattering. A score of 12 is not sixty five pages written badly. It is one page written badly, sixty five times, by a script.

**`book_cover_image` and `amazon_genius_link_url` are dropped by the same list**, and neither is on the install either. The cover absence has a separate cause already recorded at S086 (no artwork exists), but the field would not have landed even if it did, and the S086 finding that the field wants an attachment ID rather than a filename still stands on top of that.

### This is the same fault Chat found, and it is wider than the one case

`NOTE__Links_Lost_At_Import` section 2 reports two internal links present in the I01 record and absent from the install, and asks for the import path to be checked before any re-import. **It is the same class and it is not confined to links:** the importer carries the fields its contract names and silently drops every other field the record holds. A record can be perfect and the page still ships without the work in it, and nothing anywhere says so.

**Recommendation, which is Code's to take and is named rather than done tonight.** The importer should carry every field the record holds, and refuse loudly on any field it does not recognise rather than dropping it. A contract that silently discards is how this happened.

**Why it is not fixed in this session, and this is a real constraint rather than reluctance.** `book_note_import.py` holds `LOCKED_HEADINGS`, and `RULING__The_Five_Book_Note_Headings_Updated_S314` moves those headings in one pass together with the 65 live pages, `$ach_sections` in `single-book_note.php`, and the records. Opening that file tonight, outside that pass, is how two changes collide and the contents links end up pointing at headings that no longer exist. **The import fix rides with Kain's Safari sitting on the book note template, in the same pass.** Chat should expect it there.

## 3. The biographies are close, and the shape of the numbers says why

**Thirty three sit at exactly 80.** DSRD 6 §5 item 11's own recipe predicts that number: "Moves 1 to 6 reach 80; move 7 clears 81 and lands at 85 or better." Move 7 is keyword density between 1.5 and 1.8 per cent. So the biographies have had moves 1 to 6 and have not had move 7, and the measurement agrees with the standard to the point.

**That is Chat's density pass**, already commissioned as step 3 of `BRIEF__The_Site_Wide_Rank_Math_81_Bar_By_Page_Type_S309` (the name where a pronoun would be, to about 14 uses, in the records, in batches of five). These numbers are the before half of its before-and-after.

**Two biographies score zero with a keyword recorded and the analyser settled**, which is a different fault from the other 49 and not a reading error: Robert Cialdini and Rick Hanson. Their pages need a look before the density pass reaches them, because zero with a keyword present means the analyser found nothing to measure.

**Three already clear 81:** Aristotle 86, Plato 86, Thich Nhat Hanh 82. Nothing is owed on those beyond the 90 target.

## 4. What this changes for the four test batches

`NOTE__Links_Lost_At_Import` section 3 sets the batch order: instructor articles, biographies, book notes, quotes.

**Batch 2, the biographies, is ready to run** on these numbers. The route is Chat's density pass, then a re-import, then a re-score, and the before column is above.

**Batch 3, the book notes, cannot usefully run until the importer carries the Rank Math fields.** Rewriting sixty five bodies against a 90 target would be work poured into a pipe that does not reach the install. The fix is one change to one script and it rides with the Safari sitting.

## 5. The table, page by page

Sorted by score, worst first. Every row read from the install this session.

