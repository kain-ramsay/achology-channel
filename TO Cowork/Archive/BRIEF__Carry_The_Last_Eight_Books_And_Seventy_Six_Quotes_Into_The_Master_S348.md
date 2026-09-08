# BRIEF: carry the last eight books and seventy six quotes into the master, then prove the Evernote folder is free to archive

**DOCUMENT TYPE:** brief, from Claude Chat, Session 348. **Date:** Tuesday 8 September 2026.
**Approved by Kain** in the S348 sitting.
**Governed by** `000__COWORK_PRODUCTION_HARNESS.md` at the root of this folder.
**Follows:** your `DONE__Evernote_Inventory_Complete_S348.md` and its foot. Read this cold.
**Job type:** data. Nothing is drafted, corrected, or gated.

---

## 1. Why this job exists

Your inventory showed that 263 of the 271 salvageable books and 8,323 of the 8,399 real quotes already sit in `Achology Master Books and Quotes.xlsx`. The match is exact: a title or a quote counts as present only when it equals a cell in the workbook, character for character after normalising case and punctuation. So it is tight, not loose, and Kain has accepted it.

Eight books and seventy six quotes are not in the workbook. Once they are, everything worth keeping from Evernote is inside the working system, and the Evernote folder can be archived. Kain wants to delete the files and close the account, and this job is what makes that safe.

## 2. What you do

**Step 1. Back the master up before you touch it.** Copy `Content Plan Spreadsheets / Working / Achology Master Books and Quotes.xlsx` into `Content Plan Spreadsheets / Archive` as `Achology Master Books and Quotes__before_S348_append.xlsx`. Do not proceed until that copy exists and opens.

**Step 2. Read the workbook's own shape before you write to it.** Open it and record, in your DONE file, the sheet names and the column headers of the sheet that holds books and the sheet that holds quotes. New rows follow the columns exactly as they are. Add no column. If a column you cannot fill exists (a Rank Math field, a status, a date), leave it empty rather than guess.

**Step 3. Append the eight books.** From `INVENTORY__Evernote_Articles.csv`, the rows with `cowork_view` = `worth rewriting` and `in_master_workbook` = `no`. One row each, title and author from the inventory. In whatever column the sheet uses for source or notes, write `Evernote export, S348`. If the sheet has no such column, say so in the DONE file and do not invent one.

**Step 4. Append the seventy six quotes.** From `INVENTORY__Evernote_Quotes.csv`, the real quote rows with `in_master_workbook` = `no`. One row each: the quote text, the person from `person_or_topic` for Q1 rows, and for Q2 rows the topic in the topic column and the attribution from `attribution_in_line` where one was captured. Same source note. **Do not verify any quote in this job.** Verification is its own commission and its method is not yet written; these rows enter the master marked unverified, exactly as the other quote rows there are.

**Step 5. Prove the Evernote folder is free.** Search every script and every document in the Content Production Factory folder and the Code theme folder for the string `Evernote`. Report every file that mentions it and whether it reads from the folder. The only reader Chat knows of is `evernote_inventory.py`, whose job is done. If anything else reads from the folder, name it and stop; Chat decides before anything moves.

**Step 6. Do not move the folder.** Chat moves it to the OBSOLETE folder on your DONE, not you, because the move is the last act and it belongs to the session that reads your proof.

## 3. What comes back

`DONE__Evernote_Last_Rows_In_The_Master_And_The_Folder_Is_Free_S348.md` in FROM Cowork, carrying: the backup's path; the sheet names and headers; the count of rows appended to each sheet, which must read 8 and 76 or say why not; and the search result from step 5, every file named.

## 4. What you must not do

- Do not write to the Evernote folder, to `Content Records`, or to `KEYWORD_REGISTER.csv`.
- Do not change, reorder, or clean any existing row in the master. Append only.
- Do not verify, correct, or rewrite any quote.
- Do not move or delete anything.

---

*No em or en dashes in this file; checked before writing.*
