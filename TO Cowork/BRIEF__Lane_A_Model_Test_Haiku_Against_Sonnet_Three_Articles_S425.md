First line of need: Lane A, a model test before any volume: three field authority articles each written twice, once by a Haiku 5.5 writer and once by a Sonnet 5.5 writer, every version checked by a Sonnet 5.5 checker, with the allowance used and the rounds counted. Outputs go to a test folder, never into the records. Kain's yes, Session 425.

# BRIEF: which model writes and which checks (Chat, Session 425, Thursday 15 October 2026)

**Why.** Kain signed PACK_01 (version 1.0) today. Before about 350 articles go through it, Kain wants to know the right model for the job on evidence, not reputation. All seven proofs used Opus to write and check. This test asks whether Haiku 5.5 or Sonnet 5.5 can write to the pack, and whether Sonnet 5.5 can check, at what cost.

**Read from the vault first:** none needed beyond the pack.

**Read first, whole (every writer and checker agent reads these too):** `Content Type Packs/PACK_01__Articles/00. Start Here.md`, `06. How Kain Writes (the moves).md` (signed 1.0), `05. Gold Examples.md`, and the gold example for this kind: `Content Records/field-authority-article/learned-helplessness-experiment-the-psychology-of-helplessness.md` (signed by Kain). Never copy a sentence, scene or device from a gold example.

**The three articles** (field authority, psychology, not signed, about 1,700 to 1,830 words each), in `Content Records/field-authority-article/`:
1. `the-dynamics-of-cognitive-dissonance.md`
2. `unraveling-apathy-insights-from-the-bystander-effect-study.md`
3. `mimicking-aggression-insights-from-the-bobo-doll-experiment.md`

**Never write into these records.** Copy each into a new folder, `PROOF__Ten_Articles_S423/model_test_S425/`, twice: `{name}__HAIKU.md` and `{name}__SONNET.md`. All work happens on the copies.

**How, for each of the six copies.**
1. **Writer:** a fresh agent with `model: haiku` for the HAIKU copies and `model: sonnet` for the SONNET copies. It rewrites the body through all twelve moves, keeping every fact, figure, source, link, heading and field, adding no fact, no em or en dashes, within the length band (file 06, Move 8).
2. **Checker:** a fresh agent with `model: sonnet` for every copy, never the writer. One line per paragraph per move, met or not met with the phrase; the Move 10 list of paragraph endings; teaching words against the band. Save as `model_test_S425/{name}__{MODEL}_check_N.md`.
3. Every "not met" goes back to a writer of the same model; up to four rounds. If it still misses after four, stop that copy and say which moves.
4. Run `content_gate.py` on each finished copy.

**Count, for every agent you start:** its model, which copy, writer or checker, which round, and the tokens and time it reports when it finishes. Also read `/usage` before you start and after you finish, and write both down.

**Report.** One file in FROM Cowork, `LANE_A__DONE__Model_Test_Haiku_Against_Sonnet_S425.md`, with:
- A table per copy: rounds taken, moves still missed at the end, final gate result, teaching words.
- A table of every agent: model, role, round, tokens, time.
- Totals: tokens for the three HAIKU copies and for the three SONNET copies, writing and checking shown apart; `/usage` before and after.
- Anything a writer got wrong that a checker missed, if you noticed it.
Do not say which model is better; Chat compares the six copies against the gold example and brings Kain the answer. Then stop.

OWED BACK: the DONE file above.

*No em or en dashes in this file; checked before writing.*
