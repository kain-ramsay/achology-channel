# RULING: the Watch Member Testimonials card comes off the Reviews page gateway

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**Authority:** Kain, directly in session. Filed per Harness Rule 14.
**Status:** acted on, shipped at v0.60.6, deployed and verified on the live page.

## Kain's words

> "Remove the Watch member testimonials card from this block on the Reviews page RIGHT NOW - I did not approve this!"

He sent a screenshot of the `/reviews/` gateway block with the card in it.

## What was done

The row is filtered out at the Reviews page's own call site in `page-reviews.php`. **`achology_site_routes()` is untouched**, because that shared ten-row set is what the About page's gateway renders from as well, and editing the set to satisfy one page would silently change another (DSRD 3 section 2.6).

Verified on the live pages after deploying: the card is absent from `/reviews/` and still present on `/about/`.

The shape follows the self-link guard already inside `achology_routes_grid()`, which drops a row pointing at the page it is on. That guard is why the row does not appear on `/testimonials/` and did appear on `/reviews/`.

## What Chat needs to write down

1. **The Reviews page's closing gateway carries nine rows, not ten**, and the excluded one is Member Testimonials. That belongs in the page's signed record in the Verified Student Reviews Page folder and wherever DSRD 9 section 29.4 records the as-built block.

2. **How the row got there is worth recording, because it was not a decision anyone took.** The S053 build put the shared ten-row set on this page as "About's own gateway", and the row set gained its Member Testimonials row separately. Nobody chose to put a testimonials card on the reviews page; it arrived with the set. **The general lesson: a page rendering a shared row set inherits every future addition to that set, unapproved.** Whether that is acceptable at the other call sites is worth a look and is not mine to rule.

3. **The Where-next question this reopens.** `PLAN__Reviews_Page.md` section 8 originally gave this page a three-row panel whose third row was Watch Video Testimonials, and that section is already marked superseded. Both routes to a testimonials link from this page are now closed. Whether the page should link to testimonials at all is Kain's, and it is not a gap for anyone to fill quietly.

*No em or en dashes in this file; checked before writing.*
