# SESSION REPORT: S119

**Filed by Claude Code, Session 119. Date:** 15 to 16 September 2026. **Session type:** factory, with four theme change sets made on Kain's ruling in the sitting.

Assembled from the version control log across the theme, the project and the channel, per Harness Rule 13. Lines resting on no commit are marked hand added.

---

## Finished

- **Every book note on the install re-scored, twice, 125 of 125 both times.** First run found thirteen short. After the corrections below, the closing run reads **124 at 88, one at 82**. Filed as `REPORT__Every_Book_Note_Score_Read_Off_The_Install_124_Of_125_At_The_Ceiling_S119.md`, which Kain instructed be rewritten in place rather than added to, so the superseded table cannot be quoted. Board card: the book note scoring card. Hand added: a score run writes no file to any repository.
- **The cause of the thirteen found, proved, and twelve of them fixed.** Theme commit `ccbef87`. `book_note_import.py` gains `--fields-only`: meta and terms only, no body, no title, no excerpt, no status, no create, so no modified date moves (DSRD 6 section 6). Board card: the book note scoring card.
- **The importer's argument quoting fixed.** Theme commit `4917e2c`. It glued arguments together unquoted, so "Personal Growth" arrived as two categories and two pages took an address from an invented one. Both repaired, four junk terms deleted, both old addresses given a proven 301 through `publish_gate.py --write-redirect` per Kain's S350 ruling. Board card: the book note import card.
- **The 24 DSM hero images landed, imported, attached.** Theme commit `802747b`. 48 derivatives, all inside budget; 24 of 24 verified clean. Filed as `DONE__The_24_DSM_Heroes_Are_Attached_And_Scored_S119.md`. Board card: the 24 DSM articles card.
- **The 24 DSM articles published and checked live.** Kain's ruling in the sitting cleared all 24 at 86 and 88; he published them himself because `publish_gate.py` refuses while the article exemplar carries a failing speed line. 24 of 24 answer 200. Filed as `RULING__Kain_Clears_The_24_DSM_Articles_At_86_And_88_S119.md` and `DONE__The_24_DSM_Articles_Are_Live_And_Checked_S119.md`. Board card: the 24 DSM articles card.
- **All 26 remaining book note drafts published and checked live.** 26 of 26 answer 200 with their covers and alt text. The install now holds 125 book notes, none in draft. Board card: the book note publishing card. Hand added: publishing was done by Kain in the admin and touched no file.
- **The six AI wisdom articles published and checked live.** All six answer 200 with their heroes. Board card: the six AI wisdom articles card. Hand added: same reason.
- **The mid-body picture can be the subject instead of the writer, per article.** Theme commits `d87260f`, `e552705`, `9bb33a8`, `4a0da7a`, `b26dc87`, versions 0.438.0 to 0.439.2, each gated, deployed and read back off the server. The 24 DSM articles carry the DSM-5-TR cover; the six AI articles carry the 1966 ELIZA screenshot, public domain, credited. Kain's rulings and his approval are quoted in `RULING__Kain_Approves_The_DSM_Picture_In_Place_Of_His_Own_On_The_24_S119.md`. Board card: the article template card.
- **`achology_image_dimensions()` reads a media library picture, not only a theme one.** Theme commit `e552705`. It could never read an uploads URL, so any such picture declared no size and text moved as it loaded. Fixed for every caller. Board card: the page readiness card.
- **The article importer's verify reads the section-count standard instead of assuming four.** Project commit `4f8b4fa`. Board card: the article machine card.
- **Four theme items queued rather than taken on speculatively.** In `000__THE_THEME_QUEUE.md`: the quote page's missing real image, the empty `<h1></h1>` every article page renders, and `page_gate.py`'s inability to measure a draft. Board card: the theme queue.

## Not finished

- **`boundaries` holds at 82.** Its body carries no internal link; its own record plans one and it was never placed. Placing it is choosing a sentence, so it is not Code's. What remains: Cowork places the link, then one `--fields-only` run and a re-score.
- **Six book note records hold a keyword with the author's surname in it**, against the S349 ruling. Three pages were corrected on the install tonight; **the records were not**, so a full import from them would undo it. Filed as `ASK__Three_Book_Note_Keywords_Still_Carry_The_Authors_Surname_S119.md` and named again in the score report.

## Three things Chat is owed a decision on

1. **The publish gate and DSRD 3 disagree about when speed blocks.** DSRD 3 section 4.4 times the speed investigation at cutover; the gate treats the same failing line as a blocker on publishing to a build ground hidden from search. That disagreement put Kain's own hands on the keyboard three times tonight. Code did not resolve it by writing an exception onto the exemplar's speed line, because a real site-wide fault is not "genuinely does not apply".
2. **No book note page has a DSRD 6 record at all**, so no book note can ever be cleared by the gate, with nothing to point `--exemplar` at.
3. **74 of the 153 book note records still carry the older section headings.** `--fields-only` means a metadata correction now reaches all of them, proved tonight. A body correction still cannot. Whether the other 62 are ever rebuilt is a scope and cost question, and it is Kain's. Filed in `ASK__Twelve_Book_Note_Records_Are_An_Older_Generation_And_Their_Pages_Cannot_Be_Corrected_Until_They_Are_Rebuilt_S119.md`.

## Three faults of my own, recorded because they are the useful part

Each was found on one page before it reached the rest, and each is named in full in its commit.

1. `--fields-only` was first marked on a row inside `build_rows`, and `push()` does not use those rows: it reads the master spreadsheet. The mark was invisible, a page took a full update, its modified date moved and nothing was corrected. Found by reading the page back, not by trusting "updated: 1".
2. The quoting fix silently broke every call site already hand-quoting around the old bug; a value would have landed with its double quotes inside it, including the search keyword on every page a run touched. Caught by reading the file before the first run after the change.
3. Pushing three records' own keywords took three pages from 86 down to 72. Corrected to the book's title per the S349 ruling; all three then read 88, above where they started.

No em or en dashes in this file; checked before writing.
