> DISPOSITION, Chat S370: STAYS. Waits on Code: push these 25 corrected records to the live posts, gate first, and write their DSRD 6 records. One fact closes it, Code's confirmation that the 25 are live.

DONE, from Cowork to Claude Chat, Session 369. Continues `BRIEF__The_Help_Section_Reader_First_Correction_Pass_216_Answers_Worst_First_25_Per_Batch_S362.md` (still in TO Cowork, runs across sittings). Batch 8 of the 216-answer worst-first pass.

# Help Section Batch 8: 25 Worst-First Answers Corrected

Same method as batches 6 and 7: read all 25 source files fresh, dispatched five parallel drafting passes carrying the full DSRD 2 section 2.24 standard, the S362 human-first ruling verbatim, and the S361 single-sentence-paragraph ban verbatim (with the S358 fixed-structure exception and the settled colon-terminated-list-header exemption). Rebuilt all 25 files centrally from the returned drafts, ran the automated check, reviewed every flag by eye, and pushed all 25 to the live records.

## Method

Computed from `MEASURED__All_250_Help_Answers_S117.csv`: 216 in-scope rows minus the 175 slugs already corrected through batch 7, leaving 41; took the next 25, worst-first, ordered by longest single paragraph as the tiebreak (the same basis used since batch 7, since all remaining rows sit at `paragraphs_over_cap: 1`).

Twelve flags came back from the automated check, all confirmed false positives on inspection: every one was a colon-terminated list-header line separated from its bulleted list by a blank line in the markdown source, which is normal formatting and matches the settled exemption exactly. One drafting slip was also caught and fixed before commit: a subagent-supplied link in `which-courses-included-each-school-bundle.md` was mistyped during file assembly and was corrected back to the source's original target before the file was written to disk.

## The 25 corrected, worst-first, with final word counts

1. `refund-course-complimentary-membership-cancel-too` — 383 words
2. `which-courses-included-each-school-bundle` — 433 words
3. `kain-ramsay-udemy-vs-achology-courses` — 375 words
4. `set-up-achology-community-profile` — 378 words
5. `principle-led-education-achology` — 382 words
6. `achology-coaching-competency-review-sessions` — 439 words
7. `create-posts-achology-community` — 453 words
8. `personal-responsibility-achology-learning` — 428 words
9. `achology-updates-course-already-purchased` — 430 words
10. `who-is-achology-not-for` — 414 words
11. `achology-membership-free-coaching-included` — 426 words
12. `achology-certification-practice-competence` — 403 words
13. `does-achology-offer-partnerships-collaborations` — 397 words
14. `fix-achology-community-notification-problems` — 393 words
15. `why-achology-emphasises-personal-responsibility` — 415 words
16. `achology-vs-coursera-psychology-education` — 348 words
17. `coaching-vs-counselling-credentials-difference` — 412 words
18. `achology-vs-therapy-training-counselling` — 391 words
19. `guest-speakers-policy` — 400 words
20. `direct-message-achology-members` — 402 words
21. `do-achology-courses-get-updated` — 385 words
22. `earn-cpd-credit-hosting-session-only` — 421 words
23. `which-achology-events-earn-accreditation-credit` — 415 words
24. `homework-assessment-achology-courses` — 366 words
25. `achology-success-stories-do-courses-work` — 440 words

All 25 sit between the 320-word floor and the 625-word target, all now measure 0 paragraphs over cap, 0 label headings and 0 remaining machine tells, each carrying a new `corrected_S369` line under its original `measured_at_S117` line. Page fields tables, UKRLP closer sentences and every fact, figure and link target were left byte-for-byte untouched, verified programmatically.

## What the correction actually found

The same three recurring patterns as prior batches, at similar volume:

**Short one-sentence "hook" or fragment paragraphs standing alone right after a heading.** Still the single most common violation. Fixed by merging into the neighbouring paragraph, expanding with genuine content, or folding into a list. `achology-updates-course-already-purchased.md` had two sentence fragments masquerading as prose ("Compliance with changes in law or regulation, and technical adjustments...") which were converted into proper bulleted lists rather than patched as sentences.

**Dense multi-part sentences that should have been lists.** `who-is-achology-not-for` (the mismatch-of-expectation and mismatch-of-need groupings), `create-posts-achology-community` (the four things worth posting), `does-achology-offer-partnerships-collaborations` (the four elements of a strong proposal), and `achology-success-stories-do-courses-work` (the evidence figures) were each converted to the colon-header-plus-list pattern.

**Bare noun-phrase or broken restated-title headings.** Several files carried a heading that was really a fragment of the page title glued onto extra words (`achology-coaching-competency-review-sessions`'s "...At Achology: Credit And Attending", `who-is-achology-not-for`'s "...Mismatches Of Expectation", `achology-membership-free-coaching-included`'s "...What It Is For, And What It Is Not", `guest-speakers-policy`'s "...The Reasoning"). All rewritten into genuine reader-question form. Several more headings that the S117 baseline scored as passing (0 label headings) were caught on fresh read as bare labels regardless (`principle-led-education-achology`, `which-achology-events-earn-accreditation-credit`, `earn-cpd-credit-hosting-session-only`, `achology-success-stories-do-courses-work`), continuing the pattern flagged in batches 6 and 7 that the S117 label-heading count should not be trusted without a fresh manual check.

Two files (`kain-ramsay-udemy-vs-achology-courses`, `who-is-achology-not-for`) had "plainly" removed; `achology-vs-therapy-training-counselling` and `why-achology-emphasises-personal-responsibility` likewise, all four rewritten naturally rather than swapped bare for "simply".

## Facts flagged, not fixed, per the brief's instruction

- `direct-message-achology-members.md` names "the Community Code of Conduct" in body text without a hyperlink, while a differently-named "Code of Ethics" is linked elsewhere on the site. This may be an inconsistency or a missing link. Left exactly as-is; flagging for review.

No prices, dates, figures, counts, or CPD requirement numbers were changed anywhere in this batch. Every external link and internal link target is unchanged from the source records, aside from formatting-only changes (turning dense sentences into lists without altering any link's destination).

## Definition of done

All 25 corrected files written to their live locations in `Content Records/help-answer/`, each carrying its `corrected_S369` measurement line, committed with zero rejections. This report filed to FROM Cowork. 16 of 216 help answers remain after this batch. Per Kain's mid-session instruction to push through all remaining batches in this run rather than stopping after each one, continuing straight into batch 9, the final batch, without a further check-in.
