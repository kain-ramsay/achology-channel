# RECORD: the Manifesto, page 8 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Page:** https://achologytest.com/about/manifesto/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_manifesto.md` (S230 era).

**Verdict: the page is clean. Its machine gate passes for the first time ever, and two chapters wait on a ruling rather than on a fix.**

**Read this first, because it changes what earlier records meant.** This page has never actually been gated. The standing health check listed it as `/manifesto/`, which 301s to `/about/manifesto/`, so every run measured a redirect rather than a page, produced 4 of the 29 rows, and reported "4 pass, 4 FAIL". It looked like a page with problems. It was a page nobody had measured. Same for the Code of Ethics. Both instruments are fixed and the fix is proved below.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. **The first true measurement this page has had:**

```
  PASS      hairline-present   desktop boundary 1 (policy-breadcrumb | policy-header policy-heade): breadcrumb junction, no line, correct
  PASS      hairline-spacing   desktop boundary 2 (policy-header policy-heade | policy-body policy-body--r): 48 above, 48 below
  PASS      hairline-present   tablet boundary 1 (policy-breadcrumb | policy-header policy-heade): breadcrumb junction, no line, correct
  PASS      hairline-spacing   tablet boundary 2 (policy-header policy-heade | policy-body policy-body--r): 48 above, 48 below
  PASS      hairline-present   mobile boundary 1 (policy-breadcrumb | policy-header policy-heade): breadcrumb junction, no line, correct
  PASS      hairline-spacing   mobile boundary 2 (policy-header policy-heade | policy-body policy-body--r): 32 above, 32 below
  PASS      hairline-edges     no line at page top or bottom
  PASS      boundary-owner     desktop boundary 2: lastOfA_marginBottom 48px, declared by .policy-page:not(.policy-page--404) .policy- in policies.css
  PASS      boundary-owner     desktop boundary 2: lastOfA_paddingBottom 48px, declared by .policy-page:not(.policy-page--404) .policy- in policies.css
  PASS      header-to-content  desktop: 48.0px (want 48)
  PASS      header-to-content  tablet: 48.0px (want 48)
  PASS      header-to-content  mobile: 32.0px (want 32)
  PASS      content-width      page-container: 1200px
  PASS      content-width      article-container: 880px
  PASS      h1                 32px / 700 "The Achology Manifesto"
  PASS      gutters            desktop: 48 / 48 (want 48)
  PASS      gutters            tablet: 32 / 32 (want 32)
  PASS      gutters            mobile: 20 / 20 (want 20)
  PASS      meta-title         55 chars: Achology Manifesto: The Standard Our Community Lives By
  PASS      meta-description   138 chars: The Achology Manifesto exists so that everyone who learns, t
  CARVE-OUT canonical          absent, and correct: page is noindex, so Rank Math withholds it by design. Verified at cutover, not here.
                               ^ DSRD 6 section 3.3 (amended S245)
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      41 checked, all resolve
  NOT-BUILT links-resolve      planned in DSRD 1, page not built yet: /academy/ (404); /academy/schools/ (404); /certification/ (404); /courses/ (404); /accreditation/ (404); /academy/neuro-linguistic-programming/ (404)
------------------------------------------------------------------------------
  PASS   23 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
```

23 rows rather than 28, because this page has one block boundary where the legal policies have two: it carries no endnote block. That is the page's shape, not a missing check.

**The guard, proved both ways.** `page_gate` now refuses to grade a redirect instead of quietly scoring one:

```
page_gate  https://achologytest.com/manifesto/
  FAIL      page-loaded  no h1, no block boundaries and almost no text: this address very likely
                         redirects, so what was measured is not a page. Check the address against
                         DSRD 1's URL table and gate the address the redirect points at.
                         ^ DSRD 6 §11
```

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **Pass, with one narrow ordering fault worth your judgement** | Dash check clean: 0 em, 0 en on the rendered page, confirmed twice. **A tool correction I owe you:** my own reporter announced one em dash on this page. It was wrong. Every occurrence sits inside HTML and JavaScript source comments, which are developer notes and not "page copy, articles, headings, metadata, captions, CSV fields and emails" as DSRD 2 s3.0 defines the ban. `page_gate` read the rendered text and correctly said zero. I fixed my reporter to strip comments before it cost a false finding on the fourteen pages still to walk. **SoMAP is expanded, and expanded well:** "Our Code of Ethical Practice, developed by the Society of Modern Applied Psychology (SoMAP)". **The narrow fault is ordering:** the H2 "Our Commitment to the SoMAP Code of Ethical Practice" uses the short form, and the expansion arrives in the paragraph immediately beneath it. s1 requires the full name to have "already appeared", so by the letter this fails, though by one heading and with the expansion in the very next sentence. I record it as a fail for consistency with how I treated the same ordering test on the Disclaimers, and I flag that its real reader impact is close to zero. The fix is one heading or one sentence, and the words are yours. |
| **s2 Structure and headings** | **Pass** | One H1 ("The Achology Manifesto"), five section H2s, and a "Related Questions" H2 for the `.help-popular` block now registered as DSRD 8 s17. No skipped levels. Read alone the headings tell the page's story: what the manifesto is and why it matters, that it is read aloud daily, what the learning is like, the commitment to the ethical code, and how to start. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception** | Title 55 characters, unique, subject in the first two words. Description 138 characters, unique. **The em dash in the OG alt text is gone**, fixed under your S246 extension and read back off this live page: "The Achology Manifesto: an ancient handwritten scroll lit in amber against a dark background". Worth noting the image itself still does not render into `og:image` on this page, which rides with the site-wide OG imagery item and is not raised as a gap. **Carve-out:** the canonical. **Exception:** OG imagery provision, site-wide. |
| **s4 Schema** | **WAITING ON RULING** | The page emits `AboutPage` and `BreadcrumbList` with its ListItems. Whether that is correct depends on which row of DSRD 3 s5.3 governs this page, and the document names neither the Manifesto nor the Code of Ethics in any row. Filed as `QUESTION__Which_DSRD_6_Row_Governs_The_Manifesto_And_Code_Of_Ethics.md`. If it is an About page, `AboutPage` is right and two schema dates are missing. If it is a policy page, `WebPage` is right and the type is wrong. I am not choosing. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 **Address correct, and this is the chapter that caught the instrument fault:** DSRD 1 section 2 pins "| /about/manifesto/ | Brand manifesto |", the built page is there, and `/manifesto/` 301s to it. The site was right and the health check was wrong. 2 One clear subject. 4 All 41 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb reads Home > About > The Achology Manifesto, matching the `/about/` hierarchy DSRD 1 puts it in. 8 Unique. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **WAITING ON RULING on the date line; pass on the rest** | The author line is exempt under either candidate row, so that is settled. **The date line is the open one:** this page shows no "Last updated" line, which is correct for an About page and a failure for a policy page. It does carry "This organisational standard was adopted on 17 August 2019", which is an adoption date rather than a last-updated date and I do not think satisfies either row as written. Same question file. **What passes regardless:** the answer sits in the delivered HTML in the open; sources are named; accessibility tree clean, with 62 reachable focusable elements, zero positive tabindex, zero links or buttons without an accessible name, one `main`, one `h1`, and no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **Pass on this page's own account; one chrome item outstanding by reference** | **Zero contrast failures** anywhere in the page, measured across every paragraph, list item, link, bold and emphasised run, heading, span and blockquote in `main`, with alpha compositing and the correct threshold for each size and weight. This page carries no off-white panel links, so the page 6 finding does not reach it. Keyboard walk clean. `scroll-padding-top` 80px. Reflow at 320px: no horizontal overflow, no overflowing element. No forms. **Outstanding chrome item:** the footer column headings, by reference to the corrected finding. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone. Krug's trunk test: a cold arrival gets logo, breadcrumb, one H1, and an opening line that tells them what they are reading and when it was adopted. Nielsen's ten lenses: consistent with the family, breadcrumb the way back, no forms so no error states, and the Related Questions block gives a reader who wants more an obvious next step rather than a dead end. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32. Phone tier 32/32 per DSRD 7 s4.3 as amended S245. No unnamed value found. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 41 links resolve. Checked for the Cookie Policy failure mode: this page makes no claims about how the site behaves. 3 Tracking not instrumented on the build ground. 4 Images: content images carry descriptive alt text, chrome icons deliberately `alt=""`. 5 Kain has not confirmed this page at three widths since it was last changed, and unlike pages 1 to 7 I cannot lean on the 2026-07-29 confirmation, because that pass measured a redirect and he may never have been shown this page in the walk's context. **It should go in front of him at three widths before it is called done.** |
| **s12 Page-type exemptions** | **WAITING ON RULING** | The whole chapter turns on the question above. |

---

## 3. Fixes made this pass

**None to the page.** Two instruments were fixed and committed under their own declaration: `health_check.py` now names the real address, and `page_gate` refuses to grade a redirect at all.

## 4. What I need

1. The page-type ruling, which closes s4, s6's date line and s12 on both this page and the next.
2. Approved wording for the SoMAP heading ordering, if you agree it is worth changing.

Page 9, the Code of Ethics, starts now and completes the policy family.

*No em or en dashes in this file; checked before writing.*
