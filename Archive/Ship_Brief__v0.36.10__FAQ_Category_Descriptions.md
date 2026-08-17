# Ship brief · v0.36.10 then v0.36.11 · FAQ category descriptions tightened + one rename

From: Claude Code · 2026-07-23 · ship brief (standing practice).

## Correction (v0.36.11 supersedes v0.36.10)
v0.36.10's descriptions used em-dashes in four categories. Achology copy never
uses em-dashes anywhere (house standard), so **v0.36.11** rewrote those four to
use commas, colons and periods instead, keeping title case and the length. Use
**v0.36.11** as the final. All 15 seed descriptions are now free of em and en
dashes; the paste-ready set Kain applies is the corrected one.

## What changed
`faq-setup.php` — the `achology_faq_categories()` seed values, Kain-approved
today:
- **All 15 category descriptions rewritten to ≤155 chars** (were 165–180) and
  **title-cased** (first letter of every word) at Kain's instruction.
- **One category renamed:** `certificates-cpd-accreditation` display name
  "Certificates and Accreditation" → **"Accreditation & CPD"**. Display name
  only — the **slug/URL stays `certificates-cpd-accreditation`**, so the 18
  live article URLs under it are untouched (no redirects needed).

Shipped **v0.36.10**, pushed; Kain uploads the zip.

## Why
The DSRD 6 §3.2 sweep flagged all 15 descriptions over the ~155 limit. Note
these term descriptions do **double duty** — they're both the meta
description *and* the visible hero paragraph on each category page
(`taxonomy-faq_category.php`), so the tightening shortens the on-page intro
too (Kain accepted this), and the title-case now shows on the visible hero as
well.

## Important — this is seed data, not a live change
The seeder is guarded (`term_exists` skips existing terms), so v0.36.10 does
**not** alter the live terms. It keeps the theme's source-of-truth seed
matching the approved copy for any fresh re-seed. **Live application is Kain's
WP-admin edit** to the 15 term Description fields + the one Name — the theme
never overwrites term content by design.

## What I need from you
Nothing blocking. For your records: if your FAQ SEO export in folder 011
holds the old category descriptions/name, they're now superseded by this
approved revision — flag for update when you next touch that export. The
`certificates-cpd-accreditation` slug is unchanged, so nothing in the
redirect map or URL inventory moves.
