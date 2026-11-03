> CODE DISPOSITION, S454: DONE. All six briefs run again: 78 of 78 imported and verified, redirects proved, 78 of 78 at 86 or more. See the six DONE files in TO Chat of the same names.
> CODE DISPOSITION, S203: WAITS ON a factory session running the six briefs again; read in full by the theme main session, which runs no imports.
**For Code. What this needs from you:** nothing except to run the six refused quote import briefs again, as written. Chat, 3 November 2026, on Kain's "Yes, fix them".

# REPLY: the 14 refused records are mended at source

Answers the six DONE files that say "Imported: 0 of N" for the S453 quote import briefs.

## What was wrong

Twelve of the 14 had an idea inside the third heading of eight or nine words. The quote standard's `heading_patterns` allows an idea of two to seven words, so your body shape check read the heading as a section the type does not rule. The curly marks were never the fault. I cut each idea to seven words or fewer inside the same curly marks. No prose and no title changed.

Two records, CQ001-079-1 and CQ001-085-1, also carried a second, empty `signed` row at line 40 of the fields table, under the real signature on line 8. Your reader takes the last row, so it read them as unsigned. CQ001-079-1 was hiding that behind its heading fault. I removed the empty row from both. Kain's 2 November signature is untouched on both, and nothing was signed.

## The 14 records, by brief

- Experience, truth and perspective (12): CQ018-065-1, CQ018-066-2, CQ018-095-1.
- Goals, family and habits (14): Q07037.
- Maturity, communication and good intent (14): CQ018-052-1, CQ018-090-1.
- Self centredness, self control and self reflection (14): CQ001-070-1, CQ018-069-2, CQ018-130-1.
- Motivation, respect, quick fixes, imperfection and openness (16): CQ001-079-1, CQ018-012-2, CQ018-048-1, and CQ001-085-1 (the empty signed row).
- Boundaries, insecurity and society (8): CQ018-073-2.

## What I ran after the change

- `import_quote_pages.py --offline` on all 14: 14 of 14 pass, none refused.
- `stage5_import_checks.py` on all 14: fields complete and body shape pass on 14 of 14. Its check 3 reads `featured_image`, which is a dead field on a quote record, so it is not a measure here.
- `body_guard.py --signed` on all 14: 0 working notes.
- The content gate: the two heading lines (section headings found 4, unexpected section) no longer fail on the 12 records that had them. Every other line it reports is the same as before the change.

## Held on purpose

Nothing else was touched: no other record, no course page copy, no standard and no importer. The vault gate batches for this mend are `quote_idea_headings_seven_words_s454` and `quote_stray_signed_row_s454`, both with titles kept.

*No em or en dashes in this file; checked before writing.*

OWED BACK: your DONE for each of the six briefs, run again as written.
