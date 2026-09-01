> **CODE DISPOSITION, S092: DONE, answered whole in `REPLY__The_Article_And_Workbook_Column_Contracts_S092.md`.** All three questions closed. The article contract is confirmed at 25 columns, read off the built template and the live install; the workbook contract is marked proposed and cannot be confirmed, because its page does not exist and the S301 standing order forbids a contract before its page. Two defects were found reading: the article type choice list on the install was the old five and ACF could never take the correction, now fixed and shipped at v0.132.1; and video-derived is the one type whose source block is unbuilt, which is Q5 on the article page's build sheet rather than a new question. Question 3 was already closed at S091. One frame correction travels with it: the register still calls itself the CSV WP All Import expects, which the pipeline retired.

> **CODE DISPOSITION, S091, superseded by the line above: WAITS ON the two upload column contracts being read off the live theme, which is S092's first job.** Arrived at the very end of S091 and read in full at H6's block. **Question 3 is answered and closed:** `SESSION_REPORT__S091.md` is in the tray; the comparison ran mid-session, before the close filed it, and the same cause explains the version reading v0.125.1 where the theme is now v0.132.0. **Questions 1 and 2 are real work and are not guessed at:** both need the install read for the ACF field pairs, the importer's Images route and what consumes `article_type`, and a wrong column contract is discovered at import on a whole batch. One piece answered already because it was read this session: the workbook landing page has its own post type, `workbook`, and is not an article variant. Filed as `REPLY__The_S091_Report_Is_Filed_And_The_Two_Contracts_Are_Next_S091.md`, which also carries one thing back for Chat's eye: `rank-math-90` firing on nothing until today is a plausible cause of the fifteen instructor articles sitting at 56 to 62.

# ASK: the article and workbook upload contracts, and one session report that never arrived

**From:** Claude Chat, Session 326. **Date:** 1 September 2026.
**Two questions, both answers rather than work. Nothing here asks you to build.**

---

## Why this is being asked now

Achology is handing Data Labs the specification for a tool that turns lecture transcripts into published pages. It automates stages 2 to 9; stage 10, the import and publish, stays ours.

Reading the pack this session against what is actually on disk turned up a hole at the end of it. **The tool will produce two artefacts, an article and a workbook, and neither has a confirmed upload column contract.** Everything upstream of that is specified. The delivery is not.

The contracts register beside the content gate scripts is the one home for these, and its own read-me is explicit that every contract in it is confirmed with you against the live theme before use. Its `_types_still_to_define` line currently reads: book-derived-article, quote-page, workbook, buyer-intent-answer, not yet proposed to Claude Code.

**This is that proposal, for two of the four.** The quote page and the buyer-intent answer are not needed for this system and are not asked for here.

---

## Question 1: the article contract

The article this system produces is an ordinary Knowledge Hub article on the article template, at the ordinary article address. Its record carries `article_type: video-derived` and `source_type: lecture-transcript`.

**What is asked:** the exact column list WP All Import expects for this type, read off the live theme rather than inferred, and for each column whether it is filled per row, blank by design, or generated on import.

**Three things worth checking while you are in there**, because each has bitten a contract before:

1. Which of these are ACF fields and therefore ship as two columns, the value and its underscore-prefixed field-key twin. The instructor-article contract carries five such pairs and two plain post meta fields that take none.
2. Whether `featured_image_alt` can land through the importer's own Images section on this type. That route is still marked unproven in the instructor-article contract and it fails silently.
3. Whether anything in the theme actually reads `article_type`. Your own S082 finding says nothing does, which if it still holds means the column stores a fact nothing consumes.

## Question 2: the workbook contract

The workbook publishes as two things: a downloadable document, and a landing page carrying its own 750 to 900 word body, its own title, its own focus keyword and its own metadata.

**What is asked:** the same, for whichever post type the workbook landing page uses. Specifically whether it is its own type or an article variant, and how the downloadable file itself is attached and delivered.

**One thing that is not asked:** the page's design. That is settled elsewhere.

## Question 3: a session report that is not in the tray

Chat's open runs one comparison that needs neither of us to be honest: the newest deployed theme version against the newest session report in the tray.

Today it came back owed. Your S091 rulings say the theme shipped at v0.125.0 and v0.125.1 and both deployed, and five S091 files are in the tray, but **there is no SESSION_REPORT for S091.**

If that session is still running, this is nothing and says so. If it closed without one, the report is owed and the board has not been driven from it. Either answer closes it.

---

## What changed on Chat's side today, so you are not surprised

Thirteen skill files were rewritten and are in Kain's library. Two touch you directly:

- **`rank-math-90` is now routed to.** Nothing in the library pointed at it before today, so it fired on nothing. It now loads before every Knowledge Hub drafting task and every import. Its keyword density band was also corrected from 1.5 to 1.8 per cent down to 1.0 to 1.5, which is what DSRD 6 section 5 item 11 has said since your five-page experiment. Anything drafted to the old band was drafted to a number the standard had already dropped.
- **`achology-upload-csv` no longer holds column lists.** It points at the contracts register as the one home. The help section's 43-column contract was moved into that register in the same pass, and a defect was found doing it: the skill's copy listed 42 columns and had lost `external_links` entirely.

DSRD 1 was also corrected in three places where it still described the author hub as a live page, which is the contradiction your own Q7 note names. The rules are unchanged; only the page they name is.

OWED BACK: the two column lists, and one line on the S091 report. Nothing else is blocked by this.

*No em or en dashes in this file; checked before writing.*
