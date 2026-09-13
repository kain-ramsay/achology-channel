> **CODE DISPOSITION, S113: WAITS ON the check existing in `content_gate.py` and the count being run.** Arrived mid-session and read in full the turn H6 named it, before the next edit. Nothing in it cancels the work in hand. Its four `shared` keys are already in `content_gate_standards.json`, written by Chat this session; `content_gate.py` does not yet read them, so the gate silently passes bodies this brief means to fail. One note for Chat, found while this session re-gated the 51 author biography records: that re-gate ran against the standards file as it stood, so its stored printouts do not carry the paragraph floor and will move again when the check lands. **Testable: archived when `content_gate.py` fails a body carrying two short paragraphs in one section, and the session report carrying the two totals and the per-record table exists in TO Chat.**

# BRIEF: build the paragraph floor into the gate, measure every article, book note and quote page, and report the count before anything is rewritten

**DOCUMENT TYPE:** brief, from Claude Chat, Session 357. **Date:** Sunday 13 September 2026.
**Authority:** Kain, live in Chat, on the live article "What Is Bandura's Social Learning Theory?", whose opening ran five paragraphs of one to three sentences: "It is simply unacceptable ... whatever already published articles must get reworked to meet this standard." Signed here by Chat.
**Session type:** factory. A gate change and a measurement; no theme change and no body changed.
**Read this cold.**

---

## 1. The standard, already written home

The Achology Base Voice item 8 (vault) and DSRD 2 section 3.0 now carry it, and `content_gate_standards.json` `shared` carries the values: on every article type, every book note and every quote page, a paragraph is **at least three sentences or at least 50 words**, whichever it reaches first; the top of the band stays four sentences. A paragraph below both floors is a short paragraph; **one is allowed per section**, counting each headed section and the unheaded opening separately; a second in the same section fails. List items are not paragraphs. The help-answer type is excluded and keeps its S356 ceiling.

## 2. The work

1. **Build the check in `content_gate.py`**, reading the four new `shared` keys (`paragraph_sentences` now `[3, 4]`, `paragraph_floor_words`, `single_sentence_paragraph`, `short_paragraph_allowance_per_section`). Print, on every run, the count of short paragraphs per section and the worst section. Fail on a second short paragraph in one section. Leave the help-answer type on its own override.
2. **Measure before anyone rewrites.** Run the gate with the new line across every record in `Content Records/` of the governed types (every article type, `book-note`, `quote-page`, including the 250 quote records and the 24 DSM articles waiting for import), and across every published page of those types read off the install. Report, worst first: how many fail, how many short paragraphs each carries, and which sections. A table, in your session report to TO Chat, with the two totals (records failing; published pages failing) in its first line.
3. **Do not rewrite anything.** The rewrite is Cowork's, at the record, on a brief Chat writes from your count; you then push the corrected bodies to the published pages and re-score them. This brief ends at the count.

## 3. Acceptance criteria

The gate fails a body carrying two short paragraphs in one section and passes one carrying one. The report carries the two totals and the per-record table. No body changed.

## 4. What this brief does not authorise

Editing any record or any live body. Changing the help-answer standard. Treating the count as the fix.

OWED BACK: the session report with the two totals and the table.

*No em or en dashes in this file; checked before writing.*
