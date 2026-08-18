# COMMISSION: flag every row where the two names disagree about an ordinal, read only, list first

**DOCUMENT TYPE:** commission. Read-only. Approved by Kain in session, S284. Not a page spec. **From:** Claude Chat, Session 284. **Date:** 18 August 2026.
**Runs before:** any further renaming. Course 014 and everything after it waits on the list this produces and on Kain's ruling over it.
**Reads with:** `STOP_AND_CHECK__The_Fresh_Eyes_Review_Ran_And_Three_Findings_Land_On_Renamed_Courses_S284.md`, filed beside this, and the review it summarises.

---

## Why this exists, standalone

The whole Drive to lesson map rests on matching by number, because 83 per cent of lesson names disagree between the spreadsheet and Drive. That was the right call: names are unreliable and numbers are not. **But the fresh-eyes review found two places where the number match and the content visibly disagree, and both are in courses already renamed:**

    001-018  CSV:   19 Perspectives on the Meaning of Life (Part 2)
             Drive: DMAP 018 Contemplating the Meaning of Life Part 1.mp4
    001-019  CSV:   19 Perspectives on the Meaning of Life (Part 1)
             Drive: DMAP 019 Contemplating the Meaning of Life Part 2.mp4

    003-134  Drive: NLPPRAC 134 Breaking Habits with Conversation (Part 1) Demonstration.mp4
    003-135  Drive: NLPPRAC 135 Breaking Habits with Conversation (Part 1) Demonstration.mp4
             (the CSV says 135 is Part 2)

Those were found by one reader eyeballing four courses out of twenty eight. **The exception class exists and its size is unknown.** A rename on a crossed pair is recoverable. A Vimeo replacement on one is not: the wrong lecture plays for paying students, and every count stays green throughout because the counts are all correct.

**This job finds the rest of them, cheaply, and hands Karen a short list instead of 2,145 files.**

## The job

**Read `Drive to Lesson name comparison (18 August 2026).csv` in the `Course + Lesson Data | MASTER` folder and flag every row where the two names disagree about an ordinal.**

An ordinal, for this purpose, is any token in a name that asserts position or sequence: `Part 1`, `Part One`, `(Part 2)`, `Session 2`, `Phase 1`, a bare trailing numeral that is not the lesson number itself, `i`/`ii`/`iii`, `A`/`B` used as a part marker, `Demo 1`, `Continued`, `cont`.

**Flag a row when both sides carry an ordinal and the two ordinals differ.** A row where only one side carries an ordinal is a separate, weaker flag: report those in their own list rather than mixed in, because a name that simply dropped its part marker is far less alarming than two names that both assert a position and disagree.

**Do not flag** rows that merely reword the lecture. Those are the expected 83 per cent and they are not this job's business.

## What comes back

**One file in the master folder, named for its date, plus a report in TO Chat.** For every flagged row: the Lesson Key, the spreadsheet lesson name, the Drive file name, the ordinal read from each side, and whether the file has already been renamed. Sorted by course, hard disagreements first.

**In the report, four numbers stated plainly:** rows checked, hard disagreements found, single-sided ordinals found, and how many of the hard disagreements sit in the courses already renamed.

**Include the two pairs above whatever the script decides**, so the list is never shorter than what is already known.

**Say plainly if the answer is zero beyond those two.** That is a real and useful result, not a disappointing one: it would mean the exception class is tiny and Karen's checking is a ten minute job.

## The boundaries

**Read only. Nothing is renamed, moved, downloaded, replaced or edited by this job**, and no CSV is written except the new flag file. No Drive call is needed at all: everything comes from the comparison CSV already on disk.

**Do not rule on any flagged row.** Do not decide which side is right, do not correct a spreadsheet name, and do not adjust the map. **Every flagged row is Karen's to settle by watching the opening seconds of the file, and Kain's to rule on.** A row you find obvious is still theirs: the entire point of this job is that the machine cannot see content.

**Do not rename another course until Kain has ruled on the list.** Courses 001, 002, 003, 004 to 013 and 028 stay as they are; nothing is undone.

## One thing to say back if you disagree with the method

If reading the comparison CSV is not the cheapest route to this list, or if the ordinal definition above misses a shape you can see in the data, say so before running it rather than after. The method matters less than the list; it exists to be improved by whoever is looking at the actual rows.

*No em or en dashes in this file; checked before writing.*
