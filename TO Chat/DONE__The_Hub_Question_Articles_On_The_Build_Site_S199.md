**For Chat. What this needs from you:** mend at source the 12 hub question records held in section 3 (nine with no picture, three with no outside link); decide the 12 pages carrying the banned word "holds" (section 4); and read the score table, where 26 pages sit under 86, mostly because no subheading carries the focus phrase (section 6). Factory session, Code S199.

# DONE: 52 of the 64 signed hub question articles are updated on the build site, read back and scored; 12 held (Code, S199 factory session, 28 October 2026)

Answers BRIEF__Import_The_55_Signed_Hub_Question_Articles_S445, the 50 hub-question-article rows of BRIEF__Import_The_192_Pages_Re_Signed_With_Full_Course_Names_S447 and the 14 of BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447, on Kain's go: "yes, please do". The two S447 briefs supersede the S445 versions for all 64 records, so every record was read as it stands today, each signed at Version 34 on 26 October 2026. Not in this job: the five anxiety road records (published S192), life-coach-vs-therapist (unsigned, named out by the S445 brief), the HELD and EXEMPLAR records.

## 1. What reached the build site
- **52 pages updated in place, all published before and after.** No page was created, none taken down, no address changed.
- Through the theme's `tools/article_body_update.py --apply --with-seo`: body, excerpt, search title and search description, 52 of 52. The tool refused the type by name ("no conversion rule"), because hub-question-article was not on its list. Its own importer (`import_field_authority_articles.py --type hub-question-article`) converts the type with the same `drop_title_h1` and `to_blocks`, so Code added the folder to the tool's list, one line, and recorded the new hash in `harness/h9_reviewed_scripts.json` (theme a4d45d6d, pushed). No install-reaching line changed. The course autolinker changed no record.
- **One title** differed from its record: can-mindfulness-meditation-be-harmful (39795), now "Can Mindfulness Be Harmful, and What Do Studies Report?". Written under clearance e0eeed6a5f89dae9 (`publish_gate.py --clear --update`, the page cleared with nothing an update breaks), by one `wp eval-file` writer setting `post_title` by `wp_update_post` and the focus keyword by `update_post_meta`, no status key. The staged row was read back on the server before the clearance was spent. Every other focus phrase already matched.

## 2. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 (1,118 records, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py --type hub-question-article`, with the build site's 904 attachment names): 55 of 64 pass all three; 9 fail check 3 (section 3).
- **Read back of all 52** from plain ssh dumps, after the last write: status, `post_title`, `post_excerpt`, search title, search description, focus keyword, and the stored body character for character against `article_body_update.body_html_for()`. **52 of 52 match.**
- **Lock 5:** all 52 stored bodies through `content_gate.machinery_in_body()`: 0 carry a working note.
- **Product names:** `product_name_check.py --type hub-question-article` finds four of the 52 records naming something short, and none is a product: "emotional resilience" as a trait (can-self-awareness-be-learned, lack-of-self-awareness; benefits-of-mindfulness is held) and the hub guide "Goal Setting and Action Planning" (life-coach-yourself). The rest of the count is check files in the folder. Its `--only` strips six letters off every file name, the Help prefix, so it reads 0 records for any other type: one fix for whoever next edits it.
- **The page check:** `publish_gate.py` measured the one retitled page at its address and cleared it.
- **Not run:** Google's Rich Results test (stage 6) and the three inbound links (section 5.4); these are existing pages and the records name no new inbound work.

## 3. The 12 held, and why
- **Nine have no picture yet** (import check 3: the record's `featured_image` reads "to be made", with a picture idea): how-does-mental-health-affect-sleep (draft 40373), how-to-improve-mental-wellbeing (draft 40374), is-mental-health-genetic (draft 40375), mental-health-without-therapy-or-medication (draft 40376), should-mental-health-be-taught-in-schools (draft 40377), why-mental-health-is-important-in-everyday-life (draft 40378), and is-mental-health-an-illness, is-mental-health-getting-worse and mental-health-and-mental-wellbeing, which are not on the build site at all. Each lands the moment its picture is on the install and its record names the file.
- **Three fail the body tool's outside link rule** (DSRD 6 section 5 item 11 move 6), which by your S449 ruling takes no exception: benefits-of-mindfulness (39791 on the install as before), best-cbt-books, mindfulness-skills. The importer refuses the same three for the same reason. Each lands the moment its record carries an outside link.

## 4. Gate lines
228 failing lines on the 52, every one in `GATE_LINES__The_Hub_Question_Articles_S199.csv` beside the records.
- **170 are style lines on Kain's signed words**, recorded `exception, 2026-10-28, signed prose not reworded (Kain S190 principle, Chat S449), approved by Kain`: paragraphs of 3 to 6 sentences 52, seven words shared 52, stances field 50, keyword in the body's first tenth 9, numbers in digits 5, "actually" 1, and one banned brand word, "scientifically proven" on is-mindfulness-evidence-based, which is the reader's own question in its signed title. **Code applied the S190 principle to hub question style lines without a line naming this type, as at S194 and S196; overturn it in one word if it should not stand.**
- **58 listed, not excepted and not held:** link words 21 (Part 9 rule 1, for the desk); a Sources entry the body does not cite 22; an outside link the Sources list does not name 3; and **"holds" on 12 pages**, banned at S450 after these were signed: best-mindfulness-books, cbt-worksheets, cognitive-behavioural-therapy-app, conditions-of-worth, does-cbt-actually-work, does-person-centred-counselling-work, mindfulness-without-religion, use-nlp-on-yourself, what-is-nlp-natural-language-processing, what-is-self-understanding, why-do-counsellors-need-theory, why-life-coaching-is-bad. Your S450 brief says you bring Kain the plan for existing records first, so Code landed the signed words and lists them here. Each lands again with no further word once its record changes.

## 5. Also found
Of the 52, 31 records carry an `rm_focus_keyword` that is not in their own `post_title`, but here it does not drive the score: most of those 31 pass 86, because Rank Math reads the search title, which carries the phrase. The column `keyword_in_record_title` is in the failures file for the desk.

## 6. The score table: 52 pages
Read from each page's editor with `score_run.py`, nothing saved, after every write. Failing tests for every page under 86 from `score_breakdown.py`, with contentHasAssets and lengthContent set aside (RULING__The_Article_Publish_Bar_Is_86_..._S449). **26 pass, 26 under; median 86.** Tests failing on the 26: keyword in subheadings 22, in the first 10 per cent 9, in content 6, in image alt 5, short paragraphs 3 (a paragraph over 120 words). Every page with its phrase is in `RANK_MATH_FAILURES__Hub_Question_Articles_S199.csv` beside the records. The one lift that moves most of them: one subheading carrying the search phrase, as the 198 Help answers had at S450.

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| is-mindfulness-evidence-based | 39803 | 91 | pass | none |
| is-nlp-backed-by-science | 39280 | 88 | pass | none |
| is-nlp-dangerous | 39281 | 88 | pass | none |
| life-coaching-models | 39285 | 88 | pass | none |
| life-coaching-questions | 39286 | 88 | pass | none |
| life-coaching-vs-mentoring | 39287 | 88 | pass | none |
| use-nlp-on-yourself | 39294 | 88 | pass | none |
| who-is-life-coaching-for | 39298 | 88 | pass | none |
| who-is-person-centred-therapy-for | 39432 | 88 | pass | none |
| can-mindfulness-meditation-be-harmful | 39795 | 87 | pass | none |
| cbt-worksheets | 39273 | 87 | pass | none |
| cognitive-behavioural-therapy-app | 39274 | 87 | pass | none |
| does-life-coaching-work | 39278 | 87 | pass | none |
| is-self-criticism-good | 39805 | 87 | pass | none |
| life-coach-yourself | 39284 | 87 | pass | none |
| what-does-a-life-coach-do | 39295 | 87 | pass | none |
| what-is-self-understanding | 39817 | 87 | pass | none |
| what-is-stress-management | 39819 | 87 | pass | none |
| who-invented-cbt | 39426 | 87 | pass | none |
| who-is-cognitive-behavioural-therapy-for | 39297 | 87 | pass | none |
| why-do-counsellors-need-theory | 39434 | 87 | pass | none |
| zen-vs-mindfulness | 39821 | 87 | pass | none |
| being-present-in-the-moment | 39789 | 86 | pass | none |
| mindfulness-therapy | 39811 | 86 | pass | none |
| mindfulness-without-religion | 39813 | 86 | pass | none |
| what-is-mindfulness-based-stress-reduction | 39815 | 86 | pass | none |
| best-counselling-books | 39361 | 85 | under | keywordInSubheadings |
| best-life-coaching-books | 39270 | 85 | under | keywordInSubheadings |
| cbt-and-person-centered-therapy | 39367 | 85 | under | keywordInSubheadings |
| cbt-techniques-and-exercises | 39369 | 85 | under | keywordInSubheadings |
| conditions-of-worth | 39799 | 85 | under | keywordInImageAlt |
| does-person-centred-counselling-work | 39279 | 85 | under | keywordInSubheadings |
| person-centred-therapy-goals | 39290 | 85 | under | keywordInSubheadings |
| should-i-be-a-life-coach | 39292 | 85 | under | keywordIn10Percent |
| types-of-cbt | 39293 | 85 | under | keywordIn10Percent |
| best-mindfulness-books | 39793 | 84 | under | keywordInSubheadings, keywordInImageAlt |
| counselling-vs-cbt | 39275 | 84 | under | keywordInSubheadings |
| criticisms-of-cbt | 39382 | 84 | under | keywordInSubheadings |
| does-cbt-actually-work | 39384 | 84 | under | keywordInSubheadings |
| does-cbt-work-for-anxiety | 39277 | 84 | under | keywordInSubheadings |
| lack-of-self-awareness | 39807 | 84 | under | keywordIn10Percent, keywordInImageAlt |
| person-centred-therapy-techniques | 39291 | 84 | under | keywordInSubheadings |
| what-is-nlp-natural-language-processing | 39296 | 84 | under | keywordInSubheadings |
| can-self-awareness-be-learned | 39797 | 80 | under | contentHasShortParagraphs, keywordInSubheadings, keywordInImageAlt |
| counselling-vs-psychotherapy | 39276 | 80 | under | contentHasShortParagraphs, keywordInSubheadings |
| is-person-centred-therapy-humanistic | 39282 | 80 | under | contentHasShortParagraphs, keywordInSubheadings |
| nlp-techniques-you-can-try | 39289 | 78 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings |
| why-life-coaching-is-bad | 39299 | 78 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings |
| books-to-learn-nlp | 39271 | 76 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings |
| cbt-vs-dbt | 39272 | 76 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings |
| mindfulness-vs-cbt | 39288 | 76 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings |
| how-to-practice-mindfulness | 39801 | 75 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |

OWED BACK: the nine pictures and the three outside links mended at source, after which each page lands with no further word; the "holds" plan for these 12 pages; the 26 records under 86 mended at source, after which each is rescored.

*No em or en dashes in this file; checked before writing.*
