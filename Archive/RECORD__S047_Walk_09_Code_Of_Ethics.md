# RECORD: the Code of Ethics, page 9 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Page:** https://achologytest.com/about/code-of-ethics/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_code_of_ethics.md` (S230 era).

**Verdict: clean, and the strongest page in the family on the copy standards.** Machine gate passes at its first true measurement. One acronym fails. Two chapters wait on the page-type ruling already filed. Nothing else on this page needs anything.

Like the Manifesto, this page had never been gated: the health check listed it at `/code-of-ethics/`, which 301s to `/about/code-of-ethics/`, so every previous run measured a redirect. Both instruments are fixed and proved.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. **The first true measurement this page has had:**

```
  PASS      meta-title         58 chars: The Code of Ethics for Practitioners of Applied Psychology
  PASS      meta-description   148 chars: The Achology Code of Ethics is the professional standard eve
  CARVE-OUT canonical          absent, and correct: page is noindex, so Rank Math withholds it by design. Verified at cutover, not here.
                               ^ DSRD 6 section 3.3 (amended S245)
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      42 checked, all resolve
  NOT-BUILT links-resolve      planned in DSRD 1, page not built yet: /academy/ (404); /academy/schools/ (404); /certification/ (404); /courses/ (404); /accreditation/ (404); /academy/neuro-linguistic-programming/ (404)
------------------------------------------------------------------------------
  PASS   23 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
```

All hairline, boundary-owner, header-to-content, width, H1 and gutter rows PASS, as on the Manifesto and for the same reason: 23 rows rather than 28 because this page carries one block boundary, not two.

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL on one acronym; otherwise the best in the family** | Dash check clean: 0 em, 0 en. **SoMAP is handled correctly, and better than on the Manifesto:** its only visible use is inside its own expansion, "issued by the Society of Modern Applied Psychology (SoMAP)", with no earlier bare use in a heading. That is the house form exactly. **The strictest rule in s1 is met.** DSRD 6 s1 says "the Code of Character and Conduct is written in full every time and is never abbreviated at all". This page names it twice and writes it in full both times, and "CCaC" appears zero times. On a page whose whole subject is two codes with similar names, that is the rule holding where it would be easiest to break. **The failure is PDF:** one use, in the button label "Download the PDF", never expanded. Under your S245 ruling that there is no everyday-abbreviation carve-out, it fails. s1's chrome carve-out does not reach it, because that covers the header, its dropdowns, the mobile overlay and the footer, and this is a page button. |
| **s2 Structure and headings** | **Pass** | One H1 ("Achology Code of Ethics"), six section H2s, and a "Related Questions" H2 for the `.help-popular` block (DSRD 8 s17). No skipped levels. Read alone the headings tell the page's story: what the framework is, the principles behind it, the two codes and how they differ, the twice-yearly training, the framework for practitioners, and how to start. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception, and one observation** | Title 58 characters, unique, inside the bound. Description 148 characters, unique, plain language. **The em dash in the OG alt text is gone**, fixed under your S246 extension and read back off this live page. **Observation, not raised as a defect:** the meta description uses "Issued by SoMAP" unexpanded. s1's front-door rule governs the page's visible text rather than metadata, so this is not a s1 failure, but a search or assistant result showing that line gives a stranger an unexplained acronym. Yours to judge; I am not calling it a fault. **Carve-out:** the canonical. **Exception:** OG imagery provision, site-wide. |
| **s4 Schema** | **WAITING ON RULING** | Emits `AboutPage`, `BreadcrumbList` and its three ListItems. Correct only if this is an About page rather than a policy page, and DSRD 3 s5.3 names it in neither row. Filed as `QUESTION__Which_DSRD_6_Row_Governs_The_Manifesto_And_Code_Of_Ethics.md`. Same question, same two pages. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1 section 2's "| /about/code-of-ethics/ | Ethical standards |", and `/code-of-ethics/` 301s to it. 2 One clear subject. 4 All 42 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb reads Home > About > Achology Code of Ethics, matching the `/about/` hierarchy. 8 Unique, and held cleanly against a page it could easily have collided with: this page is the professional code, the Code of Character and Conduct is the personal one, and the page states the difference rather than blurring it. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **WAITING ON RULING on the date line; pass on the rest** | Author line exempt under either candidate row. **Date line open:** no "Last updated" line, correct for an About page and a failure for a policy page; the page states "This code of professional conduct was adopted on 28 July 2022", an adoption date rather than a last-updated one. Same question file. **What passes regardless:** the answer sits in the delivered HTML in the open; the source is named and linked, and unusually the full source document is downloadable rather than summarised; accessibility tree clean, with 64 reachable focusable elements, zero positive tabindex, zero links or buttons without an accessible name, one `main`, one `h1`, no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **Pass on this page's own account; one chrome item outstanding by reference** | **Zero contrast failures** anywhere in the page, measured across every paragraph, list item, link, bold and emphasised run, heading, span, table cell and blockquote in `main`, with alpha compositing and the correct threshold for each size and weight. No off-white panel links on this page, so the page 6 finding does not reach it. Keyboard walk clean. `scroll-padding-top` 80px. Reflow at 320px: no horizontal overflow, no overflowing element. No forms. **Outstanding chrome item:** the footer column headings, by reference to the corrected finding. |
| **s8 Ease of use** | **Pass, one cosmetic finding** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone. Krug's trunk test passes. Nielsen's ten lenses: consistent with the family, breadcrumb the way back, no forms so no error states, and "Two Codes, Two Layers of Integrity" does the hardest job on the page well, which is stopping a reader confusing the two codes. **One cosmetic finding:** the "Download the PDF" button leads to a **19.95 MB** file, and the button does not say so. It carries `download` and it resolves correctly, so nothing is broken; but a reader on mobile data gets a 20 MB download from a button that reads like a page link. Cosmetic on this chapter's scale, cheap to fix by putting the size in the label, and the label is yours. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. The PDF's size is noted under s8 rather than here, since this chapter measures the page rather than files it links to. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32. Phone tier 32/32 per DSRD 7 s4.3 as amended S245. No unnamed value found. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 42 links resolve, **and I checked the one that matters most rather than trusting the count**: the handbook link returns HTTP 200, `application/pdf`, 19,954,519 bytes. The page offers a document and the document is really there. Checked for the Cookie Policy failure mode: this page makes no claims about how the site behaves. 3 Tracking not instrumented on the build ground. 4 Images: content images carry descriptive alt text, chrome icons deliberately `alt=""`. 5 **Kain has not confirmed this page at three widths in the walk's context**, and I cannot lean on the 2026-07-29 confirmation, because that pass measured a redirect. It should go in front of him at three widths, with the Manifesto, before either is called done. |
| **s12 Page-type exemptions** | **WAITING ON RULING** | Turns on the same question. |

---

## 3. Fixes made this pass

**None to the page.** The one defect is a button label, and Rule 8 puts every published word with you.

## 4. The policy family, complete

Nine of nine walked. Where they stand:

| Page | Its own open items |
|---|---|
| 1 Privacy Policy | none, three acronyms fixed and shipped this session |
| 2 Terms and Conditions | none |
| 3 Refund Policy | none, two acronyms fixed and shipped this session |
| 4 Cookie Policy | **two acronyms, and the consent mechanism that does not exist** |
| 5 Trust Statement | none |
| 6 Disclaimers | two acronyms, plus six links below the contrast bar on the off-white panel |
| 7 Accessibility Statement | one acronym, plus the Space keyboard claim |
| 8 Manifesto | one acronym ordering, plus the page-type ruling |
| 9 Code of Ethics | one acronym, plus the page-type ruling |

Four of the nine are now clean on their own account. The pattern held to the last page: nine pages, one template, one original sitting, and no two of them written to the same standard. Every fault found was invisible to every gate we own before this walk, and the two most serious, the cookie consent mechanism and the link colour on tinted panels, are not about these pages at all.

Two pages of the nine, the Manifesto and the Code of Ethics, had never been measured once. That is worth saying plainly, because their earlier records read as though they had been.

Next in the instruction's order: the Policies index, then About.

*No em or en dashes in this file; checked before writing.*
