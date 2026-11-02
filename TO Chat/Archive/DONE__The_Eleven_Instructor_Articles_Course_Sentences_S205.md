ARCHIVED, Chat S452 (2 November 2026): road step 18 read: every page this file names that is under its bar or held is listed with its cause and state in 99 Working Papers, planning, STEP18__Every_Landed_Page_Under_The_Bar_S452; the records needing mends go to a writing session and back to Code; the rest wait on signed briefs Code has not landed yet.

**For Chat. What this needs from you:** record mends for the 10 pages under 86 (section 3). Each cause is in its record: the focus phrase is missing from the first tenth, or a paragraph runs over 120 words, or the phrase sits in no subheading. Factory session, Code S205.

# DONE: the eleven instructor articles carry their warm course sentences and the 37 fact mends (Code, factory S205, a side session of S203, 1 November 2026)

Answers BRIEF__Import_The_Eleven_Instructor_Articles_Course_Sentences_S450, its added paragraph included (batch `fix_instructor_facts_s450`), on Kain's order of 1 November 2026. The current records were imported once, after both signatures. Route followed: TO Chat/DONE__The_19_Instructor_Articles_And_The_Last_Help_Answers_On_The_Build_Site_S202, body only.

## 1. The import checks

- **Fields complete and signed, body shape.** `stage5_import_checks.py` on the eleven: 11 of 11 pass checks 1 and 2. Check 3 (named files) was not run, because no picture changed. `body_guard.py --signed`: 1,118 records, 0 with a working note in the body.
- **Every link resolves.** All 14 site addresses are published pages on the build site (read from the server's own list). Of the 21 outside links, 14 answer below 400. The 7 that refuse a script are:
  - the two course checkouts on community.achology.com (Mental Health and Wellbeing Practitioner Diploma Course; Neuro-Linguistic Programming Master Practitioner Course). Both are the checkout addresses the theme's own course register names.
  - the two dds.ca.gov reports, the 1999 report the brief names and the 2002 final study beside it on the same page. dds.ca.gov refuses scripts, as the brief says.
  - three publisher pages whose DOIs doi.org confirms as registered: 10.1073/pnas.2018340118, 10.1126/science.1207745, 10.1080/1047840X.2016.1082418.
  Nothing held.
- **The signatures read as the brief quotes.** For example is-my-grief-normal carries "Kain Ramsay; 28 October 2026; yes (the 37 fact mends ...)", and a separate Chat batch this afternoon (Session 451) touched none of the eleven records, as `git status` shows.

## 2. Landed

- The theme's `tools/article_body_update.py instructor-article:<slug> --apply`: 11 of 11 bodies sent, 0 refused. All 11 stay published. No title, address, search field or excerpt was sent, since the brief says none changed. No course link was written by the tool, because each course is already linked once.
- **Read back** with `--verify` (publish_gate.rendered_faults): 11 of 11 clean.
- **On the page, read from the server:** ai-give-you-a-second-opinion (36512) now links "Neuro-Linguistic Programming Master Practitioner Course" to its checkout, as the brief says the two AI articles do.
- No record was changed by the run.

## 3. Scores (bar 86), read by `score_run.py`; failing tests by the per-test reader; nothing saved

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| ai-give-you-a-second-opinion | 36512 | 86 | pass | contentHasShortParagraphs |
| a-diagnosis-actually-describing | 36603 | 85 | **under** | keywordIn10Percent, keywordInImageAlt, contentHasAssets |
| is-my-grief-normal | 36631 | 85 | **under** | keywordIn10Percent |
| the-definition-of-mental-disorder | 36639 | 85 | **under** | keywordInSubheadings |
| a-false-epidemic-happen-without-anyone-lying | 36605 | 81 | **under** | contentHasShortParagraphs, keywordIn10Percent |
| ai-making-us-worse-thinkers | 36514 | 81 | **under** | contentHasShortParagraphs, keywordIn10Percent |
| five-symptoms-mean-depression | 36625 | 81 | **under** | keywordIn10Percent, keywordInSubheadings |
| self-report-decide-a-diagnosis | 36637 | 81 | **under** | contentHasShortParagraphs, keywordIn10Percent |
| the-rise-in-autism-diagnoses-real | 36645 | 81 | **under** | contentHasShortParagraphs, keywordInSubheadings |
| what-is-concept-creep | 36647 | 81 | **under** | contentHasShortParagraphs, keywordIn10Percent |
| hypomania-from-an-ordinary-mood-swing | 36629 | 79 | **under** | contentHasShortParagraphs, keywordIn10Percent |

**1 passes, 10 under.** The causes, measured in the records:
- **A paragraph over 120 words, 7 pages:** exactly the 7 records whose longest body paragraph is over 120 words (hypomania-from-an-ordinary-mood-swing has three, the longest 142). The four that pass this test have none over 120.
- **The focus phrase is not in the first tenth, 8 pages** (keywordIn10Percent). On is-my-grief-normal, for example, the phrase "is my grief normal" is in the title and not in the opening.
- **The phrase in no subheading, 3 pages.** Separately, a-diagnosis-actually-describing has no picture whose alt text carries the phrase.

## Commits

Project: none, because no tool or record changed. Channel: this DONE and the brief's disposition line.

OWED BACK: the record mends for the 10 under 86; Code updates and rescores them on the mend.

*No em or en dashes in this file; checked before writing.*
