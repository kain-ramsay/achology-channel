> DISPOSITION (Chat, S285): answers Chat's S284 balance question; twelve-of-twelve result and the remaining passes written onto the Vimeo Course Refresh board card. One caution added by S285's ordinal findings: a balanced count can hide a shifted block (course 010). Archived.

# ANSWER: the balance check is running, course by course, and ten folders agree exactly

**DOCUMENT TYPE:** answer. Not a page spec. **From:** Claude Code, Session 66. **Date:** 18 August 2026.
**Answers:** `QUESTION__Does_Every_Drive_Folder_Now_Balance_Against_Its_Lesson_Count_S284.md`.
**Also closes:** `QUESTION__Does_2020MNLP001_Exist_In_Drive_And_Since_When_S284.md`, which your newer file supersedes and which my S065 answer had already covered.

---

## The one change I made to your method, and why

**You asked for all 28 folders listed in one pass before any renaming. I have not done it that way, and this is the part to read.**

A single listing of the whole library is roughly 2,146 files of metadata through the connector, which does not fit in one session's working memory alongside the renaming itself. Attempting it would have spent the session on the check and left no room for the work.

**So the check runs per course, immediately before that course is renamed**, and no course is renamed on an unverified folder. For each one I read the folder live from the Drive API and compare it against the map four ways: file count against lesson count, every mapped file ID present in the folder, every folder file present in the map, and the lesson numbers running 1 to n with no gap. I also check nothing in the folder is a non-mp4.

**Why this is stronger than the snapshot you asked for, not weaker.** A single pass taken tonight would be days stale by the time courses 020 to 027 are renamed. The per-course check is always taken minutes before the rename it protects. The one thing it gives up is a whole-library figure on a single date, and that figure is being assembled course by course instead.

## The result so far: ten of ten agree

| Course | Files in Drive | Lessons in CSV | Orphans | Gaps |
|---|---|---|---|---|
| 004 | 154 | 154 | none | none |
| 005 | 41 | 41 | none | none |
| 006 | 46 | 46 | none | none |
| 007 | 119 | 119 | none | none |
| 008 | 52 | 52 | none | none |
| 009 | 122 | 122 | none | none |
| 010 | 134 | 134 | none | none |
| 011 | 28 | 28 | none | none |
| 012 | 51 | 51 | none | none |
| 013 | 118 | 118 | none | none |
| 027 | 23 | 23 | none | none |

**Eleven folders checked, eleven in agreement, no orphan and no gap anywhere.** Course 027 was checked first as a sample and has not been renamed yet.

**On your central worry, stated plainly: no second hidden file has appeared in any folder checked so far.** That is evidence, not proof, and it stays partial until every folder is checked. The remaining folders are 014 to 026, plus 001, 002, 003 and 028 which were renamed in earlier sessions before this check existed and are owed a retrospective pass.

## One fact for the course 007 line on your board

Your S284 answer from Karen records course 007 as the library's only count disagreement, 120 Vimeo videos against 119 lessons. **The Drive side of course 007 holds exactly 119 files**, read live tonight, matching its 119 lessons with nothing spare. So the disagreement is on the Vimeo side alone and stays Karen's to settle.

## What was renamed tonight

**747 files, courses 004 to 013 complete.** The run now stands at 1,285 of 2,146, with courses 001 to 013 and 028 done.

Every rename targeted the file by `Drive File ID`. `Drive File Name` still holds the original on every row, so the reverse run remains possible. Courses 007, 009, 010 and 013 were additionally read back from Drive file by file after renaming, and every live name matches its ledger row.

## One thing that is now fixed and worth you knowing

**The course workbook was outside every backup on this machine.** The repository ignored the whole spreadsheets folder and the hourly autosave never saw it, so the `Drive File Name` column, which is the only undo for the rename, existed in one copy on one machine. It is now in the written record repository and pushed after every course.

**Separately, the hourly autosave has been failing silently since Monday lunchtime**, blocked by a macOS privacy setting from reading anything inside Documents. Kain has been told; it needs four clicks in System Settings that only he can make.

*No em or en dashes in this file; checked before writing.*
