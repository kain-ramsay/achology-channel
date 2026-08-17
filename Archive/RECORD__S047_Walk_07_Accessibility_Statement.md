# RECORD: Accessibility Statement, page 7 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Page:** https://achologytest.com/policies/accessibility-statement/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_accessibility_statement.md` (S230 era).

**Verdict: the page is in far better shape than the walk's earlier findings made me expect, and its section 4 is the best-written thing I have read on this site.** Two defects: one acronym, and one of its four keyboard claims is not true. Neither is serious, and the reason neither is serious is that the page deliberately does not overclaim.

This is the page that makes promises about everything the walk has been measuring, so I tested its claims by driving the real page rather than reading its code.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. All hairline, boundary-owner, header-to-content, width, H1 and gutter rows PASS. The tail:

```
  PASS      meta-title         34 chars: Accessibility Statement | Achology
  PASS      meta-description   143 chars: Achology's accessibility statement explains how we work to m
  CARVE-OUT canonical          absent, and correct: page is noindex, so Rank Math withholds it by design. Verified at cutover, not here.
                               ^ DSRD 6 section 3.3 (amended S245)
  PASS      dashes             0 em, 0 en
  PASS      assets-load        nothing failed
  PASS      links-resolve      38 checked, all resolve
  NOT-BUILT links-resolve      planned in DSRD 1, page not built yet: /academy/ (404); /academy/schools/ (404); /certification/ (404); /courses/ (404); /accreditation/ (404); /academy/neuro-linguistic-programming/ (404)
------------------------------------------------------------------------------
  PASS   28 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
```

---

## 2. What I tested by driving the page

The page makes four keyboard claims. I pressed the keys.

| Claim | Result |
|---|---|
| Enter opens the menu | **True.** `aria-expanded` false to true, panel visible at opacity 1, its 7 links reachable, no navigation despite the trigger carrying a real href. |
| Escape closes it and returns focus to where you were | **True, in its strong form.** Menu hidden, `aria-expanded` back to false, panel links out of the tab order, and focus is on the trigger itself. |
| Tab moves through the links | **True.** 7 reachable open, 0 reachable closed. |
| **Space opens the menu** | **False.** Verified in the DOM and confirmed by screenshot. |

Filed as `FINDING__Accessibility_Statement_Claims_Space_Opens_The_Menu.md`, with the two honest fixes set out and neither chosen.

**A method note I owe you, because it nearly cost a false finding.** My first probe of the menu reported `visibility: hidden` after Enter, and I was one step from filing "the mega menu is not keyboard operable", which would have been alarming and wrong. The screenshot showed the menu plainly open. The probe was measuring the wrong instances of a three-instance component. DSRD 6 section 11's line is exactly right and I nearly proved it the expensive way: measurement is not verification. Every keyboard result above is confirmed on screen as well as in the DOM.

---

## 3. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL, one acronym** | Dash check clean: 0 em, 0 en. **Two acronyms are handled correctly and are the house form exactly:** "the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA" and "the Equality Advisory and Support Service (EASS)". AA and AAA are conformance levels inside the WCAG naming rather than separate acronyms, and are introduced by the WCAG expansion that precedes them. **HTML fails:** "Pages are built with semantic HTML" is the only use, and the full name appears nowhere on the page. Under your S245 ruling that there is no everyday-abbreviation carve-out, that is a fail. I note without arguing it that expanding it inside that particular sentence will read awkwardly, and the wording is yours either way. |
| **s2 Structure and headings** | **Pass** | One H1, one opening H2, nine numbered H2s, no skipped levels. Read alone the headings tell the page's story in the order a reader needs it: commitment, standard, what is built in, conformance status, known limitations, compatibility, how to report a problem, what to do if unsatisfied, and about the statement. The three trailing H2s are footer chrome. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception** | Title 34 characters, unique, subject in the first two words. Description 143 characters, unique, plain language. The em dash is gone, fixed under the S245 sweep and read back off this live page. **Carve-out:** the canonical, per DSRD 6 s3 row 3 as amended S245. **Exception:** preview image present and branded; OG imagery provision handled site-wide. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 All 38 internal links resolve, including `/enquiries/`, which is the contact form the page's section 7 points a reader to; six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9. 8 Unique. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest: "Last updated: 1 July 2026", with section 9 recording that it was prepared on 1 July 2026 and will be reviewed when the post-rebuild assessment completes and at least annually. That is the honest-date line done properly rather than minimally. The answer sits in the delivered HTML in the open. Accessibility tree clean, as measured above. |
| **s7 Accessibility** | **Pass on this page's own account; one chrome item outstanding by reference** | **Zero contrast failures** in the reading column, with primary text at 10.48 to 1. This page carries no off-white panel links, so the page 6 finding does not touch it. Keyboard walk clean and, unusually, driven rather than inspected: see section 2 above. Focus outline 2px brand orange, keyboard only. `scroll-padding-top` 80px. Reflow at 320px clean. No forms. **On the WCAG version pairing, which I checked before saying nothing about it:** the page commits to "WCAG 2.1 at Level AA" and says it monitors 2.2. DSRD 6 s7 records that pairing as deliberate, "the site promises the lower and holds itself to the higher, never the reverse... the pair is intentional, and no audit flags it as a contradiction". So it is not flagged. **Outstanding chrome item:** the footer column headings, by reference to the corrected finding. |
| **s8 Ease of use** | **Pass, no findings** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone. Krug's trunk test passes. Nielsen's ten lenses: consistent with the family, breadcrumb the way back, and section 7 gives a reader three routes to report a problem (email, telephone, a form) with a stated response time of two working days, which is the "help and documentation" lens done well rather than tokenistically. No blockers, no hindrances, no cosmetic findings. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32. Phone tier 32/32 per DSRD 7 s4.3 as amended S245. No unnamed value found. |
| **s11 Live verification** | **Fail on item 2, narrowly** | 1 No failed asset. 2 **Fail, on one claim.** Every link resolves. But this chapter tests the page against reality, and one of its four keyboard promises is not true: Space does not open the menus. The other three are true and were driven, not assumed. **The other claim worth testing here, and its verdict:** section 3 says "all body-length text uses a colour combination that passes WCAG AA". The page 6 finding measured six body links at 4.23 to 1 on the off-white panel, so that sentence is currently inaccurate site-wide, though not on this page, whose own text is clean. It is covered by `FINDING__Link_Orange_Fails_On_The_Off_White_Panel.md` and will become true again if the colour is corrected. 3 Tracking not instrumented on the build ground. 4 Images: 10, content images with descriptive alt, 7 chrome icons deliberately `alt=""`. 5 Kain's three-width confirmation stands. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 4. What deserves saying about section 4

This page's conformance section is the reason its two defects are minor rather than serious:

> "Until that assessment is complete, we do not claim full conformance; we claim the commitment and the standards described here, and we will publish an honest account of where the site stands once it has been verified."

Everything this walk has found, the link orange on tinted panels, the footer headings, is exactly what that sentence anticipates and reserves. A statement that had claimed conformance would now be contradicted by its own site. This one is not. Whoever wrote it left the right door open, and it is worth keeping that sentence intact when section 5 is eventually filled in.

## 5. What I need for this page

1. Approved wording for **HTML**, or a ruling that this instance is not worth expanding.
2. A choice between the two fixes for the Space claim.

That closes the seven legal policies. Pages 8 and 9, the Manifesto and the Code of Ethics, complete the policy family and carry the two OG alt texts already corrected under your S246 extension.

*No em or en dashes in this file; checked before writing.*
