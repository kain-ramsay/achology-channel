# ANSWER: there is no Book Note importer yet, so this is the contract to build the file to

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `QUESTION__Book_Note_Upload_Column_Contract.md`.

**The plain answer first: no Book Note importer exists, no Book Note field group exists, and there are zero book notes on the site.** So unlike the Help/FAQ 43, there is nothing to confirm against. What follows is the contract I would build the importer to, read off what the theme and the documents already commit to. Author the master file to this and I build the importer to match, exactly as you proposed.

## What does exist today, so you know what this rests on

- **The post type is registered and routed.** `book_note`, segment `book-notes`, so DSRD 1's `/learn/{category}/book-notes/{slug}/` is already the address shape.
- **The Knowledge Hub templates already read book note fields**: `book_cover_image`, `source_book_author`, `source_book_reference`, `author`. They are read by the card system and by the quote pages that point back to their source book.
- **The card is fully specified.** DSRD 8 section 6.2 pins what a Book Note card shows: cover image, type label, title, italic subtitle, and "by [Author Name]".
- **What is missing:** the ACF field group (only "Article Fields" and "Quote Fields" exist), the importer, and the single template's book note branch.

## The proposed column contract

Ordered as I would consume it. Fixed, derived and blank-by-design are named per column, the way the 43 were.

| # | Column | Consumed as | Notes |
|---|---|---|---|
| 1 | `title` | post_title | The book's title as the note's title. |
| 2 | `slug` | post_name | Authored, never derived from the title at import: the slug is a URL commitment and must not change if the title is edited. |
| 3 | `category` | `kh_category` term | One primary category, matching DSRD 1's category set. |
| 4 | `secondary_categories` | `kh_category` terms | Pipe separated, may be blank. |
| 5 | `book_author` | `source_book_author` | The book's writer. This is the field the Author Hub groups by, so it must match the Authors tab spelling exactly. |
| 6 | `book_author_slug` | link to `/learn/authors/{slug}/` | Derived at import if blank, but authored is safer for the same reason as column 2. |
| 7 | `subtitle` | `source_book_reference` | The italic line on the card, per DSRD 8 section 6.2. |
| 8 | `note_author` | `author` | The Achology pen name that wrote the note, per DSRD 2's assignment. Not the book's author. |
| 9 | `blurb` | post_excerpt | The card and listing summary. |
| 10 | `body_html` | post_content | The five-section note per DSRD 2 section 3.1. |
| 11 | `cover_image_url` | `book_cover_image` | Sideloaded at import into the media library, not hotlinked. |
| 12 | `cover_image_alt` | attachment alt text | Required: DSRD 6 section 11 item 4 makes the filename and alt a pre-upload property. |
| 13 | `amazon_url` | the Get This Book button | **Plain Amazon URL, no wrapper.** See the note below. |
| 14 | `related_quote_slugs` | cross-links | Pipe separated, may be blank at first import and filled by a later pass. |
| 15 | `related_article_slugs` | cross-links | As above. |
| 16 | `rm_focus_keyword` | `rank_math_focus_keyword` | |
| 17 | `rm_seo_title` | `rank_math_title` | |
| 18 | `rm_seo_description` | `rank_math_description` | |
| 19 | `rm_robots` | `rank_math_robots` | Blank by design on almost every row: blank means index, follow. |
| 20 | `first_published` | post_date | See sub-question 1. |
| 21 | `last_modified` | post_modified | See sub-question 1. |

**Blank by design, and not in the file at all:** canonical URL (Rank Math derives it from the address, and a hand-written canonical is how duplicates get created), breadcrumb trail (the theme builds it from the category and DSRD 1's hierarchy), schema type (fixed per post type in the theme, not per row), and the OG image (handled site-wide, never per page).

## Sub-question 1: dates

**Send both as ISO 8601 in the CSV** (`2026-07-29`, or with a time if you have one), and I set post_date and post_modified from them at import.

The reason is the one that bit us this week: WordPress stamps import time onto anything you leave to it, and an import date pretending to be a publication date is a false freshness signal. DSRD 6 section 6: "The date changes only when the content genuinely changes; bumping dates to look fresh is a known trick that AI systems and readers both learn to distrust." If a book note has no genuine earlier date, say so with a single agreed baseline date in the column rather than leaving it blank, exactly as Kain ruled June 2020 as the help section's baseline.

## Sub-question 2: Rank Math fields

**Yes, the same four fields, consumed the same way as the Help/FAQ import:** `rank_math_focus_keyword`, `rank_math_title`, `rank_math_description`, `rank_math_robots`. One difference worth carrying over: the FAQ import also stamps `rank_math_primary_faq_category` so the primary term is pinned rather than guessed. Book notes need the equivalent pin for `kh_category`, and I will build it in, so column 3 must always carry exactly one primary.

**One warning from today, worth heeding before 620 rows are produced.** Rank Math's score is only ever computed inside the editor, so imported posts arrive with no score, and the focus keyphrase decides that score almost entirely: a keyphrase that does not appear verbatim in the article scores about 8, one that does scores about 47. Full evidence in `REPORT__Keyphrases_And_Bulk_Rank_Math_Run.md`. So column 16 should be authored as a phrase that genuinely appears in the note's own opening, not derived from the title. Getting that right in the file costs nothing; fixing it afterwards costs a pass over 620 pages.

## One thing your brief changes here

`BRIEF__Adopt_Amazon_OneLink_Retire_Genius_Links.md` arrived alongside this question and settles column 13: the plain Amazon URL, no Genius Link wrapper, no per-book redirect. **DSRD 1 line 150 still says "Features Amazon Genius Link"**, so the document and the decision now disagree, and that line is yours to correct. The theme has no Genius Link wiring to unpick: nothing in it reads an affiliate field at all yet, so there is nothing to align beyond building the button to read column 13.

*No em or en dashes in this file; checked before writing.*
