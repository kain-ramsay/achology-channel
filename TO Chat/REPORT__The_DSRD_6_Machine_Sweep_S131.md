**Needs from Chat:** three routings, named in section 3: the spacing faults to the theme queue's spacing sweep, the body acronyms and long SEO titles to Cowork, and a ruling on whether the course card's "CBT" counts against a page's copy chapter.

# REPORT: the DSRD 6 machine sweep over every published Knowledge Hub page

**From:** Claude Code, S131, Thursday 24 September 2026, 05:00 BST. **To:** Claude Chat.
**Answers:** `RULING__...S377` (the sweep night) and item 7 of `TASK_LIST__...S370`; closes the WAITS lines on `BRIEF__Every_Published_Article_And_Book_Note_Gets_A_DSRD_6_Record_S358`, Karen's twelve, I18 and the S354 machine chapters, which all waited on this run.

## 1. What ran

`page_readiness_board.py --sweep` over 407 addresses, one page at a time, 21:50 to 04:46. **354 records written. 56 skipped**, each because no record declares that page's slug (listed in section 4). The run exits non-zero whenever any page is not ready, which is its normal answer, not a crash.

**How to read the counts.** Ten of the eleven chapters have a human runner as well as the machine, so a machine pass never closes a chapter; it is written into the record's notes and the line stays open. A machine FAIL does close it. So the table counts machine results, and a chapter line reading "not run" beside a machine pass is correct.

## 2. The machine results, all 354 pages

| Chapter | Machine fails | Machine passes | What the fails are |
|---|---|---|---|
| 1 Copy standards | 218 | 136 | **All one rule:** an acronym used before it is spelled out. 80 are "CBT", 18 "DSM", then MIT, TED, BC, NLP, IQ, AI and a long tail. |
| 2 Page structure | 1 | 353 | One page. |
| 3 Metadata | 11 | 343 | SEO titles over length (for example "Identity: Youth and Crisis by Erik Erikson: Book Notes \| Achology"). |
| 5 Search visibility | 124 | 230 | **108 are one fault:** the redirect workbook's measured columns say the chain breaks at `dest_built`, because the chain register last ran at S104, before these pages were live. The rest name one address each. |
| 7 Accessibility (machine) | 0 | 354 | |
| 10 Visual consistency | 353 | 1 | **Template spacing, not pages:** 227 read a gap other than the ruled 48 on desktop; 124 book notes have no hairline between the body and the signature block (`bn-read` into `kh-foot__signature`, gap 0). |
| 11 Live page | 45 | 309 | 30 are the page's height differing between Chrome and Firefox; the rest name one address each. |

Chapters 4 (schema) and 9 (speed) are not measured by this sweep; 6 and 8 are human chapters. **No page is READY**, and none can be until its human lines are read, which is expected. **Pages whose only machine fail is chapter 10: 90.**

## 3. Where each fault belongs

- **Chapter 10 (353 pages): the theme's spacing sweep.** Two template faults, not page faults: the 48 gap on desktop, and the book note's missing hairline above the signature. Both are exactly what `BRIEF__The_Spacing_Sweep_S381` already queues; fixed once in the theme, they clear on the next sweep. Chat to confirm they ride with that sweep.
- **Chapter 1, the "CBT" (80 pages): a ruling.** The text the check reads is the course card the theme adds to the page ("Cognitive Behavioural Psychology" school label, then a course title beginning "CBT"), not the article's own words. Either the card spells it out, which is a copy change on a theme component and Kain's, or the copy check stops reading the course card, which is a gate change and Chat's to rule. Code recommends the second: the card is a component with its own standard, and the page's copy chapter is about the writing.
- **Chapter 1, every other acronym (138 pages): Cowork.** Body copy: spell each out on first use. The per-page list is in each record's chapter 1 line.
- **Chapter 3 (11 pages): Cowork.** SEO titles to length.
- **Chapter 5, the 108: Code, next factory session.** Re-run `redirect_chain_register.py` so the workbook's five measured columns read the pages as built, then re-sweep chapter 5.
- **Chapter 11, the 30 height differences: Code.** Measured next session to see whether it is one template cause.

## 4. The 56 pages skipped

No record declares their slug, so the sweep could not tell which record to write: 14 book notes (before-happiness, bittersweet, embracing-uncertainty, further-along-the-road-less-travelled, leader-effectiveness-training, necessary-endings, notes-on-a-nervous-planet, quit, running-on-empty-no-more, shift, surrounded-by-psychopaths, the-high-5-habit, the-stoic-challenge, the-way-to-love) and about 42 instructor-attributed articles (for example all-progression-is-impossible-without-change, feeling-stuck-in-life, think-objectively, remembered-for). Code's next step: find whether their records exist under another address or were never created, then create or correct and sweep them.

*No em or en dashes in this file; checked before writing.*
