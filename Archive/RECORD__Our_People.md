# RECORD: Our People, chapter by chapter through DSRD 6

**From:** Claude Code, S049. **Date:** 2026-08-06. **Page:** https://achologytest.com/about/instructors/
**Answers:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`, page 4 in its order. **Theme:** v0.38.61, `page_gate` v6.

**Verdict: the page had no block separators at all and now has them. Two copy fails remain, both Chat's, and one component-registration question that DSRD 6 §10 routes to DSRD 8.**

## What changed, and the line each fix implements

One change, in `people.css`, the page's own stylesheet.

**The separators.** The page ran three people groups and a header with no hairline at any boundary and a page-local 56px gap. DSRD 7 §4.3 ruling 1: *"A hairline separates every pair of blocks. There is no block boundary anywhere on the site without one."* Ruling 2, which is why the 56 is gone rather than kept: *"Where a page sets its own spacing values, those declarations are deleted so the page inherits this standard. A page-local variant is a defect."*

`.pp-group` now carries `border-top`, with `margin-top` the space above the line and `padding-top` the space below, per §4.3's one-owner rule: *"If it carries border-bottom, its padding-bottom is the space above the line and its margin-bottom is the space below; if border-top, the mirror."* The phone tier is hand written on the rule rather than taken from the token, per the S245 amendment.

## The machine gate

**Before:** 14 pass, **12 fail**. Every boundary at every tier reported no hairline.

**After:** 26 pass, 6 fail. Every hairline row passes at all three tiers:

```
  PASS  hairline-present  desktop boundary 1 (ap-crumb | pp-header): breadcrumb junction, no line, correct
  PASS  hairline-spacing  desktop boundary 2 (pp-header | pp-group): 48 above, 48 below
  PASS  hairline-spacing  desktop boundary 3 (pp-group | pp-group):  48 above, 48 below
  PASS  hairline-spacing  desktop boundary 4 (pp-group | pp-group):  48 above, 48 below
  PASS  hairline-spacing  tablet  boundaries 2 to 4: 48 above, 48 below
  PASS  hairline-spacing  mobile  boundaries 2 to 4: 32 above, 32 below
  PASS  hairline-edges    no line at page top or bottom
  cache-purge  dynamic cache purged before measuring
```

**Two of the twelve were my instrument, not the page.** This page names its breadcrumb `ap-crumb`; the gate's breadcrumb-junction test matched only `/breadcrumb/`, so it was telling me a hairline was missing at the top of the page, which is the one place Kain has ruled a line must never be drawn (S230). The test now matches `/crumb/`, which covers all three names the theme uses. A check that depends on a naming convention fails silently the first time a page names something else, and this is the second instrument defect this session found by walking a page rather than reading a file.

## The six that remain, and why they are one question

All six are the same row, repeated across three boundaries and two properties:

```
  FAIL  boundary-owner  desktop boundary 2: firstOfB_marginTop 48px, declared by .pp-group in people.css
                        ^ DSRD 7 §4.3, declared outside any DSRD 8 component
```

The check is Chat's S227 ruling, implemented mechanically: it reads DSRD 8 for class names and fails spacing declared by a selector DSRD 8 does not name. `.pp-group` is not in DSRD 8. So the gate is not saying the spacing is wrong; it measures 48/48 and passes it. It is saying this block is unregistered.

That is DSRD 6 §10's own routing: *"Whether a repeated arrangement of those values has earned promotion from a page-local block to a named component is DSRD 8's question, raised here whenever a block appears on a page for the second time, and settled there."* The block appears three times on this page and is the same arrangement as `.help-group` in `help.css`. **So the question is whether the people group and the help group are one component, and it is yours.** I cannot register it: Rule 8, Code never edits a DSRD.

## The twelve chapters

| Chapter | Verdict | Evidence |
|---|---|---|
| §1 Copy standards | **FAIL, two acronyms** | Zero em and en dashes (gate). **CTO** appears twice, in Kain's role line and in his bio line, and "Chief Technology Officer" appears nowhere on the page. **TAYA** appears once, in Isabella S. Whitmore's role, and is never expanded. DSRD 6 §1: "An acronym may be used only after its full canonical name has already appeared in the page's visible text, with the acronym in brackets at that first appearance." Both are copy, so both are Chat's and Kain's (Rule 8). Karen's role line is the model of what is wanted: it writes "Chief Executive Officer" in full. Nothing else on the page leaves a term unfilled; "Achologist" does not appear here at all. |
| §2 Structure and headings | **Pass** | H1 "Our People", then three group headings: Achology Management Team, Achology Course Instructors, Achology Editorial Team. Read alone they tell the page's story. Twelve cards across the three groups, each a person with photo, name, role and one-line bio. |
| §3 Metadata | **Pass, canonical carved out** | Title 55 chars, unique. Description 142 chars, plain language. Canonical absent and correct: noindex build ground (DSRD 6 §3.3 carve-out, S245). Preview image is the sitewide default per the standing ruling. |
| §4 Schema | **Pass, one line unverified** | `CollectionPage` and `BreadcrumbList`, which is what a hub page should carry and what DSRD 10 §9 decision (d) ruled at S219. Rich Results Test not runnable: the host refuses the outside fetch. |
| §5 Search visibility | **Pass on six of eight, two recorded exceptions** | Address `/about/instructors/` matches DSRD 1. One clear subject. All 50 links resolve (gate); six more are DSRD 1 addresses nobody has built. Breadcrumb correct. Not orphaned: About and the footer both link here. **Exceptions:** indexing intent and the redirect map, both cutover. |
| §6 AI visibility | **Pass on the lines that apply** | About pages are exempt from §6's author and date lines per §12. Every bio sits in the delivered text, in the open. 63 focusable elements, every one named, none unnamed. Lighthouse agent-readiness not runnable against this host. |
| §7 Accessibility | **Pass** | 63 focusable elements, all reachable and named. Seven photographs, each carrying the person's name as its description, each with a plain-words filename keyed to the person's slug. No forms. Measured at 375, 640 and 800: no horizontal scroll and nothing overflowing at any of them. |
| §8 Ease of use | **Pass at desktop and phone** | Krug: the page says at a glance what it is and where it sits; every card is unmistakably a link to a person. Nielsen: consistent with the About family, breadcrumb always the way back, no error states, carries only what serves. **Fresh-eyes caveat, stated rather than glossed:** this walk ran in the same session as this page's only change. That change was the block separators, so the thing I changed is the thing I am least able to read cold. The separators are machine-verified at 48/48 and 32/32 rather than judged by my eye, and the look of them is on Kain's list below. |
| §9 Speed | **Not verified** | PageSpeed Insights is refused by the host. Verifiable at cutover, or on DSRD 3's representative-page basis. |
| §10 Visual consistency | **FAIL, and it is not this page's doing** | `css_gate` fails on `people.css`, on three 640px breakpoints that are not system boundaries. All three predate this session and this change set. §4.5's mechanism for legitimising them is an annotation naming an **approved** exception, and the approval is Kain's, not mine, so I have not written one. Filed as `QUESTION__People_CSS_640px_Stack_Points_S049.md`. Everything else measured passes: widths, gutters, H1 32/700, and the separators at both tiers. |
| §11 Live verification | **Pass on four of five; item 5 waiting on Kain** | The gate reports no failed asset and all 50 links resolving. Every photograph carries a plain-words filename and a description. Tracking not yet assigned for this page type. **Item 5 open:** Kain has not been asked to confirm the page at tablet and phone width, and on this page that ask matters more than usual, because the separators are new. |
| §12 Page-type exemptions | **Applied** | Our People is an About page: exempt from §6's author and visible date lines. Applied above. |

## What would close this page

1. **Chat writes the CTO and TAYA expansions**, and Kain approves them. Copy is not mine to draft. Karen's "Chief Executive Officer" is the pattern already on the page.
2. **A ruling on the three 640px stack points**, filed separately. It is the only thing standing between this page and a clean CSS gate.
3. **A DSRD 8 decision on the group block:** is `.pp-group` the same component as `.help-group`, and does it get registered? Six gate rows turn on it and it is §10's own routing question.
4. **Kain confirms the page at tablet and phone width**, and looks at the new separators.
5. Three lines that cannot close on a build site: the canonical, the indexing intent and the speed measurement. Plus the Rich Results Test, refused by the host.

*No em or en dashes in this file; checked before writing.*
