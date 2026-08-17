**DISPOSITION (S275, written at archive):** read at the S275 close. Board card moved: Hosting & Go-Live | Pooka & Co, SiteGround, Domain Switch, whose Connections now carry this file's whole switch-on list, the Google Analytics hazard (G-HJ29S4Z0R8), and the content pipeline widget with its trigger (Kain-approved, S275). Two decisions it carried were ruled by Kain: the pipeline widget is dispositioned to that card and not commissioned; the Activity and Events widgets are removed. Both rulings travelled to Code in RULINGS__S059_Addenda_Answered_S275.md (FROM Chat).

# CUTOVER ITEM: capability already bought and switched off, and one thing that must stay off

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Written on:** Kain's question, in session, about what a dashboard should carry once the site is live, and his instruction to file it as a cutover item.
**For the board:** the cutover card. Nothing here is commissioned and nothing has been switched on.

---

## The finding, before the recommendation

Kain asked what the site would benefit from having on its dashboard after launch, naming image optimisation, security and analytics as guesses. **Most of it is already installed and dormant**, measured on the server this session:

| Capability | State | Where it already lives |
|---|---|---|
| Image compression, WebP conversion, lazy loading | **all three unset** | SiteGround Speed Optimizer |
| Security hardening and monitoring | installed and active | SiteGround Security Optimizer |
| Google Analytics, with the **live** property already configured | **module off** | Rank Math SEO Pro |
| Search Console query data | module off | Rank Math SEO Pro |
| 404 monitoring and redirections | active and reporting | Rank Math, on the dashboard now |

**So the honest answer to his question is that nothing needs buying.** What needs doing is switching on what is already paid for, in the right order, on the right day.

## THE ONE THAT MUST STAY OFF UNTIL CUTOVER, and it is a real hazard

`rank_math_google_analytic_options` on the build ground already holds **the live site's Google Analytics property**: measurement ID `G-HJ29S4Z0R8`, stream name `achology.com`, account `228691851`.

**The Analytics module is currently off, and that is the only thing preventing the test site from reporting into the live site's analytics.** If anyone enables it here to "see the dashboard working", achologytest.com traffic starts landing in achology.com's data, and the pollution is not retrospectively separable.

This belongs beside the noindex carve-out as a build-ground rule rather than a defect: the configuration is correct for the live site and correctly inert here. **It is enabled once, on the live domain, at cutover, and never before.**

## The order at cutover

1. **Indexing on.** `blog_public` from 0 to 1. This is the one that must not be done early and must not be forgotten late, and it is already carried by `RULING__Noindex_Sitemap_Fails_Are_Build_Ground_Exceptions_S272`.
2. **Rank Math Analytics and Search Console connected**, on the live domain only, per the hazard above.
3. **Speed Optimizer's image handling on**: compression, WebP, lazy loading. Done after the content is final, since it processes what is there.
4. **Re-run the checks that could not run on the build ground**: the DSRD 6 §4 schema check, which is permanently blocked here by the captcha wall, and the indexing consistency reading.

## What actually belongs on the dashboard, and what does not

Kain's own words on why he asked: every dashboard a developer has handed him has been a mess. That is the useful frame, and the answer is not a longer list of widgets.

**The test worth applying: would he do something differently because of this number?** If not, it is furniture. Three things pass it.

**1. Search queries and traffic, from Rank Math.** Already owned. This one matters most because the business model is articles bringing people in, so which questions actually pull traffic is the input to the content plan rather than a vanity figure.

**2. The content pipeline, which no plugin can provide.** How many articles, book notes, quotes and workbooks are draft against published, and how many reviews are unpublished. Achology runs six content types in the thousands. No plugin knows that structure; the theme does. **This is the one thing worth building rather than installing, and it is not built.** If Chat wants it, it needs a commission.

**3. Uptime and broken links as notifications, not widgets.** If the site is down or a link dies, that is a message on a phone, not a box that might be opened. A monitoring service, outside WordPress.

**One thing to not chase: revenue.** Courses sell on Udemy and in the Circle community, not in WordPress, so no honest sales figure can appear on this dashboard and any plugin offering one would be estimating.

## What was done this session, so the board is not surprised

The dashboard was cleared of what is not this project's, on Kain's ruling: the WordPress welcome panel, Quick Draft, and Rank Math's blog adverts, the last removed at its own hook so the widget's useful half survives and the dashboard stops making an HTTP request to rankmath.com to draw.

A brand panel linking to the Circle community was added at the top of the side column, at his request. **The distinction is deliberate and worth recording**: three boxes were removed for being somebody else's marketing, and this one stays because it is a door to a place he works in daily. It passes the same test the others failed.

**Its address is a filter, `achology_community_admin_url`, defaulting to the community root**, because Circle's administration sits behind a path that could not be confirmed without guessing and a shortcut landing on a 404 is worse than none. Kain names the exact admin address and it is a one-line change.

Two widgets remain that fail the test on the same grounds already accepted: **Activity**, which lists recent posts and comments and so is permanently empty, and **WordPress Events and News**, which is the logo menu's content in box form. Both were put to Kain and are awaiting his word.

*No em or en dashes in this file; checked before writing.*
