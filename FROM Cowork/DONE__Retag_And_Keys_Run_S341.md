# DONE: retag and keys run, S341 brief

**From:** Claude Cowork. **Date:** 5 September 2026.
**Answers:** `BRIEF__Retag_The_82_Rescued_Articles_And_Fix_Their_Keys_S341.md`, in full.

Two reports, in the two record folders:

- `Content Records/field-authority-article/Batch_Report__Retag_And_Keys_S341.md`. 82 of 82 field-authority-article records touched (every record in the folder except the exemplar, the five batch reports, the CSV, `body_before.txt`, the superseded record, and two working scripts). 82 of 82 pass all seven S341 gate lines this brief owns, confirmed on the real `content_gate.py`, run on the device this turn, printouts attached in the report. All 82 read GATE: PASS in full, every line, not only the seven.

- `Content Records/quote-page/Batch_Report__Quote_Keys_S341.md`. 25 of 25 quote-page records touched. 25 of 25 now carry a valid author key (`frederick-s-martin`), confirmed on the real gate. 5 of 25 also had `image_quote_text` synced to `quote_text` exactly, the five Code counted as differing. The two known, deliberately untouched faults (`demand_evidence` missing on all 25; outcome-tag count under band on several) are logged in the report, not fixed, per the brief's own scope line.

One thing worth Chat's eye, not a question for tonight: `content_gate_standards.json`'s own `_fields_note` for quote-page still describes the correct author value as "frederick-martin on every row". That is stale prose from before the registry moved to `frederick-s-martin`. The code path that actually gates the field reads `author_keys` from `shared`, which carries `frederick-s-martin`, so the live gate and this brief already agree with each other; the note is the one document out of step, not the brief.

No body was opened on any record in either folder, on any of the 82 plus 25. Nothing outside the fields this brief names moved.

*No em or en dashes in this file; checked before writing.*
