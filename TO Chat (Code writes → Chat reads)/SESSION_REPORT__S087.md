# SESSION REPORT: S087

**From:** Claude Code, Session 087, 26 August 2026.
Assembled from the theme's version control log for the session, per Harness Rule 13, with hand-added lines marked. Five change sets in the log, all committed, pushed and deployed; the theme reads CURRENT on all three deploy proofs.

---

## Finished

**The publishing wall, H9, built and accepted.** Commit `1adc522`. Nothing in the harness guarded content going live, because every other hook watches file edits and publishing touches no file; 116 pages went live at S086 unchecked. Filed as `RULING__The_Publishing_Wall_Is_Kains_S087` and `REPORT__The_Publishing_Wall_And_The_Search_Runner_S087`. Board: Plugins and Site Configuration.

**DSRD 6 chapter 5's missing machine half, built.** Same commit. Items 1, 3, 5, 6, 7 and 11 had no runner anywhere; `page_gate` carried only 4, 9 and 10 of the nine the standard assigns the machine. Closes `COMMISSION__Five_More_Chapter_Five_Machine_Checks_S305` and step 5 of `BRIEF__The_Site_Wide_Rank_Math_81_Bar_By_Page_Type_S309`. Board: page readiness.

**The keyword density counter.** Commit `6dc6626`. Ruled by Kain in session after his placement rule was measured and talked out of on the evidence. Filed as `RULING__The_Density_Counter_Is_Built_Not_A_Placement_Rule_S087`, which also answers gap 6 of the S316 dry run. Board: Knowledge Hub scoring.

**The wall widened to taking a page down, and a hole in it closed.** Commit `fb6f396`. Closes `RULING__The_Publishing_Wall_Widens_To_Taking_A_Page_Down_S317`. Filed as `REPORT__The_Wall_Widens_And_A_Hole_In_It_Is_Closed_S087`. Board: Plugins and Site Configuration.

**The false zero scores, diagnosed and fixed at source.** Same commit. Two biographies were filed as scoring zero; they score 80 and 74, and the fault was in the reading instrument rather than the pages. Corrected in both filed reports rather than quietly. Board: Knowledge Hub scoring.

**The per-test reader.** Commit `4e63161`. Reads which individual Rank Math tests each page fails, which had never been read here. Found that `hasContentAI` fails on every page of both types and always will, being a paid add-on: a fourth test to refuse alongside the three title ones. Board: Knowledge Hub scoring.

**The wall's blind spot on the real importers, closed.** Commit `2d01135`. The scripts that import and publish every Knowledge Hub article live outside the theme, so ground B could not see them. Board: Plugins and Site Configuration.

**The retro score table across all 116 published pages.** Filed as `REPORT__The_Retro_Score_Table_65_Book_Notes_And_51_Biographies_S087`. Closes job 2 of `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315`. Its finding: all 65 book notes carry no Rank Math field at all, because the importer's `META` map writes nine keys and none of them is one. Board: Knowledge Hub scoring.

**SearchWP checked on all three counts, verdict clean.** Filed as `REPLY__SearchWP_Checked_Before_The_Licence_S087`. Closes `RULING__SearchWP_Stands_Check_It_Before_The_Licence_Is_Bought_S311`. Board: Plugins and Site Configuration.

**The demand screen on all 116 published pages.** Filed as `REPORT__The_Demand_Screen_On_The_116_Published_Pages_S087`. Sixteen of the 51 author names already earn 184,752 impressions on the live site at poor positions; not one of the 65 book notes covers any of the 80 live book pages that earn. Board: Knowledge Hub scoring, and book note selection.

## Started and not finished

**The book note page Safari sitting**, Kain's third job and the only one needing him in the room. Not started. It has grown to four things that must move in one pass: the five headings ruled at S314, the template itself, the section header component, and the import fix that unblocks all 65 book notes.

**The five page density experiment**, `BRIEF__The_Five_Page_Density_Experiment_S318`. Not run. Its step 1 asks the counter to read records on disk while the counter reads the install; the mismatch is named in that file's own disposition line, with a recommendation.

## Hand added, no machine record

**Kain's ruling that the density question is closed by a counter rather than by a placement rule**, taken live in the sitting after he asked directly not to be agreed with.

**Kain's ruling to run the demand screen**, same sitting. Both are hand added because neither travelled the channel on the way in, and the report is their only route out.

## One thing Code owes itself, found at the close

`publish_gate.py` has a deadlock: a clearance requires every machine check to pass, and a page scoring under 81 fails the score check, so a page below the bar can never be updated into passing it. The gate blocks the work that would satisfy it. Named here so the next session opens on it.

*No em or en dashes in this file; checked before writing.*
