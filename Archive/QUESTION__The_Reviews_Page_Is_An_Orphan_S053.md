# QUESTION: the Reviews page is an orphan, and no document says what should link to it

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.57.3.
**Why now:** Kain asked me to confirm the page is live, connected and linked to where it needs to be, before any new work. It is live. It is not connected.

## The finding

**Nothing anywhere on the site links to `/reviews/`.** Checked three ways, because one way is a guess:

1. **The theme.** No file outside the page's own six contains `/reviews/`. The header and footer templates carry no Reviews link and no Reviews label.
2. **WordPress navigation.** `wp menu list` returns an empty table. The site has no menus at all, so navigation is entirely theme-driven and point 1 is the whole answer for it.
3. **Content.** No published post or page contains `/reviews/` in its body.

DSRD 6 §5 item 7: "At least one other page on the site links to this one, from its category hub, its listing page, a related-reading block, or another page's cross-links, as DSRD 1's cross-linking plan assigns. A page nothing points to is an orphan: search engines may never find it, and no reputation flows into it from the rest of the site."

So the page fails that line, and it is the only new failure the second pass found.

## Why I have not fixed it

**DSRD 1 §6.1's cross-linking matrix assigns nothing to this page.** Every row in it covers a Knowledge Hub content type: quote pages, book note pages, author hubs, tag landing pages, school pages, the courses directory. There is no row for the proof and funnel group, and §6.3 explicitly closes course pages to cross-linking, which removes the one placement I would otherwise have assumed.

**And the placement is a funnel decision, not a technical one.** Which pages carry a link to 4,517 verified reviews, and where on those pages it sits, is DSRD 4's ground and Kain's call. Adding it to the footer because a footer is convenient would be me making a CRO decision by default, which is the thing I am not to do.

**One related note.** DSRD 1 §10 already lists reviews in `sitemap-pages.xml`, so the page is meant to be found. That makes the missing inbound link more clearly an omission than a deliberate choice.

## What I need

**One ruling naming the pages that link to `/reviews/`, and the wording of the link.** My own reading, offered as a starting point and not as a recommendation I would act on unasked: the About page and the Testimonials page are the obvious neighbours, since both are already proof pages and both already link outward; the homepage is the highest-value placement and the one most likely to need Kain's eye rather than a rule; and the footer is the cheap sitewide answer that guarantees the page is never orphaned again.

Once the ruling exists I can build it in one change set, and it closes the last item on this gate that is mine to close.

## Where this leaves the gate

Seven items still stand between this page and ready. Four closed at this second pass: the tracking question resolved as correct-by-design against DSRD 3 §6.5, the redirect line as not-applicable against DSRD 1 §11, uniqueness as a pass against `/testimonials/`, and the page confirmed live and published. The full record is in `GATE__DSRD6_Reviews_Page_S053.md`, second pass marked in place.

Of the seven, **four are yours**: the title and meta description, DSRD 8 naming the global impact block and the review archive, DSRD 6 §12 naming the proof and funnel page group, and the two §1 acronym exceptions. **This orphan question is yours and Kain's together.** Two are mine: PageSpeed Insights, which was attempted today and blocked by the API's daily quota, and the usability walk, which §8 forbids the builder to run in the same sitting.

*No em or en dashes in this file; checked before writing.*
