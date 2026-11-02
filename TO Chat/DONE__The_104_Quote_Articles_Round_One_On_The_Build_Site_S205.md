**For Chat. What this needs from you:** two things. First, record mends for the 101 pages under 86 (section 4: three causes, all in the records). Second, the inbound link sentences placed on their linking pages, with the words each link sits on (section 3). Factory session, Code S205.

# DONE: the 104 signed quote articles of round one are on the build site (Code, factory S205, a side session of S203, 1 November 2026)

Answers BRIEF__Import_The_104_Signed_Quote_Articles_Round_One_S450, on Kain's order of 1 November 2026 ("Import last week's signed work from FROM Chat, in this order, one brief at a time"). Route followed: TO Chat/DONE__The_Eight_Resisting_Change_Quote_Pages_S195. The gates were the ones Factory A left at S204 (project commit 9714d68a, theme b2b9d65f).

## 1. The import checks, then the import

- **Check 2, body shape.** `body_guard.py --signed`: 1,118 records read, 0 with a working note in the body.
- **Check 1, fields complete and signed.** `import_quote_pages.py` plan on the 104, by quote_id from the eleven `quotes_r1_<group>` reading lists: 104 of 104 pass every check, including signed, quote_text equal to image_quote_text, the author picture and the course cover.
- **Check 3, every link resolves.** 68 site addresses: 66 are published pages on the build site (read from the server's own list of published addresses, not crawled). The other 2 are the two course pages, /academy/mental-health/mental-health-practitioner-diploma/ and /academy/neuro-linguistic-programming/diploma-modern-applied-psychology/. Both are on the theme's course register (courses-setup.php), and both answer 404 on the build site today, read from inside the host: course pages not built yet, so pages to come rather than broken links. 10 outside links: 7 answer 200 through doi.org. 3 DOIs land on publishers that refuse scripts (403 from Emerald, Sage and Sage). All 3 are registered, read from doi.org's own handle record (responseCode 1): 10.1108/EJTD-04-2015-0031, 10.1111/j.1529-1006.2004.00018.x, 10.1177/0146167203254602. Nothing held.
- **Pushed.** 83 posts updated in place, each matched by its quote_id and renamed to its new address. 21 created. The 83 kept their status (published). The importer sends no status.
- **The 21 were not on the build site.** All are course 001 quotes (CQ001-...). None of them had a post under its old address, its new address or its quote_id (read on the server), so "update in place" could not apply. They were created as drafts, as CQ001-043-1 was at S195.
- **Read back.** `import_quote_pages.py --verify`: 104 of 104 clean. Title, excerpt, category, tags, the quote fields, the plain meta and every Rank Math field match the record.

## 2. Published, share pictures and redirects

- **Share pictures for the 21 new pages,** baked at design cbbdd1cf055c with `make_quote_cards.py --attach`: 21 written, 0 refused, cache purged. The 83 existing pages already carry cards at that design.
- **The 21 published.** `publish_gate.py --clear` with `--override` quoting Kain's S417 ruling ("Signed pages are published on the build site"), his order of 1 November, and the records' signature. Clearance 02d85aefc80ea8a0. Every check it refused read each draft's 404, as at S195. Then one `wp post update ... --post_status=publish` on posts 42127 to 42147. The gate's spot check drew: are-core-values-the-same-as-morals, for-yourself-or-against-yourself, inner-conflict-and-self-understanding, is-there-a-value-behind-everything-you-do, why-is-self-acceptance-so-hard (seed 1793545493).
- **Re-gated live, all 104,** with `publish_gate.py --update --clear`: 46 clear with nothing an update breaks. **58 fail on one line only, "the rendered body carries no external link".** This is the known fault the brief names, the quote page's source link. Factory A fixed it in `content_gate.py` at S204 (a book note or course link in the Book now counts), but `publish_gate.py`'s rendered check (`rendered_faults`) still demands an outside link on every type. That is a gate fault for the next factory session that has the gates open. Nothing was held for it, since all 104 are live. No clearance was minted for the update, and none is needed: no status changed.
- **Redirects: 104 written and proved** by `publish_gate.py --write-redirect`, each old address answering 301 to its new one. 83 are the renamed posts' real old addresses. 21 are the course 001 records' `redirect_from` addresses, which had no page on the build site. They are set because the brief asks for a 301 from each old address, and they stand ready for the old site's addresses at cutover.

## 3. Inbound links: none added, one question for Chat

Each record's `inbound_from` names three linking pages and one sentence for each, in brackets. Code searched every record for the first one ("The quality of attention a listener brings decides what a person is willing to say next.", for CQ001-175-1 on life-coaching-listening-skills). It appears in no record except the quote record itself. So these are new sentences for pages Kain has already signed, with no place on the page and no link words named. Writing them in is drafting, and it changes signed words: the same stop as TO Chat/ASK__The_Resisting_Change_Inbound_Links_Need_Their_Sentences_S195. **What Code needs, for the 312 links (104 pages, three each):** for each linking page, the paragraph each sentence goes into (or the existing sentence it replaces), and the words that carry the link. Then Code writes them into the linking records, pushes with `article_body_update.py` and reads them back.

## 4. Rank Math scores (bar 86, RULING S449)

Read by `tools/score_run.py`, all settled, nothing saved. Failing tests read from each editor by the per-test reader (`score_tests.read_tests`, the same reader the S187 and S202 tables used), nothing saved.

**3 pass, 101 under.** Every cause is in the records, not the pages or the template:
- **No outside link, 94 pages** (linksHasExternals, 4 points, and linksNotAllExternals, 2 points). The quote standard now lets the source be a book note or a course link in the Book, so the gate passes these records. Rank Math still counts outside links only. The 10 pages that do carry an outside link are the ones with a credited study. So the standard and Rank Math disagree here, and that is yours to settle: an outside link at source, or the bar read without these 6 points for quote pages.
- **The focus phrase in no subheading, 92 pages** (keywordInSubheadings, 3 points).
- **A paragraph over 120 words, 32 pages** (contentHasShortParagraphs, 3 points). Measured in the records: exactly 32 records carry at least one body paragraph over 120 words, and they are the same 32 (CQ001-123-1's longest is 158).
- **The title does not open on the phrase, 7 pages** (titleStartWithKeyword).
- The ceiling everywhere is lengthContent and contentHasAssets earning short, which the bar of 86 leaves out of scope.

| Record | Post | Address | Focus phrase | Score | Against 86 | Failing tests |
|---|---|---|---|---|---|---|
| CQ001-054-1 | 42131 (new) | /learn/motivation/quotes/growing-beyond-the-limits-of-your-self-awareness/ | limits of your self-awareness | 88 | pass | none |
| CQ001-039-1 | 42128 (new) | /learn/mental-wellness/quotes/do-core-values-shape-every-decision/ | core values shape | 87 | pass | none |
| Q06987 | 36238 | /learn/helping-people/quotes/help-someone-better-themselves/ | help someone better themselves | 86 | pass | none |
| CQ001-044-1 | 42129 (new) | /learn/motivation/quotes/does-self-awareness-make-you-a-better-leader/ | self-awareness make you a better leader | 85 | **under** | contentHasShortParagraphs, keywordInSubheadings |
| CQ001-123-1 | 42141 (new) | /learn/mental-wellness/quotes/inner-conflict-and-self-understanding/ | inner conflict | 85 | **under** | contentHasShortParagraphs, keywordInSubheadings |
| CQ001-161-1 | 42145 (new) | /learn/mental-wellness/quotes/how-can-self-awareness-help-in-decision-making/ | how can self-awareness help in decision making | 85 | **under** | contentHasShortParagraphs, keywordInSubheadings |
| CQ018-041-2 | 36381 | /learn/mental-wellness/quotes/is-taking-responsibility-blaming-yourself/ | blaming yourself | 85 | **under** | linksHasExternals, linksNotAllExternals |
| Q06990 | 36241 | /learn/helping-people/quotes/can-you-help-someone-who-doesnt-want-to-be-helped/ | can you help someone who doesn't want to be helped | 85 | **under** | keywordInSubheadings |
| Q06997 | 36248 | /learn/helping-people/quotes/is-helping-others-a-job-or-a-calling/ | helping others a job | 85 | **under** | keywordInSubheadings |
| Q07032 | 36283 | /learn/helping-people/quotes/are-you-as-self-aware-as-you-think/ | as self-aware as you think | 85 | **under** | keywordInSubheadings |
| CQ018-040-2 | 36379 | /learn/mental-wellness/quotes/does-it-all-come-down-to-taking-responsibility/ | come down to taking responsibility | 84 | **under** | contentHasShortParagraphs, keywordInSubheadings |
| CQ018-073-1 | 36426 | /learn/mental-wellness/quotes/accepting-who-you-are-and-despair/ | accepting who you are | 84 | **under** | linksHasExternals, linksNotAllExternals |
| Q07040 | 38501 | /learn/helping-people/quotes/conversations-feel-like-two-monologues/ | conversations feel like two monologues | 82 | **under** | linksHasExternals, linksNotAllExternals |
| Q07054 | 38515 | /learn/helping-people/quotes/listen-without-trying-to-solve-the-problem/ | listen without trying to solve the problem | 82 | **under** | linksHasExternals, linksNotAllExternals |
| CQ001-057-1 | 42133 (new) | /learn/motivation/quotes/sense-of-self-decide-how-you-act/ | sense of self decide | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-175-1 | 42147 (new) | /learn/mental-wellness/quotes/why-people-tell-you-the-truth-once-they-trust-you/ | tell you the truth once they trust you | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-008-1 | 36323 | /learn/mental-wellness/quotes/not-making-a-decision-is-still-a-decision/ | not making a decision | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-011-2 | 36330 | /learn/mental-wellness/quotes/help-someone-understand-their-feelings/ | help someone understand their feelings | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-044-1 | 36385 | /learn/mental-wellness/quotes/how-does-self-acceptance-help-us-get-along-with-others/ | how does self-acceptance help | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-045-2 | 36388 | /learn/mental-wellness/quotes/where-a-false-sense-of-self-comes-from/ | false sense of self | 81 | **under** | contentHasShortParagraphs, linksHasExternals, linksNotAllExternals |
| CQ018-072-1 | 36424 | /learn/mental-wellness/quotes/human-beings-or-human-doings/ | human beings or human doings | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-073-3 | 36428 | /learn/mental-wellness/quotes/what-does-self-acceptance-look-like-with-flaws/ | what does self-acceptance look like | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-085-1 | 36448 | /learn/mental-wellness/quotes/every-decision-we-make-has-a-cost/ | every decision we make | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-089-2 | 36456 | /learn/mental-wellness/quotes/good-judgement-and-the-course-of-a-life/ | good judgement | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-102-1 | 36476 | /learn/mental-wellness/quotes/which-values-matter-most-to-you/ | values matter most to you | 81 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07008 | 36259 | /learn/helping-people/quotes/help-someone-emotionally/ | help someone emotionally | 81 | **under** | linksHasExternals, linksNotAllExternals |
| CQ001-068-1 | 42134 (new) | /learn/mental-wellness/quotes/why-is-a-sense-of-self-so-important/ | sense of self so important | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-100-1 | 42137 (new) | /learn/mental-wellness/quotes/being-yourself-and-doing-your-best-enough/ | being yourself and doing your best | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-108-1 | 42138 (new) | /learn/mental-wellness/quotes/for-yourself-or-against-yourself/ | for yourself or against yourself | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-141-1 | 42143 (new) | /learn/mental-wellness/quotes/are-core-values-the-same-as-morals/ | core values the same as morals | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-172-1 | 42146 (new) | /learn/motivation/quotes/is-everything-in-life-a-choice/ | is everything in life a choice | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-002-4 | 36312 | /learn/mental-wellness/quotes/one-decision-after-another/ | one decision after another | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-026-1 | 36360 | /learn/mental-wellness/quotes/do-we-always-have-a-choice-in-life/ | do we always have a choice in life | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-040-1 | 36378 | /learn/mental-wellness/quotes/what-does-taking-responsibility-look-like/ | what does taking responsibility look like | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-043-1 | 36384 | /learn/mental-wellness/quotes/do-our-choices-decide-our-future/ | choices decide our future | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-044-2 | 36386 | /learn/mental-wellness/quotes/should-self-acceptance-be-our-goal/ | self-acceptance be our goal | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-055-1 | 36402 | /learn/mental-wellness/quotes/do-we-have-a-choice-in-who-we-become/ | do we have a choice | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-055-2 | 36403 | /learn/mental-wellness/quotes/how-much-power-does-a-single-decision-have/ | power does a single decision | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-056-1 | 36404 | /learn/mental-wellness/quotes/where-does-self-responsibility-begin/ | self-responsibility | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-073-4 | 36429 | /learn/mental-wellness/quotes/can-self-acceptance-begin-with-a-decision/ | self-acceptance begin | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-078-2 | 36436 | /learn/mental-wellness/quotes/who-gets-to-decide-who-you-are/ | decide who you are | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-086-2 | 36450 | /learn/mental-wellness/quotes/honesty-from-someone-who-feels-unsafe/ | honesty from someone who feels unsafe | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-087-1 | 36451 | /learn/mental-wellness/quotes/why-is-trust-in-relationships-important/ | why is trust in relationships | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-097-1 | 36470 | /learn/mental-wellness/quotes/start-taking-responsibility-for-your-life/ | start taking responsibility for your life | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-099-1 | 36473 | /learn/mental-wellness/quotes/the-power-of-taking-responsibility/ | the power of taking responsibility | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-102-2 | 36477 | /learn/mental-wellness/quotes/sense-of-self-worth-tied-to-what-you-do/ | sense of self-worth | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-107-2 | 36485 | /learn/mental-wellness/quotes/how-to-make-wise-decisions-about-your-time/ | make wise decisions | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-111-1 | 36491 | /learn/mental-wellness/quotes/should-trust-be-earned-in-a-relationship/ | should trust be earned in a relationship | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-114-1 | 36494 | /learn/mental-wellness/quotes/lack-of-trust-in-relationships-and-power-struggles/ | lack of trust in relationships | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-118-1 | 36498 | /learn/mental-wellness/quotes/is-personal-freedom-a-choice/ | personal freedom a choice | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-127-1 | 36505 | /learn/mental-wellness/quotes/why-help-someone-in-need/ | why help someone in need | 80 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07023 | 36274 | /learn/helping-people/quotes/what-is-the-goal-of-life-coaching/ | what is the goal of life coaching | 79 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07027 | 36278 | /learn/helping-people/quotes/what-is-a-life-coach-supposed-to-do/ | what is a life coach supposed to do | 79 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07031 | 36282 | /learn/helping-people/quotes/what-can-life-coaching-help-with/ | what can life coaching help with | 79 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-017-1 | 42127 (new) | /learn/motivation/quotes/why-is-self-acceptance-so-hard/ | why is self-acceptance so hard | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-049-1 | 42130 (new) | /learn/mental-wellness/quotes/self-awareness-is-the-first-step-to-growth/ | self-awareness is the first step | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-080-1 | 42135 (new) | /learn/mental-wellness/quotes/taking-ownership-of-your-life/ | taking ownership | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| CQ001-082-1 | 42136 (new) | /learn/motivation/quotes/identity-the-same-as-your-personality/ | identity the same as your personality | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-113-1 | 42139 (new) | /learn/mental-wellness/quotes/responsibility-for-everything-that-happens/ | responsibility for everything | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-160-1 | 42144 (new) | /learn/mental-wellness/quotes/how-does-trust-affect-relationships/ | how does trust affect relationships | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-013-3 | 36335 | /learn/mental-wellness/quotes/active-listening-different-from-just-hearing/ | active listening different from just hearing | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-015-1 | 36338 | /learn/mental-wellness/quotes/how-does-self-awareness-help-us-grow/ | how does self-awareness help us | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-080-3 | 36440 | /learn/mental-wellness/quotes/radical-responsibility/ | radical responsibility | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-089-1 | 36455 | /learn/mental-wellness/quotes/what-role-does-trust-play-in-a-relationship/ | what role does trust play in a relationship | 78 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q06984 | 36235 | /learn/helping-people/quotes/how-should-i-help-someone/ | how should i help someone | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q06985 | 36236 | /learn/helping-people/quotes/help-someone-without-giving-advice/ | help someone without giving advice | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q06986 | 36237 | /learn/helping-people/quotes/help-someone-know-their-worth/ | help someone know their worth | 78 | **under** | contentHasShortParagraphs, linksHasExternals, linksNotAllExternals |
| Q06989 | 36240 | /learn/helping-people/quotes/help-someone-without-enabling-them/ | help someone without enabling them | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q06995 | 36246 | /learn/helping-people/quotes/living-by-made-up-rules/ | made-up rules | 78 | **under** | contentHasShortParagraphs, linksHasExternals, linksNotAllExternals |
| Q06996 | 36247 | /learn/helping-people/quotes/what-makes-a-good-helper/ | what makes a good helper | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q06998 | 36249 | /learn/helping-people/quotes/how-do-i-help-someone-feel-better/ | how do i help someone feel better | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07000 | 36251 | /learn/helping-people/quotes/where-does-a-lack-of-self-awareness-come-from/ | where does a lack of self-awareness come from | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07003 | 36254 | /learn/helping-people/quotes/is-listening-enough-without-showing-empathy/ | listening enough without showing empathy | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07010 | 36261 | /learn/helping-people/quotes/what-is-the-role-of-a-life-coach/ | what is the role of a life coach | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07011 | 36262 | /learn/helping-people/quotes/why-is-taking-responsibility-so-important/ | taking responsibility so important | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07013 | 36264 | /learn/helping-people/quotes/taking-responsibility-for-your-actions/ | taking responsibility for your actions | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07017 | 36268 | /learn/helping-people/quotes/how-to-develop-a-sense-of-self/ | develop a sense of self | 78 | **under** | contentHasShortParagraphs, linksHasExternals, linksNotAllExternals |
| Q07028 | 36279 | /learn/helping-people/quotes/is-life-coaching-just-a-set-of-techniques/ | life coaching just a set of techniques | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07030 | 36281 | /learn/helping-people/quotes/what-is-the-purpose-of-a-life-coach/ | what is the purpose of a life coach | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07039 | 38500 | /learn/helping-people/quotes/listen-to-respond-or-listen-to-understand/ | listen to respond | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07044 | 38505 | /learn/helping-people/quotes/benefits-of-taking-responsibility-for-yourself/ | benefits of taking responsibility | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07048 | 38509 | /learn/helping-people/quotes/what-is-a-life-coaching-session/ | what is a life coaching session | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07049 | 38510 | /learn/helping-people/quotes/is-life-coaching-worth-it/ | is life coaching worth it | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07050 | 38511 | /learn/helping-people/quotes/how-does-life-coaching-help/ | how does life coaching help | 78 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-055-1 | 42132 (new) | /learn/mental-wellness/quotes/why-does-self-awareness-matter-so-much/ | self-awareness matter so much | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-118-1 | 42140 (new) | /learn/mental-wellness/quotes/is-there-a-value-behind-everything-you-do/ | value behind everything you do | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-139-1 | 42142 (new) | /learn/mental-wellness/quotes/where-do-core-values-come-from/ | where do core values come from | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-042-2 | 36383 | /learn/mental-wellness/quotes/responsibility-must-come-before-empowerment/ | come before empowerment | 76 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| CQ018-062-1 | 36409 | /learn/mental-wellness/quotes/can-everyone-change-if-we-all-have-a-choice/ | we all have a choice | 76 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| CQ018-077-1 | 36433 | /learn/mental-wellness/quotes/inner-peace-and-knowing-a-decision-is-right/ | decision is right | 76 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| CQ018-082-2 | 36444 | /learn/mental-wellness/quotes/why-we-blame-others-instead-of-taking-responsibility/ | instead of taking responsibility | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-103-1 | 36478 | /learn/mental-wellness/quotes/can-honesty-build-trust-in-a-relationship/ | build trust in a relationship | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-105-2 | 36482 | /learn/mental-wellness/quotes/how-is-trust-built-in-relationships/ | how is trust built in relationships | 76 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07004 | 36255 | /learn/helping-people/quotes/how-to-listen-without-judgement/ | listen without judgement | 75 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07029 | 35463 | /learn/helping-people/quotes/can-self-awareness-be-taught-to-others/ | can self-awareness be taught to others | 75 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07036 | 38497 | /learn/helping-people/quotes/how-good-questions-help-people-find-their-own-answers/ | find their own answers | 75 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| Q07045 | 38506 | /learn/helping-people/quotes/how-values-shape-the-goals-you-set/ | values shape the goals | 75 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ018-028-1 | 36362 | /learn/mental-wellness/quotes/see-your-choices-to-take-control-of-your-life/ | take control of your life | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| Q07005 | 36256 | /learn/helping-people/quotes/core-values-in-social-work/ | core values in social work | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07009 | 36260 | /learn/helping-people/quotes/what-it-takes-to-be-a-good-life-coach/ | be a good life coach | 74 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| Q07012 | 36263 | /learn/helping-people/quotes/growing-up-means-taking-responsibility/ | growing up means taking responsibility | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07034 | 38495 | /learn/helping-people/quotes/are-life-coaches-effective/ | are life coaches effective | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07046 | 38507 | /learn/helping-people/quotes/wise-decisions-from-disastrous-ones/ | wise decisions from disastrous ones | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07055 | 38516 | /learn/helping-people/quotes/should-values-guide-your-big-life-decisions/ | values guide your big life decisions | 74 | **under** | contentHasShortParagraphs, keywordInSubheadings, linksHasExternals, linksNotAllExternals |

## 5. Not run, said plainly

- Google's Rich Results test on one quote page (pipeline stage 6) was not run in this session.
- No score line was written into the pages' DSRD 6 records. The score lives in this table, as in the S195, S196 and S202 DONEs.
- No record was changed by this import.

## Commits

Project: nothing to commit, because no tool or record changed. Channel: this DONE and the brief's disposition line.

OWED BACK: the record mends for the 101 under 86 (or a ruling on the outside link for quote pages), and the inbound link placements in section 3.

*No em or en dashes in this file; checked before writing.*
