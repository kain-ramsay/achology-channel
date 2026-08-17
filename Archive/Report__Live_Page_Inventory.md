# Live Page Inventory — achologytest.com (theme v0.36.7)

From: Claude Code · 2026-07-23 · Kain green-lit producing the full list.
Method: WordPress REST API enumeration (`/wp-json/wp/v2/…`), unauthenticated,
published content only. Snapshot taken today against the live test site.

**Complete machine-readable manifest:** `live-inventory-manifest.csv`
(alongside this note) — 315 rows, columns: url, kind, status,
rendering_template, template_source, note. This markdown is the readable
summary; the CSV is the row-by-row.

---

## Totals

| Kind | Count | Source |
|------|-------|--------|
| WordPress objects (Pages + CPT items) | **223** | REST, exact |
| Theme-owned routes (archives, taxonomy, listings) | **92** | derived from terms + rewrite matrix |
| **Total live URLs** | **315** | |

WordPress objects break down: **22 Pages · 200 FAQ articles · 1 Article ·
0 posts · 0 book notes · 0 quotes · 0 workbooks.** The Hub content types are
empty bar one test article — expected, the import hasn't run.

`template_source` matters for your gate: **REST (assigned)** = the template
WordPress itself reports; **derived** = I resolved it from the theme's
template hierarchy + the rewrite rules (re-verified this session). Only the
21 Pages with an assigned page-template are REST-reported; everything else is
derived but deterministic.

---

## A. WordPress objects (REST, exact)

### Pages (22)
All 22, with the rendering template REST reports:

- `/about/` → **page-about.php** *(derived — no assigned template; matches the
  page-{slug} hierarchy)*
- `/about/instructors/` → template-our-people.php
- `/about/instructors/{slug}/` ×10 → template-author-profile.php
  (amelia-sinclair, benjamin-lockwood, charlotte-avery, declan-fitzpatrick,
  evelyn-montgomery, frederick-martin, gerard-egan, isabella-whitmore,
  jackson-hartley, kain-ramsay)
- `/about/code-of-ethics/`, `/about/manifesto/` → template-policy.php
- `/policies/` → template-policies-index.php
- `/policies/{slug}/` ×7 → template-policy.php (accessibility-statement,
  cookie-policy, disclaimers, privacy-policy, refund-policy,
  terms-and-conditions, trust-statement)

### FAQ articles (200) → single-faq_article.php
URLs follow `/help/{category}/{article-slug}/`. All 200 are in the CSV.
Distribution across the 15 categories is in section B (the counts sum above
200 because articles carry multiple categories with one pinned for the URL —
consistent with the spec).

### Articles (1) → single-article.php
- `/learn/psychology/articles/the-power-of-self-awareness-in-personal-growth-test/`
  — a test/sample item.

---

## B. Theme-owned routes (live URLs, not WordPress objects)

These resolve through the theme, not through a WP Page/post object, so they
never appear as REST items. Enumerated from the taxonomy terms + the fixed
rewrite matrix.

### /help/ archive → archive-faq_article.php
- `/help/` (the Support & FAQs landing)

### FAQ category pages (15) → taxonomy-faq_category.php
- https://achologytest.com/help/achology-basics-and-identity/ — 28 articles
- https://achologytest.com/help/certificates-cpd-accreditation/ — 18 articles
- https://achologytest.com/help/community-and-conduct/ — 8 articles
- https://achologytest.com/help/comparisons-and-alternatives/ — 20 articles
- https://achologytest.com/help/curriculum-and-subjects/ — 5 articles
- https://achologytest.com/help/events-and-mentorship/ — 21 articles
- https://achologytest.com/help/getting-started/ — 13 articles
- https://achologytest.com/help/learning-experience/ — 18 articles
- https://achologytest.com/help/membership-and-access/ — 20 articles
- https://achologytest.com/help/outcomes-and-expectations/ — 24 articles
- https://achologytest.com/help/partnerships-and-press/ — 7 articles
- https://achologytest.com/help/pricing-and-payments/ — 17 articles
- https://achologytest.com/help/privacy-and-legal/ — 28 articles
- https://achologytest.com/help/refunds-and-billing/ — 9 articles
- https://achologytest.com/help/technical-help/ — 22 articles

### Knowledge Hub — /learn/
- `/learn/` → **302 redirect → /learn/articles/** (the temporary self-retiring
  redirect; deletes itself once the /learn/ home is built)
- Cross-category listings (4) → learn-listing.php:
  `/learn/articles/`, `/learn/book-notes/`, `/learn/quotes/`, `/learn/workbooks/`
- Category hub pages (7) → taxonomy-kh_category.php:
  - https://achologytest.com/learn/general-interest/
  - https://achologytest.com/learn/helping-people/
  - https://achologytest.com/learn/mental-wellness/
  - https://achologytest.com/learn/motivation/
  - https://achologytest.com/learn/personal-growth/
  - https://achologytest.com/learn/psychology/
  - https://achologytest.com/learn/wisdom-for-life/
- Category-scoped listings (28) → learn-listing.php:
  each of the 7 categories above × {articles, book-notes, quotes, workbooks}
  (full URLs in the CSV)
- Tag landing pages (36) → **index.php (fallback)** — see flag below. Full URLs
  in the CSV.

---

## Two things worth flagging for the reconciliation

1. **Tag pages have no template yet.** `/learn/tags/{tag}/` resolves (all 36
   terms are seeded and live) but the theme has no `taxonomy-kh_tag.php`, so
   these currently fall through to `index.php`. Not a bug in what's built —
   the tag-landing template simply isn't built yet (page design, pending your
   DSRD reconciliation). Recorded so the gate sees it.

2. **Author profiles confirm the URL conflict I flagged separately.** All 10
   instructor pages are live at `/about/instructors/{slug}/` and there is
   **nothing** at `/learn/authors/…`. That's live evidence for
   `Note_for_Chat__Author_URL_Conflict_DSRD_1.md` — the build sits entirely on
   the §2.2 URL, and §2.4's `/learn/authors/` row is stale.

---

## The one limit (as promised)

REST returns **published, public** content only. Any draft, private,
scheduled, or trashed page is invisible to this method — if the reconciliation
needs those, Kain exports from WordPress. Everything live and public is above.
