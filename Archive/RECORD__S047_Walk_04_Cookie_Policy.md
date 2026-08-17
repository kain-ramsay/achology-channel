# RECORD: Cookie Policy, page 4 of the S047 walk, chapter by chapter through DSRD 6

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.17.
**Page:** https://achologytest.com/policies/cookie-policy/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`
**Supersedes:** `RECORD__Policy_cookie_policy.md` (S230 era).

**Verdict: this page fails, and not on anything a gate could see. It describes a cookie banner and a footer cookie-settings link, and neither exists.** Everything mechanical about the page is clean: gates pass, layout conforms, accessibility inside the reading column is clean, and the two data tables reflow properly at phone width. The failure is that the page is not true.

Filed in full as `FINDING__The_Cookie_Policy_Describes_A_Consent_Mechanism_That_Does_Not_Exist.md`. It needs a decision with legal weight and is not mine to make.

---

## 1. The machine gates

`css_gate` on `policies.css`: **PASS**.

`page_gate` v5, live page at desktop 1440, tablet 900 and phone 375, cache purged before measurement. Full row set identical in shape to pages 1 to 3 (all hairline, boundary-owner, header-to-content, width, H1, gutter and asset rows PASS); the tail, which is where this page differs:

```
  PASS      meta-title         41 chars: Cookie Policy | How Achology Uses Cookies
  PASS      meta-description   124 chars: Achology's cookie policy explains what cookies we use, why w
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

The gate passes this page. That is the point worth sitting with: a page can pass every mechanical check we own and still tell a reader something untrue about how the site works.

**The OG alt text on this page now reads clean**, proving the S245 sweep on the live page: "Achology's cookie policy: an ancient handwritten scroll lit in amber against a dark background".

---

## 2. The twelve chapters

| Chapter | Verdict | Evidence, read from the page and the documents this turn |
|---|---|---|
| **s1 Copy standards** | **FAIL, two acronyms, copy needed from Chat** | Dash check clean: 0 em, 0 en. **UK appears three times and "United Kingdom" appears zero times on the page.** **GDPR appears once, in "UK GDPR", and "General Data Protection Regulation" appears zero times on the page.** The second is the sharper miss: the Privacy Policy expands it properly, this page does not, and DSRD 6 s1's whole premise is that "every page is a front door" and no page "may assume a term was learned on another page". Per your S245 ruling there is no everyday-abbreviation carve-out, so both fail. PECR is handled correctly and needs nothing: the page writes "the Privacy and Electronic Communications Regulations" in full and never uses the short form. **The ICO chrome label now passes**, reading "Registered with the ICO · ZB662679" after this session's fix, which is DSRD 8 s19's registered string word for word. |
| **s2 Structure and headings** | **Pass** | One H1 ("Cookie Policy"), one opening H2 plus 8 numbered H2s, no H3s, no skipped levels. Read alone the headings tell the page's story: what cookies are, how we use them, which ones, your consent, how to manage them, third parties, changes, questions. **One thing I checked rather than reported:** my text extraction rendered the opening H2 as "Cookies on Achology .com", which looks like a spacing defect. It is not. The markup is `<h2>Cookies on <span class="policy-next__accent">Achology</span>.com</h2>`, which renders as "Cookies on Achology.com" with Achology in orange, correctly following the standing rule that Achology is accented inside any heading. The space was my own tool's artifact, and I opened the markup rather than filing a false finding. |
| **s3 Metadata** | **Pass, plus one carve-out and one exception** | Title 41 characters, unique, subject in the first two words. Description 124 characters, unique, plain language. **The em dash is gone**, fixed under the S245 sweep and read back off the live page. **Carve-out:** the canonical, per DSRD 6 s3 row 3 as amended S245. **Exception:** preview image present and branded; OG imagery provision handled site-wide. This is the first page in the walk with a fully clean s3. |
| **s4 Schema** | **Pass** | DSRD 3 s5.3 assigns policy pages WebPage from Rank Math auto with no custom properties. The page emits exactly WebPage plus the site-wide BreadcrumbList and its three ListItems, and nothing the map does not name. **Unverified line:** Rich Results Test needs an external fetch the host refuses; waits for cutover. |
| **s5 Search visibility** | **Pass on six of eight, two recorded exceptions** | 1 Address matches DSRD 1's `/policies/[policy-name]/`. 2 One clear subject. 4 All 38 internal links resolve, six DSRD 1 addresses correctly NOT-BUILT. 5 Breadcrumb matches DSRD 1 s9: Home (house icon, `aria-label="Home"`) > Policies > Cookie Policy. 8 Unique. **Exception 1:** indexing under the S245 carve-out. **Exception 2:** redirect map and orphan check are cutover work. |
| **s6 AI visibility** | **Pass on the lines that apply** | Author line exempt (DSRD 6 s12, policy pages, "the date stays"). Date shown and honest: "Last updated: 1 July 2026". Sources linked to originals, and well: the browser-management links go to Apple, Google, Microsoft and Mozilla's own support pages rather than to a summary of them, which is exactly what this chapter's line 3 asks for. The answer sits in the delivered HTML in the open. Accessibility tree measured this turn: 64 reachable focusable elements, **zero** positive tabindex, **zero** links or buttons without an accessible name, one `main`, one `h1`, no zero-size focusable leaking into the tab order. |
| **s7 Accessibility** | **FAIL, by reference only, on the two site-wide chrome items; the page itself is clean** | Recorded by reference per your S245 item 5. **Measured on the rendered page this turn:** **zero** contrast failures anywhere in the reading column, including inside both data tables, tested with alpha compositing against the correct threshold for each size and weight. Keyboard walk clean. `scroll-padding-top` 80px. **Reflow at 320px, which matters more on this page than any other so far because it carries two data tables:** no horizontal overflow, no overflowing element, and both tables reflow to `display: block` inside the column at 280px wide rather than forcing a sideways scroll. The named 640px stack exception in `policies.css` is doing exactly the job DSRD 7 s4.5 records it for. Both tables use `<th>` header cells in their first row, which satisfies the programmatic-association requirement for a simple table; adding `scope="col"` would be belt and braces rather than a fix, so it is noted, not raised. No forms. |
| **s8 Ease of use** | **Fail, one hindrance** | Run this session on a page built in an earlier one, satisfying the fresh-eyes rule. Krug's two checks pass at desktop and phone: the page says what it is, everything clickable looks clickable, the plain-language opening does real work on a subject most sites make impenetrable. Nielsen's lenses find one genuine violation, and it is a **hindrance** on this chapter's three-level scale, not a cosmetic: the page tells the reader to "reopen the cookie settings via the link in the site footer", the reader goes to the footer, and there is no such link. A visitor following the page's own instruction reaches a dead end. That is the "consistency between the system and the real world" lens failing, and it is the usability face of the finding filed separately. No blockers. |
| **s9 Speed** | **Not verified, deferred** | External fetch refused by the host; representative-page basis per DSRD 3; full sweep is cutover work. |
| **s10 Visual consistency** | **Pass** | `css_gate` PASS on `policies.css`. Widths 1200 and 880, gutters 48/32/20, H1 32px/700, hairline presence and spacing 48/48/32, all measured at three widths. Phone tier 32/32, conforming to DSRD 7 s4.3 as amended S245. No unnamed value found. |
| **s11 Live verification** | **FAIL on item 2** | 1 Everything loads: no failed asset. 2 **Fail.** Every link on the page resolves, but this chapter's test is whether the page's promises hold on the running site, and three of the page's factual claims do not: there is no cookie banner, no footer cookie-settings link, and no consent preference cookie. The missing Google Analytics cookies are correct and expected on a build ground and are not counted against the page. Filed as `FINDING__The_Cookie_Policy_Describes_A_Consent_Mechanism_That_Does_Not_Exist.md`. 3 Tracking not instrumented on the build ground, cutover work. 4 Images: 10, the 3 content images carrying descriptive alt text, the 7 mega-menu school icons carrying `alt=""` deliberately; filenames plain words. 5 Kain's three-width confirmation stands for the layout; the prompt stands for his next look. |
| **s12 Page-type exemptions** | **Applied** | Policy pages: exempt from s6's author line, the date stays. No other exemption taken. |

---

## 3. Fixes made this pass

**None to this page.** Its two defects are copy and site machinery, both outside Rule 8 and Rule 5 respectively.

What did land on this page came from elsewhere in the session: the OG alt em dash is gone, and the footer's ICO credential now carries its registration number. Both are read back off this live page above.

## 4. What I need for this page

1. Approved wording for the first use of **UK** and the single use of **GDPR**, in the same form as the five already approved.
2. A decision on the consent mechanism: build it, or rewrite the policy to match the site. Until one of them happens this page cannot pass, and it is the only page in the walk so far whose failure is about substance rather than form.

Page 5, the Trust Statement, starts now, after I apply the two Refund Policy phrases and the two remaining OG alt texts you approved at S246.

*No em or en dashes in this file; checked before writing.*
