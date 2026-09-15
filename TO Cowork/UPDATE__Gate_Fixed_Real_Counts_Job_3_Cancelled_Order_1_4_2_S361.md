# UPDATE: the gate is fixed and the real counts are in. Job 3 is cancelled, Job 4 is 42 records, Job 2 stands. Order: 1, 4, 2.

**Filed by Claude Chat, Session 361. Date:** 15 September 2026. Supersedes the HOLD and PRIORITY notes in this folder; read this one.

Code patched `content_gate.py` to Kain's S357 ruling (commit ed16460, 106 acceptance cases pass) and re-measured everything.

- **Job 3 (I04, I14, I18): cancelled.** All three pass whole under the real rule. Do not touch them.
- **Job 1 (strip `featured_image` from the 200 CQ018 records): unchanged, do it first.**
- **Job 4 (unpublished book notes): now 42 records, not 50.** Nine pass and are importing. Of the 42: 30 still fail paragraph rhythm under the real rule (genuinely short paragraphs beyond the one-per-section allowance), 28 carry "plainly" (swap for "simply"), 9 fail outcome-or-problem tag count, 4 fail reading ease, 4 fail body word count, 1 the keyword in the first 10 per cent, 1 the external source link. Run `content_gate.py` on each to get its own lines; fix only what it names; no rewording beyond that. Report 42 of 42 passing with the path.
- **Job 2 (24 DSM records): stands.** All 24 fail the paragraph floor for real, 20 to 30 short paragraphs each against one allowed per section. Rewrite to the floor, carry the sourcing register in the brief, report 24 of 24.

One DONE line per job to FROM Cowork. Code imports each set as it lands.

*No em or en dashes in this file; checked before writing.*
