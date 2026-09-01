# REPLY: what each content template actually reads, field by field

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Closes:** job 1 of `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315.md`, and the first item of the OWED BACK line at the foot of `000__THE_PUBLISH_READY_PIPELINE.md`: the template read lists, the "Code confirms" column of its section 3.
**Also answers:** the one question to Code in `NOTE__Sixty_Book_Notes_In_Production_Not_Yet_Ready_S306.md`, at the end.
**Every list below was read this turn** from the template file named above it. Nothing is recalled.

---

## The shared core, every type

Read by every content template through WordPress itself rather than through a field: `post_title`, `post_name`, `post_content`, `post_excerpt`, `post_status`, `post_date`, the featured image, and the two taxonomies `kh_category` and `kh_tag`.

`kh_category` does three jobs and is the one to get right: `achology_kh_permalink()` in `knowledge-hub-setup.php` substitutes the FIRST term into the address, the template builds the breadcrumb from it, and it goes into the schema. With no term the address becomes `/learn/uncategorised/...` and nothing reports it.

`kh_tag_order` and `lead_tag` are read as plain post meta by `courses-setup.php`, lines 342 and 350. `lead_tag` is what DSRD 1 section 5.7 derives the course row from.

The three Rank Math columns are read by Rank Math, not by the theme, under the meta keys `rank_math_focus_keyword`, `rank_math_title` and `rank_math_description`.

---

## 1. The article template, `single-article.php`

**Built, and its spec is signed.** It reads exactly two of its own fields by name:

| Field | Where and what for |
|---|---|
| `author` | line 40. The byline and the author signature block, resolved through the people registry |
| `source_reference` | line 578. The source block, and only when it resolves to a `book_note` post |

**And it reads nothing else.** `article_type`, `source_type` and `source_video_id` are searched for across every PHP file in the theme this turn: zero matches outside the ACF definition. They store facts nothing consumes.

**So the answer to section 3.2's "Code confirms" line is: still nothing reads `article_type`.** The S082 finding holds, re-measured today. The one place it does work is the ACF admin, where it drives the conditional that shows `source_video_id`.

**One consequence worth carrying into the signed spec.** The spec's sentence that the six types "differ by two switches only, both keyed off `article_type`" does not describe what is built, and your own S306 instinct to correct the spec rather than build switching logic to match it is the right one. The source block switches on whether `source_reference` resolves to a book note. The instructor close is authored into the body.

---

## 2. The book note template, `single-book_note.php`

**Built and live.** Nine fields by name, lines 50 and 76 to 84:

`book_cover_image`, `source_book_author`, `source_book_title`, `author_slug`, `author_website_url`, `amazon_url`, `goodreads_rating`, `goodreads_url`, `isbn`, `achology_rating`.

**Three findings, and the first is a real fault.**

**The byline is hardcoded.** Line 792 passes `'author_slug' => 'benjamin-lockwood'` into `achology_content_foot()` as a literal. The book note's own `author` field is written at import and never read for the byline. It is harmless today, because the register says the value is benjamin-lockwood on every row, and it is the same shape as the Tasha Eurich fallback: a literal standing in for a field, invisible until the day the value differs. **Mine to fix, and I will fix it in the same change set as the book note page's next work**, which is where the S311 section header rebuild is already waiting.

**`amazon_genius_link_url` is read by nothing.** It is in the confirmed fifteen column contract; the template reads `amazon_url`, which the contract does not carry. This is the gap section 3.3 already records from S086, and it is worth naming again because the OneLink ruling at S309 lands on exactly this field: step 2 of that ruling appends the tag to the Amazon URL "at source (the CSV column)", so the column it lands on has to be the one the template reads.

**`cover_status` is an ACF field nothing reads**, and `prod_subtitle`, `prod_first_published` and `prod_cover_image_alt` are record-side only. Zero matches for all four in the theme. That is correct rather than a fault, and it is stated so nobody adds a column for them.

---

## 3. The quote template

**It does not exist.** There is no `single-quote.php` in the theme. The `quote` post type is registered and live, its ACF group is real, and a published quote would fall through to `index.php`, which is the design system proof page.

So section 3.4's "Code confirms" line stays open, and it cannot be closed by reading. The quote page is item 3 of `BRIEF__The_Four_Content_Templates_Are_Yours_With_Kain_S303`.

**What the quote CARDS read**, which is the nearest real answer today: `quote_text`, `quote_author` and `source_book_reference`, in `knowledge-hub-parts.php` sections 6.3 and 6.6. That is the card, not the page, and it does not settle the page's list.

---

## 4. The workbook template

**It does not exist either**, and its full state is in `REPLY__The_Article_And_Workbook_Column_Contracts_S092.md`, filed beside this file today. In short: the post type is live, zero workbooks exist, there is no `single-workbook.php`, and of its four ACF fields only `author` is read by anything. The two workbook cards read title, excerpt, featured image and author.

So section 3.5's "Code confirms" line stays open on the same terms as the quote's.

---

## The answer to the S306 book note question

You asked whether `primary_recommended_course`, retired at S255, had been stripped from the live `Book_Note_Upload.csv`.

**It has not. The header still carries it**, read this turn, and the file also still lacks `author_slug`, which the contract gained at S299.

**My recommendation is not to strip it.** That file is no longer an import path at all: pipeline section 1 item 3 retires the upload CSV for every Knowledge Hub type, and section 6 keeps `build_upload_csv.py` for regenerating master sheets only. Editing a dead file to make it correct leaves a dead file that now looks live, which is the worse of the two states. **The clean move is to delete `Book_Note_Upload.csv` outright**, so nobody can import from a shape that disagrees with the records.

That is a deletion of a file in your and Cowork's folder, so it is not mine to make. Say the word and I will do it, or do it yourself.

OWED BACK: one word on deleting `Book_Note_Upload.csv`. The three remaining "Code confirms" lines, for quote and workbook, close when their pages are built, not before.

*No em or en dashes in this file; checked before writing.*
