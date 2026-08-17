# Verified live — v0.36.16 to v0.36.19

From: Claude Code · 2026-07-23. Kain uploaded the zip; staging now runs
v0.36.19. Everything below is read off the rendered pages, not reasoned from CSS.

## The hairlines (v0.36.16, v0.36.17)

`/policies/refund-policy/`, both carriers:

| | Desktop 1440 | Phone 375 |
|---|---|---|
| Header hairline | 48 above / 48 below | 32 / 32 |
| Endnote hairline | 48 above / 48 below | 32 / 32 |

DSRD 7 §4.3's default tier, on both, at both widths.

**Controls, unmoved as intended.** The Code of Ethics kept all six of its
hairlines: header 32, three section rules at 32/32, the Aristotle host at 32/32,
Related Questions at 48/48. The 404 kept 43 above and 48 below at its header,
your recorded optical correction, and 48/48 at its Related Questions block.

## The Related Questions block on /about/ (v0.36.18)

48 above and 48 below, at 1440 and at 375. It was 32/32. The Code of Ethics reads
48/48 at both widths, so the two pages now agree, which is what §4.3's
own-standard clause asks for. The rest of the About page did not move: header
32/32, the ruled body's rule 32/32.

## One Article block per article page (v0.36.19)

Rank Math's Article node and its `#author` Person node are both gone. Its
Organization, WebSite, ImageObject and WebPage nodes remain. The page now emits
one Article, the theme's, with the author reading **Kain Ramsay** and linking to
the author profile, instead of "Achology Admin" with a Gravatar.

**The graph is fully connected.** I enumerated every `@id` node and every bare
`@id` reference on the page: four references, all four resolve.

  isPartOf -> #website ...... OK
  isPartOf -> #webpage ...... OK
  primaryImageOfPage -> ..... OK
  publisher -> #organization  OK

No orphaned Person, no dangling reference left by the removal.

## Sweep

Seven page types fetched: `/about/`, `/policies/`, a policy page, the Code of
Ethics, `/help/`, an author profile and the article. All HTTP 200, no PHP fatal,
warning, notice or deprecation in any response, and every schema block parses.
Every About page image returns 200 with real bytes, including the five video
thumbnails.

`/help/` still shows the split you have yet to rule on: Rank Math's
CollectionPage with the theme's BreadcrumbList. Decisions (b), (c) and (d) in
`Report__Per_Page_Type_Schema_Inventory.md` §3 are unchanged and still with you.
