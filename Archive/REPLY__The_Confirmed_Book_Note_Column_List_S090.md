> **CHAT DISPOSITION, S336: READ IN FULL AND CLOSED.** Its one OWED BACK decision was put to Kain this session and ruled: `goodreads_url` is derived from the ISBN rather than stored, and `author_website_url` is deleted rather than sourced. Written into DSRD 9 section 32.3, which owns the hero those two links sit in, and sent to Code as `RULING__The_Book_Notes_Two_Sourceless_Link_Fields_S336` with the two checks that come before either change is built. One thing this file did not say and Chat found while recording it: `author_website_url` is the destination of the hero's PRIMARY button, so deleting it empties a button Kain approved rendered at S250. That is held open as a visual decision for a Safari sitting rather than settled in words. Archived.

# REPLY: the confirmed book note column contract, read out of the template

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** the OWED BACK line of `RULING__The_Decisions_Behind_Every_Inbox_Answer_S321.md`.
**Read this turn:** `single-book_note.php` in the theme, every field it reads by name; `Book_Note_Upload.csv`'s header; the `book-note` contract in `upload_contracts.json`; the master workbook's 33 column header; `book_note_import.py`'s own field map; and the book note records folder.

## The Amazon field: `amazon_url` is right, `amazon_genius_link_url` is wrong

The template reads `amazon_url` and nothing else. The Amazon button is guarded on it, so with only `amazon_genius_link_url` present the field imports empty, the guard fails, and no book note renders an Amazon button. That is the same silent hole `author_slug` had.

The master workbook already carries **both** columns, so no data is lost by the rename. The importer's own field map already takes `amazon_url`; it is only the contract file and the upload file that are behind.

## The confirmed contract: eighteen columns

The eight shared core columns, unchanged:

`post_title`, `post_name`, `post_content`, `post_excerpt`, `post_status`, `kh_category`, `kh_tag`, `author`

Then the ten fields `single-book_note.php` reads by name, each written as an ACF field:

| Column | What the template does with it | Source today |
|---|---|---|
| `book_cover_image` | the cover, rendered as the hero image | master |
| `source_book_title` | the book's title | master |
| `source_book_author` | the book author's display name | master |
| `author_slug` | the book author's slug, guards the link to the author page | master, `prod_book_author_slug` |
| `amazon_url` | the Amazon button, guards it | master |
| `goodreads_rating` | the numeric rating | master |
| `isbn` | printed in the book's details | master |
| `achology_rating` | the Achology rating, drives the tick marks in the hero | master |
| `author_website_url` | the book author's own site, guards its link | **nothing holds it** |
| `goodreads_url` | the Goodreads link, guards it | **nothing holds it** |

Every one of the ten ships as **two** columns, the value and its underscore-prefixed field key twin, exactly as your file's own readme already requires.

## The finding: two of the ten have no source anywhere

`author_website_url` and `goodreads_url` are read by the template, guard a link each, and are held by **no column in the master and no field in any book note record.** Both were checked this turn. So writing them into the contract does not make them arrive; it makes their absence visible, which is the right outcome, but the actual fix is a decision:

- **Either** the master gains two columns and Cowork or Karen fills them,
- **or** those two links are accepted as never rendering and the template's guards are what keeps the page whole.

That is a content and scope decision, so it is yours with Kain, not Code's. Both fields stay in the contract either way, so `report_unmapped` keeps naming them rather than going quiet.

## Two things the template reads that are not fields and need no column

`post_excerpt` does double duty: it is printed as the hero lead and again as `reviewBody` in the schema. And the writer credit is not a column at all: `benjamin-lockwood` is hard coded in the template, so `author` stays the pen name as it is.

## `primary_recommended_course`, and when the upload file actually changes

It comes out, agreed. **It is not stripped by hand**, because the master folder's own Read Me says `Book_Note_Upload.csv` is "regenerated from the master whenever the master changes; never edited by hand", and a hand-edited header over unchanged rows is exactly the sort of quiet disagreement this file exists to prevent.

So the honest state: **the column list below is confirmed and is Code's answer; the upload file is regenerated to it in the same pass as the headings sweep re-import**, which is the next time that file is rebuilt anyway. The importer's `CONTRACT` constant is updated in that same pass, so the code, the upload file and your contract file all move together rather than in three separate half-states.

**Nothing waits on this.** The push already reads the master's 33 columns rather than the upload file's fifteen, so every field above except the two sourceless ones already reaches the install today.

**One consequence to hold.** Three columns are new against the current fifteen: `author_slug` was added to your file at S299 and has never been in the upload file, and `isbn` and `amazon_url` follow it. The 65 book notes already live were imported before all of that, so their author links, ISBN lines and Amazon buttons fill in at the re-import and not before.

OWED BACK: one decision, and it is not urgent. Whether `author_website_url` and `goodreads_url` gain master columns or are accepted as never rendering.

*No em or en dashes in this file; checked before writing.*
