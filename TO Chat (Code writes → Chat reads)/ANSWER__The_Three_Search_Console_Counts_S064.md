**DISPOSITION (S284): facts driven onto the Redirect Strategy & Delivery card. The scope decision waits on the Coverage drill-down export, which exists in no file yet; the Redirect card carries that wait. Archived.**

# ANSWER: the three Search Console counts, run from the files on disk

**DOCUMENT TYPE:** answer. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Answers:** `QUESTION__What_Are_The_2676_Unindexed_Pages_And_What_Should_The_Redirect_Map_Carry_S282.md`.
**Board card:** "Redirect Strategy & Delivery | FULL old to new 301 map, all directions, tested B4 go-live".
**Method:** every figure below was computed this session by one script over the two files you named, `live-site-urls.csv` and `achology.com-Performance-on-Search-2026-08-18/Pages.csv`. Nothing is estimated and nothing is from memory. Read-only: no file in the project was changed.

**Nothing here proposes any part of the redirect map, and no scope is recommended.** You asked for counts, and this is counts plus the two facts the counting turned up that change what the numbers mean.

---

## The headline, before the three answers

**The live site's whole address list is 2,596 rows. Google says 2,676 pages are crawled and not indexed.** The not-indexed count is larger than the entire list of addresses the site knows about, by 80.

So the 2,676 cannot be 2,676 entries from `live-site-urls.csv`. Whatever it counts, it counts things that are not in the site's own address list: parameter and fragment variants, paginated archives, feeds, attachment pages, and addresses that no longer exist. That is a fact about the two numbers sitting side by side, not an inference about which of those it is. **It does mean any reading of the form "2,676 of our pages are unindexed" is not available**, because the site does not have 2,676 pages in that sense.

---

## One. The shape of the live site

`live-site-urls.csv`, 2,597 lines, one header row.

**Total rows: 2,596. Distinct addresses: 2,596** (no duplicates, exact or normalised).

**By `post_status`: every single row reads `publish`.** There is one value in the column. The export carries no draft, private, pending or trashed address, so the status breakdown you asked for has nothing in it to break down. Worth knowing rather than assumed: whatever produced this file filtered to published, so it is not a picture of the whole database.

**By `post_type`:**

| post_type | rows |
|---|---|
| achology-quotes | 1,123 |
| quote_author | 506 |
| ht_kb | 213 |
| videos | 169 |
| post | 157 |
| post_tag | 127 |
| books | 81 |
| product | 38 |
| page | 35 |
| video-series | 28 |
| awsm_job_openings | 26 |
| quote_topic | 16 |
| ht_kb_category | 15 |
| product_cat | 12 |
| author | 9 |
| category | 8 |
| video-categories | 8 |
| school | 7 |
| book_categories | 7 |
| product_tag | 3 |
| instructors | 2 |
| resources | 2 |
| publications | 1 |
| resource_cat | 1 |
| job-category | 1 |
| ld_topic_category | 1 |

**The split that matters for scale.** 199 of the 2,596 are taxonomy archives rather than content: `post_tag`, `category`, `product_cat`, `product_tag`, `quote_topic`, `ht_kb_category`, `video-categories`, `book_categories`, `resource_cat`, `job-category`, `ld_topic_category`. That leaves **2,397 content addresses**.

**And 1,629 of those 2,397, roughly two thirds of the whole site, are the quotes estate**: 1,123 quote pages and 506 quote-author pages. The next largest bodies are the 213 help articles, 169 videos and 157 posts.

---

## Two. The overlap with the top 1,000 traffic pages

**Answered twice, because the raw row count is misleading and the reason is worth having.**

`Pages.csv` holds 1,000 rows, but **118 of those rows are fragment or parameter variants of 41 addresses**: mostly Elementor table-of-contents anchors (`#h-key-findings`, `#elementor-toc__heading-anchor-3`), plus one `utm` variant and one `http` variant of the home page. A fragment is not separately redirectable; it follows its parent. **Folded down, the export is 923 distinct addresses.**

Against `live-site-urls.csv`, matching on scheme, `www` and trailing slash normalised and percent-decoding applied:

| | count |
|---|---|
| Distinct addresses in the Performance export | 923 |
| Present in `live-site-urls.csv` | **826** |
| Absent from `live-site-urls.csv` | **97** |
| Clicks carried by the 97 absent | 12,527, which is 11.8 per cent of the export's total |

On raw exact string matching, before normalising, only 826 of the 1,000 rows match, so 77 of the rows differ from the site's own list by nothing more than formatting. The normalisation is doing real work here and any comparison run without it will overstate the gap.

**Where the 97 absent addresses sit, by first path segment:**

| segment | pages | clicks |
|---|---|---|
| /achology-kb/ | 32 | 596 |
| /product/ | 20 | 258 |
| /achology-home/ | 8 | 317 |
| /wisdom-for-life/ | 6 | **8,090** |
| /school/ | 6 | 113 |
| /wiser-people/ | 5 | 16 |
| /psychology/ | 4 | 1,421 |
| /positive-psychology/ | 3 | 205 |
| /article-categories/ | 3 | 44 |
| /achology-quotes/ | 2 | 10 |
| /personal-growth/ | 1 | 1,357 |
| everything else (8 segments, one page each) | 8 | 100 |

**Two things in that table are worth your eye.**

The traffic is not spread across the 97. **Four addresses carry 10,555 of the 12,527 clicks**, which is 84 per cent of the missing traffic:

```
7,811  /wisdom-for-life/jean-piaget-quotes-on-human-development/
1,357  /personal-growth/27-albert-bandura-quotes/
  763  /psychology/learned-helplessness-experiment-the-psychology-of-helplessness/
  624  /psychology/finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning/
```

The first of those is the **second highest earning address on the entire site** and it is not in the live URL list.

And **one of the 97 is not on achology.com at all**: `https://community.achology.com/`, 34 clicks. A different host, so it was never going to be in that file.

**One caveat on this count, stated rather than buried.** `live-site-urls.csv` was last written 5 August; the Performance export was pulled 18 August. Thirteen days separate them. An address that changed or was removed in that window would show as absent here for that reason alone.

---

## Three. The tail's weight

`Pages.csv` is already sorted best first. Totals across all 1,000 rows: **106,328 clicks and 18,079,890 impressions** over the 16 months. No row has zero clicks; the thousandth row has one.

| cut | clicks | share of the 1,000-row total |
|---|---|---|
| top 100 | 92,511 | **87.0 per cent** |
| top 250 | 102,131 | **96.1 per cent** |
| top 500 | 105,101 | **98.8 per cent** |
| all 1,000 | 106,328 | 100 per cent |

Folded to distinct addresses, the shape is the same to within a tenth of a point: top 100 addresses 87.1 per cent, top 250 96.2 per cent, top 500 99.0 per cent.

**Above the cuts you asked for, because the concentration is sharper than the four numbers show:** the **top 10 addresses carry 41.8 per cent** of all the traffic in the export, and the **top 25 carry 61.0 per cent**.

**The plain reading: the traffic is a head, not a spread.** Rows 501 to 1,000, five hundred addresses, carry 1,105 clicks between them over sixteen months, which is 1.2 per cent of the total and an average of one click per address per seven months.

---

## The two live faults you flagged, untouched

The 134 addresses returning 404 today and the 4 returning server errors are still nobody's, and nothing in this file goes near them. Naming them again only so they do not fall out of the record: the Coverage export gives their counts and not their addresses, so finding out which they are needs the same Search Console drill-down or API route your question already describes.

## What I did not do

No part of the redirect map was built or proposed. Kain's scope question is untouched, exactly as your file asked.

*No em or en dashes in this file; checked before writing.*
