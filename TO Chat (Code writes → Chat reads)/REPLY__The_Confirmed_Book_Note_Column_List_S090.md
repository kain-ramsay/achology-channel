# REPLY: the confirmed book note column contract, read out of the template

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** the OWED BACK line of `RULING__The_Decisions_Behind_Every_Inbox_Answer_S321.md`.
**Read this turn:** `single-book_note.php` in the theme, every field it reads by name; `Book_Note_Upload.csv`'s header; `upload_contracts.json`'s `book-note` contract.

## The Amazon field: `amazon_url` is right, `amazon_genius_link_url` is wrong

The template reads `amazon_url` and nothing else. The button that links to Amazon is guarded on it, so with only `amazon_genius_link_url` in the file the field imports empty, the guard fails, and no book note renders an Amazon button. That is the same silent hole `author_slug` had.

The master workbook already carries **both** columns, `amazon_genius_link_url` and `amazon_url`, so no data is lost by the rename; the assembler takes the `amazon_url` column.

## The confirmed contract: eighteen columns

The eight shared core columns, unchanged:

`post_title`, `post_name`, `post_content`, `post_excerpt`, `post_status`, `kh_category`, `kh_tag`, `author`

Then the ten fields `single-book_note.php` reads by name, each written by the template as an ACF field:

| Column | What the template does with it |
|---|---|
| `book_cover_image` | the cover, rendered as the hero image |
| `source_book_title` | the book's title |
| `source_book_author` | the book author's display name |
| `author_slug` | the book author's slug, guards the link to the author page |
| `author_website_url` | the book author's own site, guards its link |
| `amazon_url` | the Amazon button, guards it |
| `goodreads_rating` | the numeric rating |
| `goodreads_url` | the Goodreads link, guards it |
| `isbn` | printed in the book's details |
| `achology_rating` | the Achology rating, drives the tick marks in the hero |

Every one of the ten ships as **two** columns, the value and its underscore-prefixed field key twin, exactly as your file's own readme already requires.

## Two things the template reads that are not fields and need no column

`post_excerpt` does double duty: the template prints it as the hero lead and again as `reviewBody` in the schema. And the writer credit is not a column at all: `benjamin-lockwood` is hard coded in the template, so `author` stays the pen name as it is.

## `primary_recommended_course` is out, and it is out on this side already

Stripped from `Book_Note_Upload.csv` this session. The file's header now reads the eighteen columns above. Strip it from `upload_contracts.json` and the two files agree again.

**One consequence to hold.** Three columns are new to the upload file: `author_website_url`, `goodreads_url` and `isbn`. All three exist in the master workbook, so nothing has to be sourced. The 65 book notes already live were imported without them, so their author-site links, Goodreads links and ISBN lines are absent on the page today and will fill in at the re-import that follows the headings sweep. Nothing else changes for them.

OWED BACK: nothing from Code. `upload_contracts.json` is yours to write, verbatim from the eighteen above.

*No em or en dashes in this file; checked before writing.*
