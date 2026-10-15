> CODE DISPOSITION, S169: WAITS ON the rerun of the 16 finishing and its COST_REPORT being filed (the worker is being rebuilt to this design now; the report will be TO Chat/DONE__One_Pass_Rerun_S169.md).

First line of need: Code, factory session, FIRST before anything else in the S426 group: rebuild the API worker as one writing pass plus a fact check, then rerun the first 16 articles that way and stop. This replaces the writer and checker rounds in every S426 brief.

# RULING: the worker becomes one pass and a fact check (Chat, Session 426, Thursday 15 October 2026; Kain's yes: "if there is some way of simplifying this work, yes, 100%")

## Why
The first batch: $4.53, 16 articles, none passed. Chat read the checks. Whatever the round, the per-paragraph checker found 8 to 25 small "not met" points on an article of about 30 paragraphs. More rounds did not lower that number (Ainsworth went from 31 to 10, but split brain went from 8 to 26 and the visual cliff from 4 to 10), and changed facts appeared in every round. The rounds cost money and churned the text without bringing it closer to finished. Meanwhile Chat's five author biographies, one Sonnet pass checked only for fidelity and then read, were signed by Kain as "brilliant". Chat read the Zimbardo output in full: the writing is good. The fault was in the design, not the writer.

## The new design, for every type
1. **One writing pass.** The writer prompt, reading list, model (Sonnet 5.5, effort high) and pack are as now, with the paragraph line fixed (120 words is a target, never clip a thought). No second writing round.
2. **Free checks (script, no API cost).** Every heading, link (text and address), quotation, field and fixed line must be identical to the original record. Then run the gate. Only these lines block: dashes, the always-banned words, banned link labels, a changed heading, link or quote. Every other gate line prints as a NOTE into FAILS_LOG.csv for Kain's Friday ruling. The four known lines never block.
3. **One fact check (Sonnet 5.5, effort medium; a fresh call that never saw the writer).** It reads the original record (with its Sourcing record and Search and Citation Brief) and the new Body, and answers one question only: "List every sentence in the new Body that states a fact, figure, name, date, place, cause or claim that the original record does not support, or that changes one it does." It returns JSON: the sentence copied exactly, what is unsupported, and the original sentence it came from (or "new"). No style points, no moves.
4. **Repair without rewriting.** Each sentence it names is replaced by the matching original sentence, or deleted where it was new. That is done by script, never by another writing call. Log every repair.
5. **Result:** "ready" when the free checks pass. The record goes to `out/` with its repairs listed at the foot. "needs_chat" only when a free check still fails after repair, or more than 5 sentences needed repair.
6. **Quality is judged by reading.** Chat reads five pages a batch, whole, against the signed examples; Kain signs the batch list.

## The weekend queue's stop rule 1 changes to:
The queue stops itself when more than a quarter of a batch ends "needs_chat". The other two stop rules, the $200 cap and the STOP file, stand.

## First: the rerun of the 16
Rebuild the worker, then rerun `first_batch.txt` (the same 16) the new way, cap $5, and stop. File one DONE with the COST_REPORT, the repairs per article, and the FAILS_LOG. Chat reads all 16 tonight against batch 1 and the signed examples before the queue starts. Then the S426 briefs follow in their order, all built on this design: the types, the dry runs (one pass each), the queue.

## What stays
Rule 12: Sonnet 5.5, never a bigger model. Staging only; never a signed record. Nothing imported until Kain signs.

OWED BACK: the rebuilt worker with a test (a planted invented sentence is repaired; a planted changed link fails); the rerun's DONE.

*No em or en dashes in this file; checked before writing.*
