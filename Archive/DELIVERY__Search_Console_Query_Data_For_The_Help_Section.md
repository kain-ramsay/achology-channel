# DELIVERY: the Search Console query data for the help section

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Answers:** `BRIEF__Search_Console_Query_Pull_For_The_249.md` (Chat, S235), now fully
delivered and archived.
**The file:** `search-console-help-queries.csv` in this folder. 1,030 rows.
**Read with:** `REPORT__Search_Console_Coverage_Is_192_Not_249.md`, filed earlier today.

---

## 1. The access question is closed

The property is **`sc-domain:achology.com`**, a **Domain property**, not a URL prefix
one. That answers the open item in your ASK.

A read-only service account now holds Restricted access to it, verified on the
rendered permissions page:
`achology-search-reader@achology-search-data.iam.gserviceaccount.com`.
Restricted rather than Full, because the pull only reads. Kain can remove it in two
clicks and nothing else on the property changed.

**The 16 month window is available.** The pull ran 2025-04-06 to 2026-08-02, the full
window less Google's three day reporting lag.

## 2. What was pulled

| | |
|---|---|
| Live help articles queried | 213 |
| Articles with real query data | **158** |
| Of those, articles that exist in the build | **142** |
| Articles with no query data at all, flagged in the file | 55 |
| Total impressions across the section, 16 months | 10,666 |

Columns: `url, slug, post_title, query, impressions, clicks, no_query_data, in_build`.
Titles are joined from the build by slug, so an article on both sides carries its real
title. `in_build` tells you whether a live article survived into the rebuild, so you
can set aside the ones that did not without cross-referencing.

## 3. What the data says, before anyone rules on it

**This is a brand-name section.** The ten queries that reach it most:

| impressions | query |
|---|---|
| 2,540 | achology |
| 1,307 | achology meaning |
| 1,047 | what is achology |
| 864 | achology certified |
| 700 | kain ramsay |
| 619 | achology curriculum |
| 526 | udemy kain ramsay |
| 484 | kain ramsay udemy |
| 385 | is achology recognized |
| 168 | achology life coaching |

Eight of the ten contain "achology" or "kain ramsay". The section is not found by
people searching psychology topics; it is found by people who already have the name
and are checking it out. That matches the section's job, and it has a direct
consequence for the keyphrase rule: **for most of these articles the honest keyphrase
is a brand phrase, and a brand phrase is already in the title.**

**The volume is small, and you should see that plainly.** 10,666 impressions across 16
months and 213 articles averages 50 impressions per article over more than a year. The
best performing article has 1,084. This data is good evidence of which phrasing real
people use. It is thin evidence for ranking decisions. I would not let it carry more
weight than that, and I would say so to Kain before he reads a strategy into it.

**Your fallback is not an edge case.** The 55 with no data, plus the 58 built articles
that never existed live, means the openings-based proposal governs most of the built
section rather than a remainder. It deserves the same care as the main rule.

## 4. What I did not do

Per your brief, in writing: no keyphrases, no meta titles, no meta descriptions, no
score run. The 96 scored articles are untouched and the remaining 153 stay unscored.
Nothing was written to WordPress. The only writes were the two CSVs in this folder.

## 5. The 80 point question, ready to answer as soon as you rule

You asked whether slugs not carrying the ruled keyphrase puts 80 out of reach on a
material number of articles. I can answer that with a real count rather than an
estimate, but it needs the ruled keyphrases first, which are yours and Kain's. Send
them and I will report exactly how many articles lose the URL check and what each
scores without it, before a single one is set.

*No em or en dashes in this file; checked before writing.*
