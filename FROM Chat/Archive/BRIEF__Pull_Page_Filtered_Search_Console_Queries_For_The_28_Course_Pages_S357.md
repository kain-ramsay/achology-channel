> **CODE DISPOSITION, S131: DONE.** `search-console-course-queries.csv` written: 28 courses with data, 0 without, 4,390 query rows; in `SHIP__Inbox_Work_Part_2_S131.md`.

# BRIEF: pull page-filtered Search Console queries for the 28 course pages, in the help file's shape

**DOCUMENT TYPE:** brief, from Claude Chat, Session 357. **Date:** Sunday 13 September 2026.
**Authority:** Kain, live in the Cowork sitting of 13 September, in his own words ("Yes, absolutely, that's a great suggestion, please go ahead Claude!"), recorded by Cowork in `FROM Cowork/RULING__Kain_Approves_Commissioning_Code_For_The_Course_Page_Search_Console_Pull.md`; signed here by Chat as the brief that word authorises.
**Board card:** The 252 buying answers (3d54da19af3581eb990ad735477ed1ee), which this pull unblocks.
**Session type:** factory, not theme. A data pull, no theme change.
**Read this cold.**

---

## 1. Why

The buying-questions research brief (Cowork, S356 with the S357 addendum) ran in full across all 28 courses and returned zero evidenced candidates. The reason is structural: the only Search Console form Cowork could reach is the site-wide top-1000-by-clicks export, which cannot prove a query landed on a specific course page. You solved exactly this for the help section at S051 with a page-filtered API pull; this brief asks for the same pull on the 28 course pages, so the research can run again with real evidence.

## 2. The work

1. **Match each of the 28 courses to its old, indexed course page URL** (or URLs; several courses had more than one over the years) using your redirect map, the folder built for old-to-new mapping. Cowork's cross-check from the top-1000 export found old URLs for eleven courses; that table is in Cowork's ruling named above and is a check, not the method.
2. **Pull page-filtered query data** through the Search Console API with the service-account key already set up, for every matched URL, over the widest date range the property holds.
3. **Write one file** beside its help sibling in `05. Spreadsheets | Data | CSV Files/Search Console + Live Site Exports/`: `search-console-course-queries.csv`, one row per course per query, columns `course_number, course_name, old_url, query, impressions, clicks, no_query_data`, with `course_name` the canonical name from DSRD 5 section 1.
4. **Name every gap plainly.** A course with no identifiable old URL, or an old URL with no search history, gets its row with `no_query_data` set and the reason, exactly as `help-slug-map.csv` marks a new help slug. Nothing is omitted silently.
5. **Report** the count of courses with data, without data, and the total query rows, in a session report to TO Chat, with the file's path.

## 3. Acceptance criteria

All 28 courses appear in the file, each with data or a named reason for none. Column names as above. Course names canonical to DSRD 5. The report in TO Chat names the file and the three counts.

## 4. What this brief does not authorise

Any change to the theme, the redirect map or the live site. Any drafting. Any judgement on which queries are buying questions; that is the research brief's job when it runs again.

OWED BACK: the session report with the three counts and the file's path.

*No em or en dashes in this file; checked before writing.*
