# Report — Rank Math live audit + WebSite name fix

From: Claude Code · 2026-07-24
Ran the Rank Math configuration runbook against the RUNNING site over WP-CLI
(direct SSH now available). The picture is very different from what the runbook
assumed: almost nothing needs clicking. Filing so the runbook and board reflect
reality.

## The one change shipped live
- **WebSite schema name** was emitting `"achology.com"`; set the Rank Math option
  `website_name` to **"Achology"**. Verified in the live homepage JSON-LD: the
  `#website` node now reads `name: "Achology"`. This was the "Rank Math WebSite
  name — dashboard setting" outstanding item. Now closed.
- No theme change, no zip. Live config only.

## Already correct on the live site (runbook rows that are DONE, not pending)
- Identity: Company, org name "Achology", legalName carried; live `#organization`
  emits `EducationalOrganization` name "Achology".
- Logo set, OG default image set.
- Social profiles ALL populated: Facebook, X (@AchologyAcademy), LinkedIn,
  YouTube, Instagram, TikTok. The "[KAIN INPUT] social URLs" ask is already met.
- Modules correct: Local SEO OFF, Video Sitemap OFF, Content AI OFF; Schema ON,
  Sitemap ON.
- Noindex correct: author archives disabled + noindex, date archives noindex,
  search noindex, attachments noindex + redirect on.
- Pages + faq_article indexed and in sitemap; faq_article + Pages schema default
  = None (theme owns output). No double schema on the live surfaces.

## NOT config gaps — waiting on content (do NOT flip yet)
Published counts on the live site: page 22, faq_article 200, **article 1,
book_note 0, quote 0, workbook 0, review 0 (drafts)**. The Knowledge Hub is
effectively empty. So these runbook rows are premature, not outstanding:
- Sitemap inclusion for `article`/`book_note`/`quote`/`workbook`/`kh_category`
  (currently off — correct, they'd be empty sections).
- `article` schema default is still "article" (harmless with ~no content; set to
  None in the same pass when the KH lands).
- `kh_tag` currently index across 36 terms whose URLs don't resolve yet.
- **Recommendation:** set all KH indexing/sitemap/schema-default in ONE pass when
  the Knowledge Hub content is built, not now.

## Still genuinely needs Kain (unchanged)
- Google Search Console verification code (Webmaster Tools). Not yet set.
- Whether the current logo (a 512 favicon) is the intended square logo.

Net: the "Rank Math configuration session" is essentially complete for what is
live; the remainder is one KH pass (content-gated) plus the Search Console code.
