> **ARCHIVED, Session 268, 12 August 2026.** Read and used. Both cards it was written to settle have moved from To Do to In Progress with the counts written into them: **Build WordPress Back End** (five content types registered, three taxonomies populated, six field groups version controlled in the theme, analytics absent rather than unconfigured, search absent, four of five Knowledge Hub types empty) and **Plugins and Site Configuration** (nine plugins, all active, four configured and doing real work, nothing installed but inactive). Claude's S267 inference that the site search plugin was live is corrected on both cards. One thing Code asked for is answered on the back end card and goes to him in the channel at this session's close: the four legacy suite names, which were already sitting in that card's own definition of done. The workbench guard half of this file needs no card: it is closed, Kain's outcome met, and it is below board altitude.

# MEASUREMENT: the WordPress back end, read from the site rather than from any document

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `APPROVED__Install_The_Package_Plus_One_Back_End_Measurement_S267.md`, items 2 and 3.
**Every number below came out of the live database or the theme on disk this session.** No opinion on either board card; the counts settle them.

## 1. Post types

| Post type | Public | Published items |
|---|---|---|
| `faq_article` | yes | **250** |
| `page` | yes | 26 |
| `article` | yes | **1** |
| `book_note` | yes | **1** |
| `quote` | yes | **0** |
| `workbook` | yes | **0** |
| `review` | no | **4,517** |
| `post` | yes | 1 |
| `attachment` | yes | 18 |

**All five Knowledge Hub types are registered. Four of them are empty or nearly so.** The templates exist and are deployed; the content does not. `book_note` holding one against a master of 601 is the same fact I reported on the Book Note page, seen from the other side.

## 2. Taxonomies

| Taxonomy | Attached to | Terms |
|---|---|---|
| `faq_category` | `faq_article` | **15** |
| `kh_category` | `article`, `book_note`, `quote`, `workbook` | **7** |
| `kh_tag` | `article`, `book_note`, `quote`, `workbook` | **36** |

Both Knowledge Hub taxonomies are registered against all four content types and populated. Nothing outstanding.

## 3. Field groups, and the one part worth reading twice

**Six field groups exist, held as version-controlled JSON in the theme** at `acf-json/`: about videos, article fields, **book note fields**, quote fields, review fields, workbook fields.

**Only two are in the database as posts:** Article Fields and Quote Fields.

**That difference does not mean four are missing.** I checked rather than reasoned: the one `book_note` post returns real values for `source_book_author` (Viktor Frankl), `isbn` (0807067997) and `book_cover_image` (attachment 10902). The fields resolve, so ACF's local JSON is doing its job whether or not the database holds a copy.

**Version-controlled is the answer to your question:** all six live in the theme repository, so they survive a database reset and travel with a deploy.

## 4. Plugins

Nine, **all active. Nothing is installed-but-inactive.**

| Plugin | Version | Configured, where I can tell |
|---|---|---|
| `advanced-custom-fields-pro` | 6.8.7 | **Configured.** Six field groups resolving on real posts |
| `seo-by-rank-math` | 1.0.276 | **Configured.** Generates the sitemap, holds titles, descriptions and keyphrases across the help section |
| `seo-by-rank-math-pro` | 3.0.118 | Active alongside the free plugin |
| `complianz-gdpr` | 7.5.2 | **Configured.** The consent mechanism is built and verified, with the footer control the Cookie Policy promises |
| `sg-security` | 1.6.5 | **Configured**, and its bot challenge is why page_gate fetches through an SSH mirror |
| `sg-cachepress` | 7.8.0 | **Configured.** `wp sg purge` works and every gate run purges before measuring |
| `wordpress-starter` | 3.4.7 | Host plugin, no configuration of ours |
| `wp-all-import` | 4.1.1 | **Installed, not visibly configured.** The 250 help articles arrived through it, so it has been used |
| `import-xml-csv-settings-to-rank-math-seo` | 1.2 | Companion to the importer |

## 5. The four legacy suites

**None of the nine above is a legacy suite, and there are no inactive plugins at all**, so nothing from the old site is sitting dormant.

**I cannot go further than that honestly.** The commission names "the four legacy suites, by name" and I do not hold those names. Send them and I will confirm each in a single pass. What I can state without them: the list above is the complete set, active and inactive, and it is nine.

## 6. Analytics and tracking: nothing is present

**No analytics container. No tag manager. No tracking of any kind.**

Checked on the delivered markup of `/about/`: zero occurrences of `googletagmanager`, `gtag`, `GTM-` or `analytics`. Three apparent hits on `G-` turned out to be letters inside `Achology-OG-Default-Image.png`, so I opened them rather than counting them.

**None of the ten named events can fire, because there is nothing to fire into.** This is the emptiest part of either card.

## 7. Search: no plugin

None installed. Nothing is indexing the content types.

## What this settles, without my opinion

**"Build WordPress Back End" is substantially further on than To Do.** Post types, taxonomies, field groups and templates exist and hold real content in the help section. Missing: content in four of the five Knowledge Hub types, and search.

**"Plugins and Site Configuration" is genuinely mixed.** Four plugins are configured and doing real work. Analytics is not merely unconfigured, it is absent. Search is absent.

---

# The `/cards/` workbench: done, and my first attempt was wrong

Kain's outcome, in your words: never reachable by a member of the public, at cutover or after, and the component gate can still read it.

## Draft is not available, tested rather than assumed

I set the page to draft and fetched it anonymously: **404**. So the gate cannot read a draft either, and the page has to stay published with something else keeping it away. Restored to published immediately.

## My first mechanism reported itself as working while protecting nothing

I keyed the guard on `REMOTE_ADDR`, reasoning that the gate fetches from the loopback and the public cannot. I deployed it and fetched from outside: **200.** Behind SiteGround's proxy `REMOTE_ADDR` is not what a naive reading expects, so the loopback exemption matched everybody and **the guard let the whole world through.**

**I caught it only because I tested the refusal rather than the permission.** Had I checked that the gate could still read the page and stopped there, I would have reported this as done and it would have been a public page wearing a guard. The failure is recorded in the code above the working version rather than quietly replaced, because the next person to touch it should meet the reasoning that failed.

## What is there now, and it depends on no network topology

The page answers only a request carrying a workbench key as a query parameter. Proved in four directions:

```
public, no key:      404
public, wrong key:   404
with the key:        200
control, /about/:    200
```

**Both gates carry the key**, because four build sheets name `/cards/` as their specimen and without it the component gate would fetch a 404 and report cards that had stopped matching their sheets. Verified: `page_gate` reads the page and returns its full measurement.

**It lives in the theme**, so it is version controlled, survives a database reset, travels with every deploy, and cannot be forgotten at cutover the way a plugin setting can. That was your concern and it is the reason it is not a Rank Math setting.

**On the key being a secret: it is not one and is not meant to be.** The page holds card specimens and nothing else. Its job is to be unreachable by accident and unfindable by a crawler, not to withstand an attacker. Say the word if you want it treated as a credential instead and I will move it out of the repository.

*No em or en dashes in this file; checked before writing.*
