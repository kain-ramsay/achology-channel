# THE LINE IS 650 Mbps. The files are not the problem. Your loop is.

**DOCUMENT TYPE:** finding and instruction, from Claude Chat, Session 288. **Date:** 19 August 2026.
**Supersedes:** `QUESTION__Can_The_Masters_Be_Made_Smaller_Without_A_Student_Seeing_It_S288` **in full. That question is withdrawn. Do not run the encode test. Do not re-encode anything.**
**Measured by:** Kain, at the machine you are running on, in session.

---

## The number

**Upload speed at your machine: 650.92 Mbps.**

## What that means, in one line

**The entire 2.767 TB library should upload in under ten hours. About sixteen seconds a lesson.**

The sums: 650.92 Mbps is roughly 81 MB per second. 2,767,000 MB divided by 81 is about 34,000 seconds, which is 9.4 hours. Per lesson, 1,290 MB average at 81 MB per second is under sixteen seconds of actual transfer.

**You are not getting anywhere near that, which is the whole finding.**

## The compression idea is dead, and Chat killed it rather than putting it to Kain

At this line speed, cutting every file by 40 per cent would save roughly four hours off a job that should take nine and a half. **That is not worth a day of anyone's work, and it costs a generation of picture quality on 2,146 lectures.** The question file is withdrawn. Do not spend a minute on it.

## Where the time is actually going. Check these four, in this order.

**One. Serial uploads against a very fast line. This is the most likely answer by a distance.** A single TCP connection to a cloud ingest endpoint rarely carries anything like 650 Mbps, whatever the line can do. **Vimeo will not take your whole pipe down one socket.** Six or eight concurrent uploads is how a line this size gets filled, and it is a change to how the loop is written, not to anything else. **Measure achieved throughput at one concurrent upload, then at four, then at eight, and report all three.** If it scales, that is the entire answer to Kain's problem and nothing else needs doing.

**Two. Waiting on Vimeo to transcode.** If the loop blocks until Vimeo reports the new version processed before it starts the next lesson, that wait is dead time and it dwarfs the transfer. **Fire the upload, record the ID, move on, and check processing separately in a sweep at the end.** Never block the queue on someone else's encoder.

**Three. rclone staging to local disk.** If the file lands on disk before the upload begins, every lesson pays a disk write plus a disk read on top of two network hops. Stream it if you can, and if you cannot, at least overlap the download of the next file with the upload of the current one so the two are never waiting on each other.

**Four. Per file overhead.** Authentication, metadata calls, the title write, the caption track delete, the version delete. At sixteen seconds of transfer per lesson, a handful of round trips per file is no longer a rounding error. Count them.

## What to send back

**Three throughput numbers at one, four and eight concurrent uploads, and the breakdown of where a single lesson's wall clock time actually goes.** Then one line: what is slow, and the change that fixes most of it.

**Then resume course 028 with that change in place.** Do not run the rest of 028 the slow way just to finish it.

## What has not changed

Everything else stands: course 028 first, the titles, the caption handling, the descriptions to Shape C, the full stop and report at the end of the course, and prior versions kept until Kain signs the course off.

*No em or en dashes in this file; checked before writing.*
