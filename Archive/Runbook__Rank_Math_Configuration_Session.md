# Runbook — Rank Math configuration session (click-by-click)

From: Claude Code · 2026-07-24
The planning half of the board item "Rank Math WP SEO Plugin Configuration —
Planning & Implementation Session." This turns the session into a click-by-click
run. Sourced from DSRD 3 §5, DSRD 10 §9, and DSRD 1 §9.

## How to read the ownership tags
- **[THEME — done]** the theme already handles this in code (`rank-math-feed.php`
  or a template). Nothing to click; listed so it isn't redone or undone.
- **[DASHBOARD]** a setting to set in WP admin. This is the actual session work.
- **[KAIN INPUT]** needs a value only Kain has (a URL, a logo, an ID).
- **[LIVE CHECK]** confirm against the plugin's real output after the settings
  are in — best done with WP access (see the access note I sent separately).

---

## 1. Modules (Rank Math → Dashboard → Modules)
| Module | Setting | Why |
|---|---|---|
| Local SEO | **OFF** | It published Place schema + a locations feed claiming a physical venue, wrong for an online academy (2026-07-19). The theme restores `EducationalOrganization` typing instead. **[THEME — done]** for the typing; **[DASHBOARD]** to keep the module off. |
| Schema (Rich Snippets) | **ON** | Needed for the site-wide identity graph. Per-page schema is mostly theme-owned; leave the module on but set default types to None per §4. |
| Sitemap | **ON** | Needed. Inclusions in §5. |
| Breadcrumbs | **ON** (function available) but the theme owns the JSON-LD trail | The theme emits `BreadcrumbList` and switches Rank Math's off where it owns a page. **[THEME — done]**. If any template uses `rank_math_the_breadcrumbs()` visually, set separator `>` and home label "Home" to match DSRD 1 §9. |
| Video Sitemap | **OFF** | The About videos are buttons with a Vimeo ID injected on click, so the module finds no `<video>` tag and would build an empty sitemap (DSRD 10 §9). |
| Content AI | **OFF / not used** | Declined sitewide; the theme also removes its analyser test. **[THEME — done]** for the test. |
| Role Manager, Redirections, 404 Monitor, Analytics | Kain's preference | Not schema-critical. Redirections useful at go-live for old→new URL maps. **[KAIN DECISION]** |

## 2. Organisation identity (Titles & Meta → Global, or Setup Wizard)
| Field | Value | Tag |
|---|---|---|
| Person or Company | **Company** | [DASHBOARD] |
| Name | **Achology** | [DASHBOARD] — the theme now also sets `name`=Achology + `legalName`=Achology Transactions Ltd on the org node, so keep this "Achology" so they agree **[THEME — done]** |
| Logo | Achology logo (square + wide as prompted) | [KAIN INPUT] |
| Social profiles (sameAs) | the real profile URLs | [KAIN INPUT] — supply the exact URLs for each active channel (e.g. YouTube, LinkedIn, Instagram, X, Facebook) |

## 3. Titles & Meta — indexing per source (Titles & Meta → Posts / Pages / CPTs / Taxonomies)
| Source | Index? | In sitemap? | Notes |
|---|---|---|---|
| Pages | Index | Yes | |
| Posts (if used) | per use | per use | |
| `article` (KH articles) | Index | Yes | Schema theme-owned **[THEME — done]** |
| `faq_article` (/help/) | Index | Yes | FAQPage + trail theme-owned **[THEME — done]** |
| KH types: `book_note`, `quote`, `workbook` | Index | Yes | Schema theme-owned/spec'd |
| **`review`** | **Noindex, exclude from sitemap** | No | `public=false` by design (fragments, not pages). Confirm Rank Math isn't forcing them in. **[LIVE CHECK]** |
| Taxonomies: `faq_category`, `kh_category` | Index | Yes | CollectionPage + trail theme-owned; Rank Math's stripped **[THEME — done]** |
| `kh_tag`, KH author | Noindex until URLs resolve | No | DSRD 10 §9 notes URLs don't resolve yet |
| Author archives | **Disable / noindex** | No | No WordPress author accounts exist; authorship is the people registry |
| Date archives | **Disable / noindex** | No | Not used |
| Search results | Noindex | No | Default |

## 4. Schema defaults per type (Titles & Meta → [type] → Schema)
Set the **default schema type to "None"** for every source whose schema the theme
owns, so Rank Math doesn't auto-attach a second block: `article`, `faq_article`,
`book_note`, `quote`, `workbook`, Pages using the About/Policies/Our People/
Reviews templates. On singular pages Rank Math emits nothing anyway (Standard 1),
so this is belt-and-braces. On the archive/taxonomy pages (`faq_category`,
`kh_category`, /help/) the theme's filters strip Rank Math's `CollectionPage`
and breadcrumb at output **[THEME — done]** — a **[LIVE CHECK]** should confirm
exactly one of each ships.

## 5. Sitemap (Sitemap Settings)
- Include: Pages, `article`, `faq_article`, `book_note`, `quote`, `workbook`,
  `faq_category`, `kh_category`.
- Exclude: `review` (noindex), `kh_tag` + KH author (until URLs resolve), author
  and date archives.
- Ping search engines: on.

## 6. Links (General Settings → Links)
- **Open external links in a new tab: ON** — DSRD 3 requires it, though the theme
  already sets `target="_blank" rel="noopener"` sitewide, so coverage never
  depends on the plugin. **[THEME — done]** for coverage; **[DASHBOARD]** as
  belt-and-braces.
- Nofollow external links: **off** (let editorial links pass value) unless Kain
  wants otherwise. **[KAIN DECISION]**
- Redirect attachment pages to parent: **ON**.

## 7. Webmaster / verification (General Settings → Webmaster Tools)
- Google Search Console verification code. **[KAIN INPUT / LIVE]**

## 8. Analyser tests already declined [THEME — done]
Five tests are removed in code so scores don't count tests we'll never act on:
title sentiment, title power-word, title number, Table of Contents, Content AI.
No dashboard action needed; listed so they aren't re-enabled expecting a score bump.

---

## What this leaves
Almost every **[DASHBOARD]** row is a WP-admin click that needs a WP login. The
**[KAIN INPUT]** rows (logo, social URLs, Search Console code) are the values to
have ready before the session. The **[LIVE CHECK]** rows are the ones I could
verify directly the moment I have site access — see the access recommendation I'm
sending alongside this.
