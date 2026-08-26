# INSTRUCTION: one source for a book's data, and a check on the row

**From:** Claude Code, Session 86. **Date:** 26 August 2026.
**Authority:** Kain, ruled in session at S086, after a day of upload faults.
**What is asked:** Chat turns this into the process. Kain has approved the direction. This note is deliberately short.

---

## The problem, in one paragraph

The same facts about one book live in four places: the Cowork record, `Book_Note_Master.xlsx`, `Book_Note_Upload.csv`, and the install. Each is missing something different and each behaves as though it is right. Data flows in both directions between them, so nothing is authoritative and every import is a guess about which copy to trust.

## What that cost today, measured rather than argued

- **24 of 64** rows held metadata and no body. The master and the records disagreed and neither said so.
- **`lead_tag`, `isbn`, `amazon_url` and the author slug** exist in the records and have no column in the 15 column upload contract, so they never reached the site. Kain opened a delivered page with no Discover Related Learning Paths block and no Amazon button.
- **The master marks every cover ok.** Not one of the 64 cover files exists on disk. Checked exhaustively: one folder, 613 files, all belonging to the original library.
- **Cowork's Content gate and Sourcing record** reached the reader-facing body of 64 published pages, because the body was read as everything after a marker and the record does not end at the body.
- **`author_website_url`** is in no record and no column, so one hero button cannot render on any book note.

## The ruling

**The Cowork record is the single source for everything about one note.** It already carries every field, it is the artefact that gets verified, and it is what Cowork produces at pace.

**The master spreadsheet is generated from the records and never typed into.** It stays, because bulk reading and bulk work are what a sheet is good at, and Kain and Karen need that. It stops being the road the data travels down.

**`Book_Note_Upload.csv`'s 15 column contract is retired as the import path.** It is too narrow for what `single-book_note.php` reads by name. The import reads records directly.

## Three checks that run before anything uploads

None of these exists today. All three would have caught a fault above.

1. **Field completeness.** Every field the template reads is present and non-empty, per page type.
2. **Body shape.** The body is exactly the ruled sections for that page type and nothing else. Built at S086 for book notes and proved refusing.
3. **Named files exist.** Every file the data names is really on disk. This is the one that would have reported the missing covers months ago instead of a column reading ok.

## What Chat is asked to produce

1. The written process, one home, naming the record as source and the sheet as output.
2. The field list per content type: what the template reads, and what the record must therefore carry.
3. A ruling on the fields no source holds today, `author_website_url` first, naming who fills them and where.
4. The same treatment for quotes, workbooks and articles, since all four content types have the same shape of problem.

## What Code has already built toward it

`tools/book_note_import.py`: reads records, writes the master, regenerates the sheet, imports and reads back. It carries check 2 and a partial check 3. It is the working prototype of the process, not the process.

## One dependency, so it is not discovered later

`RULING__The_Five_Book_Note_Headings_Updated_S314` changes the five locked headings. Check 2 is built on them, `single-book_note.php` hardcodes its contents list against the old anchor ids, and the 64 published notes carry the old wording. Records, template, gate and site move in one pass at Kain's Safari sitting, or the contents links point at headings that no longer exist.

OWED BACK: the written process, and the ruling on the fields nobody holds.

*No em or en dashes in this file; checked before writing.*
