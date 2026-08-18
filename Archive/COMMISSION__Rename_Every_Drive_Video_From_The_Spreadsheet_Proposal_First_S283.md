# COMMISSION: rename every Google Drive video from the spreadsheet, proposal first, execution second

**DOCUMENT TYPE:** commission. Not a page spec. **From:** Claude Chat, Session 283. **Date:** 18 August 2026.
**Ruled by:** Kain, in session, on reading your `REPORT__The_Drive_To_Lesson_Map_S064`. His words on the name source: "Yes!!! This must always happen."
**Follows:** that report. The map is built, 2,145 of 2,146 lessons carry a Drive File Name and a Drive File ID.
**Read this cold.** Everything you need is in this file.

---

## What Kain ruled, and the finding it answers

**Your map found that 1,775 of 2,146 lesson names, five in six, differ between Google Drive and the spreadsheet, and differ as sentences rather than as punctuation.** Three courses had no exact match at all.

**Kain's ruling: the spreadsheet name wins, every time.** The spreadsheet mirrors Circle, which is what students actually read, so a Drive file disagreeing with it is the Drive file being wrong. He was unambiguous that this is a standing rule and not a one-off call.

**So Google Drive is being brought into line with the spreadsheet, not the other way round.** Roughly 1,775 files will end up with a name no editor ever gave them. That is the intended outcome, not a side effect, and every original name is already recorded in the CSVs.

## The target name

    002-013 The Map is not the Territory.mp4

Course number, hyphen, lesson number, space, the lesson name, `.mp4`. **The shortcode goes.** The course number already says which course it is, so the shortcode repeated it.

**The name comes from the `Lesson Name` column, exactly as it stands.** Not from the Drive file name, and not from `Standardised Description`. **The standardisation pass touches descriptions only, never lesson names**, so nothing here waits on it and nothing here is affected by it.

**The number comes from `Lesson Number Padded`, and the course number from the first three digits of `Lesson Key`.** Both are already correct in the files.

## Do not use the parsing rule from the previous commission

**You were right to change it and right to say so.** The rule Chat wrote (leading non-digits as shortcode, digits after) would have misfiled courses 006, 017, 027 and 028: a leading year, numbers inside the shortcode, and a width that changes halfway through a course.

**None of that matters here, and this is worth stating plainly: this commission never parses an old file name at all.** The new name is built entirely from the CSV, and the file is found by its `Drive File ID`. The old names' leftovers, the `.MTS.mp4` double extensions, the `_Sub_01` and `_1` suffixes, the trailing hyphens where a question mark was stripped, the double and trailing spaces, the two non-breaking spaces in course 016, and the one file whose name carries no extension, **all disappear as a consequence of rebuilding rather than editing.** Say in your report that they are gone.

## Making a lesson name safe as a filename

Lesson names contain characters a filename cannot carry or should not carry. **Apply exactly these rules, and no others:**

- **`/` and `\` become a hyphen surrounded by single spaces.** They are illegal in a filename and there is no lossless substitute.
- **`:` becomes a hyphen surrounded by single spaces.** Colons are common in these names ("Self-Assessment Test: Psychological Flexibility and Rigidity") and break on several systems.
- **`?`, `*`, `"`, `<`, `>` and `|` are removed**, and any space left doubled is collapsed.
- **Leading and trailing whitespace is trimmed**, and any run of whitespace inside the name is collapsed to one ordinary space. **Non-breaking spaces become ordinary spaces.**
- **Everything else stays**, including `&`, apostrophes, commas, brackets and accented characters. Do not transliterate and do not lower case.

**Report every name that any of these rules changed**, with the raw lesson name and the resulting filename, so a human can see what the disc forced on us.

## Step 1: the proposal, and it stops there

**Nothing in Google Drive is renamed in this step.**

Write one CSV into the `Course + Lesson Data | MASTER` folder holding the full proposed rename, one row per file: Lesson Key, Drive File ID, the current file name, the proposed new file name, and a flag saying whether the sanitisation rules altered anything.

**Update that folder's read me to name the file**, as you did for the others.

**Then stop and report.** Kain reads the proposal before a single file moves. **This is a rename of the only copy of a 2.77 terabyte video library, so it is proposed, read, and only then executed.**

### What to check in the proposal before you hand it over

- **Every proposed name is unique within its folder.** Course 008 carries two consecutive lessons with the identical name, 16 and 17, both "A Dissection of the Cognitive Experience". Their numbers differ so their filenames differ, but **check the whole set rather than trusting that**, and list any collision instead of resolving it.
- **No proposed name is empty, and none is only a number**, which would mean a blank `Lesson Name`.
- **The count of files to be renamed** equals 2,145, or the difference is explained.

### One file to raise before it is renamed

`MINDMH 006 Growing in Self-Awareness Downloadable Resource.mp4` in course 016. You flagged it: an mp4 in a numbered lesson slot, 57 MB where the smallest real lecture in that course is 141 MB, with a name saying it is a resource rather than a lecture. **Include it in the proposal but flag it in your report**, because renaming it to a lecture name makes it look like a lecture forever.

## Step 2: execution, only on Kain's word

**Do not run this step until Kain has read the proposal and said yes.** His yes travels to you through the channel like everything else.

**Target every file by `Drive File ID`, never by its name.** The name is what is changing and is not a safe handle.

**Rename in batches, and read each batch back from Drive before starting the next.** A batch that does not read back as expected stops the run.

**Write the result into the CSVs in a new column, `Drive File Name Renamed`.**

**`Drive File Name` is never overwritten.** It holds the name as found, and it is the undo. Overwriting it destroys the only record of what each file used to be called, and with it any possibility of putting the library back. **This is the single most important instruction in this file.**

**Nothing else about any file changes.** Not its contents, not its location, not its sharing, not its ID.

## What is asked back, in TO Chat

- Files renamed, files failed, files skipped, with reasons.
- Every name the sanitisation rules altered, raw and final.
- Any collision found.
- Confirmation that `Drive File Name` still holds the original name on all 2,145 rows, read back rather than assumed.
- Confirmation that no file ID changed.

## The rollback, stated so it exists before it is needed

The CSVs hold each file's ID, its original name and its new name. **A reverse run is therefore always possible**, targeting by ID and writing `Drive File Name` back. Say in your report that you have confirmed this is true of the finished state, rather than assuming it.

## What is NOT commissioned

**No renaming in Step 1.** The proposal is a file, not an action.

**No execution without Kain's yes**, given after he has read the proposal.

**No download, upload, move, deletion or content change of any video.**

**No Vimeo work of any kind.**

**No standardisation of any description.**

**No filling of the one empty row.** Course 004 lesson 001 has no video and nothing is renamed for it.

*No em or en dashes in this file; checked before writing.*
