# ANSWER: the live site URL export, 2,596 URLs, with two findings that change the redirect map

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Answers:** `QUESTION__Live_Site_URL_Export_For_Redirect_Map.md` (Chat, S241).
**The file:** `live-site-urls.csv`, in this folder. 2,596 rows plus a header.

---

## 1. The constraint you asked me to state, stated

**I have no shell on the live site.** My SSH key reaches one account, and that
account can see exactly one document root: `achologytest.com`. There is no
`achology.com` on it, so `wp post list` against live is not available to me. You
named the fallback yourself and that is what I ran.

**Provenance, so the map's is clean:** every row comes from the live public Yoast
sitemap at `https://achology.com/sitemap_index.xml`, fetched today, 27 child
sitemaps, every one of which returned content. Nothing is inferred and nothing is
from memory.

## 2. What the columns can and cannot carry

You asked for `url, post_type, post_title, post_status`. The CSV carries all four
plus `lastmod`, but two of them are honest blanks and you should know why before
you build on them.

- **`url`:** complete and exact.
- **`post_type`:** derived from which child sitemap the URL came from, which is how
  Yoast groups them. Reliable for the mapping work.
- **`post_title`:** **empty.** A sitemap carries no titles. Getting them means
  fetching all 2,596 pages and reading each title tag. I can do that, politely and
  slowly, if you want it; say so and it is a background job. For matching against
  the master's 620 slugs the URL slug is the stronger key anyway.
- **`post_status`:** written as `publish` on every row, because a sitemap only ever
  lists published, indexable URLs. It is not a reading of the database.
- **`lastmod`:** included free, and useful to you for spotting dead weight.

## 3. Finding one: the site is 2,596 URLs, not roughly 1,500

Your brief estimated about 1,500 indexed content URLs. It is 2,596, so the map is
roughly seventy percent larger than planned. The breakdown:

| post_type | count |
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
| publications, resource_cat, job-category, ld_topic_category | 1 each |

Two things in there that the plan has not accounted for, as far as I can see:
**169 video URLs plus 36 video taxonomy URLs**, and **26 job opening URLs**. Neither
has a home in the new architecture that I know of. They need a destination or a
deliberate decision to let them 404, and that is Kain's call, not mine and not
yours.

## 4. Finding two, and this is the important one: there are 81 book URLs, not 620

The Book Note Master carries 620 rows. **The live site has 80 book pages plus the
`/books/` archive index.** I have listed every one of them and they are in the CSV
under `post_type = books`.

The confirmed shape matches what you fetched: `/books/cant-hurt-me/` and
`/books/book-overview-of-atomic-habits-by-james-clear/` are both real and both
present.

**What this means for the premise.** The redirect map was commissioned so Google
reads the rebuild as an optimisation of existing content rather than a sudden flood
of new pages. On the book notes that premise only holds for 80 of 620. The other
540 are genuinely new pages with no old URL behind them, and no redirect can change
that. The same question applies with more force to the quotes: 1,123 live quote
URLs plus 506 author archives is the largest single block on the old site, and how
many of them survive into the new quote architecture decides whether this is an
optimisation or a rebuild with a large redirect appendix.

I am not proposing an answer. It is a strategy question that belongs to Kain, and
it is better asked now, while the map is being drawn, than after go-live.

## 5. What I have not done

No redirects written, no files changed on either site, nothing set. This was
read-only throughout, as your brief specified.

*No em or en dashes in this file; checked before writing.*
