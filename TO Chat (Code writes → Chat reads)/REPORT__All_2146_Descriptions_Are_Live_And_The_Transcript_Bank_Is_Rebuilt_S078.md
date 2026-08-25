**DISPOSITIONED S306: read in full. Historical record, the finding it raised (list derived artefacts before bulk replacement) was already ruled at S305 and is now written into the Harness (Version 3.5, Rule 3). No further action. Board card: the video upgrade run.**

# REPORT: all 2,146 descriptions are live on Vimeo, and the transcript bank is rebuilt

**From:** Claude Code, session 078, 23 August 2026.
**Board card:** the video upgrade run.
**Closes:** `COMMISSION__Rewrite_All_2146_Standardised_Descriptions_To_V4_S294`.

---

## The three numbers

**Videos: 28 of 28 courses, 2,146 lessons, replaced and live.** The run closed at 10:55 on 23 August.

**Descriptions: 2,146 of 2,146 written to V4 and pushed to Vimeo.**

**Transcripts: 2,106 of 2,146 harvested from the new files.** Forty outstanding, named below.

## What was verified, and how, because "the log says so" is not evidence

Kain asked for absolute confirmation and would not take the run's own record for it. He was right not to. Each of the three was checked against Vimeo rather than against our ledgers.

**The videos.** All 3,801 videos on the account were read. Exactly 2,146 carry the new `NNN-NNN` naming, and cross-matched against the 2,146 lesson keys in the master sheets there are zero missing and zero extra: a clean one-to-one. Transcode is complete on every one. A 69-video random sample spanning all 28 courses was additionally checked row by row for title and status, with no mismatches.

**The six course 014 lessons flagged during the run** (147, 152, 157, 162, 167, 172) were inspected. All six are correctly named with exactly one active version. The extra versions are undeleted old copies occupying storage, not a correctness fault.

**The descriptions.** Gated before anything was sent, all 2,146 passing: four parts, a question first, no long dash. Each row was read back from Vimeo immediately after writing and compared character for character; a mismatch was treated as a failure, not a warning. Then the whole set was re-read in an independent pass: **2,146 checked, 0 differ from the sheets.**

**Before the push, the position was worse than anyone had said.** Fifteen courses still carried V3 text on Vimeo, compared directly and confirmed as not matching. Thirteen carried no description at all. Nothing from the V4 rewrite had ever reached the platform, because the commission deliberately held it until Kain's reading.

## Kain read, and approved

The commission required five full rows per course, original beside new, chosen across the course rather than from its opening. 140 rows across 28 courses were built as one page and opened in Safari. His words: *"I'm totally happy with this standard."* The push followed that approval and not before it.

## The two rows held since the beginning are written and live

**010-094** and **014-141** were the two rows nobody could write: 010-094 is the only blank source in 2,146, and 014-141's source paragraph belongs to the preceding lesson. Both waited on transcripts that did not exist.

The harvest produced both. Both are now written to V4 from the lecture itself, per `COMMISSION__Write_The_Four_Broken_Descriptions_From_The_Lecture_Audio_S294`, and both are live. **Nothing is held back any more.**

## The transcript bank was rebuilt, not topped up

**This is the finding worth carrying into DSRD.** The bank held 923 transcripts. Every one was harvested from video files that the upload run has since replaced, so all 923 were evidence about videos that no longer exist. Eight courses had no folder at all: 001, 003, 004, 009, 010, 014, 015 and 018, which is 1,170 lessons on its own.

The whole bank has been re-derived from what is live. 2,106 lessons now carry all three files in the established shape: the verbatim `.vtt`, the plain `.txt`, and the `.corrected.txt` with the house glossary applied. The glossary made 2,199 corrections across 867 transcripts, every context-sensitive one printed with its surrounding sentence and read before it was applied.

**The lesson generalises, and it is the same one as the stale audio at S049:** when a bulk replacement happens, everything derived from the old artefact is silently invalidated and nothing reports it. The derived thing has to be listed before the replacement runs, not discovered afterwards.

## The forty outstanding transcripts

Thirty-nine videos have **no caption track on Vimeo at all**, and one track returned a 404 on download. This is not simply generation still running: several of the affected videos were last modified on 19 and 20 August and still have nothing.

```
003-014  004-101  004-103  004-107  005-011  006-024  008-008  008-022
008-025  008-043  009-101  010-051  010-097  012-006  013-004  013-010
013-012  013-016  013-020  013-021  013-029  013-033  013-051  016-011
016-014  016-021  016-027  016-030  016-032  018-004  018-005  018-007
018-011  018-013  018-019  018-053  018-081  018-113  020-038
024-045  (track exists, download returned 404)
```

The harvester is resumable and skips anything already present, so re-running it costs nothing and picks up any that appear. Vimeo ticket #28738572 is open and this is worth adding to it.

## The upload slowdown, for the record

Between 19 and 22 August throughput fell to roughly a fifteenth of normal, then recovered abruptly at about 01:00 on 23 August with nothing changed at this end. Measured per connection: 0.40 MB/s in the hour before, 5.95 MB/s in the hour after. Vimeo's API support has confirmed there is no tus rate limit and has been sent the video IDs and the measurements.

Ruled out at this end, and worth recording so nobody re-derives it: the connection (617 Mbit/s measured free while uploads crawled), concurrency (12 lanes gave 80 Mbit/s, 20 lanes gave 26, so more connections made it worse), client faults (3 connection errors in 2,292 progress intervals), storage, and machine load.

## What DSRD needs from this

1. **The transcript bank's provenance.** It should say in writing that the bank is derived from the live Vimeo caption tracks, and must be re-derived whenever the underlying videos are replaced.
2. **The forty gaps** recorded as a known state rather than discovered again.
3. **A standing rule candidate:** before any bulk replacement, list what is derived from the thing being replaced. This is now the second time its absence has cost a rebuild.

*No em or en dashes in this file; checked before writing.*
