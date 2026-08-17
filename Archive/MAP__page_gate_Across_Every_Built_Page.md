# MAP: page_gate across every built page

**From:** Claude Code, S230. **Date:** 2026-07-28. **Answers:** `00__ANSWERS__Walk_Order_Check3_And_Breadcrumb_Hairline.md` section 1, and item 4 of your S229 rulings.
**Read only. No page was touched, nothing was fixed.**

**This file replaces both earlier versions filed today.** Two things changed under it and both are documented beside it: the checker had a measurement fault, corrected and reported in `REPORT__The_Spacing_Drift_Was_The_Checker.md`, and Kain ruled the breadcrumb question outright, recorded verbatim in `NOTE__Kains_Ruling_No_Hairline_At_The_Top_Of_A_Page.md`. The numbers below are the corrected run with his ruling applied.

Every published page on achologytest.com, measured in a real browser at desktop 1440, tablet 900 and phone 375. Twenty three pages, the whole built set: the seven legal policies, the Manifesto, the Code of Ethics, the Policies index, About, Our People, the ten people profiles, and Testimonials.

**421 checks pass, 172 fail, nothing is left open for review.** 23 of the failures are the site wide canonical, one per page, which you have already ruled out of page work. That leaves 149 real rows.

## The table, worst first

| Page | Passed | Failed |
|---|---|---|
| /testimonials/ | 18 | 21 |
| /about/instructors/ | 14 | 13 |
| /about/instructors/isabella-whitmore/ | 13 | 11 |
| /about/instructors/frederick-martin/ | 13 | 11 |
| /about/instructors/declan-fitzpatrick/ | 13 | 11 |
| /about/instructors/charlotte-avery/ | 13 | 11 |
| /about/instructors/benjamin-lockwood/ | 13 | 11 |
| /about/instructors/jackson-hartley/ | 14 | 10 |
| /about/instructors/evelyn-montgomery/ | 14 | 10 |
| /about/instructors/amelia-sinclair/ | 14 | 10 |
| /about/instructors/gerard-egan/ | 14 | 10 |
| /about/instructors/kain-ramsay/ | 14 | 10 |
| /about/ | 17 | 8 |
| /about/code-of-ethics/ | 18 | 4 |
| /about/manifesto/ | 18 | 4 |
| /policies/ | 18 | 4 |
| /policies/accessibility-statement/ | 26 | 2 |
| /policies/disclaimers/ | 26 | 2 |
| /policies/trust-statement/ | 26 | 2 |
| /policies/cookie-policy/ | 26 | 2 |
| /policies/terms-and-conditions/ | 26 | 2 |
| /policies/privacy-policy/ | 26 | 2 |
| /policies/refund-policy/ | 27 | 1 |

## What is failing, by kind

| Check | Failing rows | What it is |
|---|---|---|
| hairline-present | 119 | a block boundary with no hairline at all, on pages built before the separator was locked |
| canonical | 23 | no canonical tag. Site wide, already ruled Rank Math configuration and not a page defect |
| hairline-spacing | 16 | a hairline present but not at 48 above and 48 below, 32 on phone |
| dashes | 7 | em or en dashes in the live copy, which the house standard bans outright |
| meta-title | 5 | a title longer than the 60 character limit |
| boundary-owner | 2 | spacing at a boundary declared outside any component DSRD 8 names |

## Group one: the seven legal policies are structurally at standard

Every one passes every structural check: hairlines present, 48 above and below at desktop and tablet, 32 on phone, widths, gutters, H1, header gap, assets, links, and now the top of the page under Kain's ruling. What is left on them is copy:

- **Em and en dashes in live copy.** Privacy policy 43 em dashes, cookie policy 19, trust statement 12, terms and conditions 11, disclaimers 5 plus 3 en dashes, accessibility statement 5. About carries 6 en dashes. All of it predates the ban, and all of it is baked into the theme rather than held in WordPress, so it is mine to sweep page by page.
- **The refund policy has no defect at all** beyond the site wide canonical. It is the first page in the built set to reach that state.

## Group two: About, the Policies index, the Manifesto, the Code of Ethics

A handful of rows each: a missing hairline at one or two boundaries, some spacing off, plus About's en dashes. Each needs its own pass.

## Group three: the people pages and Testimonials

The ten profiles and Our People have no hairline at any boundary at all. They are not drifted; they were built before the separator existed, so this is adding what was never there. Five profiles also carry a meta title over 60 characters: Isabella Whitmore 61, Frederick Martin 61, Benjamin Lockwood 61, Charlotte Avery 64, Declan Fitzpatrick 67.

Testimonials is furthest from the standard, expected of the newest page with its own layout, and the only page where a boundary spacing is declared outside any component DSRD 8 names.

## Page by page, every failing row

### /testimonials/

18 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 2 (policy-header policy-heade | tm-heading): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (tm-heading | tm-intro): no hairline, gap 8.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 4 (tm-intro | tm-filter): no hairline, gap 24.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 5 (tm-filter | lite-grid): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-spacing`: desktop boundary 6 (lite-grid | policy-body policy-body--r): 72.0 above, 49.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: desktop boundary 7 (policy-body policy-body--r | policy-body policy-body--r): 119.5 above, 81.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: tablet boundary 2 (policy-header policy-heade | tm-heading): 78.0 above, 48.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-present`: tablet boundary 3 (tm-heading | tm-intro): no hairline, gap 8.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 4 (tm-intro | tm-filter): no hairline, gap 24.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 5 (tm-filter | lite-grid): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-spacing`: tablet boundary 6 (lite-grid | policy-body policy-body--r): 72.0 above, 49.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: tablet boundary 7 (policy-body policy-body--r | policy-body policy-body--r): 115.4 above, 81.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: mobile boundary 2 (policy-header policy-heade | tm-heading): 353.0 above, 48.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-present`: mobile boundary 3 (tm-heading | tm-intro): no hairline, gap 8.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 4 (tm-intro | tm-filter): no hairline, gap 24.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 5 (tm-filter | lite-grid): no hairline, gap 32.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-spacing`: mobile boundary 6 (lite-grid | policy-body policy-body--r): 56.0 above, 33.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: mobile boundary 7 (policy-body policy-body--r | policy-body policy-body--r): 71.0 above, 57.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `boundary-owner`: desktop boundary 3: lastOfA_marginBottom 8px, declared by *, ::before, ::after in base.css  (DSRD 7 §4.3, declared outside any DSRD 8 component)
- **FAIL** `boundary-owner`: desktop boundary 4: lastOfA_marginBottom 24px, declared by *, ::before, ::after in base.css  (DSRD 7 §4.3, declared outside any DSRD 8 component)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | pp-header): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (pp-header | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 4 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | pp-header): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (pp-header | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 4 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | pp-header): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (pp-header | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 4 (pp-group | pp-group): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/isabella-whitmore/

13 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `meta-title`: 61 chars: Isabella S. Whitmore | TAYA Copywriting Specialist | Acholog  (DSRD 6 §3.1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/frederick-martin/

13 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `meta-title`: 61 chars: Frederick S. Martín | Content Lead For Wise Quotes | Acholog  (DSRD 6 §3.1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/declan-fitzpatrick/

13 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `meta-title`: 67 chars: Declan Fitzpatrick | Copywriter For Articles And Content | A  (DSRD 6 §3.1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/charlotte-avery/

13 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `meta-title`: 64 chars: Charlotte J. Avery | Research Copywriter For Articles | Acho  (DSRD 6 §3.1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/benjamin-lockwood/

13 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `meta-title`: 61 chars: Benjamin Lockwood | Lead For Book Research Content | Acholog  (DSRD 6 §3.1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/jackson-hartley/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/evelyn-montgomery/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/amelia-sinclair/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/gerard-egan/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/instructors/kain-ramsay/

14 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: desktop boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 1 (ap-crumb | ap-hero): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (ap-hero | ap-bio): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 3 (ap-bio | help-articles): no hairline, gap 56.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/

17 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-spacing`: desktop boundary 3 (policy-body policy-body--r | policy-body policy-body--r): 48.0 above, 81.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: tablet boundary 2 (policy-header policy-heade | policy-body policy-body--r): 78.0 above, 48.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: tablet boundary 3 (policy-body policy-body--r | policy-body policy-body--r): 48.0 above, 81.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: mobile boundary 2 (policy-header policy-heade | policy-body policy-body--r): 353.0 above, 48.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: mobile boundary 3 (policy-body policy-body--r | policy-body policy-body--r): 48.0 above, 73.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 0 em, 6 en  (house standard)

### /about/code-of-ethics/

18 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /about/manifesto/

18 passed. The rest:

- **FAIL** `hairline-present`: desktop boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: tablet boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `hairline-present`: mobile boundary 2 (policy-header policy-heade | policy-body policy-body--r): no hairline, gap 48.0px  (DSRD 7 §4.3 ruling 1)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /policies/

18 passed. The rest:

- **FAIL** `hairline-spacing`: desktop boundary 2 (policy-header | policy-index): 49.0 above, 73.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: tablet boundary 2 (policy-header | policy-index): 49.0 above, 73.0 below (want 48/48)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `hairline-spacing`: mobile boundary 2 (policy-header | policy-index): 33.0 above, 57.0 below (want 32/32)  (DSRD 7 §4.3 ruling 4)
- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

### /policies/accessibility-statement/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 5 em, 0 en  (house standard)

### /policies/disclaimers/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 5 em, 3 en  (house standard)

### /policies/trust-statement/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 12 em, 0 en  (house standard)

### /policies/cookie-policy/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 19 em, 0 en  (house standard)

### /policies/terms-and-conditions/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 11 em, 0 en  (house standard)

### /policies/privacy-policy/

26 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)
- **FAIL** `dashes`: 43 em, 0 en  (house standard)

### /policies/refund-policy/

27 passed. The rest:

- **FAIL** `canonical`: (missing)  (DSRD 6 §3.3)

## How check 4 was implemented, for your confirmation

Your ruling: "fail only on spacing declared outside a DSRD 8 component ... You do not judge 'owner'; you read where the spacing is declared." The checker reads the CSS rule that declares each contribution at a boundary and asks one mechanical question: does that selector name a class DSRD 8 names? The list is read out of DSRD 8 on every run, never held in the script, the same way the planned URLs are read out of DSRD 1. Fifty three component classes come back from the document today. DSRD 7 section 4.3 carries the same carve-out in its own words: "It does not govern rules inside a DSRD 8 component (a card footer, a card's stats row, the header's bottom border, the footer's internal lines), which keep their own specified values."

Two honest limits. Where several rules declare the same property the checker takes the last match, which is the cascade's order only at equal specificity, so a reported selector can be one the winner overrode. And DSRD 8 names classes unevenly, so a component the document describes without naming its class reads as outside a component. Both are pointers to look, not proof.

## Where the walk stands

Kain has set the order: the policy family first. On this map that is a copy sweep across seven pages plus About, since their structure is already right, and the refund policy needs nothing. The people pages are the real body of work and are the same shape repeated eleven times. Testimonials is its own piece.

Nothing here has been fixed. Nothing will be outside a declared page pass.

*No em or en dashes in this file; checked by the gate, not by eye.*