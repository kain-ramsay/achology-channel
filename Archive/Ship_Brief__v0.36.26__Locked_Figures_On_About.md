# Ship Brief — v0.36.26 — the locked figures land on the About page

From: Claude Code · 2026-07-24
Executes `Brief__Learner_And_Review_Figures_Locked__Update_The_About_Page.md`.

## What changed

The About page now carries **695,578 learners** and **175,162 ratings**
everywhere, exact figures, no plus sign. All old forms retired.

`page-about.php`
- Lead paragraph (L58): "more than 670,000 students" → "695,578 students".
  Kain approved dropping "more than" since it no longer fits an exact number.
- Timeline lede (L160): "670,000 students strong" → "695,578 students strong".
- 2025/26 milestone stat (L320): `data-count` 670000→695578, suffix `+` removed,
  visible text "670,000+" → "695,578".
- Terminus line (L330): "670,000+ mature learners" → "695,578 mature learners".
- Statistics panel (L343): Total Student Ratings 171,306 → 175,162.
- `AboutPage` schema description (L604): 670,000 → 695,578.

`about.js`
- Era-chart final data point `[2026, 670]` → `[2026, 695.578]`, so the live
  counter and odometer scrub land on 695,578.
- Removed the odometer's hardcoded `'670,000+'` snap string and its two
  threshold numbers; the counter now simply formats the exact figure.

Version bumped 0.36.25 → **0.36.26** (single-sourced from style.css, so the
about.js change is cache-busted too). Zip rebuilt, previews/ and .git excluded.

## Sitewide consistency check (Kain asked)

I swept the **whole theme**, not just the About page: every 6-figure
comma-number, and every template mentioning students/learners/ratings. Result:
the only learner/rating figures in the theme were on the About page, and they
are now all correct. The 100,000 / 350,000 / 500,000 on the timeline are
historical era milestones and were correctly left alone. Policy-page mentions of
"learners/ratings" are generic prose with no numbers.

**One boundary Kain should know:** this covers theme templates only. Any figure
typed into WordPress **page content** (homepage, membership, sales copy) lives
in the database, not these files, so it is outside what I can grep from here and
outside my remit (Kain owns the pages). If a stale number shows anywhere on the
live site that is not the About page, it is editor content, not the theme.

## Left for Kain
- The About page **Rank Math meta description** must be updated to match the new
  schema description or the two drift: "About Achology: a decade teaching
  applied psychology to 695,578 students in 216 countries. What we teach, what
  we stand for, and who it's for."
- 872,284 enrolments: untouched, as you flagged.

## Verify on upload
achologytest.com/about/ — the stat panel, terminus and timeline should all read
695,578 / 175,162, and scrubbing the timeline should land the counter on 695,578
with no "+".
