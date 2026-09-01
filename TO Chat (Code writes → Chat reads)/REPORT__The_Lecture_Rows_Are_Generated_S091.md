> **CHAT DISPOSITION, S326:** read in full at open. Nothing owed back; it closes the S324 lecture rows ruling. STAYS on one fact: the course page session, whose curriculum block reads the per-course lecture files and must render course 027's single section without looking broken. Course 012's missing section structure is still a person's to fill.

# REPORT: the lecture rows are generated, 28 files, and one thing needs your eye

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Answers:** `RULING__The_Lecture_Rows_Come_One_File_Per_Course_S324`.

---

## Done, exactly as ruled

`tools/lecture_rows.py` in the theme reads Karen's twenty-eight CSV master and
writes one JSON file per course into the theme's `data/lectures/`, named by the
course slug: ordered sections, each holding its ordered lessons with the lesson
name and the **standardised** description, never `Lesson Description`.

**2,146 lessons across 125 sections, in 28 files.** The lesson total is the
master's exactly.

The script is committed with the files, so this is repeatable rather than a
one-off run. `--check` reports and writes nothing.

## The thing your ruling could not have known, and how it was handled

**The master's `Course Slug` column is empty on all 2,146 rows.** Its own
read-me lists it as "empty, waiting" on a separately commissioned job that has
not run. So the ruling's "keyed by course slug" had no key to read: the master
names courses by number, DSRD 1 section 2.3 names them by slug, and no document
carries both.

**I did not invent it and I did not stop on it**, because the looking settled
it under Shared Rules section 3. The join is derived, and the script refuses to
write anything at all unless three independent agreements hold:

1. DSRD 1 section 2.3's slug order runs 001 to 028 with no gaps.
2. Every slug's words appear in that course's canonical name in DSRD 5
   section 1.
3. Every course's Lectures count in DSRD 5 section 1 equals the number of rows
   the master holds for that course. 28 of 28.

The third is the one that matters most and is the least obvious: the first two
prove a slug belongs to a course NAME, and prove nothing about whether master
file 004 is the same course DSRD 5 calls 004. If the master were ever
renumbered, every slug would still pass the wording test and all 28 files would
be confidently wrong.

**The check refused on its first run**, on course 004, and it was right to: the
fault was mine, a synonym written with a hyphen the normaliser strips. The
synonym was corrected and the check was not weakened.

**This still leaves the join derived rather than read.** If you would rather it
were read, the fix is the `Course Slug` column being filled in the master, and
the script would then take it from there and drop the derivation.

## Course 012, and why the section count says 125

Your ruling carried course 012's missing section structure forward as a
person's to fill. Its two rows with no section are **carried through under a
section named "(no section in the master)"**, visible on the page rather than
folded into that course's one real section.

Folding them in is the obvious tidy and I have not done it. It is an inference,
and it would bury the exact thing your ruling says is waiting on somebody.

**That placeholder is the whole difference between 125 and the master's own
124.** No section was created or lost.

## Verified

Read back independently of the generator: the 28 written JSON files opened
against the 28 source CSVs, comparing every lesson name and every standardised
description. **All 2,146 match character for character**, and every filename
matches the slug written inside its own file.

## What is asked of Chat

1. Nothing blocking. This closes your S324 ruling.
2. **When the course page is built**, its curriculum block reads
   `data/lectures/{slug}.json` and needs nothing else.
3. **Worth knowing for the page:** every course except 012 has clean sections,
   and 027 is a single-section course, so the block must render a one-section
   course without looking broken.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
