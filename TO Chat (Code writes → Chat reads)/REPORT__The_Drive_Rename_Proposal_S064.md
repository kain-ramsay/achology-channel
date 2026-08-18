**DISPOSITION (S284): facts and all three pre-rename flags driven onto the Vimeo Course Refresh card. Step 2 waits on the fresh-eyes review, then Kain reading the proposal and saying yes; the card carries that wait. Archived.**

# REPORT: the rename is proposed, 2,145 files, and nothing has been renamed

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Closes Step 1 of:** `COMMISSION__Rename_Every_Drive_Video_From_The_Spreadsheet_Proposal_First_S283.md`.
**Step 2 has not run and will not run until Kain has read this and said yes.**

**Nothing in Google Drive has been renamed, moved, opened, downloaded or altered.** This step produced a file, not an action.

---

## The proposal

**`Drive rename proposal (18 August 2026).csv`, in the `Course + Lesson Data | MASTER` folder.** The folder's read me names it.

One row per file: Lesson Key, Drive File ID, current file name, proposed file name, whether the sanitisation rules altered anything, which rules fired, and the raw lesson name they were applied to.

| | |
|---|---|
| Files proposed for rename | **2,145** |
| Rows with no video, nothing proposed | **1** (course 004 lesson 001) |
| Within-folder name collisions | **0** |
| Proposed names that are empty or only a number | **0** |
| Names the sanitisation rules altered | **670** |
| Longest proposed name | **85 characters** |

**The count is 2,145 and needs no explanation:** it is every row carrying a Drive File ID, which is every lesson except the one with no video.

**Course 008's two identically named lessons do not collide**, as you expected but asked me to check rather than assume: 16 and 17 are both "A Dissection of the Cognitive Experience", and their numbers make `008-016 ...` and `008-017 ...`. **I checked the whole set rather than only that pair, and there are no collisions anywhere.**

---

## The sanitisation, and which rules actually fired

Applied exactly as specified, and no other rule was invented.

| Rule | Names affected |
|---|---|
| Colon becomes a hyphen surrounded by single spaces | 606 |
| Whitespace collapsed to one ordinary space | 616 |
| `?` removed | 72 |
| Slash becomes a hyphen surrounded by single spaces | 11 |
| Leading or trailing whitespace trimmed | 10 |
| `"` removed | 5 |
| `|` removed | 3 |
| `>` removed | 1 |
| `*` removed | 1 |

**One honest note on the whitespace figure.** Most of those 616 are a consequence of the colon rule rather than pre-existing double spaces: replacing `: ` with ` - ` leaves a double space, which the collapse then tidies. **Only about ten names had genuine extra whitespace of their own.** Reported this way because 616 read alone would overstate how untidy the source is.

**Everything else stays**, as instructed: ampersands, apostrophes, commas, brackets and accented characters are untouched, nothing is transliterated and nothing is lower cased.

**The full list of all 670 altered names, raw and final, is in the CSV**, one row each with the rules that fired named. The two representative shapes:

```
001-004   lesson name : Self-Assessment Test: Psychological Flexibility and Rigidity
          filename    : 001-004 Self-Assessment Test - Psychological Flexibility and Rigidity.mp4

001-023   lesson name : Can Psychology be Regarded as an Empirical Science?
          filename    : 001-023 Can Psychology be Regarded as an Empirical Science.mp4
```

---

## Every leftover in the old names disappears, as you said it would

**Confirmed, and worth stating because it is the strongest argument for rebuilding rather than editing.** The new name is built entirely from the CSV and no old file name is parsed at any point, so all of the following are simply gone from the 2,145 proposed names:

- the `.MTS.mp4` double extensions in courses 025 and 026
- the `_Sub_01` and `_1` suffixes in courses 006 and 026
- the trailing hyphens left where a question mark was stripped, across six courses
- the double and trailing spaces in courses 005, 012 and 027
- **the two non-breaking spaces in course 016**
- the one file whose name carries no extension at all, `PG 13 017 How Present are Your Parents` in course 027, which becomes a properly named `.mp4`

**None of that required a rule.** It is what rebuilding gets you for free.

---

## Three things to raise before a single file moves

### 1. One lesson name is corrupted in the source, and the rename would make it permanent

**Course 014, lesson 151.** The master holds:

```
The BThe Becca Sessions (Phase 2 → Session 2 → Part 4)
```

That `The BThe` is a data fault in the spreadsheet, not a transcription error of mine. Its sibling lessons read `The Becca Sessions (Phase 1 → Session 1 → Part 3)` and so on, so the intended name is clear, **but correcting it is not mine to do.** The proposal carries it exactly as the master holds it.

**If the rename runs as proposed, a Drive file is called `014-151 The BThe Becca Sessions ...` from then on.** Karen fixing one cell before Step 2 avoids that entirely.

### 2. Six lesson names contain a line break

They sanitise cleanly, because the whitespace rules collapse and trim them, so the proposal is correct. **But a line break inside a lesson name is a fault in the data rather than a formatting choice**, and it is the sort of thing that will surprise the website import later. Courses 012 and 014 hold them.

### 3. Unusual characters survive into filenames, correctly and perhaps unwantedly

Your rules say everything not named stays, so these are in the proposed names:

| Character | Lesson names | Example |
|---|---|---|
| A right arrow | 25 | `014-143 The Becca Sessions (Phase 1 → Session 1 → Part 1).mp4` |
| Circled numerals | 1 | `013-089 The ① Head ② Heart, and ③ Gut Hypnotic Technique.mp4` |
| Greek | 1 | `012-044 The Four Different Categories of Idea (ἰδέα).mp4` |
| An accented character | 1 | `001-166 Júrgen Habermas - The 'Influence of Minority' Groups.mp4` |

**All legal in a filename and all a little strange to meet in a video library.** I have not stripped them, because stripping them would be me editing Kain's copy on my own authority. **If he wants them plainer, that is a rule to add before Step 2, not a judgement for me.**

### And the file you asked me to flag again

`MINDMH 006 Growing in Self-Awareness Downloadable Resource.mp4`, course 016 lesson 006. It is in the proposal and would become `016-006 Growing in Self-Awareness Downloadable Resource.mp4`. **It is 57 MB where the smallest real lecture in that course is 141 MB, and its name says resource rather than lecture.** Renaming it makes it look like a lecture forever, exactly as you said.

---

## What Step 2 will do, recorded now so it is agreed before it runs

- **Target every file by `Drive File ID`, never by name.**
- **Rename in batches and read each batch back from Drive before starting the next.** A batch that does not read back as expected stops the run.
- **Write the result into a new column, `Drive File Name Renamed`.**
- **`Drive File Name` is never overwritten.** It holds the name as found and it is the undo.

**On the rollback, checked rather than assumed.** The CSVs currently hold, for all 2,145 matched rows, the Drive File ID and the original Drive File Name. **I have confirmed both columns are populated on all 2,145 and that the 2,146 Lesson Keys are unique**, which is what makes a reverse run possible: target by ID, write the original name back. That will be confirmed again from the finished state after Step 2 rather than taken on today's reading.

## What has not been done

No file renamed, not one, not as a proof. No download, upload, move, deletion or content change. No Vimeo work. No description standardised. **The one lesson with no video has nothing proposed for it.**

*No em or en dashes in this file; checked before writing.*
