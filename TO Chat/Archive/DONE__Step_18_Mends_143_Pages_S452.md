> ARCHIVED by Chat S454 (2 November 2026): its record mends are all in BRIEF__Update_The_106_Mended_Records_Under_The_Bar_S453 (signed S453, queued for Code); Code's rescore after that import is the next evidence.

**For Chat. What this needs from you:** read the score table for the 143 step 18 pages not accepted below the mark, and send the record mends named in section 4 to a writing session; Code needs nothing else from you on BRIEF__Update_The_151_Step_18_Mended_Records_S452.

# DONE: the 143 step 18 pages not accepted below the mark (Code, factory side session, 2 November 2026)

**In one line.** 140 of the 143 pages are on the build site from their signed records and read back field by field; 3 hub questions have no post and were not created; 62 read 86 or more and 78 read under 86. Every page under 86 is under for a reason in its record, its fixed address or the workbook landing copy, never the import.

## 1. What was done

- **91 article pages** (field authority 50, hub questions 13 of 16, hub guides 8, instructors 4, book notes 7, Help answers 6) updated with `article_body_update.py --apply --with-seo`: body, excerpt, search title and search description from each record, 0 refused. The 8 pages accepted below the mark are in the other DONE and were sent the same way.
- **Focus phrases and picture descriptions.** The body tool does not carry them, so 59 values were written from the records with `wp post meta update` (rank_math_focus_keyword, and the featured picture's alt), then read again: 96 of 96 match. The johari window Help answer's focus now carries its variants as the Help importer writes them. Atomic Habits' book cover description now reads as its record.
- **Titles.** 13 pages carried an older title than their signed record: helping-people-help-themselves, karpman-drama-triangle, listening-to-understand-not-to-reply, the-foundational-principles-of-person-centred-counselling, the eight hub guides and how-does-mental-health-affect-sleep. Each now carries its record's post_title. No title changed at step 18; these were signed earlier and never reached the page.
- **The eight hub guides held at S201** now carry their outside link, so they landed as DONE__The_Hub_Guides_On_The_Build_Site_S201 section 3 set out: body, title and Pillar Content on all eight. The five drafts (behavioural-psychology, cognitive-psychology, developmental-psychology, hypnotherapy, social-psychology) were published under clearance f4edeae422f92b82, with `--override` quoting Harness Rule 8 (Kain, S417: signed pages are published on the build site, which stays noindex until go-live) and this brief; each refused only the draft's 404. Their S429 redirects (rows 37, 40, 41, 42 and 45) were switched off on RULING__The_28_Unpublished_Articles_Decided_And_The_S429_Tool_Changes_Kept_S432, each address proved to answer 200, and `publish_gate.py --update --clear` at the live addresses passed all five.
- **The six hub question drafts with no picture** (how-does-mental-health-affect-sleep, how-to-improve-mental-wellbeing, is-mental-health-genetic, mental-health-without-therapy-or-medication, should-mental-health-be-taught-in-schools, why-mental-health-is-important-in-everyday-life) carry their mended text and stay drafts.
- **Workbooks, 52.** All 52 documents were rebuilt from today's records with the workbook build tool; every one passed its parse check, each cover came from its record's cover_image, and no rotation row was written. The PDF and render of each are in The Stock's Built Workbooks folder. The brief named 26 CBT documents; all 33 CBT records changed in their bodies at step 18 (the banned word and the writing space lines), so all 33 were rebuilt and updated, not 26. `import_workbook_pages.py --push`: 33 pages updated in place and 19 sent (18 created, and the Ladder of Inference draft 40321 updated); `--verify` 52 of 52 match. The 19 were published under the same clearance and the same ruling as the 33 at S206. The re-gate at their live addresses refuses them only on the rendered body carrying no internal and no external link, as at S206. Staging copies were moved to `~/media-holding/workbook-import-S452`, and `media_gate.py --report` reads CLEAN.
- **One tool change.** `import_workbook_pages.py` refused all 52 because its signature check read only a date written as 2026-11-02, and the vault gate now writes "2 November 2026". It now reads both forms; checked on six cases (both forms on 2 November pass; 20 October in either form, a malformed date and no signature fail).

## 2. Not done, and why

- **is-mental-health-an-illness, is-mental-health-getting-worse, mental-health-and-mental-wellbeing:** no post exists on the build site and none has a picture, so none was created. They wait on their pictures.
- **KEYWORD_REGISTER.csv:** untouched; the brief says it is not covered here.
- **post_date and watch_due** are not written back into the signed records, which the vault gate hashes.

## 3. The scores

Read by Code off each built page in the editor (`score_run.py` session, one page every 12 seconds, nothing saved), in turns agreed with the other factory sessions. The failing tests are every test the analyser marks failed. Bar: 86 for every kind.

| Kind | Pages | 86 or more | Under 86 | Median |
|---|---|---|---|---|
| Field authority | 50 | 31 | 19 | 89 |
| Hub questions | 16 (13 with a post) | 11 | 2 | 86 |
| Hub guides | 8 | 8 | 0 | 94 |
| Instructor articles | 4 | 2 | 2 | 88 |
| Book notes | 7 | 6 | 1 | 88 |
| Help answers | 6 | 4 | 2 | 93 |
| Workbooks | 52 | 0 | 52 | 13 |

## 4. Why each page under 86 is under, and where it is mended

- **The address test alone (keywordInPermalink), 21 pages.** 18 field authority pages at 84: triggers-that-lead-to-relationship-breakdowns, carl-rogers-person-centered-counseling, decide-with-confidence-10-timeless-principles-for-wise-decision-making, psychology-history-timeline, the-myth-of-having-it-all, unraveling-behaviorism-psychology-a-historical-perspective, embracing-your-innermost-values, psychology-theories-for-motivation, starvation-insights-from-ancel-keys-the-minnesota-experiment, the-truth-about-eloquence, unlocking-life-coaching-excellence, 10-ethically-dubious-experiments, dynamics-of-leading-effective-diplomatic-discussions, from-roots-to-revolution, history-and-timeline-of-counselling-psychology, how-immediacy-shapes-engaging-and-impactful-conversations, the-reality-of-life-coaching and timeless-lessons-from-the-life-and-works-of-hans-j-eysenck. Also two instructor articles (AW04, what-does-leading-under-pressure-teach-you, 82; cover-up-incompetence-with-head-knowledge, 84) and nature-emerson (82), whose address the brief says cannot carry its phrase. These are the "about ten more" the brief names, and there are 21. Each keeps its address, so each stays under 86 unless its focus phrase moves to words its address carries.
- **the-foundational-principles-of-person-centred-counselling, 44:** keywordInTitle and titleStartWithKeyword. Its focus phrase "principles of person-centred counselling" is not in its signed search title "Person-Centred Counselling: The Principles Rogers Set Down". A record mend: the phrase or the search title.
- **HELP__valts-achology and HELP__cips-when-need-them, 84:** the address test and no outside link (both are Achology-only answers, which the body tool lets pass without one).
- **mental-health-without-therapy-or-medication, 85:** no picture yet (a held draft). Its other tests pass.
- **best-cbt-books, 85:** keywordInSubheadings. A record mend: the phrase in one subheading.
- **The 52 workbooks, 5 to 74:** the two causes in ASK__Workbook_Landing_Copy_Links_And_Focus_Phrases_S206, still in the records: no link in the landing copy (linksHasInternal, linksHasExternals), and the "{name} workbook" focus phrase not word for word in the title, description, opening or subheadings. The 19 older pages land with the same two causes. A record mend in each landing copy.

## 5. The table, every page

| Batch | Record | Post | Focus phrase | Score | Bar | Failing tests |
|---|---|---|---|---|---|---|
| mend_bn | nature-emerson | 33815 | nature by emerson | 82 | 86 | keywordInPermalink |
| mend_bn | a-way-of-being | 33791 | a way of being | 88 | 86 | none |
| mend_bn | atomic-habits-clear | 35936 | atomic habits clear | 88 | 86 | none |
| mend_bn | civilization-and-its-discontents | 36535 | civilization and its discontents | 88 | 86 | none |
| mend_bn | the-4-hour-body | 33824 | the 4-hour body | 88 | 86 | none |
| mend_bn | the-high-5-habit | 37048 | The High 5 Habit | 88 | 86 | none |
| mend_bn | the-relationship-cure | 33842 | the relationship cure | 88 | 86 | none |
| mend_fa | an-exploration-of-freuds-psychoanalytic-theory | 35190 | psychoanalytic theory | 89 | 86 | none |
| mend_fa | sigmund-freuds-defence-mechanisms | 35270 | defence mechanisms | 89 | 86 | none |
| mend_fa | two-factor-models-of-personality | 35599 | two-factor models of personality | 89 | 86 | none |
| mend_fa | unveiling-attachment-insights-from-harlows-monkey-experiments | 35314 | monkey experiments | 89 | 86 | none |
| mend_fa | 13-morally-dubious-psychology-experiments | 35180 | psychology experiments | 89 | 86 | none |
| mend_fa | a-guide-to-building-inner-resilience | 35479 | inner resilience | 89 | 86 | none |
| mend_fa | qualities-of-a-true-leader | 35268 | qualities of a true leader | 89 | 86 | none |
| mend_fa | rosalynn-carter-and-mental-health-stigma | 35548 | rosalynn carter | 89 | 86 | none |
| mend_fa | the-importance-of-self-awareness | 35436 | self-awareness | 91 | 86 | none |
| mend_fa | neuro-linguistic-programming-myths | 35538 | neuro-linguistic programming myths | 89 | 86 | none |
| mend_fa | the-psychology-of-self-improvement | 35581 | psychology of self-improvement | 89 | 86 | none |
| mend_fa | triggers-that-lead-to-relationship-breakdowns | 35304 | relationships break down | 84 | 86 | keywordInPermalink |
| mend_fa | carl-rogers-person-centered-counseling | 35200 | what is person-centred counselling | 84 | 86 | keywordInPermalink |
| mend_fa | a-guide-to-breaking-bad-habits | 35424 | bad habits | 91 | 86 | none |
| mend_fa | conditioning-fear-insights-from-the-little-albert-experiment | 35202 | little albert | 89 | 86 | none |
| mend_fa | decide-with-confidence-10-timeless-principles-for-wise-decision-making | 35204 | wise decisions | 84 | 86 | keywordInPermalink |
| mend_fa | psychology-history-timeline | 35262 | history of psychology timeline | 84 | 86 | keywordInPermalink |
| mend_fa | the-4-stages-of-human-evolution | 35556 | stages of human evolution | 89 | 86 | none |
| mend_fa | the-myth-of-having-it-all | 35572 | have it all | 84 | 86 | keywordInPermalink |
| mend_fa | the-stages-of-change-model | 35588 | stages of change | 89 | 86 | none |
| mend_fa | unraveling-behaviorism-psychology-a-historical-perspective | 35312 | what is behaviourism | 84 | 86 | keywordInPermalink |
| mend_fa | embracing-your-innermost-values | 35500 | core values | 84 | 86 | keywordInPermalink |
| mend_fa | psychology-theories-for-motivation | 35264 | theories of motivation | 84 | 86 | keywordInPermalink |
| mend_fa | starvation-insights-from-ancel-keys-the-minnesota-experiment | 35553 | minnesota starvation experiment | 84 | 86 | keywordInPermalink |
| mend_fa | the-core-competencies-of-coaching | 35559 | core competencies | 89 | 86 | none |
| mend_fa | the-eisenhower-decision-making-matrix | 35565 | the eisenhower | 89 | 86 | none |
| mend_fa | the-truth-about-eloquence | 35592 | 7-38-55 rule | 84 | 86 | keywordInPermalink |
| mend_fa | unlocking-life-coaching-excellence | 35606 | grow coaching model | 84 | 86 | keywordInPermalink |
| mend_fa | what-habits-are-and-why-people-get-stuck | 35318 | people get stuck | 86 | 86 | titleStartWithKeyword |
| mend_fa | 10-ethically-dubious-experiments | 35176 | unethical psychology experiments | 84 | 86 | keywordInPermalink |
| mend_fa | dynamics-of-leading-effective-diplomatic-discussions | 35208 | diplomatic communication | 84 | 86 | keywordInPermalink |
| mend_fa | embracing-your-shadow-side | 35502 | your shadow | 89 | 86 | none |
| mend_fa | from-roots-to-revolution | 35430 | third force psychology | 84 | 86 | keywordInPermalink |
| mend_fa | history-and-timeline-of-counselling-psychology | 35232 | history of counselling psychology | 84 | 86 | keywordInPermalink |
| mend_fa | how-immediacy-shapes-engaging-and-impactful-conversations | 35432 | immediacy in counselling | 84 | 86 | keywordInPermalink |
| mend_fa | the-reality-of-life-coaching | 35583 | what is life coaching | 84 | 86 | keywordInPermalink |
| mend_fa | lessons-from-how-to-win-friends-influence-people | 35246 | how to win friends | 89 | 86 | none |
| mend_fa | the-smart-goal-setting-framework | 35300 | smart goal | 89 | 86 | none |
| mend_fa | the-worlds-most-influential-psychologists | 35302 | most influential psychologists | 89 | 86 | none |
| mend_fa | timeless-lessons-from-the-life-and-works-of-hans-j-eysenck | 35595 | hans eysenck | 84 | 86 | keywordInPermalink |
| mend_fa | finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning | 35226 | search for meaning | 89 | 86 | none |
| mend_fa | understanding-your-core-values | 35440 | core values | 89 | 86 | none |
| mend_fa | aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology | 35186 | aaron beck | 89 | 86 | none |
| mend_fa | helping-people-help-themselves | 35518 | people help themselves | 89 | 86 | none |
| mend_fa | karpman-drama-triangle | 35434 | karpman drama triangle | 91 | 86 | none |
| mend_fa | listening-to-understand-not-to-reply | 35531 | not to reply | 89 | 86 | none |
| mend_fa | the-foundational-principles-of-person-centred-counselling | 35284 | principles of person-centred counselling | 44 | 86 | keywordInTitle, titleStartWithKeyword |
| mend_fa | the-power-of-useful-thinking | 35579 | useful thinking | 89 | 86 | none |
| mend_fa | exploration-of-the-split-brain-experiment-by-roger-sperry | 35222 | split brain experiment | 89 | 86 | none |
| mend_fa | misattribution-of-arousal-study-insights-into-emotional-perception | 35254 | misattribution of arousal | 91 | 86 | none |
| mend_ha | HELP__valts-achology | 10014 | VALTS learning sessions | 84 | 86 | keywordInPermalink, linksHasExternals, linksNotAllExternals |
| mend_ha | HELP__cips-when-need-them | 10016 | CIPS credit | 84 | 86 | keywordInPermalink, linksHasExternals, linksNotAllExternals |
| mend_ha | HELP__what-is-achology | 218 | what exactly is Achology | 88 | 86 | keywordInPermalink, keywordInSubheadings |
| mend_ha | HELP__where-can-i-learn-the-johari-window | 42030 | johari window | 100 | 86 | keywordInContent, keywordInSubheadings |
| mend_ha | HELP__achology-uk-register-learning-providers | 10025 | UK Register of Learning Providers | 93 | 86 | keywordInPermalink |
| mend_ha | HELP__what-do-you-learn-in-social-psychology | 41481 | learn in social psychology | 100 | 86 | keywordInContent, keywordInSubheadings |
| mend_hg | behavioural-psychology | 39456 | behavioural psychology | 94 | 86 | none |
| mend_hg | cognitive-psychology | 39460 | cognitive psychology | 94 | 86 | none |
| mend_hg | developmental-psychology | 39464 | developmental psychology | 94 | 86 | none |
| mend_hg | hypnotherapy | 39480 | hypnotherapy | 94 | 86 | none |
| mend_hg | social-psychology | 39508 | social psychology | 94 | 86 | none |
| mend_hg | values-and-decision-making | 39510 | values and decision making | 91 | 86 | contentHasShortParagraphs |
| mend_hg | skilled-helper | 39506 | skilled helper | 91 | 86 | contentHasShortParagraphs |
| mend_hg | human-nature-and-behaviour | 39476 | human nature and behaviour | 94 | 86 | none |
| mend_hq | cbt-vs-dbt | 39272 | cbt vs dbt | 88 | 86 | none |
| mend_hq | counselling-vs-psychotherapy | 39276 | counselling vs psychotherapy | 88 | 86 | none |
| mend_hq | counselling-vs-cbt | 39275 | counselling vs cbt | 88 | 86 | none |
| mend_hq | conditions-of-worth | 39799 | conditions of worth | 88 | 86 | none |
| mend_hq | how-does-mental-health-affect-sleep | 40373 | how does mental health affect sleep | 86 | 86 | contentHasAssets, keywordInImageAlt |
| mend_hq | how-to-improve-mental-wellbeing | 40374 | how to improve mental wellbeing | 86 | 86 | contentHasAssets, keywordInImageAlt |
| mend_hq | is-mental-health-genetic | 40375 | is mental health genetic | 87 | 86 | contentHasAssets, contentHasShortParagraphs, keywordInImageAlt |
| mend_hq | mental-health-without-therapy-or-medication | 40376 | mental health without therapy | 85 | 86 | contentHasAssets, keywordInImageAlt |
| mend_hq | should-mental-health-be-taught-in-schools | 40377 | should mental health be taught in schools | 86 | 86 | contentHasAssets, keywordInImageAlt |
| mend_hq | why-mental-health-is-important-in-everyday-life | 40378 | why mental health is important | 86 | 86 | contentHasAssets, keywordInImageAlt |
| mend_hq | is-mental-health-an-illness | no post | is mental health an illness | not read | 86 | - |
| mend_hq | is-mental-health-getting-worse | no post | is mental health getting worse | not read | 86 | - |
| mend_hq | mental-health-and-mental-wellbeing | no post | mental health and mental wellbeing | not read | 86 | - |
| mend_hq | benefits-of-mindfulness | 39791 | benefits of mindfulness | 86 | 86 | keywordInImageAlt |
| mend_hq | best-cbt-books | 39359 | best cbt books | 85 | 86 | keywordInSubheadings |
| mend_hq | mindfulness-skills | 39809 | mindfulness skills | 86 | 86 | keywordInImageAlt |
| mend_ins | does-ai-actually-understand | 36516 | does ai actually understand us | 88 | 86 | none |
| mend_ins | K02__what-employees-want-from-their-managers | 35778 | what do employees want from their managers | 88 | 86 | none |
| mend_ins | AW04__what-does-leading-under-pressure-teach-you | 39661 | stay calm in an emergency | 82 | 86 | keywordInPermalink |
| mend_ins | cover-up-incompetence-with-head-knowledge | 36865 | skill vs knowledge | 84 | 86 | keywordInPermalink |
| mend_wb | 006-002__workbook__managing-expectations | 42727 | managing expectations workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-003__workbook__wise-mind | 42734 | wise mind workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-004__workbook__neissers-self-knowledge | 42741 | neissers self-knowledge workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-005__workbook__how-your-past-shapes-you | 42748 | how your past shapes you workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | 006-006__workbook__cognitive-flexibility | 42755 | cognitive flexibility workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-007__workbook__fixed-and-growth-mindset | 42762 | fixed and growth mindset workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-010__workbook__pause-before-you-react | 42769 | pause before you react workbook | 7 | 86 | contentHasShortParagraphs, keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-011__workbook__ellis-abc-model | 42776 | elliss abc model workbook | 5 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-012__workbook__inner-and-outer-authority | 42783 | inner and outer authority workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-013__workbook__self-reflection-questions | 42790 | self-reflection questions workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-014__workbook__current-self-and-ideal-self | 42797 | current self and ideal self workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-015__workbook__coveys-circle-of-control | 42804 | coveys circle of control workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-016__workbook__how-you-handle-problems | 42811 | how you handle problems workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-018__workbook__core-assumptions-of-cbt | 42818 | core assumptions of cbt workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-019__workbook__labels-and-identity | 42825 | labels and identity workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-021__workbook__public-and-private-self | 42832 | public and private self workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-022__workbook__where-beliefs-come-from | 42839 | where beliefs come from workbook | 64 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | 006-023__workbook__five-categories-of-belief | 42846 | five categories of belief workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-024__workbook__self-fulfilling-prophecy | 42853 | self-fulfilling prophecy workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-025__workbook__the-map-is-not-the-territory | 42860 | the map is not the territory workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-026__workbook__your-two-inner-voices | 42867 | your two inner voices workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-027__workbook__emotional-time-travel | 42874 | emotional time travel workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-030__workbook__socratic-questioning | 42881 | socratic questioning workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-031__workbook__feelings-faith-and-facts | 42888 | feelings, faith and facts workbook | 74 | 86 | keywordInContent, keywordInSubheadings, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | 006-032__workbook__honesty-with-yourself | 42895 | honesty with yourself workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-036__workbook__seven-levels-of-awareness | 42904 | seven levels of awareness workbook | 64 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | 006-038__workbook__seven-choices-of-maturity | 42926 | seven choices of maturity workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-040__workbook__mungers-human-misjudgment | 42953 | mungers human misjudgment workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-041__workbook__short-and-long-term-goals | 42973 | short and long-term goals workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-042__workbook__positive-goal-setting | 42999 | positive goal setting workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-043__workbook__solution-focused-questions | 43024 | solution-focused questions workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-044__workbook__how-to-learn-anything | 43045 | how to learn anything workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | 006-046__workbook__turning-learning-into-action | 43073 | turning learning into action workbook | 13 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Blooms_Taxonomy_Workbook | 43735 | bloom's taxonomy workbook | 7 | 86 | contentHasShortParagraphs, keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Choice_Theory_Workbook | 43742 | choice theory workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Defence_Mechanisms_Workbook | 43749 | defence mechanisms workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Human_Givens_Emotional_Needs_Workbook | 43756 | human givens emotional needs workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Id_Ego_Superego_Workbook | 43763 | id ego superego workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Ikigai_Workbook | 43770 | ikigai workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Kohlbergs_Stages_of_Moral_Development_Workbook | 43777 | kohlberg's stages of moral development workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Maslows_Hierarchy_of_Needs_Workbook | 43784 | maslow's hierarchy of needs workbook | 58 | 86 | contentHasShortParagraphs, keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Perceptual_Positions_Workbook | 43791 | perceptual positions workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Rogers_Core_Conditions_Workbook | 43798 | rogers core conditions workbook | 59 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Stages_of_Human_Connection_Workbook | 43805 | stages of human connection workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__The_ABCDE_Model_Workbook | 43812 | abcde model workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__The_Human_Experiential_Model_Workbook | 43819 | thoughts feelings behaviour workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__The_Johari_Window_Workbook | 43826 | johari window workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__The_Ladder_of_Inference_Workbook | 40321 | ladder of inference workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__The_Pygmalion_Effect_Workbook | 43838 | pygmalion effect workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__The_Six_Domains_of_Self_Concept_Workbook | 43845 | six domains of self-concept workbook | 61 | 86 | keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals |
| mend_wb | DRAFT__Transference_and_Countertransference_Workbook | 43852 | transference and countertransference workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
| mend_wb | DRAFT__Who_Am_I_Workbook | 43859 | who am i workbook | 11 | 86 | keywordIn10Percent, keywordInContent, keywordInImageAlt, keywordInMetaDescription, keywordInSubheadings, keywordInTitle, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals, titleStartWithKeyword |
