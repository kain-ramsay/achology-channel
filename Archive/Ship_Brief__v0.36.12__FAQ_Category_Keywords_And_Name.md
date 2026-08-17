# Ship brief · v0.36.12 · FAQ category #7 rename + focus-keyword strategy

From: Claude Code · 2026-07-23 · ship brief (standing practice).

## What changed (theme, v0.36.12)
`faq-setup.php`: category `certificates-cpd-accreditation` display name is now
**"Accreditation and Certification"** (was "Accreditation & CPD", earlier
"Certificates and Accreditation"). Display name only; slug/URL unchanged.
Seed data, so live application is Kain's WP-admin edit.

## Bigger item: focus keywords for the 15 FAQ categories (not theme code)
The categories had no focus keyword assigned (the folder-010 "FAQ Category
Pages SEO Meta" export shows the `focus_keyword` column empty). Kain and I set
them, with a deliberate architecture decision:

**FAQ category pages target help-intent "... questions" long-tails, not the
commercial head terms.** e.g. `achology membership questions`, not "achology
membership". Every category keyword is `achology <topic> questions`.

Why: a support hub should not compete for the term a money page or pillar
article should win. Leaving "achology membership", "achology pricing",
"achology accreditation" etc. free means future dedicated pages can own them
without cannibalising the category. The "questions" suffix also matches what
the page actually is.

**Uniqueness verified against the real data:** all 15 checked against the 200
live article focus keywords (pulled from the folder-010 master) plus each
other. Zero exact duplicates, zero internal duplicates, zero substring
collisions. My first head-term draft had 5 exact dups and was discarded.

The 15 keywords (slug order): basics / beginner / curriculum / outcomes /
alternatives / learning / accreditation / membership / pricing / refund /
community / events / technical / privacy / partnership, each prefixed
"achology" and suffixed "questions".

## What I need from you
For your records: the folder-010 "FAQ Category Pages SEO Meta" export should
have its empty `focus_keyword` column filled with these 15, and its
`seo_title` / name for category 7 updated to "Accreditation and
Certification". Both are superseded-vs-export items to fold in when you next
touch that file. Nothing blocking.
