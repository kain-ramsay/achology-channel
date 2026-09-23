**Needs from Chat:** the questions marked ASK below, each named with the one thing it needs; everything else here is done and read back.

# SHIP: Code's inbox worked through, newest first (Kain, S131: "start working through them now please and dont stop until the full 55 have been fully addressed")

**From:** Claude Code, S131 (factory session), Wednesday 23 September 2026. **To:** Claude Chat.
**The list worked:** section 1 of `REPORT__Inbox_Audit_What_Code_Has_Not_Answered_S131.md`, then section 2. One entry per file, in the order worked.

## Entries

### REPLY__The_Instalments_Answer_Corrected_And_The_Pricing_Pages_Search_Values_S380: DONE

- **Post 341, pay-instalments-achology-courses:** pushed with `--with-seo` (body, SEO title, meta description, excerpt) and read back clean. The live excerpt now reads Chat's line word for word; the live body carries no retired figure. Chat's excerpt sat in the record's notes, so it was copied word for word into the record's `post_excerpt` field, which is the field the push sends.
- **The other 249 help records searched** for "two, three", "three or four", "four monthly" and "two or three": no hit in any record or any live help body (the only hit was post 341 itself, now corrected).
- **/pricing/, page 36845:** search title, description and focus keyword set exactly as Chat typed them. `page_readiness_board.py --sweep` re-ran the gate: **§3 machine half now passes** (3 checks, 1 recorded carve-out) and is written into the page's DSRD 6 record. **§5 still fails, on one thing Code cannot fix here:** one workbook row in the register points at /pricing/ and its chain is broken at `dest_built` and `dest_in_sitemap`. Its Rank Math score moves at Kain's next Recalculate Scores.

### BRIEF__Switch_On_The_Article_And_Book_Note_Sitemaps_S377: DONE

- Rank Math sitemap settings: `article`, `book_note` and `quote` switched on (the previous settings saved on the server as `~/ach_sitemap_before.json`). Indexing is untouched: the build site still carries noindex.
- `sitemap_index.xml` 200, nine children, each 200: page 35 URLs, faq_article 201 plus 50, **article 200 plus 69 (269), book_note 139, quote 200 plus 50 (250)**, faq_category 15.
- **Left out:** `workbook`, because no workbook is published (0), so its sitemap would be empty; switch it on the day the first workbook goes live.
- The Notion card's sitemap line is Chat's to mark done (Code does not edit the board).

### ASK__Every_Cookie_And_Outside_Script_On_The_Build_Site_S377: DONE (answer below; no setting changed)

**How it was read.** A visitor's-eye load of seven real pages in a fresh browser each time, nothing logged in, once before and once after pressing the banner's Accept: the homepage, an article (`a-diagnosis-actually-describing`), a book note carrying Amazon links (`necessary-endings`), an article that names YouTube (`mark-manson`), a help answer, `/pricing/` and `/about/`. Every request and every cookie recorded. Complianz's own cookie table was also read: **it holds no rows at all** (0 cookies, 0 services), so its local scan has never recorded a result on this install; the visitor load below is the true list.

| Cookie or script | Set by | For | Lasts | Complianz category | Loads |
|---|---|---|---|---|---|
| `cmplz_banner-status` | first party (Complianz) | remembers the banner was answered | 365 days | functional (Complianz's own) | after the visitor answers |
| `cmplz_consented_services` | first party (Complianz) | which services were consented | 365 days | functional | after |
| `cmplz_functional`, `cmplz_preferences`, `cmplz_statistics`, `cmplz_marketing` | first party (Complianz) | the visitor's choice per category | 365 days | functional | after |
| `cmplz_policy_id` | first party (Complianz) | the policy version the choice was made against | 365 days | functional | after |

**Nothing else.** Not one request to any outside host on any of the seven pages, before or after consent: no Google, no Kit, no YouTube, no Vimeo, no Bunny, no Amazon, no Circle. Before consent the pages set no cookie at all.

1. **Kit:** the Kit plugin (`convertkit`) is active but loads nothing on any sampled page; no page on the install carries a Kit form yet (none of 658 Knowledge Hub bodies, and the Kit form render is still a theme item). What it sets once a form exists cannot be read until one does.
2. **Amazon links on book notes:** plain links, acting only on click. No OneLink or Genius Link script loads (23 book notes carry `amazon.` links; none carries a script).
3. **Embedded videos:** none on any published article, book note or help answer (the YouTube mentions are links). No placeholder test is possible until a page embeds one; the course pages that will are not on the install.
4. **Loading before consent that is not strictly necessary:** nothing.
5. **GA4:** GTM4WP is not installed or active on the build install, so the one tracker Kain ruled for launch is not yet present; nothing Google loads today.

### ASK__Are_The_Subjects_And_Topics_Set_Up_And_Editable_Inside_WordPress_S378: DONE (answer below)

Read off the install today.

1. **The terms and their fields.** 7 `kh_category` subjects (general-interest 25 posts, helping-people 89, mental-wellness 240, motivation 67, personal-growth 51, psychology 133, wisdom-for-life 53) and **39** `kh_tag` terms, not 36: the 36 approved topics plus three strays created by an import, `helping-people` (1 post), `motivation` (2) and `psychology` (1), each named in lower case as its slug. `learn-hypnotherapy` has 0 posts. **Every one of the 46 terms has an empty WordPress description, and none carries a Rank Math SEO title or meta description of its own.** Rank Math's defaults apply to all: title `%term% Archives %page% %sep% %sitename%` (so the live title reads "Psychology Archives | ..."), description `%term_description%`, which is empty, so no subject or topic page has a meta description.
2. **What editing in WordPress would change.** Subject pages (`taxonomy-kh_category.php`): the name (H1, breadcrumb, schema) comes from WordPress, so a rename in admin shows; the hero intro comes from the theme's code (`achology_kh_category_intros()` in `knowledge-hub-parts.php`), and WordPress's description is read only as a fallback for a subject the code does not list, which none is; the section lines are in the theme's code. So editing a subject's description in admin changes nothing on the page today, but filling it would give Rank Math a meta description through `%term_description%`. Topic pages have **no template of their own** (there is no `taxonomy-kh_tag.php`): `/learn/tags/{slug}/` answers 200 through the generic fallback, showing the WordPress name only. A topic description typed in admin would appear only as its meta description.
3. **Indexed and in the sitemap.** Rank Math is set to index both term types (robots `index`), but they sit under the build site's noindex today like every page. **Neither is in the sitemap:** `tax_kh_category_sitemap` and `tax_kh_tag_sitemap` are both off. Switching them on is one setting each, the same job as the S377 sitemap brief, and waits on Chat's word since this ask was read-only.
