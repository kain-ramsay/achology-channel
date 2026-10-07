> CODE DISPOSITION, S154: WAITS ON a factory session (this file is for the factory session; the S154 theme session left it untouched).

# BRIEF: two gate changes for workbooks, from Standard Version 13 (S412)

**From:** Claude Chat, S412, Wednesday 7 October 2026, on Kain's rulings in the session. **For:** Claude Code, a factory session. **Board card:** Workbook library and publication.

## What happened

Kain read Cowork's proving batch of five workbooks at S412 and approved the shape. He signed the Content Standard **Version 13**: in a workbook, "In Achology's view" and every phrase like it appears once at most, and the gate fails a workbook at two (Part 7 rule 4, Part 17.6, section 15.2's machine table; defect register S412 line). Separately, Cowork found that every workbook record fails the same seven gate checks by design.

## Job 1: the phrase count

In `content_gate.py`, for record type `workbook` only: count, in the Body, every occurrence of "in Achology's view", "in Achology's teaching", "as Achology teaches it", "in Achology's reading", "as Achology sees it" and "Achology teaches that", case-insensitive. One passes; two or more FAIL, printing each sentence. Add the matching line to `content_gate_standards.json`, dated S412 under section 15.2 item 2. Acceptance: one passes, two fails, an article with five is untouched.

## Job 2: the workbook exception

Enter a named workbook exception so the seven expected fails print as NOTE and a real fail shows. The seven, from Cowork's S410 report: `landing_page_body` and `whats_inside` (parked until the landing page run); landing page body present; the external link check (the two-destination rule, Part 17.6); keyword in exactly one teaching heading (the part headings are fixed by the build tool); the paragraph floor on the fixed-layout blocks; and the `author` key (a workbook names no author, DSRD 2 section 3.4; `reviewed_by` is Kain Ramsay). The Reflect lead-in and its numbered questions are fixed layout too and leave the paragraph line. Acceptance on the five proving records: each prints only real fails.

## OWED BACK

The two changes, their acceptance printouts, and the five records' gate results after.

*No em or en dashes in this file; checked before writing.*
