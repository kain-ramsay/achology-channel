# Ship brief — v0.36.28: Member Testimonials page built into the theme (from Code, 2026-07-25)

## What shipped
The Member Testimonials page (`/testimonials/`) is now a real theme template, productionised
from the approved preview. New/changed theme files:
- `page-testimonials.php` — the static template (auto-applies to the page with slug
  `testimonials`; the theme still creates no pages — Kain creates it).
- `testimonials.css` — its styles (the `tm-*` / `lite-*` rules + hairline/bleed overrides),
  lifted from the canonical preview builder. No baked data URIs.
- `testimonials.js` — the question navigator (single-grid FLIP card shuffle) + the video
  lightbox (real Vimeo embed on open, `player.vimeo.com/video/{id}`).
- `images/testimonials/` — 91 member frames (45 avatars + 45 posters + header banner).
- `functions.php` — enqueues about.css on `/testimonials/` too (the two closing blocks reuse
  its grey-block + proof-strip classes), then testimonials.css/js on that page only.
- `style.css` — version 0.36.27 → **0.36.28**.

Verified: PHP + functions.php lint clean on the server, class-name audit clean (79/79 classes
resolve), design verified in Safari across the build. Zip rebuilt (previews/ + .git excluded).
**Not live yet** — Kain uploads the zip and creates the `testimonials` page, then live-verify.

## The page (for your understanding)
Header copied from About (policy-header--doc); a context lead; five FULL-QUESTION buttons
(the real questions, verbatim; soft orange washes on hover/active, no dark slab; the leading
number swells to 20px on the selected one); ONE grid of nine member cards that physically
relocate (FLIP) on question switch, each card its own 293px grey backdrop within a 944 row;
a 56px play badge (page-specific, see below); a video+transcript lightbox. Closes with the
two About blocks ("In Our Students' Words" proof strip + "Explore Achology" 944 grey grid),
copied from page-about.php with real `$ach_uri` paths.

## Things you need to know
1. **The 56px play badge is page-specific and must NOT be reused elsewhere** (Kain's ruling).
   It's oversized for these unique member cards only; the site-wide play-icon standard is a
   separate matter Kain will settle with you. Do not fold this size into a general DSRD rule.
2. **The self-referential proof note was dropped** on this page. On About that strip ends with
   "…visit our Member Testimonials page" linking to `/testimonials/`; on the testimonials page
   that points at itself, so I removed just that `<p class="about-proof__note">` line.
3. **944-bleed drift (repeat of the earlier finding).** The About grey block reaches 944 via a
   `-32px` inline bleed that computes on the LIVE site but is NOT in the local theme source I
   build from. I reproduced 944 for both our grey card row and the copied Explore grid via an
   explicit override, so the page matches what Kain sees on About. The theme source and the
   DSRD still need reconciling on where that bleed rule lives.
4. **Git repo is behind the shipped theme.** The theme's git working tree carries ~9 files of
   prior-session uncommitted drift (about.js, components.css, page-about.php, policies.css,
   rank-math-feed.php, the taxonomy templates, template-our-people.php). I did NOT bundle those
   into my ship (I only touched functions.php, style.css, and the new testimonials files), so
   they remain uncommitted. The zip is correct regardless (built from the working tree), but the
   git history is out of sync with what's actually been shipped and wants a reconciliation pass.

Nothing is asked of you here beyond awareness on 1–4; the play-icon standard (1) and the
944-bleed reconciliation (3) will come to you properly when Kain schedules them.
