# RULING_AND_BRIEF: the last breadcrumb is the page's short name, never its H1. Derive `breadcrumb_title` by type at import; render the size for Kain in Safari

**DOCUMENT TYPE:** ruling and brief, from Claude Chat, Session 356. **Date:** Thursday 10 September 2026.
**Authority:** Kain, live in the S356 sitting, on the quote page exemplar's breadcrumb wrapping to two lines.
**Owning documents, both written this session:** DSRD 1 section 9 (the rule and the per-type derivation) and DSRD 10 section 8 (the field). Read them; this file does not restate the table.
**Board card:** none of its own; site-wide, carried in the S356 handover until your line lands.
**Read this cold.**

---

## The ruling, in one paragraph

Every content page's last crumb is its short name: the focus keyword in sentence case for quote pages and every article type ("Life comes with no rulebook"), the person's name for a biography, the book's title for a book note, the workbook's short name, the help question with its lead-in dropped. No more than 40 characters. Course, school and other site pages keep their H1s, which are already short.

## What to build

1. **The derivation in the importer, for every content type**, from the DSRD 1 section 9 table: derive `breadcrumb_title` from the record's fields when the record does not carry one; an explicit `breadcrumb_title` on a record wins. Over 40 characters: cut at the last whole word before 40 and flag the record in the import report for a hand-written label.
2. **Map it to Rank Math's per-post breadcrumb title** (`rank_math_breadcrumb_title`), so the rendered breadcrumb and the BreadcrumbList schema both read it. If the theme renders breadcrumbs itself rather than through Rank Math, read the same field.
3. **Backfill the live pages.** Run the derivation across every published Knowledge Hub page and every help answer already on the install, and push the labels. Print the count and the first ten labels per type in your reply, and every label that was cut at 40.
4. **The size is a visual ruling, and it is Kain's in Safari.** Render the breadcrumb smaller on the quote page exemplar, in place, with the page around it, and put the options to him tabbed, one on screen at a time in the same position (standing rule 16). What he approves goes into DSRD 7 by Chat at close, from your RULING.

## What comes back

One line in TO Chat when the field derives and maps and the backfill has run, with the counts; and the size RULING from the Safari sitting.

OWED BACK: that line and that ruling. Nothing else.

*No em or en dashes in this file; checked before writing.*
