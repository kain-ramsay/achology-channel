# ANSWER: the book note column contract, as the theme actually consumes it today

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Answers:** `QUESTION__Book_Note_Column_Contract.md` (Chat, S235).

## Read this first: there is no book note importer

You asked for the contract "as the theme's importer and the book note template actually consume it today". The honest answer to the first half is that **the theme has no book note importer**. The only CSV importer in the theme is `reviews-import.php`, which is hardcoded to the review post type and its fields, and reads `data/reviews.csv.php`. Nothing reads a book note CSV.

So the column contract below is what the **fields and the templates** consume. Whatever loads it, a plugin or an importer I build, must land the values in these exact meta keys. That decision is still open, and it changes nothing about the columns.

If you want the CSV to go straight in with no new code, say so and I will tell you what a plugin needs; if you would rather I build the importer to match `reviews-import.php`, that is a small named job and needs Kain's word, not mine.

## The contract

Post type `book_note`. Field group `group_book_note_fields.json`. Permalink pattern is `learn/{kh_category}/book-notes/{slug}`, so the category term must exist before the row imports or the address cannot be built.

### WordPress core columns

| Header | What it becomes | Required | Format rule |
|---|---|---|---|
| `post_title` | the note's title, the H1 | yes | plain text |
| `post_name` | the slug, the last segment of the address | no | lowercase, hyphens, no stops; if omitted WordPress derives it from the title, and it is then fixed for good, so set it deliberately |
| `post_content` | the note body | yes | HTML. This is the editor field, so Rank Math can see it and score it, unlike the theme-rendered pages |
| `post_excerpt` | the card description on listings and hubs | yes in practice | plain text, one or two sentences |
| `post_status` | publish or draft | yes | `publish` |
| `kh_category` | the category term, and the middle segment of the address | yes | must match an existing `kh_category` term slug |
| `kh_tag` | tags | no | comma separated existing term slugs |
| `_thumbnail_id` or a featured image URL | the post's own featured image | no | this is separate from the book cover below and is not the same picture |

### The eight book note fields

| Header | Type | Required | What the template does with it | Format rule |
|---|---|---|---|---|
| `author` | select | **yes** | the byline and the author signature block | the `achology_author` slug from the people registry in `people-setup.php`, not a display name. An unregistered slug renders no byline |
| `source_book_title` | text | **yes** | names the book on the page and in the source book callout | the title exactly as the book prints it |
| `source_book_author` | text | **yes** | the book's author, read by the source book callout on article pages as well as here | plain text |
| `achology_rating` | select | **yes** | the only rating that enters schema | one of exactly three values: `recommended`, `highly-recommended`, `essential-reading`. Anything else fails |
| `goodreads_rating` | number | no | display only, social proof on the page. **Never enters schema** (DSRD 10 §9) | number |
| `amazon_genius_link_url` | url | no | the "Get This Book" destination | full URL |
| `book_cover_image` | image | no | the book note card and the source book callout | an attachment. A URL column needs the importer to sideload it first; it cannot be a bare URL in post meta |
| `primary_recommended_course` | post_object | no | the course the note points readers towards | a WordPress **page ID**, restricted to the `page` post type. A course name string will not resolve |

### Three columns not to populate

- **Anything for a book note author biography.** The byline resolves through `author` and the people registry; there is no per-post author field.
- **A star rating for schema other than `achology_rating`.** `goodreads_rating` is display only, by rule.
- **A `book_cover_image` URL, if the loader does not sideload.** It will import as a string and render nothing.

## The two that will bite at volume

1. **`author` and `primary_recommended_course` are both references, not text.** One is a registry slug, the other a page ID. At 598 rows these are where a bulk build goes wrong, because a wrong value fails silently rather than erroring. If it helps, I can export the current author slugs and the course page IDs as a lookup table, the same way I exported the `kh_tag` terms; say the word.
2. **`kh_category` must exist first.** The address contains the category, so a row whose term is missing does not get a broken category, it gets a broken address.

## What I have not done

Nothing is built and nothing is set. This is the assessment you asked for.

*No em or en dashes in this file; checked before writing.*
