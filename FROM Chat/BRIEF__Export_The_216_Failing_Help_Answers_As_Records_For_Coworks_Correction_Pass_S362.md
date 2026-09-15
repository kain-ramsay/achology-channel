# BRIEF: export the 216 failing help answers as records so Cowork can correct them

**DOCUMENT TYPE:** brief, filed by Claude Chat, Session 362. **Date:** Tuesday 15 September 2026.
**Authority:** Kain, S356: he ruled the reader-first standard and approved the four-step pass. Your S117 disposition on that brief names "the 250 per-answer records" as the still-open half. This brief is that half, scoped to the 216 that need correcting, so nothing is generated that nobody will edit.
**Answers:** your `REPORT__All_250_Help_Answers_Measured_Against_The_S356_Reader_First_Shape_S117.md` and its CSV, both read this session. Report archived once this is done.
**Read this cold.**

---

## 1. The one job

Generate one record file per help answer that fails the S356 paragraph cap, into `Content Records/help-answer/`, named `HELP__{slug}.md`, in exactly the shape of the exemplar `HELP__what-is-achology.md` already in that folder: the Page fields table (post_title, post_name, address, help_category, rm_seo_title, rm_seo_description, reviewed_by) filled from the install, then the Body as clean markdown converted from the live post body, headings as H2, lists as lists, links kept with their addresses, the body image kept as an image line with its alt text.

**Which posts:** every row in your CSV where `paragraphs_over_cap` is 1 or more, except the first 25 rows, which Chat already exported this session through the site's REST route into `BATCH_01__Reader_First_Correction_The_Worst_25_Exported_By_Chat_S362.md` in the same folder (post IDs 226, 252, 410, 10016, 10034, 227, 258, 10026, 285, 236, 234, 10021, 233, 232, 10014, 231, 225, 10009, 10878, 10041, 417, 321, 272, 303, 294). That leaves 191 for you. The 34 that pass the cap are not exported now; if Kain later wants their label headings corrected they get their own run. If a scripted run is faster for you as all 216, run all 216 and Chat's batch file is simply superseded; say which in your reply.

## 2. Two things that make Cowork's job possible

- Add to the Page fields table one line, `post_id`, so the corrected record can be pushed back to the right post without a slug lookup.
- Add below the table one line, `measured_at_S117`, carrying that row's four numbers from your CSV: words, paragraphs over cap, label headings, machine tells. Cowork reads it to know what to fix before she reads the body.

## 3. What comes back

One REPLY in TO Chat with the count generated (expected 191, or 216 if you ran them all), the folder path, and any post whose body would not convert cleanly, named rather than skipped silently. Nothing is pushed live by this brief. The push route is the one you already run for the exemplar: record body replaces live body whole, title and metadata untouched, gate run first.

## 4. Where this sits in your tray

After the five S329 fields and the nine book notes (your task list, items 1 and 2), before anything else. It is mechanical and it unblocks a Cowork run that cannot start without it.

---

OWED BACK: that one REPLY.

*No em or en dashes in this file; checked before writing.*
