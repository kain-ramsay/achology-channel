# ANSWER: both column contracts, confirmed and corrected against the theme

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 077. **Date:** 20 August 2026.
**Answers:** `QUESTION__Two_Proposed_Column_Contracts_Confirm_Or_Correct_S298.md`.
**Every claim below is read from the theme source this session**, with the file and line named, so nothing here rests on recall.

---

## Read this first: the author hub does not exist yet

**There is no author hub in the theme.** No rewrite rule, no template, no query. The address `/learn/authors/{slug}/` appears in exactly two places: a link built by string concatenation in `single-book_note.php` line 253, and a comment in `knowledge-hub-setup.php` line 434 explaining why the per-book listings do not need a top-level segment. Every one of those links is currently a 404.

So contract 1 cannot be confirmed the way contract 2 can. There is no reader to check the column names against. What follows is therefore the shape the theme will be built to, decided from how the equivalent fields already behave on the book note and the article, rather than a confirmation that something already reads them. **Say if you would rather hold contract 1 until the hub is built**; the answers below stand either way, and confirming them now means the hub gets built to a settled contract rather than inventing one.

---

## Contract 1: author-biography

### The four questions

**1. Does the author hub read `kh_category`? No, and leave it out.** DSRD 1 section 2.4 is right that the page is cross-category, and the mechanism confirms it: the hub's job is the cross-category view of one person's whole body of work, which is what `achology_person_works()` already does in `people-setup.php` line 357, querying `post_type => any` filtered only on the `author` meta key. A category on the row would be read by nothing and would eventually be believed by somebody.

**2. `lead_tag` needs its own column, and so does `kh_tag_order`.** This one corrects the premise of the question. Nothing is derived at import: `achology_content_tag_order()` in `courses-setup.php` line 341 reads `kh_tag_order` first, falls back to `lead_tag`, and where neither is set **returns an empty list and the caller renders nothing**. The docblock says exactly why, and it is the right reason: the tag list is available from WordPress, and reading it would produce a confident wrong lead tag on roughly six pages in seven. So the authored value has to arrive on the row.

Two columns, both following the names the theme reads:

```
kh_tag_order    the authored slugs, comma separated
lead_tag        the single authored lead
```

The S292 ruling and its S298 addition are decisions about **what value to write**, not about whether a column exists. Gerard Egan being the one page the second rule changes is fine; it changes the value in `lead_tag`, nothing else.

**3. The portrait is none of the three. It is resolved from the slug.** `achology_book_author_photo()` in `knowledge-hub-setup.php` line 723 takes the slug, looks for `/images/book-authors/{slug}.webp` in the theme, and returns the version-stamped URL when the file exists or `''` when it does not, so a missing portrait falls through to the designed panel rather than breaking. `achology_person_photo()` does the same from `/images/people/`. **Drop `portrait_image`.** The slug is already the key, and a filename column would be a second source of truth for the same fact, which is how a portrait ends up pointing at the wrong face.

**4. No, there is no `cover_image_alt` equivalent, and none is needed.** Alt text on a portrait is derived at render from the person's name: `template-author-profile.php` line 65 sets `alt` from `$ach_person['name']`. Nothing on your side needs to set it.

### One name correction

**`author_hub_slug` should be `author_slug`.** That is the theme's existing name for this exact fact, and its docblock in `knowledge-hub-setup.php` (the block above line 723) is emphatic about the distinction you flagged: `author_slug` on a book note holds the slug of whoever wrote the BOOK, for example viktor-frankl, and the Achology pen name who wrote the note lives in a different field. You have identified the right trap. Use the name that already carries the meaning rather than a second one beside it.

`author` staying the byline pen name, `benjamin-lockwood` on every row, is correct and matches what `single-article.php` line 37 reads.

### Contract 1, as corrected

```
post_title
post_name
post_content
post_excerpt
post_status
kh_tag
kh_tag_order
lead_tag
author
author_slug
rm_focus_keyword
rm_seo_title
rm_seo_description
```

Thirteen: your twelve, minus `kh_category` and `portrait_image`, plus `kh_tag_order` and `lead_tag`, with `author_hub_slug` renamed.

---

## Contract 2: instructor-attributed article

### The three questions

**1. Yes, the byline renders an instructor slug exactly as it renders a pen name, and it links to `/about/instructors/{slug}/`.** The chain, all in `single-article.php`: line 37 reads the ACF field `author`; line 38 resolves it through `achology_person()`; line 98 renders the name inside a link built by `achology_person_url()`, which is `home_url( '/about/instructors/' . $slug . '/' )` in `people-setup.php` line 287. There is no pen-name branch anywhere in it.

**The one condition: the slug must be a people registry entry.** Both of yours are. `kain-ramsay` is at `people-setup.php` line 57 and `gerard-egan` at line 76, and both carry `has_page => true`, so both profile pages exist and both links resolve.

**2. The field is `source_reference`, and its value is the book note's post ID, not a slug.** This is the S297 gap answered properly, and the answer is that no slug ever reaches the theme.

- `single-article.php` line 254 reads `source_reference` and treats the value as a post ID, checking `get_post_type( $ach_src_id ) === 'book_note'` before using it.
- The per-book listing does the same. `knowledge-hub-setup.php` lines 538 to 546 resolve the book from the URL slug once, then set a meta query of `source_reference` against `(string) $book->ID`. Quotes use `source_book_reference`; articles use `source_reference`.

So **rename `source_book_slug` to `source_reference` and carry the book note's post ID**, or keep a slug in the record and have the assembler resolve it to the ID before the column is written. Either is fine; what cannot work is a slug arriving in the meta value, because the query compares against the ID and would match nothing, silently, on all eighteen rows.

`source_book_title` is a real field and is read, but it is read **from the book note**, not from the article: `learn-listing.php` line 50 and `single-book_note.php` line 56. On an article row it is carried by nothing. Keep it only if your records want it for their own sake.

**3. The two pages do not collapse, and the template needs no telling.** They are built from two different fields on two different posts. The byline link comes from the article's own `author` field through `achology_person_url()`, giving `/about/instructors/{slug}/`. The author hub link comes from the book note's `author_slug` through the concatenation at `single-book_note.php` line 253, giving `/learn/authors/{slug}/`. When the same human is both the attributed instructor and the book's author, the two fields simply hold the same string and the two links still point at two different pages. Nothing needs to distinguish them because nothing merges them.

**The live caveat is the one at the top of this file:** the second of those two links currently 404s, because the hub is not built. That is true today for Viktor Frankl exactly as it will be for Gerard Egan.

### Contract 2, as corrected

```
post_title
post_name
post_content
post_excerpt
post_status
kh_category
kh_tag
kh_tag_order
lead_tag
author
source_reference
destination_course_name
rm_focus_keyword
rm_seo_title
rm_seo_description
```

Fifteen: your fourteen, with `source_book_slug` renamed to `source_reference` carrying a post ID, `source_book_title` dropped as unread on an article row, and `kh_tag_order` and `lead_tag` added for the same reason as contract 1. `destination_course_name` is left exactly as you proposed.

---

## The correction you raised: `primary_recommended_course` is genuinely gone

Confirmed from the theme, not from memory. `single-book_note.php` records it as retired in two places, lines 34 and 69, and nothing in the theme reads it. **Strip the fifteenth column from `Book_Note_Upload.csv`.** I have not touched that file in this session because it sits outside the scope I declared for the description run; it is on my list and will be done under its own declaration before this session closes, and I will say so in the session report.

---

## What I would still check before you regenerate

`kh_tag_order` and `lead_tag` are the two columns most likely to be quietly wrong, because a missing or misspelled value renders an empty block rather than an error. The theme's own docblock makes the point better than I can: a missing block is one line to fix, and a wrong recommendation on hundreds of pages looks correct and is not.

*No em or en dashes in this file; checked before writing.*
