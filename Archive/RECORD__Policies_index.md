# RECORD: the Policies index, chapter by chapter through DSRD 6

**From:** Claude Code, S048. **Date:** 2026-08-06. **Page:** https://achologytest.com/policies/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`, page 10 in its order. **Theme:** v0.38.52.

**Verdict: one copy fail, which is Chat's to fix. Everything else runnable on a build site passes.** Nothing was changed on this page: the walk found nothing at page level that a written standard fails.

**Updated in place later the same session.** The walk found a second failure, the site header not fitting between 768px and 879px, which was template rather than page. Kain ruled the fix in session on the rendered options, it shipped as v0.38.53, and he confirmed the result at phone, iPad and laptop width. The §7, §8 and §11 rows below are updated accordingly, and the only thing still open on this page is the "Achologist" copy line.

## The machine gate first

`page_gate` v5 against the live page, cache purged before measuring, at desktop, tablet and phone: **28 pass, 0 fail, 1 not built yet, 1 carved out.**

```
  PASS   28 passed, 0 failed, 0 for review, 1 not built yet, 1 carved out
  cache-purge  dynamic cache purged before measuring
  CARVE-OUT canonical   absent, and correct: page is noindex (DSRD 6 3.3, amended S245)
  NOT-BUILT links-resolve  planned in DSRD 1, not built yet: /academy/, /academy/schools/,
                           /certification/, /courses/, /accreditation/,
                           /academy/neuro-linguistic-programming/
```

Hairlines, boundary ownership, header-to-content, both widths, H1 32/700, gutters at all three tiers, meta title and description, dashes, assets and 40 links all pass.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **FAIL, one term** | Zero em and en dashes on the rendered page (gate). No acronyms appear, so the acronym step does not arise. **The fail:** the Code of Ethics card reads "The expected level of character and behaviour that every practising Achologist pledges to uphold." "Achologist" is named word for word in §1's own list of terms that must be identified at first use, and the page never identifies it. A stranger arriving cold from a search result is left holding a word they cannot fill in, which is exactly what the front-door rule exists to stop. **The fix is copy, so it is Chat's and Kain's, not mine (Rule 8).** Everything else on the page identifies itself: the governance paragraph names the owners, the companies and what binds them, and each of the nine cards says what its document covers. |
| §2 Structure and headings | **Pass** | Built order matches DSRD 9 §31.1 item by item: sticky header, breadcrumb (home icon linking to /, then "Policies"), H1 plus lead, governance paragraph, hairline, "Our Legal Policies" plus seven cards in the locked order (Privacy, Terms and Conditions, Cookie, Refund, Trust Statement, Disclaimers, Accessibility Statement), hairline, "Our Training Standards" plus two cards, rainbow stripe and footer. Nothing extra: no closing CTA panel and no sales content, as §31.1 requires. Read alone, the headings tell the page's story: one H1, two H2s. |
| §3 Metadata | **Pass, canonical carved out** | Title 51 chars, unique, subject in the first words. Description 147 chars, plain language. Canonical absent and correct: the page is noindex, so Rank Math withholds it by design (DSRD 6 §3.3 carve-out, S245). Preview image handled site-wide per the standing ruling. |
| §4 Schema | **Pass, one line unverified** | Emits `CollectionPage` and `BreadcrumbList`, which is what a structural index page should carry. **Not run through Google's Rich Results Test:** the test fetches the URL from outside and the host answers automated fetches with a challenge. Unverified until cutover, as on every page in this walk. |
| §5 Search visibility | **Pass on six of eight, two recorded exceptions** | Address `/policies/` matches DSRD 1 §2.6 row 1 exactly. One clear subject. Internal links present, all 40 resolve (gate); the nine document links go to the exact addresses DSRD 9 §31.1 names, including the two `/about/` ones. Breadcrumb matches DSRD 1 §9. Not orphaned: the footer links to it site-wide. Uniquely answers its question. **Exception 1:** indexing reads `nofollow, noindex` because the build site sets `blog_public` 0; correct here, verified at cutover. **Exception 2:** the redirect map belongs to cutover. |
| §6 AI visibility | **Pass on the lines that apply** | Structural pages are exempt from §6's author and date lines per §12. The answer sits in the delivered HTML, in the open, not behind a tab or a click. No claim on the page rests on an outside source, so nothing needs citing. Accessibility tree: all ten focusable elements carry an accessible name, the nine cards are real links, and nothing interactive is invisible to the tree. **Not verified:** the Lighthouse agent-readiness audit needs the live URL and the host refuses it. |
| §7 Accessibility | **Pass at page level; one template failure recorded below** | Ten focusable elements, all reachable, all named, none unnamed. Contrast measured on the rendered page: the lowest two values are 5.36:1 (breadcrumb current page, and the orange Achology accent in the H1), everything else 10.48:1. All above the 4.5 AA bar; both lowest values are the darkened link orange shipped this session. 200 percent zoom equivalent (640px): no horizontal scroll, nothing overflows, all nine cards present and readable. No forms on the page. **The template failure, now closed:** between 768px and 879px the page scrolled sideways. It was the site header, not this page, and it affected every page. Kain ruled the fix in session and it shipped as v0.38.53: the mobile menu now takes over up to 880px. Re-measured live at 375, 768, 800, 879, 880 and 1440, sideways scroll gone at every one, and the menu proven to open. See `RULING__Mobile_Nav_Triggers_At_880_Not_768_S048.md`. |
| §8 Ease of use | **Pass at all three widths, the tablet hindrance now fixed** | Krug's self-evidence and trunk tests at desktop and phone width: the page says at a glance what site this is, what page you are on and where it sits; the nine cards are unmistakably clickable; every label uses the reader's plain words. Nielsen's lenses: consistent with the policy family it gates, the breadcrumb is always the way back, no forms so no error states, the page carries only what serves its one job. **The one hindrance found, now fixed:** a visitor on an iPad held upright met a page that slid sideways under their thumb. Ruled and shipped the same session as v0.38.53; re-measured clean. **Fresh-eyes note:** this walk ran in the same session as this page's only change, but that change was site-wide colour, not this page's layout or copy, so the builder-and-walker overlap §8 warns about does not touch what was read. |
| §9 Speed | **Not verified** | PageSpeed Insights fetches from outside and the host refuses it. Verifiable at cutover, or on DSRD 3's representative-page basis. Unchanged from every earlier record. |
| §10 Visual consistency | **Pass** | `css_gate` passes on policies.css and on every stylesheet this page loads. Widths (1200 page, 880 article), gutters at all three tiers, H1 32/700, hairline presence, and 48/48 desktop and tablet with 32/32 phone, all measured by the gate. The ghost word behind each card renders at desktop and tablet and is correctly absent below 768, as DSRD 9 §31.2 specifies. |
| §11 Live verification | **Pass on five of five** | Everything loads: the gate reports no failed asset. Every link resolves, and the six that do not are addresses DSRD 1 plans and nobody has built, which the gate reports as NOT-BUILT rather than as failures. Images carry their descriptions. Tracking is not yet assigned for this page type. **Item 5 closed, 2026-08-06:** Kain was shown this page in real viewports of 375, 768 and 1200 and confirmed all three. His words: "yes, they do, they look very good". His approval covers all three widths, per this item's own wording. |
| §12 Page-type exemptions | **Applied** | The Policies index is a structural page: exempt from §6's author and date lines. Applied above. |

## What would close this page

1. **Chat writes an identification for "Achologist"** into the Code of Ethics card line, and Kain approves it. Copy is not mine to draft.
2. ~~The header overflow is fixed.~~ **Closed the same session:** Kain ruled it in session, it shipped as v0.38.53, and it is verified live across the whole band.
3. ~~Kain confirms the page at tablet and phone width.~~ **Closed 2026-08-06**, all three widths.
4. Three lines that cannot close on a build site at all: the canonical, the indexing intent and the speed measurement. All cutover work, recorded as deferred rather than left looking like defects. A fourth, the Rich Results Test, is refused by the host and joins them.

*No em or en dashes in this file; checked before writing.*
