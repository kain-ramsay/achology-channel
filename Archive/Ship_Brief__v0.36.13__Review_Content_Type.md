# Ship brief · v0.36.13 · the `review` content type

From: Claude Code · 2026-07-23 · ship brief (standing practice). Follows
`Brief__Reviews_Content_Type_Proposal.md`, which Kain approved.

## What changed
New `reviews-setup.php` (wired into `functions.php`) registering the **`review`
post type**, plus `acf-json/group_review_fields.json`. Shipped v0.36.13.

## The one design decision worth knowing
**Reviews are registered as data, not pages.** `public => false`, no single
URLs, no archive, excluded from site search. A review is a fragment (median 36
words), so 4,000+ of them with their own URLs would manufacture thousands of
thin pages and breach DSRD 6 §5.8. `/reviews/` and `/testimonials/` stay two
separate root-level pages (DSRD 1 §2.1) for Kain to create; they query this
type rather than being its archive. The Social Proof components (DSRD 4
§14.2) query it the same way.

## Fields
Ten, covering every column of the Notion Review Bank export with nothing
unmapped: `reviewer_name`, `star_rating`, `review_date`, `review_text`,
`course_name`, `source_course`, `primary_school`, `all_schools`,
`review_tier`, `is_featured`.

Two notes on the mapping:
- The export's "Website Published" column maps to **post_status**, not a
  field, so publish state is not duplicated.
- `source_course` (post object) is deliberately empty at import because the 28
  course pages do not exist yet. `course_name` is the text fallback the course
  blocks match on until they do.

## A guard I wrote into the code, please hold it in the page work
`star_rating` is the **individual reviewer's** score, for ordering and for the
stars shown beside their words. It must **never** be aggregated into a
headline rating. Social proof figures stay DSRD 5's, using Udemy's displayed
recency-weighted values, never arithmetic averages of this data (DSRD 4 §14).

## Kain's selection decision (2026-07-23)
Publish all 4,060 Displayable rows; each course page surfaces its own best few
automatically by rating and length; `is_featured` is reserved for the handful
Kain hand-picks for the `/reviews/` hero or homepage. He is not hand-curating
4,000 rows.

## Still open, and my two questions to you stand
From the proposal brief: (1) does the Notion Review Bank still match the
4,517-row 23 March export I worked from, and (2) were any rules agreed in the
earlier review conversations I should honour, particularly on how student
names are displayed and anything GDPR-related about publishing them.

Also for whoever builds the components: **"Mindset Mastery: The Ultimate
NLP-Based Guide to Self-Discovery" has only 3 reviews**, and a few others sit
at 40 to 73 against a 250 cap on the largest. The course block needs a
graceful low-count state.

The import itself is not built yet and is not in this ship.
