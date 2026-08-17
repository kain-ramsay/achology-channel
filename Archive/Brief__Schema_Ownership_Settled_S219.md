# BUILD BRIEF — Schema ownership settled (S219)

**From:** Claude Chat · **To:** Claude Code · **Date:** 24 July 2026 · **Status:** approved by Kain

## Why you're getting this

At S218 the per-page-type schema inventory (theme v0.36.15) left four schema-ownership questions open — three were "which source owns this page type", one was a naming conflict. Kain ruled all four at S219. They are now written into **DSRD 10 §9** (the schema table plus the two blocks beneath it, "Three decisions, ruled S219" and "The naming conflict, ruled S219") in `003. DSRD's | … / DSRD 10. Developer Handoff Instructions / DSRD_10_Implementation_Spec.md`. That file is the source of truth; this brief is the implementation ask.

This is a read-and-build commission, not a question. Everything needed to build is here.

## What was decided, and what to build

**1. `/help/` (help hub archive) and the FAQ category pages — theme owns both.**
Today these split their source: Rank Math emits `CollectionPage`, the theme emits `BreadcrumbList` — a Standard 3 breach. Change: the theme owns `CollectionPage` **and** `BreadcrumbList` on both. Switch Rank Math's `CollectionPage` off for these page types so only one block of each type ships (Standard 2).

**2. `/learn/` home, the 7 category hubs, and the 32 listing pages — theme owns both.**
Today Rank Math gives a `CollectionPage` and no trail; the theme emits nothing. Change: the theme owns `CollectionPage` + `BreadcrumbList`, switching Rank Math's `CollectionPage` off. The breadcrumb trail for every one of these is specified in **DSRD 1 §9** — read it from there; never invent a trail.

**3. Our People (`/about/instructors/`) — standard directory treatment; `Person` retired to the profiles.**
Today it emits a bare `BreadcrumbList`. The old row promised `WebPage` + a `Person` node per profile — that promise is retired. Change: give the hub theme-owned `CollectionPage` + `BreadcrumbList` (same shape as the other directory pages). Do **not** add `Person` nodes to the hub — the `Person` node stays on each individual author profile page, which is its correct home and already ships there.

**4. `#organization` naming — `name` = "Achology", `legalName` = "Achology Transactions Ltd".**
Today Rank Math names `#organization` "Achology Transactions Ltd" and the theme names the same `@id` "Achology" — one identifier, two names across the graph. Change: the public-facing `name` is **Achology** (the brand people search); **Achology Transactions Ltd** (the entity registered at Companies House, UK) is carried as a separate `legalName` property, not as the display name. Ensure only one `#organization` `name` exists across the whole site graph — align Rank Math's value to "Achology", or switch Rank Math's `#organization` name off in favour of the theme's block. `name` and `legalName` are distinct schema.org properties; both stay true.

## Acceptance criteria

- On `/help/`, the FAQ category pages, `/learn/` home, the category hubs, the listing pages, and `/about/instructors/`: exactly one theme-sourced `CollectionPage` and one theme-sourced `BreadcrumbList` ship, with Rank Math's duplicate `CollectionPage` switched off (Standard 2 dedup holds).
- Every breadcrumb trail matches DSRD 1 §9 exactly.
- `/about/instructors/` emits `CollectionPage` + `BreadcrumbList` and **no** `Person` node; author profile pages continue to emit their own `Person`.
- Across the site graph, `#organization` carries a single `name` ("Achology") plus `legalName` ("Achology Transactions Ltd"); no page emits two conflicting `#organization` names.

## Dependencies and sequencing

- No blocking dependency. Apply to each page type where its template already exists. Where a target template is not yet built (some `/learn/` listing/category pages, Our People), this brief is the spec that template is built to — the rule is recorded now and applied at build time.
- Trails and URLs come from DSRD 1; product/name facts are as stated above. No design, content, or architectural choices are left open.

## Definition of done

Each affected page type passes the **DSRD 6 page gate** once built/verified, with the per-chapter record returned. Confirm back on this channel (write to `TO Chat`) which page types you applied it to now and which are recorded-pending-build.
