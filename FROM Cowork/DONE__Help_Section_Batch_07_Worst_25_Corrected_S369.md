DONE, from Cowork to Claude Chat, Session 369. Continues `BRIEF__The_Help_Section_Reader_First_Correction_Pass_216_Answers_Worst_First_25_Per_Batch_S362.md` (still in TO Cowork, runs across sittings). Batch 7 of the 216-answer worst-first pass.

# Help Section Batch 7: 25 Worst-First Answers Corrected

Same method as batch 6: read all 25 source files fresh, dispatched five parallel drafting passes carrying the full DSRD 2 section 2.24 standard, the S362 human-first ruling verbatim, and the S361 single-sentence-paragraph ban verbatim (with the S358 fixed-structure exception). This batch also carried the colon-terminated-list-header exemption as a **settled convention** rather than an open question, since Kain confirmed it at the close of batch 6 ("Yes, i'm totally happy with that!"). Rebuilt all 25 files centrally from the returned drafts, ran the automated check, reviewed every flag by eye, and pushed all 25 to the live records.

## Method

All remaining in-scope rows now sit at `paragraphs_over_cap: 1` (the worse rows, 2 and 3 over cap, were cleared in batches 1-6), so this batch was ordered by longest single paragraph as the tiebreak. Computed from `MEASURED__All_250_Help_Answers_S117.csv`, 216 in-scope rows minus the 150 slugs already corrected through batch 6, leaving 91; took the next 25.

Six flags came back from the automated check, all confirmed false positives on inspection: five were colon-terminated list-header lines immediately followed by their bulleted list (exactly the settled exemption), and one was "plainly" sitting inside the `rm_seo_description` field of the untouchable Page fields table on `what-does-achology-expect-from-learners`, not in the body text at all.

## The 25 corrected, worst-first, with final word counts

1. `seven-schools-achology-curriculum-explained` — 425 words
2. `how-much-do-achology-coaches-earn` — 436 words
3. `achology-peer-learning-community-teaches` — 395 words
4. `achology-on-udemy-should-i-join-achology` — 405 words
5. `revisit-achology-courses-after-completion` — 381 words
6. `pay-instalments-achology-courses` — 409 words
7. `what-does-achology-expect-from-learners` — 402 words
8. `join-professional-body-after-achology` — 372 words
9. `achology-s-three-learning-paths` — 379 words
10. `verify-achology-certificate` — 398 words
11. `achology-vs-school-of-life-comparison` — 394 words
12. `first-course-complete-beginner` — 400 words
13. `can-achology-replace-university-degrees` — 415 words
14. `who-does-achology-share-personal-data-with` — 417 words
15. `choose-right-achology-event-level` — 388 words
16. `what-does-achology-mean-becoming-wiser` — 394 words
17. `is-achology-educational-provider-or-professional-body` — 409 words
18. `achology-mentorship-vs-coaching-difference` — 464 words
19. `achology-vs-tony-robbins-comparison` — 393 words
20. `platform-changes-course-access-achology` — 429 words
21. `achology-evidence-based-humanistic-psychology` — 416 words
22. `achology-professional-indemnity-insurance` — 424 words
23. `call-myself-certified-achology-credentials` — 397 words
24. `how-long-achology-keeps-personal-data` — 440 words
25. `achology-s-nine-value-based-principles` — 519 words

All 25 sit between the 320-word floor and the 625-word target, all now measure 0 paragraphs over cap, 0 label headings and 0 remaining machine tells, each carrying a new `corrected_S369` line under its original `measured_at_S117` line. Page fields tables, UKRLP closer sentences and every fact, figure and link target were left byte-for-byte untouched, verified programmatically.

## What the correction actually found

The same three patterns as batch 6, recurring at similar volume:

**Short one-sentence "hook" paragraphs standing alone right after a heading.** The single most common violation again. Fixed by merging into the neighbouring paragraph or giving the line a genuine second sentence.

**Dense multi-part sentences that should have been lists.** `how-much-do-achology-coaches-earn` (four things that move earnings), `achology-on-udemy-should-i-join-achology` (four things joining adds), `who-does-achology-share-personal-data-with` (the opening's illustrative examples trimmed since the full 8-item list already follows immediately below), `how-long-achology-keeps-personal-data` (four things the five-year window allows), `choose-right-achology-event-level` (two three-item event lists) and `seven-schools-achology-curriculum-explained` (the six "choose by X" options) were each converted, using the colon-header-plus-list pattern throughout.

**Bare noun-phrase label headings.** Nearly every file in this batch had at least one heading rewritten into genuine reader-question form; several subagents also caught and fixed headings the S117 baseline had scored as already passing (0 label headings) but which read as labels on a fresh reader-first check. Flagging this pattern for awareness: the S117 label-heading count is proving as unreliable as the paragraph count was, so it should not be trusted without a fresh manual check, same as previously noted for paragraph caps.

Four files (`pay-instalments-achology-courses`, `is-achology-educational-provider-or-professional-body`, `achology-vs-tony-robbins-comparison`, and the `what-does-achology-mean-becoming-wiser`/`achology-mentorship-vs-coaching-difference` pair) had their flagged "plainly" instance removed or rewritten, all in body text, all replaced with a natural rewrite rather than a bare swap to "simply" where "simply" would have read awkwardly.

## Facts flagged, not fixed, per the brief's instruction

- `seven-schools-achology-curriculum-explained.md`'s closing sentence links to `[What are the seven schools of Achology?]` pointing at the exact URL of the page the reader is already on, a self-referencing link that looks like a leftover from an earlier draft. Left untouched.
- Two files had a lowercase "achology" corrected to "Achology" at the start of a sentence (`achology-peer-learning-community-teaches`, `achology-mentorship-vs-coaching-difference`, `revisit-achology-courses-after-completion`) — treated as ordinary proofing rather than a fact change, since the correctly-capitalised form is used everywhere else on each page, but flagging the pattern in case it points to something systemic in how these records were first generated.

No prices, dates, figures, counts, or CPD requirement numbers were changed anywhere in this batch. Every external link and every internal link target is unchanged from the source records, aside from one anchor-text-only split (not a target change) in `choose-right-achology-event-level.md`, where "The Coaching HOT Seat as an observer" was split into linked anchor text "The Coaching HOT Seat" plus trailing "as an observer" to form a clean list item — the link's destination is unchanged.

## Definition of done

All 25 corrected files written to their live locations in `Content Records/help-answer/`, each carrying its `corrected_S369` measurement line. This report filed to FROM Cowork. 41 of 91 help answers remain after this batch. Kain asked mid-session to push through all remaining batches in this run rather than stopping after each one, so continuing straight into batch 8 without a further check-in.
