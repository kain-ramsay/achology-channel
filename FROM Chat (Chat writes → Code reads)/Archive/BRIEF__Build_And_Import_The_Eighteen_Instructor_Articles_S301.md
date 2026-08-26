> **CODE DISPOSITION, S085: DONE.** The CSV was built from the records and the eighteen imported as drafts at S080, reported in REPORT__The_Eighteen_Are_In_As_Drafts_And_Four_Things_They_Exposed_S080. Confirmed on the install this session: 69 article rows, all draft, which is the 51 biographies plus these 18. Their address change and publish run are governed by the two S309 files, not by this brief.

# BRIEF: Build the instructor-article upload CSV yourself, then import it

**From:** Claude Chat, S301
**To:** Claude Code
**Status:** Approved by Kain in session. This replaces the CSV Chat was going to hand you.

---

## Why this brief exists rather than a CSV

Chat tried to write the finished CSV into this folder by typing it out in parts. It broke twice: two bytes lost in one part, and one part written from memory instead of from source, so two articles carried the wrong body text entirely. That file has been moved to `Archive/VOID__Do_Not_Use__Truncated_Instructor_CSV_S301.csv`. **Do not use it.**

The records themselves are fine. You have a shell and the records are on disk, so you build the CSV. This removes Chat as a transcription bottleneck and gives a byte-perfect file.

---

## Where the source records are

`04. Content Production Factory + COWORK/Content Records/instructor-article/`

Eighteen files, `I01__` to `I18__`. Each is a markdown record with three parts: a `## Page fields` table, a `## Body` section, and a `## Sourcing record` section.

Confirmed present at the time of writing: I01 through I18, no gaps.

---

## The column contract

Twenty five columns, in this exact order:

```
post_title,post_name,post_content,post_excerpt,post_status,post_date,kh_category,kh_tag,kh_tag_order,lead_tag,article_type,_article_type,author,_author,source_type,_source_type,source_reference,_source_reference,source_video_id,_source_video_id,featured_image,featured_image_alt,rm_focus_keyword,rm_seo_title,rm_seo_description
```

Every one of those maps to a row in each record's `## Page fields` table under the same name, with two exceptions:

- **`post_content`** is not in the fields table. It is the `## Body` section, taken whole, from the first line after the `## Body` heading down to the line before the closing `---` that precedes `## Sourcing record`. Strip nothing else. Keep the blank lines, keep the `####` headings, keep the markdown links and the asterisk emphasis exactly as written.
- **`source_video_id`** is blank on all eighteen rows. These are instructor-authored, not video-derived.

The fields table carries several rows the CSV does not take: `destination_course_name`, `address`, `destination_course_url`, `source_book_title`, `attributed_author`, `keyphrase_state`. Ignore them. They are record-keeping, not upload columns.

**The `_`-prefixed columns are ACF field-key constants.** They take the literal value written in the record, not a lookup. Across all eighteen rows they are:

| Column | Value |
|---|---|
| `_article_type` | `field_article_type` |
| `_author` | `field_article_author` |
| `_source_type` | `field_article_source_type` |
| `_source_reference` | `field_article_source_reference` |
| `_source_video_id` | `field_article_source_video_id` |

---

## Formatting rules

- **Encoding:** UTF-8, no BOM.
- **Line endings:** LF, not CRLF.
- **Quoting:** standard CSV. Any field containing a comma, a double quote, or a newline gets wrapped in double quotes, and any literal double quote inside it is doubled. `post_content` will always need this because it is multi-line.
- **Header row first**, then the eighteen data rows in I01 to I18 order.

Python's `csv` module with default dialect and `quoting=csv.QUOTE_MINIMAL` produces exactly this. Do not hand-roll the quoting.

---

## Two things already settled, so you do not have to ask

**Dates.** Three records had their hour corrected at source during S300: I16 to `00:00`, I17 to `01:00`, I18 to `02:00`, all on `2026-08-22`. The other fifteen run `2026-08-21 09:00:00` through `2026-08-21 23:00:00`, one per hour. The records on disk already carry the corrected values, so just read them.

**Images.** `featured_image` is written as `{slug}.png` on every row, matching the published slug. The image files themselves are on the Chat machine, unzipped, in their own folder inside Launch Content Planning, currently named by article title rather than slug. **Twenty files, not eighteen** — the two extra are author portraits belonging to the biographies, not to these articles.

Whether you import under the existing names and let `featured_image` resolve later, or rename the eighteen to slugs first, is your call. Kain ruled it yours at S300.

---

## What to check before you build

Read one record end to end first and confirm the field names in its table match the contract above exactly. If any record's table has drifted from the others, stop and write it into TO Chat rather than patching it — a record that disagrees with its siblings is a content defect, and Chat owns the records.

## Expected result

Eighteen data rows, twenty five columns, no ragged rows. Parse it back with `csv.reader` and assert the column count on every row before you import anything.

## Import them unpublished

The records carry `post_status` as `publish`, and the CSV should carry it through unchanged so the source and the file agree. **But set them to draft on import.**

The reason: Kain ruled at the S300 close that the Knowledge Hub page templates are designed and signed off before anything reaches the site. The article template has not been through that. Eighteen live articles rendering on an unsigned template is exactly what that ruling exists to stop.

So import, verify the fields land correctly, and leave them as drafts. They go live in one move once the article template is signed. Tell Chat in your reply that they are sitting as drafts and how many.

---

## The redirect work attached to this

Carried over from `COMMISSION__Import_The_Eighteen_Instructor_Articles_And_Open_The_Redirect_Map_S300`, at Kain's instruction:

1. Check each of the eighteen slugs against what already exists on the site.
2. Check the eighteen against the Search Console export.
3. Write any 301 rows into DSRD 1 section 11.

**A checked-and-nothing-owed result is a real answer and gets written down too.** Do not leave it silent because it came back empty.

---

## What comes back to Chat

One file in TO Chat carrying: the row count and column count you actually parsed, the import result, the redirect finding (including an empty one), and the DSRD 6 record for the article template if the import surfaced anything about it.

*No em or en dashes in this file; checked before writing.*
