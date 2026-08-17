# Ship brief — v0.36.9 · Policies index CollectionPage schema

From: Claude Code · 2026-07-23 · a ship brief (new standing practice — see foot).

## What changed
Added theme-owned **CollectionPage** JSON-LD to the `/policies/` index page
(`template-policies-index.php`). Shipped as **v0.36.9**, pushed; Kain uploads
the zip. Its `hasPart` lists the policy pages, sourced from the same builder
(`achology_policy_index_rows()`) the visible list uses, so schema and page
can't drift.

## Why
The DSRD 6 live sweep this session found `/policies/` emitting zero structured
data. Same root cause `/about/` had: Rank Math outputs no JSON-LD on a
template-rendered page with an empty editor, so DSRD 6 §4 (page carries its
type's schema) fails unless the theme owns it. This is now the **established
pattern**: any template-rendered index/structural page needs theme-owned
JSON-LD, because Rank Math can't see it.

## What this means for your reconciliation
- The **About-page schema decision is resolved**: theme owns it, live on
  v0.36.8 (`AboutPage`). That answers the About half of
  `Note_for_Chat__Schema_Findings_for_Page_Checklist.md` — you can close it.
- The same theme-owns pattern now covers `/about/` and `/policies/`. When you
  reconcile schema for other structural pages (the future `/learn/` home,
  category hubs, listings), expect them to need the same — Rank Math won't
  cover template-rendered pages.

## What I need from you
Nothing blocking. One thing to note for when you rule on it: I've
deliberately left **breadcrumb schema** out of these theme-owned blocks
because DSRD 10 / the back-end card scope it to the Rank Math card. If your
reconciliation decides breadcrumb schema should be theme-owned too on these
pages, tell me and I'll add it in the same place.

---

*New standing practice (Kain, 2026-07-23): every zip ship or theme change I
make now gets a short brief like this into `TO Chat` — what changed, why, and
anything I need from you — so your understanding stays current with the build
and you can meet my requests fast. This is the first one.*
