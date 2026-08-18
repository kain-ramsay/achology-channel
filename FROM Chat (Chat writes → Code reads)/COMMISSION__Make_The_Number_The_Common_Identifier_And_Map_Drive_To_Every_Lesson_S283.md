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

**Two things this fixes at once.** Every key becomes directly comparable to a Drive file name. And the two rows in course 012 that carry no section, which you correctly refused to guess at, now take keys without anybody inferring anything, because a flat key needs no section. **Build their keys from their own Lesson Number values, whatever those are.** Your report called them "rows 47 and 49" and Chat cannot tell from that whether 47 and 49 are their positions in the sheet or their lesson numbers, so no key is written here for you to copy. **Confirm both are keyed after the rewrite, so the set reads 2,146 of 2,146 rather than 2,144, and state the two keys you produced.**

**`Section Order` stays.** It is no longer part of the key, and that is the only thing that changed about it. It is kept because the website's curriculum browser groups lessons under section headings and needs it. Do not drop it.

## Step 2: add two columns for the video itself

| Column | What it holds |
|---|---|
| Drive File Name | The exact current file name of the matched video, carried verbatim including its shortcode and its `.mp4`. **This is the record that makes a later rename reversible**, so it is written before any rename exists and is never removed. |
| Drive File ID | The Google Drive file ID of that video. **The ID is carried as well as the name because a name changes and an ID does not**, so every later job that downloads, replaces or renames targets the file exactly rather than by a string that is about to be rewritten. |

`Drive File ID` is new; `Drive File Name` already exists empty from the split.

## Step 3: prove the folder-to-course mapping before matching anything

**Do this before Step 4 and stop if it fails.** Every join below assumes Drive folder `016` is the same course as CSV sheet `016`. That has been assumed, never checked, and if one folder is out of step then every row in it joins to the wrong lecture and the report will look clean.

**Check each of the twenty eight Drive folder names against the canonical course name in DSRD 5 section 1 for that number.** Chat has already seen that the CSV filenames follow DSRD 5 and that some Drive folder names differ in punctuation or wording, so compare on meaning rather than on an exact string, and **list every folder whose name does not clearly denote the DSRD 5 course of the same number.** If any folder is genuinely a different course, stop and report rather than matching.

## Step 4: build the map, and match on two things rather than one

For every course, read its Drive folder and match each video to its lesson row.

**Parse the number, do not assume its width.** Take the leading run of non-digit characters as the shortcode, then the run of digits immediately after it as the number. Do not assume the number is exactly three digits, and do not assume there is no space. Report anything that does not fit that shape rather than forcing it.

**Match on the number.** Pair the parsed number, padded to three digits, with the course folder number, and join to `Lesson Key`. **The number is the only matcher.**

**Then check the name, as a check and never as a matcher.** Compare the remainder of the file name, with the `.mp4` removed, against `Lesson Name`. **Normalise both sides before comparing, and use exactly this normalisation:** lower case; `&` read as `and`; all punctuation and bracketed matter ignored; runs of whitespace collapsed to one; leading and trailing whitespace removed. Then record one of three verdicts per row: **exact** (identical before normalising), **normalised** (identical after normalising), or **different**. Report the three counts separately. Without a stated method the flag count means nothing, because a different rule would produce a different number.

**Write the match into the row.** For every row whose number matched a Drive file, write that file's name into `Drive File Name` and its ID into `Drive File ID`. **This happens whether the name verdict is exact, normalised or different.** The name verdict is recorded for a human to read; it never decides whether the row is filled. A row left empty means no video was found for that lesson, and it must mean only that.

**Where the number matches nothing**, write nothing into that row and list the lesson.

**Where two or more Drive files in one folder carry the same number**, write nothing into that row, list every file involved with its ID and size, and move on. **Do not choose between them.** Picking the larger, the newer or the better-named one is an inference about somebody's library, and a wrong pick here puts the wrong video on a lesson with nothing left to show it happened.

**Nothing in Google Drive is opened, moved, renamed or downloaded.** Metadata only.

## What is asked back, in TO Chat

**Per course, as a table:** Drive files found, CSV rows, matched with an exact name, matched with a normalised name, matched with a different name, CSV rows with no Drive file, Drive files with no CSV row, and duplicate-number collisions.

**The size of the library, per course and in total.** Every Drive file's size in bytes is already in the metadata you are reading, so this costs nothing extra. Report it per course and as one total, in bytes and in terabytes.

**Why it is asked, added on Karen's question in session.** Vimeo is currently at seventy one per cent of a seven terabyte allowance, which is roughly 4.97 TB used and 2 TB free. The Drive files are the re-edited versions and she expects them to be substantially smaller than what Vimeo holds. If that is right, the replacement run frees real space and the hosting plan may be able to come down, which is a money decision rather than a technical one. **The Drive total is half of that sum. The Vimeo half is commissioned separately in `COMMISSION__Export_The_Whole_Vimeo_Library_Read_Only_And_Answer_The_Account_Questions_S283`, which also asks whether replacing a file actually releases the old version's storage.**

**Then, listed in full rather than counted:**

- Every row where the number matched and the name verdict was **different**, with both strings side by side, and the raw strings rather than the normalised ones.
- Every row whose name verdict was **normalised**, with both strings, because a punctuation difference today becomes a rename decision tomorrow.
- Every lesson with no video, by key and name. These are the ones that cannot be replaced in Vimeo.
- Every Drive file with no lesson row, by file name, ID and size. These are either extra material, duplicates, or a lesson missing from the master.
- **Every duplicate-number collision**, with every file involved.
- **Every Drive folder whose name did not clearly denote the DSRD 5 course of the same number** (Step 3).
- **Any course folder holding files that are not lecture videos at all**, or holding subfolders. **Karen stated in session that there is nothing else in these folders: no resources, no bonus files, no older duplicates, no subfolders.** That is her answer and it is expected to hold. It is still asked back because one folder was read this session and twenty seven were not, and a stated fact confirmed by machine is worth more than either alone. **Report agreement as plainly as you would report an exception.**
- Any course using more than one shortcode, or a file whose name does not fit the shortcode-then-number pattern.

**Say plainly which courses came back clean**, because those are the ones ready to move first.

## What is NOT commissioned

**No rename of any Drive file.** Not one, not as a proof. The rename is its own commission, written only after Kain has read this map, and it will carry the old name in the CSV as its undo.

**The agreed target name, recorded now so the rename commission is not re-litigated later.** Kain and Karen settled it in session: once the map is clean, the shortcode comes out of every file name, because the course number already says which course it is and the shortcode repeats it. Course 002's thirteenth video becomes `002-013 The Map is not the Territory.mp4`. **This is safe only after the map**, because the shortcode is currently the one thing that would betray a file sitting in the wrong folder, and the map is what proves none are.

**No download, upload, replacement or deletion of any video.** Drive holds the only copy of this library.

**No Vimeo work of any kind in this commission.** The Vimeo library export is a separate commission, `COMMISSION__Export_The_Whole_Vimeo_Library_Read_Only_And_Answer_The_Account_Questions_S283`, which is written and sitting beside this one. Run this one first: its map is what the Vimeo export gets read against.

**No standardisation of any description.** That pass is Chat's.

**No filling of gaps by inference.** A lesson with no video stays empty and gets listed.

## The two things from your report that need Kain, not you

Recorded here so they are not lost, and neither blocks this job.

**Course 021's name differs in meaning, not punctuation:** the workbook says "Master Your Emotions", DSRD 5 says "Master Your Emotional IQ". That is Kain's call and it is going to him.

**The 115-lecture gap between these 2,146 rows and DSRD 5's 2,261.** You were right to name it and right not to reconcile it. This map is the instrument that will explain most of it, since a lesson with no video and a video with no lesson are exactly what that difference is made of.

*No em or en dashes in this file; checked before writing.*
