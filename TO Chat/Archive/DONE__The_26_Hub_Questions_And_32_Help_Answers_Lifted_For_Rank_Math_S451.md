ARCHIVED, Chat S452 (2 November 2026): road step 18 read: every page this file names that is under its bar or held is listed with its cause and state in 99 Working Papers, planning, STEP18__Every_Landed_Page_Under_The_Bar_S452; the records needing mends go to a writing session and back to Code; the rest wait on signed briefs Code has not landed yet.

**For Chat. What this needs from you:** mend at source the four hub question records held for dead outside links (section 2), and one Help answer that went out with a dead outside link (section 2). Everything else is done. Factory side session of Code S203, 2 November 2026.

# DONE: 26 hub question articles and 32 Help answers lifted for Rank Math (Code, factory, 2 November 2026)

Answers BRIEF__Update_26_Hub_Questions_And_32_Help_Answers_Lifted_For_Rank_Math_S451. Route followed: TO Chat/DONE__The_Hub_Question_Articles_On_The_Build_Site_S199 and DONE__The_104_Quote_Articles_Round_One_On_The_Build_Site_S205.

## 1. Counts

- **54 of 58 updated in place and read back clean:** 22 hub question articles and all 32 Help answers. Every one stays published.
- **4 held** (section 2): conditions-of-worth, cbt-vs-dbt, counselling-vs-psychotherapy, counselling-vs-cbt. Their build site pages are untouched.
- **3 addresses moved, 3 redirects written and proved** (section 4).
- **1 inbound link repointed** (section 5).
- **Score table:** 22 of 22 articles at 86 or over, 32 of 32 Help answers at 90 or over. None under its bar (section 6).

## 2. The three import checks

- **Check 1, fields complete and signed.** `stage5_import_checks.py`: 26 of 26 and 32 of 32 pass. All 58 carry the S451 signature dated 2026-11-02. No form of hold, holds, held, holding or holder in the body, title, excerpt, search title, description or picture text of any of the 58. Every article picture description is 125 characters or fewer.
- **Check 2, body shape.** 58 of 58: ruled sections only, no working note.
- **Check 3, every link resolves.**
  - **Site addresses, read against the server's own list of 1,265 published addresses:**
    - 15 course pages under /academy/ are not built yet. They are pages to come, not broken links.
    - 5 articles are drafts: hypnotherapy, behavioural-psychology, cognitive-psychology, developmental-psychology and social-psychology (posts 39480, 39456, 39460, 39464, 39508). Also pages to come.
    - 4 book note links name a different subject in the address from the post's own. awaken-the-giant-within and words-that-change-minds are linked under /learn/personal-growth/. the-history-of-philosophy and the-power-of-now are linked under /learn/wisdom-for-life/. Read from inside the host, each of the four answers 200, so they resolve. The records could carry each note's own address: awaken-the-giant-within under motivation, words-that-change-minds under psychology, the other two under general-interest.
  - **Outside links, 165 distinct:** 128 answer 200. The rest are sites that refuse scripts or timed out (403, 429, timeouts), except **six really gone**, each read in a browser:
    - conditions-of-worth: eden.cs.univie.ac.at .../theory-of-psychotherapy and .../theory-of-psychotherapy/fully-functioning-person (both 404). **Held.**
    - cbt-vs-dbt: psychwire.com .../what-is-wise-mind (404). **Held.**
    - counselling-vs-psychotherapy: counseling.org consensus definition of counseling (404) and bacp.co.uk scoped FAQ, "faqs-scoped-titles" (410, "The page you requested was removed"). **Held.**
    - counselling-vs-cbt: the same BACP scoped FAQ (410). **Held.**
    - HELP__what-do-you-learn-in-social-psychology: curriculum.maastrichtuniversity.nl/meta/486518/social-psychology (no such host). **Not held.** Factory S205's 198 Help answers run had already sent this page this morning from the current record, which carries the S451 signature (`article_body_update.py --with-seo`, 09:01). So it is on the build site with that link. S205 names it in its own DONE as well. It scored 100.
  - **What Code needs:** a replacement source or a cut for each of the six links, in the records. Then the four held articles land from their current records with the rest of this brief's work: body, search fields, picture description, read-back and score.

## 3. The update

- **Order of work, so the update tool could match each record by its new name:**
  - **The three renames,** first, under clearance 9526d2fe4a4ca016 (`publish_gate.py --update --clear`; "nothing an update breaks" on all three). One command, three `wp post update --post_name`, no status key.
- **Body, excerpt, search title and search description:**
  - The theme's `tools/article_body_update.py --apply --with-seo` sent 40 of the 54: 22 articles and 18 Help answers, 0 refused.
  - The 14 Help answers shared with the S450 brief were sent by factory S205 at 09:01 from the same current records. Code did not send them a second time. They were agreed between the two sessions by message, and Code read back all 14 against today's records afterwards.
- **Help answer titles and focus phrases with their other phrasings:** `import_help_answers.py --update --push`, 32 of 32.
- **Article picture descriptions:** 16 changed and 6 already matched (`wp post meta update` on each featured picture).
- **Article focus phrases:** four changed, as the brief's table names: 39367, 39801, 39291, 39282. The other 18 already matched.
- **Read back, 54 of 54 match.** Read from the install after the last write, against each record:
  - status (publish), address name, title, excerpt, search title and search description;
  - focus phrase (Help answers with their variants, as the importer writes them);
  - picture description (articles);
  - the stored body, character for character, against `article_body_update`'s own conversion of the record.

**Correction, added after filing.** Factory S205 then found that the record reader cut a field at any pipe. Two of the shared Help answers carry " | Achology.com" in their search title: what-do-you-learn-in-behavioural-psychology and what-do-you-learn-in-social-psychology. So the send and this read-back both used the shortened title, and "match" was true only of the shortened value. S205 fixed the body tool (theme d9a3183d) and re-sent both pages whole. None of the other 56 records carries a pipe in any search field.

## 4. Redirects

Written and proved by `publish_gate.py --write-redirect`. Each old address answers 301 to its new one:

| Record | Old address | New address |
|---|---|---|
| cbt-and-person-centered-therapy (39367) | /learn/general-interest/articles/cbt-and-person-centered-therapy/ | /learn/general-interest/articles/cbt-and-person-centred-counselling/ |
| how-to-practice-mindfulness (39801) | /learn/general-interest/articles/how-to-practice-mindfulness/ | /learn/general-interest/articles/practising-mindfulness/ |
| HELP__hypnotherapist-license-do-you-need-one (41450) | /help/certificates-cpd-accreditation/hypnotherapist-license-do-you-need-one/ | /help/certificates-cpd-accreditation/licence-to-practise-as-a-hypnotherapist/ |

## 5. The one inbound link

what-is-mindfulness-based-stress-reduction (39815), the paragraph under "What does looking at yourself involve from day to day?". The link on the words "starting to practise mindfulness" now points at /learn/general-interest/articles/practising-mindfulness/.

- **In the record:** only the address changed, no word.
- **On the build site:** sent by `article_body_update.py --apply`, body only, and read back matching the record.

## 6. Rank Math scores

- **How they were read:** `score_run.settled_score`, one editor at a time, 12 seconds apart, nothing saved (`block_every_write`), after the S205 session had finished its own scoring. No challenge page and no 202 met.
- **The bars:** articles against 86, with contentHasAssets and lengthContent set aside (RULING S449); Help answers against 90.
- **No page is under its bar,** so no failing tests are owed. The per-test reader reports only part of Rank Math's list here: it showed keyword tests at 0 on a page scoring 100. So it was not used to name anything.

| Record | Post | Address | Focus phrase | Score | Against bar |
|---|---|---|---|---|---|
| best-mindfulness-books | 39793 | /learn/general-interest/articles/best-mindfulness-books/ | best mindfulness books | 89 | pass (86) |
| can-self-awareness-be-learned | 39797 | /learn/general-interest/articles/can-self-awareness-be-learned/ | can self-awareness be learned | 89 | pass (86) |
| lack-of-self-awareness | 39807 | /learn/general-interest/articles/lack-of-self-awareness/ | lack of self-awareness | 89 | pass (86) |
| best-counselling-books | 39361 | /learn/general-interest/articles/best-counselling-books/ | best counselling books | 88 | pass (86) |
| best-life-coaching-books | 39270 | /learn/helping-people/articles/best-life-coaching-books/ | best life coaching books | 88 | pass (86) |
| cbt-and-person-centered-therapy | 39367 | /learn/general-interest/articles/cbt-and-person-centred-counselling/ | cbt and person-centred counselling | 88 | pass (86) |
| cbt-techniques-and-exercises | 39369 | /learn/psychology/articles/cbt-techniques-and-exercises/ | cbt techniques and exercises | 88 | pass (86) |
| does-person-centred-counselling-work | 39279 | /learn/general-interest/articles/does-person-centred-counselling-work/ | does person-centred counselling work | 88 | pass (86) |
| how-to-practice-mindfulness | 39801 | /learn/general-interest/articles/practising-mindfulness/ | practising mindfulness | 88 | pass (86) |
| is-person-centred-therapy-humanistic | 39282 | /learn/general-interest/articles/is-person-centred-therapy-humanistic/ | is person-centred therapy humanistic | 88 | pass (86) |
| nlp-techniques-you-can-try | 39289 | /learn/motivation/articles/nlp-techniques-you-can-try/ | nlp techniques | 88 | pass (86) |
| person-centred-therapy-goals | 39290 | /learn/general-interest/articles/person-centred-therapy-goals/ | person-centred therapy goals | 88 | pass (86) |
| should-i-be-a-life-coach | 39292 | /learn/helping-people/articles/should-i-be-a-life-coach/ | should i be a life coach | 88 | pass (86) |
| types-of-cbt | 39293 | /learn/psychology/articles/types-of-cbt/ | types of cbt | 88 | pass (86) |
| why-life-coaching-is-bad | 39299 | /learn/helping-people/articles/why-life-coaching-is-bad/ | why life coaching is bad | 88 | pass (86) |
| books-to-learn-nlp | 39271 | /learn/motivation/articles/books-to-learn-nlp/ | books to learn nlp | 87 | pass (86) |
| criticisms-of-cbt | 39382 | /learn/psychology/articles/criticisms-of-cbt/ | criticisms of cbt | 87 | pass (86) |
| does-cbt-actually-work | 39384 | /learn/psychology/articles/does-cbt-actually-work/ | does cbt actually work | 87 | pass (86) |
| does-cbt-work-for-anxiety | 39277 | /learn/psychology/articles/does-cbt-work-for-anxiety/ | does cbt work for anxiety | 87 | pass (86) |
| mindfulness-vs-cbt | 39288 | /learn/psychology/articles/mindfulness-vs-cbt/ | mindfulness vs cbt | 87 | pass (86) |
| person-centred-therapy-techniques | 39291 | /learn/general-interest/articles/person-centred-therapy-techniques/ | person-centred therapy techniques | 87 | pass (86) |
| what-is-nlp-natural-language-processing | 39296 | /learn/motivation/articles/what-is-nlp-natural-language-processing/ | what is nlp natural language processing | 87 | pass (86) |
| HELP__become-a-certified-nlp-practitioner | 41429 | /help/comparisons-and-alternatives/become-a-certified-nlp-practitioner/ | become a certified nlp practitioner | 100 | pass (90) |
| HELP__best-cbt-course-or-certification | 41433 | /help/comparisons-and-alternatives/best-cbt-course-or-certification/ | best cbt course or certification | 100 | pass (90) |
| HELP__best-hypnotherapy-course-and-who-accredits-it | 41434 | /help/comparisons-and-alternatives/best-hypnotherapy-course-and-who-accredits-it/ | best hypnotherapy course | 100 | pass (90) |
| HELP__best-online-psychology-course | 41435 | /help/comparisons-and-alternatives/best-online-psychology-course/ | best online psychology course | 100 | pass (90) |
| HELP__how-much-does-a-mental-health-course-cost | 41446 | /help/pricing-and-payments/how-much-does-a-mental-health-course-cost/ | mental health course cost | 100 | pass (90) |
| HELP__how-much-does-a-psychology-course-cost | 41447 | /help/comparisons-and-alternatives/how-much-does-a-psychology-course-cost/ | psychology course cost | 100 | pass (90) |
| HELP__how-to-start-learning-cbt | 41448 | /help/getting-started/how-to-start-learning-cbt/ | how to start learning cbt | 100 | pass (90) |
| HELP__hypnotherapist-license-do-you-need-one | 41450 | /help/certificates-cpd-accreditation/licence-to-practise-as-a-hypnotherapist/ | licence to practise as a hypnotherapist | 100 | pass (90) |
| HELP__introduction-to-mental-health-for-beginners | 41451 | /help/getting-started/introduction-to-mental-health-for-beginners/ | introduction to mental health | 100 | pass (90) |
| HELP__is-an-nlp-course-worth-it | 41454 | /help/comparisons-and-alternatives/is-an-nlp-course-worth-it/ | nlp course worth it | 100 | pass (90) |
| HELP__is-there-a-child-psychology-course-online | 41458 | /help/curriculum-and-subjects/is-there-a-child-psychology-course-online/ | child psychology course | 100 | pass (90) |
| HELP__learn-hypnotherapy-online-or-free | 41459 | /help/comparisons-and-alternatives/learn-hypnotherapy-online-or-free/ | learn hypnotherapy online | 100 | pass (90) |
| HELP__learn-psychology-for-free-online | 41460 | /help/comparisons-and-alternatives/learn-psychology-for-free-online/ | learn psychology for free | 100 | pass (90) |
| HELP__learn-psychology-on-your-own | 41461 | /help/comparisons-and-alternatives/learn-psychology-on-your-own/ | learn psychology on your own | 100 | pass (90) |
| HELP__mental-health-course-different-from-first-aid | 41463 | /help/curriculum-and-subjects/mental-health-course-different-from-first-aid/ | course different from first aid | 100 | pass (90) |
| HELP__mental-health-courses-accredited-or-recognised | 41465 | /help/certificates-cpd-accreditation/mental-health-courses-accredited-or-recognised/ | mental health courses accredited | 100 | pass (90) |
| HELP__should-you-become-a-hypnotherapist | 41469 | /help/outcomes-and-expectations/should-you-become-a-hypnotherapist/ | should you become a hypnotherapist | 100 | pass (90) |
| HELP__study-mental-health-online-is-it-worth-it | 41470 | /help/comparisons-and-alternatives/study-mental-health-online-is-it-worth-it/ | study mental health online | 100 | pass (90) |
| HELP__train-as-a-mental-health-practitioner-online | 41472 | /help/getting-started/train-as-a-mental-health-practitioner-online/ | mental health practitioner online | 100 | pass (90) |
| HELP__train-as-a-wellbeing-coach-or-practitioner-online | 41473 | /help/getting-started/train-as-a-wellbeing-coach-or-practitioner-online/ | train as a wellbeing coach | 100 | pass (90) |
| HELP__what-do-you-learn-in-applied-psychology | 41477 | /help/curriculum-and-subjects/what-do-you-learn-in-applied-psychology/ | learn in applied psychology | 100 | pass (90) |
| HELP__what-do-you-learn-in-behavioural-psychology | 41478 | /help/curriculum-and-subjects/what-do-you-learn-in-behavioural-psychology/ | learn in behavioural psychology | 100 | pass (90) |
| HELP__what-do-you-learn-in-developmental-psychology | 41480 | /help/curriculum-and-subjects/what-do-you-learn-in-developmental-psychology/ | learn in developmental psychology | 100 | pass (90) |
| HELP__what-do-you-learn-in-social-psychology | 41481 | /help/curriculum-and-subjects/what-do-you-learn-in-social-psychology/ | learn in social psychology | 100 | pass (90) |
| HELP__what-does-a-cbt-course-cover | 41482 | /help/curriculum-and-subjects/what-does-a-cbt-course-cover/ | what does a cbt course cover | 100 | pass (90) |
| HELP__what-makes-a-good-nlp-course | 41488 | /help/comparisons-and-alternatives/what-makes-a-good-nlp-course/ | what makes a good nlp course | 100 | pass (90) |
| HELP__where-can-i-learn-about-carl-rogers | 41490 | /help/curriculum-and-subjects/where-can-i-learn-about-carl-rogers/ | learn about carl rogers | 100 | pass (90) |
| HELP__where-can-you-study-behavioural-psychology-online | 41492 | /help/curriculum-and-subjects/where-can-you-study-behavioural-psychology-online/ | study behavioural psychology | 100 | pass (90) |
| HELP__where-can-you-study-cognitive-psychology-online | 41493 | /help/curriculum-and-subjects/where-can-you-study-cognitive-psychology-online/ | study cognitive psychology | 100 | pass (90) |
| HELP__where-can-you-study-developmental-psychology-online | 41494 | /help/curriculum-and-subjects/where-can-you-study-developmental-psychology-online/ | study developmental psychology | 100 | pass (90) |
| HELP__where-can-you-study-psychoanalysis-online | 41495 | /help/curriculum-and-subjects/where-can-you-study-psychoanalysis-online/ | study psychoanalysis | 100 | pass (90) |
| HELP__will-ai-replace-hypnotherapists | 41498 | /help/comparisons-and-alternatives/will-ai-replace-hypnotherapists/ | will ai replace hypnotherapists | 100 | pass (90) |

Not scored: the four held articles, because their pages still carry the earlier words.

## 7. Not run, said plainly

- Google's Rich Results test (pipeline stage 6) was not run.
- No score line was written into the pages' DSRD 6 records. The scores live in this table, as in the S199 and S205 DONEs.
- One record changed: what-is-mindfulness-based-stress-reduction, one link address. No tool changed.

## 8. Found in passing, for the session that owns it

H9's `scanned_folders()` finds the factory scripts by a folder name ending "Content Production Factory + COWORK", which was retired at S434. So the wall no longer reads the Machine's importers (`import_help_answers.py` among them) when deciding whether a command could publish. This is a wall gap for a factory session with the hooks open. Nothing was done about it here.

OWED BACK: the six dead outside links mended in five records (section 2). Then the four held articles land.

*No em or en dashes in this file; checked before writing.*
