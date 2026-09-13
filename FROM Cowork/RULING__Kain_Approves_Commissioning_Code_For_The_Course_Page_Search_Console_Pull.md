> CHAT DISPOSITION, S357: answered. Signed as BRIEF__Pull_Page_Filtered_Search_Console_Queries_For_The_28_Course_Pages_S357 in FROM Chat. Archived.

RULING, from Cowork, 13 September 2026, Kain approves commissioning Code for a page-filtered Search Console pull on the 28 course pages.

**Context.** Answers the open question in `RULING__The_28_Course_Buying_Questions_Research_Is_Complete_Zero_Candidates_S356.md`, this same folder. That research found zero evidenced buying-question candidates across all 28 courses because Search Console's only reachable form for Cowork, the site-wide top-1000-by-clicks bulk export, cannot prove a query landed on a specific page. Kain's word, direct in conversation: "Yes, absolutely, that's a great suggestion, please go ahead Claude!", approving the fix named as the fastest path: a Code session pulls page-filtered query data for the 28 course pages, the same way he already pulled it for the Help section.

**What this is, and what it is not.** This is the commissioning content for that pull, written here because Cowork cannot write a file named BRIEF into this channel; that is Claude Chat's role alone, per established house precedent. A Claude Chat session needs to read this, turn it into a signed BRIEF, and forward it through FROM Chat before Code can act on it. Nothing here is itself an instruction Code should act on directly.

**The precedent to work from.** Code has already solved this exact problem once, for the Help section: `search-console-help-queries.csv` (05. Spreadsheets | Data | CSV Files/Search Console + Live Site Exports/), 1,030 rows, one row per help page per query, with columns `url, slug, post_title, query, impressions, clicks, no_query_data, in_build`. A companion file, `help-slug-map.csv`, marks each new help slug that carries no search history at all ("new page, no search history"). This is the working model: the same shape, run against the 28 course pages instead.

**What is being asked for.** A page-filtered Search Console API pull, using the service-account key already set up for exactly this, covering each of the 28 courses' pages, matched to their historical, indexed old-site URL where one exists, output as one row per course per query, in the same shape as the Help file: course number, course name (DSRD 5, canonical), old URL, query, impressions, clicks. Written to a new file beside its Help sibling, for example `search-console-course-queries.csv`, in the same Search Console + Live Site Exports folder. Where a course's old URL cannot be identified or carries no search history, name it plainly in the output rather than omitting it silently, matching the pattern the Help file already uses.

**A starting point, not the source of truth.** Cowork's own research this session matched the site-wide top-1000 bulk export against course names and found old URLs for eleven of the 28, listed below. That match is necessarily incomplete: a course with real but lower-traffic search history would not appear in a top-1000-by-clicks cut at all. Code's own redirect map, the folder built for exactly this old-to-new URL mapping, is the more complete source and should be used ahead of this list; this table is a cross-check, not an instruction on method.

| Course | Old URL found in the top-1000 export |
|---|---|
| 001 DiMAP | /product/online-psychology-diploma-course/, /product/diploma-in-modern-applied-psychology-training-course/, /product/diploma-course-in-modern-applied-psychology-dmap-course-upgrade/ |
| 007 CBT Practitioner | /product/cbt-cognitive-behavioural-therapy-training-course/ |
| 009 Life Coaching Certificate | /product/online-life-coaching-certification-course/, /product/life-coaching-certification-training-course-online/ |
| 013 Hypnotherapy Practitioner | /product/hypnotherapy-practitioner-training-course-online/, /product/hypnotherapy-and-hypnosis-practitioner-course/ |
| 014 Counselling Skills Practitioner | /product/counselling-skills-practitioner-training-course/ |
| 015 Mindfulness Practitioner Diploma | /product/online-mindfulness-practitioner-training-course/ |
| 017 Mindfulness Leadership | /product/mindfulness-leadership-training/, /product/mindfulness-training-for-nurturing-influential-leadership/ |
| 019 Self-Belief Assertiveness | /product/self-belief-development-course/ |
| 025 Hyper-Focus Productivity | /product/motivation-hyper-focus-and-self-efficiency-course/ |
| 027 Healthy Marriage | /product/marriage-relationships-and-premarital-preparation-class/ |
| 028 Entrepreneurs Guide | /product/a-guide-to-business-innovation-and-entrepreneurship-course/ |

The other 17 courses had no old URL in the top-1000 cut; that does not mean no old URL exists, only that none carried enough traffic to appear in it.

**Why this matters.** Without this, the S356/S357 buying-questions research brief cannot produce evidenced course-specific candidates; it was run in full this session and returned zero for exactly this reason, set out in full in the research file. With page-filtered course-page query data in hand, the same brief can be run again and stands a real chance of producing candidates this time.

**Status.** Content ready for a Chat session to sign as a proper brief and forward through FROM Chat. Not yet sent to Code; nothing here is an instruction Code should act on directly.

OWED BACK: nothing further from this side. Whenever Kain is next in a Claude Chat session, this is ready to become a signed brief.
