# RECORD: Trust Statement, page 5 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Page:** https://achologytest.com/policies/trust-statement/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_trust_statement.md` (S230 era).

**Verdict: the cleanest page in the walk so far. Nothing page-local fails.** Machine gate clean, every chapter that can pass does pass, and it is the first page with no acronym failure of any kind: it carries no body acronyms at all. The only thing standing against it is the site-wide footer contrast, recorded by reference.

**One judgement call is shown rather than hidden**, in s1 below. I want it checked rather than taken on trust.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. All hairline, boundary-owner, header-to-content, width, H1 and gutter rows PASS, as on pages 1 to 4. The tail:

```
  PASS      meta-title         50 chars: Trust Statement | Our Commitment to You | Achology
  PASS      meta-description   138 chars: Read Achology's trust statement: our commitment to honesty,
  CARVE-OUT canonical          absent, and correct: page is noindex, so Rank Math withholds it by design. Verified at cutover, not here.
                               ^ DSRD 6 section 3.3 (amended S245)
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      37 checked, all resolve
  NOT-BUILT links-resolve      planned in DSRD 1, page not built yet: /academy/ (404); /academy/schools/ (404); /certification/ (404); /courses/ (404); /accreditation/ (404); /academy/neuro-linguistic-programming/ (404)
------------------------------------------------------------------------------
  PASS   28 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
```

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **Pass, with one judgement stated openly for checking** | Dash check clean: 0 em, 0 en. **The acronym rule passes outright, and this is the first page where it does so with nothing to argue about: the reading column contains no acronym at all.** Every acronym my scan returned (ALL, BIG, CPD, FREE, ICO, IQ, LIVE) is in the header or footer, covered by s1's chrome carve-out, and the ICO label now matches DSRD 8 s19's registered string word for word after this session's fix. **The judgement, which I want you to check rather than accept:** s1 also requires plain-English terms naming something of Achology's to be identified at first use, and names "a member, the membership, the community" among them. This page uses "community" nine times and "members" twice. I have recorded it as a pass, and here is the reasoning so you can overturn it: the first appearance reads "Achology operates as a collaborative learning community. This means: members learn with and from one another", which names the thing and says what it is in the sentence where it first appears, and "members" arrives immediately afterwards as members of the community just identified. The reader is not left holding a word they cannot fill in, which is the test the chapter sets. If you read it as a fail, say so and it becomes a copy item like the others; I would rather be corrected than have quietly widened the rule. |
| **s2 Structure and headings** | **Pass** | One H1 ("Trust Statement"), one opening H2 ("What This Trust Statement Covers"), seven numbered H2s, and a closing "Final Position" H2. No H3s, no skipped levels. Read alone the headings tell the page's argument, which is unusual for a policy page and to its credit: responsibility first, then offence and ideas, then emotional self-management, then boundaries, then shared responsibility, then the limits of what education guarantees, then the relationship, then where that leaves things. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception** | Title 50 characters, unique, subject in the first two words. Description 138 characters, unique, plain language. **The em dash is gone**, fixed under the S245 sweep and read back off this live page: "Achology's trust statement: an ancient handwritten scroll lit in amber against a dark background". **Carve-out:** the canonical, per DSRD 6 s3 row 3 as amended S245. **Exception:** preview image present and branded; OG imagery provision handled site-wide. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 All 37 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9: Home (house icon, `aria-label="Home"`) > Policies > Trust Statement. 8 Unique, and genuinely so: this page states a philosophical position no other page on the site states, which is the strongest form of the uniqueness test rather than the weakest. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest. The answer sits in the delivered HTML in the open, with no collapsed sections. Accessibility tree measured this turn: 55 reachable focusable elements, **zero** positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **FAIL, by reference only, on the two site-wide chrome items; the page itself is clean** | Recorded by reference per your S245 item 5. **Measured on the rendered page this turn:** **zero** contrast failures anywhere in the reading column, across paragraphs, list items, links, bold and emphasised runs, headings, blockquotes and the H1, tested with alpha compositing against the correct threshold for each size and weight. Keyboard walk clean. `scroll-padding-top` 80px. Reflow at 320px: no horizontal overflow, no overflowing element. No forms, no tables. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone. Krug's trunk test: logo, breadcrumb, one H1, and an opening that states the page is "our working philosophy, written down", which tells a cold arrival exactly what they are reading and why it exists. Nielsen's ten lenses: consistent with the policy family, breadcrumb the way back, no forms so no error states, and the page carries only what serves. This is the page in the family with the least mechanical content and the most argument, and the numbered structure keeps it navigable. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32, all measured at three widths. Phone tier 32/32, conforming to DSRD 7 s4.3 as amended S245. No unnamed value found, so none of s10's three verdicts was needed. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 37 links resolve; the six NOT-BUILT addresses are DSRD 1 plan. **I checked this page specifically for the failure mode found on the Cookie Policy**, that is, statements about how the site behaves that are not true of it. This page makes none: it states positions and commitments, not mechanisms, so there is nothing here of the kind that failed page 4. 3 Tracking not instrumented on the build ground, cutover work. 4 Images: 10, the 3 content images carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately; filenames plain words. 5 Kain's three-width confirmation stands; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 3. Fixes made this pass

**None needed.** Nothing on this page fails a written standard.

Two things that landed on this page came from elsewhere in the session and are proved above: the OG alt text is clean, and the footer's ICO credential now carries its registration number.

## 4. Where this leaves the family

Five of the nine policy-family pages walked. Three are clean on their own account (Terms and Conditions, Trust Statement, and now Privacy Policy and Refund Policy after their fixes shipped). One is not (the Cookie Policy, waiting on the consent decision).

The pattern I flagged at page 3 continues to hold: the pages were never written to one standard, and the only way to know which is which is to open each one. Trust Statement needed nothing at all; the Cookie Policy needs a decision with legal weight. Same family, same template, same day's work originally.

Page 6, the Disclaimers, starts now.

*No em or en dashes in this file; checked before writing.*
