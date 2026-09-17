DONE, from Cowork to Claude Chat, Session 369. Completes `BRIEF__The_Help_Section_Reader_First_Correction_Pass_216_Answers_Worst_First_25_Per_Batch_S362.md` (now fully closed). Batch 9 of 9, the final batch, of the 216-answer worst-first pass.

# Help Section Batch 9: Final 16 Worst-First Answers Corrected

Same method as batches 6 through 8: read all 16 source files fresh, dispatched four parallel drafting passes carrying the full DSRD 2 section 2.24 standard, the S362 human-first ruling verbatim, and the S361 single-sentence-paragraph ban verbatim (with the S358 fixed-structure exception and the settled colon-terminated-list-header exemption). Rebuilt all 16 files centrally from the returned drafts, ran the automated check, reviewed every flag by eye, and pushed all 16 to the live records.

## Method

Computed from `MEASURED__All_250_Help_Answers_S117.csv`: 216 in-scope rows minus the 200 slugs already corrected through batch 8, leaving the final 16. Ordered worst-first by longest single paragraph, the same basis used since batch 7.

Seven flags came back from the automated check, all confirmed false positives on inspection: every one was a colon-terminated list-header line separated from its bulleted list by a blank line in the markdown source, matching the settled exemption exactly. No fixes needed.

## The 16 corrected, worst-first, with final word counts

1. `achology-vs-icf-coaching-certification` — 389 words
2. `does-achology-sell-personal-data` — 359 words
3. `is-achology-accredited-somap` — 366 words
4. `delete-achology-account-and-data` — 356 words
5. `is-achology-suitable-for-beginners` — 410 words
6. `achology-course-order-sequence` — 434 words
7. `achologist-led-tutorials-alts` — 432 words
8. `psychology-as-practical-wisdom` — 390 words
9. `what-law-governs-achology-terms` — 371 words
10. `cant-see-achology-course-space-community` — 386 words
11. `cpd-journey-after-leaving-achology` — 437 words
12. `membership-first-or-course-first` — 402 words
13. `download-achology-community-app` — 384 words
14. `achology-courses-other-languages` — 359 words
15. `achologist-title-without-membership` — 375 words
16. `achology-character-development` — 452 words

All 16 sit between the 320-word floor and the 625-word target, all now measure 0 paragraphs over cap, 0 label headings and 0 remaining machine tells, each carrying a new `corrected_S369` line under its original `measured_at_S117` line. Page fields tables, UKRLP closer sentences and every fact, figure and link target were left byte-for-byte untouched, verified programmatically.

## What the correction actually found

The same recurring patterns as prior batches:

**Sentence-fragment paragraphs standing alone right after a heading**, still the most common violation: "Because a bare promise not to sell your data..." (`does-achology-sell-personal-data`), "Stated plainly, rather than letting the word do more work..." (`is-achology-accredited-somap`, also removed "plainly"), "Because preparing to teach something exposes..." (`achologist-led-tutorials-alts`), "Because the alternative has a cost that is easy to miss." (`psychology-as-practical-wisdom`), "This is the part worth being clear about..." (`what-law-governs-achology-terms`), "Because of the one thing you cannot catch up on later." (`download-achology-community-app`), "Because of what a client hears." (`achologist-title-without-membership`), and three in a row at the open of `achology-character-development`. All fixed by merging into the neighbouring paragraph or rewriting the fragment as a complete sentence, never by patching a single word.

**Dense multi-part sentences converted to lists**: the four ICF credential requirements, the three accreditation-weighing questions, the three items to include in a deletion request, the three things to give support, the five preserved CPD activities, and the four daily-life examples in `psychology-as-practical-wisdom` were each converted to proper bulleted lists.

**A garbled heading**: `achology-courses-other-languages` carried a broken restated-title fragment as its second heading ("Achology Courses Available In Other Languages? What English-Only Covers"), rebuilt into a clean reader question ("What does English-only actually cover?").

**"Plainly" removed** from three files: `is-achology-accredited-somap`, `delete-achology-account-and-data`, and confirmed as already absent from body text in `achology-vs-icf-coaching-certification` despite the S117 flag (the actual instance was in a since-rewritten closing sentence).

All bare-label and restated-title headings across the 16 files were converted to genuine reader questions, continuing the pattern flagged since batch 6 that the S117 label-heading count under-reports real violations on fresh read.

## Facts flagged, not fixed, per the brief's instruction

- `psychology-as-practical-wisdom.md`: both "Related questions" links point to the same URL despite different anchor text ("applied psychology" vs "becoming wiser"). The first almost certainly should point to `/help/achology-basics-and-identity/what-is-applied-psychology-achology/`, the correct target already used in the file's own body text. Left exactly as-is; flagging for review.
- `achology-course-order-sequence.md` and `achology-courses-other-languages.md`: both carry an `rm_seo_title` field missing a space before/after the pipe character (e.g. "...Order?|Achology Help"). Metadata-level formatting issue, left untouched since the Page fields table is off-limits; flagging for a separate fix pass.

No prices, dates, figures, counts, company registration numbers (SC697126, SC612822 preserved exactly in `what-law-governs-achology-terms`), or CPD requirement numbers were changed anywhere in this batch. The `delete-achology-account-and-data.md` file's second external link, to the Information Commissioner's Office (ico.org.uk), was preserved exactly in position. Every other external and internal link target is unchanged from source.

## Definition of done

All 16 corrected files written to their live locations in `Content Records/help-answer/`, each carrying its `corrected_S369` measurement line, committed with zero rejections. This report filed to FROM Cowork.

**0 of 216 help answers remain uncorrected.** This closes the 216-answer worst-first pass in full: batches 1 through 9 together correct all 216 in-scope help section records to the DSRD 2 section 2.24 reader-first standard, the S362 human-first ruling, and the S361 single-sentence-paragraph ban. The three flagged-not-fixed items above (one likely broken Related-questions link, two metadata pipe-spacing issues) are the only open threads, and none blocks the pass being complete.
