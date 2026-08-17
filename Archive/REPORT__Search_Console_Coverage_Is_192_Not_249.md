# REPORT: the Search Console pull can cover 192 articles, not 249, and here is the map

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Against:** `BRIEF__Search_Console_Query_Pull_For_The_249.md` (Chat, S235).
**The file:** `help-slug-map.csv` in this folder, 271 rows, one per slug on either side.
**Sources, read this turn:** the live Yoast sitemap at achology.com, and the build
database at achologytest.com over SSH. Nothing recalled.

## Why this arrives before the data

Your brief rests on one sentence: "Search Console answers it for these 249 better
than any tool could, because it is first-party and specific to these pages." That
holds, but not for 249 of them. I found the ceiling while preparing the pull, and
it is better in your hands now than after the spreadsheet lands looking thin.

## The three numbers

| | count |
|---|---|
| Help articles on the build | 250 |
| Help articles live on achology.com today | 213 |
| Same slug on both sides, so search data maps | **192** |
| Built but new, so no search history can exist | **58** |
| Live but with no successor built | **21** |

## What each number means for the keyphrase rule

**192 articles.** These have a live page at the same slug, so the pull will return
real queries for them. This is the population your rule can be written against, and
it is 77 percent of the section rather than all of it. Good enough to rule from, and
worth doing.

**58 articles.** These never existed on the live site. No first-party data will ever
exist for them, no matter which property or window we use. Your own brief already
names the answer: "Your openings-based proposal is not discarded. It becomes the
fallback for any article Search Console has no data on." That fallback is not an
edge case, it is 58 articles, so it needs to be as considered as the main rule.

**21 articles.** Live pages with nothing built to replace them. These are not a
keyphrase problem, they are a redirect problem, and they belong in the redirect map
alongside the export I filed today.

## One thing the brief assumes that is not true

The brief says "Slugs do not change" and reasons from it. The slugs largely do not
change, and that part holds. **But the path does.** Live help articles sit at
`/achology-kb/{slug}/` and the built ones do not. So every one of the 192 is a URL
change even where the slug is identical, and the internal link map, the audio and
the redirect map all hang off that, exactly as your S042 counsel warned.

I am not proposing a fix. It may already be accounted for in DSRD 1's new
architecture and simply not stated in this brief. Flagging it rather than assuming.

## What I have and have not done

The pull script is written and tested against its own arguments. It does exactly
what your brief specifies, one row per article with the top queries, impressions,
clicks, the longest window Search Console holds, and a flag on any article with no
data. It sets nothing: no keyphrases, no meta titles, no meta descriptions, no score
run, per your instruction in writing.

It cannot run yet. Access is still blocked, and the blocker is now down to one
click by Kain, which he has been given.

*No em or en dashes in this file; checked before writing.*
