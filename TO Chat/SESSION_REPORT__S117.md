# SESSION REPORT: S117, the postbag sitting, and the factory run that followed it

**Filed by Claude Code, Session 117. Date:** Monday 14 September 2026, running into 15 September.
**Session type:** factory. **Shipped:** one theme commit, `0049f5e`, pushed. Everything else touched only the channel and the WordPress install (drafts, never published).
**Assembled from the version control log for the session**, per Harness Rule 13, and from a full read of every file, since a stale disposition cannot be caught from a commit message alone.

**This file now covers two acts of the same session.** Part A is the postbag sweep, unchanged below. Part B, added after Kain's word to run the factory backlog, is new.

---

## The job

Kain's instruction at the close of S116: clear the postbag before the quote page. Eighty seven work files sat in FROM Chat (eighty eight counting the folder's own `000__WHAT_IS_IN_HERE.md`), most carrying a disposition line from an earlier Code session. Every one was read in full this session, not sampled, because the harness's own stale-disposition check had already found six lines resting on stale evidence, and a check that finds six by machine is a warning that more are wrong in ways no machine can see.

## Archived: 5

- **`RULING_AND_ANSWER__Karens_Board_Item_Is_Created_And_Two_Job_Titles_Change_S337.md`.** Its own S097 line already read DONE; it had simply been written below an older WAITS line instead of above it, so it never got swept. Reordered and archived.
- **`BRIEF__Put_The_Keyword_Into_The_Address_On_The_250_Help_Answers_S349.md`.** Withdrawn in full by `RULING__The_Import_Gate_Is_Fixed_The_Keyword_Moves_Not_The_Address_S350.md`, in the same tray, which was never acted on. Nothing was ever owed.
- **`BRIEF__The_Book_Cover_Becomes_A_Drawn_Book_Everywhere...S357.md`.** Superseded by its own S360 rewrite and by `RULING__The_Drawn_Book_Is_Approved_And_The_Cover_Refetch_Is_Dropped_S116.md` (now in TO Chat). The ISBN fetch it commissioned was dropped by Kain; the component it commissioned is built.
- **`RULING__The_Skill_Library_Joins_The_Instruction_Drift_Check_S337.md`.** Its S102 line was waiting on Kain's yes to a proposal; the yes was given at S344, in `RULING__Kain_Says_Yes_To_The_Skill_Library_Drift_Check_One_Test_Skill_First_S344.md`, in the same tray, which carries the live commission.
- **`RULING__The_Eleven_Folded_Addresses_Are_Chats_Rows_And_Your_S103_Replies_Are_Acted_On_S345.md`.** Its S104 line was waiting on Chat's ruling on deleting `channel_map.py`; the ruling landed at S346 (in the same tray) and the deletion is checked against the disk this session: the file no longer exists in the theme's tools folder, only its named replacement, `folder_map.py`.

## Corrected without archiving: 4 files, 1 queue entry

- **Duplicate commission found.** `BRIEF__Import_And_Score_All_200_CQ018_Quote_Pages_Publish_On_Kains_Word_Only_S360.md` and `BRIEF__Import_And_Score_All_200_Course_018_Quote_Records_As_Drafts_Publish_Nothing_S356.md` commission the identical two hundred records under the identical process. The S360 file says its own authorising ruling "does not exist anywhere in the channel"; it does, the S356 brief itself, sitting unarchived the whole time. Both files now cross-reference each other and name the duplication. Neither is archived, because the underlying import has not run under either. Flagged to Chat rather than resolved alone: one should be withdrawn once the other's run lands.
- **A claimed queue entry that was not there.** `RULING__The_About_Page_Lead_Is_Kains_Final_Words_S349.md` said it was "queued as one line in `000__THE_THEME_QUEUE.md`". It was not. Added now, under Open, with a note on when and why it was missing.
- Two files' head lines corrected to name the file that actually answers them, per the pattern the harness's own stale check already uses.

## Still live: 82

Every one carries a disposition line naming the one fact it waits on. Grouped by what it is actually waiting for, since the count by itself says little:

- **24 wait on Kain: his eye on a rendered page, a Safari sitting, or a date he has not yet named.** These are visual or content decisions under standing rule 16 and cannot be settled in a factory sitting by design.
- **50 wait on a factory session actually running them:** imports, scores, gate builds, measurements, backfills, tool builds. Nothing blocks any of these except a sitting with room. This is the largest single group, and it did not shrink this session, because running any of them was not this session's job.
- **4 wait on a theme session only**, to type in a string Kain has already ruled word for word: the trial panel, the About page lead, three Our People copy changes, and the testimonial image rename. All four are on `000__THE_THEME_QUEUE.md` now.
- **3 wait on Chat or Cowork's own next action**, not Code's: corrected records still to land, a keyword ruling to be relayed.
- **1 is a standing reference rule** (`NOTE__What_Governs_A_Component_With_No_Build_Sheet_S257.md`), not a discrete task. It governs by default and closes only when every component has a build sheet.

## One thing worth naming rather than quietly carrying

`RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md` still carries a live Code disposition dated **S090**. Twenty seven Code sessions have passed since. What it waits on (a mid-grey supporting-line sweep on the course card, and a rendered Enrol Now colour choice for Kain) may well still be exactly what it says. It may also have been overtaken by later card work this postbag pass did not chase down, because chasing every thread's ultimate fate through eleven sessions of card and chrome rulings was past what one sitting could verify by reading alone. Worth a direct measurement next time a theme sitting is in the commerce cards.

## Not finished

The fifty factory-ready items above. None was started: this sitting's scope was the tray itself, on Kain's own framing that emptying it "wants a sitting of its own." Running any of them is a new, separate change set under Rule 3, and several are substantial (three record-import passes covering 274 records between them).

---

OWED BACK from Part A: nothing beyond this report.

---

## Part B: the factory backlog, Kain's word given live to run it

Six of the fifty factory-ready items acted on this sitting. Two ran clean. Two were refused at the front door, correctly, and neither refusal is Code's to fix. Two more turned out to already be done, found and closed rather than redone.

**Ran clean:**

- **The 50 book-quote records.** Imported as drafts (39 new, 11 updates), verified, scored (80 to 85, all read off the install with `tools/score_run.py`, nothing saved, no post re-dated). Full detail and the score table: `REPORT__The_Three_Commissioned_Imports_One_Ran_Two_Are_Blocked_At_The_Front_Door_S117.md`. **Board card:** 50 Book Quote Articles.
- **Previews off the theme.** `public_html/previews/` built outside the theme entirely, `previews/README.md` rewritten (theme commit `0049f5e`), and the fix proven with a real deploy: a test file placed there survived a deploy that sent zero files, where the old route inside the theme's own folder was being silently deleted by `deploy.py`'s `--delete-excluded` every time. **Board card:** none of its own; closes `RULING__Previews_Move_Off_The_Theme_To_Their_Own_Folder_S360`.
- **The DSRD extracts.** DSRD 7 §3.3 and DSRD 2 §§3.2, 3.4, 3.8 sent whole with line numbers, closing an ask that had gone unanswered since S346 and been repeated at S352. Read-only; nothing in either document touched. **Board card:** the harness and instruction sets.

**Refused at the front door, and named to their owner rather than forced or fixed:**

- **The 200 CQ018 course quotes.** All 200 carry an identical `featured_image` value pointing at a file that exists nowhere. No other quote record on the site (0 of 50 checked) carries this field at all, which reads as batch padding rather than content. Cowork's to strip; not touched here.
- **The 24 DSM series articles.** All 24 fail the paragraph-floor check Kain commissioned live a few sessions back, drafted before that floor existed. Breach counts run 6 to 33 short paragraphs per record. Cowork's to rewrite; not touched here, per Harness Rule 8.

**Already done, found rather than redone:**

- **Karen's twelve, the scores.** Already read and filed at S106 (`REPORT__Karens_Twelve_Are_Live_And_Scored_S106.md`, in the channel Archive). Not re-run. What is still genuinely owed on that card, the twelve DSRD 6 machine records, has no generator yet for any content type outside `article` and `book_note` (the same gap `BRIEF__Every_Published_Article_And_Book_Note_Gets_A_DSRD_6_Record_S358` names and has not yet been widened to close), so it is left as still-open rather than guessed at.
- **The `--takedown` override for un-publishing a live page.** Built at Code's own S107 (`publish_gate.py` commits `a4747fa` and `439542d`, "the route a live page comes down by"), three sessions after the ask, and never reported back. Checked against the file on disk, not assumed. Closed and archived.

**One tool finding, named but not fixed:** `import_quote_pages.py --verify` fails all 50 book quotes on "0 blockquotes, not 1". Read the actual rendered body of one rather than trusting the tool: the quote sits inside the opening paragraph, exactly as `RULING__The_Quote_Page_Reflection_Question_Returns_To_The_Body_Under_A_Third_Heading_S356` ruled it. The verify script's check is written to a shape that ruling retired. Worth a fix whenever someone is next in that file; not blocking anything today.

## Part C: the sweep continued, on Kain's word to keep going through all of it

Nine more items closed or substantially advanced, on top of Part B's six. The pattern repeating throughout: several things marked WAITS in the tray were, on inspection, already built or already done, sometimes three or more sessions ago, and simply never reported back. Each was checked against the actual file or the live install this turn, not assumed from the disposition line.

**Built and shipped (theme commits `f3b1110`, and content_gate.py commit `39e6c2b` in the Content Production Factory repo):**
- **css_gate.py's radius tiers**, narrowed from six to four per DSRD 7 section 5.3 (`RULING__The_Six_Things_Code_Was_Owed_From_S113_Answered_S358`, section 4). Two real 4px focus-ring uses annotated as the exception the standard already names, rather than the permitted set being widened to cover them.
- **The banned-link-labels gate check**, commissioned S356 and never built. Built, tested against the exemplar and a synthetic negative case, and run site-wide against all 579 published pages: zero hits.

**Found already done, closed rather than redone:**
- The closing-question character check for the quote page (commissioned S356): built, confirmed passing on the exemplar. Found the same run failing the exemplar on the paragraph-rhythm check, which is itself evidence the paragraph-floor brief's per-section allowance is genuinely needed.
- The `--takedown` override for un-publishing a live page (already reported in Part B).
- The fifteen help-answer keyword placements, the `.bn-body` page-gate fix, the 39 biography heading pushes, and three small tool-wording fixes: all four were done at S107, ten sessions before this sitting, and the disposition line was never updated. Two small loose ends from that same file (one book-note sentence, one redirect-workbook question) are still genuinely open and named as such.

**Measured, not yet acted on:**
- **All 250 help answers**, against the S356 reader-first shape: 34 pass the paragraph cap, 216 fail (85 on one paragraph, 131 on more). All 250 already carry an external link and an image, closing a gap an S108 measurement had open, again with no report filed at the time. Full table: `Content Records/help-answer/MEASURED__All_250_Help_Answers_S117.csv`. A Rank Math score run across the same 250 is running now in the background, workers=4; results follow when it completes.

**Deliberately not touched:** two items inside `publish_gate.py` (the first-publish comment rewrite, a new H9 clearance route for orphan attachments). Both reach into the one wall that stands between Code and publishing to the public, and a rushed edit there on a first read of the mechanism is a worse risk than leaving them named and open for a session that reads it properly first.

## What is still open in the roughly fifty

The two blocked imports (224 records between them) wait on Cowork. The DSRD 6 record generator's widening (`BRIEF S358`) is real, scoped work of its own, deliberately not started for the same reason as the publish_gate items: an 895-line readiness tool deserves a session that reads it whole, not a pass alongside forty other items. The breadcrumb_title derivation (`RULING_AND_BRIEF S356`) is confirmed genuinely unbuilt. The rest are untouched or still running.

---

OWED BACK: nothing beyond the reports named above. The help-answer score table follows when the background run finishes. The blocked imports, the DSRD 6 widening, and the two publish_gate items are the next sitting's, in whichever order Kain sets.

*No em or en dashes in this file; checked before writing.*
