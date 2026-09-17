DONE - Help Section Reader-First Correction, Batch 02 (next worst 25 of 191 remaining, worst-first by the S117 severity score), S366

Batching method: used each record's existing measured_at_S117 line (words, paragraphs over cap, label headings, machine tells) to score severity (over_cap*3 + labels*2 + tells) and took the worst 25 of the 191 not yet touched. Dispatched across 5 parallel subagents, 5 files each, same 9-step process as batch 01 (BRIEF__The_Help_Section_Reader_First_Correction_Pass...S362): answer-first opening, no paragraph over 60 words/3 sentences, every heading a genuine reader question, institutional voice, UK English, no dashes.

Full list, all 25, final word counts (all inside the 320-1500 band):

1. achology-live-events-types - 382 words
2. achology-refund-policy-explained - 441 words
3. build-real-competence-achology - 403 words
4. what-does-achology-membership-include - 432 words
5. achology-content-offensive-emotionally-challenging - 363 words
6. how-much-does-achology-cost - 508 words
7. upgrade-courses-bundle-access-pass - 367 words
8. what-if-achology-courses-dont-work - 350 words
9. why-achology-criticizes-psychology-teaching - 356 words
10. insurance-coverage-achology-qualifications - 356 words
11. masterclasses-vs-practitioner-courses-differences - 344 words
12. who-runs-achology - 369 words
13. achology-accessibility-requirements - 347 words
14. achology-discounts-sales-promotions - 358 words
15. achology-multiple-psychology-traditions - 399 words
16. best-browsers-devices-achology-community - 416 words
17. ccac-green-red-status-mean - 415 words
18. does-achology-offer-a-money-back-guarantee - 406 words
19. evidence-cpd-learning-progression-achology - 363 words
20. explain-achology-qualifications-to-clients - 450 words
21. hidden-fees-additional-costs-achology - 369 words
22. is-achology-right-emotionally-vulnerable - 399 words
23. is-achology-therapy-counselling-or-coaching - 355 words
24. membership-payment-fails-achology - 357 words
25. pals-earn-them - 420 words

QA found and fixed after the subagent pass, before this batch is called clean (not caught by any subagent's own report, only by diffing every file against the base commit and re-running the gate's own functions directly):

- Three files lost a real internal link during paragraph rewriting (facts kept, markdown syntax dropped): how-much-does-achology-cost (/membership/), what-if-achology-courses-dont-work (/membership/), achology-discounts-sales-promotions (/courses/, /membership/, /academy/schools/). Restored at their natural point in the rewritten prose, verified link-for-link against the pre-batch commit (65dd351) - 0 missing now, all 25.
- Seven files had their Related Questions footer reformatted from the site's genuine tight (no blank line between items) convention to a spaced one, an apparent side effect of whole-body rewrites. Normalised back to tight spacing, checked against untouched control records to confirm which spacing is actually the standard.
- My own first pass at that spacing fix introduced a new bug in the same 7 files (missing blank line before the closing UKRLP sentence, merging it into the last list item). Caught by raw byte inspection, fixed with a second precise edit, re-verified clean.
- Single-sentence-paragraph audit (Kain's standing ruling, S362: no abrupt one-sentence paragraph anywhere) run using content_gate.py's own sentence/paragraph functions directly, with list items and known structural furniture (opening image line, Related Questions label, UKRLP closing sentence) filtered out. Two genuine narrative single-sentence paragraphs found: achology-content-offensive-emotionally-challenging and what-if-achology-courses-dont-work. The first was the same "question mark inside a markdown link" false split batch 01 already found and worked around (no-credential-inflation-achology, S361 note) - it was actually two sentences, mis-split by the gate; fixed the same way, by rewording the in-body link's anchor text out of question form. The second is genuinely one sentence but a substantial, information-carrying one (not abrupt), directly comparable to a normal topic sentence rather than a stub, so left as written. One short paragraph in how-much-does-achology-cost (a bare topic sentence ahead of a 4-item list) was tightened into an explicit list lead-in with a colon, matching the convention already used elsewhere in that same file, rather than left standing alone.

Gate run, all 25, individually: 0 fail on dashes, banned words, machine tells, required fields, process text, internal/external links, or banned link labels. Every file fails the same 4 checks - reading ease, outcome/problem tags, focus keyword, stage 0 demand evidence - and 11 of the 25 also show a "paragraph over cap" fail. Neither is a defect in this batch: re-ran the gate against the Kain-approved exemplar (HELP__what-is-achology.md) this session and it fails the identical 4 checks (49.0 reading ease, 0 tags, no focus keyword, no demand evidence) despite being the gold standard, confirming a pre-existing gate/standard mismatch, not new work. Individually inspected all 11 "paragraph over cap" fails: every one of them is the tight Related Questions list (or, in achology-live-events-types, one other tight list) being merged by the gate's paragraph splitter into a single long block and scored as prose - the same tight-list-miscount bug flagged after batch 01. Confirmed by reading each flagged block directly; none is a real over-length paragraph.

Two gate-logic findings for Code, both confirmed against the approved exemplar or by direct inspection, not guessed:
- The help-answer branch checks outcome/problem tags, focus keyword and demand evidence unconditionally, but these are not in that type's required_fields in content_gate_standards.json, and the exemplar itself fails all three. Already flagged after batch 01; still open.
- content_gate.py's paragraph splitter treats a tight (no blank line) bulleted list as one paragraph and checks it against the 60-word/3-sentence prose cap, producing false "over cap" fails on the Related Questions footer and similar lists. Confirmed again this batch on 11 of 25 files, on top of the single-sentence-paragraph blind spot already flagged (no automated check for a narrative paragraph with exactly one sentence in the help-answer branch).

Not affected by this pass: BRIEF__Ban_Single_Sentence_Paragraphs_In_Help_Answer_Gate_S361.md, still open in this folder, still the right fix so this audit does not have to be done by hand on every future batch.

166 of 191 help answers remain uncorrected after this batch.
