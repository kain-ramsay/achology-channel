# Answer for Code — Knowledge Hub listing breadcrumb trails, now LOCKED (from Chat, S220, 2026-07-24)

From: Claude Chat. This supersedes the holding reply
`Reply__KH_Listing_Breadcrumb_Trails_S219.md`. Both trails are now settled and
written into DSRD 1 §9. This is a read-only answer — no work is commissioned here.

## Context (so this note stands alone)

You were blocked on the breadcrumb trail for the Knowledge Hub listing pages,
which DSRD 1 §9's breadcrumb table did not cover. Kain and I settled it this
session against DSRD 1 §9's own governing rule — **breadcrumbs mirror the URL
hierarchy exactly** — and Kain has approved both trails.

## The locked trails

| Page type | URL pattern | Breadcrumb trail |
|---|---|---|
| Knowledge Hub listing page (per category) | `/learn/{category}/{content-type}/` | `Home > Learn > [Category] > [Content Type]` |
| Knowledge Hub listing page (cross-category) | `/learn/{content-type}/` | `Home > Learn > [Content Type]` |

Worked examples:

- `/learn/psychology/articles/` → `Home > Learn > Psychology > Articles`
- `/learn/articles/` → `Home > Learn > Articles`
- `/learn/psychology/book-notes/` → `Home > Learn > Psychology > Book Notes`
- `/learn/quotes/` → `Home > Learn > Quotes`

## Where this is now recorded

DSRD 1 §9, at its one home
(`003. DSRD's | Achology Specification Documents / DSRD 1. Site Architecture &
Taxonomy Rules (URLS)`). Two rows were added to the breadcrumb table, immediately
below the Workbook page row. Read them there rather than from this note if the two
ever disagree — DSRD 1 is the source, this note is the message.

## Rules that apply to both trails

These come from DSRD 1 §9's existing document-level rules, not from anything new:

- Separator is the right chevron (`>`). In the built markup the visual separator is
  the Lucide `ChevronRight` glyph rather than a text character, per DSRD 9 §20.3.
- Every segment except the current page is a clickable link. The final segment (the
  content type on a listing page) is the current page and is not linked.
- `Home` links to `/`, `Learn` links to `/learn/`, and on the per-category trail
  `[Category]` links to `/learn/{category}/`.
- `[Content Type]` renders as the display label — Articles, Book Notes, Quotes,
  Workbooks — not as the URL slug.

## Consistency check already run

The category hub trail locked in DSRD 9 §20.3 is `Home > Learn > [Category]`. The
per-category listing trail is that trail plus one segment, and the individual
article trail (`Home > Learn > [Category] > Articles > [Article Title]`) is the
listing trail plus its leaf. The three are consistent by construction, which is
what the URL-mirroring rule is there to guarantee.

## Related, for your awareness only

DSRD 1 §2.4 lists ten Knowledge Hub page types. Three have locked layout
specifications in DSRD 9 (§20 category hub, §21 listing pages, §22 individual
article). The remaining six — the `/learn/` landing page, individual book note,
individual quote, individual workbook, tag landing page, and Author Hub — have no
layout specification yet. Composing them is now a board card and will come to you
as an approved brief when their specifications exist. Nothing is asked of you on
them now.
