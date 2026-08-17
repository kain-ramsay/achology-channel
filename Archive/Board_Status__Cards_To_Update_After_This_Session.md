# Board status — cards to close / update after this session (2026-07-24)

From: Claude Code · for Chat to action on the Notion board (Chat owns the board).
Kain asked at close which cards moved. Here they are.

## Mark DONE
- **Confirm Reviews & Testimonials Content-Type ACF + Reconcile the Full
  Content-Type Inventory** — delivered. See
  `Report__Content_Type_Inventory_Reconciled_And_Reviews_Confirmed.md`. Reviews
  type confirmed; testimonials confirmed as intentionally not-a-CPT; inventory
  reconciled; name-display locked (first name + initial); per-review country
  dropped on integrity grounds; topic-tag approach decided.
- **Learner / review figures locked → About page** — shipped v0.36.26,
  **verified live**. About page reads 695,578 / 175,162 throughout.
- **"Where next?" panel → library component (S219)** — shipped v0.36.27,
  **verified live** (schema unaffected; CSS move only, pixel-identical intended).

## Update (progressed, not fully closed)
- **Schema ownership settled (S219)** — applied to all existing templates and
  **verified live** (one CollectionPage + one BreadcrumbList each; Rank Math
  duplicates gone; Our People no Person; #organization name/legalName fixed).
  Residual, recorded pending-build: `/learn/` home + KH **listing** pages
  (I need the listing-page breadcrumb trails confirmed — see the ship brief),
  plus two polish items from live verification (a same-@id org/website tidy to
  bundle next ship, and a Rank Math WebSite-name setting). See
  `Verification__v0.36.27_Schema_Live.md`.
- **Rank Math WP SEO Plugin Configuration — Planning & Implementation** —
  **planning half done**: full click-by-click runbook filed
  (`Runbook__Rank_Math_Configuration_Session.md`). Implementation (dashboard
  settings) pending; I can now assist directly, see access note below.
- **SiteGround Dynamic Cache Configured + Verified** — executor correction
  confirmed with live evidence: **SG Optimizer (sg-cachepress 7.8.0) IS installed
  and active** on the build site, so the toggle is reachable from WP admin /
  WP-CLI. **Not Pooka's** for the build site. With the new SSH access I can now
  check and set it. Suggest re-pointing the executor and letting me verify.
- **Icon Standardisation (raw SVG → Lucide)** — my cost answer is delivered
  (`Answer__Icon_Standardisation_Cost.md`): recommendation is the rule should
  bend to "named Lucide glyph, inline delivery OK". The card's trigger (my
  answer) is met; it now needs **Kain's ruling**.

## New (worth a card, or note on the infra card)
- **Claude Code now has direct SSH + WP-CLI access to achologytest.com**
  (set up with Kain today). This ends the "can't see the live site" block and is
  what made today's live schema verification possible. Reads free; live changes
  shown to Kain first.

## No action from me needed
- Help-article import heads-up — understood; the slug-match constraint is logged
  for when I build that importer. Nothing to change now.
