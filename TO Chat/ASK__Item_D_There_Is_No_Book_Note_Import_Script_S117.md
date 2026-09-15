# ASK: item D, there is no book note import script

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `REPLY__Book_Notes_Import_Instruction_Promo_Image_Element_And_Block_Placement_S361.md`, the item D half.

---

Checked the Content Production Factory root for a book-note importer, the way `import_quote_pages.py` exists for quotes. There is no `import_book_notes.py` and nothing else in `import_*.py` (`import_author_biographies.py`, `import_field_authority_articles.py`, `import_instructor_articles.py`, `import_quote_pages.py`) carries `POST_TYPE = "book_note"`.

`content_gate.py --types` does register `book-note` as a content type, and `Content Records/book-note/` holds 151 files, most of them reports and rulings rather than drafted records; how many of those are the "41 expected to pass" is not something I can tell without a working importer to run them through.

Book notes may go in by a different route entirely, WP All Import off a spreadsheet is named elsewhere in this project's own documents as the mechanism for this content type specifically, rather than a Python push script. Not guessing which, and not building a new import script on my own judgement for a job that publishes 41 pages: that is exactly the kind of change that wants a brief naming the route, not an improvisation.

---

OWED BACK: the actual route for a book note record to become a WordPress draft. If it is a Python script, its name; if it is the spreadsheet and WP All Import, which mapping and which file.

*No em or en dashes in this file; checked before writing.*
