# Ship Brief — v0.36.27 — "Where next?" component + schema ownership (S219)

From: Claude Code · 2026-07-24
Executes two approved S219 briefs in one zip: `Brief__Promote_Where_Next_Panel_To_Component_S219.md`
and `Brief__Schema_Ownership_Settled_S219.md`.

## Part 1 — "Where next?" panel promoted to a library component (DSRD 8 §13)

Moved the whole `.policy-next*` family from `policies.css` §9 to `components.css`
(new SECTION 4), verbatim, no visual change. Markup and class names untouched;
the pages point at it by class.

- Moved: the main block, the `--pair` variant, the `button.policy-next__row`
  variant, the `.policy-body .policy-next*` in-prose overrides, the `--ruled`
  rhythm rules, the phone `@media`, and the `.policy-page--404 .policy-next`
  zeroing (its comment bullet in the 404 §12 header was trimmed to match).
- Left as-is per your instruction: the `.policy-next__icon` orange tint stays
  its raw `rgba(237,105,34,0.07)` — that's the Icon Standardisation card's, not
  this move.

Verified statically: no `.policy-next` rule remains in `policies.css`; both
files brace-balanced; every design token the rules use is defined in `base.css`,
which loads before `components.css`; and the move is cascade-safe (nothing
outside `.policy-next*` selectors targets those elements, so source-order can't
flip). Pixel-identical render + the DSRD 6 page gate on manifesto, Code of
Ethics and 404 confirm on upload.

## Part 2 — Schema ownership (DSRD 10 §9)

**Applied now (templates that exist):**

- **(b) /help/ hub + FAQ category pages** — theme now emits `CollectionPage`
  (added to `archive-faq_article.php` and `taxonomy-faq_category.php`); Rank
  Math's `CollectionPage` and breadcrumb are switched off for the `faq_article`
  archive and the `faq_category` taxonomy in `rank-math-feed.php`. Standard 3
  breach resolved.
- **(c) Knowledge Hub category hubs** — `taxonomy-kh_category.php` now emits
  `CollectionPage` + `BreadcrumbList` (Home > Learn > [Category], mirroring the
  visible trail); Rank Math's `CollectionPage` and breadcrumb switched off for
  the `kh_category` taxonomy.
- **(d) Our People** — `template-our-people.php` now emits `CollectionPage`
  (standard directory treatment), and carries NO `Person` node; the per-profile
  `Person` stays on each author profile. It's a Page template, so Rank Math
  emits nothing there and no dedup filter is needed.
- **(#organization naming)** — `rank-math-feed.php` now sets the org node's
  `name` to "Achology" and adds `legalName` "Achology Transactions Ltd" wherever
  Rank Math prints the graph. The theme's own org references already said
  "Achology", so one `@id` no longer carries two names.

**Recorded pending-build (no template yet, or trail not unambiguous — not
touched, so no trail was invented):**

- `/learn/` home — no template built yet. The rule is recorded; applied when the
  template is built.
- Knowledge Hub **listing** pages (`learn-listing.php`: `/learn/{category}/{type}/`
  and the cross-category `/learn/{type}/`). DSRD 1 §9 gives the per-content-type
  trails but not the listing-page trail directly, and the cross-category listing
  trail isn't stated. I did not guess it. **Need from Chat:** confirm the exact
  trails for these two listing shapes (my read: per-category =
  Home > Learn > [Category] > [Type]; cross-category = Home > Learn > [Type] —
  but that second one is a derivation, not something DSRD 1 §9 states, so I want
  it confirmed before I build it).
- KH tag pages / author hubs — DSRD 10 §9 notes their URLs don't resolve yet;
  left on Rank Math auto, untouched.

## Honest verification note
The RM `CollectionPage` removal fires on an archive and two taxonomy terms —
the first pages where we strip a node from Rank Math's live graph rather than a
page where it emits nothing. Static analysis is clean, but the page gate on
upload should confirm each of `/help/`, a FAQ category, and a KH category emits
**exactly one** `CollectionPage` and **one** `BreadcrumbList`, with no dangling
`@id` reference left behind. I can't see RM's runtime graph from here.

## State
Version 0.36.26 → **0.36.27**. Zip rebuilt, previews/ and .git excluded. Both
jobs in the one upload, as Kain asked.
