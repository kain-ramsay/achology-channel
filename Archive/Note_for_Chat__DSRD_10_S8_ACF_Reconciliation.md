# Note for Chat — DSRD 10 §8 (ACF Field Reference) needs two reconciliations

From: Claude Code · 2026-07-23 · re: the WordPress Back End card (ACF slice)

I verified all ACF Local JSON groups against DSRD 10 §8. The four groups
(article, quote, book_note, workbook) match §8 field-for-field. Two things
in **DSRD 10 itself** are now out of step with the as-built theme. These are
DSRD edits, so they're yours — I'm not touching the spec.

## 1. The `author` field — §5.4 and §8 contradict each other
- **§5.4** says authorship is an ACF author slug on "Knowledge Hub content"
  (all types).
- **§8** lists `author` **only** under Articles.
- **The build** reads `author` and renders a "by …" byline on **article,
  book_note AND workbook** cards (`knowledge-hub-parts.php`, both the standard
  and featured card renderers). DSRD 2's pen-name assignments also cover all
  Hub types.

Kain's call today: the build is right. I've added `author` to the book_note
and workbook Local JSON groups (theme side, done). **DSRD 10 §8 needs `author`
added to the Book Notes and Workbooks field tables** so the spec matches. Quote
is deliberately excluded — quote cards byline the person quoted (`quote_author`),
never an Achology author.

## 2. §8's `faq_article` rows are stale vs the as-built FAQ system
§8 lists three ACF fields for `faq_article`: `primary_category`,
`also_relevant_to`, `meta_description`. **The shipped FAQ system uses none of
them.** It's Rank Math–native: the pinned category comes from Rank Math's
`rank_math_primary_faq_category` primary-term meta, the category comes straight
off the `faq_category` taxonomy, and the meta description is Rank Math's. There
is no `faq_article` Local JSON group and none is needed — nothing reads those
fields.

Recommend **§8's faq_article rows be rewritten to describe the Rank Math–native
model** (or removed), so the spec stops implying an ACF group that shouldn't
exist.

No blocker for me either way — the theme side is already correct and locked.
