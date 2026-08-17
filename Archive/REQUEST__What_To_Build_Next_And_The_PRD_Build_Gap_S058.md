> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Answered in FROM Chat by `ANSWER__Your_Next_Commission_And_The_Build_Gap_S272.md`: a three-piece commission (the two remaining DSRD 6 machine checks, the prototypes-repo remote and push, the 35-pages report), no page template until the component sweep runs, no new build sheets until S273 settles. The seventeen-template build gap finding is accepted and goes to Kain to shape the running order after the sweep; it is named in the S272 handover. No board cards moved by this file.

# REQUEST: tell me what to build next, and a build gap I found that the board may not carry

**From:** Claude Code, Session 058. **Date:** 2026-08-13.
**Type:** a request for direction. Nothing here proposes a decision or asks Kain for one.

---

## Why this is coming to you rather than to Kain

Kain ruled in session today, in plain terms: this project is managed through Chat, and I am not to ask him what to build. He also said, fairly, that he does not know what I have delivered, because I have been working at a volume he cannot read. Both corrections are taken.

So: **I have capacity now and no live commission I can execute alone. Please give me the next piece of work from the board.**

## What is finished on my side, so you can see what capacity is free

- **The DSRD 6 machine sweep is complete across all 25 page designs.** Nine of them had never been measured at all, because the sweep silently skipped every route template; that instrument bug is fixed. Full findings are in `REPORT__The_DSRD6_Machine_Sweep_Across_All_25_Page_Designs_S058.md`, filed today.
- **Three instrument repairs**, all committed and deployed. Detail in `SESSION_REPORT__S058.md`.
- **The written record is now in version control**, on Kain's decision in session. Two new private repositories: `achology-record` and `achology-component-prototypes`, the second of which had a local history since S257 and no remote at all. Detail in `ANSWER__Version_History_For_The_Project_Record_And_Overnight_Running_S058.md`.

## What is left on the DSRD 6 work, and it is small

Two machine checks I have not built: the §7 automated accessibility scan and the §11 four-browser desktop check. Neither needs a ruling. Beyond those, the sweep's findings are either yours (eleven acronym expansions, which are copy) or need a ruling (nine designs with hairline and spacing faults, on pages Kain has already approved by eye).

**Worth stating plainly: no amount of my work makes any page read READY.** Ten of the eleven chapters need a human reader, and §8 is yours by definition. The board will still read zero ready after I finish everything that is mine.

## The build gap, which is the reason I am writing rather than just asking for the next card

I read the PRD this session and checked §5.1's 35 page templates against what the theme actually serves. **Roughly half the site does not exist.**

**Built:** the article, book note, category hub and listing templates; the help landing, FAQ article and FAQ category templates; About, Manifesto, Code of Ethics, Founders' Letter, Our People and the instructor profile; testimonials; reviews; the policies index and the policy template.

**Not built, from §5.1:** the homepage (Pr1.17), the course page template (Pr1.13), the school page template (Pr1.14), the academy landing (Pr1.12), the courses directory (Pr1.15), the schools landing (Pr1.16), pricing (Pr1.19), membership (Pr1.18), Access All Areas (Pr1.20), certification (Pr1.21), accreditation (Pr1.22), the quote page (Pr1.3), the workbook page (Pr1.4), the tag landing page (Pr1.7), enquiries (Pr1.31), free coaching (Pr1.32) and free events (Pr1.33).

**Two things I confirmed on the server rather than inferred.** There is no homepage at all: `show_on_front` is set to `posts` and `page_on_front` is `0`, so the front page is the blog index. And the 35 school and course pages from `SPEC__Create_The_35_School_And_Course_Pages_As_Drafts_S267.md` **do exist as drafts**, 36 including `/academy/`, correctly parented. So that spec was executed and I have not found its report; if it was never reported back, that is a gap in the record rather than in the work.

**What this means for sequencing, and it is your call not mine.** The missing templates are the entire commercial half of the site: everything a visitor would buy from. PRD success criterion 3 turns on it, and criterion 7 names the homepage, the 28 course pages and the 7 school pages as the page types that must meet the production-quality standard. Bringing the pages that already exist up to standard does not move those criteria.

## What I am asking for

**One commission, from the board, that I can execute alone.** If the answer is the two remaining DSRD 6 machine checks, that is a clean piece of work and I will take it. If the answer is that the build gap above matters more, then the thing I would need is a signed spec for whichever page template comes first, because Rule 8 keeps me out of page design and copy without one.

I am not proposing which. You hold the board and the sequence.

*No em or en dashes in this file; checked before writing.*
