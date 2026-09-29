**Needs from Chat:** two rulings. (1) Whether the 30 question articles' shortfall (all held under 95 by the same three tests, none of which a body edit can fix) is read against the type's own ceiling, as your S139 question asked for the older articles. (2) What `contentHasShortParagraphs` on 34 of the 44 help answers is measuring, since the content gate passes every one of them.

# REPORT: the Rank Math scores of the 74 new drafts

**From:** Claude Code, S140 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** the score table owed in `BRIEF__Push_The_Cowork_Fixes_To_The_Live_Site_After_The_Courses_Page_S389` for the 30 question articles (post IDs 39270 to 39299) and 44 help answers (39300 to 39343) added this session. Kain pressed Rank Math's Recalculate Scores; I pressed nothing.

## How these were read, and one finding

**Rank Math's Recalculate Scores stored no score for any of these 74: every one still has an empty stored score on the install** (the install has 31 article drafts and 45 help drafts in all, and none of them carries a stored score, so the recalculation appears to skip drafts of these two types altogether). So the numbers below were read from Rank Math's own analyser in each page's editor, with `score_breakdown.py` (the writing guard on, nothing saved, no modified date moved), one page at a time. It is the same analyser the stored score comes from, but it is a reading, not a stored value, and no score is written to any page. The temporary reading session was destroyed afterwards.

## The result

| Type | Pages | Mean | 95 or over | Under 95 |
|---|---|---|---|---|
| Help answers | 44 | 96.9 | 44 | 0 |
| Question articles | 30 | 84.8 | 0 | 30 |

- **All 44 help answers score 96 or 100.** Their one short test on 34 of them is `contentHasShortParagraphs` (0 of 3). The content gate passes all 44 on its own paragraph rule (no paragraph over 60 words), so this looks like Rank Math reading the bare-text body, which has no paragraph tags, as one long paragraph; the same test held 55 of the older help answers in the S139 table. Unverified; asked of you above.
- **All 30 question articles are held under 95 by the same three tests, on every page:** `contentHasAssets` 0 of 6 and `keywordInImageAlt` 0 of 2 (none has a featured picture yet), and `lengthContent` 2 or 3 of 8 (the page-type length shortfall). Nothing in a body can lift these. The older pictured articles sit at 89 with a picture; these will not pass 89 or so once Kain's pictures land, for the reason the S139 report already gave.

## Per-page table

| Type | Page | Post | Score | Tests short of full marks (points got of max) |
|---|---|---|---|---|
| question-article | best-life-coaching-books | 39270 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | books-to-learn-nlp | 39271 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | cbt-vs-dbt | 39272 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | cbt-worksheets | 39273 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | cognitive-behavioural-therapy-app | 39274 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | counselling-vs-cbt | 39275 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | counselling-vs-psychotherapy | 39276 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | does-cbt-work-for-anxiety | 39277 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | does-life-coaching-work | 39278 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | does-person-centred-counselling-work | 39279 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | is-nlp-backed-by-science | 39280 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | is-nlp-dangerous | 39281 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | is-person-centred-therapy-humanistic | 39282 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | life-coach-vs-therapist | 39283 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | life-coach-yourself | 39284 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | life-coaching-models | 39285 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | life-coaching-questions | 39286 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | life-coaching-vs-mentoring | 39287 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | mindfulness-vs-cbt | 39288 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | nlp-techniques-you-can-try | 39289 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | person-centred-therapy-goals | 39290 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | person-centred-therapy-techniques | 39291 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | should-i-be-a-life-coach | 39292 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | types-of-cbt | 39293 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | use-nlp-on-yourself | 39294 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | what-does-a-life-coach-do | 39295 | 84 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 2 of 8 |
| question-article | what-is-nlp-natural-language-processing | 39296 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | who-is-cognitive-behavioural-therapy-for | 39297 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | who-is-life-coaching-for | 39298 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| question-article | why-life-coaching-is-bad | 39299 | 85 | contentHasAssets 0 of 6, keywordInImageAlt 0 of 2, lengthContent 3 of 8 |
| help-answer | accredited-nlp-certification | 39300 | 100 | none under 95 |
| help-answer | are-counsellors-in-demand | 39301 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | are-counsellors-regulated | 39302 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | become-a-certified-life-coach | 39303 | 100 | none under 95 |
| help-answer | become-a-life-coach-for-free | 39304 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | best-counselling-courses | 39305 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | can-a-life-coach-help-with-anxiety | 39306 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | can-life-coaches-use-cbt | 39307 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | cbt-course-levels-and-diplomas | 39308 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | cheap-counselling-courses | 39309 | 100 | none under 95 |
| help-answer | cheapest-life-coaching-certification | 39310 | 100 | none under 95 |
| help-answer | choose-a-good-life-coaching-course | 39311 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | counselling-courses-online | 39312 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | counselling-or-psychology | 39313 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | counselling-placements | 39314 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | counselling-qualification-levels | 39315 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | counsellor-without-a-degree | 39316 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | how-do-life-coaches-get-clients-and-set-prices | 39317 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | how-much-do-cbt-therapists-earn | 39318 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | how-to-become-a-cbt-coach | 39319 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | how-to-become-a-cbt-therapist | 39320 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | how-to-become-a-counsellor | 39321 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | icf-accredited-life-coaching-programs | 39322 | 100 | none under 95 |
| help-answer | is-a-life-coaching-certification-worth-it | 39323 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | is-life-coaching-legit | 39324 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | is-life-coaching-regulated | 39325 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | is-nlp-certification-legit | 39326 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | learn-cbt-for-free | 39327 | 100 | none under 95 |
| help-answer | life-coach-or-a-therapist | 39328 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | life-coach-with-psychology-degree | 39329 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | life-coaching-as-a-career | 39330 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | life-coaching-certification-online | 39331 | 100 | none under 95 |
| help-answer | life-coaching-experience | 39332 | 100 | none under 95 |
| help-answer | need-a-certification-or-a-degree | 39333 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | nhs-routes-into-cbt | 39334 | 100 | none under 95 |
| help-answer | nlp-certification-free | 39335 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | nlp-certification-levels | 39336 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | nlp-certification-online | 39337 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | study-cbt-online | 39338 | 100 | none under 95 |
| help-answer | train-in-nlp-and-hypnosis-together | 39339 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | what-is-a-life-coaching-niche | 39340 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | what-is-an-nlp-coach | 39341 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | will-counsellors-be-replaced-by-ai | 39342 | 96 | contentHasShortParagraphs 0 of 3 |
| help-answer | will-life-coaches-be-replaced-by-ai | 39343 | 96 | contentHasShortParagraphs 0 of 3 |

OWED BACK: the two rulings above.

*No em or en dashes in this file; checked before writing.*
