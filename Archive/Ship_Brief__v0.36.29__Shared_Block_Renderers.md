# Ship Brief: v0.36.29, the shared block renderers

**Date:** 2026-07-27
**Zip:** rebuilt at `../achology.zip`, awaiting Kain's upload
**Trigger:** Kain asked how we stop re-hand-building blocks on every new page.

## What changed and why

The theme had no mechanism for sharing markup. Not one `get_template_part`
call, and no shared renderer for page blocks. Shared CSS was possible, shared
HTML was not, so every reuse was a copy-paste and every copy drifted. That is
the whole reason a second page carrying an existing block has been costing
hours.

DSRD 8 §12.3 already sets out the promotion procedure. When /testimonials/
became the second page needing the routes grid and the member-story strip,
they should have been promoted. They were copied instead. This ship corrects
that and puts the missing plumbing in.

### New file: `shared-parts.php`

The site-wide block renderers, following the existing `*-parts.php` house
pattern (`achology_*` functions taking an `$args` array, required from
functions.php). It holds:

1. **A site-wide icon registry** — `achology_icon( $name, $attrs )`. The ten
   Knowledge Hub glyphs moved here from knowledge-hub-parts.php, plus the nine
   the routes grid was hand-pasting. `achology_kh_icon()` is now a thin
   wrapper, so nothing that called it had to change. No template hand-pastes
   SVG path data any more.
2. **`achology_routes_grid( $args )`** — the "Explore and Experience Achology
   for Yourself" block. Variant set, derived from reading both uses as §12.3
   step 1 requires: `tone` (dark/orange/slate/tint), `size` (lead/tall),
   `bg` (accred/schools/hub), optional inset `image`, optional `paths` list.
3. **`achology_member_stories( $args )`** — the five-clip video strip, with
   the footnote optional.
4. **The shared content sets** — `achology_site_routes()` (the ten routes) and
   `achology_member_story_cards()` (the five clips). Both pages draw from
   these, so a copy edit to a route or a clip now lands on every page that
   shows it in one edit. That was Kain's explicit ask.

A school page's routes grid is now a data array plus one call, not a rebuild.

### CSS promoted

`about.css` §5 and the routes-grid rules moved into `components.css` as a new
§4A (§12.3 step 3). Verified: 340 rules before, 340 after, identical set.
components.css is enqueued site-wide, so the blocks now work on any page.

### Preview builders

Both builders kept their own private copy of these blocks, which is the same
drift problem one level down, and the About builder's copy had already
diverged from the theme. They now render the real `shared-parts.php` through
PHP (`previews/_php_render.py`; there is no PHP on Kain's Mac, so it renders
over SSH on the build site and caches locally).

Two real drifts this surfaced and fixed:
- The **testimonials preview** was showing a "visit our Member Testimonials
  page" footnote that the shipped page never had, and which is self-referential
  on that page anyway.
- The **About preview** was showing generic `aria-label="Play member story"`
  and `alt="Achology member story"`, where the page ships the specific
  per-question text.

## Verification

- Every promoted block rendered through the server's PHP 8.2 and diffed
  against the previous markup: **identical** on all four (routes grid and
  member stories, on both pages).
- CSS rule sets before and after the move: **identical**, both files.
- Both previews rebuilt; everything outside the two blocks is byte-identical.
- Measured in the browser at 1440 against the pre-change page: grid columns,
  lead/tall spans, all four icon tones, all three backdrop images and their
  opacity, the bubble mark's left/right, the six-column proof strip. **Every
  value matches.**
- `php -l` clean on all five changed PHP files. All preview images confirmed
  loaded, no THEMEURI leftovers.

## What I need from Chat

**DSRD 8 needs updating and I do not edit DSRDs.** §12.3 steps 2 and 4 are
yours:

1. Write the two promoted blocks into DSRD 8 as numbered component sections
   with their locked anatomy and the variant sets recorded above.
2. Remove "Member stories" and "Routes grid" from the §12.1 page-local table,
   noting where they went.

Two remaining §12.1 reuse candidates are **not** promoted yet, deliberately:
the question selector (`.pfq*`) and the statistics panel (`.story-proof*`).
§12.2 says the stats panel needs its DSRD 4 proof-block assignment reconciled
first, and the question selector needs comparing against the /help/ question
door before either is promoted. Both are still one-page blocks, so promotion
would be premature under §12.3.

**One contradiction to put to Kain.** He wants the Achology story scroll (the
timeline window, dark stage, timeline rows, era chart, odometer) on all the
school pages. DSRD 8 §12.1 marks every one of those "page-local, permanent".
Reusing it contradicts the spec as written. That needs a decision from Kain and
then a DSRD amendment, not a quiet build.

---

## Addendum, same ship: the container setting

Kain raised that the site runs two container widths (DSRD 7: 880 reading
column for informative pages, 1200 page container for product/home/menu
pages) and asked how a promoted block crosses between them without skewing.

Measured first, on the real block: dropped into the wide container as it was,
nothing broke or overflowed, but each card inflated from 283 to 336, a fifth
wider than drawn. Four columns instead pulls them down to 248. Neither is
free, and the ten-card composition (lead spanning two columns, tall spanning
two rows) is tuned to exactly three columns.

`achology_routes_grid()` now takes **`container`**: `'article'` (default,
byte-identical to today) or `'page'`. On `'page'` the panel widens to the page
container but the heading, lead and card row stay pinned to
`--container-article`, so the block is the same object in a wider frame.

**The guarantee, measured.** A comparison page renders both side by side:
`previews/routes-grid-container-test.html`. Across 700 measurements per
breakpoint (23 selectors x 28 computed properties, plus every one of the ten
card boxes) at 375, 834, 1259 and 1440: **zero differences**. Panel frame 944
vs 1104, content width 880 in both, block height identical to 5 decimal
places. Below 1024 the two are literally the same, as the variant is
desktop-only. All images and all three backdrop layers confirmed loaded.

**Still owed to Kain:** the genuine full-width arrangement (four across, or
larger cards, with the lead/tall cards re-placed). Until he designs that with
us, a wide page gets the undistorted block rather than a stretched one. This
is deliberate, not an oversight.
