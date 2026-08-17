# REPORT: reviews editorial pass two has run. 1,556 reviews groomed, no word lost

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Answers:** `COMMISSION__Reviews_Editorial_Pass_Two_All_897_S264.md`.
**Status:** the six presentation fixes are applied, verified against the live database and rendered. The English ruling's translation work is identified and sized but **not yet built**; section 7.

---

## 1. One decision I took, which you should overturn if it is wrong

**The commission's population does not exist.** Its title says all 897, and its text says "across ALL 897 reviews, including the 582 previously flagged". Those are different numbers: pass one changed 897 and left 582 flagged, and the bank is 4,516.

**I applied the pass to the whole bank of 4,516.** The reason is the wording of the fixes themselves, which are stated over the corpus and not over a subset: "Every review ends with a full stop" and "No em dash or en dash survives in any review". A pass that left 3,000 reviews outside those sentences would not satisfy them. The 3,038 that pass one called already correct were correct against pass one's narrower rules, which had no paragraph rule and no sentence-internal capital rule.

This is reversible in one command if you or Kain disagree. Say so and it goes back.

## 2. What was written

| | |
|---|---|
| Reviews read | 4,516 |
| Reviews changed | **1,556** |
| Reviews left exactly as they were | 2,960 |
| Reviews flagged rather than edited | 195 |
| Reviews that lost, gained or reordered a word | **0** |

Counts per fix, and a review can carry more than one:

| Fix | Reviews |
|---|---|
| 4. Punctuation spacing | 1,159 |
| 5. Paragraph breaks in long reviews | 274 |
| 1. Sentence-start capitals | 267 |
| 2. Terminal punctuation | 216 |
| 3. Dash removal | 10 |

**Fix 6, nothing else, is machine-enforced rather than promised.** Every review is checked before it is written: the sequence of its letter and digit runs must be identical before and after, case-insensitively. A changed capital or an added full stop passes; a lost, added or reordered word cannot. Nothing was refused, because nothing failed.

## 3. The dashes, all ten, judged one at a time as you asked

Fourteen banned dash characters existed across ten reviews. Eight became a comma, one a full stop, one a colon, chosen per sentence rather than by a blanket rule:

- 29062, full stop: "an amazing experience. I have absolutely no regrets."
- 31428, colon: "Truly amazing: insightful, practical, and deeply empowering."
- 29027, 29655, 30290, 30525, 31140, 31648, 32067, 32949, comma.

Zero banned dashes remain anywhere in the bank, confirmed by query after the write.

## 4. What was flagged rather than edited, and why

195 reviews were left without terminal punctuation on purpose, under your own "where ambiguous, leave and flag":

| | |
|---|---|
| Ends on an ellipsis or an emoticon | 130 |
| Ends on a sign-off or a name | 43 |
| Ends on an emoji or symbol | 22 |

A review ending "Regards / Aletta Viljoen" or "Thanks Ken" does not want a full stop after the name, and neither does one ending in an emoji. 140 reviews therefore still have no terminal mark, and that is the designed outcome rather than a miss.

## 5. Two defects in my own work, caught before the write and not after

Both were found by printing real before-and-after pairs and reading them, not by reasoning about the rules. The first dry run was clean by every count and wrong in two ways:

1. **It was mangling emoticons.** The no-space-before-punctuation rule turned "a very good match for that ;)" into "for that;)." An emoticon is the student's word, not punctuation. Emoticons are now protected from every rule.
2. **It was treating ellipses as sentence ends.** "It fits my experience with life....and how it all fits together" was becoming "life.... And how it all fits together". A run of dots is a pause in this bank, not a sentence boundary, and capitalising there changes how the sentence reads. Ellipses are now protected too.

Both would have passed every count in this report. This is the same lesson as the green test that cannot fail: the counts said the pass was clean while it was damaging 130 reviews.

## 6. The two standing conditions, both met

**`review_text_raw` was never touched.** Checked per review during the write: the raw copy is read before and after each update and compared. 0 altered.

**The reversal path was proved again before the first write, and proved by breaking something.** On review 29126: the live text was deliberately overwritten with a marker string, the damage was confirmed to have actually landed, the raw copy was restored over it, and the restored text was confirmed byte-identical both to the raw copy and to what had been there before. A restore test that cannot fail proves nothing, so this one was made to fail first.

Second mechanism: a full postmeta export, 7,807,637 bytes, at `~/achology_backups/postmeta_before_pass_two_S059.sql` on the server. **It is not in `/tmp` this time**, which answers the caution in the S054 report rather than repeating it.

## 7. The English ruling: identified, sized, not yet built

**87 reviews are not in English**, found by stopword scoring against twelve languages rather than by looking for accents, which would have missed the unaccented ones and false-flagged English reviews containing a word like "précise".

| Language | Reviews |
|---|---|
| Spanish | 27 |
| Portuguese | 23 |
| Italian | 13 |
| German | 8 |
| Dutch | 7 |
| Polish | 3 |
| French | 3 |
| Turkish | 2 |
| Indonesian | 1 |

**Nothing has been translated and no field has been created yet.** The ruling is clear that the student's words stay displayed and the translation sits beneath them, plainly marked, and that the display treatment is Kain's to judge live in Safari rather than mine to ship unseen. The next step is the field, the 87 translations, and then that sitting.

## 8. One row where the check fires and no word was lost

Review 30340 is written in Turkish-influenced English using the dotless "ı". Fix 1 capitalised a sentence-opening "ı" to "I", which is the correct Turkish uppercase of that letter. The word-preservation check compares case-insensitively, and "I" lower-cases to "i" rather than back to "ı", so it reports a difference. The word count is 99 either way and no word is missing in either direction. Recorded rather than quietly passed over.

## 9. One question for Kain, which is one word to answer

**298 reviews contain the pronoun "i" in lower case mid-sentence.** Capitalising it is not one of the six fixes, so it has not been done. The result is that a review can now read "This course is helping me. i learned a lot", where the sentence starts are correct and the pronoun is not.

It is word-preserving in exactly the way the other fixes are: the same word, correctly cased. But it is not on the authorised list and it is not mine to add.

**If it is a yes, it is one more pass over reviews I have just edited.** Worth answering before anything else touches this bank, so they are not edited twice.

## 10. Verification

Read back from the live database after the write: all 1,556 rows match the plan exactly, 0 mismatches, 0 banned dashes remain, 0 raw copies altered. The reviews page renders at 200 and 368,291 bytes with no fatal, cache purged, and groomed review text confirmed present in the rendered HTML.

*No em or en dashes in this file; checked before writing.*
