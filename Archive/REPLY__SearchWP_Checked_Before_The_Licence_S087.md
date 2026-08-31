> **CHAT DISPOSITION, S321: closed and archived. The one fact it waited on has landed: Kain bought the licence, recorded by Code in `RULING__Kain_Has_Bought_The_SearchWP_Licence_S087`. The remaining SearchWP work (the tier, the zip, the install) lives on that ruling and on the Plugins and Site Configuration card, not here. No board card moved by this file.**

> **CHAT DISPOSITION, S318: read. STAYS on one fact: Kain buying the licence (Standard at 99 dollars a year, or Pro at 199 for two sites), put to him at S318. Archives when his word is filed to FROM Chat as a RULING.**

# REPLY: SearchWP checked on all three counts. Verdict: clean. Kain can buy it.

**From:** Claude Code, Session 087, 26 August 2026.
**Answers:** `RULING__SearchWP_Stands_Check_It_Before_The_Licence_Is_Bought_S311`, its three numbered checks and its OWED BACK line, in order.
**Board card:** Plugins and Site Configuration.

The ruling's own instruction is obeyed: this is not a plugin comparison and no alternative is offered. The choice was made at S176 and Kain declined to reopen it at S311. Nothing below is a blocker, so the choice stays closed.

---

## Check 1: fitness. Clean.

The S176 decision needed five things. Every one holds against SearchWP's current documentation, read this session rather than recalled.

**Indexing the four Knowledge Hub content types plus the help answers as separate sources.** SearchWP's unit of indexing is a Source, and a custom post type is a Source. The four Knowledge Hub types and the help answers are five custom post types, so they are five sources. Its own words: a Source is an indexable type of content on the site, and an Engine returns results only from the Sources added to it.

**Filterable, so the Knowledge Hub search excludes the help answers.** This is what Engines are for, and it matters here more than it sounds: DSRD 1 §2.5 says the help section is deliberately excluded from Knowledge Hub search. Two engines, one carrying the four content types and one carrying the help answers, is the plugin's ordinary shape rather than a workaround.

**Owner-operable, no code to add a source later.** Sources, attributes and their relevance weights are configured in the WordPress admin, per source and per engine, with a slider for weight. Kain and Karen can add a source without anyone writing anything.

**It reads the ACF fields.** This one is not in the original decision and it should have been, so it is named here. The book note page's content lives in ACF fields, not in `post_content`, and ACF Pro is one of the nine installed. SearchWP indexes custom fields as attributes chosen from a drop-down, per source and per engine, and it groups ACF repeatable fields as a single attribute. **Had this gone the other way, the book notes would have been indexed as empty pages** and nobody would have seen it until a search returned nothing.

**Current version is 4.6.1**, read from its changelog this session. That matters for check 2.

## Check 2: compatibility, against the nine plugins actually on the install. Clean, with one thing to configure.

The nine, read back off the install this session rather than from any document:

| Plugin | Version | Verdict |
|---|---|---|
| advanced-custom-fields-pro | 6.8.8 | supported, and load-bearing here (see check 1) |
| complianz-gdpr-premium | 7.6.4 | no contact |
| seo-by-rank-math | 1.0.276 | no conflict |
| seo-by-rank-math-pro | 3.0.119 | no conflict |
| sg-security | 1.6.5 | no contact |
| wordpress-starter | 3.4.8 | no contact |
| sg-cachepress (Speed Optimizer) | 7.8.2 | **one setting to make, see below** |
| wp-all-import | 4.1.1 | handled automatically from SearchWP 4.1.16 |
| import-xml-csv-settings-to-rank-math-seo | 1.2 | no contact |

**Rank Math and its Pro: no conflict, and this is evidence rather than an absence of alarm.** Rank Math publishes its own list of plugins known to conflict with it. That list was read this session: it runs to roughly seventy plugins, and SearchWP is not on it. The two also do different jobs at different moments. Rank Math writes meta tags, schema and the sitemap on a page render; SearchWP replaces the query WordPress runs when a visitor searches. They do not touch the same thing.

**WP All Import: this was the real risk and it has been closed by the plugin's own authors.** SearchWP's documentation states the problem plainly: an import makes many concurrent edits in a short time, the indexer is flooded with edit notifications, and the index ends up out of sync. That is precisely this project's shape, because the library is imported rather than hand entered. **As of SearchWP 4.1.16 WP All Import is handled automatically**, and current is 4.6.1, so the manual pause-import-rebuild dance is not needed. A manual rebuild is still available two ways if it is ever wanted: a Rebuild Index button in the admin, and `wp searchwp index --rebuild` over WP-CLI.

**SiteGround Speed Optimizer: the one thing that needs doing, and it is a setting rather than a problem.** Dynamic caching is ON on the install (`siteground_optimizer_enable_cache` reads 1, read this session), and **no URL exclusions are configured at all**: `siteground_optimizer_excluded_urls` does not exist as an option yet. A cached search results page is the classic way search goes stale, exactly as the ruling anticipated. The fix is the Speed Optimizer's own Exclude URLs From Caching setting, applied to the search results address once that page exists. It is not a reason to hesitate; it is a line on the build list for the day the search results page is built.

**Complianz: no contact, and the reason is worth stating rather than assuming.** The consent blocker holds back third-party scripts. SearchWP's search runs in PHP on the server and loads no third-party script, so there is nothing for the blocker to catch. This is different from the Kit question at S294, where the risk was real because a Kit form IS a third-party script.

## Check 3: cost, stated plainly. Read from SearchWP's own pricing page this session.

| Tier | Price today | Normal price | Sites | What it adds |
|---|---|---|---|---|
| Standard | **99 dollars a year** | 199 | 1 | unlimited search queries and engines |
| Pro | 199 dollars a year | 399 | 3 | priority support, eCommerce integrations |
| All Access | 399 dollars a year | 699 | 100 | bundles WPFilters |

**Standard, at 99 dollars a year, is the tier that covers what we need**, and the ruling asked directly whether a lower tier still does. It does. Unlimited engines and unlimited sources are in the Standard tier, so the two engines the Knowledge Hub needs cost nothing extra. Pro's additions are WooCommerce and the other eCommerce integrations, which this site does not use: Achology sells through its own checkout, per DSRD 4.

**Three things Kain should see before he pays.**

It is an annual subscription, not a one-off. There is no lifetime tier.

The 99 is introductory. SearchWP's own page says renewals revert to the full price, so the second year is 199 unless they change it.

**It covers one site, and this project has two:** achologytest.com, the build ground, and achology.com, which goes live at cutover. Standard's single-site licence covers one of them at a time. In practice that is fine, because the licence key moves with the site at cutover and the build ground stops being used, but it is a real constraint and he should know it before he buys rather than at cutover. If he would rather have both covered at once, that is the Pro tier at 199, and that is a money decision and therefore his.

There is a fourteen day money back guarantee on every tier.

## The verdict

**Clean on all three.** No blocker was found on any count, so the S176 choice is not reopened.

## What is needed from Kain, and what happens next

**From Kain: buy the Standard licence, or say the word if he wants Pro for the two-site reason above.** Nobody but him spends money, and no key is typed by anyone but him.

**Then, and only then:** the plugin is installed on the build install and the five sources are indexed, per the ruling's own sequencing. The ruling's reasoning for doing it now rather than at the end stands and is worth repeating: the search results page has nothing to read until an index exists, and building it against an empty set is testing an empty page rather than testing search.

**One thing to hand Chat when that happens**, because it is Chat's page: the search results page is one of the eleven Knowledge Hub templates and sits on Chat's side of the S314 split. The index will be ready before the page is.

OWED BACK: nothing further from Code until Kain buys the licence. On his word: install, configure the two engines, index all five sources, and file the read-back.

*No em or en dashes in this file; checked before writing.*
