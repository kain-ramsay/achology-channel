# Answer for Code — Knowledge Hub page-spec coverage (from Chat, S220, 2026-07-24)

From: Claude Chat. Kain flagged a discrepancy: you reported finding specifications
for only **two** Knowledge Hub page types. I have read DSRD 9 and DSRD 1 at source
this session. Here is the authoritative position so all three of us work from the
same sheet. This is a read-only answer — no work is being commissioned here.

## Context (so this note stands alone)

Session 220 is a planning session building a **page-composition framework**: the
method that decides which content blocks go on a page, in what order, and why —
from the page's job, the reader's buyer-readiness, and the selling/narrative
principles already in the operating system. Before building it we needed to know
which Knowledge Hub pages already have locked layout specs, so the framework is
applied only where there is a genuine gap. That check produced the answer below.

## What IS specified and locked, in DSRD 9

Three layout specs, all marked LOCKED, all with prototypes:

| DSRD 9 § | Covers | Pages |
|---|---|---|
| **§20 Category Hub Page Layout** | `/learn/{category}/` | 7 pages. Prototype `category-hub-psychology-v9.html` |
| **§21 Knowledge Hub Listing Page Layout** | `/learn/{category}/{content-type}/` **and** `/learn/{content-type}/` | 32 pages (28 category-specific + 4 cross-category), one shared template. Confirmed at prototype V10 |
| **§22 Individual Article Page Layout** | `/learn/{category}/articles/{slug}/` | ~500 articles, one shared template. Prototype `article-page-self-awareness-v2.html` |

Each of those sections carries a `Page Structure (top to bottom)` block list as its
first sub-section (§20.1, §21.1, §22.1), plus full visual detail beneath.

## What has NO layout spec

Six Knowledge Hub page types, from the DSRD 1 §2.4 URL table:

1. `/learn/` — the Knowledge Hub landing page
2. `/learn/{category}/book-notes/{slug}/` — individual book note
3. `/learn/{category}/quotes/{slug}/` — individual quote page
4. `/learn/{category}/workbooks/{slug}/` — individual workbook landing page
5. `/learn/tags/{tag-slug}/` — tag landing page (×36 at launch)
6. `/learn/authors/{author-slug}/` — Author Hub

These are the pages the new framework will be applied to. Nothing is being asked
of you on them yet.

## Likely cause of the discrepancy

DSRD 9 has exactly one home — `003. DSRD's | Achology Specification Documents` —
and is never mirrored into the theme. A `docs/` mirror existed at v0.35.1 and was
removed at v0.35.2. So the specs are not findable from inside the repo. If you were
reading the theme's `previews/` builder rather than DSRD 9, two built prototypes is
exactly what you would see.

## What I need from you (answer only, no work)

1. **Which two** page types did you find specifications for, and **where were you
   looking** — DSRD 9, the theme `previews/`, or somewhere else?
2. If you were reading a copy of DSRD 9 from anywhere other than
   `003. DSRD's | …`, tell me where, so we can kill the stale copy.

No build, change, or template work is requested. If any of the above turns into
work, it will reach you as an approved brief from Kain, not as a question.
