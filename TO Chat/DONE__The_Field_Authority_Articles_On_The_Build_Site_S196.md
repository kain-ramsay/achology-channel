**For Chat. What this needs from you:** mend at source the four pages with no outside link and the EXEMPLAR record's missing sourcing section (section 3); mend the 27 focus phrases that are not in their own title (section 6); and read the score table. One fact for a theme session is on the theme queue (section 2). Factory session, Code S196.

# DONE: 112 of the 117 signed field authority articles are on the build site, read back and scored; 5 held, and 10 keep their old title until four old redirects go (Code, S196 factory session, 28 October 2026)

Answers BRIEF__Import_The_105_Signed_Field_Authority_Articles_S445, the field-authority rows of BRIEF__Import_The_192_Pages_Re_Signed_With_Full_Course_Names_S447 (91 records) and BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447 (10 records), and the one field authority record of BRIEF__Import_The_11_Pages_With_Prices_And_Counts_Removed_S447 (character-traits-of-a-life-coach), on Kain's go: "Yes. Start the field authority articles in a fresh factory session." Every record was read as it stands today: 117 signed (15 at Version 33 Session 445, 101 at Version 34 Session 447, 1 at Version 34 27 October). The SUPERSEDED record is not imported, as the S445 brief says. This session first claimed S195; the resisting change quote session had already filed under that number, so this report moved to S196. The S196 book notes session also filed under S196 (TO Chat/DONE__54_Book_Notes_Updated_Mended_And_Rescored_S196).

## 1. What reached the build site
- **112 pages updated in place, all now published.** 108 were already published and stay so; 4 were drafts and are published through a clearance (section 2). No page was created and none taken down. Addresses are unchanged.
- Through the theme's `tools/article_body_update.py --apply --with-seo` (its article branch unchanged since 5a47d0df; 860046b5 touched Help answers only, read in full): body, excerpt, search title and search description, 112 of 112, 0 refused. The course autolinker changed no record.
- **Title and focus phrase,** through `publish_gate.py --clear --update` and one `wp eval-file` writer per clearance (`post_title` by `wp_update_post`, `rank_math_focus_keyword` by `update_post_meta`, no status key; every row read `ok publish` after): 98 pages. The gate's reads over SSH dropped on a few pages per run while other sessions shared the line, and a clearance is all or nothing, so the 92 went in chunks of 10 to 16, each re-measured whole and spent at once: clearances b8d754f9146276a8 (2), b44c7c18ffd0c6ac (16), 033c3ed6e05f4414 (16), 9ad2cde11aba3151 (10), ab1b0e6ec7ac45b4 (10), 2fb6642b30ece333 (10), 20ee23fac9c150a9 (10), 9a860eb45d26c7bb (10), 9c425583dc915bdb (10). Every page in every chunk cleared with nothing an update breaks.

## 2. The four drafts, and the ten that keep their old title
- **First publish** of neuro-linguistic-programming-myths 35538, the-importance-of-self-awareness 35436, unraveling-behaviorism-psychology-a-historical-perspective 35312 and what-is-counselling 35320, with their record titles and phrases, under clearance 5771d44f64edc075, minted with `--override` quoting Kain's S417 rule (Harness Rule 8) and his go. The checks it refused were each draft's "page-loaded", as expected for a draft. Read back: all four `publish`.
- **But all four addresses still redirect.** `qbk_rank_math_redirections` rows 52 to 55 (made 19 October when the four were unpublished) send each address to its category list. RULING__The_28_Unpublished_Articles_Decided_And_The_S429_Tool_Changes_Kept_S432 tells Code to remove the redirect and republish; none of the 28 rows (28 to 55) has been removed, because `publish_gate.py` has no door that removes a redirect and H9 rightly refuses a writing `wp db query`. A reader still lands on the category list, as before this import; the re-gate at the live addresses could not read them for the same reason.
- **Ten other pages link to two of those four** (unraveling-behaviorism..., the-importance-of-self-awareness), so the gate refuses them on links-resolve (an address answering 301) and they keep their old title and phrase until the rows go: aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology, albert-banduras-social-learning-theory, conditioning-fear-insights-from-the-little-albert-experiment, exploration-of-the-cognitive-maps-experiment-by-edward-tolman, learn-about-the-psychologist-dr-albert-ellis, psychology-history-timeline, qualities-of-a-true-leader, twenty-pivotal-moments-in-psychologys-history, understanding-your-core-values, what-habits-are-and-why-people-get-stuck. Their bodies, excerpts and search fields are already the record's.
- **Filed:** one line in `000__THE_THEME_QUEUE.md` for the removal door. Once the four rows are gone, the ten land with one clearance and are rescored, with no further word.

## 3. The 5 held, and why
- **Four fail the body tool's outside link rule** (DSRD 6 section 5 item 11 move 6: no external link). By your S449 principle they take no exception and are mended at source; each lands the moment its record changes: helping-people-help-themselves (article 35518; its address is shared with quote 36238), karpman-drama-triangle, listening-to-understand-not-to-reply, the-foundational-principles-of-person-centred-counselling.
- **EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344 fails import check 2:** no `## Sourcing record` section and no `## Search and Citation Brief`. It is signed and named in the 192 brief, but the pipeline says a record failing a check does not import.

## 4. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 before the landing (1,014 records read, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py --type field-authority-article`, with the build site's 904 attachment names): 116 of 117 pass all three; the EXEMPLAR fails check 2. One record predates the Search and Citation Brief standard and is dated so, not counted.
- **Product names:** `product_name_check.py --type field-authority-article`: 0 records naming a product short. All 12 short names it finds sit in old LANE_C check files and one REPORT in the same folder, not in records.
- **The page check:** `publish_gate.py` measured all 98 retitled pages in the chunks above and every one cleared.
- **Read back of all 112** against their records: status, `post_title`, `post_excerpt`, search title, search description, focus keyword, and the stored body character for character against `article_body_update.body_html_for()`. 102 match in full. The other 10 are the ten of section 2, which differ only in title (and on six, focus phrase), as expected. 0 records write " | Achology" in `rm_seo_title`.
- **Lock 5:** all 112 stored bodies read with `content_gate.machinery_in_body()`: 0 carry a working note. Found in passing: instructor post 36510's body holds the word "placeholder" in ordinary prose, not a leak.
- **Content gate:** 767 failing lines on the 112, in `GATE_LINES__The_Field_Authority_Articles_S196.csv` beside the records. **532 are style lines on Kain's signed words** (seven words shared 111, stances field 110, paragraphs 95, keyword in the description's first 120 characters 37, in the body's first tenth 36, in the search title's first 50 characters 26, numbers in digits 35, keyword in address slug 33, "actually" 16, voice 10, destinations linked once 8, one keyword heading 7, title and excerpt banned words 3, "truly" 1, "steady" 1, link in paragraph 1, price in body 2, both prices research figures: a $925,000 settlement and $13.5 on the monster study), each recorded `exception, 2026-10-28, signed prose not reworded (Kain S190 principle, Chat S449), approved by Kain`. **Code applied the S190 principle to field authority style lines without a line naming this type, as at S194; overturn it in one word if it should not stand.**
- **235 lines listed, not excepted and not held,** because they judge a choice in the record rather than the prose: link words (103, Part 9 rule 1, for the desk as at S194); **content type is not retired (112):** the gate says field-authority-article was retired at S351, and your S445 brief commissions this import under that type; **course link (8):** six pages name no course at all (a-guide-to-breaking-bad-habits still carries PLACEHOLDER in `destination_course_name` and `destination_course_url`, fields no page shows; checked, nothing with PLACEHOLDER reaches any field authority page) and two name The School of Person-Centred Counselling and Psychology unlinked; **focus phrase claimed elsewhere in KEYWORD_REGISTER.csv (6):** personal-growth, multiple-intelligences-new-horizons, mans-search-for-meaning, social-psychology, humanistic-psychology, learn-life-coaching; **Sources entries not cited in the body (4) and outside links missing from Sources (2).** None is a wrong name, a wrong link or a broken link.
- **Not run:** Google's Rich Results test on one page (pipeline stage 6) and the three inbound links per page (section 5.4), which these existing pages' records do not name as new work.

## 5. Tool fault found again, not fixed here
`product_name_check.py --type` counts the LANE_C check files and REPORT files in a record folder as records (136 read, where the folder holds 117 records and 2 others). Harmless to this run; one filter for whoever next edits it.

## 6. The score table: 112 pages
Read from each page's editor with `score_run.py`, nothing saved, after the titles and phrases were written. Failing tests for every page under 86 from `score_breakdown.py` on that page, with contentHasAssets and lengthContent set aside by RULING__The_Article_Publish_Bar_Is_86_..._S449. The ten of section 2 were scored on their old title and are marked; their scores move when they land. **63 pass, 49 under; median 86.** Tests failing on the 49: keyword in first 10 per cent 36, in description 34, in image alt 34, in subheadings 33, in content 33, short paragraphs 31, in address 30, title starts with keyword 29, in title 28, no internal link 1 (the-importance-of-self-awareness).

**The main cause of the low scores is in the records, as with the instructor articles:** on 27 of the 112 the record's `rm_focus_keyword` is not in its own `post_title`, and 24 of those read 19 to 44. Many differ only in spelling or punctuation from the title's words ("person centred therapy books" against "Person-Centred Therapy Books", "freud defense mechanisms" against "Freud's Defence Mechanisms", "behaviorism" against "Behaviourism"); Rank Math matches the phrase exactly, so every keyword test fails. The 31 short-paragraph fails are paragraphs over 120 words, as your S450 book notes NOTE found. Code wrote each phrase as signed; a mend at source lifts them. Every page, keyed by post id with its phrase, a `keyword_in_record_title` column and its failing tests, is in `RANK_MATH_FAILURES__Field_Authority_Articles_S196.csv` beside the records.

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| 20-common-cognitive-biases-that-influence-your-decisions | 35182 | 91 | pass | none |
| learned-helplessness-experiment-the-psychology-of-helplessness | 35244 | 91 | pass | none |
| obedience-to-authority-stanley-milgram | 35258 | 91 | pass | none |
| perceptions-illusion-insights-from-the-halo-effect-experiment | 35260 | 91 | pass | none |
| social-conformity-insights-from-the-asch-conformity-experiment | 35274 | 91 | pass | none |
| the-complete-history-of-life-coaching-and-its-predecessors | 35278 | 91 | pass | none |
| 12-psychological-principles | 35178 | 89 | pass | none |
| an-antidote-to-narcissism | 35482 | 89 | pass | none |
| an-exploration-of-the-pygmalion-effect-experiment-on-expectations | 35192 | 89 | pass | none |
| benefits-of-practical-learning-why-experience-outweighs-academic-knowledge | 35196 | 89 | pass | none |
| compassions-test-insights-from-the-good-samaritan-experiment | 35426 | 89 | pass | none |
| connection-and-authenticity-in-life-coaching | 35493 | 89 | pass | none |
| exploration-of-the-split-brain-experiment-by-roger-sperry | 35222 | 89 | pass | none |
| exploring-self-determination-theory-key-principles-applications | 35224 | 89 | pass | none |
| fundamentals-of-social-psychology | 35515 | 89 | pass | none |
| gerard-egans-skilled-helper-model-using-the-3-stage-framework | 35230 | 89 | pass | none |
| how-irresponsibility-leads-to-personal-disempowerment | 35234 | 89 | pass | none |
| insights-from-mary-ainsworths-the-strange-situation-study | 35238 | 89 | pass | none |
| jean-piagets-contributions-to-developmental-psychology | 35240 | 89 | pass | none |
| learn-about-the-psychologist-dr-albert-ellis (old title) | 35242 | 89 | pass | none |
| life-coaching-listening-skills | 35529 | 89 | pass | none |
| maslows-hierarchy-of-needs | 35248 | 89 | pass | none |
| mastering-the-art-of-persuasion | 35250 | 89 | pass | none |
| navigating-life-with-a-sound-mind | 35256 | 89 | pass | none |
| qualities-of-a-true-leader (old title) | 35268 | 89 | pass | none |
| the-dynamics-of-cognitive-dissonance | 35282 | 89 | pass | none |
| the-origins-of-humanistic-psychology | 35438 | 89 | pass | none |
| the-origins-of-positive-psychology | 35294 | 89 | pass | none |
| the-power-of-useful-thinking | 35579 | 89 | pass | none |
| the-road-to-character-10-lessons-from-david-brooks-classic | 35296 | 89 | pass | none |
| unraveling-apathy-insights-from-the-bystander-effect-study | 35310 | 89 | pass | none |
| what-is-the-meaning-of-life-a-comprehensive-exploration | 35322 | 89 | pass | none |
| delayed-gratification-insights-from-the-marshmallow-test-study | 35428 | 87 | pass | none |
| exploration-of-the-cognitive-maps-experiment-by-edward-tolman (old title) | 35218 | 87 | pass | none |
| mimicking-aggression-insights-from-the-bobo-doll-experiment | 35252 | 87 | pass | none |
| misattribution-of-arousal-study-insights-into-emotional-perception | 35254 | 87 | pass | none |
| what-is-counselling | 35320 | 87 | pass | none |
| albert-banduras-social-learning-theory (old title) | 35188 | 86 | pass | none |
| balanced-lifestyle-seven-practical-steps-to-achieve-life-balance | 35194 | 86 | pass | none |
| character-traits-of-a-life-coach | 35490 | 86 | pass | none |
| depth-perception-insights-from-the-visual-cliff-experiment | 35206 | 86 | pass | none |
| essential-character-traits-for-personal-growth-and-development | 35210 | 86 | pass | none |
| ethically-questionable-insights-from-the-robbers-cave-experiment | 35212 | 86 | pass | none |
| examining-the-doll-test | 35214 | 86 | pass | none |
| exploration-of-the-false-memory-experiment-by-elizabeth-loftus | 35220 | 86 | pass | none |
| finding-purpose-how-human-values-shape-your-lifes-direction | 35228 | 86 | pass | none |
| outgrowing-your-limiting-beliefs | 35541 | 86 | pass | none |
| psychology-understanding-the-blue-eyes-brown-eyes-experiment | 35266 | 86 | pass | none |
| stereotyping-the-unseen-threat-to-diversity-and-inclusion | 35276 | 86 | pass | none |
| the-dark-side-of-human-behavior-the-impact-of-the-zimbardo-deindividuation-study | 35280 | 86 | pass | none |
| the-depths-of-empathy | 35562 | 86 | pass | none |
| the-impact-of-the-hawthorne-studies-on-workplace-dynamics | 35286 | 86 | pass | none |
| the-impact-of-the-invisible-gorilla-experiment-explained | 35288 | 86 | pass | none |
| the-lucifer-effect-10-lessons-from-philip-zimbardos-classic | 35292 | 86 | pass | none |
| the-origin-of-cognitive-therapy | 35574 | 86 | pass | none |
| the-origin-of-the-drama-triangle | 35576 | 86 | pass | none |
| the-role-of-freedom-in-personal-autonomy-and-decision-making | 35298 | 86 | pass | none |
| the-truth-about-active-listening | 35590 | 86 | pass | none |
| understanding-the-cognitive-load-theory-experiment | 35601 | 86 | pass | none |
| understanding-the-layers-of-identity | 35308 | 86 | pass | none |
| unlock-personal-empowerment-with-the-empowerment-dynamic | 35604 | 86 | pass | none |
| voices-of-vulnerability-insights-from-the-monster-study-experiment | 35316 | 86 | pass | none |
| what-is-counselling-psychology-a-search-for-a-definition | 35613 | 86 | pass | none |
| finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning | 35226 | 78 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInSubheadings, keywordInImageAlt |
| exploration-of-dr-howard-gardners-nine-types-of-intelligence | 35216 | 75 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInImageAlt |
| how-philosophy-illuminates-our-understanding-of-psychology | 35236 | 75 | under | keywordInMetaDescription, keywordInPermalink, keywordInImageAlt, titleStartWithKeyword |
| the-worlds-most-influential-psychologists | 35302 | 75 | under | contentHasShortParagraphs, keywordIn10Percent, keywordInContent, keywordInSubheadings |
| timeless-lessons-from-the-life-and-works-of-hans-j-eysenck | 35595 | 75 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| lessons-from-how-to-win-friends-influence-people | 35246 | 72 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInImageAlt |
| the-smart-goal-setting-framework | 35300 | 72 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInImageAlt |
| 10-ethically-dubious-experiments | 35176 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| dynamics-of-leading-effective-diplomatic-discussions | 35208 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| embracing-your-shadow-side | 35502 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| from-roots-to-revolution | 35430 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| history-and-timeline-of-counselling-psychology | 35232 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| how-immediacy-shapes-engaging-and-impactful-conversations | 35432 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-reality-of-life-coaching | 35583 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| embracing-your-innermost-values | 35500 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| psychology-theories-for-motivation | 35264 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| starvation-insights-from-ancel-keys-the-minnesota-experiment | 35553 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-core-competencies-of-coaching | 35559 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-eisenhower-decision-making-matrix | 35565 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-truth-about-eloquence | 35592 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| unlocking-life-coaching-excellence | 35606 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology (old title) | 35186 | 44 | under | keywordInTitle, titleStartWithKeyword |
| the-stages-of-change-model | 35588 | 44 | under | keywordInTitle, titleStartWithKeyword |
| unraveling-behaviorism-psychology-a-historical-perspective | 35312 | 44 | under | keywordInTitle, titleStartWithKeyword |
| conditioning-fear-insights-from-the-little-albert-experiment (old title) | 35202 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| decide-with-confidence-10-timeless-principles-for-wise-decision-making | 35204 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| psychology-history-timeline (old title) | 35262 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| the-4-stages-of-human-evolution | 35556 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| the-myth-of-having-it-all | 35572 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| a-guide-to-breaking-bad-habits | 35424 | 38 | under | contentHasShortParagraphs, keywordInTitle, keywordInSubheadings, titleStartWithKeyword |
| twenty-pivotal-moments-in-psychologys-history (old title) | 35306 | 36 | under | contentHasShortParagraphs, keywordInTitle, keywordIn10Percent, titleStartWithKeyword |
| understanding-your-core-values (old title) | 35440 | 36 | under | contentHasShortParagraphs, keywordInTitle, keywordInSubheadings, titleStartWithKeyword |
| carl-rogers-person-centered-counseling | 35200 | 32 | under | keywordInTitle, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInImageAlt, titleStartWithKeyword |
| the-psychology-of-self-improvement | 35581 | 29 | under | contentHasShortParagraphs, keywordInTitle, keywordIn10Percent, keywordInContent, keywordInSubheadings, titleStartWithKeyword |
| triggers-that-lead-to-relationship-breakdowns | 35304 | 29 | under | contentHasShortParagraphs, keywordInTitle, keywordIn10Percent, keywordInContent, keywordInSubheadings, titleStartWithKeyword |
| what-habits-are-and-why-people-get-stuck (old title) | 35318 | 29 | under | contentHasShortParagraphs, keywordInTitle, keywordIn10Percent, keywordInContent, keywordInSubheadings, titleStartWithKeyword |
| neuro-linguistic-programming-myths | 35538 | 25 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| the-importance-of-self-awareness | 35436 | 24 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInImageAlt, linksHasInternal, titleStartWithKeyword |
| 13-morally-dubious-psychology-experiments | 35180 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| a-guide-to-building-inner-resilience | 35479 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| rosalynn-carter-and-mental-health-stigma | 35548 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| books-about-person-centred-psychology | 35198 | 21 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| an-exploration-of-freuds-psychoanalytic-theory | 35190 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| dialogue-versus-monologue | 35497 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| sigmund-freuds-defence-mechanisms | 35270 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| skills-for-highly-effective-counseling | 35272 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| the-impact-of-transference-and-counter-transference | 35290 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| two-factor-models-of-personality | 35599 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| unveiling-attachment-insights-from-harlows-monkey-experiments | 35314 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |

OWED BACK: the four outside links, the EXEMPLAR's sourcing section and the 27 focus phrases mended at source, after which each page lands or is rescored with no further word; the redirect removal door from a theme session, after which the ten land and are rescored.

*No em or en dashes in this file; checked before writing.*
