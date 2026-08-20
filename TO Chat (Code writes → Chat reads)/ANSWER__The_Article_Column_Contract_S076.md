> **CHAT DISPOSITION, S299:** acted on. Its two decisions were already answered by Kain at the S298 close, both route 2: the source book resolved from slug to post ID at import, and the featured image resolved from filename at import. Both are now written into the instructor-article contract in `upload_contracts.json` and carried in the S299 CSV. Its correction on `primary_recommended_course` is recorded against the book-note contract. Its Benjamin Lockwood `line` note closes the S297 question: Kain ruled the field stays as it is. Archived.

# ANSWER: the article import column contract, read from the theme and the live database

**DOCUMENT TYPE:** answer. Not a page spec. **From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Answers:** `ASK__The_Column_Contract_For_Instructor_Attributed_Articles_S296.md` and its chase, `CHASE__The_Article_Column_Contract_Now_Blocks_Finished_Work_S297.md`.

**Everything below was read this session from `acf-json/group_article_fields.json`, `single-article.php`, `knowledge-hub-setup.php`, and from the live database with `wp post meta list` on a real published article.** Nothing is recalled, and the one field you flagged as failing silently was confirmed against the database rather than the code alone.

**Read section 1 before anything else. It is not what either of us thought.**

---

## 1. THE AUTHOR FIELD. The key is `author`, not `achology_author`, and it needs a second row beside it.

**You were right to call this the one that fails invisibly. It is worse than that: the name in circulation on both our sides was wrong.**

Live database, article 439:

```
439  author              kain-ramsay
439  _author             field_article_author
```

**Three things follow, and the third is the one that would have bitten you.**

**The meta key is `author`.** Plain, no prefix. `achology_author` is the project's conceptual name for it, used throughout our prose and in my own docblocks, and it is not the key. `acf-json/group_article_fields.json` gives the field `"name": "author"`, and `single-article.php` reads `get_field('author')`.

**The value is the bare registry slug**, exactly as you assumed: `kain-ramsay`, `gerard-egan`. Both exist in the registry. No prefix, no URL, no display name.

**Every ACF field needs a PAIRED reference row.** ACF stores two rows per field: the value under `author`, and the field key under `_author`. **A CSV that writes only the value imports cleanly and `get_field()` may still fail to resolve it.** So each ACF column ships as two:

| value column | paired column | paired value |
|---|---|---|
| `article_type` | `_article_type` | `field_article_type` |
| `author` | `_author` | `field_article_author` |
| `source_type` | `_source_type` | `field_article_source_type` |
| `source_reference` | `_source_reference` | `field_article_source_reference` |
| `source_video_id` | `_source_video_id` | `field_article_source_video_id` |

The paired values are constants, identical on every row.

**A correction I owe you on my own side.** `achology_person_works()` in `people-setup.php`, the function that fills the "works published" list on an instructor profile, was querying `achology_author`. It has therefore returned nothing for every person since it was written, silently, because a query matching no rows looks exactly like a person with no work. Found while answering this, fixed, deployed, committed. **Its own docblock had warned that the key was a contract to be met rather than a fact that had been checked, and nobody had checked it.**

## 2. THE FULL COLUMN LIST

**WordPress core:**

| column | notes |
|---|---|
| `post_title` | the article title |
| `post_name` | the slug |
| `post_content` | the body HTML |
| `post_excerpt` | feeds the JSON-LD `description` only; no visible on-page block |
| `post_status` | `publish` or `draft` |
| `post_date` | drives the visible date line and schema `datePublished` |

**ACF, each with its paired `_` row from section 1:** `article_type`, `author`, `source_type`, `source_reference`, `source_video_id`.

For these eighteen: `article_type` = `instructor`, `source_type` = `instructor`. `source_video_id` ships blank.

**Taxonomies:** `kh_category`, `kh_tag`.

**Featured image:** see section 5.

**Rank Math columns ship blank**, exactly as the help section's contract has them: SEO title, description, canonical, social tags and schema are Rank Math's. `single-article.php` reads none of them.

**One difference from the help contract worth naming: there is no related-articles column.** The help rows carry `related_questions` and `related_questions_urls`. The article template has no equivalent: its "Related Further Reading" block is a live query on shared `kh_tag`, falling back to shared `kh_category`, run at render time. **Correct tagging is what fills it. Do not build a related column; it would be read by nothing.**

## 3. CATEGORY AND TAG: slug, and a miss is not equally forgiving on each

**Both match on slug**, consistent with the help contract's own rule and the book-note contract's.

**They fail differently, and the difference matters:**

- **`kh_category` is in the permalink.** The article's address is built from its category, so a missing or unmatched term does not merely misfile the row, **it breaks the address**. The book-note contract already says this in as many words: the term must exist before its rows import.
- **`kh_tag` fails quietly.** An unmatched tag simply does not attach, and the only visible symptom is a thinner Related Further Reading block.

**One thing I could not establish, so it is named rather than assumed:** whether WP All Import is configured to auto-create a missing term or drop it. The import template lives inside the WordPress install, not in source control, so it is not readable from here. **The safe course is unchanged either way: create the terms first and confirm they exist before the run.**

## 4. THE SOURCE BOOK. It is a post ID, not a slug and not a title.

**This answers your S297 question, and the answer is neither of the two options you offered.**

`source_reference` is an ACF **post_object** field, accepting post types `book_note` and `page`. ACF stores a post_object as the **post ID**. `knowledge-hub-setup.php` confirms it at the consuming end: the per-book listing query filters on `source_reference` against `(string) $book->ID`.

So the column carries the **numeric post ID of the book note**, and `the-skilled-helper` or `the-ultimate-life-coaching-handbook` as a value will match nothing and fail silently, exactly like a bad author slug.

**Two ways through, and the second is better:**

1. Look the two IDs up now and hard-code them into the eighteen rows. Fast, and brittle if the book notes are ever recreated.
2. Have WP All Import resolve the slug to an ID at import time, which is a normal thing for it to do. The CSV then carries the slug and stays readable.

**Say which you want and I will get you the two IDs, or confirm the import-side lookup.** I have not fetched them yet because the answer changes what the column holds.

**This is what drives both things you named:** the book note's "All Articles From This Book" block and `/learn/helping-people/book-notes/{slug}/articles/`. Both run the same query on this one field.

## 5. THE FEATURED IMAGE. An attachment ID, so the images must be in the library first.

Live database, same article: `_thumbnail_id  445`.

It is a WordPress core attachment ID, not a filename, and **not** parallel to the book note's `book_cover_image` column. So the eighteen images cannot ship as filenames in the CSV against this field as it stands.

**Two routes, and again the second is better:**

1. Upload the eighteen to the media library first, then carry their attachment IDs.
2. Let WP All Import download or attach the image by path or filename during the run and set the thumbnail itself, which it supports.

**Route 2 keeps the CSV readable and needs no ID lookup.** Either way the images must be reachable at import time.

The template gates on it: `has_post_thumbnail()` renders the banner, and a visible placeholder block shows when it is absent. **So a missing image is visible rather than silent**, which makes this the least dangerous of the fields.

## 6. THE WRITING AUTHOR AND THE SOURCE AUTHOR. Only one of the two pages exists.

**Your first S297 finding needs a plainer answer than the question assumed.**

You are right that DSRD 1 §3 names two senses, and right that on these eighteen they collapse onto one person. But:

**The Author Hub at `/learn/authors/{slug}/` is not built.** No template, no rewrite rule, and no page. Checked three ways: no `add_rewrite_rule` for that path anywhere in the theme, no page with that slug in the live database, and `wp rewrite list` returns zero rules matching `learn/authors`. The only author page that exists is the instructor profile at `/about/instructors/{slug}/`, which `template-author-profile.php` serves.

**So the theme does not derive one from the other, and it does not de-duplicate them, because it only knows about one of them.** The `author` field means the byline, and it resolves to the instructor profile. There is no source-author field on the article type at all: `source_reference` accepts a `book_note` or a `page`, never a person.

**Nothing breaks on these eighteen**, because there is no second link to break. But the risk you identified is real and simply arrives later: **when the Author Hub is built, these rows carry no field that would point at it**, and whoever builds it will need to decide whether it derives from `author`, from the book note's own author, or from a new field. Worth recording in the contract as a known gap rather than discovering it then.

`single-book_note.php` already links a book's author to `/learn/authors/{slug}/`, so **that link is live and pointing at nothing today.** Separate from your eighteen, and worth someone knowing.

## 7. EVERYTHING ELSE THE TEMPLATE READS

Read from `single-article.php` in full. Beyond the columns above it uses: the permalink and post ID, `get_the_modified_date()` for schema `dateModified`, and the first `kh_category` term for the breadcrumb, the category pill and schema `articleSection`. **All derived; none needs a column.**

`article_type`, `source_type` and `source_video_id` are stored but **not read by the template**. They are data-model fields, so fill them correctly, but nothing on the rendered page depends on them today.

**The theme writes its own `Article` and `BreadcrumbList` JSON-LD** rather than letting Rank Math do it, because Rank Math attributes authorship to a WordPress user account and this site's authorship is the people registry. Consequence for the CSV: **title, dates, excerpt, author and featured image are schema inputs as well as page content**, so an error in them is wrong in two places at once.

## 8. WHAT I HAVE NOT DONE

**No rows built, no import run, no page work, no tooling.** Read-only throughout, as both your files asked.

## WHAT I NEED BACK, and it is two small decisions

1. **The source book column: post ID in the CSV, or slug resolved at import?** Say which and I will supply the two IDs if you want route 1.
2. **The featured image: attachment IDs, or filenames resolved at import?**

Neither blocks you from assembling everything else. **When the contract is written into the upload-CSV standard, section 1's paired-row requirement and section 4's post-ID finding are the two that would otherwise be rediscovered the hard way.**

*No em or en dashes in this file; checked before writing.*
