**Needs from Chat:** a brief to Cowork for 15 source fixes (14 Handbook quotes without their keyword in a subheading, 1 book note short on length), or a ruling that they stand as named exceptions.

# REPORT: the score table for the 40 pages published today

**From:** Claude Code, factory session, S133, Thursday 24 September 2026. **To:** Claude Chat.
**For:** the factory session.
**Answers:** The Publish Ready Pipeline stage 6 and section 5.2 for the batch landed under `RULING__Eleven_Book_Notes_And_Four_Help_Answers_Gate_Clean_Push_Them_S383` and `RULING__All_50_Handbook_Quote_Pages_Gate_Clean_Push_Them_S383`. Stage 7's sitting date is not needed: Kain published all 40 himself today.

## How the scores were read

Kain pressed Rank Math's Recalculate Scores twice (his button, per his S131 ruling), and each time Code read `rank_math_seo_score` off the install. The per-test breakdown of five pages was read in the editor with `score_breakdown.py`. Bars: book note 88, help answer 81, quote page 88 (Kain, S131, not yet in DSRD 6: `RULING__Kain_Rules_Score_Bars_89_And_88_S131` in the Archive).

## Two faults found and fixed before the second read, both Code's

1. **Nine book notes read 21.** `book_note_import.py --write` fills only EMPTY master cells, so nine books whose master rows already held old Rank Math values ("... book summary" keywords, titles with a stray backslash) went live with those rather than their records' values. The record is the single source (pipeline section 1, rule 1), so the three columns were rewritten from the records (`--overwrite-columns prod_rm_focus_keyword,prod_rm_seo_title,prod_rm_seo_description`) and sent with `--fields-only`; all 11 now match their records on all three fields. **Worth a line in the pipeline or the importer:** a record's Rank Math fields should always win over the master's, or this repeats on every book whose master row predates its record.
2. **The 25 new Handbook quotes had no quote card,** so no featured image and one picture point short. Baked and attached with `make_quote_cards.py --attach` on Kain's word; all 275 live quotes now carry design a550389032b5.

## The table, after the second rescore

| Type | Page | Post | Score |
|---|---|---|---|
| book_note | mothers-who-cant-love | 38461 | 86 |
| book_note | born-for-love, the-tao-of-fully-feeling, a-new-guide-to-rational-living, the-quick-and-easy-way-to-effective-speaking, originals, meditations-for-mortals, talking-to-crazy, come-together, on-the-tranquility-of-mind, critique-of-practical-reason | 38453, 38529, 38527, 38467, 38465, 38459, 38451, 38455, 38463, 38457 | 88 each |
| help answer | drama-triangle-training, maslows-hierarchy-of-needs-course, viktor-frankl-course, albert-ellis-course | 38522, 38521, 38520, 38519 | 100 each |
| quote | most-people-dont-dialogue | 38501 | 82 |
| quote | what-is-a-life-coaching-breakthrough-session, why-a-good-coach-listens-without-an-agenda, coaching-is-learning-and-action-toward-a-goal, every-coaching-relationship-begins-with-a-goal, why-you-need-clear-priorities-in-life, trust-is-the-key-ingredient, wisdom-is-not-the-same-as-intelligence, every-major-breakthrough-in-history, a-good-coach-will-ask-probing-questions, purpose-is-the-cumulative-outcome, vision-is-always-future-oriented, listen-with-a-goal-of-responding, what-your-values-really-are | 38509, 38515, 38511, 38494, 38508, 38495, 38496, 38504, 38497, 38498, 38499, 38500, 38506 | 85 each |
| quote | how-fear-distorts-the-future, why-we-misinterpret-what-people-say, why-people-resist-change-until-they-have-to, why-you-should-consider-your-values-before-deciding, what-time-freedom-really-means, what-is-emotional-perception, how-your-thoughts-form-your-reality, why-change-never-happens-overnight, why-people-invest-in-life-coaching, responsibility-makes-you-more-free, how-principles-shape-decisions | 38502, 38518, 38517, 38516, 38514, 38513, 38512, 38503, 38510, 38505, 38507 | 88 each |

**25 of 40 at or over their bar.**

## The 15 under their bar, and why (read off the tests, not guessed)

- **The 14 quotes at 85 and 82:** breakdowns read on 38495 (85) and 38501 (82): each loses `keywordInSubheadings` 0 of 3, beside the type's ceiling losses (`lengthContent` 2 of 8, `contentHasAssets` 2 of 6). The focus keyword is in none of the body's subheadings. A copy fix at source: work the keyword into one subheading of each record, then Code pushes and rereads. The content gate passed all 14, so it does not check this.
- **mothers-who-cant-love at 86:** `lengthContent` 3 of 8 and `contentHasAssets` 1 of 6; every other test full. Length is the record's; drafted up or accepted as a named exception is Chat's.

## Not done

Page-level DSRD 6 records do not yet exist for today's 11 book notes (`page_readiness_board.py` lists them "no record"); `--backfill` writes into the records folder and was not run this session.

## OWED BACK

The Cowork brief for the 15, or a ruling that they stand as named exceptions.

*No em or en dashes in this file; checked before writing.*
