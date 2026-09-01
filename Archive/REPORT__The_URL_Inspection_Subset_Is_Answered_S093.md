> **CHAT DISPOSITION, S329:** read. The run-end confirmation of the S092 subset report: same 1,000, same 768 and 232, zero errors. Written onto the Redirect Strategy card with its S092 twin; the 132-unknown and 591-no-sitemap readings put to Kain in the S329 sitting. Board cards moved: Redirect Strategy (edited). Archived.

# REPORT: the URL Inspection subset is answered, all 1,000, no errors

**From:** Claude Code, Session 093. **Date:** 1 September 2026.
**Answers:** `RULING__URL_Inspection_Subset_First_Then_The_Tail_S311.md`, its first owed file. The tail's own printout follows as a second file when that pass finishes, per the ruling's "two files, not one held back".
**Board card:** Redirect Strategy and Delivery.
**The data itself:** `url-inspection-subset.csv`, in the Search Console and Live Site Exports folder inside the spreadsheets folder. One row per address, carrying the five things the ruling asked for. This file is the printout and the reading, never a second copy of the rows.

---

## The run

The subset was left running at the S092 close at roughly 750 of 1,000. It finished. **1,000 addresses answered, 0 rows carrying an error.** No request reached the live site at any point: this reads Google's index, which is why the S092 crawl incident does not touch it.

## The verdict

| | |
|---|---|
| PASS | 768 |
| NEUTRAL | 232 |

## The coverage state, in Google's own words

| State | Addresses |
|---|---|
| Submitted and indexed | 768 |
| URL is unknown to Google | 132 |
| Page with redirect | 29 |
| Not found (404) | 28 |
| Discovered, currently not indexed | 22 |
| Crawled, currently not indexed | 10 |
| Excluded by a noindex tag | 6 |
| Alternative page with proper canonical tag | 3 |
| Soft 404 | 2 |

## What is worth your attention, in the order I would take it

**768 indexed addresses are the asset the redirect map exists to protect.** Every one of them is in the file with the canonical Google actually chose beside it. That is the drill-down the Coverage export could not give us, reconstructed.

**132 addresses are unknown to Google, and not one of them is on a sitemap.** These carry clicks or impressions in `Pages.csv` and yet Google says it has never seen them. The two facts sit oddly together and I have not reconciled them: my reading is that these are addresses whose traffic predates a change, so the Performance report still remembers them while the index no longer holds them. **Worth your eye before the map treats them as live.**

**409 of the 1,000 are on a sitemap and 591 are not.** That split is a finding in its own right and it is not mine to rule: a traffic-carrying address absent from every sitemap is either deliberate or a gap in the sitemap.

**59 addresses already fail today**: 28 return 404, 29 are pages with a redirect, and 2 are soft 404s. The 404s cluster in two families, `/achology-kb/` and `/achology-home/`, and the two soft 404s are both quote pages. These are the addresses whose answers change what the map does, exactly as the ruling said they would.

**Google chose a different canonical from ours on 2 addresses**, both the same self-improvement piece sitting under two categories, `/positive-psychology/` and `/motivation/`. Google settled on the `/motivation/` one. A two-address finding rather than a pattern.

**154 addresses carry no last-crawl time**, which is the same set the unknown and never-indexed states already cover.

## What I did not do, and it is deliberate

**I have not written a single redirect row.** The S301 method puts the rows in DSRD 1 section 11 per page type as each template is confirmed, and none of the four content templates is confirmed yet. This file is the measurement the map is built from, not the map.

**I have not decided anything about the 132 or the 591.** Both are Kain's call by the S301 brief's own words on an old address with no new home.

OWED BACK: nothing from you on this file unless the reading of the 132 is wrong. The tail's printout is still mine and follows when its pass finishes.

*No em or en dashes in this file; checked before writing.*
