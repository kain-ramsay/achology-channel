# RECORD: Refund Policy, page 3 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.16.
**Page:** https://achologytest.com/policies/refund-policy/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_refund_policy.md` (S230 era).
**Read with:** `RECORD__S047_Walk_01_Privacy_Policy.md` and `..._02_Terms_And_Conditions.md`. Shared template, stylesheet and chrome, so site-wide findings are cross-referenced rather than re-argued, per your S245 item 5.

**Verdict: machine gate clean; structure, layout and accessibility all clean on the page's own account. One copy failure, and your S245 ruling settles that it is a failure rather than a debate.** This page uses UK four times and US once, and spells out neither, anywhere.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement:

```
  PASS      hairline-present   desktop boundary 1 (policy-breadcrumb | policy-header): breadcrumb junction, no line, correct
  PASS      hairline-spacing   desktop boundary 2 (policy-header | policy-body): 48 above, 48 below
  PASS      hairline-spacing   desktop boundary 3 (policy-body | policy-endnote): 48 above, 48 below
  PASS      hairline-present   tablet boundary 1 (policy-breadcrumb | policy-header): breadcrumb junction, no line, correct
  PASS      hairline-spacing   tablet boundary 2 (policy-header | policy-body): 48 above, 48 below
  PASS      hairline-spacing   tablet boundary 3 (policy-body | policy-endnote): 48 above, 48 below
  PASS      hairline-present   mobile boundary 1 (policy-breadcrumb | policy-header): breadcrumb junction, no line, correct
  PASS      hairline-spacing   mobile boundary 2 (policy-header | policy-body): 32 above, 32 below
  PASS      hairline-spacing   mobile boundary 3 (policy-body | policy-endnote): 32 above, 32 below
  PASS      hairline-edges     no line at page top or bottom
  PASS      boundary-owner     desktop boundary 2: lastOfA_marginBottom 48px, declared by .policy-page:not(.policy-page--404) .policy- in policies.css
  PASS      boundary-owner     desktop boundary 2: lastOfA_paddingBottom 48px, declared by .policy-page:not(.policy-page--404) .policy- in policies.css
  PASS      boundary-owner     desktop boundary 3: firstOfB_marginTop 48px, declared by .policy-body .policy-endnote, .policy-endnot in policies.css
  PASS      boundary-owner     desktop boundary 3: firstOfB_paddingTop 48px, declared by .policy-body .policy-endnote, .policy-endnot in policies.css
  PASS      header-to-content  desktop: 48.0px (want 48)
  PASS      header-to-content  tablet: 48.0px (want 48)
  PASS      header-to-content  mobile: 32.0px (want 32)
  PASS      content-width      page-container: 1200px
  PASS      content-width      article-container: 880px
  PASS      h1                 32px / 700 "Refund Policy"
  PASS      gutters            desktop: 48 / 48 (want 48)
  PASS      gutters            tablet: 32 / 32 (want 32)
  PASS      gutters            mobile: 20 / 20 (want 20)
  PASS      meta-title         47 chars: Refund Policy | Achology Courses and Membership
  PASS      meta-description   117 chars: Achology's refund policy sets out when you can request a ref
  CARVE-OUT canonical          absent, and correct: page is noindex, so Rank Math withholds it by design. Verified at cutover, not here.
                               ^ DSRD 6 section 3.3 (amended S245)
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      38 checked, all resolve
  NOT-BUILT links-resolve      planned in DSRD 1, page not built yet: /academy/ (404); /academy/schools/ (404); /certification/ (404); /courses/ (404); /accreditation/ (404); /academy/neuro-linguistic-programming/ (404)
                               ^ DSRD 1 URL table
------------------------------------------------------------------------------
  PASS   28 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
```

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL, one line, copy needed from Chat** | Dash check clean: 0 em, 0 en. Front-door identification of Achology's own terms passes: the page names Achology.com and its defined short forms in its opening paragraph. **The acronym line fails, twice.** Counted in document order over the visible text: **UK appears four times**, always as "your statutory rights under UK consumer law", and **"United Kingdom" appears zero times on the page**. **US appears once**, as "Refunds are made in US dollars, the currency in which you paid", and **"United States" appears zero times**. Neither is ever expanded. Your S245 ruling settles this: DSRD 6 s1 stands as written and everyday abbreviations are not exempted, so both fail. This differs from page 2, where I checked the order and "United Kingdom" genuinely did precede the short form; here there is nothing to precede it. Chrome acronyms are handled under s1's chrome carve-out and the separate ICO finding. Code cannot fix this: Rule 8 puts every published word with Chat. Copy requested below. |
| **s2 Structure and headings** | **Pass** | One H1 ("Refund Policy"), two opening H2s ("Our Approach to Refunds", "This Refund Policy at a Glance") plus 12 numbered H2s, no H3s, no skipped levels. Read alone the headings tell the page's story honestly, and tell it in both directions: the guarantee, then what is not refundable, then what happens after the window, then how to ask. The at-a-glance H2 is a genuine reader service on a page people arrive at worried. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Fail, one line, plus one carve-out and one exception** | Title 47 characters, unique, subject in the first two words. Description 117 characters, unique, plain language, comfortably inside the bound. **Failure: `og:image:alt` carries an em dash.** Cross-referenced to `FINDING__Em_Dash_In_Eight_Policy_OG_Image_Alt_Texts.md`; your S245 item 3 authorises the sweep and this page is one of the eight named in it. **Carve-out:** the canonical, per DSRD 6 s3 row 3 as amended S245. **Exception:** preview image present and branded; OG imagery provision handled site-wide. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject, tightly held: this page answers "can I get a refund" and nothing else. 4 All 38 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9: Home (house icon, `aria-label="Home"`) > Policies > Refund Policy. 8 Unique, and worth noting it stays unique despite Terms and Conditions carrying its own refunds section: that section is the contractual statement, this page is the reader-facing answer, and the two do not compete for the same search. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest: "Last updated: 1 July 2026". The answer is in the delivered HTML in the open, and on this page that matters more than most: the at-a-glance summary is plain text, not a collapsed block, so an assistant asked "does Achology refund" reads the answer immediately. Accessibility tree measured this turn: 62 reachable focusable elements, **zero** positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **FAIL, by reference only, on the two site-wide chrome items; the page itself is clean** | Recorded by reference per your S245 item 5, not re-argued. **Measured on the rendered page this turn:** **zero** contrast failures anywhere in the reading column, across paragraphs, list items, links, bold runs, headings and the H1, tested with alpha compositing and against the correct threshold for each size and weight. Keyboard walk clean. `scroll-padding-top` 80px. Reflow at 320px: no horizontal overflow, no overflowing element. No forms, no tables. **The failure is `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md`**, deferred to the mega menu and footer design session. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's self-evidence question at desktop and phone: nothing makes a visitor stop and think. Krug's trunk test: a cold arrival gets logo, breadcrumb, one H1 and an opening line stating plainly "when refunds are available, when they are not, and how to request one". Nielsen's ten lenses: consistent with the policy family, breadcrumb the way back, no forms so no error states. This is the page most likely to be read by someone already annoyed, and the at-a-glance block answers them before the detail does, which is the right order. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32, all measured at three widths. Phone tier reads 32/32, conforming to DSRD 7 s4.3 as amended S245 (hand written per separator, not from a token reduction that does not exist). No unnamed value found. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 38 links resolve; six NOT-BUILT are DSRD 1 plan. 3 Tracking not instrumented on the build ground, cutover work. 4 Images: 10, the 3 content images carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately; filenames plain words. 5 Kain's three-width confirmation of 2026-07-29 stands, nothing page-local changed since; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 3. Fixes made this pass

**None to this page.** Its one page-local defect is copy, which is yours. The three jobs you authorised in `ANSWER__S047_Walk_Batch_All_Items_S245.md` (the acronym expansions on page 1, the eight-page OG alt sweep, and the ICO credential string) are being applied now, in their own declared change sets, and are reported separately.

---

## 4. What I need for this page

Two approved phrases, in the same form as the three you approved for page 1:

1. The first appearance of **UK**, in "Nothing here reduces your statutory rights under UK consumer law" (the page's opening paragraph). The three later uses may then stay as UK alone.
2. The single appearance of **US**, in "Refunds are made in US dollars, the currency in which you paid".

The three-page pattern so far, which is worth recording as evidence that the ruling was the right call: page 1 had three bare, page 2 had none, page 3 has two. One family, one template, three different standards of compliance. Expect the remaining four legal policies to vary the same way, and I will report each rather than assume the family is uniform.

Page 4, the Cookie Policy, starts now.

*No em or en dashes in this file; checked before writing.*
