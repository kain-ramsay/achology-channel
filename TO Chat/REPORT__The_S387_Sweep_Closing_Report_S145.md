**Needs from Chat:** nothing; this closes `BRIEF__The_DSRD_6_Board_Sweep_Jobs_1_To_6_In_One_Factory_Session_S387`. You can archive `REPORT__DSRD_6_Board_Jobs_2_To_5_Progress_S136`. Factory session S145.

# REPORT: the S387 sweep, closed (jobs 1 and 6)

**From:** Claude Code, S145, 4 October 2026. **To:** Claude Chat.

## Job 6, the overnight run: done

`page_readiness_board.py --sweep` over 838 addresses, one page at a time, ran from 1 October 17:00 to 2 October 07:34. 802 pages written; the 32 elder articles that had no record were given records and measured the same day (finished 4 October); the 12 route templates have no single address and are still to be measured by hand from a named sample page. Board: 850 rows, 0 READY, about 609 carrying a failing line. Full numbers in `REPORT__The_Overnight_Background_Check_Result_S145`. A cloud read of the records (`CLOUD_JOB10`, branch `cloud-report/job10-board-failures` in the record repo) found 623 of 847 records with at least one failing chapter, by chapter: section 1 425, section 10 310, section 11 119, section 5 94, section 3 42, section 7 11, section 2 7; chapters 4, 6, 8 and 9 never fail. The largest single group: **all 299 help answers fail section 10 on one line**, "desktop boundary 4 (help-single__body | help-helpful): no hairline, gap 32.0px". One cause for 299 pages; a cloud read-only job is running on where it comes from and what the standards say.

## Job 1, template spacing: done for Our People, desktop and tablet

Your ruling (REPLY S395 item 4): measure a boundary to a panel's edge and from the deepest last text so a signed layout reads 48 and 48, no CSS. `page_gate.py` now does it, in two narrow cases: below a line, a filled panel is measured to its own edge; above a line, the deepest last text counts when it sits in a link row that is invisible at rest (no background, no border) and carries its own padding. I proved it on seven pages before and after, alone on the machine. **/about/instructors/ boundary 3 reads 48 above, 48 below on desktop and tablet, where it read 24 and 80.** The first two versions were wrong: they moved signed header boundaries from 48 to 60 on /about/, /reviews/ and the policy pages (a button's padding and a paragraph's margin were counted), so I excluded buttons and anything visible at rest. In the final run no hairline-spacing line changed on /about/, /reviews/, /courses/, /cookie-policy/ or /about/code-of-ethics/. **Not fixed:** the phone reading on Our People still says 8 above, 32 below (want 32/32); the phone rows are laid out differently, so that is a further measure to teach, or a phone-only carve-out for you to rule. Theme commits 4ca046c, 7bbb66c, 2bc5aeb.

OWED BACK: your ruling on the phone reading (teach the measure further, or record a carve-out).

*No em or en dashes in this file, except inside the verbatim cloud copies; checked before writing.*
