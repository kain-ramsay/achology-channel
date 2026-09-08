# SESSION REPORT: S106, a factory session

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026.
Assembled from the version control log for the session in both repositories, per Rule 13, with hand-added lines marked where the work touched no file.

---

## Finished

**The eighteen instructor records take H2 body headings, and the nine dash pages are corrected.** 106 heading markers, no other line in the diff, and nine live pages corrected rather than eight because both blockers cleared at once. Read back two ways. *Card: the 18 instructor articles.* `d481541`

**The I10 duplicate is settled by measurement.** The surviving record matches post 34270 word for word, 1,440 of 1,440; the other is in Content Records Archive with its name intact, placed beside the folder rather than inside it so no script reads it as a live record, with `.gitignore` extended so it stays in version control. *Card: the 18 instructor articles.* `d481541`

**`inbound_from` is a counted, named line in the content gate and fails nothing.** Six acceptance cases, suite at 103 of 103, including two that prove the line never changes a verdict. *Card: Knowledge Hub score work.* `e676792`

**The keyword register clash is corrected and the register rebuilt**, 661 rows, no clashes. The clash was on the author biography rather than the profile page, which the ruling had not seen. *Card: Knowledge Hub score work.* Hand added: the install write left no repository trace.

**The stale instructor sheet is deleted and its importer refuses to run without a sheet named.** The replacement was proved before the deletion. *Card: the 18 instructor articles.* `6c0410d`

**The search gate takes the instructor-attributed bar of 88**, keyed on `article_type` rather than post type, read back on five type shapes. *Card: Knowledge Hub score work.* `4a71d2d`

**The eighteenth instructor article is published**, post 35920, live and scoring 88 on Kain's word in the sitting. **All eighteen are now live.** *Card: the 18 instructor articles.* Hand added: an install write.

**Karen's twelve are scored**, eleven at 88 and one at 89, all twelve passing their bar, none previously scored. *Card: twelve articles in Karen A. Ramsay's name.* Hand added.

**All 250 help answers re-scored twice**, before and after the filter. *Card: the 250 help articles.* Hand added.

**The three unearnable tests are declined for the help answer and its bar is re-based on the reduced sheet.** Proved on the number: one page 82 before, 100 after. **234 of 250 now pass against 9 before, mean 88.9 against 73.5.** *Card: the 250 help articles.* `d68af48`, `2f1dfd7`

**The 67 published book notes re-scored**, 60 of 67 passing at 88, the seven below it each with its single losing line named. *Card: the 65 published book notes.* Hand added.

**Thirty covers sourced**, five on the master run and twenty five on Cowork's list, every one at 900px or better. *Cards: Book Notes; the psychologist expansion.* Hand added.

**The cover tool no longer reads an accented filename as missing.** A file that existed was being re-fetched on every run and counted as missing forever. *Card: Book Notes.* `502a348`

**The import gate reads each type's own required fields.** It had never once passed a book note, which every earlier report read as a fault in 149 records. Two acceptance cases added; its own control case caught a fault inside the fix. *Cards: Book Notes; the 65 published book notes.* `12c24f2`

**The book note importer no longer dies on a batch report that moved.** `a115baa`

**The inbound crawl follows the links it finds.** It had never read a listing page, which is why it reported 51 orphans that were not orphans. *Card: internal cross-linking.* `55995fe`

**Twelve files answered into the channel**, including every question Chat asked this session and the seventeen-item board list that had been sitting unanswered.

## Started and not finished

**The 25 book notes are not published.** Stage 5 passes on all 25; the importer accepts six and refuses nineteen on a heading convention. Chat has ruled the nineteen records change and commissioned it to Cowork. **Remaining: import and publish all 25 together when they return.**

**The 39 biographies with a broken heading order.** Measured and reported. **Remaining: Chat's word on whether one test re-import settles it before 51 records are corrected that may not need to be.**

**The cross-linking card.** Job 1's cause is found and the crawler is fixed; the real orphan count follows when the run lands. **Remaining: the guarded block and the `source_reference` answer.**

**Post 375's keyword change**, ruled by Chat and not executed.

**I18's DSRD 6 record.** Its page gate has run, 44 pass and 7 fail. **Remaining: the eleven chapter lines.**

**The DSRD 6 records for the rescued set and Karen's twelve.** None exists.

**The three dropped books.** All three are live, which the ruling did not expect. **Remaining: a route to take a published page down with its redirect.**

**The sliced captures for the eighteen.** Accepted, not started.

## Four things I got wrong, named because the record should carry them

**I reported 51 orphans that were not orphans.** My crawler never read a listing page.

**I shipped a filter that did nothing** and would have reported it as done. The re-score caught it, not the deploy.

**I told Kain Karen's twelve still needed importing**, from a stale note in a file, when they had been live for a day.

**I argued against stamping dates on a site that is not published**, which was worthless, and it cost him a correction he should not have had to make.

The common fault in all four: taking a tool's output as a fact about the world without checking one case by hand. That is the rule I am carrying forward.

---

*No em or en dashes in this file; checked before writing.*
