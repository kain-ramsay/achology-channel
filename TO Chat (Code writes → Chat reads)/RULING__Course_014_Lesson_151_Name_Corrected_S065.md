# RULING: course 014 lesson 151 is "The Becca Sessions (Phase 2 → Session 2 → Part 4)", corrected in the master

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14. Not a page spec. **From:** Claude Code, Session 65. **Date:** 18 August 2026.
**Ruled by:** Kain, in session, asked directly whether the name should read as its neighbours do. His words: **"Yes, that is correct, please fix it"**.
**Closes:** item 3 of `NOTE__Where_The_Course_Video_Stream_Stands_And_What_Chat_Must_Check_S064.md`, which routed this to Karen. It did not need to go to her.

---

## What was wrong

The master held a corrupted lesson name on one row of 2,146:

    course 014, lesson 151
    Lesson Name:  The BThe Becca Sessions (Phase 2 → Session 2 → Part 4)

Every neighbouring lesson in that block reads `The Becca Sessions (Phase 2 → Session 2 → Part N)`, and **the same row's own Lesson Description already opened with the correct form**, which is what made the diagnosis safe rather than a guess: the row disagreed with itself, and only one of the two readings had a stray `The B` in it.

## Why it mattered enough to stop the rename

**The rename builds every filename from `Lesson Name` exactly as it stands**, per `COMMISSION__Rename_Every_Drive_Video_From_The_Spreadsheet_Proposal_First_S283`. So the proposal carried this:

    014-151 The BThe Becca Sessions (Phase 2 → Session 2 → Part 4).mp4

That is a typo becoming a permanent filename on the only copy of a 2.77 terabyte library. Kain's own instruction at this session's open was that Step 2 does not run until this is fixed.

## What was changed, and it is three files rather than one

The correction was made at source and then carried into the two files derived from it, so no derived file still disagrees with the master.

| File | What changed |
|---|---|
| `014 Counselling Skills Practitioner Course (Beginner to Advanced).csv` | `Lesson Name` on the `014-151` row |
| `Drive rename proposal (18 August 2026).csv` | the proposed filename, and the raw lesson name column beside it |
| `Drive to Lesson name comparison (18 August 2026).csv` | the lesson name held for comparison |

**Read back after the edit:** the string `The BThe` no longer appears anywhere in the `Course + Lesson Data | MASTER` folder, and the proposal row now reads `014-151 The Becca Sessions (Phase 2 → Session 2 → Part 4).mp4`.

**Nothing else on that row was touched.** Not the description, not the Drive file name, not the Drive file ID, not the key.

## One thing deliberately left alone

That row's `Lesson Name` also carries **a line break inside the field**, which is one of the six named in the S064 note as a data fault rather than a style choice. Kain ruled the wording, not the line break, so it stands. The sanitisation rules collapse it on the way into a filename, so it does not reach the disc either way.

## What this changes for the record

**Item 3 of the S064 note is closed and does not need Karen.** Items 1, 2 and 4 of that note still do: the missing video on course 004 lesson 1, the extra Vimeo video on course 007, and whether she wants the six embedded line breaks gone at source.

**Step 2 of the rename commission is now unblocked on this count.** It still waits on Kain reading the proposal and saying yes, which is where it was always going to wait.

*No em or en dashes in this file; checked before writing.*
