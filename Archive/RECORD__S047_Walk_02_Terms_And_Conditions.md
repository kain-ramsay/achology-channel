# RECORD: Terms and Conditions, page 2 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.16.
**Page:** https://achologytest.com/policies/terms-and-conditions/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_terms_and_conditions.md` (S230 era).
**Read with:** `RECORD__S047_Walk_01_Privacy_Policy.md`. This page shares that page's template, stylesheet and chrome, so the site-wide findings are cross-referenced rather than re-argued.

**Verdict: the page passes its machine gate outright, and its own copy and structure are clean.** Its acronym handling passes where the Privacy Policy's failed, and it is the model for the fix page 1 needs. Three defects stand against it, all three chrome or metadata rather than the page: two carried from page 1, one new and found here.

**This is the first page in the walk to return a clean machine gate**, because your S245 canonical carve-out landed mid-session and `page_gate` was corrected to take it. Until that correction every one of the 25 built pages read FAIL for a reason that is not a defect.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5 against the live page at desktop 1440, tablet 900 and phone 375, S047 on v0.38.16, cache purged before measurement:

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
  PASS      h1                 32px / 700 "Terms and Conditions"
  PASS      gutters            desktop: 48 / 48 (want 48)
  PASS      gutters            tablet: 32 / 32 (want 32)
  PASS      gutters            mobile: 20 / 20 (want 20)
  PASS      meta-title         31 chars: Terms and Conditions | Achology
  PASS      meta-description   146 chars: Read the Terms and Conditions for using Achology, including
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
| **s1 Copy standards** | **Pass on the page's own copy; fail on one chrome label** | Dash check clean: 0 em, 0 en in visible text. **The acronym rule passes on this page's copy, and passes well:** ATL is introduced as "Achology is the trading name of Achology Transactions Ltd (ATL), Scottish company number SC697126", which is the house form exactly. UK also passes: I checked the order rather than assuming it, and "United Kingdom" appears at character 30,650 of the visible text, before the first bare "UK" at 30,782, so the full name precedes the short form as the rule requires for an outside term in common public use. Front-door identification passes: the page names the entity, its company number and its jurisdiction in plain words. **The one failure is a chrome label, not this page's copy:** the sub-footer's ICO credential renders "ICO Registered" where DSRD 8 s19 registers "Registered with the ICO · ZB662679". Since s1's chrome carve-out works by testing chrome labels word for word against DSRD 8's registered strings, this label fails that test. Filed as `FINDING__Footer_ICO_Credential_Does_Not_Match_DSRD_8_19.md`, with the fix already written. |
| **s2 Structure and headings** | **Pass** | One H1 ("Terms and Conditions"), one definitions H2 plus 14 numbered H2s, 18 H3s, no skipped levels. Read alone the headings tell the page's story end to end: definitions, who we are, the contract, what is sold, prohibitions, both sides' rights to change and to end, refunds, statutory rights, liability, other terms, final provisions. The three trailing H2s are footer chrome, not page structure. |
| **s3 Metadata** | **Fail, one line, plus one carve-out and one exception** | Title 31 characters, unique, subject in the first three words. Description 146 characters, unique, plain language. **Failure: `og:image:alt` carries an em dash.** Same defect as page 1 and on all eight policy-family images; DSRD 2 s3.0 names metadata explicitly in the ban. Cross-referenced to `FINDING__Em_Dash_In_Eight_Policy_OG_Image_Alt_Texts.md`, where all eight strings are listed. **Carve-out, no longer an exception I have to argue:** the canonical row is formally carved out by DSRD 6 s3 row 3 as amended S245, and the gate now records it as such. **Exception:** preview image present and branded; OG imagery provision handled site-wide, not raised as a gap. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 All 38 internal links resolve, six DSRD 1 addresses correctly reported NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9's "Home > Policies > [Policy Name]": Home (house icon, `aria-label="Home"`) > Policies > Terms and Conditions. 8 Unique. **Exception 1:** indexing `nofollow, noindex` from `blog_public = 0`, correct on the build ground, verified at cutover under the same S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest: "Last updated: 1 July 2026". The answer sits in the delivered HTML, nothing behind a tab or a click. Accessibility tree measured directly this turn: 69 reachable focusable elements, **zero** positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, and every zero-size focusable confirmed sealed out of the tab order rather than merely hidden by size. |
| **s7 Accessibility** | **FAIL, on the two site-wide chrome items only; the page itself is clean** | **Measured on the rendered page this turn:** every string in the reading column passes its required ratio, with **zero** contrast failures across paragraphs, list items, links, headings and the H1, tested with alpha compositing and against the correct threshold for each size and weight. Keyboard walk clean. `scroll-padding-top` 80px, so the S233 sticky-header fix holds. Reflow at 320px: no horizontal overflow, no overflowing element. No forms and no tables on this page. **The failure is the footer, inherited, not page-local:** the four column headings at 3.32 to 1 and the "Start Your Trial" button at 3.16 to 1, both against the 4.5 required. Filed at page 1 as `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md`; no page can pass s7 while it stands. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying this chapter's fresh-eyes rule. Krug's self-evidence question at desktop and phone: nothing makes a visitor stop and think. Krug's trunk test: logo, breadcrumb, one H1 and a plain opening line ("Please read these terms and conditions before making a purchase") tell a cold arrival where they are and what the page is for. Nielsen's ten lenses: consistent with the policy family, breadcrumb always the way back, no forms so no error states, and the numbered structure makes a long legal document navigable, which is this page's real usability risk and it is handled. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32, all measured at three widths this turn. The phone tier reads 32/32 at both boundaries, which conforms to DSRD 7 s4.3 as amended at S245: the phone tier is hand written per separator on the component's own rule, and this template's separators carry it rather than relying on a token reduction that does not exist. No unnamed value found. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 No failed asset. 2 All 38 links resolve; the six NOT-BUILT addresses are DSRD 1 plan. The ICO credential's outbound link was checked against DSRD 8 s19 and is exactly right, even though its visible label is not. 3 Tracking not instrumented on the build ground, cutover work. 4 Images: 10, the 3 content images carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately as decorative icons beside their own labels; filenames plain words. 5 Kain's three-width confirmation of 2026-07-29 stands and nothing page-local has changed; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 3. Fixes made this pass

**None to the page.** Nothing on this page fails a written standard. Three defects stand, all chrome or metadata:

1. Footer contrast, awaiting Kain (filed page 1).
2. OG alt em dash, awaiting Chat or a sweep brief (filed page 1).
3. The ICO credential label, new this pass, fix already written and awaiting one line of authorisation.

One instrument change landed under its own declaration and commit: `page_gate` v5, taking your S245 canonical carve-out. Page 1's record is amended to match.

Worth saying plainly: this page's own copy passed the chapter page 1 failed, and it passed because the copy does the identification properly. It is the model for the three fixes page 1 needs.

Page 3, the Refund Policy, starts now.

*No em or en dashes in this file; checked before writing.*
