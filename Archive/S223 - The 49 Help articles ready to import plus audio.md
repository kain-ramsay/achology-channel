# FROM Chat: the 49 Help/FAQ articles are ready to import, plus the audio to set in motion

**Written:** S223 (27 July 2026). **From:** Claude Chat. **For:** Claude Code.
**Kain has approved these next steps.** This explains what we finished today, gives you the file and its column contract, asks you to lay out and run the exact import-and-audit steps, and sets the audio process in motion.

## 1. What we did today

We completed the 49 new Help/FAQ articles (the gap-analysis set, minus the two parked Professional Directory rows) into a finished import CSV. Each article was written to the house standard: answer first, plain human voice, every acronym glossed in full on first use, at least three internal links, and the thinner ones deepened where a reader needed more. Every in-body link is a relative `/help/...` path.

We assembled them into a **43-column import CSV that matches the proven 200-article master column-for-column**, and verified it: the content gate passes, zero em or en dashes, the fill pattern matches the master exactly, every internal link resolves, meta descriptions are within 155 characters, and the focus keywords are unique. The category rename you flagged is handled: the ten certificate-category rows carry "Accreditation and Certification" with the unchanged slug `certificates-cpd-accreditation`.

## 2. The file and where it is

**Filename:** `Achology_FAQ_49_Help_Articles_IMPORT_43col.csv` (49 rows, 43 columns, byte-order mark on the `id` header, matching the master).
**Location:** Kain is placing it in the Help-section assets folder, beside the master: `000. www.achology.com | All Website Assets/04. Single Page Template Assets/Achology FAQ's (HELP Section)/`.

## 3. The column contract (so you can confirm every column is right)

43 columns, identical schema to the master. Filled per row: id, category, category_slug, title, slug, url, seo_title, meta_description, word_count, headings_h2_h3, internal_links_count, internal_links, external_links_count, related_questions, related_questions_urls, excerpt, answer_text_full, answer_html_full, rm_focus_keyword, date_published, date_modified. Fixed on every row: schema_types = `Answer, BreadcrumbList, FAQPage, ListItem, Question, SpeakableSpecification`; cta_type = `pre-purchase ($7)`; has_audio = `yes`; rm_is_pillar_content = `no`; rm_robots = `index`; rm_advanced_robots = `max-image-preview=large`. Derived: rm_seo_description copies meta_description; rm_seo_title is authored per article. Blank by design (the FAQ system is Rank Math-native, as you confirmed): canonical, rm_seo_score, rm_canonical_url, rm_primary_term, rm_schema_data, all six rm_social_* fields, rm_redirect_to, rm_redirect_type. Conventions: url uses the build domain `https://achologytest.com/help/{category_slug}/{slug}/`; external_links_count is `0`.

## 4. What we are asking you to do next

Please get clear on, then lay out and run, the exact steps to bring these 49 into the site and audit that every column landed correctly. In particular:

- Confirm the import method you will use (the same route that brought the 200 in), and that categories match on `category_slug`, never on the display name, so the renamed-category rows do not fail silently.
- Import the 49, then verify the counts: 49 new `faq_article` rows, 249 total, all indexed and in the sitemap.
- Spot-check a handful end to end (a certificate-category row among them) to confirm the category, the Rank Math title and description, the internal links, and the rendered page all resolve.
- Report back anything that did not import cleanly, any column the importer did not accept, or anything you still need from us. If a column needs to change, tell us the exact treatment and we will fix it at source and re-hand the file.

## 5. The audio, to set in motion

The 49 all carry has_audio = `yes`, so they need spoken versions the same way the 200 do. Kain has asked us to set that process moving now, and you know how it runs. Please kick it off for these 49 and tell us anything you need from us. The article text is the `answer_text_full` column in the same CSV, keyed by `id` and `slug`. If it helps, confirm the voice, the audio file format and naming convention, and the destination (the `008. Audio | Kain Ramsay Voice Files` folder, or wherever the 200's audio lives), and we will provide whatever is missing.

Please reply in the TO Chat folder. Thank you.
