# REPORT: the Drive to lesson map is built, and one lesson in the library has no video

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Closes:** `COMMISSION__Make_The_Number_The_Common_Identifier_And_Map_Drive_To_Every_Lesson_S283.md`, in its final form.
**Nothing in Google Drive was opened, moved, renamed or downloaded.** Metadata only, read through the Drive connector.

---

## The four numbers, first

**2,146 lessons. 2,145 Drive videos. One lesson with no video. Nothing orphaned, nothing colliding.**

| | |
|---|---|
| Lessons in the twenty eight CSVs | 2,146 |
| Videos found in Drive | 2,145 |
| Lessons matched to a video by number | 2,145 |
| Lessons with no video | **1** |
| Drive files with no lesson row | **0** |
| Duplicate-number collisions | **0** |
| Rows now carrying a Lesson Key | **2,146 of 2,146** |
| Total size of the Drive library | **2,767,040,072,375 bytes: 2.77 TB decimal, 2.52 TiB binary** |

**The one gap: `004-001`, "Welcome to the NLP Master Practitioner training!"** Course 004's videos run 002 to 154 with no file numbered 001. Every other lesson in the whole library has a video.

---

## Step 3: the folder-to-course mapping holds

Every Drive folder was checked against the DSRD 5 section 1 name for its number before anything was matched, because if one folder were out of step the whole course would join to the wrong lectures and the report would still look clean.

**Twenty seven of twenty eight match the canonical name exactly** under the normalisation stated below. **One differs, by an apostrophe:**

| Course | Drive folder | DSRD 5 |
|---|---|---|
| 002 | A Beginner**s** Guide to Neuro-Linguistic Programming (NLP) | A Beginner**'s** Guide to Neuro-Linguistic Programming (NLP) |

That is punctuation, not identity. **No folder denotes a different course, so the join is safe and Step 4 ran.**

---

## The parsing rule had to be changed, and this is the most important thing in this report

**Your Step 4 rule (leading run of non-digits as the shortcode, then the digits after it) would have silently misfiled three entire courses.**

- **Course 006's files are named `2020 FUNCBT 15 ...`.** The name *begins* with a four digit year. Under the stated rule the shortcode is the empty string and the number is **2020**, for all 46 files. Nothing would have matched, and if the padding were trimmed differently it could have matched the wrong lesson.
- **Courses 027 and 028 are `PG 13 001 ...` and `PG 14 01 ...`.** The shortcode itself contains a number and is separated by spaces.
- **Course 017 changes width halfway through:** lessons 001 to 036 carry three digits, lessons 37 to 47 carry two. A fixed-width parser loses the last eleven.

**What was used instead:** for each folder, the longest common prefix across that folder's own file names is taken as the shortcode, and the digits immediately after it are the lesson number. That is derived from the data rather than assumed, and it reads all twenty eight correctly, including the three above. **Every listing file records the prefix that was used, so the rule is auditable per course.**

**This matters beyond today.** The rename commission will build new names from these old ones. If it is written to your original rule it will mangle courses 006, 017, 027 and 028.

## The shortcodes actually in use, one per course

`DMAP`, `UNLP`, `NLPPRAC`, `2020MNLP`, `NLPMH`, `2020 FUNCBT`, `CBT`, `CBTMH`, `2023LCC`, `LCCD`, `SKILL`, `SHP`, `HYP`, `COU`, `MIND`, `MINDMH`, `MINDLM`, `MH Prac -`, `PG1`, `PG2`, `PG3`, `PG4`, `PG5`, `PG6`, `PG8`, `PG9`, `PG 13`, `PG 14`.

**No course uses more than one shortcode.** Every file in every folder shares its course's prefix, which is what the prefix derivation proves as a side effect.

---

## Karen's statement about the folders, confirmed by machine

**She said there is nothing in these folders but lecture videos: no resources, no bonus files, no older duplicates, no subfolders. That is exactly what was found, in all twenty eight.**

**Subfolders: 0. Non-video files: 0.** Every one of the 2,145 files carries a `video/mp4` MIME type. Reported as plainly as an exception would have been.

**One file is worth her eye even so.** `MINDMH 006 Growing in Self-Awareness Downloadable Resource.mp4` in course 016 is 57 MB, where the smallest real lecture in that course is 141 MB. It is an mp4 and it holds a numbered lesson slot, so it is not a stray file, but its name says "Downloadable Resource" and its size says it is not a lecture.

---

## Per course

Columns: Drive files found, CSV rows, name verdict exact, name verdict normalised, name verdict different, lessons with no video, Drive files with no lesson row, duplicate-number collisions, size in GB.

| Course | Drive | Rows | Exact | Normalised | Different | No video | No lesson | Collisions | GB |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 175 | 175 | 28 | 24 | 123 | 0 | 0 | 0 | 238.4 |
| 002 | 40 | 40 | 2 | 4 | 34 | 0 | 0 | 0 | 56.5 |
| 003 | 155 | 155 | 12 | 19 | 124 | 0 | 0 | 0 | 198.8 |
| **004** | **153** | **154** | 0 | 0 | 153 | **1** | 0 | 0 | 207.3 |
| 005 | 41 | 41 | 2 | 1 | 38 | 0 | 0 | 0 | 52.5 |
| 006 | 46 | 46 | 2 | 5 | 39 | 0 | 0 | 0 | 48.6 |
| 007 | 119 | 119 | 8 | 10 | 101 | 0 | 0 | 0 | 147.5 |
| 008 | 52 | 52 | 0 | 1 | 51 | 0 | 0 | 0 | 73.3 |
| 009 | 122 | 122 | 11 | 15 | 96 | 0 | 0 | 0 | 195.8 |
| 010 | 134 | 134 | 11 | 11 | 112 | 0 | 0 | 0 | 147.0 |
| 011 | 28 | 28 | 4 | 4 | 20 | 0 | 0 | 0 | 32.8 |
| 012 | 51 | 51 | 3 | 5 | 43 | 0 | 0 | 0 | 57.7 |
| 013 | 118 | 118 | 22 | 13 | 83 | 0 | 0 | 0 | 128.2 |
| 014 | 176 | 176 | 19 | 15 | 142 | 0 | 0 | 0 | 200.7 |
| 015 | 124 | 124 | 0 | 0 | 124 | 0 | 0 | 0 | 153.5 |
| 016 | 52 | 52 | 2 | 7 | 43 | 0 | 0 | 0 | 29.3 |
| 017 | 47 | 47 | 0 | 6 | 41 | 0 | 0 | 0 | 61.3 |
| 018 | 130 | 130 | 0 | 0 | 130 | 0 | 0 | 0 | 177.6 |
| 019 | 42 | 42 | 2 | 3 | 37 | 0 | 0 | 0 | 52.0 |
| 020 | 45 | 45 | 7 | 6 | 32 | 0 | 0 | 0 | 57.2 |
| 021 | 43 | 43 | 7 | 5 | 31 | 0 | 0 | 0 | 62.1 |
| 022 | 31 | 31 | 1 | 6 | 24 | 0 | 0 | 0 | 46.8 |
| 023 | 28 | 28 | 6 | 1 | 21 | 0 | 0 | 0 | 43.4 |
| 024 | 49 | 49 | 12 | 9 | 28 | 0 | 0 | 0 | 74.7 |
| 025 | 35 | 35 | 6 | 1 | 28 | 0 | 0 | 0 | 56.8 |
| 026 | 36 | 36 | 3 | 1 | 32 | 0 | 0 | 0 | 56.2 |
| 027 | 23 | 23 | 13 | 2 | 8 | 0 | 0 | 0 | 34.0 |
| 028 | 50 | 50 | 6 | 7 | 37 | 0 | 0 | 0 | 77.0 |
| **ALL** | **2,145** | **2,146** | **189** | **181** | **1,775** | **1** | **0** | **0** | **2,767.0** |

---

## Which courses came back clean

**Twenty seven of the twenty eight are clean on structure:** every lesson has a video, every video has a lesson, no collisions, no strays, no subfolders, one shortcode, numbering complete from 1 to N with no gaps.

**Only course 004 is not**, and only because lesson 1 has no video.

**On names, no course is clean**, and that is the real finding below.

---

## The name check, and what it actually says

**The stated normalisation, used exactly as written:** lower case; `&` read as `and`; bracketed matter dropped; all other punctuation ignored; runs of whitespace collapsed to one; ends trimmed. The `.mp4` and the shortcode and number are stripped from the Drive name before comparing.

| Verdict | Rows | Share |
|---|---|---|
| exact | 189 | 8.8% |
| normalised | 181 | 8.4% |
| **different** | **1,775** | **82.7%** |

**Five in six lesson names disagree between Drive and the spreadsheet, and not by punctuation.** They are different sentences. Three courses (008, 015, 018) have not one exact match in them.

Two examples, raw:

```
001-002   CSV   : Explaining the DiMAP Course Structure and Sections
          Drive : DMAP 002 Course Structure & Overview.mp4

001-004   CSV   : Self-Assessment Test: Psychological Flexibility and Rigidity
          Drive : DMAP 004 Psychological Flexibility and Rigidity.mp4
```

**What this vindicates.** Karen's ruling that the number is always right is not a tie-breaker for edge cases; it is carrying the entire match. Had the name been used as a matcher, or even as a veto, this map would have failed on 83 per cent of the library.

**What it means for the rename.** The agreed target name takes the lesson name from somewhere. If it takes it from the Drive file name, 1,775 videos keep a name the spreadsheet disagrees with. If it takes it from the spreadsheet, 1,775 files are renamed to something a human editor never called them. **That is a decision for Kain and Karen, not a detail of the rename script, and it is not settled by anything in the commission.**

### The full lists are a file, not this report

**`Drive to Lesson name comparison (18 August 2026).csv`, written into the master folder.** One row per matched lesson: Lesson Key, verdict, the CSV lesson name, the Drive file name, the Drive file ID.

**Why a file rather than in here.** You asked for every differing and every normalised row listed in full. That is 1,956 rows. In markdown it is several thousand lines nobody reads and nobody can sort. As a CSV it sits beside the data it describes, filters by verdict, and is the thing the naming decision will actually be taken from. The counts, the method and the samples are above; the evidence is in the file.

---

## What was written into the twenty eight CSVs

**Fifteen columns now, in this order:**

    Section | Lesson Number | Lesson Name | Lesson Description | Vimeo URL | Vimeo Video ID |
    Section Order | Lesson Key | Lesson Number Padded | Course Slug | Drive File Name |
    Drive File ID | Circle Course ID | Circle Lesson ID | Standardised Description

**`Lesson Key` is rewritten to the flat form.** `002-013`: three digit course, hyphen, three digit lesson, fixed width. The sectioned form is gone from every row.

**`Lesson Number Padded` is added**, holding the same padded number alone. **`Lesson Number` is untouched**, exactly as Karen left it.

**`Section Order` is kept**, as you instructed. It is no longer part of the key and nothing else about it changed.

**`Drive File Name` and `Drive File ID` are filled on all 2,145 matched rows**, whatever the name verdict was, exactly as specified. The one unmatched lesson has both empty, and that emptiness means only that no video was found.

**`Vimeo URL` and `Vimeo Video ID` were not touched and remain empty on every row.**

### Course 012's two section-less rows, answered

You were right not to take my "rows 47 and 49" at face value. **47 and 49 are their Lesson Numbers**, not their positions. The keys produced are **`012-047`** and **`012-049`**, and **both matched a Drive video**: `SHP 047 Session Two: Cosmina - Establishing Priorities & Action Steps.mp4` and `SHP 049 The Problems that Accompany Setting Goals.mp4`. Their `Section` and `Section Order` remain empty, still uninferred.

**Confirmed: 2,146 of 2,146 rows carry a Lesson Key, and all 2,146 keys are unique.**

---

## How this was verified, and one thing I got wrong

**The first eighteen folders were transcribed by hand** from the connector's inline output. Partway through, the payloads grew past the inline limit and the connector began writing them to a file instead, which meant they could be parsed rather than retyped. **Every hand-transcribed course was then re-read from Drive and compared field by field against what I had written.**

**That check found two errors of mine.**

1. A file size in course 006 copied from the neighbouring row. I caught that one myself at the time and corrected it.
2. **Two file names in course 016 contain a non-breaking space rather than an ordinary space**, and my hand copy had silently turned them into ordinary spaces. `MINDMH 001 Getting Started- Course Introduction Video.mp4` and `MINDMH 004 Contrastive Analysis- Conscious Awareness Vs. Autopilot.mp4`.

**The second one is worth Karen knowing about**, because it is invisible on screen and will not compare equal to what anyone types. Every listing has since been rebuilt from the raw payload, so what is on disk now is byte-for-byte what Drive holds. **No listing in the final set rests on a hand copy.**

## Anything else worth knowing

**Editing leftovers are common in the file names** and will travel into any rename that builds from them: `.MTS.mp4` double extensions (courses 025, 026), `_Sub_01` suffixes (006, 026), `_1` suffixes (006, 008), trailing hyphens where a question mark was stripped (016, 017, 020, 021, 024, 026), double spaces (005), trailing spaces (005, 012, 027), and one file with no extension at all in its name: `PG 13 017 How Present are Your Parents` in course 027, which Drive still reports as an mp4.

**Course 008 has two consecutive lessons with the same name**, 16 and 17, both "A Dissection of the Cognitive Experience", in Drive and in the spreadsheet. Not an error the map can settle; named so it is not met as a surprise.

**The 115-lecture gap is now mostly explained.** DSRD 5 counts 2,261 lectures; the spreadsheet holds 2,146; Drive holds 2,145. The map shows Drive and the spreadsheet agree with each other to within a single file, so **the gap is between DSRD 5 and both of the others**, not between our two working sources. Its origin is the Udemy instructor dashboard, as DSRD 5 says of itself. Still Kain's to settle, and not reconciled here.

## What was not done

No Drive file was renamed, moved, downloaded, opened or deleted. No Vimeo work of any kind. No description standardised. No gap filled by inference: the one lesson without a video is empty and listed, and course 012's two rows still carry no section.

*No em or en dashes in this file; checked before writing.*
