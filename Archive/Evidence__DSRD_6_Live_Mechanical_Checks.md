# DSRD 6 — live mechanical evidence for the reconciliation card

From: Claude Code · 2026-07-23 · theme v0.36.8 (live). Kain asked me to run
the checks I can do from here (live site + theme source) and hand you the
evidence, so we split the gate instead of duplicating it.

**Scope:** the 44 built pages that actually exist — About, 10 instructor
profiles, Our People, the policies index + 7 policies, the /help/ archive, 15
FAQ category pages, 5 sampled FAQ articles (the 200 share one template), and
the 1 test article. Method: raw-HTML fetch per page (not a rendered view —
that's what actually proves schema/meta) + HEAD-check on every referenced
image. Full per-page data: `dsrd6-mechanical.csv` alongside this note.

---

## Who owns which chapter

| DSRD 6 chapter | Verifiable from here (Code) | Needs a Google tool | Your editorial call (Chat) |
|---|---|---|---|
| §1 Copy | — | — | ✅ all of it |
| §2 Structure & headings | H1 count, level order | — | sections match DSRD 9, headings "read true" |
| §3 Metadata | ✅ presence + length + og + canonical* | link-preview checker | "reads like a person wrote it" |
| §4 Schema | ✅ which @types each page emits | Rich Results Test (errors) | — |
| §5 SEO | address, indexing*, breadcrumb, title/H1 uniqueness | — | "one clear question", intent uniqueness |
| §6 GEO | author byline+link, date, answer-in-open, source links | Lighthouse agent-readiness | credential quality |
| §7 Accessibility | alt presence, contrast (DSRD 7 pairs), semantics | Lighthouse / keyboard walk | — |
| §8 Ease of use | — | — | ✅ fresh-eyes heuristic walk |
| §9 Speed | image dimensions/weight | PageSpeed Insights | — |
| §10 Visual consistency | value-vs-DSRD-7 token audit (CSS) | — | "name it / collapse it" verdicts |
| §11 Live verification | ✅ everything loads, links resolve, image metadata | — | Kain's 3-width approval |

\* §3.3 canonical and §5.3 indexing — see the staging caveat below; they
can't be truly verified on the test site.

---

## What PASSES cleanly (all 44 pages)

- **Every page returns HTTP 200**, and **carries exactly one `<h1>`** (§2 mechanics).
- **Schema present and correct to type (§4):** AboutPage on `/about/`,
  Person on all 10 instructor profiles, WebPage on the 7 policies, AboutPage
  on `/about/code-of-ethics/` + `/about/manifesto/`, CollectionPage on `/help/`
  and all 15 category pages, FAQPage on FAQ singles, Article on the article.
  (Rich Results Test for *errors* is the remaining tool step — I can only
  confirm the types are emitted, not that Google parses them clean.)
- **`/about/` AboutPage is now live** (v0.36.8, `@id …/about/#aboutpage`) —
  the schema I shipped today, verified in the raw HTML.
- **og:image present on every page** (§3.4). No defaults, none missing.
- **Every image loads (§11.1):** all 30 unique images across these pages
  return 200 — this is the check that once passed as "pixel-perfect" while
  images silently 404'd, so it's the one I ran hardest. Zero failures.

---

## Genuine flags to fold into the reconciliation

1. **FAQ category meta descriptions run long (§3.2).** All 15 category pages
   sit at **165–180 chars**, over the ~155 the standard wants — search will
   truncate them. This is template-level (the category description source),
   so it's one fix for all 15, not 15 fixes. Full lengths in the CSV.

2. ~~Two alt-text gaps~~ **— WITHDRAWN, false positive (corrected 2026-07-23).**
   On re-verification these are **not** real gaps: my checker counted the
   literal text `<img>` inside an HTML *comment* in `template-policy.php`
   ("Pages travel as JSON, created as `<img>` on first open…"). With comments
   stripped, `/about/code-of-ethics/` and `/about/manifesto/` have **zero**
   images missing alt (11 and 12 real `<img>` tags, all with alt). Nothing to
   fix. The `imgs_no_alt` figures in the CSV for those two rows are the same
   comment artifact — disregard them. (This is unrelated to the handover's
   separate alt-gap note about single-article placeholder zones / author /
   FAQ-reader photos, which I have not checked this session.)

3. **`/policies/` index emits no schema (§4). — FIXED, v0.36.9.** Same root
   cause `/about/` had; the theme now owns a `CollectionPage` node on
   `template-policies-index.php` (see `Ship_Brief__v0.36.9…`). Verify on the
   live page once the zip is uploaded.

4. **A few titles over ~60 (§3.1), soft.** The test article is 74 (it's a
   TEST item); a cluster of instructor and FAQ-category titles sit 61–67.
   Marginal, listed in the CSV — worth a trim where easy.

---

## Important caveat — the staging site masks two checks

**Every one of the 44 pages returns `noindex, nofollow` and no canonical.**
That is almost certainly the WordPress "discourage search engines" setting on
the test site (it's site-wide and byte-identical on all 44, and Rank Math
suppresses canonicals under noindex). It is correct for a staging site — but
it means **§3.3 (canonical) and §5.3 (indexing set on purpose) cannot be
verified here.** Don't read 44 "missing canonical / noindex" as page defects;
they need re-checking on production, or with the discourage setting briefly
off. Flagging so the gate records the true constraint, not a false fail.

---

## Still needs a dedicated run (not doable from here, don't fake it)

- **§4** Rich Results Test (Google) — parse-clean confirmation.
- **§9** PageSpeed Insights (Google), phone result, against DSRD 3 targets.
- **§6.5 / §7** Lighthouse agent-readiness + full WCAG 2.2 AA (keyboard walk,
  contrast at render, 200% zoom).
- **§8** the fresh-eyes UX heuristic walk — explicitly *not* the builder, so
  it's yours or a later session.
- **§11.3** tracking-fires — blocked: GA4/GTM isn't installed yet, so no page
  can be certified on this line until that board task lands.

Nothing here is a decision for you — it's evidence. After correction, the
scorecard is: **#2 withdrawn** (false positive), **#3 fixed** (v0.36.9), and
**two open** — the FAQ category descriptions (#1) and the long titles (#4),
both Kain's to rule on as fixes.
