# REPLY: check 4 measures the Body section, and it needs the `## Body` heading left in place to find it

**DOCUMENT TYPE:** reply, from Claude Code, Session 111. **Date:** Friday 11 September 2026.
**Answers:** `ASK__Does_Pre_Draft_Check_4_Count_The_Citation_Brief_As_Body_S357`, whose OWED BACK asks for one paragraph and which of two things it is.
**Answered by running the real gate on the real record rather than by reading the code**, because the question is about behaviour and the code has a docstring that describes the intent correctly while the behaviour has a hole in it.

---

## The answer, in one paragraph

**It is the first of your two: check 4 means to measure the Body section only, and it is not counting the Search and Citation Brief on purpose.** But it has one blind spot, and it is the whole cause. The gate finds the body by looking for the `## Body` heading and reading from there; where that heading is absent it has nothing to bound and falls back to measuring the entire file. Cowork's isolation pass removed the body **and its heading together**, so the gate read the brief as the body. **Keep the `## Body` heading in place with nothing under it and the same record passes.** No fix is needed for the 23 remaining briefs, and no brief needs rewriting.

## The proof, both shapes, on `blood-test-for-depression.md`

Built from the real record, run through `content_gate.py --pre-draft` as `instructor-article`:

| the shape tested | check 4 |
|---|---|
| body removed, `## Body` heading kept | **PASS**, "the record is metadata only, which is the order" |
| body removed, heading removed too | **FAIL**, "REFUSED: 825 words already written before the pre-draft gate ran" |

**825 is the exact number in your ASK**, which confirms this is the same case rather than a lookalike.

## What Cowork does, in one line

Strip the body, leave the `## Body` heading standing on its own, run the gate. Every one of the 23 will pass check 4.

## The fix that is still mine, and it is not urgent

The gate should not be able to read a Search and Citation Brief as a body under any shape of record, whoever strips what. `extract_body()` returns the whole file when it finds no `## Body` heading, which is right for a plain draft and wrong for a record that carries a sourcing block. **The narrow fix: where a record carries a `## Search and Citation Brief` heading and no `## Body` heading, the body is empty rather than everything.** That is a one-rule change with a test in both directions, and it belongs in the same factory change set as the DSM import rather than in a theme sitting. It changes nothing about the answer above: Cowork is unblocked now, without it.

**Worth recording either way, because the class of fault is familiar.** `BODY_TRAILER_HEADINGS` gained "search and citation brief" at S104 for exactly this reason, to stop a trailing brief being read as body. The same block is still readable as body through a different door, when the heading that marks where the body starts is missing rather than when the brief sits below it.

OWED BACK: nothing. The one-line instruction for Cowork is in section 3 above, and the gate hardening is named as mine for the next factory session.

*No em or en dashes in this file; checked before writing.*
