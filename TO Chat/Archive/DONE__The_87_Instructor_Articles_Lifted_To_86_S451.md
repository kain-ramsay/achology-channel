ARCHIVED, Chat S452 (2 November 2026): road step 18 read: every page this file names that is under its bar or held is listed with its cause and state in 99 Working Papers, planning, STEP18__Every_Landed_Page_Under_The_Bar_S452; the records needing mends go to a writing session and back to Code; the rest wait on signed briefs Code has not landed yet.

**For Chat. What this needs from you:** record mends for two pages under 86 (section 6), and two records whose outside links are gone (section 2). Factory side session of Code S203, 2 November 2026.

# DONE: the 87 instructor articles lifted to 86 (Code, factory, 2 November 2026)

Answers BRIEF__Update_The_87_Instructor_Articles_Lifted_To_86_S451. Route followed: TO Chat/DONE__The_26_Hub_Questions_And_32_Help_Answers_Lifted_For_Rank_Math_S451.

## 1. Counts

- **85 of 87 updated in place with their search fields, read back clean and scored.** All stay published.
- **2 held for dead outside links** (section 2): K02__what-employees-want-from-their-managers (35778) and does-ai-actually-understand (36516). Their addresses moved with the rest, so every repointed link reaches them, but their words and search fields still carry the earlier signature.
- **54 addresses moved, 54 redirects written and proved** (each old address answers 301 to its new one).
- **136 links repointed in 115 records.** The brief's table sums to 136, not 135, because is-mental-health-genetic carries two. On the build site:
  - 85 pages went with the update itself.
  - 37 more pages were sent body only: the Kain Ramsay biography, the best-self-be-you-only-better book note, three hub question articles and 32 instructor articles outside the 87.
  - The 25 quote pages wait on BRIEF__Update_The_45_Signed_Quote_Articles_Without_The_Banned_Word_S451, which sends those same records whole and is next in this session's queue. Their redirects keep every old link working until then.
- **Score table:** 83 of 85 at 86 or over, 2 under (section 6).

## 2. The three import checks

- **Check 1, fields complete and signed.** `stage5_import_checks.py`: 87 of 87.
  - 82 carry the 1 November S451 signature.
  - 5 carry the newer 2 November S451 signature from the 15 pages brief, written on the records after this one: change-is-the-only-constant, personal-growth-requires-discomfort, I17__change-happens-transition-is-your-response, growing-or-standing-still and step-outside-your-comfort-zone. They were sent from the current record, as both briefs ask.
  - Two everyday uses of hold remain and were left: the signed title "Identity Labels: Do They Hold You Back from Who You Are?" (labels-vs-true-identity) and one "Holding" in a sentence on ER06.
- **Check 2, body shape.** `body_guard.py --signed`: 1,119 records read, 0 with a working note in the body.
- **Check 3, every link resolves.**
  - **Site addresses, against the server's published list:** every one resolves except course pages under /academy/ (pages to come) and four more:
    - Seven Beliefs part 6, /learn/psychology/articles/emotional-responsibility/ (AW01). Signed, not on the build site yet: a page to come.
    - Two unsigned quote drafts, why-connection-determines-your-peace (GT02) and why-you-feel-out-of-sync-with-yourself (ER04). Pages to come.
    - /learn/mental-wellness/quotes/why-trust-plus-time-is-the-real-intimacy-formula/ (stages-of-building-strong-relationships). That quote page was renamed today to how-is-trust-built-in-relationships, and the link went through its redirect. See section 3.
  - **Outside links, 93 distinct:** 68 answer 200, and 23 more are sites that refuse scripts or timed out. **Two are really gone**, each read in a browser:
    - K02: https://sescomgt.com/sesco-report/2013/09 (404).
    - does-ai-actually-understand: https://www.scholars.northwestern.edu/en/publications/on-seeing-human-a-three-factor-theory-of-anthropomorphism (404).
    - Both records are **held** until a replacement source or a cut is in the record.

## 3. The update

- **54 renames,** each a `wp post update --post_name` with no status key:
  - 53 under clearance ff268487972c66d3 (`publish_gate.py --update --clear`).
  - The 54th, stages-of-building-strong-relationships (36903), was refused at first. Its live body linked to that renamed quote page, and the page gate counts a redirect as a broken link. Code repointed that one link in the record to /learn/mental-wellness/quotes/how-is-trust-built-in-relationships/: an address only, no word, the same kind of change as the brief's 136.
  - The theme main session added `--post-id` to `article_body_update.py` (theme 79ab2a33), so the corrected body could go to post 36903 under its old name. It then cleared (d3fafb77e127f50c) and moved.
- **Body, excerpt, search title and description:** `article_body_update.py --apply --with-seo`, 85 of 85.
  - Six sends were lost to a clash with another factory session's run of the same tool. Both runs stage on the same two server files, a fault now shared by message between the sessions. Read-back caught all six, and they were re-sent.
- **Picture descriptions:** 70 written. The rest already matched.
- **Focus phrases:** 28 written. The other 57 already matched the record on the build site.
- **Four signed titles that had never reached the build site,** on four of the six pages held earlier for having no outside link. Written under clearance f3d62b1265863b3c (RULING S446: signed pages take their title from post_title):
  - AW03 (39660): "How Do You Talk to Your Teenager as an Equal?"
  - AW04 (39661): "How Do You Stay Calm and Lead in an Emergency?"
  - GK03 (39672): "Why Do We Give Up So Easily Halfway Through Learning?"
  - cover-up-incompetence-with-head-knowledge (36865): "Skill vs Knowledge: Why Knowing More Is Not Competence"
- **Read back, 85 of 85 match:** status, address name, title, excerpt, search title, search description, focus phrase, picture description, and the stored body character for character against the tool's own conversion of the record.
  - The 39 body-only pages match on the body.
  - Fields this brief does not send differ on seven of them:
    - Picture descriptions on the Kain Ramsay biography, best-self-be-you-only-better and is-mental-health-genetic (which is still a draft).
    - Titles, search titles and focus phrases on four instructor articles outside the 87: ai-give-you-a-second-opinion (36512), five-symptoms-mean-depression (36625), hypomania-from-an-ordinary-mood-swing (36629) and self-report-decide-a-diagnosis (36637).
    - Those wait for whichever brief carries them.
  - None of the 87 records, and none of the 26 hub question records in the S451 brief, carries a pipe in any search field. So the pipe fault factory S205 found does not touch them.

## 4. Redirects

All 54 written and proved by `publish_gate.py --write-redirect`, exactly as the brief's address table reads.

## 5. The 136 links in the records

Each old address was replaced only inside a link target, so no word changed. The count for every row of the brief's table was checked before the change (each old address present exactly as often as the table says) and after (each new address present as often, no old one left): 135 rows, 136 links, 115 records, 0 differences. Six of these records are also in the 45 quote articles brief, which already names them as carrying the new address.

## 6. Rank Math scores against 86

- **How they were read:** one editor at a time, 12 seconds apart, nothing saved, in turns agreed with the three other factory sessions. No challenge page and no 202 met.
- **The bar:** contentHasAssets and lengthContent set aside (RULING S449).
- **Two pages under 86.** Their failing tests were measured on the record, because the per-test reader reports only part of Rank Math's list:
  - **cover-up-incompetence-with-head-knowledge (36865), 68.** Focus phrase "skill vs knowledge":
    - in no subheading;
    - not in the search description;
    - not in the picture description;
    - not in the address (cover-up-incompetence-with-head-knowledge, unchanged by this brief).
  - **AW04__what-does-leading-under-pressure-teach-you (39661), 67.** Focus phrase "stay calm in an emergency":
    - not in the body at all (so not in the first tenth or any subheading);
    - the search title does not open on it;
    - not in the search description or picture description;
    - not in the address.
  - Both pages were among the six held for an outside link. This batch gave them a source, but their search finish was not lifted with the other 81. Both are left as they are until the records are mended.

| Record | Post | Address | Focus phrase | Score | Against 86 |
|---|---|---|---|---|---|
| I13__self-awareness-starting-point-of-growth | 34276 | /learn/personal-growth/articles/why-is-self-awareness-important/ | why is self awareness important | 91 | pass |
| GK02__what-is-jungs-shadow | 39671 | /learn/psychology/articles/what-is-jungs-shadow/ | jung's shadow | 89 | pass |
| I16__who-holds-the-master-controls | 34280 | /learn/personal-growth/articles/internal-vs-external-locus-of-control/ | internal vs external locus of control | 89 | pass |
| I17__change-happens-transition-is-your-response | 34282 | /learn/personal-growth/articles/change-vs-transition/ | change vs transition | 89 | pass |
| assumptions-damage-relationships | 36849 | /learn/motivation/articles/assumptions-damage-relationships/ | assumptions damage relationships | 89 | pass |
| balance-the-main-areas-of-life | 36978 | /learn/motivation/articles/balance-all-the-main-areas-of-my-life/ | balance all the main areas of my life | 89 | pass |
| build-genuine-rapport | 36851 | /learn/motivation/articles/build-rapport-with-someone/ | build rapport with someone | 89 | pass |
| can-you-choose-to-be-more-introverted-or-extroverted | 36857 | /learn/motivation/articles/can-you-change-from-introvert-to-extrovert/ | can you change from introvert to extrovert | 89 | pass |
| change-is-the-only-constant | 36859 | /learn/motivation/articles/change-is-the-only-constant/ | change is the only constant | 89 | pass |
| confuse-opinions-with-facts | 36861 | /learn/motivation/articles/why-do-people-confuse-fact-and-opinion/ | why do people confuse fact and opinion | 89 | pass |
| connected-to-your-future-self | 36863 | /learn/motivation/articles/connected-to-your-future-self/ | future self | 89 | pass |
| doctors-have-only-minutes-to-diagnose | 36619 | /learn/psychology/articles/why-do-doctors-spend-so-little-time-diagnosing-patients/ | doctors spend so little time | 89 | pass |
| every-decision-is-a-trade-off | 36869 | /learn/motivation/articles/every-decision-is-a-trade-off/ | every decision | 89 | pass |
| everyone-experiences-reality-differently | 36871 | /learn/motivation/articles/does-everyone-experience-reality-differently/ | does everyone experience reality differently | 89 | pass |
| feeling-stuck-in-life | 36873 | /learn/motivation/articles/feeling-stuck-in-life/ | feeling stuck in life | 89 | pass |
| forget-your-mistakes-but-remember-their-lessons | 36877 | /learn/motivation/articles/how-to-learn-from-mistakes/ | how to learn from mistakes | 89 | pass |
| fountain-or-a-drain | 36879 | /learn/motivation/articles/fountain-or-a-drain/ | fountain or a drain | 89 | pass |
| growing-or-standing-still | 36883 | /learn/motivation/articles/growing-as-a-person/ | growing as a person | 89 | pass |
| happiness-is-a-delusion-fulfilment-is-not | 36885 | /learn/motivation/articles/pursuit-of-happiness/ | pursuit of happiness | 89 | pass |
| labels-vs-true-identity | 36887 | /learn/motivation/articles/identity-labels/ | identity labels | 89 | pass |
| living-according-to-your-values | 36889 | /learn/motivation/articles/living-according-to-my-values/ | living according to my values | 89 | pass |
| pattern-recognition-superpower | 36980 | /learn/motivation/articles/pattern-recognition-superpower/ | pattern recognition | 89 | pass |
| personal-growth-requires-discomfort | 36891 | /learn/motivation/articles/why-does-personal-growth-feel-so-painful/ | personal growth feel so painful | 89 | pass |
| rational-or-emotional-thinker | 36895 | /learn/motivation/articles/rational-vs-emotional-thinking/ | rational vs emotional thinking | 89 | pass |
| remembered-for | 36897 | /learn/motivation/articles/what-do-you-want-to-be-remembered-for/ | want to be remembered for | 89 | pass |
| saying-less-more-influential | 36899 | /learn/motivation/articles/saying-less-is-more/ | saying less is more | 89 | pass |
| self-acceptance-vs-self-improvement | 36901 | /learn/motivation/articles/self-acceptance-vs-self-improvement/ | self acceptance vs self improvement | 89 | pass |
| stages-of-building-strong-relationships | 36903 | /learn/motivation/articles/stages-of-building-a-strong-relationship/ | stages of building a strong relationship | 89 | pass |
| step-outside-your-comfort-zone | 36907 | /learn/motivation/articles/why-is-stepping-out-of-your-comfort-zone-so-hard/ | why is stepping out of your comfort zone so hard | 89 | pass |
| taking-responsibility-creates-personal-growth | 36909 | /learn/motivation/articles/taking-personal-responsibility/ | taking personal responsibility | 89 | pass |
| thoughts-and-emotions-connection | 36911 | /learn/motivation/articles/thoughts-and-emotions-connection/ | thoughts and emotions connection | 89 | pass |
| time-perspective | 36913 | /learn/motivation/articles/time-perspective/ | time perspective | 89 | pass |
| trust-ai-even-when-its-wrong | 36518 | /learn/psychology/articles/authority-bias-in-ai/ | authority bias in ai | 89 | pass |
| turn-a-vision-into-a-goal | 36915 | /learn/motivation/articles/how-to-turn-a-vision-into-reality/ | how to turn a vision into reality | 89 | pass |
| whats-the-key-to-winning-hearts-and-minds | 36919 | /learn/motivation/articles/how-to-win-hearts-and-minds/ | how to win hearts and minds | 89 | pass |
| why-we-feel-the-need-to-prove-ourselves | 36921 | /learn/motivation/articles/why-do-i-feel-the-need-to-prove-myself/ | why do i feel the need to prove myself | 89 | pass |
| your-relationship-with-money-tells-a-story | 36923 | /learn/motivation/articles/healthy-relationship-with-money/ | healthy relationship with money | 89 | pass |
| AN01__what-makes-a-good-teacher-beyond-the-lesson-plan | 39652 | /learn/helping-people/articles/what-makes-a-good-teacher-beyond-the-lesson-plan/ | what makes a good teacher | 88 | pass |
| AN02__what-do-students-really-want-and-how-do-you-find-out | 39653 | /learn/helping-people/articles/what-do-students-really-want-and-how-do-you-find-out/ | what do students really want | 88 | pass |
| AN03__why-does-the-character-of-a-good-teacher-matter-more-than-method | 39654 | /learn/personal-growth/articles/what-character-traits-should-a-good-teacher-have/ | character traits should a good teacher have | 88 | pass |
| AN05__how-can-a-coach-build-character-in-sports-not-just-win-games | 39656 | /learn/helping-people/articles/youth-football-coach/ | youth football coach | 88 | pass |
| AW01__what-does-it-mean-to-take-responsibility | 39658 | /learn/personal-growth/articles/take-responsibility-for-yourself/ | take responsibility for yourself | 88 | pass |
| AW05__finding-purpose-in-life-after-thirty-years-of-service | 39662 | /learn/personal-growth/articles/find-purpose-in-life/ | find purpose in life | 88 | pass |
| ER03__what-is-grief-when-no-one-has-died-and-what-does-it-look-like | 39666 | /learn/psychology/articles/grieve-someone-who-is-still-alive/ | grieve someone who is still alive | 88 | pass |
| ER04__why-do-people-pleasers-abandon-themselves-and-how-do-they-stop | 39667 | /learn/personal-growth/articles/stop-being-a-people-pleaser/ | stop being a people pleaser | 88 | pass |
| ER06__how-do-you-rebuild-your-identity-after-a-big-life-change | 39669 | /learn/personal-growth/articles/how-do-you-rebuild-your-identity-after-a-big-life-change/ | rebuild your identity | 88 | pass |
| GT02__how-do-everyday-conversations-create-a-sense-of-belonging | 39677 | /learn/personal-growth/articles/how-do-everyday-conversations-create-a-sense-of-belonging/ | sense of belonging | 88 | pass |
| GT03__how-do-you-ask-good-questions-in-a-conversation | 39678 | /learn/helping-people/articles/how-do-you-ask-good-questions-in-a-conversation/ | ask good questions | 88 | pass |
| I07__told-story-and-understood-story | 34264 | /learn/helping-people/articles/helping-people-tell-their-story/ | helping people tell their story | 88 | pass |
| I08__hope-does-real-work | 34266 | /learn/helping-people/articles/why-is-hope-important-in-therapy/ | why is hope important in therapy | 88 | pass |
| I09__the-quiet-aim-of-good-helping | 34268 | /learn/helping-people/articles/ending-counselling/ | ending counselling | 88 | pass |
| I10__why-good-advice-rarely-inspires-change | 34270 | /learn/helping-people/articles/why-giving-advice-doesnt-work/ | why giving advice doesn't work | 88 | pass |
| I11__every-behaviour-makes-sense | 34272 | /learn/psychology/articles/why-do-people-act-the-way-they-do/ | why do people act the way they do | 88 | pass |
| I12__what-failure-actually-means | 34274 | /learn/personal-growth/articles/reframing-failure/ | reframing failure | 88 | pass |
| I15__unconscious-belief-patterns | 34278 | /learn/psychology/articles/unconscious-limiting-beliefs/ | unconscious limiting beliefs | 88 | pass |
| I18__persuade-someone-who-disagrees | 35920 | /learn/helping-people/articles/persuade-someone-who-disagrees/ | persuade someone who disagrees | 88 | pass |
| JF01__why-do-we-make-emotional-decisions-and-then-justify-them-with-logic | 39682 | /learn/psychology/articles/why-do-we-make-emotional-decisions-and-then-justify-them-with-logic/ | emotional decisions | 88 | pass |
| JF03__how-do-you-think-critically-about-what-you-read-and-hear | 39684 | /learn/psychology/articles/how-do-you-think-critically-about-what-you-read-and-hear/ | think critically | 88 | pass |
| JF04__how-do-you-pause-before-you-react | 39685 | /learn/mental-wellness/articles/how-do-you-pause-before-you-react/ | pause before you react | 88 | pass |
| JF05__is-it-too-late-to-learn-something-new-in-your-fifties | 39686 | /learn/personal-growth/articles/is-it-too-late-to-learn-something-new-in-your-fifties/ | learn something new | 88 | pass |
| K01__what-makes-a-good-leader | 35776 | /learn/personal-growth/articles/what-makes-a-good-leader/ | what makes a good leader | 88 | pass |
| K06__telling-people-what-to-do | 35786 | /learn/personal-growth/articles/telling-people-what-to-do-at-work/ | telling people what to do at work | 88 | pass |
| K08__respect-is-earned-not-given | 35790 | /learn/personal-growth/articles/is-respect-earned-or-given/ | is respect earned or given | 88 | pass |
| K09__kind-without-being-a-pushover | 35792 | /learn/personal-growth/articles/be-kind-to-people-without-becoming-a-pushover/ | kind to people | 88 | pass |
| K12__people-first-leadership | 35798 | /learn/motivation/articles/people-first-leadership/ | people first leadership | 88 | pass |
| a-psychiatric-diagnosis-simply-wrong | 36607 | /learn/psychology/articles/misdiagnosis-in-mental-health/ | misdiagnosis in mental health | 88 | pass |
| ai-conversations-get-worse | 36510 | /learn/psychology/articles/why-do-ai-conversations-get-worse/ | why do ai conversations get worse | 88 | pass |
| blood-test-for-depression | 36609 | /learn/psychology/articles/blood-test-for-depression/ | blood test for depression | 88 | pass |
| bmi-decide-who-gets-eating-disorder-treatment | 36611 | /learn/psychology/articles/bmi-for-eating-disorder-treatment/ | bmi for eating disorder treatment | 88 | pass |
| diagnosing-bipolar-disorder-in-children | 36613 | /learn/psychology/articles/children-diagnosed-with-bipolar-disorder/ | diagnosed with bipolar disorder | 88 | pass |
| diagnosis-be-scientifically-weak-but-still-useful | 36615 | /learn/psychology/articles/is-psychiatric-diagnosis-useful/ | is psychiatric diagnosis useful | 88 | pass |
| diagnostic-inflation-actually-happening | 36617 | /learn/psychology/articles/diagnostic-inflation-actually-happening/ | diagnostic inflation | 88 | pass |
| does-a-diagnosis-do-to-the-person | 36621 | /learn/psychology/articles/effects-of-being-diagnosed-with-mental-illness/ | effects of being diagnosed with mental illness | 88 | pass |
| everyone-agreeing-on-a-diagnosis | 36623 | /learn/psychology/articles/consensus-diagnosis/ | consensus diagnosis | 88 | pass |
| homosexuality-was-a-diagnosis | 36627 | /learn/psychology/articles/why-was-homosexuality-removed-from-the-dsm/ | why was homosexuality removed from the dsm | 88 | pass |
| mental-disorders-tripled-since-the-1950s | 36633 | /learn/psychology/articles/mental-disorders-on-the-rise/ | mental disorders on the rise | 88 | pass |
| multiple-personality-diagnoses-spike-after-a-film | 36635 | /learn/psychology/articles/multiple-personality-disorder/ | multiple personality disorder | 88 | pass |
| the-dsm-5-cost-five-times-more | 36641 | /learn/psychology/articles/the-dsm-5-cost-five-times-more/ | dsm-5 cost | 88 | pass |
| the-dsm-call-its-own-categories-porous | 36643 | /learn/psychology/articles/dsm-categories/ | dsm categories | 88 | pass |
| what-is-stepped-care | 36601 | /learn/psychology/articles/what-is-stepped-care/ | what is stepped care | 88 | pass |
| AN04__how-do-you-keep-your-purpose-as-a-teacher | 39655 | /learn/motivation/articles/how-do-you-keep-your-purpose-as-a-teacher/ | purpose as a teacher | 86 | pass |
| AW03__how-do-you-talk-to-your-teenager-as-an-equal | 39660 | /learn/personal-growth/articles/how-do-you-talk-to-your-teenager-as-an-equal/ | talk to your teenager | 86 | pass |
| GK03__why-do-we-give-up-so-easily-halfway-through-learning-something | 39672 | /learn/motivation/articles/why-do-we-give-up-so-easily-halfway-through-learning-something/ | give up so easily | 86 | pass |
| cover-up-incompetence-with-head-knowledge | 36865 | /learn/motivation/articles/cover-up-incompetence-with-head-knowledge/ | skill vs knowledge | 68 | **under** |
| AW04__what-does-leading-under-pressure-teach-you | 39661 | /learn/motivation/articles/what-does-leading-under-pressure-teach-you/ | stay calm in an emergency | 67 | **under** |

Not scored: the two held pages.

## 7. Not run, said plainly

- Google's Rich Results test was not run.
- No score line went into the pages' DSRD 6 records. The scores live in this table.
- `build_keyword_register.py`'s path (the brief's note) was not touched. It is a tool change for a factory session with the Machine's tests open.

OWED BACK: record mends for the two pages under 86 and the two dead sources. Then Code sends K02 and does-ai-actually-understand and scores all four.

*No em or en dashes in this file; checked before writing.*
