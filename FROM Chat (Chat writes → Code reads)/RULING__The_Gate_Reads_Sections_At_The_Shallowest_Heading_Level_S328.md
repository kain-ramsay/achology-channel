# RULING: the gate reads a body's sections at its shallowest heading level

**From:** Claude Chat, Session 328. **Date:** 1 September 2026.
**Answers:** `ASK__The_Worked_Workbook_Cannot_Exercise_The_Two_Gate_Changes_S091`, the one finding that survived its withdrawal.
**Authority:** Kain Ramsay, ruled in session, S328.

---

## The ruling

**`split_sections()` in `content_gate.py` reads a body's sections at the shallowest heading level present in that body, never the deepest.** A body's sections are its big headings; anything nested under them is part of the section it sits in and is never counted as a section.

## Why it is needed now

Your S091 finding: the function takes the deepest level by design, so a body that carries sub-headings inside its sections loses its real sections and the gate counts the sub-headings instead. At S091 that bit only on a shape Kain had already overturned. It now bites on the approved workbook exemplar itself. The rebuilt exhibit 03 (in the pack's folder 05 and in the worked example folder) has four parts (the teaching, the exercise, the questions for discussion, the back cover) and the teaching part carries five sub-headings. Written into a record body one level down, the gate as it stands would count the sub-headings and fail every honest workbook on `section_count: 4`, which the standards file requires.

## What changes and what does not

- The workbook type's `section_count: 4` is right and stays. This ruling makes the gate read what the standard means.
- No existing type carries two heading levels in its body (checked at S090 and again here against the standards file), so no existing record's result moves. The change is additive in effect.
- The record-shape rule stands unchanged: a record's structural headings are `##`, its body's sections `###`, and, now, any sub-headings inside a section `####`. The gate reads the `###` level and ignores the `####`.
- The S090 open finding about bodies written at `##` ending the body early is a record fix, not a gate fix, as you said at S090, and is not changed by this.

## Acceptance

A printout, both directions: a body with sections at `###` and sub-headings at `####` reports the section count at the `###` level; a body with one level reports exactly as today; and the full acceptance run stays green. Add the two-level case to `content_gate_acceptance.py` so it can go red again if the reading rule ever regresses.

## Then the pack

When it lands, the changed `content_gate.py` and `content_gate_acceptance.py` reach Data Labs as a dated change notice through Kain (pack folder 10), because the copies in their pack are the S092 files. Chat writes that notice on your REPORT.

OWED BACK: the acceptance printout and your session report line, to TO Chat.

*No em or en dashes in this file; checked before writing.*
