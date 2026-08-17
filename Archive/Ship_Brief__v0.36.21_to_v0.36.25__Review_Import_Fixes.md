# Ship brief — v0.36.21 to v0.36.25, the review import fixes

From: Claude Code · 2026-07-24 · all pushed and uploaded.
Follows `Ship_Brief__v0.36.20__Review_Bank_Importer.md`.

Five versions, four of them me correcting my own work. Recording it honestly
because the lesson is more useful than the outcome.

**What went wrong, in order.**

1. **v0.36.21** — the import stopped after one batch of 200. `wp_nonce_url()`
   escapes its result for HTML, so the `&` separators came back as `&#038;`. A
   browser decodes that inside an href; JavaScript does not decode entities
   inside a string, so `window.location` was handed a mangled query string.
2. **v0.36.22** — replaced the JavaScript continuation with a meta refresh, and
   moved the batch to `admin_init` so it runs before any output. No scripting,
   and no server-redirect chain, which browsers abandon after about twenty hops.
3. **v0.36.23** — the real cause. Every review cost about thirty queries:
   `wp_insert_post()` sanitises, builds a unique slug with its own query, fires
   the save hook stack and rebuilds caches, and each of nine `update_field()`
   calls resolves the field, reads the old value and writes two meta rows.
   4,517 reviews meant roughly 135,000 queries. **The batching was a workaround
   for a cost that should not have existed.** Rows are now written directly:
   about 4,700 queries, one pass.
4. **v0.36.24** — the read-back check was gated on a run having created
   something, so on the final run, which created nothing, it never displayed.
   The bank was complete and unproven at once. It now runs on every screen load
   and samples three reviews: first, middle and last.
5. **v0.36.25** — and the check immediately earned itself. The first review read
   back with an empty `review_text`. The version that imported the first 200
   rows named the field `field_review_review_text`; ACF's key is
   `field_review_text`. **ACF does not treat an unresolvable selector as an
   error** — it writes the value under the selector's own name, so those 200
   reviews hold their words in a meta row nothing reads. The 4,317 written by
   the direct path were correct, which is exactly the split the three-point
   sample exists to expose. v0.36.25 adds a two-step rebuild that empties the
   bank and re-imports through the single write path.

**Three things worth carrying into DSRD 10 as rules, not memories.**

- A field written by ACF key must have that key verified against the Local JSON
  group. A wrong key fails silently and looks like success.
- A bulk import verifies itself by reading back through the same API the site
  reads with, and says so on screen. Without that, this defect would have been
  found by a visitor looking at a blank quote.
- Data shipped inside the theme is not web readable. `data/reviews.csv.php`
  opens with an `exit` and has an `.htaccess` beside it, verified 403 after
  upload.

**Closed at end of session. The rebuild worked and the check is green.**

  #5487  OLEKSANDR DUDKA, course 001 : all 8 fields read back correctly
  #7745  Mario Edvin Greters, 013    : all 8 fields read back correctly
  #10003 Kerry Werchon, course 028   : all 8 fields read back correctly

New post IDs across the whole range, which is what proves the rebuild really
deleted and re-imported rather than skipping. 4,517 rows, 100 per cent of the
export, every one a draft.

**Nothing displays them yet**, because the course pages, `/reviews/` and
`/testimonials/` do not exist. So publishing is not urgent, and the question of
how a student's name appears beside their words does not block anything until a
page needs to render one. Still worth your answer, just not on the critical path.

**Still with you, unchanged:** the three schema decisions in
`Report__Per_Page_Type_Schema_Inventory.md` §3, the `.about-grid__paths` scope
question, and whether the Notion bank still matches this 23 March export, plus
any prior rule on displaying student names, which is now the only thing between
4,517 drafts and live social proof.
