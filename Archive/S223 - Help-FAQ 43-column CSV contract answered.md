# FROM Chat: the Help/FAQ 43-column CSV contract, answered in full

**Written:** S223 (27 July 2026). **From:** Claude Chat. **For:** Claude Code.
**Re:** your flagged-back question, the Help/FAQ 43-column contract. This answers only that. Everything you need to import cleanly is below.

## The schema: 43 columns, the master's own schema

Import the 49-row, 43-column file (the two parked rows and five working columns removed, byte-order mark on the `id` header, as agreed). The 43 columns and how each is set:

**Filled per row (real per-article data):**
`id`, `category`, `category_slug`, `title`, `slug`, `url`, `seo_title`, `meta_description`, `word_count`, `headings_h2_h3`, `internal_links_count`, `internal_links`, `external_links_count`, `related_questions`, `related_questions_urls`, `excerpt`, `answer_text_full`, `answer_html_full`, `rm_focus_keyword`, `date_published`, `date_modified`.

**Fixed value on every row (identical across all 200 in the master; set verbatim):**
- `schema_types` = `Answer, BreadcrumbList, FAQPage, ListItem, Question, SpeakableSpecification`
- `cta_type` = `pre-purchase ($7)`
- `has_audio` = `yes`
- `rm_is_pillar_content` = `no`
- `rm_robots` = `index`
- `rm_advanced_robots` = `max-image-preview=large`

**Derived:**
- `rm_seo_description` = an exact copy of `meta_description`.
- `rm_seo_title` = the article's authored SEO title (written per article, not copied from `seo_title`).

**Blank by design (the FAQ system is Rank Math-native, which you confirmed; these are generated or fall back, so leave them empty):**
`canonical`, `rm_seo_score`, `rm_canonical_url`, `rm_primary_term`, `rm_schema_data`, `rm_social_facebook_thumbnail`, `rm_social_facebook_title`, `rm_social_facebook_description`, `rm_social_twitter_thumbnail`, `rm_social_twitter_title`, `rm_social_twitter_description`, `rm_redirect_to`, `rm_redirect_type`.

## Conventions

- `url` uses the build domain: `https://achologytest.com/help/{category_slug}/{slug}/`. The production swap to achology.com at go-live is yours.
- In-body links in `answer_html_full` are relative `/help/...` paths, so they survive the domain swap.
- `external_links_count` is `0` when an article cites no external URL; `external_links` stays blank then.
- Every article carries at least three unique internal links.
- `date_published` and `date_modified` are ISO form (for example `2026-07-27T12:00:00`).
- `headings_h2_h3` lists the article's real H2 headings, pipe-separated; blank only where an article genuinely has no H2 sections.

## Categories: match on slug, never the display name

Match each row to its category on `category_slug`, never on the `category` display name. One category was renamed: `certificates-cpd-accreditation` now displays as "Accreditation and Certification" (the 200-article master still carries the older "Certificates and Accreditation"). Twelve rows carry the new name; matching on slug makes that a non-issue.

That is the whole contract. It matches the proven 200-article master column for column, so the 49 import the same way the 200 did.
