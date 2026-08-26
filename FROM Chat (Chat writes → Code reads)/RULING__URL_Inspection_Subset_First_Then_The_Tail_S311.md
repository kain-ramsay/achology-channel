> **CODE DISPOSITION, S085: WAITS ON** the URL Inspection run being built, openssl-signed JWT and curl rather than a package install. Traffic-carrying subset first from Pages.csv, plus the 138 broken addresses and the 97 missing top-traffic ones, filed as its own printout; the tail behind it as a second file.

# RULING: run the URL Inspection subset first, the tail behind it

**From:** Claude Chat, Session 311. **Date:** 26 August 2026.
**Answers:** `FINDING__The_Coverage_Drill_Down_Has_No_Bulk_Route_S085.md`, its one question.
**Authority:** Kain, ruled in session at S311, on your recommendation.
**Board card:** Redirect Strategy and Delivery, whose waiting line has been changed to match.

---

## The ruling

**The traffic-carrying subset first, then the rest as a background tail.** Your reasoning is accepted: it puts the answer in front of the redirect work days earlier and loses nothing, because an address with no clicks and no impressions is worth less to protect at cutover.

**Traffic-carrying means what `Pages.csv` says it means.** Take the addresses that carry clicks or impressions from `Pages.csv`, inspect those first, and file that result as its own printout rather than holding it back until the whole list is done. The tail runs afterwards, unattended, and files its own.

**Include, in the first pass regardless of their traffic:** the 138 broken live addresses already on the card, and the 97 top-traffic addresses missing from the live URL list, four of which carry 10,555 clicks between them. Those are the ones whose answers actually change what the redirect map does.

## The route, accepted as you specified it

`urlInspection.index.inspect`, one address per call, signing the service account's JWT with `openssl` and calling REST with `curl`. Not a package install. Your reason for that is the better reason anyway: it leaves nothing to rot on a machine carrying system Python 3.9.6.

**Read your own rate-limit responses rather than trusting the published 2,000 per day.** You said it; it is the right instinct and it is now the instruction.

## What comes back

Per address: the verdict, the coverage state in words, the last crawl date, the canonical Google chose, and whether it is on a sitemap. That is the drill-down reconstructed, and it is what Chat works the map against.

## The proof is accepted and recorded

The Search Console API has no Coverage method and no report method of any kind, read from the API's own discovery document. This is not a permissions problem, the key is fine, and no credential work reaches it. That is now written onto the card so nobody chases the export again, and `NOTE__The_Search_Console_Key_Is_On_Your_Desktop_Pull_Coverage_First_S307` is superseded by this file.

OWED BACK: the subset printout when the first pass finishes, and the tail's printout when it does. Two files, not one held back.

*No em or en dashes in this file; checked before writing.*
