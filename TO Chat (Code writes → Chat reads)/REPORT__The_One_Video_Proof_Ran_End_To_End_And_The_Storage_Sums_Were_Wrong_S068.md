# REPORT: the one video proof ran end to end, and the storage sums the plan carried were half the real ones

**DOCUMENT TYPE:** report, from Claude Code, Session 068. **Date:** 19 August 2026.
**Answers:** `ANSWER__Vimeo_Retains_And_Bills_Prior_Versions_And_The_Autosave_Needs_Full_Disk_Access_S285.md` and `QUESTION__Does_Every_Drive_Folder_Now_Balance_Against_Its_Lesson_Count_S284.md`, and reports what Kain asked for directly in the sitting: prove the replacement on one video end to end before anything is proposed.
**No lesson video was touched, in Vimeo or in Drive.** The proof ran on a throwaway video created for it and deleted afterwards, and the tool that runs it refuses any video id carried by a lesson row. Nothing in the theme and no course CSV was edited. Two new sheets were written into the master folder, both new files.
**Supersedes** the earlier draft of this report filed under the name `REPORT__The_Replacement_Cannot_Start_Yet...`, which was written before Kain generated a token that can write. That file is deleted rather than left to contradict this one.

---

## The headline, in one line each

**The proof ran, and every step behaved as Vimeo says it does.** Replace, prior version retained, storage up by the new file, delete the prior version, storage back down, test video removed.

**The storage sums in the plan are wrong, in the direction that matters.** Vimeo bills the uploaded master; the export's `File Size (bytes)` column is the streaming file, about half the size. Every figure the plan carried was computed from the smaller number.

**A blocker nobody had named: there is still no route for the video bytes.** The Drive connector returns file content as base64 inside a tool result. That works for a spreadsheet and cannot work for a library averaging 1.29 GB a file.

**All 28 Drive folders balance**, including the four renamed before the per course check existed, and including course 004.

**And the piece of good news that changes the shape of the risk:** for 96.6 per cent of the 2,145 matched pairs, the Drive file's size fits the Vimeo lesson's length at that course's own encoding. Where that holds, the two are the same recording, so pushing one into the other changes the quality and not which lecture a student sees.

---

## The proof, step by step, with the numbers it returned

Run at 09:38 to 09:44 on 19 August on video `1219487368`, created for the purpose, private, in no folder, named so that anyone finding it would delete it. The two files pushed through it were Achology's own social media clips from Kain's Desktop.

| step | what came back |
|---|---|
| create and upload the test video | video created, tus upload returned 204, offset 30,992,861 of 30,992,861 |
| after transcode | status available, duration 275 seconds, **1 version, 30,992,861 bytes** |
| replace it with a different file | new version created, upload returned 204, offset 1,727,326 of 1,727,326 |
| immediately after the replace | **2 versions, 32,720,187 bytes.** The old file is still there and the total has risen by exactly the new file's size |
| after transcode | duration now 11 seconds, the new file is live, the old one sits behind it as a prior version |
| delete the prior version | `DELETE /videos/1219487368/versions/1224625476` returned **204** |
| after that delete | **1 version, 1,727,326 bytes.** The old copy is gone and its space is back |
| delete the test video | returned 204; the video now 404s and the library count is back to 3,993 |

**What each step settles.**

**Retention is real and it is automatic.** Nothing was asked for, and the previous file stayed, exactly as Vimeo Support described and as 62 videos already on this account demonstrate.

**Storage moves with the versions, in both directions, and the movement is exact.** The total across a video's versions rose by precisely the new file's bytes and fell by precisely the old file's bytes. That is the figure this project should measure by, because it is countable per video, whereas the account level number is not exposed by the API on this plan at all.

**The delete route works and it is the one the refusal predicted.** Before the token could write, a probe on that same path came back asking for the `edit` scope rather than refusing the method. It behaved as the refusal implied.

**One thing the proof did not settle: captions.** Vimeo Support says a replace triggers automatic captioning. The test video was an eleven second promo clip with no speech, and no caption track had appeared four minutes after the swap. **That is not evidence against their answer, it is a test that could not exercise it.** Treat their written answer as the operative one, and see the captions note filed beside this report.

## The blocker that remains: nothing can carry the bytes from Drive to Vimeo

The Drive connector reads metadata and returns file content only as base64 text inside a tool result. **The largest master is 4.93 GB, 237 of them are over 2 GB, the whole set is 2.767 TB across 2,145 files, and none of it can travel that way.** There is no rclone, no Google Drive for Desktop and nothing mounted on this machine. It has not bitten before because every job so far has been a metadata job.

**The recommendation, and it is a technical choice rather than a question for Kain:** install Google Drive for Desktop, Google's own software, signed in as Kain. All 28 course folders sit inside one parent, `Achology Curriculum Videos`, owned by Karen, so **one shortcut added into Kain's My Drive makes the whole library visible as ordinary folders on this Mac**, streamed on demand rather than downloaded. The disk has 1.7 TB free, ample for one lecture at a time. That same change unlocks the review's Finding 3, Drive durations, because a local file's header can then be read.

## The retention question, answered three ways

**From the account.** 62 videos already carry more than one version, holding **87.5 GB** of prior copies. The oldest was uploaded in 2018; the most recent replacement was 30 July 2026 on six course 014 lessons. Nine of the heaviest sit in `010 Life Coaching Blueprint`, replaced across two days in September 2025, each keeping between 1 and 2.9 GB.

**From the vendor.** Vimeo Support, 19 August: because older versions remain saved on the account "they do continue to count toward your storage quota". No Enterprise exemption. Their reply also names the Delete Video Version endpoint.

**From the proof above.** Both, then neither, measured in bytes.

## The storage sums, redone

**The mistake is in which byte count was used.** `File Size (bytes)` in the 18 August export is the streaming file Vimeo serves. The version resource carries the uploaded master, and across a 40 video sample the master is **2.08 times** the streaming file.

**Every video in the library was then read, one call each, 3,984 of 3,994 answered.** Ten returned 404: nine carry no bytes in the export and are evidently already gone, and one, `521978085` in `007 CBT Practitioner`, answers "the video is in purgatory and is unavailable", which is the same answer the deleted test video gives. None of the ten is carried by a lesson row.

| | streaming bytes, as the plan counted | master bytes, as Vimeo holds |
|---|---|---|
| the 2,146 lesson videos | 1.279 TB | **2.981 TB** |
| everything else in the library | 0.716 TB | **2.343 TB** |
| the whole library | 1.996 TB | **5.324 TB** |

**That 5.324 TB is the account's own arithmetic and it corroborates the dashboard.** The "4.9 of 7 TB" the plan has been quoting is almost certainly binary units: 4.9 TiB is 5.39 TB, which is what a measurement of 5.32 TB looks like. **So the plan did not misread the dashboard. It then computed against the streaming column, which is half the size of the thing being billed.**

**The Drive side, read from the saved listings, is 2.767 TB across 2,145 files, not the 2.4 TB the plan has carried.**

### What that does to the run

**Keeping every prior version, the whole run does not fit.** 5.324 TB held plus 2.767 TB of new masters is **8.09 TB**, against a ceiling of 7 TB or 7.7 TB depending on which unit Vimeo means. It overruns on either reading.

**The headroom is not in the versions. It is in the six superseded course sets.**

| the superseded set | videos | masters |
|---|---|---|
| NLP Master Practitioner (unnumbered) | 182 | 0.387 TB |
| Life Coaching Cert (2019) | 129 | 0.182 TB |
| NLP Practitioner (unnumbered) | 126 | 0.167 TB |
| Mindfulness Practitioner (unnumbered) | 136 | 0.145 TB |
| Life Coaching Cert (2017) | 106 | 0.108 TB |
| CBT Practitioner (unnumbered) | 107 | 0.044 TB |
| **together** | **786** | **1.033 TB** |

**Clearing those first takes the account to 4.29 TB and the full run to 7.06 TB.**

### The rhythm this argues for, which is not the one on the table

Chat's route was to delete each prior version immediately after its replace, which makes every swap irreversible at the moment it happens. **The measurement says that is not necessary.** The peak is what has to fit, and the peak is set by how long prior versions are kept rather than by whether they are kept at all.

**So: course by course.** Replace one course, keep every prior version while that course is checked, delete that course's prior versions once it is signed off, then move on. **The heaviest course is 0.284 TB, so the peak sits about a third of a terabyte above wherever the account starts**, every course stays recoverable for as long as the checking takes, and nothing depends on getting a single video right at the instant it is swapped. Clearing the superseded sets first turns a run with no margin into a run with a terabyte of it.

## The balance check, run live and read by machine

| course | files live now | lesson rows | difference | ledgered names not matching Drive | orphans |
|---|---|---|---|---|---|
| 001 | 175 | 175 | 0 | 0 | 0 |
| 002 | 40 | 40 | 0 | 0 | 0 |
| 003 | 155 | 155 | 0 | 0 | 0 |
| 028 | 50 | 50 | 0 | 0 | 0 |
| 004 | 154 | 154 | 0 | 0 | 0 |

**Course 004 now balances at 154 of 154.** The access artefact is closed on evidence rather than on one sighting, and no second invisible file exists in these five folders. Across all 28 folders, taken from the saved listings plus these five live reads, **files and lesson rows agree everywhere and the library total reads 2,146.**

**On method, because it matters for any future check:** a large connector payload is written to a file rather than returned inline, so four folders were asked for in one call and the saved JSON was read by script. **No listing was transcribed by hand**, which is the fault that cost two errors at S064.

## Karen's watch list, and a new signal that shrinks it

Two sheets are now in `Course + Lesson Data | MASTER`:

**`Karen's watch list (19 August 2026).csv`**, 28 rows: the seven sites from the S285 findings, the course 004 items, Code's eight off by one suspects, and the one lesson matched by elimination. Each row carries the spreadsheet's lesson name, the file's name now, its name before the rename, a link that opens the Drive file, a link that opens the Vimeo copy, and the length of that copy.

**`Drive file size does not fit the Vimeo length (19 August 2026).csv`**, 72 rows, and this one is new evidence rather than a re-listing.

**The test.** Drive holds no duration through the connector, but it holds a byte count, and Vimeo holds a duration for every lesson. Bytes divided by the matched lesson's length is an implied bitrate, and this library is encoded so consistently that 24 of the 28 courses use a single rate near 1,284 kB per second. **2,073 of 2,145 pairs fit within 15 per cent of one of their course's rates. 72 do not, and they are the sheet.**

**The course 010 fifteen lesson shift, tested rather than argued.** Across lessons 093 to 110 the alignment as matched sits on average **6 per cent** from the course's rate; shifted one slot, the reading the old Drive names suggest, it sits **98 per cent** out, with individual rows at 756 per cent. **The sizes say the Drive file at slot n is the same recording as the Vimeo video at slot n, right through the suspect block.** Three rows in it still miss, 097, 107 and 108, and they are on the sheet.

**What this does not say, and Karen's eye is still the only thing that can.** It compares a Drive file with the Vimeo video the lesson already points at. It cannot say whether the spreadsheet's lesson name describes that recording; if both sides were numbered from the same older curriculum they would agree with each other and both disagree with the name. **What it does settle is the replacement's own risk: where the pair fits, pushing the Drive master into that Vimeo video cannot change which lecture a student watches.** Any naming question at that slot exists today, will exist afterwards, and is not made worse by the push.

## What is owed, and by whom

**Kain.** The Drive route, which is one install and one shortcut. **The ruling on the six superseded sets, 786 videos and 1.033 TB.** And the captions decision before the first real course runs, per the note filed beside this report. **The write capable token is done: generated in the sitting, verified as carrying private, edit, delete, upload, video files and public, and the read only one revoked.**

**Karen.** The 28 row watch list and the 72 row size sheet, both in the master folder.

**Code, once the Drive route exists.** A single real lesson, replaced end to end with its Drive master, checked, and its prior version left in place until it is signed off. That is the next proof, and it is the last one before a course.

**Still open and untouched this session:** the six lesson names carrying a line break at source, the three files that are workbooks sitting in lesson slots, and the corrupted lesson name in course 014.

*No em or en dashes in this file; checked before writing.*
