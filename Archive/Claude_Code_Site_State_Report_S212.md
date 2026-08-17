# CLAUDE CODE — SITE-STATE & WORKFLOW REPORT

**In answer to:** Information Request — Claude Code Site-State & Workflow Report, Session 212
**From:** Claude Code (the Achology.com theme developer)
**Date of report:** 22 July 2026

**Current theme version:** 0.35.0 (`style.css`, `Version: 0.35.0`)
**Current commit:** `9b31c72` — "About page v0.35.0 — the Achology Story as a timeline window, reworked close"
**Working tree at time of writing:** not clean. `functions.php` modified; `about.css`, `about.js`, `page-about.php` untracked. These are this session's About-template work, built after v0.35.0 and not yet committed. They are described in Part F.

**On the baseline:** DSRD 10's baseline is the Site State Report of 2026-07-15 at v0.24.1. I do not hold that report. I therefore cannot reliably say "unchanged since v0.24.1" for any given item, because I cannot see what it recorded. Where I would have to guess at that, I have described the item instead and flagged it. That is a limitation of this report and you should read it as one.

**Two things I could not do, stated up front:**

1. **I have no access to the build site.** I cannot reach achologytest.com, and I have no WordPress database, no page list, and no way to see what actually renders there. Part A3 is therefore the weakest section in this report and I have said so in place of filling it in.
2. **I do not hold DSRD 1–5 or 7–10.** I hold DSRD 6 only, as a file in the theme repo. Everywhere a "built against" answer would require one of the others, I have reported the citation the code itself carries and nothing more. See Part E.

Nothing was built, fixed, refactored or changed in producing this report. No DSRD or specification document was written.

---

## PART A1 — Components

**My definition, since you asked for it rather than for DSRD 8's:**

> A component is a named visual block with its own CSS, which is either used by more than one template or was written to be. I identify them by the name the *code* uses — the CSS section title or the BEM block prefix — not by any grouping in a specification.

That definition has one consequence worth naming before the table: **it counts things that are built but not used.** A large block of finished CSS with no PHP calling it is still a component by this definition, and there is a lot of that in `cards.css`. If your DSRD 8 grouping only counts what renders, our lists will differ there, and that difference is real rather than a naming quibble.

**Where the CSS sections come from.** Only four stylesheets use numbered sections at all: `base.css` (12), `policies.css` (12), `components.css` (3) and `people.css` (3). `cards.css`, `header.css`, `footer.css`, `help.css`, `knowledge-hub.css` and `about.css` use named block headers with no numbers — `header.css` and `footer.css` cite a DSRD §18.x / §19.x on each block, `knowledge-hub.css` cites §20/§21/§22. `about.css`'s docblock declares seven numbered sections that **do not exist in the file body** — I wrote that docblock this session and the numbering is drift I introduced.

| Component (the name the code uses) | File path(s) | Built against (verbatim from the code) | Used by | Complete? |
|---|---|---|---|---|
| **Breadcrumb** — `.breadcrumb`, `__item/__link/__home/__separator/__current` | `components.css` §2; icon class in `base.css` §6 | No DSRD § in the CSS. Templates cite "DSRD 1 §9 (breadcrumb)" | 10 templates: `404.php`, `template-policies-index.php`, `taxonomy-faq_category.php`, `learn-listing.php`, `taxonomy-kh_category.php`, `single-article.php`, `template-policy.php`, `single-faq_article.php`, `archive-faq_article.php`, `page-about.php` | Finished |
| **School accent overrides** — `.school--nlp` … `.school--pgd` | `components.css` §1 | *"Applied at: card level or page-section level — never globally"* | `single-article.php` only, and only via placeholder data | Finished as CSS; barely consumed |
| **Bubble watermark motif** | `components.css` §3 | *"the Achology bubble mark as a page watermark (Kain, 2026-07-02/03)"*; cited by `404.php` as "DSRD 7 §14.1" | Every `.policy-page`, `.help-page` and people page | Finished — pure CSS, no markup needed |
| **Question door** — `.help-q`, `__text/__title/__excerpt/__arrow`, `.help-q-list` | `help.css` | *"THE QUESTION DOOR (Kain, 2026-07-16) — one component, three homes"* | 8 files, including `page-about.php`. **The comment says three homes; it is now in eight.** Stale comment, not stale code | Finished |
| **Popular block** — `.help-popular`, `__head/__badge/__glyph/__heading` | `help.css`; 404-only override in `policies.css` §12 | Named block header, no DSRD § | `404.php`, `archive-faq_article.php`, `single-faq_article.php`, `page-about.php`, `manifesto.php`, `code-of-ethics.php` | Finished |
| **"Where next?" / pair panel** — `.policy-next`, `--pair`, `--bubble`, `--no-mark`, `__row/__icon/__text/__name/__desc/__arrow` | `policies.css` §9; renderer `help-parts.php` | *"the manifesto page's component, adopted as the /help/ close by Kain, 2026-07-16"*; *"Content by category type (DSRD 1 §8)"* | `404.php`, `template-policy.php`, `page-about.php`, `help-parts.php` → the two `/help/` templates, `manifesto.php`, `code-of-ethics.php` | Finished |
| **Author signature card** — `.author-card` | `people.css` §3; renderer `people-setup.php` | *"The signature card follows DSRD 9 §22.7 exactly"* / "DSRD 2 §1.5 item 5" | `single-article.php` only today; `people-setup.php` says *"and (later) every Knowledge Hub article's byline"* | Finished |
| **Knowledge Hub cards** — `.card`, `--article/--book-note/--quote/--workbook`, `--clickable`, three-zone `__banner/__body/__footer` | `cards.css`; renderer `knowledge-hub-parts.php` | *"card markup mirrored from the render-verified card-library brochure (DSRD 8 §6)"*; *"cards.css and this markup are a matched pair"* | `taxonomy-kh_category.php`, `learn-listing.php` | **Partial** — four `--placeholder` variants ship as the real fallback; `cards.css` labels one *"Prototype placeholder — replaced in production"* |
| **Featured cards** — `.card--featured-*` (4) | `cards.css`; renderer `knowledge-hub-parts.php` | *"§6.5 / §6.8 / §6.6 / §6.7 (§6.8 confirmed over §20.6's older reference — Kain, 2026-07-13)"* | `taxonomy-kh_category.php` | Partial — same placeholder-image caveat |
| **Compact / mini card** — `.card--mini`, `.card__thumbnail--*` | `cards.css` | DSRD 8 §6.8 cited in `single-article.php` | `single-article.php` only | Partial — its four rendered instances are prototype examples |
| **Product cards** — `.card-product`, `.card--course`, school bundle, AAA Pass, membership monthly + annual | `cards.css`, ~1,100 lines | Named blocks; DSRD 8 §7 cited in `single-article.php` | **Only `.card--course` is used anywhere,** and only by a placeholder. The bundle card, AAA Pass card and both membership cards have **no PHP consumer in the theme at all** | **CSS finished, unconsumed.** The largest block of shipped-but-unwired code in the theme |
| **Section header** — `.kh-section`, `__header/__titles/__title/__subtext` | `knowledge-hub.css`; renderer `knowledge-hub-parts.php` | *"Section header (§20.7 pattern)"* | `taxonomy-kh_category.php`, `single-article.php` | Finished |
| **Category pills / tag strip / pagination** | `knowledge-hub.css`; `base.css` §12; renderers in `knowledge-hub-parts.php` | §20.5, §20.8, §21.9 D3 | `taxonomy-kh_category.php`, `learn-listing.php` | Finished; tag strip conditional on curated lists being filled |
| **Aristotle watermark** — `.policy-aristotle`, `--tall` | `policies.css` §11 | *"the SOMAP ethics block on the quiet about-pages (Kain, 2026-07-16; artwork replaced and LOCKED 2026-07-19)"* | `manifesto.php`, `code-of-ethics.php` | Finished |
| **Document figure + lightbox** — `.policy-doc*`, driven by `$ach_policy_doc` | `policies.css` §10; `template-policy.php` | *"§10, policies.css. First use: the manifesto document on /about/manifesto/"* | `template-policy.php`, configured by `manifesto.php` and `code-of-ethics.php` | Finished |
| **Button system** — `.btn`, `-primary`, `-secondary`, `--school` | `base.css` §5 | `help.css` header: *"Buttons come from base.css (.btn system) — no button CSS here"* | Site-wide | Finished |
| **Card grid** — `.card-grid` | `base.css` §7 | 1/2/3 columns, 24px gap | `learn-listing.php`, `taxonomy-kh_category.php` | Finished |
| **Containers** — `.page-container`, `.article-container` | `base.css` §4 | Tokens `--container-page: 1200px`, `--container-article: 880px` | `.page-container` in 12 templates; `.article-container` in 6 | Finished |

**Components built this week for the About page** are listed separately in Part F3, because they belong to that build description. In short: nine new blocks (`.pfq*`, `.tw*`, `.cons*`, `.fa*`/`.fam*`/`.m-*`, `.st-*`, `.odo-*`, `.story-proof*`, `.about-proof*`/`.proof-card*`/`.about-video-lightbox*`, `.about-grid*`), all currently used by one page.

---

## PART A2 — Templates

There are **23 `.php` files in the theme root.** Nine are true WordPress templates; the rest are includes `require`d from `functions.php`, the two chrome files, and `functions.php` itself. All 23 are listed, with non-templates marked, because the request asked for every PHP template file and I would rather over-report than choose for you.

**The enqueue baseline.** These load on **every page, unconditionally**, in cascade order: Google Fonts → `fonts.css` → `base.css` → `components.css` → `cards.css` → `style.css` → `header.css` → `footer.css` → `policies.css` → `help.css` → `people.css`; scripts `header.js`, `footer.js`. Below, "baseline" means that stack and I name only additions.

**Only four enqueues in the whole theme are conditional:**

| Asset | Condition, verbatim | Line |
|---|---|---|
| `knowledge-hub.css` | `is_singular( array( 'article', 'book_note', 'quote', 'workbook' ) ) \|\| is_tax( 'kh_category' ) \|\| get_query_var( 'ach_listing' )` | functions.php:171 |
| `about.css` | `is_page( 'about' )` | functions.php:177 |
| `help-article.js` | `is_singular( 'faq_article' )` | functions.php:189 |
| `about.js` | `is_page( 'about' )` | functions.php:195 |

### Root PHP files

| File | What it serves | Built against (verbatim) | Scoped CSS/JS | Complete? |
|---|---|---|---|---|
| `404.php` | Any URL matching nothing | *"Reframed as a wayfinding page, not an error page (Kain, 2026-07-19)"*; *"the same three-bubble watermark motif (components.css §3 … DSRD 7 §14.1)"*; *"Icons: Lucide House / Compass / GraduationCap / BookOpen / LibraryBig / Tag (DSRD 7 §5.2, '404 page' block), stroke 1.75"* | Baseline; styled by `policies.css` §12 + `help.css`. No own CSS | **Finished**, but its four "Popular Questions" are hardcoded links, not a query — see Part B3 |
| `archive-faq_article.php` | `/help/` — the `faq_article` archive, registered `'has_archive' => 'help'` | *"Spec: DSRD 1 §2.5 + §8, DSRD 2 §2.24. Design approved by Kain 2026-07-02 (help-landing preview v6)"* | Baseline | **Finished.** Popular articles are explicitly a live query: *"no content baked into the template (Kain, 2026-07-03)"* |
| `faq-setup.php` | **Not a template** — registers `faq_article`, `faq_category`, `/help/{category}/{article}/` | *"spec: DSRD 1 §2.5 + §8"*; slugs *"verified against DSRD 1 §11 (redirect map)"*; *"Kain explicitly chose seeding over hand-typing the 15 terms (2026-07-02, 'option two')"* | n/a | Finished — 21 functions |
| `faq-icons.php` | **Not a template** — one Lucide icon per FAQ category | *"the /help/ section's icon set (DSRD 7 §5.2)"*; *"Path data embedded verbatim from the official lucide-static package — never hand-drawn (registry rule)"*; *"This file is generated — update the registry in DSRD 7 §5.2 first, then regenerate rather than hand-editing paths"* | n/a | Finished — all 15 slugs + a documented Info fallback |
| `footer.php` | Every page | *"the site-wide footer (DSRD 8 §19, Session 26 LOCKED)"* | `footer.css`, `footer.js` | Finished |
| `functions.php` | **Not a template** — theme bootstrap | Its opening line — *"its only job is to tell WordPress which stylesheets and fonts to load"* — is **stale**; the file also holds theme supports, `achology_policy_index_rows()` and six `require`s | n/a | Finished; header comment has drifted |
| `header.php` | Every page | *"Spec: DSRD 8 §18 (Site-Wide Header). Navigation URLs: DSRD 1 §13.1. Stage 1 = the header bar + mobile menu. The mega-menu dropdowns … are Stage 2."* | `header.css`, `header.js` | **Docblock says partial, code says finished.** Three mega-menu panels exist (`#megamenu-academy`, `#megamenu-courses`, `#megamenu-learn`) and `header.css` styles them. `README.md` calls it complete. Flagged, not resolved — not verified in a browser |
| `help-parts.php` | **Not a template** — renders the closing pair panel | *"adopted as the /help/ close by Kain, 2026-07-16"*; *"Content by category type (DSRD 1 §8)"*; *"Icons: registered Lucide slots (DSRD 7 §5.2)"* | n/a | Finished |
| `index.php` | WP fallback for anything with no specific template | *"a temporary proof page until the real layouts are built"* — no DSRD cited | Baseline; two inline `style` attributes | **Placeholder, explicitly.** Body is `<h1>The Achology design system is live</h1>` and a button linked to `#`. `404.php` names it as a known dead end |
| `knowledge-hub-parts.php` | **Not a template** — shared copy + card renderers for `/learn/` | *"Everything below is locked spec, transcribed verbatim in-session: §20.9 hero intros (7) · §20.10 section subtexts (28) · DSRD 2 §4.3 cross-category intros (4) · DSRD 7 §17.1 count labels · DSRD 7 §5.2 icons · card markup mirrored from … (DSRD 8 §6)"* | n/a | **Partial by design** — the curated tag lists render only once you fill them |
| `knowledge-hub-setup.php` | **Not a template** — registers 4 post types, 2 taxonomies, 32 listing rewrites | *"spec: DSRD 10 §9–§13"*; *"Modelled on faq-setup.php"* | n/a | Finished, incl. a deliberate 404-suppressor for empty listings |
| `learn-listing.php` | 32 URLs — 28 `/learn/{category}/{type}/` + 4 `/learn/{type}/`. Routed by `template_include`, not the WP hierarchy | *"Spec: DSRD 9 §21 (LOCKED), read line-by-line in-session 2026-07-13"* | Baseline **+ `knowledge-hub.css`** | Finished, with a designed empty state |
| `page-about.php` | `/about/` — by page slug | *"Copy and layout locked with Kain 2026-07-22, from previews/about.html."* **No DSRD section cited.** The only docblock in the theme that cites `previews/` | Baseline **+ `about.css` + `about.js`** | **Finished**, and the worst file in the theme for hardcoded values — see Part B1 |
| `people-setup.php` | **Not a template** — the people registry + `achology_author_card()` | *"DSRD 2 §2.14, accounts decision 2026-07-03"*; *"the article author signature block, DSRD 2 §1.5 item 5 / DSRD 9 §22.7"* | n/a | Finished — 11 people, all 11 photos present |
| `rank-math-feed.php` | **Not a template** — admin-only analyser feed | *"Nothing here runs on the public site"* — no DSRD cited | n/a | Finished |
| `single-article.php` | `/learn/{category}/articles/{slug}/` — the `article` post type | *"Spec: DSRD 9 §22 (LOCKED) + DSRD 10 §13 + §17 (Article schema). Converted from the locked prototype 'Article Page Template V2'"* | Baseline **+ `knowledge-hub.css`** | **Partial — three declared placeholder zones**, plus §17 speakable markup not yet implemented. See Part B3 |
| `single-faq_article.php` | `/help/{category}/{article}/` | *"Spec: DSRD 2 §2.24 + DSRD 1 §9. Design approved and locked by Kain 2026-07-02 (help-article preview, round 4)"*; *"Schema: FAQPage + BreadcrumbList"* | Baseline **+ `help-article.js`** | Finished. Audio is feature-detected from the uploads directory, not hardcoded |
| `taxonomy-faq_category.php` | `/help/{category}/` — 15 terms | *"Spec: DSRD 2 §2.24 + DSRD 1 §8 + §9. Design approved by Kain 2026-07-02 (round 7), updated 2026-07-16"* | Baseline | Finished |
| `taxonomy-kh_category.php` | `/learn/{category}/` — 7 terms | *"Spec: DSRD 9 §20 (LOCKED), read line-by-line in-session 2026-07-13"*; *"§6.8 confirmed over §20.6's older reference — Kain, 2026-07-13"* | Baseline **+ `knowledge-hub.css`** | Finished, with a designed empty state |
| `template-author-profile.php` | `/about/instructors/{slug}/`. `Template Name: Author Profile` | *"Design locked by Kain 2026-07-03 (author-profile preview, r10)"*; *"Spec: AUTHOR_PROFILE_PAGE_SPEC.md + DSRD 2 §2.14"*; *"Schema: Person + BreadcrumbList"* | Baseline | Finished, with an explicit empty state |
| `template-our-people.php` | `/about/instructors/`. `Template Name: Our People` | *"The hub page at /about/instructors/ (DSRD 2 §2.14)"*; *"Kain's call, 2026-07-03"* | Baseline | Finished |
| `template-policies-index.php` | `/policies/`. `Template Name: Policies Index` | *"Styles: policies.css (.policy-index)"* — no DSRD § in this file | Baseline | Finished. List built dynamically from child pages — *"No hardcoded links to maintain"* |
| `template-policy.php` | The 7 legal pages + the quiet `/about/` pages. `Template Name: Policy Page` | Documents its own four override variables; cites *"§10, policies.css"* for the document lightbox | Baseline | Finished — the override system is fully documented and exercised |

**Note on "built against".** Where a cell names a DSRD section, that is **the citation the code carries**, transcribed. I hold none of those documents and have verified none of those claims. See Part E2.

### PHP files in subdirectories

All ten are in `policies-content/`. There are no PHP files anywhere else below the root.

| File | Lines | What it is |
|---|---|---|
| `accessibility-statement.php` | 56 | Baked wording for `/policies/accessibility-statement/` |
| `code-of-ethics.php` | 200 | Baked wording for `/about/code-of-ethics/`; adopted-date meta line, closes on "Where next?", carries the Code of Character lightbox |
| `cookie-policy.php` | 90 | Baked wording; two cookie tables |
| `disclaimers.php` | 150 | Baked wording; framework table |
| `manifesto.php` | 150 | Baked wording for `/about/manifesto/`; *"edited in the Amelia Sinclair editorial voice (REF 2 §2.4 + §1 shared DNA, Kain 2026-07-15)"* |
| `policies.php` | 22 | **Analyser-feed only, never rendered to visitors.** A knowingly hand-maintained duplicate of the index page's intro and default descriptions: *"they must stay in step"* |
| `privacy-policy.php` | 230 | Baked wording; lawful-basis table |
| `refund-policy.php` | 108 | Baked wording |
| `terms-and-conditions.php` | 209 | Baked wording |
| `trust-statement.php` | 138 | Baked wording |

**Not present, and worth naming as absences:** there is no `front-page.php`, no `page.php`, no `single.php`, no `archive.php` and **no `search.php`**. `README.md` lists "Main page templates" as "Next phase". The missing search template is the reason the 404 page deliberately carries no search box.

---

## PART A3 — Pages

**I cannot answer this section as asked, and I would rather say so than fill it in.**

The request asks for every page that currently renders on the build site, with its content status and whether you have confirmed it rendering. I have no access to achologytest.com, no WordPress database, and no page list. The theme does not create pages — you do — so the repository holds no record of which pages exist. Anything I wrote in the "URL / Content / Verified?" columns would be inference dressed as fact.

What I can give you instead is the evidence that does exist, in three lists. **None of these is a page list.**

### A3-i. URLs the theme links to

Every internal URL referenced from `header.php`, `footer.php` and `page-about.php`. If one of these pages does not exist on the build site, that link is currently broken and I would not know.

**From the site header:** `/academy/`, `/academy/schools/`, `/academy/cognitive-behavioural-psychology/`, `/academy/life-coaching/`, `/academy/mental-health/`, `/academy/mindfulness/`, `/academy/neuro-linguistic-programming/`, `/academy/person-centred-counselling/`, `/academy/personal-growth/`, `/courses/`, `/certification/`, `/accreditation/`, `/access-all-areas/`, `/membership/`, `/pricing/`, `/testimonials/`, `/learn/`, `/learn/articles/`, `/learn/book-notes/`, `/learn/quotes/`, `/learn/workbooks/`, `/help/`

**Added by the site footer:** `/about/`, `/about/instructors/`, `/about/manifesto/`, `/about/code-of-ethics/`, `/policies/`, `/policies/privacy-policy/`, `/policies/terms-and-conditions/`, `/policies/cookie-policy/`, `/policies/refund-policy/`, `/policies/trust-statement/`, `/policies/disclaimers/`, `/policies/accessibility-statement/`, `/free-events/`, `/free-coaching/`

**Added by the new About page:** `/about/founders-letter/`, `/about/instructors/kain-ramsay/`, `/about/instructors/gerard-egan/`, `/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/`, and eight `/help/…` article URLs listed in Part F2.

Two I would flag for checking, because I introduced or inherited them this week and cannot confirm either exists: **`/about/founders-letter/`** (linked twice from the About page) and the two **`/about/instructors/{name}/`** profile URLs.

### A3-ii. Pages the theme is built to serve

Derived from the templates, not from the site. This is what *would* render if the page existed. The full template mapping is in Part A2.

### A3-iii. What the handover record says has been verified in a browser

From the memory note carried into this session, and therefore your record rather than mine:

| Page | Recorded status |
|---|---|
| All legal / policy pages | Scoring 80+ on Rank Math; the Policies front-door page exempt |
| The 404 page | Built, verified and locked |
| The About page | Design verified at desktop 1440, tablet 768 and phone 390 — **as a preview.** As a template it is verified only against that preview, by me, this session. You have not yet seen it render on the build site, because it has not shipped. |

Everything else: **unknown to me.**

---

## PART B — What was actually used

### B1. Design tokens and class names

**Where the tokens live.** One `:root` block in the entire theme, `base.css:15–107`. No other stylesheet declares `:root`. It defines **50 custom properties**: 2 font families, 12 brand colours, 14 school colours, 1 accent convenience, 7 spacing steps, 3 container widths, 3 radii, 5 shadows, 1 grid gap, 2 gradients. (A raw grep returns 53 — three of those are the same names restated inside a documentation comment.)

Two further custom properties are set outside `:root` and templates depend on them: `--school-accent-rgb`, set per school in `components.css` as raw RGB triples duplicating the school hexes, because `rgba()` needs them and no alpha helper exists; and `--era` / `--fill` / `--odo-c`, set **inline in `page-about.php`** and consumed by `about.css`.

**The proportion, by count.** Token references versus literals, per file:

| CSS file | `var(--color` | `var(--sp` | `var(--font` | hex (raw) | literal px in padding/margin/gap | literal font-size px | rgb/rgba literals |
|---|---:|---:|---:|---:|---:|---:|---:|
| `base.css` | 41 | 6 | 15 | 30 | 12 | 17 | 12 |
| `components.css` | 6 | 0 | 2 | 7 | 2 | 2 | 0 |
| `cards.css` | 110 | 27 | 57 | 11 | **107** | **64** | 28 |
| `header.css` | 36 | **0** | 13 | 7 | 30 | 13 | 16 |
| `footer.css` | 10 | **0** | 8 | 2 | **36** | 8 | 17 |
| `policies.css` | 67 | 65 | 16 | 1 | 7 | 20 | 9 |
| `help.css` | 61 | 53 | 23 | 0 | 9 | 28 | 9 |
| `people.css` | 31 | 5 | 12 | 0 | 23 | 15 | 0 |
| `knowledge-hub.css` | 48 | 33 | 25 | 0 | 29 | 36 | 6 |
| `about.css` | 64 | 117 | 12 | 24 | 28 | **45** | 32 |
| `fonts.css` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `style.css` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Read plainly, that says three different things:

1. **Colour is almost entirely tokenised.** 474 `var(--color…)` references against roughly 35 genuine live hex literals — about **93%**. The real colour gap is not hex, it is **rgba: 129 literals**, nearly all `rgba(53,65,73,…)` (brand dark) or `rgba(255,255,255,…)`, written out longhand because the token system has no alpha helper.
2. **Spacing is split hard by file.** `about.css` (117), `policies.css` (65), `help.css` (53) and `knowledge-hub.css` (33) lean on `--sp-*` heavily. **`header.css` and `footer.css` use it zero times** — every padding, margin and gap in the site chrome is a literal px. `cards.css` uses it 27 times against 107 literals.
3. **Type size is not tokenised at all.** There is **no `--font-size-*` scale**; `--font-heading` and `--font-body` are family names only. All **248** `font-size` declarations in the theme are literal px. That is a system-level gap, not a per-file lapse.

**Worst offenders, in order:** `cards.css` (107 literal spacing values, 64 literal font sizes — the highest absolute counts in the theme); `about.css` (45 literal font sizes, 24 hex, 32 rgba — the newest file and the least colour-disciplined); `footer.css` (36 literal spacing values, zero `--sp-*`); `header.css` (30 literal spacing values, zero `--sp-*`).

**Literal values that duplicate a defined token** — the real drift, as opposed to deliberate one-offs:

| Value | Duplicates | Where |
|---|---|---|
| `#354149` | `--color-dark` | `base.css` (×2, inside gradient tokens), `about.css:66`, `about.css:100` |
| `#ED6922` | `--color-orange` | `base.css` (inside a gradient), `about.css:172`, `about.css:343` |
| `#5E6B75` | `--color-soft-grey` | `base.css:105` |
| `#8A9199` | `--color-mid-grey` | `about.css:67` |
| `#D85A1B` | `--color-orange-hover` (case differs) | `about.css:172`, `about.css:343` |
| `#fff` / `#ffffff` | `--color-white` | `about.css` ×6 |
| `rgba(53,65,73,…)` | RGB of `--color-dark` | `base.css` (5 shadow tokens), `header.css`, plus `cards.css`, `policies.css`, `help.css`, `knowledge-hub.css` |
| `rgba(237,105,34,…)` | RGB of `--color-orange` | `base.css`, `knowledge-hub.css` ×2 |
| 7 school RGB triples | The 7 `--school-*-primary` | `header.css:257–263` and `components.css:17–23` |

**Genuine one-offs with no matching token.** `cards.css` carries six, and annotates five of them itself — `#B0B8BE` (*"deliberate: light grey author text, no system token — candidate for --color-light-grey"*), `#5a6d78`, `#F4943E`, `#EFAD60`, `#faf6f1`, each marked *"deliberate: gradient tint, no system token"*. The one it does **not** annotate is `#6b7078` at `cards.css:303`. `about.css` carries `#3E4E5A` and `#F5A05C`, neither annotated.

**Literals inside PHP `style=""` attributes.** Only three PHP files contain any `style=` attribute. `footer.php` has 7 and they are **fully tokenised** (`background:var(--school-*-primary)` on the rainbow stripe). `index.php` has 2, layout only, on the placeholder page. **`page-about.php` has 28, all carrying literal hex:**

| Value | Occurrences | Matches a token? |
|---|---|---|
| `#354149` | 6 | Yes — `--color-dark` |
| `#ED6922` | 8 | Yes — `--color-orange` |
| `#8A9199` | 1 | Yes — `--color-mid-grey` |
| `#4d6672`, `#6b7680`, `#c05a1a`, `#e8eaeb`, `#eaeeef`, `#f0f1f2`, `#fce8d9`, `#fde8d5`, `#7a3606` | 13 between them | No — one-offs |

Plus further literal `stop-color` values inside the hand-authored SVG chart at `page-about.php:162–165`. That markup is minified onto two very long lines and I have **not** counted them exactly — recorded as unsure rather than guessed.

**Class names I invented that come from no spec.** Everything built for the About page this week, because `page-about.php` is the one template whose docblock cites no DSRD section at all: `.about-header__art`, the `.pfq*` family, `.tw*`, `.cons*`, `.fa*`/`.fam*`/`.m-*`, `.st-*`, `.odo-*`, `.story-proof*`, `.about-proof*`, `.proof-card*`, `.about-video-lightbox*`, and the `.about-grid*` family including the four icon tones (`ic-dark`, `ic-orange`, `ic-slate`, `ic-tint`) and the background flags (`has-bg`, `bg-accred`, `bg-schools`, `bg-hub`). Roughly 100 class names. They were named in the preview builder during design and carried into the theme unchanged.

### B2. Icons

**Every icon in the theme is raw inline SVG. Not one is a Lucide named icon.**

| Form | Count across all PHP |
|---|---:|
| `<i data-lucide="…">` | **0** |
| Raw inline `<svg>` | **178** |

There is no `data-lucide` attribute anywhere in the theme's PHP, JS or CSS. The Lucide library is **not enqueued** — no `wp_enqueue_script`, no CDN tag, no `lucide.createIcons()`. That is consistent rather than broken: with zero `data-lucide` attributes there is nothing to hydrate.

This is deliberate and documented. `faq-icons.php` states the rule: *"Path data embedded verbatim from the official lucide-static package — never hand-drawn (registry rule)."* So the icons **are** Lucide icons; they are inlined rather than named.

Raw `<svg>` count by file: `page-about.php` **60**, `header.php` 19, `404.php` 14, `manifesto.php` 13, `single-article.php` 11, `template-policy.php` 11, `code-of-ethics.php` 11, `footer.php` 9, `faq-icons.php` 7, `single-faq_article.php` 4, `template-author-profile.php` 3, `template-our-people.php` 3, `template-policies-index.php` 3, `archive-faq_article.php` 2, `learn-listing.php` 2, `taxonomy-faq_category.php` 2, `taxonomy-kh_category.php` 2, `help-parts.php` 1, `knowledge-hub-parts.php` 1.

Two of those counts understate the icons carried: `faq-icons.php` and `knowledge-hub-parts.php` store icons as inner path fragments in PHP arrays and wrap them in one `<svg>` shell at render — `faq-icons.php` alone holds 15 category icons.

**Is `stroke-width: 1.75` consistent?** Applied **per icon**, written into each SVG, with a single global default at `base.css:484` (`/* 6. Lucide icon defaults */`). No other CSS sets it.

| Value | Count |
|---|---:|
| `1.75` | **159** |
| `1.5` | 13 |
| `3` | 5 |
| `2.25` | 5 |
| `1.4` | 1 |
| `2` | 1 |

**Every non-1.75 value in the theme is in `page-about.php`.** All 18 other PHP files are 100% at 1.75. The exceptions split into two kinds:

- **A real inconsistency:** `2.25` ×5 at `page-about.php:61, 65, 69, 73, 77` — the five question-selector chevrons. The same ChevronRight glyph is 1.75 everywhere else in the theme.
- **Chart strokes, arguably out of scope:** `1.4`, `1.5` ×13, `2`, `3` ×5, all inside the hand-authored SVG timeline chart at `page-about.php:164–165`. These are route paths, gridlines and bubble outlines, not icons. I do not know whether the icon standard was ever meant to cover them, so I am flagging rather than judging.

### B3. Known gaps I am already aware of

#### ACF fields read with no Local JSON definition

There are **12 ACF calls in the theme**, all `get_field` — zero `the_field`, `have_rows` or `get_sub_field`. They read **7 distinct field names**: `author`, `source_reference`, `source_book_author`, `book_cover_image`, `quote_text`, `quote_author`, `source_book_reference`.

`acf-json/` holds **exactly two field groups**: `Article Fields` (`post_type == article`) defining `article_type`, `author`, `source_type`, `source_reference`, `source_video_id`; and `Quote Fields` (`post_type == quote`) defining `quote_text`, `quote_author`, `image_quote_text`, `source_book_reference`.

**Two fields are read but never defined anywhere:**

| Field | Read at | Read from |
|---|---|---|
| **`source_book_author`** | `single-article.php:255` | a `book_note` post |
| **`book_cover_image`** | `single-article.php:257`, `knowledge-hub-parts.php:241` | a `book_note` post |

**And one defined field is read outside its location rule:** `author` is defined only for `article`, but `achology_kh_author_name()` (`knowledge-hub-parts.php:208`) is called for **all four** Knowledge Hub card types. On a `book_note`, `quote` or `workbook` there is no field to fill, so it returns null and the fallback reads an empty meta key.

**The root cause, plainly: there is no `book_note` field group and no `workbook` field group at all.** Two of the four registered Knowledge Hub post types have zero Local JSON.

In fairness: every one of these calls is guarded by `function_exists( 'get_field' )` and falls back to `get_post_meta()` or an empty value, so nothing fatals — the fields come back empty and the placeholder branches render. And `knowledge-hub-setup.php:370` defines `achology_kh_author_field_choices()`, which hints the author choice list is built in PHP and the groups may be intended to be created in the ACF admin rather than committed as JSON. **The mismatch is fact; the intent behind it is not in the repository, and I am not going to guess at it.**

#### Placeholder or dummy data standing in for a real query

There is not a single `TODO`, `FIXME`, `XXX`, `dummy` or `lorem` anywhere in the theme. Every gap below is instead documented in prose, in its own comment — with one exception, which is the one that matters most.

| Where | What stands in | Acknowledged? |
|---|---|---|
| `single-article.php:206–240` | Four hardcoded "Related Further Reading" cards, all `href="#"` — two book notes, two articles | **Yes** — *"STAGING PLACEHOLDER … the locked prototype's four example cards render instead. The live query takes over automatically as content arrives."* It is the `else` branch of a real two-stage query |
| `single-article.php:259–264` | A hardcoded source book — *Insight: The Power of Self-Awareness in a Self-Deluded World*, Tasha Eurich, `url = '#'` | **Yes** — *"Placeholder: the locked prototype's example book"* |
| `single-article.php:310–329` | A hardcoded `$ach_courses` array of two courses **with invented statistics**: DiMAP (56,701 students, 51+ hrs, 4.78 rating, $299) and Mindset Mastery (4,523, 12+ hrs, 4.77, $149). Both CTAs point at `/courses/`, not the course | **Yes**, but note: **this one has no live-query branch at all.** It renders unconditionally |
| `404.php:97–134` | Four hardcoded Popular Questions with hardcoded `/help/…` URLs and hand-written excerpts | **No.** Nothing marks these as provisional. And this is the pattern `archive-faq_article.php` explicitly rejected: *"a LIVE query, no content baked into the template (Kain, 2026-07-03, superseding the earlier static-at-launch list: the rebuild retitles and re-slugs articles, so baked links would rot)."* The 404 page carries exactly what that decision ruled out |
| `index.php:13–17` | The whole page body — proof-of-concept copy and a button linked to `#` | **Yes** |
| `policies-content/accessibility-statement.php:37` | Live visitor-facing copy that is a forward promise: *"This section will list any parts of the site that do not yet meet WCAG 2.1 AA, once the post-rebuild accessibility assessment is complete."* | It says so, but it is published |

Not counted as gaps, because they are the *designed* no-image state: `--gradient-article-placeholder`, `--gradient-workbook-placeholder`, and the six `--placeholder` card variants.

#### Anything I would flag myself

| Item | Why |
|---|---|
| **`index.php`** | The clearest placeholder in the theme, and it is the destination of any search — which is why the 404 page has no search box. Missing alongside it: `front-page.php`, `page.php`, `single.php`, `archive.php`, `search.php` |
| **`style.css`** | 479 bytes — the ID card and a note that styles come later. It is nevertheless enqueued mid-cascade as the dependency link between `cards.css` and `header.css`, so it is a load-bearing empty file |
| **`single-article.php`** | Three placeholder zones, plus §17 speakable markup declared as not yet implemented |
| **`cards.css`** | ~1,100 lines — the school bundle card, AAA Pass card and both membership cards — with **no PHP consumer anywhere in the theme.** Finished and unwired. Whether that is debt or correct sequencing depends on a roadmap I cannot see |
| **`header.php` docblock** | Says mega-menus are "Stage 2"; three are built. Stale comment, unverified in a browser |
| **`functions.php` docblock** | Says its only job is enqueueing; it does considerably more |
| **`help.css`** | Question-door comment says *"three homes"*; it is now in eight files |
| **`about.css`** | Its docblock declares seven numbered sections the file body does not have. **I wrote that docblock this session** — the drift is mine, one day old |
| **`policies-content/policies.php`** | A knowingly hand-maintained duplicate of the index page's intro and descriptions, with nothing enforcing the match. Note the asymmetry: the *row data* was refactored into one shared builder called by both consumers, but the *intro and default descriptions* were left duplicated. Half the problem was solved |
| **`README.md`** | The status table is a phase behind. It lists "Main page templates — Next phase" and does not mention `404.php`, `page-about.php`, `about.css`, `about.js`, `single-article.php`, `learn-listing.php`, `taxonomy-kh_category.php`, `knowledge-hub-setup.php`, `knowledge-hub-parts.php`, `knowledge-hub.css` or `rank-math-feed.php` — all of which exist and ship |
| **`page-about.php`** | 28 inline `style` attributes carrying literal hex, 60 inline SVGs, five chevrons at a non-standard stroke weight, and a hand-authored minified SVG chart. It is the newest file in the theme and the least disciplined in it. That is mine, from this week |
| **The `/about/founders-letter/` link** | Linked twice from the new About page. I cannot confirm the page exists |

**Two things I could not settle from the code**, recorded as unsettled rather than answered: whether `header.php`'s mega-menus are genuinely finished (code and README say yes, the file's own docblock says no — it needs a browser check), and whether the missing `book_note` / `workbook` ACF groups are an oversight or a deliberate build-it-in-the-admin choice.

---

## PART C — How I actually work

Answered as it happens, not as it ought to.

### C1. What I receive when you give me a task

Most often: **a conversation in chat.** A written prompt at the start of the session setting the agenda, then a back-and-forth. Typically it carries a link or a path to a preview file, and it names the decision you want brought back.

Alongside that, two things arrive automatically at session open and I read them before anything else:

- **`CLAUDE.md`** at `/Users/kainramsay/Documents/CLAUDE | Anthropic Ai/CLAUDE.md` — your standing rules.
- **A memory note**, `achology-next-session-plan`, which carries the state of play from the previous session.

What I rarely receive is a written specification document. Spec sections reach me **as quotations inside your prompts, or as citations already written into the code by an earlier session** — "DSRD 5 §2.6", "DSRD 7 §5.2" — rather than as documents I can open. This session was typical: your opening prompt named DSRD 9 §23 and DSRD 7 §5.2 as write-ups to produce, and I had neither document in front of me.

Screenshots are occasional. Links to the live or build site, rare.

### C2. How a template comes into existence

**Precisely: I start from HTML and convert it. I do not write PHP directly into the theme as the first step.**

The mechanism is a Python file, `previews/_build_previews.py` — 3,330 lines. It is a generator, not a page. It holds the markup, CSS and JS for every prototype as Python string blocks, and writes complete, standalone HTML files into `previews/`. Those files carry the real theme chrome — the real header, the real footer, the theme CSS — inlined, with images baked in as base64 data URIs so a preview is one portable file that opens anywhere.

The sequence, as it actually ran for the About page:

1. Design is iterated **inside the builder**, in Python string blocks. Each run regenerates `previews/about.html`.
2. You open the preview in Safari. We go round until you approve it. This is where the design work happens — nothing PHP exists yet.
3. Only once you have approved it does the CSS, JS and markup come out of the builder and into theme files.

For the About page that extraction was done by running the builder in-process and taking the exact objects it had used, rather than copying text by hand — so the shipped files could not drift from the approved preview. Then the baked-in base64 images were swapped back to theme file paths.

**The honest limit on this answer:** I directly observed this sequence for the About page, this week. `previews/` also contains prototypes for the policy pages, the policies index, the help section, the people pages, the knowledge hub and the 404 — which strongly suggests the same route was used for those. But I did not build them in a session I can see, so for those I am inferring from the artefacts, not reporting. Treat "HTML first, then convert" as **confirmed for About, strongly evidenced but not witnessed for the rest.**

### C3. What I do when a specification is missing or unclear

In practice, on a normal day, I do one of two things, and which one depends on whose decision it is:

- **If it is a technical matter** — file structure, enqueue conditions, how something is wired — I decide it myself, do it, and tell you what I decided and why. I do not ask. This is a standing instruction of yours, recorded in memory as "technical decisions are Claude's".
- **If it is a design or wording matter** — anything visible, anything about the brand — I stop and bring it to you as a single yes/no question with the evidence behind it, and I do not build the thing I am recommending until you have said yes.

The failure mode I actually have is the boundary between those two. Something that looks technical can turn out to be visible, and then I have made a design decision without meaning to. This session I removed an orphaned lightbox from the About markup on my own authority and told you afterwards. I judged it invisible dead code; it was, but it was still your page, and telling you after is weaker than asking first.

There is a third thing I do that is worth recording honestly: **where nothing tells me, I sometimes carry on and report at the end of the block of work rather than at the moment of the decision.** Part F item 7 lists everything I decided that way this session.

### C4. The deployment sequence

Exactly as it runs, from finished code to the build site.

| # | Step | Who | Detail |
|---|---|---|---|
| 1 | Edit theme files in place | Claude Code | Working directly in the theme folder, which *is* the git repository. No staging copy, no build step for PHP/CSS/JS. |
| 2 | Verify in a live browser | Claude Code | See C5. Nothing proceeds past here unverified. |
| 3 | Bump `Version:` in `style.css` | Claude Code | Every deployable change. This also cache-busts CSS and JS, because `wp_enqueue_*` passes the theme version as the asset version string. |
| 4 | `git add` + `git commit` | Claude Code | The commit message always carries the version number. Current head: `9b31c72 About page v0.35.0 — …` |
| 5 | `git push` | Claude Code | Remote: `https://github.com/kain-ramsay/achology-theme`. GitHub is the history and the backup. **GitHub does not deploy anything** — nothing on the build site is pulled from it. |
| 6 | Announce the push with its version number | Claude Code | Standing rule in `CLAUDE.md`. |
| 7 | Rebuild `../achology.zip` | Claude Code | The zip sits one level above the theme folder. Rebuilt after every push. Last rebuild recorded at 33MB. |
| 8 | Upload the zip | **Kain** | WordPress → Appearance → Themes → Add New → Upload → "Replace current with uploaded." I never do this and have no access to do it. |
| 9 | Create/edit any WordPress page | **Kain** | The theme never creates, edits or deletes pages. This is a standing rule, noted in `functions.php` and in `CLAUDE.md`. |

**The deploy target is `achologytest.com`, not `achology.com`.** Cutover to the live domain is by clone.

**One contradiction I must flag rather than resolve, because it is not mine to resolve:**

- `README.md` (theme repo) says the theme is zipped **excluding** `previews/`.
- `CLAUDE.md` (your standing rules) says rebuild `../achology.zip` **including** `previews/`, excluding `.git`.

These disagree. I have followed `CLAUDE.md` — previews included — which is why the zip is 33MB. Whichever is right, one of the two documents needs correcting, and I have changed neither.

### C5. What I check before I call something done

There is no automated test suite in this repo. No unit tests, no linting step, no CI. What there is:

1. **A live browser check, always.** Never a claim about a rendered page that I have not seen render. `CLAUDE.md` requires this and it is the check I lean on hardest.
2. **The whole page, never a component on a blank page.** Real header, real footer, real theme CSS.
3. **Verification by measurement.** In practice this means serving the page locally and reading geometry and computed styles out of the browser, rather than judging by eye from a screenshot.
4. **The states and breakpoints that matter** — this session, desktop 1440, tablet 768, phone 390.
5. **Rank Math SEO + GEO metadata** before the page is considered closed, to an 80+ score, never supplying a canonical URL.

**A weakness this report should record, because you found it this session.** My verification is stronger on measurement than on appearance. When I extracted the About page into theme files, I confirmed all 675 elements matched the approved preview in size, position, colour and font — and every image on the page was silently 404ing. A missing image does not move anything, because the header artwork, the member cards and the grid tiles all have fixed aspect ratios. The page measured perfect and looked broken. You caught it; my checks did not. Whatever check list comes out of this audit, "the images actually loaded" needs to be a line in it, because "the layout is identical" does not imply it.

---

## PART D — The 404 page

**Template file:** `404.php`, 143 lines. **It has no CSS file of its own,** no inline `<style>` block, and no `style=` attribute anywhere. It borrows two stylesheets: `policies.css` for the whole `.policy-page` frame (§1 shell, §2 breadcrumb, §3 header, §9 "Where next?" rows) plus a dedicated §12 block scoped to `.policy-page--404`; and `help.css` for the question-door component.

Root element: `<main id="main" class="policy-page policy-page--404">` → `<div class="page-container">` → `<div class="article-container">`, the 880px reading column.

### Section 1 — Breadcrumb

Two items. A link to the home page whose content is the Lucide House icon, labelled `aria-label="Home"`; then a ChevronRight separator marked `aria-hidden="true"`; then plain current-page text, not a link.

- Current-page text: `Page not found`

### Section 2 — Page header

Three stacked lines — a small orange overline, an H1, a lead paragraph. This element also hosts the 420px bubble watermark, which `components.css` §3 attaches to `.policy-header::before`.

- Overline: `Find your way`
- H1: `Oops! You&rsquo;re on a page that no longer exists.`
- Lead: `Don&rsquo;t worry! We want to help you find what you&rsquo;re here for. Whatever led you to this page, and wherever you were headed, getting access to all of Achology is just a click away. Everything else is where it should be.`

### Section 3 — "Where next?" — six doors

A heading, a lead line, then six full-width link rows. Each row is an icon on the left, a two-line text block (bold name over grey description), and a ChevronRight on the right. The data comes from a `$ach_doors` array and every href is built with `home_url()`.

- H2: `Where to instead?`
- Lead: `Here are some popular pages that people visit.`

| # | Name | Description | Links to | Icon |
|---|---|---|---|---|
| 1 | `Go to the homepage` | `Start from the front door` | `/` | House |
| 2 | `Learn about Achology` | `Who we are and what we stand for` | `/about/` | Compass |
| 3 | `Explore Achology&rsquo;s schools` | `Seven schools of applied psychology` | `/academy/schools/` | GraduationCap |
| 4 | `Browse Achology&rsquo;s courses` | `All 28 courses in one place` | `/courses/` | BookOpen |
| 5 | `Browse the Knowledge Hub` | `Articles, book notes, quotes and workbooks` | `/learn/` | LibraryBig |
| 6 | `Explore Achology pricing` | `What membership includes, and what it costs` | `/pricing/` | Tag |

### Section 4 — "Popular Questions"

Borrowed wholesale from `/help/`. A header row of a circular badge holding a CircleQuestionMark glyph beside an H2, then four question rows — bold question title over a one-line grey excerpt, with a ChevronRight.

- H2: `Popular Questions`

| # | Question | Excerpt | Links to |
|---|---|---|---|
| 1 | `Where should I start with Achology?` | `Where you start depends on your situation and goals.` | `/help/getting-started/where-should-i-start-with-achology/` |
| 2 | `What makes Achology different from other online learning platforms?` | `Courses sit inside a live community, so skills are practised with real people.` | `/help/achology-basics-and-identity/what-makes-achology-different/` |
| 3 | `What are the seven schools of Achology?` | `Seven learning paths, one for each tradition of applied psychology.` | `/help/achology-basics-and-identity/seven-schools-of-achology/` |
| 4 | `Do I need prior qualifications to study at Achology?` | `No prior qualifications, psychology credentials, or academic background are required.` | `/help/getting-started/prior-qualifications-needed-achology/` |

**These four are hardcoded, and nothing in the file marks them as provisional.** See Part B3 — this is the one placeholder in the theme that is not acknowledged in its own comment, and it is the pattern the `/help/` landing page explicitly rejected because re-slugged articles would rot the links.

**Nothing follows.** No search box, no CTA, no images beyond the CSS watermark. Then the footer.

### Styling that differs from the rest of the site

Three rules only, all in `policies.css` §12 and all scoped to `.policy-page--404`:

1. `.policy-page--404 .policy-next { margin-top: 0; }` — zeroes the panel's own 64px so the header's 48px rules.
2. `.policy-page--404 .policy-header { padding-bottom: 43px; }` — an optical correction, documented in the file: *"a box-true 48px reads as ~53px against the panel's exact 48px below. 43px of padding puts the ink-to-line distance at 48px — an optical correction, not a drifted token. 404 only."*
3. `.policy-page--404 .help-popular` gets a 48px top margin, a 1px hairline top border and 48px top padding, because the about-pages' scoped separator never reaches it.

Everything else is inherited unchanged.

### Two deliberate absences, both documented in the file

- **No search box.** *"Deliberately NO search box: the theme has no search template, so a search would land on the index.php fallback — a worse dead end than this page."*
- **No "404" or "error" wording in the visible copy.** *"no 'error', no '404', nothing that reads as the site being broken."* Confirmed — those strings appear only in the docblock and the class name.

---

## PART E — What I know about your standards

Answered honestly, including the noes.

### E1. Do I have access to DSRD 6 (The Page-Readiness Standard)?

**Yes.** It sits **in the theme repo**, at `docs/DSRD_6_Page_Readiness_Standard.md`. It was added in commit `02e3a73` ("Add DSRD 6 page-readiness gate"), which is two commits behind the current head.

It is Version 1, dated 20 July 2026, and it runs §0 to §10: how the gate works, copy standards, page structure and headings, metadata and preview data, schema markup, search visibility, AI visibility, accessibility, ease of use, speed, and the by-page-type exemption table.

I have read it in full in preparing this report. I should be straight with you: **it is in the repo, but it has not been governing my work.** I did not read it at the open of this session — `CLAUDE.md` sends me to the memory note and the theme, and does not mention `docs/`. I found it while answering this question. It has been available for two commits and I have not run a page through it.

### E2. Which of your DSRDs do I have access to, and how?

| DSRD | Do I hold it? | How I encounter it |
|---|---|---|
| DSRD 6 | **Yes — the full document** | `docs/DSRD_6_Page_Readiness_Standard.md` in the theme repo |
| DSRD 1, 2, 3, 4, 5, 7, 8, 9, 10 | **No** | Second-hand only |

"Second-hand" means precisely this: I see them **cited in code comments written by earlier sessions** — for example `template-policy.php` points to "policies.css §9" and names Lucide icons as "DSRD 7 §5.2"; `page-about.php`'s grid carries a reference to "DSRD 5 §2.6" — and I see them **quoted or paraphrased in your prompts** and in the memory notes. I have never opened DSRD 1, 2, 3, 4, 5, 7, 8, 9 or 10.

The practical consequence: when a code comment says a block was built to "DSRD 7 §5.2", **I am trusting that comment, not checking it.** I cannot verify a single one of those citations. Every "built against" answer in this report that names a DSRD other than 6 should be read as "the code claims this", not "I confirmed this".

`CLAUDE.md` tells me design-system rules live in the DSRD set and that I should read the relevant DSRD before building. In practice I cannot, because they are not reachable from here. That gap is worth your attention more than anything else in this report.

### E3. Am I aware of a file-level standard for HTML and CSS files?

**Yes — by name, as skills available to me, not as documents I have been applying.**

There are skills in my available list called **`production-html-files`**, **`production-css-files`**, **`achology-building`**, **`house-copy-standards`**, **`visual-design-craft`** and **`component-library`**. Their one-line descriptions match what DSRD 6 §0 refers to when it says the file-level tests must pass before the page gate runs — `production-css-files`, for instance, describes itself as governing executable-asset content, token references, specificity discipline, magic-number audit, class-naming, comment audit, and responsive and rendered verification.

Honestly: **I have not been invoking them.** They are listed as available; nothing in `CLAUDE.md` tells me to load them, and I have not been loading them before building. So the answer to "are you aware of a file-level standard" is yes, and the answer to "have you been meeting it" is that I do not know, because I have not read the standard I would be measured against.

### E4. Is there a standing instruction file I read at the start of each session?

**Yes — three, in this order.**

1. **`CLAUDE.md`**, at the project root (not in the theme repo). This is the one that binds. It tells me: read the memory note first and work from the theme at its canonical path; speak in plain prose, a few short lines, no headers or bullet dumps; you own every design decision and a design question is a request for options, never authorisation to build; bring one question or one recommendation per exchange; never show a component on a blank page — every preview is the whole page in Safari before it ships; one canonical file in one canonical place, never suffixed copies; you create and delete WordPress pages, the theme never does; announce every push with its version and rebuild the zip; no page is finished without its Rank Math metadata; no handover documents at session close; and design rules live in the DSRDs, never restated in `CLAUDE.md`.
2. **The memory note `achology-next-session-plan`**, which carries state, outstanding issues and the next agenda from the previous session.
3. **`README.md`** in the theme repo — not on every session, but it is the theme's own description of what is complete and how the workflow runs.

### E5. In my own words: what does "done" currently mean for a page I have built?

Before I read DSRD 6 this morning, "done" meant, in practice:

> The page renders correctly in a live browser at desktop, tablet and phone; you have looked at it and approved the design; the code is committed and pushed with a version number; the zip is rebuilt; and the Rank Math SEO and GEO metadata is written and handed to you.

That is a **build-and-render standard**. It answers "does it work and does it look right" and it stops there. Reading DSRD 6 shows me how much that leaves out. My working definition contains nothing about schema markup, nothing about whether the page is linked to rather than orphaned, nothing about keyboard operation or contrast ratios or the accessibility tree, nothing about a Krug trunk test or a Nielsen walk, nothing about PageSpeed, and no notion that the usability walk should be run by someone who did not build the page in that sitting. It also has no concept of a *recorded* exception — when something did not apply, I have simply not done it and not written down that I did not.

So: my "done" is roughly DSRD 6 §2 and part of §3, and nothing else. It is a fraction of your gate, and I have been calling pages finished on it.

---

## PART F — The About template built this week

A factual build description. Nothing here prescribes; nothing here is measured against a standard.

### F0. What it is, in one line

A new WordPress template, `page-about.php`, which renders the page at `/about/`, together with two page-scoped asset files. It was built this session from `previews/about.html`, which was designed and approved with you over the preceding day and pushed as v0.35.0. Before this session the design existed **only** as a preview — there was no template and nothing installable.

**The whole page is static.** Every word, figure, link and image is baked into the template file. It reads nothing from the WordPress editor and nothing from ACF.

### F1. Every section, top to bottom

| # | Section | What sits in it |
|---|---|---|
| 1 | Breadcrumb | Home icon linking to `/`, chevron, current-page label "About Achology" |
| 2 | Page header | Overline "About"; H1; lead paragraph; academy artwork at top-right on desktop, circle-cropped, anchored to the H1 glyph line and the container edge. Mini-header on tablet (text two-thirds, whole image one-third); stacked on phone. |
| 3 | "What It Is, and Who It's For" | H2, an intro paragraph, then a five-question selector — a 300px question rail on the left, answer panel on the right (desktop). Below desktop it becomes a true accordion, all five closed on load. |
| 4 | "The Thinking that Drives Achology" | H2, lead line, and four link cards in a 2×2 grid |
| 5 | "The Achology Story" | The timeline window. Heading and lede ride *inside* a frame that pins to the viewport; beneath them a dark stage with an animated odometer, a chart with 13 milestone dots and an era flag, and a live counter; beneath that a fixed-height window through which a 13-milestone timeline scrolls 1:1 as the page scrolls. Closes on a terminus line. Below the window, a four-figure stats panel. |
| 6 | "In Our Students' and Members' Words" | H2, one line of copy, five video cards (two across the top, three beneath), then a note line |
| 7 | "Explore and Experience Achology for Yourself" | H2, lead line, and a ten-card grid of routes into the site |
| 8 | "Other Achology Related Questions" | A badge, H2, and eight linked questions with excerpts, in two columns |
| 9 | Video lightbox | Hidden until a member-story card is clicked; moved to the end of `<body>` by script on load |

**How the timeline window behaves.** The frame pins with `position: sticky`; the timeline track translates upward one pixel for every pixel of page scroll, so the story moves through the window at 1:1. As each milestone crosses a reading line 96px inside the window it is marked reached, and the dark stage above repaints — odometer, chart dots, era name and dates, and the counter — to the year at that line. Window height is `clamp(260px, calc(100vh - 703px), 510px)` on desktop and `calc(100vh - 674px)` on tablet. If the frame cannot fit the screen, the script adds `.is-flat` and the whole block lies flat as a plain list. Measured this session: flat is **false** at 1440×1000 and at 768×1024, and **true** at 390×844.

### F2. The exact wording

Reproduced verbatim, HTML entities preserved as written in the file.

**Header**

- Overline: `About`
- H1: `About Achology` (with "Achology" in the accent span)
- Lead: `At Achology, we teach the applications of modern psychology in a practical way you can understand and actually use. We&rsquo;ve spent a decade teaching more than 670,000 students from 216 countries the psychology, people skills, and depth of self-knowledge that genuinely improves lives. Would you like to know more?`

**Section 3 — What It Is, and Who It's For**

- H2: `Achology: What It Is, and Who It&rsquo;s For`
- Intro: `Achology hosts an academy of modern applied psychology and a global network of self-motivated learners aiming to improve themselves and influence humanity. We are devoted to teaching psychology in a way that makes you wiser, not just smarter. Below are frequently asked questions from those considering studying with Achology.`

The five questions, in order, each with its three-paragraph answer:

**Q1 — `Why Does Achology Exist?`** *(open on load at desktop)*
1. `Achology exists to make psychology relevant, accessible and something you can understand, embody, and use in everyday life.`
2. `Most psychology-based education prioritises information delivery over insight, credentials over competency development, and knowledge over character development. Learners are encouraged to consume content, take assessments, and pass tests, with little consideration given to whether any of it develops genuine judgement, emotional maturity, or practical ability.`
3. `Achology&rsquo;s purpose is to close that gap. Studying psychology should help people understand themselves more thoroughly, relate to other people more thoughtfully, and act with greater clarity in every area of life. That cannot come from knowledge alone, it requires reflection, practice, dialogue, and the time needed for genuine understanding to take root.`

**Q2 — `How Does the Learning Work?`**
1. `Learning at Achology is active, applied in real life, explored through thoughtful questions, and deepened through reflective dialogue.`
2. `Most expressions of online education invite learners to watch videos, read documents, and document their own learning, which treats the acquisition of new knowledge as something that should be absorbed quietly and in isolation rather than discussed and applied. Reflection, open dialogue, and real-world practice are rarely a genuine part of the experience.`
3. `At Achology, learning moves from theory into lived experience. Students apply skills in real-life contexts, observe their own thinking and behaviour, and test their understanding through conversation with others. Through consistent practice and community dialogue, learning becomes part of how a person thinks, decides, and responds, both personally and professionally.`

**Q3 — `What Influences Achology&rsquo;s Teaching&nbsp;Philosophy?`**
1. `Achology teaches universal principles rather than quick techniques: learned for your own life, and built to be passed on.`
2. `There is an old and enduring truth about teaching. Give a man a fish and he eats for a day; teach him to fish and he eats for a lifetime. But there is a third level: teach a man to teach others to fish, and he plays an active part in ending world hunger itself. The first gives a meal, the second gives a skill, but the third multiplies wisdom far beyond any one life or lifetime.`
3. `Achology teaches at that third level. Every one of its courses is grounded in universal principles rather than anecdotal fixes or empty theory: principles any person can apply within their own life first, test through daily practice, and then share. Students find that the deepest value of what they learn arrives when they pass it on, in their families, their work, and their communities.`

**Q4 — `Is Achology Right for Me?`**
1. `Achology is designed for learners who are reflective, curious, and committed to their own personal and professional growth.`
2. `Achology was created for learners who sense that genuine, lasting personal growth requires something far deeper than credentials, formulas, or quick-fix techniques. It is for those who are reflective, humble, and curious enough to look honestly inward, and who understand that real wisdom cannot be rushed, borrowed, or reduced to a simple set of instructions.`
3. `If you want your learning to shape the way you live, work, and relate to the people around you, Achology was built with you in mind. Those who benefit most are individuals who are already committed to their own growth, and who are ready to engage honestly and courageously with the full complexity of being human. If that sounds like you, you are already thinking in the right direction.`

**Q5 — `Is Achology Accredited and Recognised? If so, by who?`**
1. `Yes. Achology&rsquo;s certification is independently verified, its training is CPD accredited, and it is a registered UK training provider.`
2. `Much of online education treats certification as a formality: certificates are bundled with course purchases and carry little weight beyond the platform that issued them. Genuine recognition, the kind that stands scrutiny, works differently. It depends on independent verification, published standards, and a defined route that asks something real and demonstrable of the student.`
3. `Achology is recognised by the Society of Modern Applied Psychology (SoMAP) and is registered with the UK Register of Learning Providers (UKRLP PRN: 10099815). Since 2024, SoMAP has been responsible for designing and maintaining the competency development framework that all accredited Achology graduates are required to complete as part of their training.`

**Section 4 — The Thinking that Drives Achology**

- H2: `The Thinking that Drives Achology`
- Lead: `Four pages and documents that detail &lsquo;how&rsquo; Achology works and the mechanics that allow it to do so.`

| Card | Name | Description | Links to |
|---|---|---|---|
| 1 | `The Achology Manifesto` | `The characteristics and professional standards that all Achology members strive to embody` | `/about/manifesto/` |
| 2 | `Achology&rsquo;s Code of Ethics` | `The unconventional code of Ethics training which bolsters the heart of our accreditation process` | `/about/code-of-ethics/` |
| 3 | `Policies &amp; Legal Documents` | `Our commitments to every student and member alike, in simple and straightforward language` | `/policies/` |
| 4 | `Foundational Principles` | `Hear directly from Achology&rsquo;s co-founders about the main reasons why Achology exists` | `/about/founders-letter/` |

**Section 5 — The Achology Story**

- H2: `The Achology Story`
- Lede: `Like all great educational institutions of our time, Achology boasts a unique origin story. Thirteen milestones across five eras, from the world&rsquo;s first video-based psychology course to a worldwide learning community 670,000 students strong.`
- Dark stage at rest: era name `Origins`, dates `2012–2014`, odometer `5,000`, counter label `Students &amp; Active Members Enrolled`

The five eras, as their tags read:

| Era tag | Dates |
|---|---|
| `Achology Origins` | `2012–2014` |
| `The Growth Years` | `2015–2017` |
| `The Expansion Years` | `2019–2020` |
| `The Evolution Years` | `2021–2023` |
| `Community Development` | `2024–2026` |

The thirteen milestones, in order. Year, title, then body. Inline links are marked.

**1. `2012` — `The world&rsquo;s first video-based psychology course, published on Udemy`**
`[Kain Ramsay →/about/instructors/kain-ramsay/] records and publishes the world&rsquo;s first video-based psychology training programme, taking a subject usually reserved for lecture halls and private clinics and putting it in front of anyone with an internet connection. The foundation of what would later become Achology is laid in this single, quiet decision.`

**2. `2014` — `The Achology learning platform was first founded with 12 courses included`**
`The Academy of Applied Psychology opens with 12 on-demand courses, built on the conviction that psychological education belongs to anyone prepared to study it seriously, whatever their background. What began as a single course becomes a platform with a curriculum, a clear direction and a name.`

**3. `2015` — `Curriculum expands to 17 interlinked psychology-based e-learning courses`**
`The curriculum deepens into 17 interlinked e-learning courses, each designed to reinforce the others rather than stand alone, so understanding compounds with study. Students no longer simply buy a course; they enter a coherent body of work with a grounded, deliberate order to it.`

**4. `2016` — `Live ONLINE skill and competency development training workshops begin`**
`Achology begins running live, real-time online group workshops for skill and competency development, connecting students across time zones who had until now studied alone. It is the first expression of the principle that comes to define the academy: psychology is learned in dialogue, with and through other people.`

**5. `2017` — figure `100,000` / `Students &amp; Active Members Enrolled` — `A landmark year for Achology: global scale, platform growth &amp; partnerships`**
`Achology passes 100,000 enrolled students, begins building its own bespoke learning management system, and launches an exclusive Skilled Helper course with [Prof. Gerard Egan →/about/instructors/gerard-egan/], one of the field&rsquo;s most respected voices. In five years, a single Udemy course has grown into a global teaching platform with infrastructure and a faculty of its own.`

**6. `2019` — `Diploma in Modern Applied Psychology launched (Achology&rsquo;s flagship course)`**
`The [Diploma in Modern Applied Psychology →/courses/] launches and gains global popularity, offering a structured route through psychological principles, from first theory to practised competence. DiMAP gives the academy its centre of gravity: one flagship course that carries the whole approach and sets its standard.`

**7. `2020` — `COVID-19 pandemic accelerated the acceptance of online learning worldwide`**
`The pandemic moves the world&rsquo;s classrooms online, and demand for flexible, remote learning rises sharply as millions seek ways to keep studying. Achology&rsquo;s platform, built for exactly this kind of learning years before it became necessary, demonstrates that it can meet the moment at scale, without loosening the standards it had set.`

**8. `2021` — figure `350,000` / `Students &amp; Active Members Enrolled` — `Community learning system upgraded and recognised with CPD accreditation`**
`Achology&rsquo;s collaborative learning environment receives significant upgrades, giving students better tools for discussion and practice, followed by [accreditation →/accreditation/] from the CPD Standards Office. Recognition arrives in the same season as scale: 350,000 students are now enrolled, and the academy&rsquo;s standards are now independently examined rather than simply asserted by the academy itself.`

**9. `2022` — figure `500,000` / `Students &amp; Active Members Enrolled` — `Half a million students reached worldwide, and the curriculum expands to 25 courses`**
`The student database passes a landmark half-million students as the curriculum expands to 25 courses, including 8 in-depth practitioner-level training programmes designed for those intending to work with others. Taken together, the academy now teaches at almost every level, from a first curiosity about human behaviour through to serious, accountable professional practice.`

**10. `2023` — `Launch of Achology version 2 community portal with new 28-course curriculum`**
`An AI-supported, platform-wide upgrade delivers the version 2 community portal and a new 28-course curriculum, the most substantial rebuild the academy has undertaken. The learning experience is reconstructed around the evolving needs of a growing, global membership rather than patched at the edges, with every course reviewed, resequenced and brought into a single coherent structure.`

**11. `2024` — `The Society of Modern Applied Psychology founded, raising integrity standards in the field`**
`Master Achologists found the [Society of Modern Applied Psychology →https://thesomap.org, new tab], an independent body created to raise the standards of training and practice across the field, and to define what competent practice requires. The Society maintains the competency development framework accredited graduates complete. The academy&rsquo;s graduates now hold the profession they trained for to a higher bar than the one they found.`

**12. `2025` — `Achology makes a full migration to Circle.io, finding its permanent online home`**
`Achology completes a full migration to Circle, giving its learning system, its events and its community a single, permanent and properly integrated home after years spread across separate platforms. For the first time, everything the academy does lives in one place, with the functionality needed to scale internationally and the stability to support members through years of study rather than weeks.`

**13. `2025 / 26` — figure `670,000+` / `Students &amp; Active Members Enrolled` — `An Eldership team established, and FREE learning is made available to the public`**
`An eldership team of senior Achologists is established to guide the community and safeguard the standards it has built, and [free group discussions and skill events →/free-events/] are opened to the general public, with no membership required. It is the earliest expression of the wider social impact that future generations of Achology graduates will carry into the world, and a statement of what the academy believes learning is for.`

**Terminus line (closes the timeline):**
`670,000+ mature learners from around the world have brought the Achology story this far. Will you [join them →/membership/]?`

**Stats panel** (four figures, below the window):

| Figure | Label |
|---|---|
| `4.66` | `Average Course Rating` |
| `171,306` | `Total Student Ratings` |
| `216` | `Countries With Students` |
| `28` | `Total Number of Courses` |

**Section 6 — Student voices**

- H2: `In Our Students&rsquo; and Members&rsquo; Words`
- Line beneath: `Student Testimonial Videos: Five Aspects of the Achology Learning Experience`
- Five cards, each a button opening a Vimeo lightbox. Vimeo IDs in order: `929543499`, `1033838777`, `1033843642`, `1033842856`, `1033845034`. Every card's alt text and aria-label are the same: alt `Achology member story`, label `Play member story`.
- Note line: `ⓘ For more authentic reviews of the Achology experience, visit our [Member Testimonials page →/testimonials/].` — the ⓘ is the text character `&#9432;`, not a registry icon.

**Section 7 — Explore and Experience Achology for Yourself**

- H2: `Explore and Experience Achology for Yourself`
- Lead: `This block gives you the complete gateway into all corners of Achology.`

| # | Card name | Description | Links to |
|---|---|---|---|
| 1 | `Start Learning With Achology&rsquo;s Flagship Course` | `The Diploma in Modern Applied Psychology (DiMAP): If understanding your own psychology is on your learning radar, this course may be the best investment you ever make into yourself.` | `/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/` |
| 2 | `Browse Achology Courses` | `Twenty-eight unique training courses, on-demand, and relevant to every man, woman, and child alive in the world.` | `/courses/` |
| 3 | `The Accreditation Pathway` | `How to earn certificates for completing courses, and achieve accreditation for becoming a competent expert.` | `/accreditation/` |
| 4 | `Explore Achology Schools` | `Seven different, yet interconnected psychological perspectives that the Achology course curriculum is built upon.` | `/academy/schools/` |
| 5 | `Review Achology&rsquo;s Pricing` | `Simple, transparent and flexible payment options for Achology full range of course and subscription options.` | `/pricing/` |
| 6 | `Access Achology for Free` | `No, you won&rsquo;t get much for free, which is fair, but what you can get is excellent. Live events, 5 days a week.` | community.achology.com join link (with invitation token) |
| 7 | `Unlock Full Access for $7` | `Get 30-day trial of the Achology membership community today for less than the price two small cappuccinos.` | `/pricing/` |
| 8 | `Meet Achology&rsquo;s Founders` | `Read an honest, and very personal message from Achology&rsquo;s co-founders, who&rsquo;ve invested in Achology since 2017.` | `/about/founders-letter/` |
| 9 | `Visit the Knowledge Hub` | `Browse our enlightening articles, book notes, thought provoking quotes and get instant access to workbooks.` | `/learn/` |
| 10 | `Learn About the Community` | `Join a community rich with learning opportunities, 1-to-1 coaching, group mentorship and reflective discussions.` | `/membership/` |

Card 2 is the tall card and carries an image plus three learning paths: `9 Mental Health and Wellbeing / On-Demand Training Courses`, `9 Personal Growth and Development / On-Demand Training Courses`, `12 Applied Psychology Certification / On-Demand Training Courses`.

Card 1 spans two columns. Cards 3, 4 and 9 carry full-bleed background images.

**Section 8 — Other Achology Related Questions**

- H2: `Other Achology Related Questions`

| Question | Excerpt | Links to |
|---|---|---|
| `What is Achology?` | `An online applied psychology academy: 28 courses across seven schools, a learning community and a certification pathway.` | `/help/achology-basics-and-identity/what-is-achology/` |
| `Who is Achology designed for?` | `Reflective, self-directed adults building helping practices, adding psychological skill, or growing on their own terms.` | `/help/achology-basics-and-identity/who-is-achology-designed-for/` |
| `What makes Achology different from other online learning platforms?` | `Courses sit inside a live learning community rather than standing alone as content to be consumed.` | `/help/achology-basics-and-identity/what-makes-achology-different/` |
| `What are the seven schools of Achology?` | `Seven learning paths, one for each tradition of applied psychology the academy teaches.` | `/help/achology-basics-and-identity/seven-schools-achology-curriculum-explained/` |
| `Is Achology a university or degree provider?` | `No. Achology is an independent education provider on the UK Register of Learning Providers, and it does not award degrees.` | `/help/achology-basics-and-identity/is-achology-a-university/` |
| `Is Achology an educational provider or a professional body?` | `Achology teaches; the Society of Modern Applied Psychology independently accredits and sets the standards.` | `/help/achology-basics-and-identity/is-achology-educational-provider-or-professional-body/` |
| `Where should I start with Achology?` | `Where you start depends on your situation and goals.` | `/help/getting-started/where-should-i-start-with-achology/` |
| `What has society lost by gatekeeping psychological knowledge?` | `Psychological understanding belongs in ordinary life, not only in clinics and lecture halls.` | `/help/comparisons-and-alternatives/society-lost-gatekeeping-psychology/` |

### F3. Which components it uses

**Reused from elsewhere** — 29 classes from the policy frame, plus the site chrome:

| Component | Where it comes from |
|---|---|
| `.policy-page` shell, `.page-container`, `.article-container` | `base.css` / `policies.css` — the frame every policy and legal page uses |
| `.policy-breadcrumb` / `.breadcrumb*` | `components.css` |
| `.policy-header`, `.policy-header--doc`, `.policy-header__overline`, `.policy-header__text` | `policies.css` |
| `.policy-title`, `.policy-lead`, `.policy-next__accent` | `policies.css` |
| `.policy-body`, `.policy-body--ruled` | `policies.css` |
| `.policy-next` family — `__title`, `__lead`, `__list`, `__row`, `__icon`, `__text`, `__name`, `__desc`, `__arrow`, `--pair` | `policies.css` §9 "Where next?" — used for both the four thinking cards and the ten-card grid |
| `.help-popular`, `.help-q-list`, `.help-q*` | `help.css` — the related-questions block |
| Site header and footer | `header.php` / `footer.php` |

**Newly built for this page** — roughly 100 classes across seven CSS blocks:

| Component | What it is |
|---|---|
| `.about-header__art` | The circle-cropped academy artwork in the header |
| `.pfq*` | The question selector: rail, panels, chevrons; two-column on desktop, accordion below |
| `.tw*` (`tw-wrap`, `tw-frame`, `tw-window`, `tw-track`, `tw-heading`, `tw-lede`) | The pinned timeline window |
| `.cons*` (`cons-stage`, `cons-count`, `cons-groups`, `cons-terminus`) | The dark stage, its counter and the closing line |
| `.fa*` / `.fam*` / `.m-*` (`fa-row`, `fa-dot`, `fam-group`, `m-year`, `m-title`, `m-desc`, `m-stat`, `m-tag`) | Timeline rows, dots, era groups and milestone content |
| `.st-*` | The inline SVG chart in the dark stage — segments, dots, bubbles, era flag |
| `.odo-*` | The odometer digit strips |
| `.story-proof*` | The four-figure stats panel |
| `.about-proof__strip`, `.proof-card*`, `.about-video-lightbox*` | Member-story grid and the Vimeo lightbox |
| `.about-grid*` (`__lead`, `__tall`, `__buy`, `__paths`, `__path`, `ic-dark`/`ic-orange`/`ic-slate`/`ic-tint`, `has-bg`/`bg-accred`/`bg-schools`/`bg-hub`) | The ten-card grid: tile layout, icon tones, background images |

### F4. Every file it comprises

| File | Lines | Status | Notes |
|---|---|---|---|
| `page-about.php` | 576 | **New, uncommitted** | Slug template — WordPress attaches it automatically to the page whose slug is `about`. No "Template Name" header, so there is nothing to assign in the editor. |
| `about.css` | 571 | **New, uncommitted** | Enqueued only on `/about/`, after `policies.css`, whose frame it extends |
| `about.js` | 305 | **New, uncommitted** | Enqueued only on `/about/`, in the footer. Four independent scripts, each a no-op without its markup: count-up figures, the timeline window, the question selector, the member-story lightbox |
| `functions.php` | modified | **Uncommitted** | Two conditional enqueues added, both gated on `is_page( 'about' )` |

Loaded alongside, unconditionally, as on every page: `fonts.css`, `base.css`, `components.css`, `cards.css`, `style.css`, `header.css`, `footer.css`, `policies.css`, `help.css`, `people.css`, `header.js`, `footer.js`, plus the Google Fonts stylesheet.

Images the page uses, all shipping in the theme:
`images/about/about-achology-header.webp`, `images/about/grid-courses.webp`, `images/about/grid-schools.webp`, `images/about/grid-accreditation.webp`, `images/about/grid-knowledge.webp`, `images/achology-bubble-mark.webp`, and five member-story posters at `images/about/testimonials/{vimeo-id}.webp`.

### F5. Every ACF field it reads

**None.** Zero calls to `get_field`, `the_field`, `have_rows` or `get_sub_field` in `page-about.php`. The page is entirely static, so the question of a missing Local JSON field group does not arise for it.

### F6. Anything that differs from the rest of the site

Factual differences, not judgements:

1. **It is the only slug-based page template in the theme.** Every other page template uses a `Template Name:` header and has to be assigned in the editor. `page-about.php` binds itself to the slug `about`.
2. **It is the only template that bakes its own page content into the template file.** The policy pages bake content too, but into separate partials under `policies-content/`, which the one shared frame then renders. About has no such separation.
3. **It is the only page with scroll-driven pinned behaviour** — `position: sticky` plus a JS-driven 1:1 transform.
4. **It is the only page with a video lightbox** and the only one embedding Vimeo.
5. **It is the only page with a hand-built inline SVG chart** driven by data in JavaScript.
6. **It is the only page carrying two page-scoped asset files.** Every other conditional enqueue in `functions.php` is either a section (`knowledge-hub.css`) or a single script.
7. **Quoting style is mixed.** The six inline links inside the timeline milestones use single-quoted attributes (`href='/accreditation/'`); everything else in the file uses double quotes. This came through from the builder and I left it as it was.
8. **The header artwork is a plain `<img>` inside `figure.policy-doc`**, not the framed clickable document button that `policy-doc` normally carries on the Manifesto and Code of Ethics pages. It reuses the container and not the behaviour.
9. **The ⓘ in the testimonials note is the text character `&#9432;`**, not an icon from the registry.

### F7. Every decision I made myself, because nothing told me

This is the section you said matters most, so it is complete rather than tidy — small things included.

**Structural**

1. **Made it a slug template (`page-about.php`) rather than a named template.** So it binds automatically to `/about/` and you have nothing to assign in the editor. Nothing specified this; a `Template Name:` header would have worked too and would have matched every other template in the theme.
2. **Gated both enqueues on `is_page( 'about' )`.** A slug template cannot be detected with `is_page_template()`, so the condition keys on the page rather than the template. If the page's slug is ever anything but `about`, the styles and scripts silently stop loading. Nothing specified the condition and nothing guards against that.
3. **Put `about.css` after `policies.css` in the dependency chain,** so it overrides the frame it borrows. It sits after `achology-policies` and therefore also after `header` and `footer`, but before `help.css` — even though the page uses `help-popular` from `help.css`. That ordering was mine and I did not test what happens if a `help-*` rule ever needs overriding from `about.css`.
4. **Split the work into two files (`about.css` + `about.js`) rather than one bundle or inline blocks.** Nothing said which.
5. **Kept the four scripts in a single `about.js`** rather than four files, each guarded to no-op when its markup is absent.

**Content and markup**

6. **Removed the orphaned prospectus lightbox** — the markup plus a 70-line script — because its trigger had gone when the prospectus block was cut, leaving it unreachable. I told you after the fact, not before. You can have it back.
7. **Left all internal links as literal root-relative paths** (`/pricing/`, `/courses/`) rather than converting them to `home_url()`. Cleaner to read, and correct while the site is at the domain root; it would break if the site ever moved to a subdirectory.
8. **Used `esc_url( $ach_uri )` with a single `$ach_uri = get_stylesheet_directory_uri()` variable** for the nine image paths, rather than repeating the function call or hardcoding.
9. **Left the mixed single/double quoting** in the timeline links as it came out of the builder rather than normalising it — normalising would have meant editing approved markup for cosmetic reasons.

**Method**

10. **Extracted by running the builder in-process** and taking its exact objects, rather than copying markup and CSS by hand, so the shipped files could not drift from the approved preview. Then reverse-mapped every inlined base64 image back to its theme file by hashing the theme's images.
11. **Referenced images as theme files rather than baking them in as base64.** This is what the preview does differently by design — a preview is one portable file, a theme is not — but nothing stated it, and it is the decision that made the images appear "missing" when my verification harness failed to serve them.
12. **Chose the verification method:** mirroring the theme the way WordPress serves it, then diffing every element inside `<main>` between the approved preview and the installed page for size, position, colour, font and display, at 1440, 768 and 390. 675 elements, zero differences at all three widths.
13. **Wrote the file header comments myself** — the section index in `about.css`, the four-script summary in `about.js`, and the note in `page-about.php` explaining why the page is static. These are my words, not from any specification, and they will read as authoritative to whoever comes next.

**Not mine, recorded for completeness:** the template-versus-policy-page decision was brought to you as a yes/no and you decided it. Everything in F1 and F2 — the sections, the running order, the wording, the removals — was designed and approved with you before this session.

---
