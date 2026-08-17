# REPORT: build state snapshot, for one board reconciliation pass

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `BRIEF__Build_State_Snapshot_Companion_To_Page_Gate_Map.md`.
**Read only. Nothing was built, changed or deployed to produce this.** Written for one reader doing one verification pass, as you asked. Companion to `MAP__page_gate_Across_Every_Built_Page.md`, which covers the built pages' readiness; this covers everything around them.

Theme at **v0.36.31**, deployed to achologytest.com today.

## 1. Theme and template inventory

**Built and serving real pages:**

| Page type | Template | State |
|---|---|---|
| Policy pages, 7 | `template-policy.php` plus a content file each | Built. Copy baked in the theme, editor empty by design |
| The Manifesto, the Code of Ethics | same template, `--doc` variants | Built |
| Policies index | `template-policies-index.php` | Built, rows authored in the template |
| About | `page-about.php` | Built |
| Our People | `template-our-people.php` | Built |
| People profiles, 10 | `template-author-profile.php` | Built |
| Testimonials | `page-testimonials.php` | Built |
| Help article, 249 | `single-faq_article.php` | Built, with audio and follow-along timings |
| Help listings | `archive-faq_article.php`, `taxonomy-faq_category.php` | Built |
| Knowledge Hub listings | `learn-listing.php`, `taxonomy-kh_category.php` | Built |
| Knowledge Hub single | `single-article.php` | Built for `article`, and reads book note fields, but no book note has ever rendered through it |
| 404 | `404.php` | Built |

**Templates that exist but serve almost nothing today:** `single-article.php` (one article live), and the whole Knowledge Hub listing layer, which renders empty categories.

**Absent entirely:** the Author Hub. DSRD 1 line 101 specifies `/learn/authors/{author-slug}/`, and **`/learn/authors/` returns 404 today**. No template, no route.

**One redirect worth noting:** `/learn/` returns 302 rather than 200. It goes somewhere sensible, but if a card or spec claims `/learn/` is a landing page, it is currently a redirect.

**Dead file found today:** `policies-content/policies.php`, an unreferenced copy of the Policies index copy, carrying seven em dashes and stale row descriptions. Nothing reads it. Reported into your collapse brief, not deleted.

## 2. WordPress back-end state

| Thing | State |
|---|---|
| `faq_article` | **249 published.** Fully populated: content, categories, audio, timings, focus keyphrases on 223 |
| `page` | **23 published.** The whole built set |
| `article` | Registered, **1 published** |
| `book_note` | Registered and routed, **0 published** |
| `quote` | Registered, **0 published** |
| `workbook` | Registered, **0 published** |
| `review` | Registered by `reviews-setup.php`, **0 published** |
| `post` | 0, deliberately |
| `faq_category` | 15 terms, populated |
| `kh_category` | 7 terms, **no content in them** |
| `kh_tag` | 36 terms, effectively unused |
| ACF field groups | **Two only: "Article Fields" and "Quote Fields".** No Book Note group, no Workbook group, no Review group |

**The honest headline for the Build WP Back End card:** the back end is built for the help section and the built pages, and it is scaffolding for everything else. Post types and taxonomies exist; the content, the field groups and the importers do not.

## 3. Deployed but untracked, as far as I know

1. **The audio system.** 249 MP3s and 249 timings files in uploads, 308MB, plus the Listen button, the sentence highlighting, and a regeneration pipeline that now rents its own GPU. I do not believe any card tracks the pipeline as an asset, and it has a running cost and a rebuild recipe.
2. **`rank-math-feed.php`.** It feeds the rendered page to Rank Math's analyser whenever the editor is empty, which is what makes the theme-built pages scoreable at all. It is the fix for a problem the board may still show as open.
3. **The three gate scripts and the harness hooks.** `page_gate.py`, `css_gate.py`, `article_gate.py` and six hooks. Excluded from the shipped zip, so they exist only in the repository.
4. **The score run instrument** built today: it drives Kain's own Safari because the host refuses automated browsers. Worth a card of its own, since anything needing the WordPress admin in bulk will hit the same wall.
5. **Direct deployment.** As of today I deploy theme changes to the build site myself over SSH rather than handing Kain a zip. That changes the ship step any card describes.

## 4. Claims against the build

1. **DSRD 1 line 150: "Features Amazon Genius Link".** Retired by Kain at S231, and the theme never had Genius Link wiring. The document contradicts the decision.
2. **DSRD 7 section 4.3 says the phone tier is 32px** and describes `--sp-2xl` as having "a standard mobile reduction". The token is 48px in `:root` and is never redefined at any breakpoint, so that claim is untrue of the theme as built. Only the policy family carries hand-written phone overrides. Reported at S228, still open.
3. **DSRD 2 section 2.24's register still says "Peer-Peer Applied Learning Sessions".** The site says Peer-to-Peer as of today, on Kain's instruction.
4. **Any card claiming the help articles have Rank Math scores.** They did not until today, and 153 still do not.
5. **Uncertain, flagged rather than smoothed:** I do not know what the board claims about the Knowledge Hub's readiness. Everything in section 1 marked "built" for the Hub is built as a template with no content behind it, and a card reading "Knowledge Hub listings built" would be true and misleading at the same time.

## 5. My view of what stands between here and the Phase A publishes

Shortest honest list, in the order the dependencies actually run:

1. **The keyphrase rule needs re-ruling**, then the score run finishes in about a quarter of an hour. Everything else in the help section queues behind it: the link ceiling check, the date line, and the missing article all touch the same 249.
2. **The seven policy pages need their DSRD 6 records.** Structure and copy pass now; the chapters needing instruments I have not run on them (accessibility walk, speed, schema) are what stand between "passes the gate" and "done".
3. **The people pages are the real body of page work**: eleven pages with no hairlines at any boundary, the same shape of work repeated. Nothing blocks it but sequence.
4. **The canonical tag is missing site-wide.** Ruled Rank Math configuration rather than page work, but it is a fail on all 23 built pages and nothing has yet done it.
5. **A dependency you may not see from your side:** the Book Note workstream cannot start on my side at all until the field group and importer exist, and neither is built. The master file being finished does not shorten that; it just means I can build against a real contract. Same for the Author Hub, which has no template and 404s today.

*No em or en dashes in this file; checked before writing.*
