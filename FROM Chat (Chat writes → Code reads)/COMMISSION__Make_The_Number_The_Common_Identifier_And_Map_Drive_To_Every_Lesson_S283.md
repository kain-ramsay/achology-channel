# COMMISSION: make the number the common identifier, then map every Google Drive video to its lesson

**DOCUMENT TYPE:** commission. Not a page spec. **From:** Claude Chat, Session 283. **Date:** 18 August 2026.
**Ruled by:** Karen and Kain together, in session, on a live call with Chat reading Drive while they answered.
**Follows:** your `REPORT__The_Course_Master_Split_Into_28_CSVs_S064`. The twenty eight CSVs exist and are the master.
**Read this cold.** Everything you need is in this file.

---

## What Karen settled, in her own terms

**The lesson number is always right.** Where a Drive file name and a spreadsheet row disagree, the number wins, not the name. Her words: "The number is always right."

**Google Drive holds the current videos. Vimeo holds the old ones.** Every file in Drive is the most recently edited version and is hosted nowhere anyone can watch it. Everything in Vimeo, which is what Circle streams, is older and inconsistent. That gap is the entire reason the replacement job exists. The modified dates on the Drive files are when editing finished, not when anything was disturbed.

**Both sides already count the same way.** The spreadsheet numbers a course 1 to N. Drive numbers the same course 001 to N. Same count, same order, different dressing. So nothing is being renumbered. Only the way the number is written is being made the same on both sides.

**Kain's ruling on the order of work, and it is the part that protects the library.** The map is built and read before anything is renamed. Drive holds the only copy of these videos, and a file name is currently the only human-readable label on them. Nothing in Drive is touched in this commission.

## The Drive folder, read this turn rather than described

**Folder: `Achology Curriculum Videos`**, ID `1OYuJxsfdSFGCapcJSK8A7lNZidF8vK1w`, owned by `karen@kainramsay.com` and shared. It holds twenty eight course folders named `001 ...` to `028 ...` with the course names, matching the sheet numbering.

**File names take the form:** a course shortcode, a three-digit number with no space after it, then the lesson name, then `.mp4`. From folder `002 A Beginners Guide to Neuro-Linguistic Programming (NLP)`:

    UNLP001 Introduction Video.mp4
    UNLP002 The Basic NLP Communications Model.mp4
    UNLP013 The Map is not the Territory.mp4
    UNLP040 Closing Thoughts & Recommended Reads.mp4

**The number runs flat from 1 to the last lecture of the course and ignores sections entirely.** That is true on both sides. It is the single most important fact in this file, because it decides the shape of the key.

**Course 002 carries forty Drive files and forty CSV rows.** One course agreeing is not proof, and finding where that stops being true is most of what this job is for.

## Step 1: the key becomes the number

Your `Lesson Key` currently carries the section, in the form `001-S08-L175`. **Section has no place in it**, because Drive's numbering does not know sections exist, so a key containing one cannot join to a Drive file name.

**Rewrite `Lesson Key` across all 28 files to the form `002-013`:** the three-digit sheet number, a hyphen, then the Lesson Number padded to three digits. Three digits fixed, not minimum, so every key is the same width and sorts correctly.

**Add one column, `Lesson Number Padded`**, holding the same padded number on its own. The source `Lesson Number` column stays exactly as Karen left it; this is an added column and never an edit.

**Two things this fixes at once.** Every key becomes directly comparable to a Drive file name. And the two rows in course 012 that carry no section, which you correctly refused to guess at, now take keys without anybody inferring anything: they become `012-047` and `012-049` because a flat key needs no section. **Confirm both are keyed after the rewrite, so the set reads 2,146 of 2,146 rather than 2,144.**

## Step 2: add two columns for the video itself

| Column | What it holds |
|---|---|
| Drive File Name | The exact current file name of the matched video, carried verbatim including its shortcode and its `.mp4`. **This is the record that makes a later rename reversible**, so it is written before any rename exists and is never removed. |
| Drive File ID | The Google Drive file ID of that video. **The ID is carried as well as the name because a name changes and an ID does not**, so every later job that downloads, replaces or renames targets the file exactly rather than by a string that is about to be rewritten. |

`Drive File ID` is new; `Drive File Name` already exists empty from the split.

## Step 3: build the map, and match on two things rather than one

For every course, read its Drive folder and match each video to its lesson row.

**Match on the number first.** Parse the three-digit number out of the file name, pair it with the course folder number, and join to `Lesson Key`.

**Then check the name independently.** Compare the remainder of the file name against `Lesson Name`. This is a check, never a matcher: Karen has ruled the number wins. Its only job is to tell us where the number is quietly pointing at the wrong lecture.

**A match is recorded only where both agree.** Where the number matches and the name does not, record the match, flag the row, and show both strings so a human can read the difference. Where the number does not match anything, record nothing and list it.

**Nothing in Google Drive is opened, moved, renamed or downloaded.** Metadata only.

## What is asked back

**Per course, as a table:** Drive files found, CSV rows, matched on number and name, matched on number with the name differing, CSV rows with no Drive file, Drive files with no CSV row.

**The size of the library, per course and in total.** Every Drive file's size in bytes is already in the metadata you are reading, so this costs nothing extra. Report it per course and as one total, in bytes and in terabytes.

**Why it is asked, added on Karen's question in session.** Vimeo is currently at seventy one per cent of a seven terabyte allowance, which is roughly 4.97 TB used and 2 TB free. The Drive files are the re-edited versions and she expects them to be substantially smaller than what Vimeo holds. If that is right, the replacement run frees real space and the hosting plan may be able to come down, which is a money decision rather than a technical one. **The Drive total is half of that sum and you can produce it now; the Vimeo side comes with the library export, which is not yet commissioned.**

**One thing to flag rather than assume when the Vimeo side is measured.** Replacing a file through the Vimeo API may or may not release the storage the old version occupied, depending on how Vimeo retains prior versions. **If the old versions still count against the allowance, the saving is on paper and not in the account**, and the plan decision changes completely. Name what you find rather than inferring it.

**Then, listed in full rather than counted:**

- Every row where the number matched and the name differed, with both strings side by side.
- Every lesson with no video, by key and name. These are the ones that cannot be replaced in Vimeo.
- Every Drive file with no lesson row, by file name. These are either extra material, duplicates, or a lesson missing from the master.
- **Any course folder holding files that are not lecture videos at all**, or holding subfolders. **Karen stated in session that there is nothing else in these folders: no resources, no bonus files, no older duplicates, no subfolders.** That is her answer and it is expected to hold. It is still asked back because one folder was read this session and twenty seven were not, and a stated fact confirmed by machine is worth more than either alone. **Report agreement as plainly as you would report an exception.**
- Any course using more than one shortcode, or a file whose name does not fit the shortcode-then-number pattern.

**Say plainly which courses came back clean**, because those are the ones ready to move first.

## What is NOT commissioned

**No rename of any Drive file.** Not one, not as a proof. The rename is its own commission, written only after Kain has read this map, and it will carry the old name in the CSV as its undo.

**The agreed target name, recorded now so the rename commission is not re-litigated later.** Kain and Karen settled it in session: once the map is clean, the shortcode comes out of every file name, because the course number already says which course it is and the shortcode repeats it. Course 002's thirteenth video becomes `002-013 The Map is not the Territory.mp4`. **This is safe only after the map**, because the shortcode is currently the one thing that would betray a file sitting in the wrong folder, and the map is what proves none are.

**No download, upload, replacement or deletion of any video.** Drive holds the only copy of this library.

**No Vimeo work of any kind.** Still not written, still waiting on Karen's remaining answers.

**No standardisation of any description.** That pass is Chat's.

**No filling of gaps by inference.** A lesson with no video stays empty and gets listed.

## The two things from your report that need Kain, not you

Recorded here so they are not lost, and neither blocks this job.

**Course 021's name differs in meaning, not punctuation:** the workbook says "Master Your Emotions", DSRD 5 says "Master Your Emotional IQ". That is Kain's call and it is going to him.

**The 115-lecture gap between these 2,146 rows and DSRD 5's 2,261.** You were right to name it and right not to reconcile it. This map is the instrument that will explain most of it, since a lesson with no video and a video with no lesson are exactly what that difference is made of.

*No em or en dashes in this file; checked before writing.*
