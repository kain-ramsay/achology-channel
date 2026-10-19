> DISPOSITION, Chat S370: STAYS. Waits on Code: push these 25 corrected records to the live posts, gate first, and write their DSRD 6 records. One fact closes it, Code's confirmation that the 25 are live.

DONE - Help Section Reader-First Correction, Batch 05 (next worst 25 of 116 remaining, worst-first by the S117 severity score), S366

Same method and process as batches 02-04, with the "never touch the UKRLP closer" and "check every paragraph, not just the ones S117 flagged" warnings both carried into this batch's brief. UKRLP closer confirmed byte-for-byte unchanged, programmatically, in all 25 - zero regressions this batch.

Full list, all 25, final word counts (all inside the 320-1500 band):

1. transfer-kain-ramsay-udemy-courses-achology - 421 words
2. what-does-achology-certification-qualify - 368 words
3. what-is-applied-psychology-achology - 356 words
4. what-makes-achology-different - 364 words
5. achology-copyright-sharing-course-content - 370 words
6. achology-customer-legal-rights-uk-consumer-law - 339 words
7. achology-s-character-code-based-aristotle - 469 words
8. achology-school-bundles-how-they-work - 366 words
9. achology-vs-mindvalley-comparison - 354 words
10. commit-practising-achologist - 458 words
11. course-included-free-membership-happens-when - 412 words
12. download-achology-course-materials - 371 words
13. how-long-achology-refund-process - 360 words
14. how-psychology-became-institutionalised - 366 words
15. inside-achology-course-modules-breakdown - 379 words
16. many-courses-achology-offer-total - 350 words
17. seven-marks-maturity-achology-teaches - 466 words
18. share-achology-account-courses - 385 words
19. slow-deep-learning-rejects-fast-certification - 371 words
20. supervision-after-achology-training - 384 words
21. what-personal-data-achology-collects - 432 words
22. what-to-include-achology-support-request - 420 words
23. where-is-achology-based - 391 words
24. which-achology-company-am-actually-contracting - 408 words
25. who-is-achology-designed-for - 383 words

The gap flagged after batch 04 was confirmed at scale this batch: every one of the 5 subagent groups reported that the S117 measurement line consistently undercounted both label headings (it typically caught 1-2 of the 3-4 actually present) and single-sentence orphan paragraphs (S117 does not measure sentence count at all, only paragraph length and count). Every group checked the whole body rather than just the flagged spots and found and fixed the extra ones. This is now a confirmed pattern across four consecutive batches, not a one-off - worth the build brief to Code: extend the S117-style measurement to count sentences per paragraph and count headings properly, so future severity scoring and batch sizing is accurate rather than a rough sort.

QA found and fixed after the subagent pass, none caught by the subagents' own self-reports, found by diffing every file against the base commit and re-running the gate's own functions directly:

- Three genuine narrative single-sentence orphan paragraphs the subagents missed or misjudged, all now fixed:
  - what-makes-achology-different: three bold-lead paragraphs ("**Live learning.**", "**Character alongside technique.**", "**Earned certification.**"), each one sentence, separated by blank lines rather than formatted as a list. The subagent's own report claimed these were "genuinely two sentences" - they were not, confirmed by direct count. Converted all three into a proper bulleted list (they are a parallel enumerated set, which is what the standard calls for anyway), which resolves the orphan issue structurally rather than by padding.
  - achology-customer-legal-rights-uk-consumer-law: the same pattern, three bold-lead single-sentence paragraphs stating the three UK consumer-law standards (as described / fit for purpose / of satisfactory quality). Same fix, converted to a bulleted list.
  - seven-marks-maturity-achology-teaches: a one-sentence list lead-in ending in a period instead of a colon, immediately followed by the seven-item list it introduces. Changed the closing period to a colon, matching the fix already applied to this exact pattern in an earlier batch.
- All 25 files' corrected_S366 word-count line synced to the true final count.

Gate run, all 25, individually: every file fails only the same 4 pre-existing checks the approved exemplar itself fails. 15 of 25 also show a paragraph-over-cap fail; all 15 individually inspected and confirmed to be the known tight-list-miscount bug (a Related Questions block, a course-list, or a data-category list merged into one long "paragraph" by the gate's splitter). No new gate-bug category found. No link regressions, no em/en dashes, no facts changed.

Three things flagged, not touched (per the brief: name a fact that looks wrong, do not fix it):
- HELP__download-achology-course-materials.md and HELP__inside-achology-course-modules-breakdown.md: both have lowercase "achology" in their rm_seo_description (Page fields, locked).
- HELP__which-achology-company-am-actually-contracting.md: rm_seo_description reads "...depends what you bought" - missing "on" before "what you bought".
- HELP__seven-marks-maturity-achology-teaches.md: the post_title/H1 says "seven signs of maturity" but the body, slug, and SEO title all say "seven marks" - a naming inconsistency that predates this pass. Body language left as "marks" to match the majority; the "signs" vs "marks" reconciliation is a naming decision, not something to guess at.

91 of 191 help answers remain uncorrected after this batch (116 minus this batch's 25).
