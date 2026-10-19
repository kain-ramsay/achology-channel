DISPOSITION, Chat S429 close: still waiting on the same fact as the line below; not touched this session. Now across seven handovers: the S429 handover recommends the Monday theme sitting takes them or Chat archives them with their facts written into DSRD 9.

DISPOSITION, Chat S423: its rulings are written into DSRD 9 section 20.0c. Stays for what is not there: (Audit Fixes) ruling 11's order of works into the plan; (Gate S159) items 12 to 14 onto Backlog: Code and job 22's ten contradictions.
DISPOSITION, Chat S422: stays. Owes Chat: rule items 7 to 11 (with Kain where it is his eye), put items 12 to 14 on Backlog: Code, read job 22's ten contradictions. Waits on: the subject page close-out sitting.

First line of need: Chat rules the five "waiting on a ruling" items below (section B), so the subject page faults can be fixed in the next theme sitting.

# REPORT: page gate on the seven subject pages, S159 (theme session)

Run 11 October 2026 on theme 0.707.217, through Google Chrome (the S158 wrapper, unchanged gate), on /learn/psychology/, /helping-people/, /mental-wellness/, /motivation/, /personal-growth/, /general-interest/, /wisdom-for-life/. Read only; nothing changed.

All seven read the same: **31 pass, 34 fail, 11 for review, 1 not built yet, 9 carved out.** The only differences page to page are the counts inside a line (acronyms, image counts, redirect rows), so every fault is the template's, not a category's.

## A. Real faults (Code's to fix in the theme, no change to the approved look)

1. **Editor's Picks pictures declare the wrong size.** The four thumbnails say 1360 by 649 in the markup but the file is 104 by 49. Same shape, so nothing looks wrong, but the declared size is false (DSRD 7 section 12.3).
2. **Author faces in the quote cards use the file name as their description** (erik-erikson.webp, sigmund-freud.webp and others). They need the person's name (DSRD 7 section 12.3).
3. **The learning path's course cover** (course-quote-cover-001.webp) has no width and height and no lazy loading, though it sits below the fold.
4. **On a phone, the largest picture on the first screen** (a quote card face) is not marked to load first, and the lead article's picture, below the fold on a phone, is not lazy.
5. **Four small icons inside the learning path tiles** are not hidden from screen readers (the inner drawings inside each tile picture). The tile and path artwork are also drawn by hand, not by the icon registry (DSRD 7 section 12.4).
6. **Book covers in the wall ship as JPEG with an editor size in the name** (for example born-for-love-199x300.jpg), and about 30 pictures have no srcset. Cloud job 20 (picture copies) covers part of this; it is held unmerged on Kain's word.

## B. Waiting on a ruling (the approved look and the standard disagree)

7. **No hairlines** between the lead row, the wall and the topic block (DSRD 7 section 4.3 ruling 1). Kain approved the page without them.
8. **The page title is 42px** where DSRD 7 section 3 sets another size.
9. **Breadcrumb spacing:** 71px below the trail on a desktop (48 wanted), 37px on a tablet; on a phone 48 above where 32 is wanted, and the header-to-content gap on a phone is 48 where DSRD 9 section 26 wants 32.
10. **Contrast of the small "Categories" label in the subject bar** (`.sj-label`, six nodes on each page): the accessibility scan fails it. Fixing it changes the approved colour, so Kain's eye.
11. **Acronyms in card titles.** The acronym check fails on article titles printed in the wall (CBT, DBT, REBT, NLP and others). Does "spell it out first" apply to titles shown on a card? Chat to rule.

## C. Tool and record problems (not page faults)

12. **Rank Math and keyword density** report "no post answers to this address": the gate looks for a post, and a category page is a term. The gate needs teaching to read a term (factory); Chat's Rank Math words are still owed (S158 BRIEF, OWED BACK 3 and 4).
13. **Orphan check** could not decide, because its crawl missed 913 pages. Needs `search_gate.py --map` first (factory).
14. **Redirect register** says the chain breaks at "destination in the sitemap", but all seven pages are in the category sitemap today (read this session). The register's stored cell is stale (factory).
15. **No DSRD 6 record** for the subject page yet. That is the close-out step in the order of works, not a fault.
16. The gate only runs here through the Chrome wrapper; no Playwright browser on this iMac (already logged for the factory session).

## D. Cloud branches, read only (nothing merged)

- Job 21 (review of the saved-wall code): no branch exists on origin at 11 October 2026.
- Job 22 (`cloud-work/job22-search-results-page`): search.php, search-parts.php, search.css, functions.php wiring, a search field on the 404, version 0.707.218. Reviewed against main: every helper it calls exists, escaping sound, queries bounded, merges with no conflict. Never rendered. Its no-results page draws a workbook form placeholder that looks live and must not ship until the real form exists; it repeats the workbook capture markup from single-workbook.php; it flags ten contradictions with the standard for a ruling (its report, `cloud-reports/job22-search-results-page.md` on the branch).

OWED BACK: Chat rules items 7 to 11 (with Kain where it is his eye), adds items 12 to 14 to the factory queue, and reads job 22's ten contradictions for the search results sitting.

*No em or en dashes in this file; checked before writing.*
