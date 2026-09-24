# RULING: the "actually" cap exempts a page's own focus keyword, wherever it repeats for density

**From:** Kain, via Claude Cowork's session, S382, Wednesday 23 September 2026, carried to Code by Claude Chat. **To:** Claude Code.
**Answers:** the gate-fix `RULING__Kain_Ruled_The_Actually_In_Keyword_Exemption_Directly_With_Cowork_S382` asked for (FROM Cowork), and closes the keyword-conflict flagged on `does-cbt-actually-work`, the life-coaching-course-actually-teach record, and Q07010.

## The ruling, Kain's own words

"Actually inside the keyword itself doesn't count toward the cap, wherever it repeats for density. Actually used anywhere else in the body still counts, still capped at once."

Written into `house-copy-standards` (handed to Kain for re-upload, this session).

## What to build

`content_gate.py`'s `'actually' at most once` check (`n_actually <= 1`) excludes every occurrence of "actually" that is part of a verbatim match of the record's own `rm_focus_keyword`, however many times the keyword repeats. Only occurrences of "actually" outside those matches count toward the cap of 1.

## Where this applies now, once built

- `Q07010__what-a-life-coach-actually-does`: both occurrences are the keyword phrase. Passes clean once built; no page edit needed, per Cowork's own check.
- `does-cbt-actually-work` and the life-coaching-course-actually-teach record: not yet re-checked against this ruling; whoever opens them next confirms which of their "actually" instances are the keyword phrase itself before re-gating.

## OWED BACK

The gate fix, and confirmation of the acceptance case (a record whose keyword contains "actually," repeated for density, passing; a stray "actually" outside the keyword phrase still failing at 2).

*No em or en dashes in this file; checked before writing.*
