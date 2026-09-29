> CODE DISPOSITION, S138: WAITS ON its turn in 000__QUEUE__What_To_Open_And_In_What_Order_S390 (the Courses page is published, S138; the next session is a factory session on the S389 push, Kain's word).

**Needs from Code:** build the What Achology Believes page, then the nine Seven Beliefs articles, then push the 39 back-links, so the page, the series and the links all go live together. Behind the Courses page.

# BRIEF: What Achology Believes and the Seven Beliefs series, one brief

**From:** Claude Chat, S390, Tuesday 29 September 2026. **To:** Claude Code.
**Board cards:** What Achology Believes (the public stance page, linked from every course page) and The Seven Beliefs: a Nine-Part Series and its Map of Ideas.
**Approved by Kain** in Chat at S386, S387 and S388.
**This one brief replaces four files**, moved to Archive with a head note pointing here: `BRIEF_AND_SPEC__Build_The_What_Achology_Believes_Page_S386`, `ADDENDUM__What_Achology_Believes_Page_Links_Each_Belief_To_Its_Article_S387`, `BRIEF__Build_The_Seven_Beliefs_Series_And_Push_The_39_Back_Links_S388` and `ASK__How_The_Import_Treats_The_Series_Previous_And_Next_Links_S387`. Nothing in them is lost. The 39 back-link export stays beside this brief.
**Where it sits:** after the Courses page (Kain, S136). Nothing here is urgent. Do Part A first; Part B lands the series and the links in one run.

---

# PART A: the page

**The page's job.** Let a person read, before they pay, the seven beliefs every Achology course is taught from, in plain words, so nobody finds the point of view halfway through a course.

**The words.** `APPROVED__What_Achology_Believes_Page_Copy_S386.md`, Launch Content Planning folder: everything below its rule. It replaces the S372 file. Flowing prose, no bold run-in labels. Copy it word for word; nothing in it changes. The H1 is the page title. One mechanical correction that changes no word: links are written site-relative (`/policies/disclaimers/`, `/certification/`, `/policies/trust-statement/`).

**The build.**
1. Address `/about/what-achology-believes/`, parent About (DSRD 1 section 2.2).
2. Template: the shared quiet-page frame the Founders' Letter, the Manifesto and the Code of Ethics use. Reading width 800 (Kain, S135).
3. Body in the WordPress editor, not a theme content file, so Kain and Karen can edit the words after launch. One small theme file turns off the "Last updated" line and sets the close. It names no body.
4. The close: the family's own "Where next" three-route grid, with "See all 28 courses" (to /courses/) as one row, as the Manifesto and the Code of Ethics close. Kain can ask for a real button on sight.
5. Metadata, Chat's proposal for Kain's yes on the page: SEO title "What Achology Believes"; description "The seven beliefs every Achology course is taught from, in plain words, so you can decide whether our approach is right for you before you enrol." (146 characters).
6. **Linked from all 28 course pages:** one link on the course page template, "Read what Achology believes", placed where a buyer meets it before the enrol buttons. Where exactly is a visual decision: show Kain on a real course page.

**The links from this page to the series** (no word of the approved copy changes; these are links only):

| On the page | Links to |
|---|---|
| Heading: Every human being can grow and mature | Part 2, /learn/psychology/articles/can-people-change/ |
| Heading: Self-knowledge comes before personal growth | Part 3, /learn/psychology/articles/know-thyself/ |
| Heading: Wisdom begins with accurate thinking | Part 4, /learn/psychology/articles/thinking-errors/ |
| Heading: Emotions can be understood and managed | Part 5, /learn/psychology/articles/understanding-and-managing-emotions/ |
| Heading: Your emotional state is your responsibility | Part 6, /learn/psychology/articles/emotional-responsibility/ |
| Heading: Personal growth comes before a better life | Part 7, /learn/psychology/articles/change-your-life-from-the-inside-out/ |
| Heading: Personal growth always serves a purpose | Part 8, /learn/psychology/articles/sense-of-purpose/ |
| The page's opening, where it speaks of where the beliefs come from | Part 1, /learn/psychology/articles/standing-on-the-shoulders-of-giants/, and Part 9, /learn/psychology/articles/philosophy-of-life/ |

Read the addresses from the records' page fields at build time, not from this table, in case one changes. **These links go live only when the nine parts are published**, so no link ever points at a missing page (DSRD 1 section 6.4 rule 5). Build them with the page; switch them on in Part B's run. How a heading carries a link, or whether a short line under it does, is a visual decision: render it for Kain in Safari, tabbed where there is a choice.

**For Kain's eye in Safari, one sitting, tabbed where there is a choice:** (1) italics: the body column has no italic rule and the copy has book titles in italics, so show the browser default beside one considered rule on the tokens; (2) the close, "Where next" as built, and a button only if he asks; (3) the course page link placement; (4) the metadata; (5) how the heading links look.

**Not in this brief:** the short block on the About page (Kain's "What Achology is for" paragraph, the seven beliefs as seven lines, a link here). Its words are drafted by Chat for Kain to read first, then briefed separately.

---

# PART B: the series and the 39 back-links

**What is ready.**
- **The nine parts, all approved by Kain** (Parts 1 and 2 at S387, Parts 3 to 9 at S388). In Content Records, `seven-beliefs-series`, as PART_01 to PART_09, each marked APPROVED in its head comment. Each record carries its page fields table, its Search and Citation Brief, its Body and its Sourcing record. The Body is what the reader sees; the Search and Citation Brief and the Sourcing record are not published.
- **Addresses:** every part at `/learn/psychology/articles/{post_name}/`, exactly as its address field gives it. The slugs are standing-on-the-shoulders-of-giants, can-people-change, know-thyself, thinking-errors, understanding-and-managing-emotions, emotional-responsibility, change-your-life-from-the-inside-out, sense-of-purpose, philosophy-of-life.
- **The 39 back-links:** `EXPORT__Seven_Beliefs_Back_Links_39_Pages_S387.csv`, beside this brief. One sentence (two on three pages) inserted into each of 39 live Knowledge Hub pages, keyed on post_name, with the exact sentence each follows. post_id is blank on every row: fill it from the install by post_name before rollout. Chat checked every sentence against the approved parts at S388 and corrected one row (the-farther-reaches-of-human-nature) in the file itself; use the file as it stands.

**The Previous and Next block, and the question that comes with it.** Kain ruled at S387 that every article in a series ends with a way back to the previous part and on to the next. The nine records end with this block, after the last paragraph and before the sourcing record:

`**Previous:** [Part N-1, {that part's H1}]({address})`
`**Next:** [Part N+1, {that part's H1}]({address})`

Part 1 carries Next only; Part 9 carries Previous plus a "Back to the start" link to Part 1. Recipe 9 of the Cowork Production Harness treats the block as navigation, not prose: not counted toward word count, reading ease or the paragraph floor.
**The question, read-only, answer it in your REPORT:** at import, does the block land in the post body as two plain paragraphs, and if so will `search_gate.py` and Rank Math count those short lines against the paragraph floor, reading ease or word count? If they will, say what marker or field would let the gate skip them. A theme "previous and next" block would be a visual decision for Kain to see rendered, and nothing about one is asked or decided here. Chat writes your answer into Recipe 9 and, if the records need a marker, briefs Cowork to add it. **Answer this before you import, so a marker can land first if one is needed.**

**The job.**
1. Build the nine parts as Knowledge Hub articles from their records, with a "Part N of 9" panel as the card's Definition of Done names.
2. Push the 39 back-links from the export; read each page back from the install after the push.
3. Switch on Part A's links to the series in the same run.
4. DSRD 6 on every one of the nine new pages, and on the 39 changed pages as your standing practice requires for an edit.

**What not to change.** No word of any part's Body, and no sentence of the export. If anything will not land as written, stop on that page and ask through TO Chat.

---

## Done when

The page answers 200 at its address, every course page links to it, Kain has ruled the Part A items by eye, its DSRD 6 record is filed with no fail and no not run (Chat writes chapters 6, 7 human half and 8 from the live copy), the nine parts are live, and the 39 pushes are read back.

## OWED BACK

One REPORT in TO Chat: the page address and Kain's rulings; the nine pages live with their post IDs; the 39 pushes read back; the answer to the Previous and Next question; each page's DSRD 6 result.

*No em or en dashes in this file; checked before writing.*
