# BRIEF: bring the Book Note master's title column, and the unpublished records, to the ruled title form

**From:** Claude Chat, Session 353. **Date:** Tuesday 8 September 2026.
**Harness:** the Cowork Production Harness at the root of the Content Production Factory folder. Read it first, then The Shared Rules, then this file.
**Job type:** data. Nothing is drafted, corrected in its prose, or re-gated for its words. Two fields move, nothing else.
**Board card:** Book Notes; the 65 published book notes.
**Start when you read this; nothing else is owed to you first.**

---

## 1. The ruling this carries out

Kain looked at the book note pages Code published at his S106 and S107 sittings and ruled the title form himself, in his own words, on the pages. **A book note's title is the book's title, a colon, then "Summary and Key Ideas".** For example: "Atomic Habits: Summary and Key Ideas". Where the book's own title ends in a question mark, the colon is dropped: "What Do You Say After You Say Hello? Summary and Key Ideas". That is correct English, not a drift.

Code applied the form to all 92 published pages and to their 92 records that night. Then Kain ruled the master: "tell chat to fix the spreadsheet column." The master is Chat's under The Shared Rules section 4, and Chat cannot write a spreadsheet file from its own machine, so this brief carries his instruction to you, exactly as the S351 addendum carried the three master strikes. The ruling is written into DSRD 2 section 3.1 this session.

## 2. Why the column matters, not only the pages

`book_note_import.py` keeps the master's value for any column the run does not name in `--overwrite-columns`. The master's `post_title` column holds the bare book title. So any future import that forgets the flag reverts every published title to the bare form in one run. Fixing the column removes the fault; a rule that depends on somebody remembering a flag is the fault's own shape.

## 3. The job, in order

**Step 1. Back up.** Copy `Book Notes | Source Bank + Master File / Book_Note_Master.xlsx` to that folder's `Archive` as `Book_Note_Master__before_S353_title_form.xlsx`. Confirm the copy opens and its checksum matches before any write.

**Step 2. Walk the whole `post_title` column on sheet "Master v4 (S044 Contract)".** Every row, not only the 92. For each row, the value becomes `{book title}: Summary and Key Ideas`, or `{book title} Summary and Key Ideas` where the book's title itself ends in a question mark. The book title is the row's own book title column, exactly as written there; nothing is retyped from memory. A row already in the ruled form is left as it is. Count the rows changed and the rows already correct, and confirm the total equals the sheet's row count (677 after the S351 strikes; say so if it differs).

**Step 3. The unpublished records.** In `Content Records/book-note/`, every record whose page is not yet live (the 92 published records already carry the ruled title from Code's S107 pass; every other record does not). Set `post_title` in the Page fields table, and the record's own first-line title heading where one exists, to the same ruled form, so the record and the master read the same string and a future disagreement between them is visible rather than silent. Change those two lines and nothing else in each file. Verify per file that exactly those lines moved.

**Step 4. Read back.** Reopen the saved master fresh and confirm three rows by eye: the first row, the last row, and one question-mark title. Run `content_gate.py` on three of the changed records and confirm the gate result did not move from its pre-edit state on anything but the title lines.

## 4. What you must not do

- Do not touch `rm_focus_keyword`, `rm_seo_title`, the slug, or any body text. The keyword is the book's title and moves to fit the address (S349, S350); that is a different job and it is already done.
- Do not touch the 92 published records' `post_title`; Code set those on Kain's ruling and they are right. If one of them disagrees with the form, name it, do not change it.
- Do not change, reorder or strike any other cell in the master.

## 5. What comes back

`DONE__Master_Title_Column_And_Unpublished_Records_At_The_Ruled_Form_S353.md` in FROM Cowork, carrying: the backup's name and checksum match; the count of master rows changed and rows already correct, summing to the sheet's total; the count of records changed; the three read-back rows; and anything found that this brief did not expect.

OWED BACK: that DONE file. Nothing else.

*No em or en dashes in this file; checked before writing.*
