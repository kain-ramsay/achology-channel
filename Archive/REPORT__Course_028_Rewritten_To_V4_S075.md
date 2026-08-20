# REPORT: course 028 rewritten to V4. Course one of the S294 commission. Kain's read owed before course two starts.

**From:** Claude Code, Session 075. **Date:** 20 August 2026.
**Answers:** `COMMISSION__Rewrite_All_2146_Standardised_Descriptions_To_V4_S294.md`, course one of the run.
**Read against:** `The_Standardisation_Rule_Set.md` V4, in full, in the Course + Lesson Data | MASTER folder.

---

## What happened, in one line

The eight courses written at S074 (028, 027, 011, 023, 022, 025, 026, 002) were built to an ad hoc rule Code invented, not to V4. Course 028's fifty rows are now rewritten to V4 and mechanically gated clean. The other seven S074 courses, and the twenty never touched, are unstarted and wait on this read.

## Rows written, word count range

**50 of 50.** Word counts run from 144 to 200, median 173. No ceiling was applied, per V4; the range is simply what the rewrite produced.

## The gate, rebuilt for V4

The S074 gate (`desc_audit_v4.py`) enforced the wrong rules: a 150 to 210 word floor V4 does not set, and a "covers" test that specifically wanted a teacher's name, which V4 forbids outright. It is retired. A new gate, `desc_gate_v4.py`, checks: four parts, a question mark on part one, no long dash, no title repeat inside the description, no Tier 1 banned term, no teacher named, full name given before a known short form, no duplicate description or question line across the library.

**Proved refusing before it was trusted**, per house standard: run against the pre-rewrite (S074-shape) rows, it caught 62 faults, 58 of them teacher names. Run against the V4 rewrite, it caught one real fault (`journey`, a banned term, in row 004) which was fixed. Course 028 now gates at zero.

## Rows flagged, by Lesson Key, with reason

**Two, both the same open question in V4, on two different shapes of it.**

- **028-001.** Course 028 is co-presented by two people. V4 says the teacher is never named and separately says a named guest, interviewee or case subject is named in full, and states plainly that whether a co-presenter counts as the first or the second has not been ruled by you directly. This is the first row it bites on. Written on the conservative reading: both presenters are treated as the teacher, and neither is named.
- **028-038.** The interview lesson, currently titled "An Interview with Kain: The Heart of Entrepreneurship". The interview subject is also the course's own teacher, which is a second and distinct shape of the same open question. Written on the same conservative reading: not named, even though the lesson is literally about his own experience.

Both are marked in amber on the five-row reading page. If either should have been named, the fix is a rewrite of one row plus every other row across the library where the same shape recurs, so it is worth ruling now rather than after more courses carry the same default.

## Tier 1 terms caught and removed

**One.** "Journey" in row 004, in the sentence about an entrepreneur's own experience. Removed.

## What comes back, per the commission

**Five full rows, chosen across the course, original and new side by side**, opened in Safari at `course_028_five_rows_v4.html`: 028-001 (welcome, carries the first flag), 028-012 (Ikigai, mid-course), 028-025 (the Maslow row, full name now given at first mention), 028-038 (the interview row, carries the second flag), 028-049 (the closing lecture, whose closing line now names the finite/infinite game rather than only thanking you for finishing).

## What is not yet touched

Course 028's fifty are not yet pushed to Vimeo a second time; that waits for the one sweep at the end of the whole run, unchanged from the standing instruction. The other seven S074 courses (027, 011, 023, 022, 025, 026, 002) are unstarted. The twenty never touched are unstarted.

## What this needs back

**Your read of the five rows, and a ruling on the co-presenter and interview-subject question**, since it will recur on 027 (Karen) and 011 (Gerard/Gerry) if it is not settled now. Course two does not start until both are in.

*No em or en dashes in this file; checked before writing.*
