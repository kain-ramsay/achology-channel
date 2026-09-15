# BRIEF: patch the paragraph-rhythm check to Kain's S357 ruling, then re-run the 77 failing records before anyone rewrites one

**Filed by Claude Chat, Session 361. Date:** 15 September 2026. Ruled on the strength of Kain's S357 ruling, already given and already in the JSON; this is the code catching up, not a new standard.
**Source:** `ASK__Content_Gate_Does_Not_Implement_The_S357_Paragraph_Floor_Ruling_S360.md`, FROM Cowork, Monday 14 September, read this session.

---

## The defect, as Cowork read it from the file

`content_gate_standards.json` carries Kain's S357 ruling: `paragraph_sentences: [3, 4]`, `paragraph_floor_words: 50`, `single_sentence_paragraph: "once_per_section"`, `short_paragraph_allowance_per_section: 1`. `content_gate.py`'s paragraph-rhythm check reads only the first key; `single_ok` tests for the literal "allowed", which the JSON no longer sets, so it is always false; `paragraph_floor_words` and `short_paragraph_allowance_per_section` are read nowhere. So the deployed gate enforces "every paragraph exactly 3 to 4 sentences, no exceptions", which is the pre-S357 rule.

## The commission

1. Patch the paragraph-rhythm check to implement the JSON as written: a paragraph passes on 3 to 4 sentences OR on 50 words or more; one paragraph per section may fall below both; a second short paragraph in the same section fails. Read every value from the JSON, hardcode nothing. Add acceptance cases to `content_gate_acceptance.py` for each branch (the word-floor pass, the once-per-section allowance, the second short paragraph failing) and confirm the suite passes whole.
2. Re-run `content_gate.py` on: the 50 unpublished book note records, I04, I14, I18, and the 24 DSM records. Report per set: how many now pass, how many still fail and on what line.
3. Everything that passes: run its route. Book notes through `tools/book_note_import.py` and `publish_gate.py` clearance, publish. I04, I14, I18 pushed and their finish pass re-run. The 24 DSM records still wait on Cowork's `featured_image` and sourcing work only if they fail on other lines; if they pass, import as drafts under `BRIEF S357`, publish nothing.
4. One DONE line per set to TO Chat with the counts.

Cowork is told this turn to hold Jobs 3 and 4 until your counts land, and to fix only what still fails after the patch.

*No em or en dashes in this file; checked before writing.*
