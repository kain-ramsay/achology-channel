# REPORT: 14 of the 25 book notes never imported are up as drafts at 88; 11 held, each named with its reason

**From:** Claude Code, factory session, S129, Tuesday 22 September 2026. **To:** Claude Chat.
**Answers:** item 5(b) of `TASK_LIST__The_Thirteen_Finished_Cowork_Jobs_Waiting_On_You_In_Push_Order_S370.md` ("153 records are on disk and 125 pages are published: which 28 are not on the install, and why?").
**Board card:** Book notes.

## The answer to 5(b)

Twenty-five real book note records are not on the install (the other three of the 28 are reports sitting in the folder), and none exists under any address, in the bin or in any hidden state. Every one reads `post_status publish` in its record, which is why they looked published from the record side. They are the S106 set that waited on covers: Cowork's `CORRECTION__The_Twenty_Six_Covers_Are_Codes_Sourcing_Job_Not_Kains_S106.md` names them, Code sourced 25 of 26 covers at S106, and the batch was never imported after.

## What was done

`tools/book_note_import.py` (H9 re-hashed after reading its five changes since review; create still hardcodes draft, update carries no status): master first, upload sheet regenerated (706 rows), then the install. **14 created as drafts, 14 of 14 on the site, each with its cover attached.** Scores read off the editor, nothing saved:

| Post | Book note | Score |
|---|---|---|
| 37026 | before-happiness | 88 |
| 37028 | bittersweet | 88 |
| 37030 | embracing-uncertainty | 88 |
| 37032 | further-along-the-road-less-travelled | 88 |
| 37034 | leader-effectiveness-training | 88 |
| 37036 | necessary-endings | 88 |
| 37038 | notes-on-a-nervous-planet | 88 |
| 37040 | quit | 88 |
| 37042 | running-on-empty-no-more | 88 |
| 37044 | shift | 88 |
| 37046 | surrounded-by-psychopaths | 88 |
| 37048 | the-high-5-habit | 88 |
| 37050 | the-stoic-challenge | 88 |
| 37052 | the-way-to-love | 88 |

88 is the book note bar Kain ruled at S344 (one image, the cover), so all 14 pass and are ready for his publish.

## The eleven held, and what each waits on

**Nine carry an S310 re-verification line reading "FAILED, awaiting escalation"** in their own notes: `born-for-love` (the person shift between sections), `come-together`, `critique-of-practical-reason`, `meditations-for-mortals`, `mothers-who-cant-love`, `on-the-tranquility-of-mind`, `originals`, `talking-to-crazy` (unsourced biographical facts about the author), `the-quick-and-easy-way-to-effective-speaking` (course facts not confirmed read from DSRD 4 or 5). Some may have been cleared since: `talking-to-crazy` and `originals` both appear in Cowork's S349 "all seventeen pass" second read. Code does not judge that. **Waits on:** Chat saying, per record, whether its S310 line is cleared.

**Two have no cover on disk:** `the-tao-of-fully-feeling` (the one of the 26 not sourced at S106), and `a-new-guide-to-rational-living`, which is also the 1975 revised edition of a book already live as `a-guide-to-rational-living` (post 33788). **Waits on:** a ruling whether the revised edition earns its own note, then its cover; and the Tao cover.

## Noted on the way

`stage5_import_checks.py` reads the book note folder against the article field list (article_type, rm_focus_keyword and the rest), so it marks every book note FAIL, the 125 live ones included. It cannot tell a ready book note from an unready one today; named, not fixed.

## OWED BACK

The nine S310 lines, cleared or not, per record; the revised-edition question; the Tao cover.

*No em or en dashes in this file; checked before writing.*
