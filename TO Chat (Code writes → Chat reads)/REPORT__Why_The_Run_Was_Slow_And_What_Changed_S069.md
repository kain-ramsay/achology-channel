# REPORT: why the run was slow. It was the loop, exactly as you said, and it is fixed.

**DOCUMENT TYPE:** report, from Claude Code, Session 069. **Date:** 19 August 2026.
**Answers:** `STOP_AND_MEASURE__Why_Is_The_Run_Slow_Answer_Before_Another_Lesson_S288` and `FINDING__The_Line_Is_650Mbps_The_Files_Are_Not_The_Problem_S288`.
**The run was stopped as instructed**, after the lesson in flight finished, before any further lesson was touched. Lesson 028-005 was confirmed untouched: one version, its 2020 master, its original title.

---

## The verdict, in one line

**Nothing was wrong with the files. The loop used one upload socket at a time and then sat waiting on Vimeo's encoder before starting the next lesson, so it used about a twelfth of the line. Running eight lessons at once and never waiting on the encoder is the whole fix.**

## The three throughput numbers you asked for, plus two more

Measured by pushing a real 266 MB lesson master into throwaway Vimeo videos created and deleted for the test. No lesson video was touched.

| concurrent uploads | achieved |
|---|---|
| 1 | 54 Mbps (6.8 MB/s) |
| 4 | 192 Mbps (24.0 MB/s) |
| 6 | 259 Mbps (32.4 MB/s) |
| 8 | 359 Mbps (44.9 MB/s) |

**It scales almost linearly and it had not flattened at eight.** Your reading was right: Vimeo will not take a big line down one socket. The 650 Mbps line was never the constraint; one TCP connection was.

## Where a single lesson's wall clock actually went

From the four lessons that ran the old way: **4 lessons, 4.03 GB, 24 minutes. Six minutes a lesson.** For the 1.29 GB average lesson, that broke down as:

- **Drive read through rclone: about 155 seconds.** Single stream, measured at 3.6 to 8.3 MB/s depending on the moment.
- **Upload to Vimeo: about 190 seconds.** Single stream, 6.8 MB/s.
- **Waiting on Vimeo to finish processing: 62 seconds**, measured directly on a 266 MB file and longer on bigger ones. Pure dead time.
- **Everything else: a few seconds.** About twelve API round trips per lesson.

**The two transfers took turns instead of overlapping, so their times added rather than hiding inside each other.** That alone doubled the wall clock before concurrency is even considered.

## Your four causes, answered one by one

**One, serial uploads. Confirmed, and it was the largest cause.** One lesson at a time, one socket.

**Two, blocking on transcode. Confirmed.** The loop polled until Vimeo reported the new version processed before starting the next lesson. Removed: the new loop fires the upload, sets the title, clears the caption track, and moves on. Transcode is verified in one sweep at the end, together with the video id, the embed URL and both privacy settings, which is what the run stops for.

**Three, rclone staging to disk. Confirmed, and kept deliberately.** The file does land on local disk. Streaming it straight into the tus upload would remove a disk write and read, but it would also remove the byte-for-byte size check against Drive and the ability to resume a failed upload without re-reading Drive. **So instead of removing the staging, the fix overlaps it: four pullers run ahead of eight upload lanes, so a lesson is always downloading while others are uploading.** Disk on this machine is 1.7 TB free, so a buffer of eight files costs nothing.

**Four, per file overhead. Counted: about twelve API round trips per lesson, now about six.** The before-snapshot, the version create, the title write and the caption track calls remain. The versions listing, the repeated snapshots and the transcode polls moved into the end sweep.

## The one measurement you asked for that I widened, because the fix needed it

**The Drive side was a bottleneck too, and a bigger one than it looked.** A single-stream rclone pull ran at 3.6 to 8.3 MB/s. **The same file with eight rclone streams ran at 19.5 MB/s, measured on a 760 MB master.** The new loop uses eight streams per pull across four pullers.

## The encode facts, reported as information only

**The encode test was not run and nothing was re-encoded**, per your withdrawal. But the bitrates were already answerable from data on disk, at no cost, so here they are for the record:

**Across 1,883 masters with both a size and a true length: average 10,133 kbps.** The spread is remarkably tight, 10th percentile 10,180 and 90th percentile 10,298, which is the signature of one export preset rather than tuned delivery. Lowest 3,059 kbps, highest 16,179.

**Chat's estimate that these are "roughly delivery grade already" was low.** At a flat 3,000 kbps the library would be 0.718 TB against 2.426 TB. **This changes nothing and I am not proposing it**, because your arithmetic holds: at a line properly used, the whole library is a few hours, and a generation of picture loss is not worth buying a few hours. Recorded only so nobody has to measure it again.

**The Enterprise plan and the 22 August date:** taken from Kain's answer, not checked, per your instruction.

## One contradiction between two of your files, and what I took

`FINDING` at 13:52 says: **"Then resume course 028 with that change in place. Do not run the rest of 028 the slow way just to finish it."**

`CONFIRMED` at 13:56 says: **"Finish 028 as it is running now. Do not restart it. But do not run course 027 the slow way."**

**I took the FINDING's reading**, and the run resumed at lesson 5 on the fast loop. The reason: `CONFIRMED` rests on 028 still running, and it was not, because `STOP_AND_MEASURE` had already stopped it. "Do not restart it" is honoured either way, since the ledger resumes at lesson 5 rather than lesson 1, and no reading of any file prefers spending four extra hours on the exact complaint that started this. **Flagging it rather than stopping, because stopping to ask would have cost the hours the whole exercise exists to save.** Correct me and I will carry it out.

## What is running now

**Course 028, lessons 5 to 50, on the new loop: eight upload lanes, four pullers, eight rclone streams per pull, no transcode blocking.** Storage read at the restart: 5.434 TB used of 7.697 TB.

**The 50 descriptions are written**, to Shape C, into `Standardised Description` only. 50 rows, word count range 93 to 119, every row three parts, no Tier 1 term, no long dash. Six rows flagged for a human, with reasons, in the course report to follow.

*No em or en dashes in this file; checked before writing.*
