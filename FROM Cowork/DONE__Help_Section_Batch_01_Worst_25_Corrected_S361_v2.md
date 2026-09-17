> DISPOSITION, Chat S370: STAYS. Waits on Code: push these 25 corrected records to the live posts, gate first, and write their DSRD 6 records. One fact closes it, Code's confirmation that the 25 are live.

DONE (v2, supersedes DONE__Help_Section_Batch_01_Worst_25_Corrected_S361.md, same session) - Help Section Reader-First Correction, Batch 01 (worst 25 of 216), single-sentence-paragraph remediation, S361

The v1 note recorded the mechanical split pass: label headings turned into questions, paragraphs cut down to the 60-word/3-sentence cap. That pass met the letter of the cap by cutting long paragraphs into pieces, and a large number of those pieces landed as a single sentence standing alone as its own paragraph, throughout all 25 records.

Kain read the batch and ruled it unacceptable: "Placing one abrupt sentence as a paragraph is not acceptable anywhere on the site Claude. Period. Write to human beings, and never to appease a machine." Scope confirmed with Kain directly to article main body copy only; fixed-form structural lines (credit lines, the quote-page provenance formula, "Put this into practice" blocks) are not in scope and are unaffected, per the standing S358 exception.

This note records the fix: every single-sentence paragraph across all 25 live records has been merged into a flowing two- or three-sentence paragraph, or, where the content was itself an enumerated set (three convictions, three commitments, three responses), converted into a bulleted list, since list items are not paragraphs. No fact, link, figure or heading was changed; connective wording was added only at merge points, and four records (course-completion-vs-competence, no-credential-inflation-achology, post-nominal-letters-achology-certificates, and the word-count floor cases already noted in v1) kept their earlier floor-clearing sentences.

Verified against content_gate.py's own sentences()/words() logic directly (not a re-implementation): 0 paragraphs over the 60-word/3-sentence cap and 0 single-sentence paragraphs, across all 25 files, confirmed in a full bulk pass run after the last edit.

Final word counts, all 25:

1. achology-free-trial-introductory-offer - 427 words
2. achology-code-character-conduct-ccac - 377 words
3. six-achology-cpd-statuses - 500 words
4. using-achology-content-branding-materials - 375 words
5. what-achology-certificate-proves - 373 words
6. does-achology-provide-crisis-support - 321 words
7. achology-discussion-boundary-feels-unsafe - 326 words
8. cips-when-need-them - 337 words
9. achology-code-ethics - 333 words
10. achology-payment-methods - 366 words
11. achology-teaching-philosophy - 361 words
12. achology-vs-linkedin-learning-comparison - 393 words
13. how-to-request-achology-refund - 396 words
14. achology-no-transformation-promises - 410 words
15. who-verifies-achology-cpd-claims - 398 words
16. achology-anti-gatekeeping-pricing - 425 words
17. achology-pricing-versus-udemy-universities - 430 words
18. valts-achology - 431 words
19. is-achology-worth-the-money - 472 words
20. achology-lifetime-access-explained - 464 words
21. principle-based-reflective-discussion - 562 words
22. difference-between-monthly-annual-achology-membership - 346 words
23. course-completion-vs-competence - 355 words
24. no-credential-inflation-achology - 350 words
25. post-nominal-letters-achology-certificates - 333 words

All still sit within the help-answer band (320 to 1500 words). Each record's count-block now carries a corrected_S361_v2 line stating the word count and the two zero counts above, and each record's Sourcing record section documents this pass with Kain's ruling quoted.

One gate-logic finding surfaced and worked around during this pass: a markdown link whose visible text itself ends in a question mark can confuse content_gate.py's sentence-splitting regex, causing a paragraph that genuinely holds two sentences to be mis-counted as one. Found in no-credential-inflation-achology and worked around there and in one other record by rephrasing the link text to move the question mark out of the anchor text. Not fixed in content_gate.py itself: flagging it here so Code can decide whether the regex should be hardened, since other content types linking to help articles by their question-form titles could hit the same false positive.

Not affected by this pass: the standing brief asking Code to add an automated single-sentence check to content_gate.py's help-answer branch and re-run measurement across all 250 live articles (BRIEF__Ban_Single_Sentence_Paragraphs_In_Help_Answer_Gate_S361.md, still open in this folder). This was a manual remediation of the 25-record batch only; the other 225 live help articles have not been touched and still rely on that automated check once built.

OWED BACK: Kain's read of these 25 for exemplar fit under the corrected standard, before batch two (the next 25 of 191) runs. Nothing owed to TO Chat beyond the standing brief already in this folder.
