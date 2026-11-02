**For Chat. What this needs from you:** one record mend, the retitled CQ001-024-1 at 80 (section 4). The other 35 of the 45 land with the 113 page brief, by agreement between the factory sessions (section 1). Factory side session of Code S203, 2 November 2026.

# DONE: the 45 quote articles without the banned word, the 10 sent here (Code, factory, 2 November 2026)

Answers BRIEF__Update_The_45_Signed_Quote_Articles_Without_The_Banned_Word_S451.

## 1. The split, and why

- **35 of the 45 are also among the 101 quote records** of BRIEF__Update_113_Pages_Lifted_To_The_Bar_From_The_S205_Scores_S451. That brief says those records already carry this one's changes and are to be imported once. So they go with the 113 run, in factory session S206.
- **The other 10 were sent here,** by agreement with S206 and with S207, which had not started this brief:
  - CQ001-005-1, CQ001-015-1, CQ001-016-1, CQ001-023-1, CQ001-024-1 and CQ001-054-1;
  - CQ018-009-1, CQ018-018-1 and CQ018-027-1;
  - Q07056.
- **Also sent here:** Q06987 (help-someone-better-themselves), the one quote page that links to the 87 instructor articles and is in neither the 45's 35 nor the 101.

## 2. The three import checks

- **Fields complete and signed, and named files.** `import_quote_pages.py`: 11 of 11 pass every check.
  - The 10 carry the 2 November banned word signature. Q06987 carries its 28 October round one signature, with the instructor link repointed today (address only).
  - The forms of hold left in the 11 bodies are everyday uses: "relaxes its hold", "holding that question open", "on hold", "hold on to" and "holding us back".
- **Body shape.** `body_guard.py --signed`: clean.
- **Links.**
  - Every site address resolves.
  - Every outside link resolves, apart from publishers that refuse scripts (Wiley, Taylor and Francis, Emerald, through doi.org).
  - The one DOI carrying brackets, 10.1016/0022-3999(67)90010-4 on CQ018-009-1, renders whole on the page and opens its ScienceDirect article.

## 3. The update

- `import_quote_pages.py --push`: 11 of 11 updated in place, each matched by its quote_id.
- `--verify`: 11 of 11 clean, all still published. That covers the title, excerpt, category, tags, the quote fields and every Rank Math field.
- **The retitle,** CQ001-024-1 (post 40338):
  - now "How Do You Know If Your Thinking Is Too Rigid?";
  - at /learn/mental-wellness/quotes/how-do-you-know-if-your-thinking-is-too-rigid/;
  - focus phrase "thinking is too rigid".
- **The redirect,** from /learn/mental-wellness/quotes/why-rigid-thinking-holds-you-back/, written and proved at 301 by `publish_gate.py --write-redirect`.
- **The six records** the brief names as already carrying a repointed link went as they stand, in the 35 (S206) or here.

## 4. Rank Math scores against 86

Read one editor at a time, 12 seconds apart, nothing saved, in turns agreed with the other factory sessions.

| Record | Post | Address | Focus phrase | Score | Against 86 |
|---|---|---|---|---|---|
| CQ001-016-1 | 40333 | /learn/mental-wellness/quotes/why-not-every-idea-is-true/ | not every idea is true | 91 | pass |
| CQ001-023-1 | 40337 | /learn/motivation/quotes/why-you-must-leave-the-old-way-behind/ | leave the old way behind | 91 | pass |
| CQ001-054-1 | 42131 | /learn/motivation/quotes/growing-beyond-the-limits-of-your-self-awareness/ | limits of your self-awareness | 88 | pass |
| CQ001-005-1 | 40324 | /learn/motivation/quotes/why-what-you-think-is-true-might-not-be/ | why what you think is true might not be | 87 | pass |
| CQ001-015-1 | 40332 | /learn/motivation/quotes/why-we-talk-ourselves-out-of-what-we-want/ | why we talk ourselves out of what we want | 87 | pass |
| CQ018-009-1 | 36325 | /learn/mental-wellness/quotes/why-do-i-resist-change-so-much/ | resist change so much | 87 | pass |
| CQ018-018-1 | 36344 | /learn/mental-wellness/quotes/is-it-human-nature-to-resist-change/ | human nature to resist change | 87 | pass |
| CQ018-027-1 | 36361 | /learn/mental-wellness/quotes/why-is-it-so-hard-to-change-your-mindset/ | hard to change your mindset | 87 | pass |
| Q06987 | 36238 | /learn/helping-people/quotes/help-someone-better-themselves/ | help someone better themselves | 86 | pass |
| Q07056 | 38517 | /learn/helping-people/quotes/why-people-resist-change-until-they-have-to/ | people resist change | 86 | pass |
| CQ001-024-1 | 40338 | /learn/mental-wellness/quotes/how-do-you-know-if-your-thinking-is-too-rigid/ | thinking is too rigid | 80 | **under** |

**CQ001-024-1, 80.** Measured on the record, the new phrase "thinking is too rigid":
- is not in the first tenth of the body (keywordIn10Percent);
- is in no section between the first and last heading (keywordInSubheadings);
- does not open the search title, "How Do You Know If Your Thinking Is Too Rigid?" (titleStartWithKeyword).

It is in the content, the title, the description and the address. The page is left as it is until the record is mended.

## 5. Not run, said plainly

- The quote cards were not re-baked. The retitle changes no quote text, and the card carries the quote.
- Google's Rich Results test was not run.
- No score line went into a DSRD 6 record.

OWED BACK: the CQ001-024-1 mend. The 35 land in S206's DONE for the 113 page brief.

*No em or en dashes in this file; checked before writing.*
