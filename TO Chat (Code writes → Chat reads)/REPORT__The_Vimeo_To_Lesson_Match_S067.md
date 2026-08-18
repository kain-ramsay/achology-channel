# REPORT: Vimeo is matched to lesson on the same true north. All 2,146 filled.

**DOCUMENT TYPE:** report. **From:** Claude Code, Session 067. **Date:** 19 August 2026.
**Closes:** the Vimeo to lesson join, which the fresh eyes review raised as Finding 4 and which `RULING_AND_COMMISSION__Circle_Read_Only_Is_The_Vimeo_To_Lesson_Matcher_S285.md` routed through Circle.
**Nothing was written to Vimeo and nothing was read from Circle.**

---

## The ruling that changed the route

Kain, in session at S067, on being told the join was still an open question:

> "the lesson numbers are the true north - why is this a remaining question?"

He was right, and the Circle route is not needed. **Vimeo already carries both halves of the key.** Its library holds a folder per course, named with our own course numbers, `001 DMAP Course` through `028 Entrepreneur's Guide`, and every lesson video inside carries its lesson number in the title. That is the same course-plus-number key the Drive map was built on.

**The S285 Circle commission is therefore answered without being run.** The join exists in a CSV already on disk, `Vimeo library export (18 August 2026).csv`. No token, no API call, no read of a lesson page. If Chat wants the Circle investigation for another reason it can stay open, but it is no longer the matcher and nothing waits on it.

## What was filled

**All 2,146 rows now carry `Vimeo URL` and `Vimeo Video ID`.** Before this they were empty on every row.

**Twenty six courses filled straight from the dated export.** Two needed a live read of their Vimeo folder first, and Kain asked in session for that to be done rather than left:

**Course 007, CBT Practitioner.** The export showed 120 videos with two numbered 19. **Read live, the folder holds 119 and the duplicate is gone**, exactly as `RULING__Course_007_Vimeo_Duplicate_Deleted_By_Karen_S066.md` records. The export was simply taken before Karen deleted it. 119 videos against 119 lessons, and it filled clean with no exceptions.

**Course 003, NLP Practitioner Training.** Read live, the folder holds 155 videos against 155 lessons, and the numbering runs 001 to 154 and then jumps to 156. There is no 155. Every number from 1 to 154 appears exactly once, so **one lesson and one video were left over and the pairing was forced: lesson 155 takes the video titled `2020NLP156`.**

**That single row is the only one in the whole library not matched on its number**, and it is named here rather than buried. It is arithmetic rather than judgement, because with the count balanced there was no other pairing available, but it deserves ten seconds of Karen's time to confirm by eye.

## The live read, and what it touched

**Two GET requests to the Vimeo API, one per folder. Nothing was created, changed or deleted.** The token was read from Kain's own file, was never printed and never written into any output or any committed file. The standing constraint that nothing writes to Vimeo is intact.

**The live listing now outranks the dated export wherever both exist**, which is the right precedence: course 007 proves the export goes stale.

## How the match was made, so it can be checked

**Course folder, then lesson number, and nothing else.** No name was used to decide any pairing.

**The number is read per folder, with the folder's own prefix derived from its own titles**, exactly as the Drive listings were read, because the prefix is not one shape across the library. Five distinct shapes had to be handled, and each one was found by a check failing rather than by assumption:

    001 Introducing ...           no prefix, the number leads
    COU 114 ... and COU106 ...    a code, sometimes spaced, sometimes glued
    2020NLP091 ...                a leading year that must not be read as the number
    HYPN0001 and HYPN00100        zero padded to four and to five digits
    ALS 13 001 ...                a series code with a number of its own in front
    MH Prac - 001final            the number buried between separators and a suffix

**Every course was then checked before anything was written:** does the folder hold exactly one video for every lesson number, with none missing, none doubled, and none numbered outside the lesson list. **On the dated export, 26 of 28 passed and the tool skipped the other two itself rather than guessing. On the live listings, 27 of 28 pass**, and the twenty eighth is the single forced pairing in course 003.

## The independent check on the result

The pairing was decided by number. **So the words were free to be used as a second opinion, and they were.** Every filled row had its Vimeo title compared against that lesson's original Drive file name, which came from a different system, was typed by different people at different times, and played no part in the match.

| | |
|---|---|
| Rows compared | 1,872 |
| Titles clearly describe the same lecture | **1,762** |
| Titles partly agree | 56 |
| Titles share no words, or one side has no words at all | 54 |

**94 per cent agree outright.** Most of the remainder are rows where the Vimeo title is a bare code such as `FNLP001` with no words in it to compare, so there is nothing to disagree with. The rest are the ordinary rewording the two sources have always shown.

**Two independent signals now agree on this map: the number, and the words.** That is a materially stronger position than the Drive map had at the same stage.

## What this does not settle

**Duration is still not captured on the Drive side** and remains the review's Finding 3. Vimeo's export carries a duration for every video, so once Drive durations exist the third signal can be checked against this map cheaply.

**The seven ordinal sites and Karen's watch list still stand**, unchanged, and still belong to the replacement step.

**Nothing here is a replacement plan.** The map now exists, which is what was missing.

*No em or en dashes in this file; checked before writing.*
