# BRIEF: build the course video rename map, and stop before renaming anything

**From:** Claude Chat, Session 260. **Date:** 2026-08-11.
**Authority:** Kain, in session. He ruled the key and the filename rule himself; both are recorded below in his own decision.
**What this asks for:** the map only. No file is renamed in this job.

## 1. Why this exists

Karen has finished the course video Drive tidy. There is now one folder, "Achology Curriculum Videos", holding 28 course folders numbered 001 to 028, all present, every number matching DSRD 5 section 1. It is shared to Kain's Google account and mounted in his Finder through Google Drive for desktop, so you can reach it on the Mac.

The videos and the master lesson data do not agree. Filenames carry course-specific prefixes rather than course numbers (DMAP on 001, 2023LCC on 009, HYP on 013, and others), and many lesson names differ substantively from the master workbook rather than cosmetically. Some files carry a number and a name; some carry only a number.

Everything downstream waits on this being reconciled: the Vimeo reconciliation map, the bulk replace, the transcript harvest, and the Transcript Pipeline card behind them.

## 2. The two rulings this job runs on

**The key, ruled by Kain at S260.** Course number identifies the course. Lesson number identifies the lesson. Names are descriptive and are never identifiers.

Chat verified the key holds before writing this: across all 28 sheets, lesson numbers run continuously from 1 to N within each course, with no restart at section boundaries and no duplicate numbers anywhere. So the two-part key is sufficient and Section is not part of it.

**The filename rule, ruled by Kain at S260.** A colon cannot appear in a macOS filename and 663 lesson names contain one, so colons become dashes. The full rule, which Chat has already run over the master and confirmed produces 2,146 unique names with no collisions and a longest name of 85 characters:

- Target filename is `{course number} {lesson number zero-padded to 3} {cleaned lesson name}.mp4`
- `: ` becomes ` - `, and a bare `:` becomes ` - `
- `/` becomes ` or `
- `\` becomes a space
- `"` `*` `?` `<` `>` `|` are removed
- runs of whitespace collapse to one space, and the name is trimmed

Worked examples from the real data:

```
001 001 Introducing the Diploma in Modern Applied Psychology.mp4
001 011 The Basis of Aristotelian Ethics.mp4
001 012 John Locke - All Ideas Originate From Experience.mp4
001 100 Triangulation - The Karpman 'Victim' Drama Triangle.mp4
```

## 3. Before you start, one thing must be true

**The master workbook on the Mac is stale.** Chat found eight corrupted lesson names in it, where accented characters and apostrophes had broken into gibberish at some point in the file's history. Karen corrected all eight this session and returned a clean file, and Chat verified the corrections landed and that no corruption remains anywhere in the 2,146 rows.

Kain is saving that corrected file over the master under its existing canonical name, in the Course + Lesson Data MASTER folder, per that folder's own Read Me rule that a replacement is saved over the exact name and the superseded copy goes to Archive.

**Check before you read it.** Sheet 001 lesson 011 must read "The Basis of Aristotelian Ethics" and sheet 003 lesson 065 must read "The Ten 'Creative' Solution-Focused Questions". If either still shows the old corrupted text, the replacement has not happened; stop and say so through the channel rather than building a map from stale names.

## 4. What to produce

Read the master workbook and derive the target names yourself using the rule in section 2, rather than taking a copy of a list from Chat. One truth, generated from its source, so nothing drifts.

Then read all 28 folders on the Finder mount and match each file to a lesson on course number plus lesson number, taking the number from wherever it sits in the current filename.

Return one spreadsheet, one row per video file plus one row per unmatched lesson, carrying: course number, lesson number, current filename, target filename, and a status of one of these five.

- **matched** — file and lesson row agree on the number, rename is straightforward
- **name differs** — matched, and the current name is materially different from the master name, so the rename is a real content change rather than a tidy
- **no lesson row** — a video file whose number has no lesson in the master
- **no video file** — a lesson row with no video carrying that number
- **ambiguous** — two or more files in one folder claiming the same lesson number, or a file whose number cannot be read

Alongside it, state four counts: files found, lessons in the master (expect 2,146), matched, and unmatched in each direction.

## 5. What not to do

**Rename nothing.** Kain reads the exceptions first. The rename is a separate job, commissioned after he has seen this map, and it runs as a dry run before it runs for real.

**Do not correct the master workbook.** If the map shows a lesson name that looks wrong, it is a finding for the map, not an edit. The workbook is Karen's and its corrections go through her.

**Do not touch the four cosmetic folder-name differences** Chat found against DSRD 5 (002 missing an apostrophe in "Beginners", 016 and 019 using an ampersand where DSRD 5 spells out "and", 008 carrying a trailing space). They are recorded and they do not affect matching, because matching is on number. Leave them.

## 6. One question worth answering in the same return

Course 001 holds 175 lessons in the master and its highest-numbered video is 175, but DSRD 5 records 179 lectures for that course. The DSRD figure came from the Udemy instructor dashboard, so the two may simply be counting different things. If your file listing settles it, say so; if it does not, say that instead rather than reasoning it out.

*No em or en dashes in this file; checked before writing.*
