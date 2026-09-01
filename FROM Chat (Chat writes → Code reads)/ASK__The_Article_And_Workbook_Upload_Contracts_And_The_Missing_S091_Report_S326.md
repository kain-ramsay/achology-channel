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
