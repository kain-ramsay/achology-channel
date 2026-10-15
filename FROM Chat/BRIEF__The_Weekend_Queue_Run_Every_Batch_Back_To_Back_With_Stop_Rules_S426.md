> CODE DISPOSITION, S169: WAITS ON the first API batch's COST_REPORT being filed, then the new types' dry runs being read by Chat (this brief starts after both); the queue mode is not built yet.

First line of need: Code, factory session, straight after BRIEF__API_Worker_Takes_Help_Answers_And_Quote_Pages_Short_Reading_Lists_Quiet_Gate_S426: give the worker a queue mode that runs Chat's 33 queued batches back to back over the weekend, under three stop rules and Kain's total money cap.

# BRIEF: the weekend queue (Chat, Session 426, Thursday 15 October 2026)

**Why (Kain, S426).** Kain approved all three phases of `Launch Content Planning/PLAN__Clearing_The_Knowledge_Hub_Backlog_On_The_API_Worker_S426.md`, Help answers included, and wants the whole backlog drafted, checked and ready to sign when he is back on Monday morning. Nothing should wait for a Chat session to start the next batch.

## What is lined up
`api_worker/batches/queue_S426/` holds 33 batch files, `Q001` to `Q033`, in the order they run, 1,232 records in all. Each file's head names its phase, type, pack and subjects. Signed, superseded, check and lane files are left out, and so are the two batches already named (`first_batch.txt`, running; `second_batch_psychology_S426.txt`, the 33 psychology articles, which runs first, before Q001).

| Phase | Type | Records | Batches | Runs when |
|---|---|---|---|---|
| 1 | field authority (second batch, then Q001 and Q002) | 33 + 57 | 3 | the paragraph line is fixed |
| 1 | hub question articles | 58 | 2 | its dry run reads well |
| 1 | hub guides | 28 | 1 | its dry run reads well |
| 1 | instructor and elder articles | 139 | 4 | the type is added (PACK_01, same as field authority) |
| 1 | Seven Beliefs parts | 9 | 1 | the type is added |
| 2 | quote pages | 415 | 9 | its dry run reads well |
| 2 | Help answers | 324 | 8 | its dry run reads well |
| 3 | book notes | 150 | 4 | Kain signs PACK_02 (Lane B's proof is running) |
| none | author biographies | 0 | 0 | moved to Lane C at S426 (Kain: use this week's plan allowance); their two batch files are in `queue_S426/moved_to_lanes/` and the queue skips that folder |

## The queue mode
1. `--queue <folder>` runs every batch file in name order, one after another, without anyone starting the next.
2. A batch whose type is not yet enabled is skipped and logged, never guessed at; the queue moves on and comes back to it on the next pass.
3. Each finished batch writes its COST_REPORT and a one-line entry in `queue_S426/QUEUE_LOG.md`: batch, records, ready, `needs_chat`, refused, dollars, running total.

## The three stop rules (the queue stops itself and says why in QUEUE_LOG.md)
1. More than a quarter of a batch ends `needs_chat` after four rounds.
2. The running total reaches Kain's cap (set at the top of `api_worker.py`; Chat will put his figure in a one-line note).
3. A file named `STOP` appears in `queue_S426/`.

## What stays as it is
Rule 12 (Sonnet 5.5 writes and checks); batch mode; output to staging only; never a signed record or one with uncommitted changes; the free checks before the paid checker. Nothing is imported until Kain has signed it; the queue makes drafts ready to sign, not pages.

## Starting it
Start the queue on the iMac 4 when the dry runs are read, and leave it running. Tell Chat in one line that it has started.

OWED BACK: the queue mode with a test (three dummy batches: one runs, one is skipped, one trips stop rule 1); a one-line DONE when the queue is running.

*No em or en dashes in this file; checked before writing.*
