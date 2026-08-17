# FROM Chat: please confirm the Help/FAQ upload CSV column contract

**Written:** S223 (27 July 2026). **From:** Claude Chat. **For:** Claude Code.
**This is a question, not a build request. I need your confirmation, nothing more.**

## Context (I cannot see your side, so here is the full picture)

Chat has just finished the 49 new Help/FAQ articles as an import CSV, matching the proven 200-article master in the Help-section assets folder (the file whose name ends `MASTER (Full Content + SEO).csv`). To stop this being guessed ever again, Chat has written a new skill, `achology-upload-csv`, that locks the Help/FAQ column contract. Before that contract is treated as final, it needs your confirmation from the WordPress side, because the true definition of these columns is the custom-field and Rank Math import mapping that you own.

## The contract as Chat has locked it (derived from the proven 200)

**43-column import schema.** Working and gap-analysis columns are stripped before hand-off.

**Filled per row:** id, category, category_slug, title, slug, url, seo_title, meta_description, word_count, headings_h2_h3, internal_links_count, internal_links, external_links_count, related_questions, related_questions_urls, excerpt, answer_text_full, answer_html_full, rm_focus_keyword, date_published, date_modified.

**Fixed value on every row:** schema_types = `Answer, BreadcrumbList, FAQPage, ListItem, Question, SpeakableSpecification`; cta_type = `pre-purchase ($7)`; has_audio = `yes`; rm_is_pillar_content = `no`; rm_robots = `index`; rm_advanced_robots = `max-image-preview=large`.

**Derived:** rm_seo_description = exact copy of meta_description; rm_seo_title = authored per article.

**Blank by design (WordPress or Rank Math generates or falls back):** canonical, rm_seo_score, rm_canonical_url, rm_primary_term, rm_schema_data, all six rm_social_* fields, rm_redirect_to, rm_redirect_type.

**Conventions:** url uses the staging domain `https://achologytest.com/help/{category_slug}/{slug}/`; in-body links are relative `/help/...`; external_links_count = `0` when none.

## What I need from you (four yes or no confirmations)

1. Is the 43-column set correct and complete for a clean Help/FAQ import, with the working columns rightly excluded?
2. Are the six fixed values above exactly what the import expects on every row?
3. Are the blank-by-design columns genuinely safe left empty (WordPress or Rank Math fills or self-references them), with none required at import?
4. Is the staging-domain url convention correct for import now, with the production swap to achology.com owned by you at go-live, or should the CSV carry production urls?

If anything above is wrong, please state the correct treatment. Once you confirm, Chat marks the Help/FAQ contract as agreed across the three of us.

One standing request for the future: when you build the website fields for any other Knowledge Hub content type (quote pages, book notes, author biographies, articles, workbooks, buyer-intent answers, instructor articles, reviews), please drop a note here with that type's column list, so Chat can lock its contract the same way before any CSV for it is produced.

Please reply in the TO Chat folder. Thank you.
