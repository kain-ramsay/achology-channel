# RECORD: Trust Statement, chapter by chapter through DSRD 6

**From:** Claude Code, S230. **Date:** 2026-07-29. **Page:** https://achologytest.com/policies/trust-statement/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`. **Theme:** v0.36.33; record updated in place S043, 2026-08-03, on v0.36.35.

**Verdict: as ready as a build-site page can be.** Every chapter runnable from here has run and passes, and Kain confirmed the page at desktop, tablet and phone width on 2026-07-29. Still open: the cutover-only lines and Chat's rulings on the template-level items referred in §7 and §8. (The §7 walk and §8 fresh-eyes read ran 2026-07-29 in S042; their rows below carry the evidence. The rest of the record is the S230 run.)

## The machine gate first

`page_gate` v2 (the S233 ruling 8 amendment: hairline spacing measured from the geometrically nearest visible content edge, versioned in the script header), re-run S043, 2026-08-03, against the live page on v0.36.35 at desktop 1440, tablet 900 and phone 375: **28 pass, 1 fail.**

```
  FAIL  canonical          (missing)
  ---- 28 passed, 1 failed
```

The single failure is the site-wide missing canonical, which you have already ruled Rank Math configuration rather than page work. It is the same on all seven.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **Pass, with one recorded exception** | Zero em and en dashes on the rendered page, verified by the gate today after the sweep that removed them. The front-door rule's acronym test passes: the page spells terms in full. **Exception:** the house-copy checklist sign-off predates the checklist itself, so no sign-off record exists for copy written before it. Kain approved this copy; the record does not exist to cite. |
| §2 Structure and headings | **Pass** | One H1 ("Trust Statement"), 9 H2s, no skipped levels. Read alone the headings tell the page's story: they open with what the page covers, then run numbered sections in order. Matches the policy layout every other page in the family uses. |
| §3 Metadata | **Fail, one line** | Title 50 chars, unique, subject first. Description 143 chars. **Canonical absent**, which is the gate's single failure and is Rank Math configuration. Preview image is handled site-wide, per the standing ruling. |
| §4 Schema | **Pass** | Emits BreadcrumbList, ListItem, WebPage. Rank Math builds it; the theme adds nothing for this page type. Not run through Google's Rich Results Test, because the test fetches the URL and this site refuses automated fetches; **that line is unverified until cutover.** |
| §5 Search visibility | **Pass on six of eight, two recorded exceptions** | Address matches DSRD 1. One clear subject. Internal links present and all resolve (gate). Breadcrumb matches DSRD 1 §9's policy pattern, Home rendered as a house icon carrying `aria-label="Home"` rather than the word. **Exception 1:** indexing is `noindex, nofollow` because the whole build site sets `blog_public = 0`, which is correct for a build ground and cannot be verified as intended until cutover. **Exception 2:** the redirect map and the orphan check both belong to cutover, not to a build-site page. |
| §6 AI visibility | **Pass on the lines that apply** | Author line exempt for policy pages per §12; the date stays and is shown, reading "Last updated: 1 July 2026". The answer is in the delivered HTML, not behind a tab or a click. Sources are named where the copy leans on one. **Not verified:** the accessibility-tree audit needs Lighthouse against the live URL, which the host's bot protection refuses. |
| §7 Accessibility | **Walk run 2026-07-29 (S042): the page passes every check that is its own; three template-level items referred to Chat** | Keyboard walk on the rendered page: every interactive element reachable in DOM order, none invisible, no positive tabindex, closed menus and the phone drawer sealed out of the tab order, skip link first, the phone menu closes on Escape and hands focus back to its toggle. Focus visibility: a global 2px orange outline, keyboard only. Contrast measured on the rendered page: body text 10.5:1, inline links 4.7:1 and underlined, footer links 5.5:1, all inside AA. A 200 percent zoom equivalent and 320px reflow both hold: no horizontal overflow, nothing lost or clipped. Tap targets pass WCAG 2.2 target size under its inline-text and spacing exceptions. No forms on the page. **Referred items, two of three resolved S043 (2026-08-03, v0.36.35):** the sticky-header item is fixed site-wide (S233 ruling 1: scroll padding of the header height plus 8px; proven live, an anchor target that landed under the bar now lands clear of it); the date line left the fine-print grey for the AA soft grey per S233 ruling 4 and DSRD 7 section 1.1, verified on the live page; the footer buttons' announced state is ruled (S233 ruling 2) and waits only on QUESTION__Footer_Heading_Achology_Accent_Collision.md before it ships. |
| §8 Ease of use | **Walk run 2026-07-29 (S042) with fresh eyes in a new session, per this chapter's rule: pass, two cosmetic findings** | Krug's two checks at desktop and phone width: the page says at a glance what site it is, what page it is and where it sits (logo, breadcrumb, one H1, a plain-words opening); everything clickable looks clickable; the site carries no search by design, so the trunk test's search question does not arise. Nielsen's lenses: consistent with the policy family, the breadcrumb gives the way back, no forms so no error states, links answer hover and focus. **Findings, both cosmetic, the copy is Chat's and Kain's to amend:** two sentences read oddly where the dash sweep left a colon mid-sentence, in section 1 ("human behaviour: will inevitably provoke") and section 2 ("management: accepts no responsibility"). No blockers, no hindrances. |
| §9 Speed | **Not verified** | PageSpeed Insights fetches the URL from outside, and the host answers automated fetches with a challenge, so no measurement can be taken against this site. Verifiable at cutover, or on the representative-page basis DSRD 3 already allows. |
| §10 Visual consistency | **Pass** | `css_gate` passes on the stylesheet behind this page. Widths, gutters, H1 size and weight, hairline presence and spacing all measured by the gate at three widths today. 10 images, 0 without alt text. |
| §11 Live verification | **Pass on five of five** | Everything loads: the gate reports no failed asset. Every link resolves. Every image carries a description. **Item 5 closed 2026-07-29 (S042):** Kain was prompted to narrow the window, checked the page, and confirmed it at desktop, tablet and phone width; his words are on record in NOTE__Kains_Standard_Ruling_S042.md. |
| §12 Page-type exemptions | **Applied** | Policy pages are exempt from §6's author line; the date stays. Applied above. |

## What would close this page

1. The §7 accessibility walk and the §8 fresh-eyes read: run 2026-07-29 (S042), evidence in their rows above.
2. Kain's confirmation at all three widths: given 2026-07-29 (S042).
3. Three lines that cannot be closed on a build site at all: the canonical, the indexing intent, and the speed measurement. All three are cutover work, recorded as deferred rather than left looking like defects.
4. Two of the three referred template items closed S043, shipped in v0.36.35 and verified live (the sticky header and the date-line grey); the footer announcement waits on the accent question to Chat. The §8 copy corrections were applied S043 on v0.36.36 and verified on the live page, the page re-gated clean.

*No em or en dashes in this file; checked before writing.*