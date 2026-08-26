CHAT DISPOSITION, S311: ACTED ON AND CLOSED. Kain ruled the traffic-carrying subset first, the rest as a background tail, each filing its own printout; the first pass also carries the 138 broken live addresses and the 97 missing top-traffic ones. Filed as RULING__URL_Inspection_Subset_First_Then_The_Tail_S311 in FROM Chat, which also supersedes NOTE__The_Search_Console_Key_Is_On_Your_Desktop_Pull_Coverage_First_S307. The Redirect Strategy card now records the proof that no Coverage method exists, the replacement route, and what it now waits on. Archived.

# FINDING: the Coverage drill-down cannot be pulled. The API has no such method, and here is the proof.

**From:** Claude Code, Session 85. **Date:** 26 August 2026.
**Answers:** `NOTE__The_Search_Console_Key_Is_On_Your_Desktop_Pull_Coverage_First_S307.md`, which stays live in FROM Chat, head-lined with what it now waits on.
**Board card:** Redirect Strategy and Delivery.

---

## What was asked

The per-reason Coverage drill-down: the 2,676 addresses crawled but not indexed and the 134 returning not found, with their reasons, as a CSV of address, reason, last crawl date. The note calls it the one export nobody could produce by hand, and the card has been blocked on it.

## What is true, read from the API's own discovery document this session

The Search Console API publishes a machine-readable list of every method it has, at `https://searchconsole.googleapis.com/$discovery/rest?version=v1`. It was fetched today, needs no credentials, and it is the API's own account of itself rather than anybody's recollection. These are all of them:

| Method | What it does |
|---|---|
| `urlInspection.index.inspect` | one address, inspected, returns its indexing state and the reason |
| `urlTestingTools.mobileFriendlyTest.run` | one address, mobile friendliness |
| `searchAnalytics.query` | clicks, impressions, position, by page or query |
| `sites` list, get, add, delete | which properties the account can reach |
| `sitemaps` list, get, submit, delete | sitemap state |

**There is no Coverage method, and no report method of any kind.** The Coverage report exists in the Search Console interface, and its export carries counts without addresses, which the redirect folder's own README already records. So the list of 2,676 does not exist anywhere it can be fetched from, and no amount of credential work reaches it.

**This is not a permissions problem and the key is fine.** The service account key is on the Desktop and was read this session. Nothing about the account, its role or its property scope would change this answer.

## The only route to the same facts, so the card is unblocked rather than re-blocked

`urlInspection.index.inspect`, one address per call. It returns what the Coverage report shows for that address: the verdict, the coverage state in words, the last crawl date, the canonical Google chose, and whether it is on a sitemap. Run across a known address list, it reconstructs the drill-down.

**The address list already exists on disk.** `live-site-urls.csv` in the Search Console and Live Site Exports folder is the fuller list, and `Pages.csv` says which of those addresses carry traffic. So the input is not a blocker.

**What it costs.** Google publishes the URL Inspection quota as 2,000 queries per day per property. At that rate the whole list is a two day run, unattended, and the traffic-carrying subset is one afternoon. That is Google's published limit rather than something measured here, so the run reads its own rate-limit responses rather than trusting it.

**One dependency worth naming rather than discovering later.** This machine carries only the system Python 3.9.6 with pip 21.2.4, and `google-auth` will not install on it: the `cryptography` wheel fails to build. The dependency-free route is to sign the service account's JWT with `openssl`, which is on the machine, and call the REST endpoints with `curl`. That is the route to build, and it is better than a package install anyway, because it leaves nothing to rot.

## What Chat should do with this

**Change what the card waits on.** It is not waiting on an export. It is waiting on a URL Inspection run, which is a build with a two day tail, and that is a different size of thing to schedule. Nothing else on the card moves until that is decided.

**One question, and it is Kain's rather than yours.** The whole list, two days, or the traffic-carrying subset first, one afternoon, on the grounds that an address with no clicks and no impressions is worth less to protect at cutover. Code's recommendation is the traffic-carrying subset first with the tail afterwards, because it puts the answer in front of the redirect work days earlier and loses nothing.

OWED BACK: nothing. The URL Inspection run itself is owed once it is scheduled.

*No em or en dashes in this file; checked before writing.*
