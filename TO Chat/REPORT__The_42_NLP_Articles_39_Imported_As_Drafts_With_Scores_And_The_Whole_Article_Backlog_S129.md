# REPORT: the 42 NLP articles, 39 imported as drafts and scored, 3 refused; and the whole written backlog, counted against the install

**From:** Claude Code, factory session, S129, Tuesday 22 September 2026. **To:** Claude Chat.
**Answers:** `BRIEF__Import_The_FortyTwo_NLP_Instructor_Articles_As_Drafts_S367.md`.
**Board card:** Kain's resource posts (the 42 articles).
**Kain's word in the sitting, which set this order:** identify every backlogged article, get it updated, uploaded and passing Rank Math 90; then the quote page, then the workbook page, then the rest of the Knowledge Hub pages systematically, governed by the DSRDs.

## 1. The 42: what was done

- **Pictures:** Kain's 42 PNG masters (1980 by 945) converted by `tools/image_pipeline.py` at the article hero slot, 680 wide, quality 82: 84 WebP files, 12 to 39KB, all inside the 200KB budget. Named from each record's own `featured_image`. Two records still carry the pre-retitle picture name (`fountain-or-a-drain` names `more-energy-than-you-found-them.webp`; `whats-the-key-to-winning-hearts-and-minds` names `factors-that-make-people-more-influential.webp`), mapped per Cowork's S366 image map. Theme commit 2b3f9cd.
- **Import:** `import_field_authority_articles.py --type instructor-article`, the route that reads records directly. **39 created as drafts, 39 of 39 verified clean** against their records (title, excerpt, section count, category, tags, image). Nothing published. The column contract was not widened: this importer reads the records' own fields, so the S301 contract question does not arise.
- **H9:** the importer's registered hash was re-recorded after reading its only change since review (commit 4f8b4fa, inside `verify()`, a read). The create payload still hardcodes draft.

## 2. The three refused, at stage 5

`balance-the-main-areas-of-life`, `pattern-recognition-superpower`, `think-objectively`: **each body carries a list, which the importer's converter does not render.** Two routes, and the choice is Chat's: the converter learns lists (Code's tooling; lists are legitimate reading content and the theme styles them), or Cowork rewrites the three lists as prose. Recommendation: the converter, since the next batch will meet the same thing.

## 3. The scores, read off each draft in the editor, nothing saved

| Post | Article | Score |
|---|---|---|
| 36847 | all progression is impossible without change | 89 |
| 36849 | assumptions damage relationships | 89 |
| 36851 | build genuine rapport | 89 |
| 36853 | build self-control | 89 |
| 36855 | can you be too self-aware | 89 |
| 36857 | introverted or extroverted | 89 |
| 36859 | change is the only constant | 89 |
| 36861 | confuse opinions with facts | 89 |
| 36863 | connected to your future self | 89 |
| 36865 | cover up incompetence with head knowledge | 89 |
| 36867 | disagreement vs division | 89 |
| 36869 | every decision is a trade-off | 89 |
| 36871 | everyone experiences reality differently | 89 |
| 36873 | feeling stuck in life | 91 |
| 36875 | fixed or growth mindset | 89 |
| 36877 | forget your mistakes but remember their lessons | 89 |
| 36879 | fountain or a drain | 89 |
| 36881 | freedom vs security | 89 |
| 36883 | growing or standing still | 89 |
| 36885 | happiness is a delusion fulfilment is not | 89 |
| 36887 | labels vs true identity | 89 |
| 36889 | living according to your values | 89 |
| 36891 | personal growth requires discomfort | 89 |
| 36893 | positive vs negative motivation | 91 |
| 36895 | rational or emotional thinker | 89 |
| 36897 | remembered for | 86 |
| 36899 | saying less more influential | 89 |
| 36901 | self-acceptance vs self-improvement | 89 |
| 36903 | stages of building strong relationships | 89 |
| 36905 | stages of human development and maturity | 89 |
| 36907 | step outside your comfort zone | 89 |
| 36909 | taking responsibility creates personal growth | 89 |
| 36911 | thoughts and emotions connection | 89 |
| 36913 | time perspective | 89 |
| 36915 | turn a vision into a goal | 89 |
| 36917 | types of listening | 89 |
| 36919 | winning hearts and minds | 89 |
| 36921 | need to prove ourselves | 89 |
| 36923 | your relationship with money tells a story | 89 |

**2 at 91, 36 at 89, 1 at 86. 37 sit under the 90 gate.**

## 4. Why 89, read off the analyser rather than guessed

On the 89s, every one of Rank Math's fourteen listed tests reads green (read on three drafts, 36847, 36869 and 36897's twin tests). The points missing are graded partials the panel shows green: **length**, and **media**. The two at 91 are the only two bodies over 2,000 words (2,092 and 2,049); the 89s run 1,800 to 1,950. And every one carries exactly one picture, the hero, where Rank Math's media points want four.

So the gap is the page type, not the records. The pipeline, section 5 item 8, says length "is graded, never padded", and item 6 says where a page type carries fewer than four images "the length and media tests are accepted as partial, and the record says so." Read literally, these 37 are at the honest ceiling for a one-image article under 2,000 words, and that ceiling sits one point under the gate. **That is a ruling for Kain, through Chat, not a fix for Code:** accept 89 for this page type as the pipeline's own partial-acceptance sentence allows; or give the instructor article in-body pictures, which Kain makes; or lengthen genuinely where a piece has more to say. Precedent worth knowing: the 24 DSM articles went live at 86 and 88 on Kain's word at S119.

**One real record fault:** `remembered-for` (86) fails "Focus Keyword at the beginning of the SEO title". That is a source fix, Cowork's, at the record; it then re-enters at stage 3.

Owed by Code and not done this session: the score line into each page's DSRD 6 record (the record generator run), and the three inbound links per page, since these records' `inbound_from` was not read this pass.

## 5. The whole written backlog, counted this session

Every record in Content Records matched by address against the install's post list, read this session:

| Record type | On disk | Live | Draft on site | Not on site |
|---|---|---|---|---|
| instructor-article | 102 real records | 60 | 39 (today) | **3** (the lists, above) |
| book-note | 149 | 125 | 0 | **24**, every one's record reading publish; none exists on the install under any address |
| help-answer | 232 | 218 | 0 | **14** new CBT answers (the HELP__ files), with no BATCH handover yet |
| hub-guide | 1 | 0 | 0 | **1**, `cognitive-behavioural-therapy`, record says draft |
| hub-question-article | 1 exemplar | 0 | 0 | **1**, approved S374; its importer question is your S374 ASK |
| field-authority-article | 119 | 117 | 1 exemplar | 1 superseded |
| author-biography | 51 | 51 | 0 | 0 |
| quote-page | about 410 | 1 | 249 | **182** |
| workbook | 1 | 0 | 0 | 1, the Karpman workbook, waiting on its page |

Also waiting, not new pages: the 216 corrected help answers (nine batches in FROM Cowork), held by your own S374 list behind Kain's softening ruling and the contraction count.

**The 24 book notes** are the ones your S374 list asks about ("153 records on disk and 125 pages are published: which 28 are not on the install, and why?"). Twenty-four of the 28 are real records (the other four are reports sitting in the folder). Why they never imported is not yet read; the S361 list's "16 held" from the three book note batches is the likely reason for most.

## OWED BACK

A ruling on the 89 ceiling for one-image instructor articles; the route for the three list bodies; the `remembered-for` title fixed at source; and the BATCH handover for the 14 CBT help answers and the hub pieces when they are ready.

*No em or en dashes in this file; checked before writing.*
