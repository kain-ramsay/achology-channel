> **CHAT DISPOSITION, S322: read in full, then SUPERSEDED within the same session and archived.** Its section 1 was overturned by `REPORT__Every_Book_Cover_Is_Sourced_And_Rendering_S089`, filed later the same day: the covers were sourced by machine, all 680 rows now hold one and all 65 pages render one, and nothing is owed to Cowork. The machinery half of this report stands. **The board note this file first produced was corrected on the Book Notes card in the same turn the later file was read.** The 220MB pre-upload offer in section 4 is not taken and is now moot.

# REPORT: the book cover machinery is built, and the 64 dark pages are a sourcing gap that no code change fills

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Answers:** `BACKLOG__Everything_Code_Owes_And_The_Order_S088` section 3 item 1, the S088 diagnosis, and Kain's instruction this session to fix the book covers permanently.
**Board card:** Book Notes.
**Shipped:** theme v0.119.1, deployed and proved.

---

## 1. The correction first, because it changes who owns the job

**The S088 diagnosis said 600 of 680 covers exist on Kain's Mac and 80 do not, and that 65 live pages show a dark placeholder. Both halves are true and the join between them was never checked.**

Read this session from the master workbook, the artwork folder and the install together:

| | |
|---|---|
| master rows | 680 |
| master rows naming a cover file | 680 |
| those files present on Kain's Mac | 600 |
| cover files on Kain's Mac | 613 |
| book notes published on the install | 65 |
| of those, whose named cover is on the Mac | **1** |

**The 600 covers that exist and the 65 pages that are dark are almost disjoint sets.** The published 65 are the psychologist expansion, and their artwork was never sourced. The 600 files belong to the rows that have not been imported yet.

**So no upload and no code change fills those 64 pages.** They keep the brand dark panel DSRD 9 section 32.9 item 2 gives them, which `single-book_note.php` correctly calls "the visible symptom of a data error, not a design state", quoting DSRD 8 section 20.2.

**That sourcing job is already commissioned and has not been delivered.** `NOTE__Sixty_Book_Notes_In_Production_Not_Yet_Ready_S306` says Kain commissioned Cowork to "source real cover images for all 60 once they exist", and records that the master wrongly marked 16 of them `cover_status: ok` when no file existed for any of the 16. Nothing has landed. **This is the one line of this report that needs Chat to act.**

## 2. The machinery, which is the half that was Code's

`tools/book_covers.py`, with `tools/book_note_import.py` calling it. Three faults, three answers.

**The artwork was never uploaded.** Measured on the install: 127 attachments in the whole media library. The tool uploads a cover once, keyed by filename, finds and reuses an existing attachment on every run after, so a second import cannot duplicate the library.

**The importer wrote a filename where an address was needed**, so a page rendered `<img src="a-guide-to-rational-living.jpg">`. It now writes the **attachment id**. The ACF field is declared `return_format: array`, so an id is what makes `get_field()` hand the templates what they actually read: the url for the book note hero, and `sizes.medium` for the source book callout on the article page. **A url string renders the hero and leaves the article page's callout blank**, which is the same fault one page further along, and is why the id and not the address is the right value.

**It only ran on create**, so a cover arriving after its page did was missed for ever. It now runs on every row on every run.

**One home for one question.** The importer calls `book_covers.cover_attachment_id()` rather than resolving a cover itself, so it cannot go back to writing a filename by anybody's oversight.

## 3. One thing the first build of the tool got wrong, named rather than buried

It derived the cover filename from the post slug, which is right for most rows and is still a guess. The Shared Rules section 4 names the master as true north for every book note row and it carries a `book_cover_image` column for all 680. The tool now reads the master. **The guess and the master agree on the rows where both exist**, so the fix changed no result; it changed whether the result was read or reconstructed, and reading it is what produced section 1.

## 4. What is not done, and it is deliberate

**The 600 covers that do exist are not uploaded yet.** They belong to rows with no post on the install, so there is nothing to attach them to today, and the import that creates those posts will upload each one as it goes. Pre-uploading them is a 220MB unattended run that buys speed at import time and nothing else. Say if it should run ahead of the import and it will.

OWED BACK: the cover sourcing for the 64, which is Cowork's under the S306 note and is the only thing standing between those pages and a real hero.

*No em or en dashes in this file; checked before writing.*
