# REQUEST: everything I need so the 49 import next session, with no further delay

**From:** Claude Code · **Date:** 2026-07-27 · **Re:** the 49 Help articles

Kain has set the import of the 49 as **the agenda for the next session**, and
asked me to request everything needed now so nothing stalls. I have done the
pre-flight checks I can do from my side first, so this asks you only for what I
genuinely cannot answer myself.

---

## A. One defect you need to fix at source, before the file is re-handed

**Two internal links in the 49 point at the two parked Professional Directory
articles.** Once those two rows are stripped, those links land on nothing.

I checked all 78 distinct `/help/` targets referenced across the 49 against the
200 live articles plus the 49 themselves. **76 resolve. Two do not**, and they
are exactly the two being removed:

- `achology-professional-directory-get-listed`
- `would-removed-achology-professional-directory`

They appear in the `related_questions_urls` column of two rows:

| Row | Slug | Dead target(s) |
|---|---|---|
| `GAP-005` | `have-each-year-keep-master-achologist` | `achology-professional-directory-get-listed` |
| `GAP-015` | `have-retake-code-ethics-training-every` | both of the above |

**Please repoint or remove those two references before you re-hand the file.**
I am not editing them here — the file you verify is the file I import, which is
the standard you set in your last note.

---

## B. What I have already confirmed myself, so you do not need to send it

Recorded here so you can correct me if any of it is wrong:

- **Import route:** WP All Import is active, and the saved template that brought
  the 200 in still exists (`help_import_200.csv`, import id 3). I will clone
  that template for the 49 so the field mapping is provably the same one that
  worked, rather than rebuilt from scratch.
- **Field storage:** the FAQ articles are Rank Math-native, as you said. No ACF.
  The meta keys in use are `rank_math_title`, `rank_math_description`,
  `rank_math_focus_keyword`, `rank_math_robots`, `rank_math_advanced_robots`,
  `rank_math_primary_faq_category` and the social fields. That matches your
  column contract, including the fields you left blank by design.
- **Categories:** all nine `category_slug` values in the 49 already exist live,
  including the renamed `certificates-cpd-accreditation` → "Accreditation and
  Certification". Nothing will fail silently. I will match on slug, never name.
- **Audio wiring:** the theme finds audio by convention, not by a meta field. It
  looks for `wp-content/uploads/help-audio/{slug}.mp3` and an optional
  `{slug}.timings.json` alongside it. 200 of each are on the server now. So the
  49 need no CSV column and no theme change for audio — only the files, named
  by slug.
- **`has_audio = yes`** on all 49 therefore needs no import handling. Tell me if
  you intended it to drive something I have missed.

---

## C. What I need FROM YOU

1. **The corrected file**, with the two dead links from §A fixed:
   `Achology_FAQ_49_Help_Articles_IMPORT_43col.csv`, 49 rows, 43 columns, BOM on
   `id`. It is not in the folder yet — only the working `...COMPLETE.csv` is.
2. **Confirm the two dead links are handled** and how (repointed to a live
   article, or the related-question entry dropped), so I can verify it landed.
3. **Confirm `date_published` / `date_modified` handling.** Should the 49 import
   with the dates in the CSV, or with today's date? The 200 have their own
   dates and I do not want to guess at the freshness signal you intend.
4. **Confirm the URL column.** It carries the build domain
   `https://achologytest.com/...`. Confirm that column is reference-only and is
   not imported into any field, so nothing carries the test domain into
   production at cutover.
5. **Anything you expect me to check that is not in my list in §D.**

---

## D. What I will do next session, for you to correct now if it is wrong

Written out so you can object before I start rather than after:

1. Re-read this note and the file, and stop if the file still shows 51 rows or
   48 columns.
2. Clone the `help_import_200.csv` template, point it at the new file, and run
   the import.
3. Verify: 49 new `faq_article` rows, **249 total**; every row assigned to the
   right category by slug; the renamed-category rows land in "Accreditation and
   Certification".
4. Spot-check end to end, including at least one certificate-category row: the
   rendered page, the Rank Math title and description, the focus keyword, and
   that the internal links resolve to real pages.
5. Confirm all 249 are indexable and in the sitemap.
6. Report back: what landed, anything the importer rejected, and any column that
   needs different treatment.
7. **Audio is a separate step, after the import is verified.** I will not run
   both in one pass.

---

## E. Audio: what I need from you, and what is mine

The pipeline that produced the 200 is mine and I still have it. For the 49 I
need only:

- **Confirmation that `answer_text_full` is the text to voice**, not
  `answer_html_full` or `excerpt`. Your note said `answer_text_full`; confirming
  because a wrong choice here wastes the whole run.
- **Confirmation that nothing in the 49's text needs pronunciation handling
  beyond the existing rule.** The engine is fed "Ackology" so it says Achology
  correctly. If the 49 introduce new proper nouns, acronyms or names that a
  voice engine will mangle, list them and I will add them to the substitution
  set before the run rather than after hearing it.

Everything else on audio is settled by convention: output is `{slug}.mp3` plus
`{slug}.timings.json`, into `wp-content/uploads/help-audio/`, same voice as the
200. No decision needed from you.

---

## F. Status

Kain has stopped my build work pending the harness. **This is a request for
inputs, not work starting.** When he releases it, §D is what runs, and the only
thing that blocks it is §C.1 and §C.2.
