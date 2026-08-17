# REPORT: every built page, what is finished and what is not

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.60.0.
**Commissioned by:** Kain, in session, in these terms: no new building, wrap up and polish every page, and guarantee schema on every page, alt text and metadata on every image, and a DSRD 6 pass on every page.
**Measured, not recalled.** 22 pages read from the live site tonight.

## The three guarantees he asked for, answered honestly

**Alt text: yes, I can guarantee it.** 22 pages, 342 images between them, **zero missing an alt attribute.** Decorative images carry an empty alt correctly and content images carry real descriptions. This is the one of the three that is genuinely finished.

**Schema on every page: no.** One real gap. `/testimonials/` emits **no JSON-LD at all**, and DSRD 10's map assigns it WebPage plus BreadcrumbList, the same pair `/reviews/` carries. That is a defect and it is mine to fix. `/learn/` and `/cards/` also emit none: `/cards/` is an internal reference sheet rather than a public page and is legitimately exempt; `/learn/` renders zero images and looks like an unbuilt stub, which needs confirming rather than assuming.

**DSRD 6 on every page: no, and not close.** **Only `/reviews/` has ever been through the full twelve-chapter gate.** Every other page has had the machine gate only, which covers roughly a third of the chapters. So the site's real readiness is unknown for every page but one, and I will not call that a pass.

## The table

| Page | Schema | Images | Missing dimensions | Meta description | Machine gate |
|---|---|---|---|---|---|
| `/` | CollectionPage, EducationalOrganization, SearchAction, WebSite | 10 | 0 | **none** | 6 pass, 11 fail |
| `/about/` | AboutPage, BreadcrumbList, EducationalOrganization, ListItem, WebSite | 19 | 0 | 147 | **37 pass, 0 fail** |
| `/about/instructors/` | BreadcrumbList, CollectionPage, EducationalOrganization, ListItem, WebSite | 22 | 0 | 142 | 26 pass, 6 fail |
| `/about/manifesto/` | AboutPage, BreadcrumbList, ListItem | 12 | **2** | 138 | not run tonight |
| `/about/code-of-ethics/` | AboutPage, BreadcrumbList, ListItem | 11 | **1** | 148 | not run tonight |
| `/about/founders-letter/` | AboutPage, BreadcrumbList, ListItem | 12 | 0 | 142 | not run tonight |
| `/reviews/` | BreadcrumbList, EducationalOrganization, ListItem, WebPage, WebSite | 69 | 0 | **none** | 37 pass, 5 fail |
| `/testimonials/` | **NONE** | 28 | 0 | 129 | 41 pass, 6 fail |
| `/policies/` | BreadcrumbList, CollectionPage, EducationalOrganization, ListItem, WebPage, WebSite | 10 | 0 | 147 | **28 pass, 0 fail** |
| the 7 policy pages | BreadcrumbList, ListItem, WebPage on each | 10 each | 0 | 122 to 148 | **0 fail** on the two run |
| `/help/` | BreadcrumbList, CollectionPage, EducationalOrganization, ListItem, WebSite | 10 | 0 | 146 | 21 pass, 11 fail |
| a help article | Answer, BreadcrumbList, FAQPage, ListItem, Question, SpeakableSpecification | 11 | 0 | 158 | 21 pass, 15 fail |
| `/learn/` | **NONE** | 0 | 0 | **none** | 0 pass, 1 fail |
| `/cards/` | NONE, exempt | 29 | 0 | none, exempt | not a public page |
| 2 author pages | BreadcrumbList, ListItem, Organization, Person | 11 each | 0 | 139 to 147 | not run tonight |

**`/pricing/` answered 404.** It is in DSRD 1's table and does not exist, so it is not a page with failures; it is a page that is not built.

## What that makes the priority, in the order I would take it

1. **`/testimonials/` schema.** A real defect, mine, and small: the same WebPage plus BreadcrumbList pair `/reviews/` already emits, plus switching Rank Math's breadcrumb off for that page so the two trails cannot disagree.
2. **The four missing meta descriptions.** `/reviews/` has its words already from Chat and waits only on Kain pasting them. The homepage and `/learn/` need words written. `/cards/` needs none.
3. **The three missing image dimensions** on the manifesto and the code of ethics. Fifteen minutes.
4. **The machine gate failures examination**, which Chat has already commissioned. This is the one that tells Kain what "finish every page" actually costs, because right now four pages carry 34 failures between them and nobody knows how many are defects and how many are carve-outs the gate has not been told about.
5. **Then the DSRD 6 runs, page by page.** This is the big one and the reason the answer to his third question is no. Twelve chapters each, and chapter 8 needs eyes that did not build the page, so it cannot all be done by me in one sitting.
6. **`/learn/`**, which needs someone to confirm whether it is a stub or a page.

## One thing to be clear about

Kain asked me to guarantee three things and I could only guarantee one. The reason is not that the pages are in poor shape: About, the policies index and the policy family all pass the machine gate with zero failures, and every image on the site has its alt text. It is that **the DSRD 6 gate has been run once, on one page**, so for everything else the honest word is unknown rather than passing.

*No em or en dashes in this file; checked before writing.*
