# Commission for Chat — write the 51 missing help articles (full data, not just copy)

From: Claude Code · 2026-07-23 · commissioned by Kain. Companion to
`Brief__FAQ_Gap_Analysis_From_The_Obsidian_Vault.md`, which explains how the
51 were found. This note is the instruction set.

---

## The job

Fill out **every field** for 51 new help articles in:

`010. Achology Help & FAQ System/Achology FAQ — Missing Question Gap Analysis (from Obsidian Vault).csv`

This is not 51 pieces of copy. It is 51 complete rows, carrying the same data
as the original 200, so they import through the same path. Kain's expectation
is that this is deliverable in one or two sessions.

---

## 1. One important correction before you start: no pen names on these

Help articles are **deliberately institutional and unsigned**. This is fixed
in two places:

- **DSRD 1 §3.3** (FAQ Article Type): "No author attribution, institutional
  answers."
- **DSRD 6 §12**: help articles are exempted from the author line; the visible
  date stays.

So do **not** assign Amelia, Declan, Jackson or any other editorial voice to
these 51. The pen names govern Knowledge Hub content (articles, book notes,
quotes), not `/help/`. Write in the **base Achology voice**. Flagging this
because Kain mentioned the pen names being ready, and they are, just not for
this content type.

---

## 2. Where the answers come from

Each row names its source in **`vault_source_note`**. That note in
`02-Achology/` holds the facts for that answer. The vault is the factual
authority here.

Three hard rules:

1. **Do not invent facts.** Every number, level name, credit rule, price and
   date comes from the named note. If the note does not answer it fully, say
   so in the row rather than filling the gap with plausible wording.
2. **Respect the vault's own "known source discrepancies" sections.** The CCaC
   and Code of Ethics notes explicitly record defects that must not be
   reproduced (the mismatched virtue excess/deficiency labels for Wisdom,
   Friendliness and Truthfulness, and the incorrect publisher name on the
   copyright page). Do not carry those errors into published copy.
3. **Never contradict the published policies.** Where an answer touches
   refunds, privacy, terms or disclaimers, the full-text policy notes win.

---

## 3. What is already filled, and what is yours

**Pre-filled by me (leave alone unless wrong):** `id`, `category`,
`category_slug`, `title`, `slug`, `url`, and every field constant across all
200 (`cta_type`, `schema_types`, `rm_robots`, `rm_advanced_robots`,
`rm_is_pillar_content`). `has_audio` is `no` until MP3s are produced.

**Yours to author:**
`seo_title` · `meta_description` · `excerpt` · `answer_text_full` ·
`answer_html_full` · `rm_seo_title` · `rm_seo_description` ·
`rm_focus_keyword` · `related_questions` · `related_questions_urls`

**Fills in after the article exists:** `word_count`, `headings_h2_h3`,
`internal_links_count`, `internal_links`, `external_links_count`,
`external_links`, `date_published`, `date_modified`.

**Leave empty:** `canonical` and `rm_canonical_url`. This matches the master
and the standing rule against issuing canonical URLs.

If you change a `slug`, update its `url` to match and re-check the slug is
unique against the 200 existing slugs. Mine are collision-checked as they
stand.

---

## 4. Standards every row must meet

- **No em-dashes. Anywhere.** House copy standard, and one Kain has had to
  enforce repeatedly. Use commas, colons or periods. Hyphens in genuine
  compounds are fine.
- **`rm_focus_keyword` must be globally unique.** Two sets are already taken:
  the **200 article keywords** in the master, and the **15 category keywords**
  set today, each of the form `achology <topic> questions`. Check any new
  keyword against both before using it. Do not reuse a category keyword.
- **`meta_description` / `rm_seo_description`: 155 characters maximum**
  (DSRD 6 §3.2). The 15 category descriptions had to be rewritten today for
  exactly this reason, so please do not repeat it.
- **`seo_title` / `rm_seo_title`: about 60 characters** (DSRD 6 §3.1).
- **Answer first.** `schema_types` includes `SpeakableSpecification` and
  `Question`/`Answer`, so the direct answer must sit early and in the open,
  not buried after preamble. This is what gets cited by AI answers (DSRD 6 §6).
- **House copy checklist applies** before any row is called done: sounds like
  a person, no banned marketing words, treats the reader as a capable adult,
  answers the question asked.
- Match the structure of the existing 200. Open one of them as a shape
  reference for `answer_html_full` and `headings_h2_h3`.

---

## 5. Suggested order of work

`priority` is set: **33 High, 17 Medium, 1 Low.** Work High first. The High
set clusters into four themes, and doing each theme together will be far
faster than working down the file:

1. **CPD pathway and progression** (statuses, levels, VALTS/PALS/CIPS,
   verification, certificates, Professional Directory)
2. **The CCaC and the ethics framework** (nine virtues, the three conduct
   instruments, green/red status, practitioner commitments)
3. **Curriculum** (28 courses, 7 schools, bundles, three learning paths)
4. **Membership, pricing and refunds** (free tier, monthly vs annual, the
   complimentary-membership behaviour on course purchase and refund)

---

## 6. One sequencing flag

12 rows carry the category name **"Accreditation and Certification"**, Kain's
rename of 2026-07-23. The master still holds the old name "Certificates and
Accreditation"; the slug `certificates-cpd-accreditation` is unchanged. If the
eventual import matches on category name rather than slug, the rename must be
live in WP admin first. Slug-based matching is unaffected.

---

## 7. Handing it back

Return the completed CSV to the same folder with the same 48 columns and the
same row order, so I can diff it against the master schema and run the
pre-import checks (uniqueness, lengths, em-dashes, slug collisions) before
anything is imported. Tell me in `FROM Chat` when a batch is ready and I will
verify it.

Kain approves the content before anything is published. Nothing here is a
decision you or I make on his behalf.
