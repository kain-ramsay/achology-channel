# COMMISSION: review normalisation dry run

**From:** Claude Chat, S262, carrying Kain's amendment made this session. **Date:** 2026-08-11.
**For:** Claude Code. Approved brief: dry run only. Nothing is applied to any review until Kain rules on your report.

## Context, standalone

The Reviews page displays all 4,517 reviews verbatim under DSRD 9 section 29.6 decision 4. Kain amended that decision at Chat's S262: typographic normalisation is now permitted, and it means exactly three things. Sentence-initial capital letters. A terminal full stop where a sentence carries none. Whitespace. Nothing else: words are never added, removed or changed, and acronyms in reviewers' own words stand at every mention. The purpose is that the record reads as cared-for text rather than a words dump while staying every reviewer's own words. The amendment is written into DSRD 9 decision 4 with this commission named in it.

## The work: a dry run over the live review data

Write a script that computes, without applying, the normalisation across all 4,517 reviews:

1. Capitalise the first letter of each sentence where it is lower case.
2. Add a terminal full stop where a sentence's final unit carries no terminal punctuation.
3. Touch nothing else.

**Flag, never force, the awkward classes.** A review whose normalisation is not mechanically certain goes on a flag list with its reason, untouched by the dry run's counts of confident changes. At minimum: sentences ending in emoji or ellipsis; deliberate fragments and scores such as "10/10"; all-caps words and stylised lower-case throughout; anything where sentence boundaries themselves are ambiguous.

**Report the paragraph facts alongside.** Kain also wants subtle spacing between paragraphs inside a review. Whether that is a pure stylesheet value depends on the data, which only you can see: report how many of the 4,517 reviews contain paragraph or line breaks in their stored text, and how breaks are stored (newline characters, markup, or nothing). Do not insert any breaks: inventing a paragraph boundary is an editorial act and is out of scope.

## The deliverable, through TO Chat

One report: total reviews changed by each rule, total untouched, the flag list with reasons, the paragraph-break facts, and a sample of 20 before-and-after pairs spanning the change types for Kain's eye. State where the script would run when approved (the bank, the WordPress data, or both) and how the change would be reversible.

## Bounds

Dry run only. No review text changes in any store. No paragraph breaks invented. The apply pass is a separate commission that follows Kain's ruling on your report.
