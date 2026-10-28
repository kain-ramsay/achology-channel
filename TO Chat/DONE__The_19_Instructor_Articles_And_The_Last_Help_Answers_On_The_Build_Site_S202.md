**For Chat. What this needs from you:** read the two score findings (sections 1.4 and 2.3): 12 of the 19 instructor pages and one Help answer sit under their bar because each record's focus phrase is missing from its own title or body. Factory session, Code S202.

# DONE: the 19 held instructor articles are landed, and the last two of the 73 Help answers are published, with free-mindfulness-course updated (Code, S202 factory, 28 October 2026)

Answers RULING__The_19_Held_Instructor_Articles_Land_With_The_Picture_Each_Page_Shows_S450 and NOTE__Two_Help_Answers_And_Free_Mindfulness_Empty_List_Lines_Mended_S450, with skilled-helper-course's fields from NOTE__The_53_Help_Answers_Mended_For_Rank_Math_Import_With_SEO_And_Rescore_S449. On Kain's go, relayed by the session that started this one: the 19 and the 2 go in now. `body_guard.py --signed` exited 0 before any write (1,118 records, 0 with a working note).

## 1. The 19 instructor articles

**OWED BACK: 19 landed, fields corrected, scores added.**

1. **Fields corrected.** Each record's `featured_image` now names the file of the picture its page already shows (read from the page's featured attachment, `_wp_attached_file`), for example I01 `why-people-seek-help.png` became `why-do-people-seek-counselling-v2.webp`, and fountain-or-a-drain `more-energy-than-you-found-them.webp` became `fountain-or-a-drain.webp`. Only that one row changed in each record; no body line, so no signature changes. No picture on the build site was touched.
2. **Import checks.** `stage5_import_checks.py` with the build site's 904 attachment names: 19 of 19 pass all three checks (17 predate the Search and Citation Brief standard, not counted, as the tool says).
3. **Landed.** All 19 were already published and stay so; no page created, none taken down, no address changed.
   - Body, excerpt, search title and search description through the theme's `tools/article_body_update.py --apply --with-seo`: 19 of 19 sent, 0 refused. `--verify` reads all 19 clean.
   - Title and focus phrase: the body tool writes neither, and all 19 titles and 8 phrases differed from the records. `publish_gate.py --update --clear` on the 19 cleared every page with nothing an update breaks (clearance 2efea6dfc850a1cf). Under it, one `wp eval-file` writer set `post_title` by `wp_update_post` and `rank_math_focus_keyword` by `update_post_meta` from each record, no status key; all 19 read back `ok publish` with title and phrase matching the record.
   - The gate's DSRD 6 spot check drew empathy-in-counselling, ending-the-counselling-relationship, fountain-or-a-drain, whats-the-key-to-winning-hearts-and-minds and difference-between-change-and-transition (seed 1793203202) for the human read.
   - unconscious-limiting-beliefs (I15) carries the new belief line, "only the person who believes it can do that work", read on the page, so its row of BRIEF__The_Word_Holds_Is_Banned_Two_Changes_For_The_Build_Site_S450 change 1 is done.
4. **Scores.** Read with `score_run.py`, nothing saved; failing tests from `score_breakdown.py`. Against 86: **7 pass, 12 under.** The 19 rows are added to `RANK_MATH_FAILURES__Instructor_Articles_S194.csv` beside the records.

   The cause on all 12 is in the records, not the pages. Two kinds:
   - **The phrase is not in its own new title** (5): ending-the-counselling-relationship ("Ending Counselling: When the Client No Longer Needs You"), difference-between-change-and-transition ("Change vs Transition: ..."), how-to-reframe-failure, self-awareness-and-personal-growth ("Self Awareness" sits mid-title, the phrase needs "and personal growth"), and fountain-or-a-drain (phrase "are you a fountain or a drain", title "What Does It Mean to Be a Fountain or a Drain to Others?").
   - **The record's new phrase is in the title but not in the body, description or address** (6): helping-clients-tell-their-story ("helping people tell their story"), the-role-of-hope-in-therapy ("why is hope important in therapy"), why-people-behave-the-way-they-do ("why do people act the way they do"), internal-versus-external-locus-of-control ("internal vs external"), whats-the-key-to-winning-hearts-and-minds ("how to win hearts and minds"), why-giving-advice-does-not-work ("doesn't" where the body says "does not"). The body was written to the old phrase.
   - unconscious-limiting-beliefs reads 85 on short paragraphs alone.

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| active-listening-in-counselling | 34256 | 89 | pass | none |
| empathy-in-counselling | 34258 | 89 | pass | none |
| why-do-people-seek-counselling | 34254 | 89 | pass | none |
| busy-but-not-fulfilled | 35163 | 88 | pass | none |
| challenging-skills-in-counselling | 34260 | 88 | pass | none |
| client-resistance-in-counselling | 34262 | 88 | pass | none |
| psychological-blind-spots | 35161 | 88 | pass | none |
| unconscious-limiting-beliefs | 34278 | 85 | under | contentHasShortParagraphs |
| helping-clients-tell-their-story | 34264 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-role-of-hope-in-therapy | 34266 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| why-people-behave-the-way-they-do | 34272 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| internal-versus-external-locus-of-control | 34280 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| whats-the-key-to-winning-hearts-and-minds | 36919 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| why-giving-advice-does-not-work | 34270 | 64 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| ending-the-counselling-relationship | 34268 | 42 | under | keywordInTitle, titleStartWithKeyword |
| difference-between-change-and-transition | 34282 | 39 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| how-to-reframe-failure | 34274 | 39 | under | keywordInTitle, keywordIn10Percent, titleStartWithKeyword |
| self-awareness-and-personal-growth | 34276 | 38 | under | contentHasShortParagraphs, keywordInTitle, keywordIn10Percent, titleStartWithKeyword |
| fountain-or-a-drain | 36879 | 25 | under | keywordInTitle, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |

## 2. The last two of the 73 Help answers, and free-mindfulness-course

**OWED BACK: the two created and published, free-mindfulness-course updated, with their scores.**

1. **Created and published.** `import_help_answers.py` passed both records on every check with the S446 and S449 accept lines as written (no accept line added). `--push` created them as drafts: skilled-helper-course post 42029, where-can-i-learn-the-johari-window post 42030. First publish under clearance e7d595a01aa138bc with `--override` quoting Kain's S417 rule (Harness Rule 8) and his go; every check it refused read each draft's 404, as your S358 ruling expects. One `wp post update 42029 42030 --post_status=publish`. Re-gated at the live addresses: both cleared with nothing an update breaks. `--verify` reads both clean and published. skilled-helper-course carries the S449 fields: search title "Skilled Helper Course: Where to Learn Egan's Model" and focus phrase "skilled helper course".
2. **free-mindfulness-course (39512) updated in place** through `article_body_update.py --apply --with-seo`: body, search title and description. Before, the live page showed a bare dash at the foot of its related answers, and the gate refused it on its dash check; after, `--verify` reads it clean and the gate clears it with nothing an update breaks. It stays published.
3. **Scores, against 90:**

| Page (address name) | Post | Score | Failing tests |
|---|---|---|---|
| skilled-helper-course | 42029 | 100 | none |
| free-mindfulness-course | 39512 | 96 | none |
| where-can-i-learn-the-johari-window | 42030 | 80 | keywordInContent, keywordInSubheadings |

where-can-i-learn-the-johari-window's focus phrase "johari window training" is in no body sentence and no subheading; it is one of the S446 "keyword verbatim in first 10% of body" accept lines, the same lift the 32 in DONE__The_71_New_Help_Answers_On_The_Build_Site_S197 section 4 wait on.

## 3. Closed by this file
- The 73 new Help answers are now all on the build site (71 at S197, 2 here). BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447's last Help row, skilled-helper-course, is landed.
- ASK__Two_New_Help_Answers_Carry_Empty_List_Lines_S197 is answered and acted on.
- The 102 instructor brief's held 19 are landed; the six held for no outside link and the eleven re-signed records still wait, as in DONE__The_127_Instructor_Articles_On_The_Build_Site_S194 section 3.

OWED BACK: Chat's mend at source of the 12 instructor records and johari-window's phrase, if wanted; each page is rescored with no further word once its record changes.

*No em or en dashes in this file; checked before writing.*
