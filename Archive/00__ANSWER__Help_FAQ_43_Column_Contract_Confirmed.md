# ANSWER: the Help/FAQ 43-column CSV contract, confirmed. This is the whole answer.

**From:** Claude Code · **27 July 2026, 21:50** · **Re:** the contract question you have now flagged twice.

You are right that I never gave you a clean confirmation. I answered it inside a
long import report at 15:47 and then pointed at that report instead of answering
you directly. That is not an answer, it is a reference. Here it is on its own.

## Confirmed: the 43-column contract is correct, in full, unchanged

**I import the file exactly as you specified it. Nothing in the schema needs to
change. No column was rejected. Nothing is owed at source.**

- **43 columns, the master's own schema, in the master's own order.** Verified
  byte-identical to the 200-article master's header row, byte-order mark on
  `id` included.
- **49 rows.** The two parked Professional Directory rows (`GAP-018`, `GAP-019`)
  and the five working columns dropped by me, as you authorised.
- **Filled per row, all correct:** id, category, category_slug, title, slug, url,
  seo_title, meta_description, word_count, headings_h2_h3, internal_links_count,
  internal_links, external_links_count, related_questions,
  related_questions_urls, excerpt, answer_text_full, answer_html_full,
  rm_focus_keyword, date_published, date_modified.
- **Fixed values, all present verbatim:** schema_types, cta_type, has_audio,
  rm_is_pillar_content, rm_robots, rm_advanced_robots.
- **Derived, both correct:** rm_seo_description is an exact copy of
  meta_description; rm_seo_title is authored per article.
- **Blank by design, all confirmed empty:** canonical, rm_seo_score,
  rm_canonical_url, rm_primary_term, rm_schema_data, the six rm_social_* fields,
  rm_redirect_to, rm_redirect_type.
- **Conventions honoured:** build-domain URLs, relative `/help/...` in-body links,
  external_links_count 0 where no external URL, three or more unique internal
  links per article, ISO dates, pipe-separated H2s.
- **Categories matched on `category_slug`, never the display name.** All nine
  slugs resolved live, the renamed `certificates-cpd-accreditation` among them.

## It is not theoretical. It is imported and live.

**49 of 49 imported clean. 249 `faq_article` posts total.** Rank Math title,
description, focus keyword, robots and primary category all landed. Sitemap
regenerated and carries all 249. A certificate-category row spot-checked end to
end and rendering.

## Two notes on columns the site does not consume, neither a defect

- **`related_questions_urls` is not imported.** The theme renders no
  related-questions block from post meta, so the two entries on GAP-005 and
  GAP-015 that point at the removed Professional Directory articles never reach
  a page and cannot 404 for a reader. Correct them at source if you want the
  file clean; there is no live defect.
- **`has_audio` is not imported.** The theme finds a recording by looking for
  `{slug}.mp3` on disk. The column carries `no` in the file, which is now stale:
  **all 49 have been recorded and are live.** 249 articles, 249 recordings, every
  article matched to its own.

## The one live link question, and your ruling on it stands

I reported `/free-coaching/` as a broken link. It is not: DSRD 1 names it and
DSRD 2 §2.19 specs the page. You ruled it stays. I had already changed it on
Kain's instruction and **I reverted it**; the article carries its original
sentence and its original link. My link checker now reads DSRD 1's URL table
first and reports a planned URL as "not built yet", never as broken.

**Nothing further is owed from me on the contract.**
