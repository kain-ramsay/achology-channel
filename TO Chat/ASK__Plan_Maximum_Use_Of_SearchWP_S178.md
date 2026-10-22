**Needs from Chat: a planning session on SearchWP's full use, commissioned by Kain in Code's S178 search sitting; one plan back to Kain with one recommendation per part, then briefs to Code.**

# ASK: plan the maximum use of SearchWP (Code, S178, 22 October 2026)

Kain, after signing off the search results page: "Seems we're using this plugin let us get maximum usage out of it ... if this requires a planning session, then please commission that." He asked what the greatest purpose of SearchWP could be, whether it helps search engines or AI models, and whether something like an Obsidian map of content (MOC) would help.

What Code told him, as grounding for the plan (facts as found on the build site today, NOTE__Search_Results_Page_SearchWP_Setup_And_The_Font_And_Spacing_Scan_S178.md and RULING__SearchWP_Five_Settings_S178.md):
- SearchWP is the site's own search engine; Google and AI models never use it, and the results page is rightly kept out of their index. It does not on its own make the site better liked by them; structure does (topic groups linked to each other, sitemaps, structured data).
- The Knowledge Hub's map of content already exists in the pages search engines can see: the seven subject pages, the 36 topic pages and All Tags. The search page cannot be the map, being noindex.

Code's three recommendations, for Chat to plan, rank and brief:
1. The demand radar (recommended first): SearchWP already logs every search and every search that finds nothing (1,103 logged by 22 October, many of them Code's own tests; clear or mark those before reading). A monthly read of the top searches and the no-result searches into the stage 0 demand list (DSRD 2 section 0.0; DSRD 1 section 7.5 names the Metrics extension at launch, Kain S357; whether the built-in statistics are enough is a question for the plan).
2. One search for the whole site (DSRD 1 section 7.1): today the engine covers the four Knowledge Hub kinds only, by Kain's S178 design "Search the Knowledge Hub". The spec asks the 28 courses, the Help answers and the commercial and policy pages too, so "life coaching" finds the course. This needs Kain's ruling on how the page shows non-Knowledge Hub results (its kinds band, its title), and settles the scope question left open in REPLY__Search_Results_Page_S375_What_Is_Done_And_What_Waits_S178.md.
3. Related reading by relevance: the same engine choosing each piece's related reading, for better links between pages (which search engines and AI models do reward).
Also open: the problem-phrase synonyms DSRD 1 section 7.1 asks for ("can't stop worrying" finding the anxiety and CBT pieces) and the DiMAP expansion, both needing Chat's list; the 404 page's search box (S375 part 5); and a separate effort for visibility to AI models (Kain asked; not a SearchWP job).

OWED BACK: the plan to Kain, then briefs to Code for whatever he signs.

*No em or en dashes in this file; checked before writing.*

## Added the same day: what SearchWP's own pages offer (read at Kain's ask, 22 October 2026)

Kain sent SearchWP's article on speeding up search; Code read it and SearchWP's documentation and blog. For the plan:
- Speed article (searchwp.com/speed-up-wordpress-search/): our setup already follows it (own index, partial matches on, re-parse and minimum word length off). Its one open item for shared hosting like SiteGround is "Reduce Indexer Load" (off today); with a one-minute rebuild it matters little. Caching plugins help little because every search is a new address.
- Live Search, a dropdown as the reader types (searchwp.com/features/live-search/): the article says it is included with every plan. This is DSRD 1 section 7.2's Option C (a preview of the top results as you type), now possible in the header search box built today.
- Redirects (searchwp.com/features/redirects/): send an exact search to one page, for example a course name to its course page. Called an extension; tier not stated.
- Related Content (searchwp.com/features/related/): related reading blocks by relevance, handpicked or automatic; the blog calls it a Pro extension.
- Statistics (searchwp.com/documentation/setup/statistics/): built in, with a No Results Searches list, ignored searches and auto-delete. Code's test searches of 22 October should be cleared or ignored before the first read. The Metrics page (searchwp.com/features/metrics/) adds clicks and CSV export as an extension.
- Stopwords per engine and extra data in the index: code-level documentation pages (knowledge base), free.
- Nothing SearchWP publishes claims it helps search engines or AI models; its "indexing issues" article separates Google's index from the site's own search.
Which extensions the licence includes is a question for Kain's SearchWP account page (the plan should check the tier before recommending any).
