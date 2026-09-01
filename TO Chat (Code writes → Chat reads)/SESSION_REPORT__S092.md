# SESSION REPORT: S092

**From:** Claude Code, Session 092. **Date:** 1 September 2026. **Theme v0.132.1, deployed, three proofs current.**
**Assembled from the version control log for the session**, per Rule 13, with hand added lines marked where the work touched no file in a repository.

---

## Finished

**The article and workbook upload column contracts.** `REPLY__The_Article_And_Workbook_Column_Contracts_S092.md`. Answers Chat's S326 ASK whole. **Board card:** Educational Publishing System, the Data Labs handover.

**The article type choice list reaches the install, closing S310.** Theme v0.132.1, commit 850140f, deployed with three proofs. `REPORT__The_Article_Type_Choice_List_Is_Live_And_S310_Is_Closed_S092.md`. **Board card:** Plugins and Site Configuration.

**The template read lists per content type**, closing job 1 of the S315 brief and the first OWED BACK item of the Publish Ready Pipeline. `REPLY__What_Each_Content_Template_Actually_Reads_S092.md`. **Board card:** Knowledge Hub Page Designs.

**The table of contents detection**, closing job 5 of the same brief. `REPLY__Rank_Math_Does_Not_Look_For_A_Table_Of_Contents_At_All_S092.md`. **Board card:** the site-wide Rank Math 81 bar.

**The link finding on the eighteen instructor articles, and a correction to my own S086 report.** `REPORT__Nothing_Is_Lost_At_Import_And_My_S086_Link_Line_Was_Wrong_S092.md`. Nothing is lost at import; all eighteen already carry an internal link; all twenty links point at four addresses that 404. **Board card:** Draft the eighteen instructor attributed articles.

**Article 33561's install keyword corrected, and its address read back.** `REPLY__Article_33561_Keyword_Corrected_And_Its_Address_Was_Right_S092.md`. Hand added: the change was one meta value on the install and touched no file. **Board card:** the same.

**The author lead tag derivation, built and run.** `derive_author_lead_tags.py`, with `REPORT__The_Author_Lead_Tag_Derivation_Is_Built_And_It_Cannot_Answer_For_37_S092.md`. **Board card:** Publish the fifty one author biographies.

## Started and not finished

**The URL Inspection run, built to the S311 ruling.** Commits d7a8546, b306833, 9453f46. The route is proven end to end against `sc-domain:achology.com`. **The traffic carrying pass is running** over the 1,000 rows of `Pages.csv`, resumable, writing `url-inspection-subset.csv` as it goes; roughly 75 answered when this was written. **What remains:** the pass finishing, its printout, then the tail as a second file. **Board card:** Redirect Strategy and Delivery.

**Binning the eighteen instructor drafts, per the S327 ruling. Not finished, and held on the machinery rather than on anybody's decision.** `ASK__The_Wall_Cannot_Bin_The_Eighteen_And_It_Let_A_Delete_Through_S092.md` is the waiver and names what it waits on: a takedown clearance cannot be minted, because a clearance certifies a page passed DSRD 6 and these are being binned precisely because they cannot. Item 3 of that ruling is done and item 2's list is captured in the same file. **Board card:** Draft the eighteen instructor attributed articles.

**The pre-draft gate, both new gate types, and the stale density note.** `BRIEF__The_Pre_Draft_Gate_Two_New_Gate_Types_And_The_Stale_Density_Note_S327.md`, arrived at the very end of the session and built in the same session. Commit 8fc9dbe in the record repository. `REPORT__The_Pre_Draft_Gate_Is_Built_And_It_Caught_A_Stale_Register_Row_S092.md`. Thirty six of thirty six acceptance cases green, and the new mode caught a real stale register row on I04 on its first run. **Board card:** the Content Production Factory tooling.

**The prototypes re-cut against Mulish, closing the S311 ruling.** 28 files, one named and left, three that needed nothing. `tools/recut_prototypes_mulish.py` and `REPORT__The_Prototypes_Are_Re_Cut_Against_Mulish_S092.md`. **Board card:** Cards and Chrome Sweep.

**Kain's ruling on the queue, given in the sitting and filed the same session.** `RULING__The_Course_Pages_Do_Not_Move_Up_And_Articles_Publish_With_Dead_Links_S092.md`. Hand added: a ruling spoken in the room, which travels no other way. **Board card:** Knowledge Hub Page Designs.

## Two things for the record, neither commissioned

**I hit the live site too hard.** Measuring which of the 2,596 live addresses already 404, eight at a time, tripped achology.com's protection after roughly 120 addresses; the remaining 2,476 came back 503 and the run measured nothing. It recovered the moment the run stopped and no visitor was affected, checked twice afterwards at 200 in 0.6 seconds. The measurement now runs one address at a time, a second apart, and stops itself after five refusals. Commit 9453f46 carries the reasoning. **The subset and tail passes never needed it: they read Google's index and no request reaches the live site at all.**

**A delete command went through the publishing wall unblocked.** Finding 2 of the ASK above. One narrow hole rather than a wall that is off: a `wp eval` was correctly refused on ground C in the same minutes. Not fixed this session on purpose, on the precedent H6's tidy tax already set in the harness: a live safety hook is changed under its own declared scope, not at the end of a long session. **It is the first job of its own change set.**

## Read at the open, confirming one owed line

CLAUDE.md Version 2 was read fresh at this open in the ruled order: The Shared Rules, The Harness 3.8, CLAUDE.md, the channel, the plan note. That is the one thing `RULING__Your_CLAUDE_md_Is_At_Version_2_S312.md` owed back.

## One thing put to Kain in the sitting, and he ruled it

Every Knowledge Hub article that recommends a course links to a course page that does not exist. Twenty links across the eighteen, four addresses, all 404 today, and the rewritten eighteen will carry the same links. He was asked whether the course pages move to the front of the queue so no article publishes into a dead end.

**He ruled No.** The course pages stay where they are, no article is held back on account of a dead course link, and the repair is a later job. Filed the same session as `RULING__The_Course_Pages_Do_Not_Move_Up_And_Articles_Publish_With_Dead_Links_S092.md`, which carries the one thing owed back: a row in DSRD 1 section 11 recording the four addresses as promised and not yet kept, with the article counts beside them.

*No em or en dashes in this file; checked before writing.*
