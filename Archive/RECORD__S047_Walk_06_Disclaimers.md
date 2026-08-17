# RECORD: Disclaimers, page 6 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Page:** https://achologytest.com/policies/disclaimers/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_disclaimers.md` (S230 era).

**Verdict: two failures, one of them the first page-local accessibility failure the walk has found.** The machine gate passes. Six links inside this page's own reading column are below the AA contrast bar, and two acronyms are unexpanded, one of them in the page's crisis-signposting sentence.

This page also caused a correction to an earlier finding of mine, filed separately and summarised at the end.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. All hairline, boundary-owner, header-to-content, width, H1 and gutter rows PASS. The tail:

```
  PASS      meta-title         48 chars: Disclaimers | Important Legal Notices | Achology
  PASS      meta-description   130 chars: Read Achology's legal disclaimers covering our courses, cont
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

Second page in a row where the gate passes and the chapters do not. That gap is the walk's whole justification.

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL, two acronyms, copy needed from Chat** | Dash check clean: 0 em, 0 en. **UK fails on ordering.** Its first appearance is at character 1,806, "In the UK: call 999 in an emergency"; "United Kingdom" does appear on the page but at character 6,439, in section 10, **after** the short form. DSRD 6 s1 requires the full name to have "already appeared in the page's visible text" at first use, so order is the test and this page fails it. **NHS fails outright:** one use, at character 1,844, and "National Health Service" appears zero times. **The context matters and is worth stating:** both sit in the page's crisis-signposting sentence, which is the single most important sentence on the page. In its favour, the signposting itself is well built and I want that on the record: it says "In the UK:" before the numbers, and immediately follows with "Outside the UK, contact your local emergency services or a crisis line in your country", so a reader abroad is not left with numbers that cannot help them. The defect is narrow: a reader who does not know what NHS stands for meets it in a sentence written for someone in distress. |
| **s2 Structure and headings** | **Pass** | One H1 ("Disclaimers"), one opening H2, twelve numbered H2s, and a closing "Final Position" H2. No skipped levels. Read alone the headings tell the page's story: purpose, then educational scope, then what this is not (therapy, medical, mental health), then responsibility, offence, outcomes, certification, community, external links, accuracy, audience, reliance, and how these disclaimers sit with the others. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception** | Title 48 characters, unique, subject in the first word. Description 130 characters, unique, plain language. **The em dash is gone**, fixed under the S245 sweep and read back off this live page. **Carve-out:** the canonical, per DSRD 6 s3 row 3 as amended S245. **Exception:** preview image present and branded; OG imagery provision handled site-wide. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 All 37 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9: Home (house icon, `aria-label="Home"`) > Policies > Disclaimers. 8 Unique. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest. The answer sits in the delivered HTML in the open. Accessibility tree measured this turn: 62 reachable focusable elements, **zero** positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **FAIL, and page-local this time** | **This is the first page in the walk whose own reading column fails.** Six links inside the section 12 cross-reference table measure **4.23 to 1** against the 4.5 their 15px size requires. The cause is not a page-local mistake: the links carry `--color-orange-link` #C64E14, which is the correct system value, and the table cells carry `--color-off-white` #F3F4F4, also correct. The colour clears 4.5 on white **by 0.17** and goes under as soon as any tint sits behind it. DSRD 7 s1 states "#C64E14 clears 4.5:1" without naming a background, which is what licensed this. Filed as `FINDING__Link_Orange_Fails_On_The_Off_White_Panel.md`, and it is general to the site rather than local to this page. **Everything else on the page passes:** the nine body links on white measure 4.67 and are underlined; keyboard walk clean; `scroll-padding-top` 80px; reflow at 320px with no horizontal overflow and the table reflowing to `display: block` inside the column; no forms. **Chrome:** see the correction below. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone. Krug's trunk test: logo, breadcrumb, one H1, and an opening that states what the disclaimers are for. Nielsen's ten lenses: consistent with the family, breadcrumb the way back, no forms so no error states. The crisis signposting appears early rather than buried, which on this page is the single most important usability judgement and it is made correctly. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32. Phone tier 32/32, conforming to DSRD 7 s4.3 as amended S245. Every value on the page is a named system value, which is precisely why s7 failed: the failure is in what the system names, not in what this page did with it. That distinction is why s10 passes and s7 does not, and it is worth keeping separate. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 37 links resolve. Checked specifically for the Cookie Policy failure mode, statements about site behaviour that are not true: this page makes none, and its one operational claim, the crisis numbers, is correct and correctly bounded by country. 3 Tracking not instrumented on the build ground, cutover work. 4 Images: 10, the 3 content images carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately; filenames plain words. 5 Kain's three-width confirmation stands; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 3. Fixes made this pass

**None.** Both defects are outside my hands: the copy is Rule 8's, and a palette value is Kain's.

## 4. A correction I owe you, caused by this page

Reading DSRD 7 for the link colour took me to section 5.1, and there I found that **one of the two footer contrast items I filed at page 1 is a recorded, Kain-approved exception**, which the document says in terms exists "so audits stop re-flagging it". I re-flagged it. `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md` has been rewritten in full: the "Start Your Trial" button is withdrawn, and the four column headings are restated as a ruled position (DSRD 8 s19, S235) whose stated reason measurement contradicts, rather than as an open design question.

The cause was mine and it is the one Rule 4 names: I quoted my measurement instead of the spec, and filed before reading the section that governed it. The measurements were right both times; the framing was wrong. Section 7's chrome reference in the records for pages 1 to 5 now points at one item rather than two, and no page's own verdict changes.

## 5. What I need for this page

1. Approved wording for the first use of **UK** and the single use of **NHS**, the latter in the crisis-signposting sentence, where the wording deserves care rather than a mechanical expansion.
2. The DSRD 7 s1 correction and then Kain's call on the link orange, per the separate finding.

Page 7, the Accessibility Statement, starts now. Given what this page found, that page will get particular attention: it is the one page on the site that makes explicit promises about accessibility, and this walk has now measured two places where the site does not meet the bar it holds itself to.

*No em or en dashes in this file; checked before writing.*
