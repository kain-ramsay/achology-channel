# QUESTION: what are the 2,676 pages Google crawls and does not index, and what should the redirect map actually carry?

**DOCUMENT TYPE:** question. Not a page spec. **From:** Claude Chat, Session 282. **Date:** 18 August 2026.
**Board card:** "Redirect Strategy & Delivery | FULL old to new 301 map, all directions, tested B4 go-live" (Urgent and Important).
**Why it is yours:** the files are on disk and this needs counting, not judgement. My filesystem connector reads text into my context, so a 271 KB CSV is not something I can total reliably. You can run it in seconds.

---

## What just landed, and where

Karen pulled two Search Console exports today, both in the **Search Console + Live Site Exports** folder under the spreadsheets folder, unzipped into folders named by report and date. The folder's own README now describes them.

- The **Performance** export's `Pages.csv`: the top 1,000 pages by clicks over 16 months, with impressions, click-through rate and average position.
- The **Coverage** export: counts only, no addresses.

## What the Coverage export says, and the number that prompted this

| State | Pages |
|---|---|
| Crawled, currently not indexed | 2,676 |
| Alternate page with proper canonical tag | 858 |
| Discovered, currently not indexed | 329 |
| Excluded by noindex | 141 |
| Not found (404) | 134 |
| Page with redirect | 96 |
| Blocked, other 4xx | 10 |
| Soft 404 | 4 |
| Server error (5xx) | 4 |
| Blocked, access forbidden (403) | 4 |
| Blocked by robots.txt | 1 |

**Two of those are live faults on the current site, not cutover problems:** 134 addresses returning 404 today, and 4 returning server errors. Nobody has looked at them.

**The one that matters for scope is the 2,676.** Google crawls them and decides they are not worth indexing. If that is a real count of real pages, then the redirect map's job is much bigger than the traffic-earning site, and most of what it would carry is pages Google has already judged worthless.

## The three things I am asking you to count

All from files already on disk. **Read-only. Nothing to build.**

**One. The shape of the live site.** From `live-site-urls.csv` in that folder: total rows, and a breakdown by `post_type` and by `post_status`. I want to know how many addresses exist in total and what kinds they are, because "2,676 not indexed" means something very different against a 4,000-page site than against a 12,000-page one.

**Two. The overlap.** How many of the top 1,000 pages in the Performance export's `Pages.csv` appear in `live-site-urls.csv`, and how many do not. A traffic-earning address that is not in the site's own URL list is either already gone or lives somewhere the export did not reach, and either way it is a redirect the map would otherwise miss.

**Three. The tail's weight.** In `Pages.csv`, the clicks total for the top 100 rows, the top 250, the top 500 and all 1,000. This tells us plainly whether the traffic is concentrated in a small head or spread across the whole list, which is the fact the scope decision turns on.

## What I am NOT asking you to do

Do not build any part of the redirect map, and do not propose one. Kain has an open scope question (does the map cover everything, or only what earns) and it stays his until these numbers exist.

## One thing neither of us can get from what we hold

**The 2,676 addresses are in no file we have.** The Coverage export gives the count and nothing else. Getting the actual list means either drilling into that reason inside Search Console and exporting it there, capped at 1,000 rows, or going through the Search Console API. That is named here so nobody spends an hour looking for a list that does not exist on disk, and so the API route can be considered on its merits rather than as a workaround.

*No em or en dashes in this file; checked before writing.*
