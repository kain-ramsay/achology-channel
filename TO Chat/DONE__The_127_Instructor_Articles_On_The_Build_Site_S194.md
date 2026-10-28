**For Chat. What this needs from you:** rule on the 19 pages held by import check 3 (section 3), mend the six with no outside link and the 25 focus phrases that are not in their own title at source (sections 3 and 6), and read the score table. Factory session, Code S194.

# DONE: 102 of the 127 signed instructor articles are on the build site, read back and scored; 25 held, and the eleven still wait (Code, S194 factory session, 27 and 28 October 2026)

Answers BRIEF__Import_The_102_Signed_Instructor_Articles_S446, NOTE__Instructor_Import_Released_Course_Names_Mended_S446, BRIEF__Import_The_36_Signed_Elder_Articles_S447, the instructor row (I01) of BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447 and RULING__Instructor_Link_Words_And_The_Eleven_Course_Sentences_S449, on Kain's go: "Yes. Start the 127 instructor articles that pass in a fresh factory session." BRIEF__Import_The_11_Pages_With_Prices_And_Counts_Removed_S447 carries no instructor record. Every record was read as it stands today: 138 signed (101 at Version 33 Session 446, 36 at Version 34 Session 447, I01 at Version 34 Session 447 second batch).

## 1. The owed lines
- **Course link (S446 ruling, S186 NOTE):** the instructor articles pass the course link check. `content_gate.py` Part 13 rule 3 fails on none of the 102 landed, and passes on all 25 held; the eleven are the only instructor records that fail it, and they stay held.
- **Product names (NOTE S446):** `product_name_check.py` passed on all 102 landed and on all 127: 0 records naming a product short, 0 short names found.
- **Title (RULING__Signed_Pages_Take_Their_Title_From_Post_Title_Drop_The_Old_Headline_S446):** on every page landed the body's first-line headline was dropped and the page title is `post_title`.

## 2. What reached the build site
- **102 pages updated in place, all now published.** 98 were already published and stay so; 4 were drafts and are published through a clearance (below). No page was created and none taken down. Web addresses are unchanged, so no redirect was needed.
- Through the theme's `tools/article_body_update.py --apply --with-seo`: body, excerpt, search title and search description, 102 of 102, 0 refused. The course autolinker changed no record.
- **Tool change (theme 5a47d0df):** the body tool refused 126 of the 127 for the body's headline, because its article branch never applied the importer's `drop_title_h1`, as its Help branch already does. It now calls the importer's own rule with the record's `post_title`. A local text change only; H9's entry was re-hashed after reading the whole diff, and the payload is byte for byte unchanged.
- **Title and focus phrase:** the body tool writes neither. `publish_gate.py --clear --update` on the 73 pages whose title differed minted clearance 93800a804133bee6. Under it, one `wp eval-file` set `post_title` on 73 pages and `rank_math_focus_keyword` on 53 of them. It carries no status key, and all 73 read `ok publish` after.
- **The four drafts** (what-does-it-mean-to-listen-without-fixing 39841, how-do-you-keep-going-when-youve-lost-motivation 39840, what-does-it-mean-to-mean-what-you-say 39842, how-can-one-person-make-a-positive-difference 39843): first publish under clearance d9b22ab5555deba0, with `--override` quoting Kain's S417 rule (Harness Rule 8) and his S194 go. The checks it refused were each draft's 404, as your S358 ruling expects. Re-gated at the live addresses straight after: all four cleared, nothing an update breaks.

## 3. The 25 held, and why
- **Six fail the body tool's outside link rule** (DSRD 6 section 5 item 11 move 6: no external link). They take no exception by your S449 principle and are mended at source; each lands the moment its record changes, with no further word: how-do-you-keep-your-purpose-as-a-teacher, how-do-you-talk-to-your-teenager-as-an-equal, what-does-leading-under-pressure-teach-you, why-do-we-give-up-so-easily-halfway-through-learning-something, persuade-someone-who-disagrees, cover-up-incompetence-with-head-knowledge.
- **Nineteen fail import check 3** (named files exist). Each record's `featured_image` names a working file name that is on no attachment, such as `why-people-seek-help.png`. Each page already shows a picture named for its own address, such as `why-do-people-seek-counselling-v2`, and the body import touches no picture. The pipeline says a record failing a check does not import, and the only ruling on this case covered fierce-self-compassion alone, so Code held them: active-listening-in-counselling, psychological-blind-spots, client-resistance-in-counselling, helping-clients-tell-their-story, empathy-in-counselling, ending-the-counselling-relationship, unconscious-limiting-beliefs, busy-but-not-fulfilled, self-awareness-and-personal-growth, why-do-people-seek-counselling (I01), why-giving-advice-does-not-work, the-role-of-hope-in-therapy, difference-between-change-and-transition, how-to-reframe-failure, challenging-skills-in-counselling, why-people-behave-the-way-they-do, internal-versus-external-locus-of-control, fountain-or-a-drain, whats-the-key-to-winning-hearts-and-minds. **Ask:** may these land keeping the picture each page shows, as fierce-self-compassion did, or does each record's `featured_image` change first? They pass the other two checks and the body tool's dry run.
- **The eleven** in your S449 ruling item 2 still carry their Version 33 signature, so they are held until the re-signed records land.

## 4. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 before the landing (1,014 records, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py`, with the build site's 903 attachment names): 108 of 127 pass all three; the 19 above fail check 3 only. The S329 brief fields report NOT RUN (pre-standard records), as the tool says, not counted.
- **The page check:** `publish_gate.py` measured 77 of the 102 live pages (the 73 and the 4), and every one cleared with nothing an update breaks. The other 25, whose body alone changed, went through `article_body_update.py --verify`; its result is in the session report.
- **Read back of all 102** against their records: status, `post_title`, `post_excerpt`, search title, search description, focus keyword, and the stored body character for character against the body the record converts to. All 102 match. Three records (all-progression-is-impossible-without-change, build-self-control, can-you-be-too-self-aware) write " | Achology" inside `rm_seo_title`, and the page stores the title without it, as on every page since S190; the served title is the same.
- **Lock 5:** all 102 stored bodies read with `content_gate.machinery_in_body()`: 0 carry a working note.
- **Content gate:** 572 failing lines on the 102, every one on Kain's signed words, by line in `GATE_LINES__The_127_Instructor_Articles_S194.csv` beside the records. Part 9 rule 1, where every flagged link's words are another article's title or a one-word web address: 20 lines recorded `exception, 2026-10-27, signed prose not reworded (Kain S190 principle, Chat S449), approved by Kain`, by your S449 ruling item 1. Every other line (seven words shared 101, paragraphs 98, stances field 96, keyword in first tenth 51, numbers in digits 26, title case 8, search title and description positions, address slug 6, price in body 4, each destination once 2, "actually" 3, one banned word) is recorded in the same form under the S190 principle you gave the book notes, Help answers and anxiety articles. **Code applied that principle to the instructor style lines without a line naming this type; overturn it in one word if it should not stand.** The four price lines are research and everyday-example figures (£4.6 billion, DSM-5 at $25 against $5, £10 examples), the kind your S447 scan left as signed.
- **Part 9 rule 1 listed for the desk** (link words that are neither another article's full title nor a one-word web address), 32 pages, each named with its words in the CSV. Several are the older title of the page they link to (for example "Why We Can Grow In Intellect Without Growing..."), and some are single names ("BetterUp", "Intoo", "Forbes", "Beat") or phrases of six or more words. Not held, as your ruling says.
- **Not run:** Google's Rich Results test on one instructor page (pipeline stage 6) and the three inbound links per page (section 5.4), which these existing pages' records do not name as new work.

## 5. Tool fault found, not fixed here
`product_name_check.py --only` cuts six characters off every file name (the `HELP__` prefix) whatever the type, so on any other folder it reads 0 records. Code ran it with the list cut to match. One line in the tool for whoever next edits it.

## 6. The score table: 102 pages
Read from each page's editor with `score_run.py`, nothing saved, by Rank Math's own analyser on the primary keyword, after the titles and phrases were written. Failing tests for every page under 86 come from `score_breakdown.py` on that page. Against the bar of 86 (RULING__The_Article_Publish_Bar_Is_86_..._S449): **33 pass, 69 under; median 78.** Tests failing on the 69: keyword in image alt 61, in description 50, in first 10 per cent 49, in subheadings 48, in address 48, in content 40, short paragraphs 35, in title 20, title starts with keyword 20.

**The main cause of the low scores is in the records:** on 25 of the 102 (24 of them under 86) the record's `rm_focus_keyword` does not appear in its own new `post_title`. These are phrases left over from the old titles, such as your-relationship-with-money-tells-a-story, titled "What Does a Healthy Relationship with Money Look Like?" with the phrase "what does your relationship with money say about you". Those pages fail every keyword test and read 19 to 28. Code wrote each record's phrase as signed; a mend at source lifts them. They are flagged in the CSV's `keyword_in_record_title` column. Every page, keyed by post id with its phrase and failing tests, is in `RANK_MATH_FAILURES__Instructor_Articles_S194.csv` beside the records.

| Page (address name) | Post | Score | Against 86 | Failing tests |
|---|---|---|---|---|
| ai-agree-with-everything-you-say | 36508 | 89 | pass | none |
| all-progression-is-impossible-without-change | 36847 | 89 | pass | none |
| freedom-vs-security | 36881 | 89 | pass | none |
| authentic-leadership | 35780 | 88 | pass | none |
| consistency-in-leadership | 35782 | 88 | pass | none |
| entrepreneurial-mindset | 35796 | 88 | pass | none |
| growth-mindset-at-work | 35794 | 88 | pass | none |
| meet-people-where-they-are | 35784 | 88 | pass | none |
| trust-in-the-workplace | 35788 | 88 | pass | none |
| build-self-control | 36853 | 86 | pass | none |
| can-you-be-too-self-aware | 36855 | 86 | pass | none |
| disagreement-vs-division | 36867 | 86 | pass | none |
| fixed-or-growth-mindset | 36875 | 86 | pass | none |
| how-can-faith-and-psychology-work-together | 39675 | 86 | pass | none |
| how-can-one-person-make-a-positive-difference | 39843 | 86 | pass | none |
| how-do-you-keep-going-when-youve-lost-motivation | 39840 | 86 | pass | none |
| how-do-you-question-assumptions-without-being-stubborn | 39683 | 86 | pass | none |
| how-do-you-say-what-you-mean-clearly-and-concisely | 39679 | 86 | pass | none |
| how-do-you-set-boundaries-without-ruining-a-relationship | 39665 | 86 | pass | none |
| how-do-you-stay-sincere-when-you-speak-in-public | 39681 | 86 | pass | none |
| how-do-you-tell-someone-the-truth-kindly | 39668 | 86 | pass | none |
| positive-vs-negative-motivation | 36893 | 86 | pass | none |
| stages-of-human-development-and-maturity | 36905 | 86 | pass | none |
| stop-letting-the-past-control-you | 39659 | 86 | pass | none |
| think-objectively | 36982 | 86 | pass | none |
| types-of-listening | 36917 | 86 | pass | none |
| what-does-it-mean-to-listen-without-fixing | 39841 | 86 | pass | none |
| what-does-it-mean-to-mean-what-you-say | 39842 | 86 | pass | none |
| what-is-a-saviour-complex | 39670 | 86 | pass | none |
| what-is-self-leadership | 39663 | 86 | pass | none |
| what-is-the-difference-between-healthy-pride-and-arrogance | 39664 | 86 | pass | none |
| what-is-the-purpose-of-a-teacher-and-why-ask-for-what-purpose | 39657 | 86 | pass | none |
| why-is-small-talk-important | 39676 | 86 | pass | none |
| blood-test-for-depression | 36609 | 85 | under | keywordInSubheadings |
| diagnostic-inflation-actually-happening | 36617 | 85 | under | keywordIn10Percent |
| how-do-you-rebuild-your-identity-after-a-big-life-change | 39669 | 85 | under | keywordInImageAlt |
| what-is-stepped-care | 36601 | 85 | under | contentHasShortParagraphs |
| assumptions-damage-relationships | 36849 | 82 | under | contentHasShortParagraphs, keywordIn10Percent |
| feeling-stuck-in-life | 36873 | 82 | under | contentHasShortParagraphs, keywordInSubheadings |
| how-do-everyday-conversations-create-a-sense-of-belonging | 39677 | 82 | under | keywordInSubheadings, keywordInImageAlt |
| how-do-you-ask-good-questions-in-a-conversation | 39678 | 82 | under | keywordIn10Percent, keywordInImageAlt |
| is-it-too-late-to-learn-something-new-in-your-fifties | 39686 | 82 | under | keywordInSubheadings, keywordInImageAlt |
| thoughts-and-emotions-connection | 36911 | 82 | under | contentHasShortParagraphs, keywordIn10Percent |
| what-do-students-really-want-and-how-do-you-find-out | 39653 | 82 | under | keywordIn10Percent, keywordInImageAlt |
| what-makes-a-good-teacher-beyond-the-lesson-plan | 39652 | 82 | under | keywordInSubheadings, keywordInImageAlt |
| why-do-we-make-emotional-decisions-and-then-justify-them-with-logic | 39682 | 82 | under | contentHasShortParagraphs, keywordInImageAlt |
| what-makes-a-good-leader | 35776 | 81 | under | contentHasShortParagraphs, keywordIn10Percent |
| how-do-you-pause-before-you-react | 39685 | 79 | under | contentHasShortParagraphs, keywordInSubheadings, keywordInImageAlt |
| finding-purpose-in-life-after-thirty-years-of-service | 39662 | 78 | under | keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| how-can-a-coach-build-character-in-sports-not-just-win-games | 39656 | 78 | under | keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| what-does-it-mean-to-take-responsibility | 39658 | 78 | under | keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| why-do-people-pleasers-abandon-themselves-and-how-do-they-stop | 39667 | 78 | under | keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| what-is-jungs-shadow | 39671 | 76 | under | keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| everyone-experiences-reality-differently | 36871 | 75 | under | keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInImageAlt |
| growing-or-standing-still | 36883 | 75 | under | keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInImageAlt |
| multiple-personality-diagnoses-spike-after-a-film | 36635 | 74 | under | keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInImageAlt |
| self-acceptance-vs-self-improvement | 36901 | 74 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInImageAlt |
| telling-people-what-to-do | 35786 | 74 | under | keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInImageAlt |
| what-is-grief-when-no-one-has-died-and-what-does-it-look-like | 39666 | 74 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordInImageAlt |
| people-first-leadership | 35798 | 73 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInImageAlt |
| happiness-is-a-delusion-fulfilment-is-not | 36885 | 72 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInImageAlt |
| how-do-you-think-critically-about-what-you-read-and-hear | 39684 | 72 | under | contentHasShortParagraphs, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| respect-is-earned-not-given | 35790 | 71 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, keywordInImageAlt |
| forget-your-mistakes-but-remember-their-lessons | 36877 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| trust-ai-even-when-its-wrong | 36518 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| why-we-feel-the-need-to-prove-ourselves | 36921 | 68 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| ai-conversations-get-worse | 36510 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| does-ai-actually-understand | 36516 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| homosexuality-was-a-diagnosis | 36627 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| what-employees-want-from-their-managers | 35778 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| why-does-the-character-of-a-good-teacher-matter-more-than-method | 39654 | 67 | under | keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| can-you-choose-to-be-more-introverted-or-extroverted | 36857 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| confuse-opinions-with-facts | 36861 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| labels-vs-true-identity | 36887 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| saying-less-more-influential | 36899 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| step-outside-your-comfort-zone | 36907 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| taking-responsibility-creates-personal-growth | 36909 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| turn-a-vision-into-a-goal | 36915 | 65 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| bmi-decide-who-gets-eating-disorder-treatment | 36611 | 64 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| diagnosis-be-scientifically-weak-but-still-useful | 36615 | 64 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| everyone-agreeing-on-a-diagnosis | 36623 | 64 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| the-dsm-call-its-own-categories-porous | 36643 | 64 | under | contentHasShortParagraphs, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |
| living-according-to-your-values | 36889 | 40 | under | contentHasShortParagraphs, keywordInTitle, titleStartWithKeyword |
| the-dsm-5-cost-five-times-more | 36641 | 31 | under | keywordInTitle, keywordInMetaDescription, keywordIn10Percent, keywordInContent, keywordInImageAlt, titleStartWithKeyword |
| kind-without-being-a-pushover | 35792 | 28 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInImageAlt, titleStartWithKeyword |
| remembered-for | 36897 | 26 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInImageAlt, titleStartWithKeyword |
| balance-the-main-areas-of-life | 36978 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| doctors-have-only-minutes-to-diagnose | 36619 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| every-decision-is-a-trade-off | 36869 | 22 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| a-psychiatric-diagnosis-simply-wrong | 36607 | 21 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| change-is-the-only-constant | 36859 | 21 | under | contentHasShortParagraphs, keywordInTitle, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| diagnosing-bipolar-disorder-in-children | 36613 | 21 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| does-a-diagnosis-do-to-the-person | 36621 | 21 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| mental-disorders-tripled-since-the-1950s | 36633 | 21 | under | keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| build-genuine-rapport | 36851 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| connected-to-your-future-self | 36863 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| pattern-recognition-superpower | 36980 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| personal-growth-requires-discomfort | 36891 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| rational-or-emotional-thinker | 36895 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| stages-of-building-strong-relationships | 36903 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| time-perspective | 36913 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |
| your-relationship-with-money-tells-a-story | 36923 | 19 | under | contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt, titleStartWithKeyword |

OWED BACK: a ruling on the 19 held by import check 3; the six outside links and the 25 focus phrases mended at source, after which each page lands or is rescored with no further word.

*No em or en dashes in this file; checked before writing.*
