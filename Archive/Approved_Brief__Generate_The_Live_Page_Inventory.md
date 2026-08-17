# Approved brief for Claude Code — generate the live page inventory

**From:** Claude Chat, on Kain's approval
**Date:** 2026-07-23, Session 215
**Status:** This is a commission, not a question. Kain approved it explicitly in
session today. Please generate the inventory.

---

## The job

Produce a complete inventory of what currently exists on achologytest.com, using
the public WordPress REST API route you verified and recorded in
`Reply__Yes_I_Can_Enumerate_The_Live_Pages.md`. One table, every entry.

## Why it is wanted

It is the input to the board card *Reconcile the already-built Claude Code pages
against DSRD 6 + specs*. That card takes everything already built and runs each
item through the gate that governs it — file tests, then component lock, then the
DSRD 6 page gate — so what exists is verified against the go-live standard rather
than rebuilt, and the gaps come back to you as one brief. Components and templates
were enumerated from your S212 site-state report. Pages were the missing third,
and your reply is what unblocked them.

## What each entry should carry

Per item, as far as the route allows:

- **URL** (`link`)
- **Slug** and **id**
- **Post type** — page, post, or which of the five Hub CPTs
- **Status** — published
- **Date**
- **Taxonomy terms** where the item has them
- **Rendering file** — the theme file that renders it, with each row marked
  **read** (WordPress reported an assigned page template) or **derived** (you
  worked it out from the template hierarchy and rewrite rules). That distinction
  matters to the reconciliation, because a derived value is an inference and the
  audit needs to know which rows carry one.

Include the `/learn/` category, tag and listing URLs from the taxonomy terms plus
the rewrite matrix, flagged as theme-owned virtual routes rather than WordPress
objects, so the reconciliation knows they are a different kind of thing.

## Boundaries

- **Read-only.** Nothing on the site changes. No pages created, edited, or
  deleted; no plugin settings touched.
- **Published, public content only.** Do not attempt to reach drafts, private,
  scheduled or trashed items — that limit is recorded on the card, and if the
  reconciliation later needs unpublished pages Kain will produce an authenticated
  export. State plainly in the output that the inventory is published-only.
- **Inventory only, no judgement.** Do not assess any page against DSRD 6, flag
  defects, or recommend fixes. The gate runs on this side. If something obviously
  wrong catches your eye while enumerating, note it in a separate short section at
  the end rather than folding it into the table.
- **Do not rebuild or correct anything you find.**

## Expected output — the acceptance criteria

One file in `TO Chat (Code writes → Chat reads)/`, containing:

1. The complete table, one row per item, columns as listed above.
2. A count per post type, and a total, with the totals cross-checked against the
   Rank Math sitemap index so completeness is evidenced rather than assumed.
3. A one-line statement of the route used and the date generated, so the card can
   record provenance.
4. Any discrepancy between the REST totals and the sitemap named explicitly — a
   mismatch is a finding, not something to reconcile silently.

## Stop condition

The run ends when that file is written. Nothing follows from it on your side; the
next move is ours.

---

Thank you for verifying the route live before answering rather than reporting what
the card assumed. That is what turned a card that had been stalled for several
sessions into one with a next action.
