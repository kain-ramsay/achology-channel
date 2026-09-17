DONE - Help Section Reader-First Correction, Batch 03 (next worst 25 of 166 remaining, worst-first by the S117 severity score), S366

Same method as batch 02: severity = over_cap*3 + labels*2 + tells from each record's measured_at_S117 line, worst 25 of the 166 not yet touched, dispatched across 5 parallel subagents, 5 files each, same 9-step process (BRIEF__The_Help_Section_Reader_First_Correction_Pass...S362).

Full list, all 25, final word counts (all inside the 320-1500 band):

1. personal-progress-checklist-count-official-cpd - 417 words
2. society-lost-gatekeeping-psychology - 350 words
3. why-achology-avoids-diagnostic-labels - 359 words
4. why-achology-includes-community-course-prices - 406 words
5. achology-change-mind-after-14-day-guarantee - 375 words
6. achology-course-prerequisites-requirements - 388 words
7. achology-members-host-workshops-events - 353 words
8. achology-recommended-practice-pathway - 368 words
9. achology-refund-disagree-course-content - 371 words
10. achology-s-registered-company-details - 379 words
11. any-achology-courses-appear-more-than - 495 words
12. call-myself-therapist-achology-courses - 346 words
13. can-achology-help-personal-struggles - 350 words
14. cancel-achology-membership-anytime - 353 words
15. cant-log-in-achology-community - 398 words
16. difference-between-certificate-completion-certificate-achievement - 386 words
17. difference-between-code-ethics-ccac-community - 444 words
18. how-to-contact-achology-support - 336 words
19. manipulative-pricing-tactics-achology-avoids - 361 words
20. navigate-achology-community-guide - 379 words
21. submit-cpd-credit-claim-hosting-attending - 417 words
22. where-should-i-start-with-achology - 355 words
23. who-is-kain-ramsay - 493 words
24. achology-access-all-areas-pass - 367 words
25. achology-automated-decision-making-profiling - 440 words

QA found and fixed after the subagent pass, none caught by the subagents' own self-reports, all found by diffing every file against the base commit (65dd351) and re-running the gate's own functions directly:

- The single biggest issue this batch: 14 of 25 files had the site-wide closing citation sentence ("Achology is listed on the UK Register of Learning Providers...") rewritten by their subagent, in three different variant wordings, instead of left as the fixed boilerplate it is (the S358 exception already covers this line; batch 01 and 02 both left it untouched). A 15th file merged it into the preceding sentence instead of keeping it as its own closing paragraph. All 15 reverted to the exact original wording and, where needed, restructured so the sentence before it isn't left as a new orphan. This is the first time this specific regression has happened at this scale (15 of 25 files) and is worth a line in the subagent brief for future batches: the UKRLP closer is off-limits, not just the Page fields table.
- One file (can-achology-help-personal-struggles) dropped its one internal link to /courses/ during a sentence rewrite. Restored, worded into the opening question naturally.
- One file (difference-between-certificate-completion-certificate-achievement) had its own new genuine paragraph-cap violation, introduced by my own UKRLP-boilerplate fix (repositioning a sentence created a 69-word, 3-sentence paragraph). Caught on the follow-up gate run and fixed by moving a sentence to the preceding paragraph instead of trimming content.
- After all of the above, corrected all 25 files' corrected_S366 word-count line to the true final count (the UKRLP revert changed body length in the 15 affected files).

Single-sentence-paragraph audit (Kain's standing ruling): 0 genuine narrative single-sentence paragraphs across all 25, checked with the same filtered method as batch 02 (list items, the image line, the Related Questions label, and the UKRLP closer excluded).

Gate run, all 25, individually: every file fails only the same 4 pre-existing checks the approved exemplar itself fails (reading ease, outcome/problem tags, focus keyword, demand evidence - confirmed not a defect, per batch 02's note). 15 of 25 also show a paragraph-over-cap fail; every one individually inspected and confirmed to be the known tight-list-miscount bug (a Related Questions block or similar list merged into one long "paragraph" by the gate's splitter) - 14 are the ordinary 60-word cap, and one (any-achology-courses-appear-more-than) is large enough to also trip the separate absolute 120-word cap: a genuine 9-item tight list (course names with school tags), 149 words, correctly formatted, not prose. No new gate-bug category found this batch, same two already flagged to Code (help-answer's unconditional tag/keyword/demand checks; the tight-list-as-paragraph miscount).

Two facts flagged, not touched, left exactly as found (per the brief: do not fix a fact, name it and leave it standing):
- HELP__achology-access-all-areas-pass.md's rm_seo_description (Page fields, locked) reads "...Pass is ,995 for all 28 courses..." - looks like "$2" is missing before "995", should likely read "$2,995". Pre-existing, not introduced by this pass.
- HELP__achology-recommended-practice-pathway.md names the same pathway status two ways: a bulleted list calls it "Senior Achologist (II)" while a later paragraph calls it "Senior Achologist (Level One)". Worth a source check against whichever page owns the practice-pathway status names.

141 of 191 help answers remain uncorrected after this batch (166 minus this batch's 25).
