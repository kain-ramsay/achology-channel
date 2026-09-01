# REPORT: the URL inspection subset is in. 768 of the 1,000 traffic-carrying addresses are indexed

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Answers:** `RULING__URL_Inspection_Subset_First_Then_The_Tail_S311.md`, the subset half of its OWED BACK line. The tail follows as its own file.
**The machine file:** `url-inspection-subset.csv`, in the Search Console exports folder, one row per address with thirteen columns. This report is the shape of it; the file is the data.
**Zero rows carry an error.** All 1,000 were answered by Google, none refused, none rate limited past the retry.

---

## The route, so the number can be trusted

`urlInspection.index.inspect`, one address per call, against `sc-domain:achology.com`, with the service account's JWT signed by `openssl` and the calls made by `curl`. No package install, exactly as ruled. Per address it returns the verdict, the coverage state in Google's own words, the last crawl, the canonical Google chose, the user canonical, the sitemaps it appears in and the referring URLs.

**The addresses are the 1,000 rows of `Pages.csv`**, which is by definition every address carrying a click or an impression, so this is the traffic-carrying set the ruling put first. The broken live addresses were to be added regardless of traffic; **the count added was zero**, because the ones identifiable were already inside `Pages.csv`.

## The headline

| | |
|---|---|
| Indexed and serving | **768** |
| Not indexed, for eight different reasons | **232** |

| Coverage state, Google's own wording | Count |
|---|---|
| Submitted and indexed | 768 |
| URL is unknown to Google | 132 |
| Page with redirect | 29 |
| Not found (404) | 28 |
| Discovered, currently not indexed | 22 |
| Crawled, currently not indexed | 10 |
| Excluded by 'noindex' tag | 6 |
| Alternative page with proper canonical tag | 3 |
| Soft 404 | 2 |

## The thirty that matter most, and they are a clean pattern

**Twenty eight addresses that carry traffic return 404 today, and two more are soft 404s.** These are losing their ranking now, before cutover has even happened.

**Twenty three of the twenty eight are `/achology-kb/...`**, the old knowledge base: the section the 249 rebuilt help articles replace. They are the single clearest redirect block on the site. One rule, `/achology-kb/{slug}/` to its new `/help/{category}/{slug}/` home, and twenty three earning addresses stop being dead. Three of them, with the full list in the CSV:

- `/achology-kb/can-you-provide-a-definition-of-modern-applied-psychology/`
- `/achology-kb/what-are-the-main-differences-between-udemy-and-achology-com/`
- `/achology-kb/whats-the-difference-between-achology-certification-and-somap-accreditation/`

**The other five are four different things**, each needing its own decision: two `/article-categories/...`, two `/wiser-people/directory/coach/...`, and `/new-courses/`, with `/achology-home/academy-for-applied-psychology/` and its accreditation child making up the rest.

**Both soft 404s are `/achology-quotes/...`**, which matters because that section is the largest block below.

## The 132 Google no longer knows, which is the finding I did not expect

**"URL is unknown to Google" means it is not in the index at all.** Every one of these sits in `Pages.csv`, so every one earned clicks or impressions across the sixteen months that export covers. They have been dropped since.

Grouped by first path segment, the 232 not-indexed addresses fall out like this:

| Section | Count |
|---|---|
| `/achology-quotes/` | 40 |
| `/psychology/` | 37 |
| `/achology-kb/` | 33 |
| `/product/` | 22 |
| `/wisdom-for-life/` | 17 |
| `/general-interest/` | 13 |
| `/videos/` | 8 |
| `/achology-home/` | 8 |
| everything else | 54 |

**`/achology-quotes/` is the biggest block, and the quote page template does not exist.** Forty earning quote addresses are out of the index while the pages meant to replace them are unbuilt. Worth knowing before the quote template's place in the running order is set.

**`/product/` at 22 is the commerce set**, which maps onto the fourteen commercial page templates.

## What I would do with this, offered rather than decided

**The 23 `/achology-kb/` 404s are redirect rows that can be written today**, without waiting on any page type, because their destinations already exist and are live. They are the cheapest recovery on the whole list.

**Everything else waits on its page type**, which is exactly the per-page-type method the S301 brief sets. This file is the evidence that method needed: it says which old addresses actually matter, and it says it from Google rather than from a guess.

## The tail

Running next: the 1,596 addresses in `live-site-urls.csv` that carry no traffic. It files its own printout rather than being held back until it finishes.

**One number to watch.** The API's published quota is 2,000 a day and this pass spent 1,000. The tool reads its own rate-limit responses rather than trusting the published figure, and it resumes where it stopped, so a quota stop costs a wait rather than a rerun.

OWED BACK: nothing on the subset. The tail's printout follows.

*No em or en dashes in this file; checked before writing.*
