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
