# Brief for Chat — 51 missing FAQ questions found in the Obsidian vault

From: Claude Code · 2026-07-23 · Kain commissioned this research piece.

**Deliverable:** `010. Achology Help & FAQ System/Achology FAQ — Missing
Question Gap Analysis (from Obsidian Vault).csv` — 51 proposed questions the
help base does not currently answer, each grounded in a named vault note, with
empty columns for you to fill.

## What I did
Kain sent a zip of his Obsidian vault (it lives on his other Mac, so I had no
prior access). I extracted it read-only into scratchpad, never into the
project. 375 notes total. I scoped the relevant corpus deliberately:

- **02-Achology (63 notes)** — the customer-facing factual substance. This is
  the corpus the analysis is built on.
- **01-Operating-System (289 notes)** — excluded. These are Kain's working
  methodology notes (session protocols, drafting methods, DSRD structure).
  They mention Achology because they are about the project, not because they
  hold customer facts.
- **04-Resources (14 notes)** — excluded. External marketing and UX frameworks
  (Hormozi, Miller, Cialdini, Nielsen, WCAG). Not Achology facts.

Every one of the 51 was then machine-checked against all 200 existing FAQ
titles for overlap. The `closest_existing_question` and `overlap_score`
columns show that working, so you can audit my judgement rather than trust it.

## The headline finding
**The entire CPD machinery is documented in forensic detail and almost
entirely unanswered in the help base.** The vault holds the six-status ladder,
the VALTS/PALS/CIPS credit rules with per-role credits, the annual Code of
Ethics training requirement, the CCaC 8-of-10 rolling rule with its green/red
consequences, the SoMAP verification pipeline, the two certificate types, the
Professional Directory, and the UKRLP registration number. The FAQ has six
loosely related questions and none of this detail.

Second: **the Code of Character and Conduct has zero coverage.** Nine
Aristotelian virtues, five community principles, and an explicit warning that
the CCaC, the Code of Ethics and the Community Code of Conduct must not be
conflated — which is precisely the confusion a reader arrives with.

Third: **Curriculum and Subject Coverage has only 2 of the 200 questions**,
while the vault documents 28 courses, 7 schools, bundle compositions, shared
courses and three learning paths.

## The file matches the master schema (48 columns)
This is **not** a shortlist, it is an import-ready shell. It carries all **43
columns of the FAQ master** so a finished row can go straight into the same
import path as the original 200, plus 5 research columns at the end
(`why_this_is_a_gap`, `vault_source_note`, `priority`,
`closest_existing_question`, `overlap_score`).

**Already filled by me:** `id`, `category`, `category_slug`, `title`, `slug`,
`url`, and every field that is constant across all 200 (`cta_type`,
`schema_types`, `rm_robots`, `rm_advanced_robots`, `rm_is_pillar_content`).
Slugs are proposals, generated and checked for zero collisions against the 200
existing slugs and against each other. `has_audio` is set to `no` because no
MP3 exists yet; it flips to `yes` when the audio is produced.

**Left for you to author:** `seo_title`, `meta_description`, `excerpt`,
`answer_text_full`, `answer_html_full`, `rm_seo_title`, `rm_seo_description`,
`rm_focus_keyword`, `related_questions` and `related_questions_urls`.
Post-authoring metrics (`word_count`, `headings_h2_h3`, the link counts) and
the two dates get filled once the article exists.

`canonical` and `rm_canonical_url` are deliberately left empty, matching the
master and the house rule against issuing canonical URLs.

**Verified against the master, not assumed:** all 43 master columns are present
in identical order, including the byte-order mark on the `id` header; every
`category_slug` exists in the master; no proposed title duplicates any of the
200; every URL matches the master's format.

**One sequencing flag:** 12 rows carry the category name **"Accreditation and
Certification"**, Kain's rename of 2026-07-23. The master still holds the old
name "Certificates and Accreditation" and the `category_slug`
(`certificates-cpd-accreditation`) is unchanged. If the import matches on
category *name* rather than slug, the rename must be applied in WP admin
first, or those 12 rows will not match an existing term. Slug-based matching
is unaffected.

Two disciplines to carry over when you do:
1. **Focus keywords must be unique.** All 200 article keywords are assigned,
   and the 15 category keywords were set today as `achology <topic>
   questions`. Check any new keyword against both sets before using it.
2. **No em-dashes anywhere in copy.** House standard.

## Caveats, stated plainly
- The vault copy is a snapshot taken today, not a live link. If notes change,
  this analysis ages.
- These are **proposals, not decisions**. Kain rules on which get written.
- I have not drafted answers. Every answer is available in the named source
  note, which is why that column is there.
