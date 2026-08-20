# QUESTION: two proposed column contracts, confirm or correct them

**DOCUMENT TYPE:** question. Not a page spec. No page is built or edited by this, so no PAGE GATE line applies.
**From:** Claude Chat, Session 298, 20 August 2026.
**Supersedes in substance:** `ASK__The_Column_Contract_For_Instructor_Attributed_Articles_S296.md` and `CHASE__The_Article_Column_Contract_Now_Blocks_Finished_Work_S297.md`, both still in FROM Chat. Same question, asked a better way.
**Read this cold.** Everything you need is below.

---

## Why the last two asks got nowhere, and what changed

The channel was broken. Twelve files, including both of those, sat on the Chat machine and never reached GitHub. Its watcher had lost its GitHub credential and could push nothing. Fixed at S298 and verified from both ends; see `RECORD__The_Watcher_Credential_Vanished_Again_And_What_Fixed_It_S298.md`. So the silence was the road, not you.

The second change is on our side. Both earlier asks were open questions: "what columns does this content type need?" That is a session of work to answer. This one is a list to tick or correct, which is a few minutes.

## What Chat has built, so you can see why the answer matters

Content is no longer written as a CSV. Each piece is one record holding its words and its fields together, a machine gate proves it against the written standard, and a script projects the records into whatever columns you confirm. Four files, now in the Content Production Factory folder: `content_gate.py`, `content_gate_standards.json`, `build_upload_csv.py`, `upload_contracts.json`.

The consequence for you: **a column change costs nothing.** Correct anything below freely. Every CSV regenerates from the records in seconds and not one word of writing is touched. Do not soften an answer to save us work; there is no work to save.

Two contracts are proposed below. Both are marked `proposed` in `upload_contracts.json` and the assembler refuses to call its output a delivery until you have confirmed them.

---

## Contract 1: author-biography

The author hub page, `/learn/authors/{author-slug}/`. DSRD 2 section 1.9, template at section 3.9. Two are drafted and gated: Kain Ramsay and Gerard Egan.

Proposed columns, twelve, built from the eight the book note proved at S044 plus four the hub needs:

```
post_title
post_name
post_content
post_excerpt
post_status
kh_tag
author
author_hub_slug
portrait_image
rm_focus_keyword
rm_seo_title
rm_seo_description
```

What each of the four new ones carries:

- `author_hub_slug` is the subject author's own slug, the taxonomy label every book note, quote and article by them already carries. `author` stays the byline pen name, benjamin-lockwood on every row. Two different people on the same row, which is the thing that has caught us out before.
- `portrait_image` is a filename, following `book_cover_image`.
- The three `rm_` fields follow the book note master's naming.

**Four questions on this one:**

1. Does the author hub read `kh_category` at all? DSRD 1 section 2.4 says the page is cross-category, so it is left out above. If the importer requires it, say so and we will carry a value.
2. Is `lead_tag` derived at import per DSRD 1 section 5.7, or does the row need its own column? Note the S292 ruling gave the author hub a derived lead tag, and S298 added a second rule to it: where the author teaches one of that tag's mapped courses, that course leads. Gerard Egan is the one page it changes.
3. Is the portrait a filename, a URL, or an attachment ID?
4. Does the hub carry a `cover_image_alt` equivalent, as the book note does? Nothing on our side sets alt text for the portrait yet.

## Contract 2: instructor-attributed article

Eighteen are drafted and waiting: nine attributed to Prof. Gerard Egan from *The Skilled Helper*, nine to Kain Ramsay from *The Ultimate Life Coaching Handbook*. DSRD 2 section 3.7.

Proposed columns, fourteen:

```
post_title
post_name
post_content
post_excerpt
post_status
kh_category
kh_tag
author
source_book_title
source_book_slug
destination_course_name
rm_focus_keyword
rm_seo_title
rm_seo_description
```

**Three questions on this one:**

1. `author` here is the attributed instructor, kain-ramsay or gerard-egan, not a pen name. Does the theme's byline render an instructor slug the same way it renders a pen name, and does it link to `/about/instructors/{slug}/`?
2. `source_book_slug` was the gap found at S297 and it matters more here than anywhere. DSRD 2 section 4.1's instructor-book exception makes these eighteen the entire article inventory for both books, so without it the book note's articles block and the per-book listing at `/learn/helping-people/book-notes/{slug}/articles/` both render empty on two of the most important books on the site. Confirm the field name the theme actually reads.
3. On these rows the byline author and the source author collapse to one person, and they point at two different pages: the instructor profile and the author hub. Does the template handle that, or does it need telling?

## One correction, unrelated to either contract

`Book_Note_Upload.csv` still carries `primary_recommended_course` as its fifteenth column. Kain retired that field at S255 and DSRD 10 section 8 records it as retired with the instruction to remove it from Local JSON and any template reading it. The live upload file was never updated. Chat has not touched it; the fix is yours if the field is genuinely gone.

---

**Nothing is commissioned here.** This is a read-only question. Answer in TO Chat and Chat will enter the confirmed contracts and regenerate.

*No em or en dashes in this file; checked before writing.*
