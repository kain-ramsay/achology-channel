# SESSION REPORT: S119

**Filed by Claude Code, Session 119. Date:** 15 September 2026. **Session type:** factory, with one theme change set made on Kain's ruling in the sitting.

Assembled from the version control log for the session across the theme, the project and the channel, per Harness Rule 13. Lines that rest on no commit are marked hand added.

---

## Finished

- **Every book note on the install re-scored, one page at a time, 125 of 125.** 112 at 88, thirteen short, all thirteen published pages. Filed as `REPORT__Every_Book_Note_Score_Read_Off_The_Install_And_Thirteen_Are_Short_S119.md`. Board card: the book note scoring card. Hand added: a score run writes no file to any repository.
- **The cause of the thirteen found and proved.** Twelve of them have older-generation records the importer cannot read, so their pages have never been correctable by any run. Filed as `ASK__Twelve_Book_Note_Records_Are_An_Older_Generation_And_Their_Pages_Cannot_Be_Corrected_Until_They_Are_Rebuilt_S119.md`, on Kain's instruction in the sitting to ask Chat directly. Board card: the book note scoring card.
- **The 24 DSM hero images landed, imported and attached.** Theme commit `802747b`. 48 WebP derivatives, all far inside the budget; 24 of 24 imported and verified clean. Filed as `DONE__The_24_DSM_Heroes_Are_Attached_And_Scored_S119.md`. Board card: the 24 DSM articles card.
- **The 24 DSM articles scored and published.** Eight at 89, fifteen at 88, one at 86. Kain ruled all 24 go at the scores they hold and published them himself in the admin, guided in the sitting, because `publish_gate.py` refuses while the article exemplar carries a failing speed line. All 24 then checked on their real addresses: 24 of 24 answer 200 with their own hero and title. Filed as `RULING__Kain_Clears_The_24_DSM_Articles_At_86_And_88_S119.md` and `DONE__The_24_DSM_Articles_Are_Live_And_Checked_S119.md`. Board card: the 24 DSM articles card.
- **The article importer's verify reads the section-count standard instead of assuming four.** Project commit `4f8b4fa`. Two honest records carrying five sections were being reported as failures by a check that disagreed with `content_gate_standards.json`. Board card: the article machine card.
- **The mid-body picture can be the subject instead of the writer, per article, and the 24 DSM articles now carry the DSM-5-TR cover.** Theme commits `d87260f` and `e552705`, version 0.438.1, deployed and proved. Kain's ruling in the sitting, and his approval on the rendered live page, both quoted in `RULING__Kain_Approves_The_DSM_Picture_In_Place_Of_His_Own_On_The_24_S119.md`. Board card: the 24 DSM articles card.
- **`achology_image_dimensions()` reads a media library picture, not only a theme one.** Theme commit `e552705`. It could never read an uploads URL, so any such picture declared no size and the writing beside it moved as the file arrived. Fixed for every caller. Board card: the page readiness card.
- **Three theme items queued rather than taken on speculatively.** Channel commits `36102c77` and `72822d9b`: the quote page's missing real image (Kain's S362 ruling, and the whole CQ018 score ceiling), and the empty `<h1></h1>` that every article page renders, found during the live check and confirmed pre-existing on a page live since well before today. Board card: the theme queue.

## Started and not finished

- **The four AI wisdom articles at 89 are still not published.** `RULING__First_Publish_Is_Publish_Gate_Live_Unpublish_On_Fail_Four_AI_Articles_Go_Now_S362.md` meets the same wall as the DSM set: the article exemplar's chapter 9 carries a measured speed fail, and the gate refuses before `--override` is read. Its disposition line in FROM Chat says so. What remains: Chat's reading of the disagreement named below, or the speed work itself.

## Two things Chat is owed a decision on

1. **The publish gate and DSRD 3 disagree about when speed blocks.** DSRD 3 §4.4 says to run PageSpeed "again across the site before cutover" and names the SiteGround Dynamic Cache as a dependency "before cutover", so the standard times the speed investigation at go-live. The publish gate treats the same failing line as a blocker on publishing to a build ground that is hidden from search. That disagreement is what put Kain's own hands on the keyboard tonight. Code did not resolve it by writing an exception onto the exemplar's speed line: a real site-wide fault is not "genuinely does not apply", and writing one would have been a false readiness record.
2. **No book note page has a DSRD 6 record at all.** Checked this session across every record on disk: none declares a `/learn/book-notes/` address. So no book note can be cleared by the gate under the volume route, with nothing even to point `--exemplar` at. That is the job `BRIEF__Every_Published_Article_And_Book_Note_Gets_A_DSRD_6_Record_S358.md` names, and tonight is the first time it has blocked a publish rather than sat on a list.

No em or en dashes in this file; checked before writing.
