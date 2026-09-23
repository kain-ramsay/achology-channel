> DISPOSITION, Chat S370: STAYS. Waits on Code: push these 25 corrected records to the live posts, gate first, and write their DSRD 6 records. One fact closes it, Code's confirmation that the 25 are live.

DONE - Help Section Reader-First Correction, Batch 04 (next worst 25 of 141 remaining, worst-first by the S117 severity score), S366

Same method and process as batches 02-03. This batch's subagent brief was updated with an explicit, named warning about the UKRLP-closer regression found in batch 03 (the exact fixed sentence quoted in full, marked non-negotiable) - all 5 groups confirmed programmatically, not just by eye, that the closer was byte-for-byte unchanged in all 25 files. It held: 0 files touched the closer this batch.

Full list, all 25, final word counts (all inside the 320-1500 band):

1. achology-career-change-coaching-mentoring - 374 words
2. achology-course-piracy-copyright - 378 words
3. achology-courses-cpd-hours - 375 words
4. achology-discussion-spaces-groups-events - 396 words
5. achology-knowledge-hub-free-read - 439 words
6. achology-membership-refund - 350 words
7. achology-password-reset-email-not-arriving - 390 words
8. achology-refund-technical-issues - 375 words
9. achology-responsible-community-member-advice - 406 words
10. achology-vs-udemy-psychology-courses - 363 words
11. achology-vs-university-psychology - 461 words
12. ask-questions-achology-community - 425 words
13. coaching-hot-seat - 407 words
14. completed-achology-course-nothing-changed - 393 words
15. find-achology-course-resources - 380 words
16. get-value-achology-mentorship-sessions - 412 words
17. have-retake-code-ethics-training-every - 428 words
18. how-achology-courses-work-self-paced - 396 words
19. how-to-join-live-achology-community-event - 381 words
20. how-to-participate-achology-discussions-events - 385 words
21. many-ccac-sessions-need-complete-often - 465 words
22. realistic-outcomes-with-achology - 357 words
23. rsvp-join-achology-live-events - 373 words
24. see-real-results-how-long-achology-takes - 358 words
25. study-multiple-achology-courses-simultaneously - 371 words

Worth noting on the correction itself: every one of the 5 subagent groups independently reported finding pre-existing single-sentence orphan paragraphs that the S117 measurement had not caught, because S117 only measures paragraph length and count, not sentence count per paragraph - roughly 25-30 extra orphans fixed across the batch beyond what the "paragraphs over cap" number predicted. This confirms the same gap flagged after batch 01: the S117 CSV undercounts how much correction a file actually needs, which is why severity-scoring off it is a rough sort, not an exact one. Worth a build brief for Code if the source measurement is ever re-run: add a sentence-count-per-paragraph check alongside the existing length check.

QA found and fixed after the subagent pass, none caught by the subagents' own self-reports, all found by diffing every file against the base commit and re-running the gate's own functions directly:

- All 25 files' corrected_S366 word-count line updated to the true final count (minor drift from post-subagent tidy-ups).
- Two lowercase "achology" typos at the start of a sentence (how-achology-courses-work-self-paced, how-to-participate-achology-discussions-events) - both flagged by their subagent as possibly deliberate SEO casing rather than fixed, but there is no such casing convention anywhere else on the site and it reads as a plain capitalisation slip. Capitalised both.
- One genuine over-cap paragraph found on the follow-up gate run (get-value-achology-mentorship-sessions, 53 words but 4 "sentences" by the gate's count) - on inspection this is a well-formed 3-sentence paragraph built around two quoted example questions; the gate's sentence splitter is over-counting because one quoted example ends in a question mark mid-paragraph, the same class of false split already flagged after batch 02 for a markdown link's anchor text, now confirmed to also happen with quoted dialogue. Left as written - it is not abrupt, not a defect, and matches Kain's ruling's actual intent (no bare orphan sentence), not the gate's literal count.

Single-sentence-paragraph audit (Kain's standing ruling): 0 genuine narrative single-sentence paragraphs remain across all 25 (the one borderline case above is a substantial 3-sentence paragraph mis-split by the gate, not a real orphan).

Gate run, all 25, individually: every file fails only the same 4 pre-existing checks the approved exemplar itself fails. 10 of 25 also show a paragraph-over-cap fail; 9 of the 10 individually inspected and confirmed to be the known tight-list-miscount bug (Related Questions or similar lists). The 10th (get-value-achology-mentorship-sessions) is the quoted-dialogue false split above, not a list. No new gate-bug category found.

One cosmetic Page-fields issue flagged, not touched (locked field, not in scope): HELP__ask-questions-achology-community.md's rm_seo_title reads "How to Ask a Question in Achology|Achology Help" with no spaces around the pipe - looks like a template artefact, worth a source check whenever that field is next touched.

No facts, prices, or claims were changed in this batch. No link regressions, no em/en dashes.

116 of 191 help answers remain uncorrected after this batch (141 minus this batch's 25).
