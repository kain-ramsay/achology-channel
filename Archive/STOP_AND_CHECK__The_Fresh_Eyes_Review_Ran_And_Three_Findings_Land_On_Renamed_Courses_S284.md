# STOP AND CHECK: the fresh-eyes review ran, and three of its must-fix findings land on courses already renamed

**DOCUMENT TYPE:** stop-and-check. Read this before renaming another course. Not a page spec. Not a new commission. **From:** Claude Chat, Session 284. **Date:** 18 August 2026.
**Why it exists:** the fresh-eyes review Kain ordered at S283 DID run, and its findings file was sitting unread in the Project Delivery System folder while tonight's rename went ahead. Chat found it at the close of S284 and read it in full on Kain's word. Nobody withheld it; nobody knew it was there.
**Source document:** `REVIEW__Fresh_Eyes_Findings_On_The_Course_Video_Plan_S284.md`, in the Project Delivery System folder. Read it whole; this file carries only what changes what you do next.

---

## What is asked of you, in one line

**Do not rename another course until Kain has ruled on Finding 1 below.** Nothing that has been renamed needs undoing tonight. Nothing is lost. The undo record is intact on every row.

---

## The finding that stops the run

**The number-only match has already failed in at least two visible places, and both are in courses you have renamed.**

The reviewer read the comparison CSV by eye for courses 001 to 004 and found two rows where number and content visibly disagree:

**Course 001, lessons 018 and 019: the Part order is crossed between the two sources.**

    001-018  CSV:   19 Perspectives on the Meaning of Life (Part 2)
             Drive: DMAP 018 Contemplating the Meaning of Life Part 1.mp4
    001-019  CSV:   19 Perspectives on the Meaning of Life (Part 1)
             Drive: DMAP 019 Contemplating the Meaning of Life Part 2.mp4

**Course 003, lessons 134 and 135: two Drive files both claim Part 1.**

    003-134  Drive: NLPPRAC 134 Breaking Habits with Conversation (Part 1) Demonstration.mp4
    003-135  Drive: NLPPRAC 135 Breaking Habits with Conversation (Part 1) Demonstration.mp4

The CSV says 135 is Part 2. Either 135 is misnamed, or it is a second copy of Part 1 and Part 2's video is not in Drive at all.

**Why this matters more than a wrong filename.** The rename is recoverable: `Drive File Name` still holds the original on every row. The replacement is not. If a mislabelled file is later swapped into Vimeo on the strength of that number, the wrong lecture plays for paying students, and the balance checks stay green throughout because the counts are all correct.

**These two were found by one instance reading four courses of a twenty eight course file.** The exception class exists; its size is unknown.

## The two other must-fix findings that touch renamed work

**Course 004 has zero name corroboration.** Every Drive file there is a bare code (`2020MNLP002.mp4` and so on), so on 153 of 154 rows the name check corroborates nothing. It is also the course that was missing lesson 001, and "the welcome video is missing" and "every file sits one slot early" produce an identical table from the outside. Four files in that folder carry unexplained versioning marks: `2020MNLP027-016.mp4`, `2020MNLP073-014.mp4`, `2020MNLP047UPDATE.mp4`, `2020MNLP053b.mp4`. A file with two numbers, in the one course with no name corroboration, is the most suspicious object in the library.

**The Drive durations were never captured**, so the plan's one identity signal that is neither a name nor a number does not exist on the Drive side. The map holds name, ID and size only. Duration is in Drive's video metadata and was simply not asked for.

## What Chat recommends, for Kain to rule

These are recommendations, not instructions. **Do not act on them until Kain says so.**

1. **A mechanical ordinal-disagreement pass over the comparison CSV**, read-only: flag every row where the two names disagree on an ordinal (Part 1 against Part 2, a numeral, a section reference). This is a small script and it produces a short list rather than a re-audit of 2,145 files. The two pairs above go on that list whatever it finds.
2. **Karen watches the opening seconds of each flagged file and rules**, plus five files in course 004: `2020MNLP002`, the two double-numbered files, the UPDATE file and the b file.
3. **One read-only metadata pass adding duration** to the Drive listings and a `Drive Duration Seconds` column to the CSVs. It can run after the rename, but it must exist before any replacement plan is agreed.
4. **Copy the twenty eight CSVs and the Drive listings into the channel repository, dated**, so the undo record stops living in one folder on one machine. One commit. The reviewer names this as the thing that breaks reversibility.

## What the review found clean, so the record is fair to your work

The split and its execution: every count cross-checked across six documents and consistent. The sanitisation rules: every dirty-name class covered, collisions structurally impossible, rebuilding from the CSV rather than editing old names judged sound. The rename mechanism itself: targeting by ID, batched with read-back, original name never overwritten, reverse run stated. The order of works: no ordering fault except that no step anywhere decides how a Vimeo video gets matched to a lesson, which is Finding 4 of the review and is Kain's to settle before the replacement plan.

*No em or en dashes in this file; checked before writing.*
