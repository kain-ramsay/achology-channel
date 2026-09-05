# COMMISSION: Reviews editorial pass two, all 897, ruled by Kain at S264

**From:** Claude Chat, S264. **Authority:** Kain's ruling, S264.
**Sequencing:** SATISFIED, S264. Chat read REPORT__Normalisation_Apply_Pass_Result_S054 this session and confirms it: 897 changed and verified by query, 582 flagged untouched, both reversals in place before the first write. Pass two may run at your next session. Two standing conditions: (1) `review_text_raw` is never touched by this pass or any future one; it is the permanent copy of the students' original words and the reversal mechanism for everything. (2) The /tmp dump need not move (Chat's call): the raw copy in the database is the durable reversal. Prove the reversal path once more before pass two's first write, same as pass one.

## IMMEDIATE ITEM, not sequenced: the nutrition review

This one item runs at your next session, independent of the sequencing lock below. Kain has spotted a review mentioning "nutrition", almost certainly a Udemy import mistake, as no Achology course covers nutrition. Search all 897 for the term. Any review that is plainly about a nutrition course (not ours) is removed, with the removal reversible and the removed text returned through TO Chat so Kain can confirm it was the right one. If the term appears only metaphorically in an otherwise genuine review of one of our courses, do not remove it; return it flagged instead. Report the count found either way.

## Context you need (you cannot see our conversation)

At S263 Kain authorised your conservative normalisation apply pass: 897 reviews, 582 flagged left untouched including the 159 written entirely in lower case. We are awaiting that result. Tonight Kain ruled pass two: a full editorial grooming pass across ALL 897 reviews, including the 582 previously flagged, making word-preserving presentation fixes only. The principle he ruled: every word the student wrote is preserved; only presentation is fixed. These are verified trust signals and must stay provably real.

## The fixes authorised, and no others

1. **Sentence-start capitals.** First letter of every sentence capitalised. This authorises sentence-casing the 159 all-lower-case reviews you flagged at pass one.
2. **Terminal punctuation.** Every review ends with a full stop (or its existing ?, !). Sentences within a review that plainly end without punctuation get a full stop where the boundary is unambiguous; where ambiguous, leave and flag.
3. **Dash removal.** No em dash (U+2014) or en dash (U+2013) survives in any review. Replace with a comma, colon, or full stop, whichever the sentence reads naturally with. Hyphens in compound words stay.
4. **Punctuation spacing tidy.** Double spaces to single; space before punctuation removed; missing space after punctuation added.
5. **Paragraph breaks in long reviews.** Reviews over roughly 80 words get breaks at natural sentence boundaries, two to four sentences per paragraph, so the page shows the line breaks Kain approved seeing. Breaks only ever at sentence boundaries; never split a sentence.
6. **Nothing else.** No spelling correction, no grammar rewording, no word added or removed beyond the punctuation marks above. If a review needs more than these fixes to read acceptably, flag it in your return rather than editing it.

## The English ruling

Non-English reviews are NOT replaced with translations. Kain's ruling: the original text stays displayed as the student's words, with an English translation beneath it, plainly marked (for example: "Translated from Spanish"). Replacing a student's words with a translation is forbidden; a sceptical visitor who spots it loses trust in all 897.

Implementation: produce the translation per non-English review, store it in its own field (never overwriting the original), and note that the reviews template needs a small display addition for the marked-translation treatment. Build the field and data now; the template treatment is a visual Kain judges live in Safari at his next sitting with you, so present it there rather than shipping it unseen.

## Mechanics

WordPress only, same as pass one. Both reversal mechanisms in place before the first write. Return through TO Chat: counts per fix type, the flagged-rather-than-edited list, the non-English count with languages found, and confirmation the reversal path was tested.

*No em or en dashes in this file; checked before writing.*
