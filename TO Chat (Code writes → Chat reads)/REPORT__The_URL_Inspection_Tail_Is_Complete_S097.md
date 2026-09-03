> **CHAT DISPOSITION, S334: ACTED ON AND ARCHIVED.** Its three findings and its one server error are written onto the Redirect Strategy and Delivery card, along with the warning that the file is append-only so addresses must be counted, never rows. The S311 ruling closes: both printouts exist. The 943 tail addresses needing a decision are recorded there as one decision rather than 943, and the 703 indexed are added to the subset's 768 as the population the map protects at cutover. Kain's one call from this file, named on the card: whether the single 500 on the anna-freud-17 quote address is worth chasing before cutover. Nothing owed back.

# REPORT: the URL inspection tail is complete. 1,770 addresses, every one answered.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** `RULING__URL_Inspection_Subset_First_Then_The_Tail_S311.md`, its second owed printout. The subset's printout was filed at S092.
**Board card:** Redirect Strategy and Delivery.
**The file:** `url-inspection-tail.csv`, in the Search Console and Live Site Exports folder.

---

## The run

The tail set is **1,770 addresses**: every address on the live URL list that was not already in the traffic-carrying subset or the broken list. It stopped at S096 on Google's daily quota, HTTP 429, with 1,700 answered. The quota reset overnight and the last 70 ran this session, all clean.

**1,770 of 1,770 answered. Not one address is left carrying only an error.** Both passes are now filed and the ruling's two printouts exist.

**One thing about reading the file, because it will mislead anybody who counts rows.** It is append-only and resumable, so an address that hit the quota left a 429 row and was answered properly on a later run. The file holds 3,591 rows for 1,770 addresses, and 1,741 of those rows are historic 429s. Counting rows reports half the run as failed. Every figure below counts addresses.

## What Google says about the tail

| Coverage state | Addresses |
|---|---|
| Submitted and indexed | 703 |
| URL is unknown to Google | 484 |
| Discovered, currently not indexed | 459 |
| Crawled, currently not indexed | 121 |
| Alternative page with proper canonical tag | 2 |
| Server error (5xx) | 1 |

By verdict: 703 PASS, 1,067 NEUTRAL. On a sitemap: 860 of 1,770.

## The three findings worth the redirect map's attention

**One. 484 addresses are unknown to Google and on no sitemap, and those two facts are the same 484.** Every single address Google has never seen is also absent from every sitemap. That is not a coincidence and it is not a Google problem: these pages have no route in. For the redirect map it is the cheapest possible finding, because **an address Google has never indexed carries no ranking to protect.** They can be handled as a block rather than one at a time.

**Two. 459 more are discovered and not indexed.** Google knows they exist and has chosen not to index them. They carry no ranking either, but unlike the 484 they are on Google's radar, so a redirect on them is worth having and a 404 is worth avoiding.

**Three. 703 are indexed and are the real asset in this set.** Added to the subset's 768, that is the population the map has to protect at cutover.

**So of the 1,770 in the tail, 943 need a decision and 943 of those need it as one decision, not 943.** That is the number worth taking into the planning sitting.

## The one server error

`https://achology.com/achology-quotes/anna-freud-17/` returns a 500 to Google's own fetcher. One address, named rather than swept into a count. Kain's call whether it is worth chasing before cutover.

---

OWED BACK: nothing. Both printouts are filed and the ruling closes.

*No em or en dashes in this file; checked before writing.*
