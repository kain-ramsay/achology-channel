# REPORT: the one video proof could not run, both blockers named, and the storage sums have to be redone

**DOCUMENT TYPE:** report, from Claude Code, Session 068. **Date:** 19 August 2026.
**Answers:** `ANSWER__Vimeo_Retains_And_Bills_Prior_Versions_And_The_Autosave_Needs_Full_Disk_Access_S285.md` (job one) and `QUESTION__Does_Every_Drive_Folder_Now_Balance_Against_Its_Lesson_Count_S284.md`, and reports what Kain asked for directly in the sitting: prove the replacement on one video end to end before anything is proposed.
**Nothing was written to Vimeo, Drive, the theme or any course CSV.** Every Vimeo call was a GET, plus four deliberately refused write probes that could not create or remove anything. Two new sheets were written into the master folder. Both are new files; nothing existing was edited.

---

## The headline, in one line each

**The one video proof could not run, and the reason is not storage.** The Vimeo token on this machine is read only, so no replacement of any kind can be made from here today.

**A second blocker nobody has named yet: there is no route for the video bytes.** The Drive connector returns file contents as base64 inside a tool result. That works for a spreadsheet and cannot work for a 1.5 GB lecture, let alone 2,146 of them.

**The storage sums in the plan are wrong, and they are wrong in the direction that matters.** Vimeo bills the uploaded master. The export's `File Size (bytes)` column is the streaming file, which is roughly half the master. Every figure the plan has carried was computed from the smaller number.

**Retention is no longer a documentation question. This account is already holding prior versions**, and they can be counted.

**All 28 Drive folders balance**, including the four that were renamed before the per course check existed, and including course 004.

**And one piece of good news that changes the shape of the risk:** for 96.6 per cent of the 2,145 matched pairs, the Drive file's size fits the Vimeo lesson's length at that course's own encoding. Where that holds, the Drive file and the Vimeo video are the same recording, and pushing one into the other does not change which lecture a student sees. It changes the quality and nothing else.

---

## Blocker one: the token is read only

`GET /oauth/verify` returns scope `private video_files public`. There is no `upload` scope and no `edit` scope, so:

```
POST   /me/videos                      -> 403 Your access token does not have the "upload" scope
POST   /videos/445607389/versions      -> 403 Your access token does not have the "upload" scope
DELETE /videos/445607389/versions/1    -> 403 Your access token does not have the "edit" scope
PATCH  /videos/445607389               -> 403 Your access token does not have the "edit" scope
```

**Two of those probes answer the question Chat could not settle from documentation.** The DELETE went to the version resource and came back with a scope refusal rather than a method refusal or a missing route. **So `/videos/{video_id}/versions/{version_id}` does accept DELETE, and what it wants is the `edit` scope.** Whether the deletion then moves the storage figure still has to be watched happening, but the route is real.

**What is needed:** a token carrying `private`, `video_files`, `upload`, `edit` and, if the 788 superseded videos are ever to be removed by machine, `delete`. That is Kain's to generate in his own Vimeo account and save over the file the read only token sits in. It is one page of tick boxes on Vimeo's developer site.

## Blocker two: nothing can carry the bytes from Drive to Vimeo

The Drive connector on this machine reads metadata and returns file content only as base64 text inside a tool result. **The largest master in the library is 4.93 GB, 237 of them are over 2 GB, the whole set is 2.767 TB across 2,145 files, and none of it can travel that way.** There is no rclone, no Google Drive for Desktop, and no other mounted route on this machine. This has not been a blocker until now because every job so far has been a metadata job.

**The recommendation, and it is a technical choice rather than a question for Kain:** install Google Drive for Desktop, Google's own software, signed in as Kain. All 28 course folders sit inside one parent, `Achology Curriculum Videos`, owned by Karen, so **one shortcut added into Kain's My Drive makes the whole library visible as ordinary folders on this Mac**, streamed on demand rather than downloaded. The disk has 1.7 TB free, which is ample for one lecture at a time. That single change also unlocks the review's Finding 3, Drive durations, because a local file's header can then be read.

## What replaced the proof: the retention question answered from the account itself

The versions connection carries a `filesize` for every version, live and retained, so the account can be read rather than reasoned about.

**62 videos on this account already carry more than one version, and 87.5 GB of prior copies are being held right now.** The oldest was uploaded in 2018; the most recent replacement was 30 July 2026, on six course 014 lessons. Nine of the heaviest sit in `010 Life Coaching Blueprint`, replaced across two days in September 2025, each keeping a copy of between 1 and 2.9 GB.

**So question 1 is settled on this account's own evidence: a replace keeps the previous version, and the previous version is still there years later.** Question 2, whether Vimeo bills it, is the one Kain's Enterprise email still has to settle, and it is the only part of this that a written answer can decide.

## The storage sums, redone

**The mistake is in which byte count was used.** `File Size (bytes)` in the 18 August export is the streaming file Vimeo serves. The version resource carries the uploaded master, and across a 40 video sample the master is **2.08 times** the streaming file.

**Every video in the library was then read, one call each, 3,984 of 3,994 answered.** Ten returned 404: nine carry no bytes in the export and appear to be gone already, and one, `521978085` in `007 CBT Practitioner`, answers "the video is in purgatory and is unavailable". None of the ten is carried by a lesson row, so none of them touches the replacement.

| | streaming bytes, as the plan counted | master bytes, as Vimeo holds |
|---|---|---|
| the 2,146 lesson videos | 1.279 TB | **2.981 TB** |
| everything else in the library | 0.716 TB | **2.343 TB** |
| the whole library | 1.996 TB | **5.324 TB** |

**That 5.324 TB is the account's own arithmetic, and it corroborates the dashboard.** The 4.9 of 7 TB figure the plan has been quoting is almost certainly binary units: 4.9 TiB is 5.39 TB, which is what a measurement of 5.32 TB plus a few weeks of drift looks like. **So the read is not that the plan misread the dashboard. It is that the plan then computed against the streaming column, which is half the size of the thing being billed.**

**The Drive side, read from the saved listings, is 2.767 TB across 2,145 files, not the 2.4 TB the plan has carried.** The largest single file is 4.93 GB and 237 of them are over 2 GB.

### What that does to the run

**Keeping every prior version, the whole run does not fit.** 5.324 TB held, plus 2.767 TB of new masters, is **8.09 TB**, against a ceiling of 7 TB or 7.7 TB depending on which unit Vimeo means. It overruns on either reading, which is the same conclusion Chat reached from documentation, reached again from measurement, and by a wider margin.

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

**Clearing those first takes the account to 4.29 TB and the full run to 7.06 TB.** That fits under 7.7 TB and not under 7.0 TB, and either way it leaves no room to be wrong in.

### The rhythm this argues for, which is not the one on the table

Chat's route was to delete each prior version immediately after its replace, which makes every swap irreversible at the moment it happens. **The measurement says that is not necessary.** The peak, not the total, is what has to fit, and the peak is set by how long prior versions are kept, not by whether they are kept.

**So: course by course.** Replace one course, keep every prior version while that course is watched, then delete that course's prior versions once it is signed off, then move to the next. **The heaviest course is 0.284 TB, so the peak sits about a third of a terabyte above wherever the account starts**, every course stays rollback-able for as long as it takes to check it, and nothing depends on getting a single video right at the instant it is swapped. **Clearing the superseded sets first is still worth doing, because it turns a run with no margin into a run with a terabyte of it.**

## The balance check, run live and read by machine

The four courses renamed before the per course check existed were re-listed from Drive this session and compared to their CSVs by machine, never by eye.

| course | files live now | lesson rows | difference | ledgered names not matching Drive | orphans |
|---|---|---|---|---|---|
| 001 | 175 | 175 | 0 | 0 | 0 |
| 002 | 40 | 40 | 0 | 0 | 0 |
| 003 | 155 | 155 | 0 | 0 | 0 |
| 028 | 50 | 50 | 0 | 0 | 0 |
| 004 | 154 | 154 | 0 | 0 | 0 |

**Course 004 now balances at 154 of 154.** The access artefact is closed on evidence rather than on one sighting, and no second invisible file exists in these five folders. Across all 28 folders, taken from the saved listings plus these five live reads, **files and lesson rows agree everywhere and the library total reads 2,146.**

## Karen's watch list, and a new signal that shrinks it

Two sheets are now in `Course + Lesson Data | MASTER`:

**`Karen's watch list (19 August 2026).csv`**, 28 rows: the seven sites from the S285 findings, the course 004 items, Code's eight off by one suspects, and the one lesson matched by elimination. Each row carries the spreadsheet's lesson name, the file's name now, its name before the rename, a link that opens the Drive file, a link that opens the Vimeo copy, and the length of that copy, so Karen can answer a row without looking anything up.

**`Drive file size does not fit the Vimeo length (19 August 2026).csv`**, 72 rows, and this one is new evidence rather than a re-listing.

**The test.** Drive holds no duration through the connector, but it holds a byte count, and Vimeo holds a duration for every lesson. Bytes divided by the matched lesson's length is an implied bitrate, and this library is encoded so consistently that 24 of the 28 courses use a single rate near 1,284 kB per second. **A pair whose implied rate fits none of its course's rates is a pair where the Drive file and the Vimeo video are probably not the same recording. 2,073 of 2,145 pairs fit within 15 per cent. 72 do not, and they are the sheet.**

**The course 010 fifteen lesson shift, tested rather than argued.** Across lessons 093 to 110, the alignment as matched sits on average **6 per cent** from the course's rate. Shifting the block one slot, the reading the old Drive names suggest, puts it **98 per cent** out, with individual rows at 756 per cent. **The file sizes say the Drive file at slot n is the same recording as the Vimeo video at slot n, right through the suspect block.** Three rows in it still miss, 097, 107 and 108, and they are on the sheet.

**What this does not say, and Karen's eye is still the only thing that can.** It compares a Drive file with the Vimeo video the lesson already points at. It cannot say whether the spreadsheet's lesson name describes that recording. If Drive and Vimeo were both numbered from the same older curriculum, they would agree with each other and both disagree with the name. **What it does settle is the replacement's own risk: where the pair fits, pushing the Drive master into that Vimeo video cannot change which lecture a student watches.** Any naming question at that slot exists today, will exist afterwards, and is not made worse by the push.

## What is owed, and by whom

**Kain.** A Vimeo token with the four scopes, saved over the read only one. The Enterprise email on whether retained versions are billed. A shortcut to `Achology Curriculum Videos` in his own Drive, once the Drive software is installed. **And the ruling on the six superseded sets, 786 videos and 1.033 TB**, which is the difference between a run with no margin and a run with a terabyte of it. That decision was already sitting on the board from S064 and it is now sized.

**Karen.** The 28 row watch list, and the 72 row size sheet, both now sitting in the master folder.

**Code, once the token exists.** The one video proof, run on a video created for the purpose rather than on a lesson: upload, replace, confirm the prior version appears, watch the storage figure, delete the prior version, watch it move back, then delete the test video. **Nothing about the proof needs a real lesson to be touched, and it should not touch one.**

**Still open and untouched this session:** the six lesson names carrying a line break at source, the three files that are workbooks sitting in lesson slots, and the corrupted lesson name in course 014.

*No em or en dashes in this file; checked before writing.*
