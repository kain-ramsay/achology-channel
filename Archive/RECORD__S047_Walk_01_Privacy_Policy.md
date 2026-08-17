# RECORD: Privacy Policy, page 1 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.16.
**Page:** https://achologytest.com/policies/privacy-policy/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_privacy_policy.md` (S230, refreshed S043 on v0.36.35), which is three theme versions and four sweeps out of date.

**Verdict: the page itself is clean. Three defects found, none page-local, none fixable by Code.** Two are site-wide chrome failing the WCAG 2.2 AA bar this gate names. One is a dash-ban breach in metadata repeating across all eight policy-family pages. Each is filed as its own finding and named in the chapters below.

**Cache state of this run:** the gate now purges the server cache before it measures, per Kain's S245 ruling 9b, and prints the proof. This is the first record taken through `page_gate` v4.

---

## 1. The machine gates

`css_gate` on `policies.css`, the stylesheet behind this page, S047 on v0.38.16:

```
=== policies.css ===
  PASS
```

`page_gate` v4 against the live page at desktop 1440, tablet 900 and phone 375, S047 on v0.38.16:

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
  PASS      h1                 32px / 700 "Privacy Policy"
  PASS      gutters            desktop: 48 / 48 (want 48)
  PASS      gutters            tablet: 32 / 32 (want 32)
  PASS      gutters            mobile: 20 / 20 (want 20)
  PASS      meta-title         47 chars: Privacy Policy | How Achology Handles Your Data
  PASS      meta-description   143 chars: Achology's privacy policy explains what personal information
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

**Amended in place, same session.** This printout was first taken while `page_gate` still reported the canonical as a FAIL. Your `ANSWER__Canonicals_Sweeps_And_Collapse_S245.md` arrived mid-session, DSRD 6 s3 row 3 now carries the carve-out on disk, and the gate was corrected to take it (v5) and re-run against this page. The page did not change; the instrument was wrong and now is not. The machine gate on this page is clean.

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL, one line, referred to Chat** | Dash check clean in visible text: 0 em, 0 en, confirmed by `page_gate` and independently by a full body-text scan. Front-door identification of Achology's own terms passes: Achology Transactions Ltd is named in full where it first matters. **The acronym line fails.** Four acronyms carry their full name at first use and are correct (UK GDPR, EU GDPR, PECR, ICO). **Three appear bare and are never spelled out anywhere on the page: HMRC, CV and IT.** Chrome acronyms (CPD, IQ) are exempt under the s1 chrome carve-out and are not counted. Code cannot fix this: Rule 8 puts every published word with Chat. Filed as `FINDING__Three_Bare_Acronyms_On_The_Privacy_Policy.md`. |
| **s2 Structure and headings** | **Pass** | One H1 ("Privacy Policy"), one opening H2 plus 19 numbered H2s, 7 H3s, no skipped levels. Read alone the headings tell the page's story: what the page covers, who we are, what data, why, who it is shared with, how long, your rights, security, changes. The three trailing H2s (About, Achology Schools, Useful Links) are footer chrome, not page structure. Matches the shape the whole policy family carries. |
| **s3 Metadata** | **Fail, one line, plus two recorded exceptions** | Title 47 characters, unique, subject in the first two words. Description 143 characters, unique, reads as a sentence a person wrote. **New failure: the preview image's alt text carries an em dash**, and the same defect sits on all eight policy-family OG images, verified this turn by reading all eight live pages. DSRD 2 s3.0 names metadata explicitly in the ban. Filed as `FINDING__Em_Dash_In_Eight_Policy_OG_Image_Alt_Texts.md`. **Exception 1:** canonical absent by design, the settled S046 finding. **Exception 2:** the preview image itself is present and branded; OG imagery provision is handled site-wide and is not raised as a gap. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns this page type: "Reviews, Testimonials, Free Coaching, Free Events, AAA, Policy pages / WebPage / Rank Math auto / None needed / None". The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. Facts in the schema match the page. **Unverified line:** Google's Rich Results Test fetches the URL from outside and the host answers automated fetches with a challenge, so that one line waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 Internal links present, all 38 resolve, with six addresses DSRD 1 names but that are not built yet correctly reported NOT-BUILT rather than as failures. 5 Breadcrumb correct: DSRD 1 s9 pins "Policy page / Home > Policies > [Policy Name]" and the page renders Home (a house icon carrying `aria-label="Home"`) > Policies > Privacy Policy, chevron separators, every segment but the last a link. 8 Unique: no other page answers this question. **Exception 1** (line 3, indexing): `robots` reads `nofollow, noindex` because the build ground sets `blog_public = 0`; correct here, verifiable as intended only at cutover. **Exception 2** (lines 6 and 7): redirect map and orphan check are both cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt: DSRD 6 s12 exempts policy pages from "s6's author line, the date stays". The date is shown and honest: "Last updated: 1 July 2026". The page's answer sits in the delivered HTML, nothing behind a tab or a click. Sources are named and linked to the originals (UK GDPR and the Data Protection Act 2018 both link out to legislation.gov.uk). Accessibility tree measured directly this turn rather than by Lighthouse, which the host's bot protection refuses: 67 reachable focusable elements, **zero** with a positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, skip link first in the tab order, and all 28 zero-size focusables (closed dropdowns, phone drawer) confirmed sealed out of the tab order rather than merely hidden by size. |
| **s7 Accessibility** | **FAIL, two site-wide chrome items, referred to Kain** | **What passes, measured on the rendered page this turn:** keyboard walk clean; focus visibility intact; `scroll-padding-top` 80px, so the S233 sticky-header fix still holds; reflow at 320px with no horizontal overflow and no overflowing element, the lawful-basis table included; no forms. Contrast inside the reading column passes with room: body 10.48, H1 and H2 10.48, inline links 4.67 **and underlined** so colour is not the only signal, date line 5.47 at 13px, breadcrumb 5.47, header nav 10.48. **What fails, both in the footer (DSRD 8 s19), therefore on every page:** the four footer column headings measure **3.32 to 1** against the 4.5 their size and weight require; the "Start Your Trial" footer button measures **3.16 to 1** against the same 4.5. Alpha compositing applied, so these are true rendered ratios. Twenty-six footer strings measured, 24 pass, 2 fail. Filed as `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md`. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying this chapter's rule that "the walk is never run by the page's builder in the same sitting it was built". Krug's self-evidence question at desktop and phone: nothing makes a visitor stop and think, every link is underlined or plainly a link, labels use the reader's own words. Krug's trunk test: a stranger landing cold sees the logo, the breadcrumb, one H1 naming the page, and an opening sentence saying what the page is for; the site carries no search by design, so that limb does not arise. Nielsen's ten lenses: consistent with the policy family, breadcrumb always the way back, no forms so no error states, links answer hover and focus, the page carries only what serves. **The two cosmetic copy findings recorded at S042 were applied at S043 and are gone.** No blockers, no hindrances, nothing outstanding. |
| **s9 Speed** | **Not verified, deferred** | PageSpeed Insights fetches the URL from outside and the host answers automated fetches with a challenge, so no measurement can be taken against this site. DSRD 3 already allows certification on a representative page of each type; the full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`, the mechanical form of DSRD 7 s4.5's three-things rule: every value is a token, a named DSRD value, or an annotated one-off. Widths read 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32, all measured at three widths this turn. Smallest text in the reading column is 14px. No unnamed value found, so none of the three verdicts (collapse, name, record) was needed. |
| **s11 Live verification** | **Pass on four of five, item 5 standing** | 1 Everything loads: no failed asset. 2 Every link goes where it claims: 38 checked, all resolve; the six NOT-BUILT addresses are DSRD 1 plan, not defects. 3 Tracking: not instrumented on the build ground, cutover work. 4 Images: 10 on the page, the 3 content images all carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately, which is correct for a decorative icon beside its own text label; filenames are plain words (`nlp.webp`, `life-coaching.webp`, `person-centred.webp`). 5 Kain confirmed this page at desktop, tablet and phone on 2026-07-29 and nothing page-local has changed since; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. Applied in s6 above. No other exemption taken. |

---

## 3. Fixes made this pass

**None to the page.** Every defect found belongs to someone else by rule:

1. The three bare acronyms are page copy, and Rule 8 puts every published word with Chat.
2. The footer contrast failures are locked chrome colours, and Rule 5 puts the remedy with Kain.
3. The em dash in the OG alt texts is metadata text in the media library, again Rule 8, and it spans eight pages, so it needs its own signed sweep brief under Rule 3.

One instrument change did land this session, under its own declaration and its own commit: `page_gate` v4, the cache purge, built to Kain's S245 ruling 9b and proved by the purge line in the printout above.

This is the walk working rather than stalling. Page 1 produced three real defects, two of which were invisible to every gate we own, because no gate reads metadata strings and no gate composites alpha before measuring contrast.

---

## 4. What I need back

1. Replacement copy for the three bare acronyms, in the house form.
2. Kain's ruling on the two footer contrast failures.
3. A signed sweep brief for the eight OG alt texts, or Chat's replacement strings.

Page 2, Terms and Conditions, starts now. It shares this page's template and stylesheet, so items 2 and 3 will recur there and will be cross-referenced rather than re-argued.

*No em or en dashes in this file; checked before writing.*
