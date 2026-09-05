# QUESTION: Full URL export of the LIVE site (for the redirect map)

**From:** Claude Chat, Session 241 (4 August 2026)
**To:** Claude Code
**Type:** Read-only data request. Nothing to build.

## Context you need

The rebuild replaces the live achology.com wholesale. The old site carries roughly 1,500 indexed content URLs: old book notes under `/books/` (post type appears to be a "books" CPT with a `book_categories` taxonomy), quotes under the wise-quotes area, plus articles and pages. Kain has ruled we build a one-to-one 301 redirect map from every old URL to its matching new page, so Google reads the rebuild as an optimisation of existing content rather than a sudden volume drop of new pages. DSRD 1 owns redirects; Chat builds the map against the Book Note Master's 620 slugs and the new URL architecture.

I verified the live structure today by fetching `https://achology.com/book_categories/motivation/`: old book URLs look like `/books/book-overview-of-atomic-habits-by-james-clear/` and `/books/cant-hurt-me/`.

## What I need from you

One export of every published URL on the LIVE site, as a CSV dropped into TO Chat, one row per item with these columns:

`url, post_type, post_title, post_status`

Include every public post type: posts, pages, the books CPT, any quotes CPT, knowledge-base/help articles, and any taxonomy archive slugs you can list cheaply (book_categories terms at minimum). If you have WP-CLI access to the live site, `wp post list` per post type covers it; if you only have the theme locally and no live shell, say so and tell me what you CAN pull (for example the live sitemap URLs), and I will work from that.

## What I will do with it

Build the old-to-new redirect map: matched book pages 301 to their new book note URL (`learn/{kh_category}/book-notes/{slug}`), matched quotes to their new quote pages, unmatched leftovers to their nearest category home. The map lands in DSRD 1's redirect section and travels back to you as part of the go-live brief.

## Please confirm

Drop the CSV (or your constraints) into TO Chat with a line on where the data came from, so the map's provenance is clean.
