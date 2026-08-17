# BRIEF: pull the Search Console query data for the 249 help articles, then stop

**From:** Claude Chat, S235. **Date:** 2026-08-03. **Approved by Kain in session.**
**Answers:** INSTRUCTION__Kain_Wants_Research_Driven_Keyphrases_Not_Derived.md, REQUEST__The_Keyphrase_Rule_Needs_Replacing.md, PROPOSAL__Keyphrases_From_Article_Openings.md, EXCEPTIONS__Keyphrase_Formula.md, REPORT__Keyphrases_And_Bulk_Rank_Math_Run.md.

## The ruling, first

**No SEO subscription is being bought for this work.** Kain's research-first instruction stands, but the source is Google Search Console, not a paid tool. He confirmed in session that a Search Console property already exists for achology.com. Search Console is Google's own record of the queries that actually reached these pages, which is the thing the paid tools estimate.

Two things were being run together and are now separated:

1. **What the Rank Math score measures.** Your own evidence settles it: exact-phrase presence in the title, URL, opening paragraph, subheadings and body. Median 47 where the phrase was in the text, median 8 where it was not. Volume is irrelevant to the score.
2. **Which phrase is worth being green for.** That is the search-data question, and Search Console answers it for these 249 better than any tool could, because it is first-party and specific to these pages.

The paid tool question is not closed forever. It is deferred to the Knowledge Hub, where pages are written to win queries the site does not yet rank for and first-party data cannot exist. It is not needed for the help section.

**Your openings-based proposal is not discarded.** It becomes the fallback for any article Search Console has no data on, and a cross-check everywhere else.

## What is asked of you now

One deliverable, read-only, no site changes:

**A spreadsheet of the Search Console query data for every help article.** One row per article, carrying:

- the article URL
- the article title
- the top queries that reached that URL, with impressions and clicks for each, taken over the longest window Search Console will give (16 months if available)
- a flag on any article with no query data at all

If the Search Console property is verified for the old site rather than the new build, pull it from wherever the history actually lives and say which property it came from. If access needs Kain to click something, name the exact click in one line and stop there.

**Set nothing.** No keyphrases, no meta titles, no meta descriptions, no score run. The 96 scored articles stay as they are. The remaining 153 stay unscored.

## What happens after you deliver it

Chat and Kain write the keyphrase rule against that data, article by article where the data warrants it, and send back a ruled set of 249 keyphrases plus meta titles and descriptions. You set them in one pass and complete the score run.

## One constraint carried into that rule now, so you can plan

**Slugs do not change.** Your S042 counsel was right and Kain has taken it: the 2,426-link internal map, the 250 audio recordings and the cutover redirect map all hang off the current addresses. Where a ruled keyphrase does not appear in its slug, the article loses Rank Math's URL check and we accept the points. If your measured view is that this puts 80 out of reach on a material number of articles, say so with the number when you deliver the spreadsheet, and Kain will rule on it then rather than at the end.

No em or en dashes in this file, checked before writing.
