# REPORT: the standing context, measured. Act 1 of the S257 commission.

**DOCUMENT TYPE:** report with a measured table. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Delivers:** Act 1 of `COMMISSION__Count_The_Standing_Context_And_Run_The_Prompt_Audit_S257.md`: "count the standing context, measured rather than estimated."
**Repeatable:** `tools/standing_context.py` in the theme. The table below is its output, not a transcription of it, and it can be re-run whenever the documents change.

---

## How it was measured, and the one caveat

Counted with `tiktoken`'s `cl100k_base`, a real byte-pair tokeniser installed on this Mac for the job. **It is not Claude's tokeniser**, which is not available offline. On English prose and markdown the two agree closely, usually within about a tenth, and both are far nearer the truth than dividing characters by four.

So: every figure is measured with a real tokeniser, and is a close proxy rather than an exact Claude count. Saying so matters, because this commission exists to replace an estimate, and quietly swapping one estimate for a different one would defeat it.

## The finding that reframes the question

**Three different things have all been called "standing context", and they cost completely different amounts.** Adding them together is how a manageable cost gets reported as an emergency, or the reverse.

| | Tokens | What it means |
|---|---|---|
| **Every turn** | **5,280** | Re-sent with every single message of a session |
| **Once a session** | **25,461** | Injected at the open, then carried in history |
| **On demand** | **253,482** | Read only when a turn actually opens the file |

**Code's real per-message overhead is 5,280 tokens.** That is the number that multiplies by every exchange, and it is small. The ranked fix list at S052 concluded that Code's standing harness should be left alone, and this measurement supports that conclusion rather than overturning it.

## Every turn, in full

| File | Tokens | Characters |
|---|---|---|
| `MEMORY.md`, the memory index | 3,464 | 13,416 |
| `CLAUDE.md`, the project instructions | 1,816 | 8,267 |
| **Total** | **5,280** | |

**The memory index is now the larger of the two, and it is the only item here that is pure accumulation.** It carries 47 entries and grows every session, while `CLAUDE.md` was rewritten down at S257 and is stable. The S257 commission already left the index to Code without needing a commission, and at 3,464 tokens a turn it is worth a prune: perhaps a third of the entries describe work that is finished and closed rather than a standing rule.

## Once a session

| Group | Files | Tokens |
|---|---|---|
| The Harness | 1 | 7,860 |
| The channel, every live file read under Rule 1 | 19 | 17,601 |
| **Total** | | **25,461** |

**The channel now costs more than twice the Harness at every session open, and nobody has been watching it.** This is the actionable finding of Act 1.

The Harness is a fixed 7,860 tokens. The channel is 17,601 and **grows with every file left unarchived**. Rule 1 requires every live file to be read in full at the open, so an unarchived consumed instruction is not merely untidy bookkeeping: it is a real, repeating cost paid at the start of every future session until somebody moves it.

Two examples from today's 19: `RULING__Component_Data_Gate_Block_Shape_S276.md` is 2,331 tokens and is now consumed; `REPLY__Four_Reports_Answered_And_What_Is_Settled_S274.md` is 1,778 and is consumed. **Archiving what this session finished removes several thousand tokens from every session that follows.** That is Rule 13's job, and the measurement shows Rule 13 is not only about tidiness.

## On demand, and the S052 estimate settled

| Group | Files | Tokens |
|---|---|---|
| The live DSRD set | 13 | 222,049 |
| Memory notes, individually | 47 | 31,433 |
| **Total** | | **253,482** |

**The S052 estimate of 214,000 for the DSRD set was good: measured, it is 222,049, about four percent higher.** The estimate can be retired and the measured figure used from here.

The four heaviest documents carry more than half of it:

| DSRD | Tokens |
|---|---|
| DSRD 8, Component Library | 39,552 |
| DSRD 2, Content Production and Knowledge Standards | 32,248 |
| DSRD 9, Page Layout Specs | 31,930 |
| DSRD 7, Design Foundations | 25,139 |

**And here is the part Chat needs, because it changes whose problem this is.** None of the 222,049 rides on a Code turn. Code opens a DSRD only when a turn needs it, reads the section, and quotes it. The number matters to **Chat**, which holds these as project attachments, and that is exactly the loading question the S257 commission reserved to Chat: "one session held inside the project against one with only the relevant documents attached."

**So the baseline for Chat's test is 222,049 tokens of DSRD, plus whatever else the project carries.** If claude.ai assembles the full attachment set into every conversation, that is the emergency; if it retrieves selectively, it is an inefficiency. Code cannot see which, and this figure is the number the test should be run against.

## What is NOT in the table, and why

**Skill bodies.** What rides on a turn is each skill's name and one-line description, not its body; a body loads only when the skill is invoked. Only two skills exist as files on this Mac (`caveman` at 484 tokens, `ui-ux-pro-max` at 10,576), and the rest arrive as a listing from the plugin registry rather than as readable files. So the on-demand cost of a skill is measurable only for those two, and the standing cost is the listing, which is a small fraction of the bodies.

`ui-ux-pro-max` at 10,576 tokens is worth naming: invoking it costs twice the Harness. It has never been used in this project, and it is a general-purpose UI library whose advice is not Achology's design system. **Recommend it is removed from this project's skill set**, so it cannot be invoked by accident on a project whose design standards are the DSRDs. That is a proposal, not an action.

**The tool schemas and the system prompt.** Genuinely unmeasurable from inside: I cannot read my own prompt, and guessing at it would be exactly the estimate this commission replaces. Named as a hole rather than filled with a number.

## Three recommendations, all Kain's or Chat's to take

1. **Archive what this session consumed** (Code's, doing it at this close). Several thousand tokens off every future session open.
2. **Prune the memory index** (Code's, already left to Code by S257). It is the largest every-turn item and the only accumulating one.
3. **Run Chat's loading test against 222,049** as the DSRD baseline (Chat's). It is the one number here that could indicate a real problem, and only Chat can see whether it does.

## Act 2

Not started. The prompt audit over the Harness and the skills is a separate piece of work of real size, and the commission's own instruction applies: "If either act turns out to be larger than it looked, say so and file what you have rather than running it to completion silently."

Act 1 is complete and filed. Act 2 is next, and it will arrive as proposals with confidences, applying nothing, exactly as commissioned.

*No em or en dashes in this file; checked before writing.*
