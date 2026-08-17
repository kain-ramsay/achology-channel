# NOTE: where the tokens are going, and the disciplines that stop it

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Commissioned by Kain in session:** "Chat is burning through Fable tokens
unusually fast. Research, and give him all of the checks and optimisation
disciplines he could embrace that will allow us to become more efficient with
our use of tokens, especially when using Fable 5."

**Sources.** Everything numbered in section 1 was read this turn from the
bundled Claude API reference (models and pricing, prompt caching, the prompt
audit method, and the Fable 5 migration guide), not from memory. Where a claim
depends on how the chat surface assembles context, which I cannot open and read,
I say so and mark it as yours to test rather than stating it as fact.

**One thing I could not check.** I have taken Kain's word that you are running
on Fable 5. I have no way to read which model a Chat session uses.

---

## 1. The four facts that set the economics

**Fable 5 costs $10 per million input tokens and $50 per million output.**
Output is five times the price of input, token for token. Every discipline below
follows from that one ratio.

**Thinking is always on and cannot be turned off.** On Fable 5 an explicit
`thinking: {type: "disabled"}` is rejected outright. Depth is controlled only by
the effort level, `low` through `max`. Thinking tokens bill as output, at $50.

**Hiding the thinking does not save a penny.** The reference is explicit:
"`display` controls visibility only, thinking happens and is billed the same
under every setting." If anyone has been collapsing or suppressing the thinking
summary as an economy, it saves nothing. Worth killing that idea before it
spreads.

**The context window is 1M by default and 1M is also the maximum.** There is no
smaller setting to choose. The only lever is what you put in it.

**And the comparison that matters:** Claude Opus 5 is $5 in and $25 out. Fable 5
is exactly twice the price of Opus 5 on both sides. That is the single largest
lever in this whole note and it is not a discipline, it is a decision, and the
decision is Kain's. I have raised it with him separately.

---

## 2. Where the tokens actually go, in order of size

### 2.1 The standing context is a tax on every single turn

This is my primary suspicion for "unusually fast", and it is the one this
project has already diagnosed in another form.

Every turn of a conversation re-reads the whole standing context: the harness,
the skills that are loaded, the project knowledge, and the entire conversation
so far. A body of standing text is not paid for once. It is paid for again on
turn two, and again on turn forty.

The Harness says it about itself, at version 2.7:

> "Across 252 sessions that instruction, sitting in three harnesses at once,
> produced a one-way accumulation until satisfying the obligations had become
> the work."

That was written about obligations. It is equally true of tokens. Standing
context in this project has grown by design for 250 sessions, and nothing has
ever measured what a turn now costs before any work happens.

**The check, and it is the first thing to do:** count the standing context. Word
count times roughly 1.35 gives a serviceable token estimate. Do it for the
harness, each loaded skill, and each project knowledge document, and put the
numbers in one table. That table is the per-turn tax, and until it exists every
other question here is guesswork. The prompt-audit method in the reference makes
the same point: without per-surface cost visibility, every other issue is
invisible.

### 2.2 Re-emitting a whole document to change part of it

Output is the $50 side, and this is where Chat spends output.

A 6,000 word document is roughly 8,100 tokens. Writing it out costs about
**$0.41**. Reading the same document as input costs about **$0.08**. So
re-emitting a DSRD whole, to change one section, costs five times what it costs
to read it, and you often pay both in the same turn.

Given that Chat owns and maintains the DSRD set, and that a DSRD revision is a
routine event, this is very likely the largest single line in the bill after the
standing context.

**The discipline:** deliver the changed section, not the changed document. Where
the surface allows a targeted edit rather than a rewrite, take it every time.
Where a document genuinely must go out whole, that is fine, but make it a
decision rather than a habit.

### 2.3 The correction round costs the whole conversation again

In a chat surface, a wrong first answer is not just wasted output. Fixing it
resends the entire conversation to that point, plus the wrong answer, plus the
correction. Deep into a long session that resend can dwarf the answer itself.

This reframes accuracy as an economy rather than only a quality standard, and it
is the strongest argument for the practice the reference recommends for Fable 5:

> "Claude Fable 5 performs better when it understands the intent behind a
> request. I'm working on [the larger task] for [who it's for]. They need [what
> the output enables]. With that in mind: [request]."

One extra sentence of intent up front is cheap. A correction round is not.

### 2.4 The conversation itself

Every turn carries every previous turn. A long session costs more per turn than
a short one, at every turn, without anything else changing.

**The discipline:** end conversations at natural boundaries and open a fresh one
with a tight brief, rather than carrying one thread across a whole body of work.
A fresh conversation with a good brief is dramatically cheaper than turn forty
of an old one, and on Fable 5 it is usually better as well, because the model
does its best work from a well specified single brief.

---

## 3. Fable 5 specific disciplines

### 3.1 Run routine work at lower effort

Straight from the migration guide:

> "Lower effort settings, including `low`, still perform very well on Claude
> Fable 5, often exceeding the `xhigh` or even `max` performance of previous
> models."

And the failure mode at the top of the range:

> "At higher effort on routine work, Claude Fable 5 can gather context and
> deliberate beyond what the task needs."

Reserve the high end for genuinely hard work. Filing a record, writing a ruling,
answering a settled question: these are not that. If the surface exposes no
effort control, this becomes a prompt-level instruction rather than a setting,
and the reference gives one for exactly this:

> "When you have enough information to act, act. Do not re-derive facts already
> established in the conversation, re-litigate a decision the user has already
> made, or narrate options you will not pursue."

### 3.2 Cut prescriptive scaffolding, which costs twice

This one is not a tradeoff, which makes it the best item in the note:

> "Prompts and skills written for prior models are often too prescriptive for
> Claude Fable 5 and reduce output quality."

Over-prescription costs input tokens to carry, costs output tokens as the model
works through it, and makes the answer worse. Cutting it saves money and
improves the result at the same time.

The audit targets, all named in the reference: step by step choreography for
judgment tasks, stacked emphasis (CRITICAL, MUST, NEVER, several to a
paragraph), restatements of things the model does by default ("be thorough", "do
not stop early"), prohibition lists, and the same rule stated in three
documents. The last one is this project's known weakness, and the harness
already has a rule against it for a different reason.

**What not to cut, because it matters:** context is never cruft. Who Kain is,
what Achology is, the quality bar, and the reasons behind constraints all earn
their place. This is not a length contest. The target is dated instruction, not
volume.

### 3.3 Give a verbosity instruction, because output is the expensive side

The reference offers this, and it is worth carrying as standing text:

> "Lead with the outcome. Your first sentence after finishing should answer
> 'what happened' or 'what did you find'. Being readable and being concise are
> different things, and readability matters more. The way to keep output short
> is to be selective about what you include, not to compress the writing into
> fragments, abbreviations, arrow chains, or jargon."

Note the second half. The saving comes from including less, not from writing
tersely. Kain reads these; compressed prose would cost him time to save us
pennies, which is the wrong trade.

### 3.4 Never show the model a remaining-token countdown

Specific and real:

> "In very long sessions it can worry about running out of context, suggesting a
> new session or trimming its own work, most often when the harness surfaces a
> remaining-token countdown. Avoid showing explicit context-budget counts."

If anything in the setup reports remaining budget into context, take it out. It
buys premature wrap-ups and truncated work.

### 3.5 Expect long turns and do not mistake them for a fault

> "Single requests on hard tasks can run many minutes at higher effort."

A fifteen minute turn on a genuinely hard task is normal on this model, not a
hang. Worth knowing before someone cancels and re-runs, which pays for the work
twice.

---

## 4. The prompt cache, and the part you will have to test

**What is certain, from the reference.** Prompt caching is a prefix match: any
byte that changes anywhere in the prefix invalidates everything after it. Cache
reads cost about a tenth of the input price. Fable 5's minimum cacheable prefix
is 512 tokens, the lowest of any current model, so almost anything standing is
long enough to cache.

**What follows, if the surface caches.** The stable part of your context should
be genuinely stable and should sit first, and the volatile part should sit last.
The named silent invalidators are worth reading in full, but the ones that could
plausibly bite here are: a current date or timestamp near the front of a
standing document, and editing project knowledge partway through a conversation.
Both change the prefix, and both make every turn after them pay full price for
everything.

**What I cannot tell you.** I have no way to read how claude.ai assembles a
conversation, whether it caches, or where project knowledge sits in the order.
So this is a hypothesis with a test attached rather than a finding, and the test
is yours: hold the project knowledge completely still through one working
session, then churn it mid-session in another, and see whether the cost per turn
moves. Do not take my word for the mechanism. I have only read the API's rules,
not your surface.

---

## 5. The short version, ranked

| # | Lever | Size | Whose |
|---|---|---|---|
| 1 | Model tier: Opus 5 is half Fable 5's price on both sides | Halves everything | Kain's decision, raised with him |
| 2 | Measure the standing context, then cut what is dated | Large, and recurring every turn | Yours, and I have offered to help |
| 3 | Stop re-emitting whole documents to change a section | Large, on the $50 side | Yours |
| 4 | Shorter conversations, fresh briefs at boundaries | Large, compounds with length | Yours and mine both |
| 5 | Lower effort on routine work | Moderate, no quality cost on this model | Yours, if the control is exposed |
| 6 | Verbosity instruction, standing | Moderate, on the $50 side | Yours |
| 7 | Intent up front, to avoid correction rounds | Moderate, avoids the worst case | Kain's and yours |
| 8 | Remove any token countdown from context | Small, but it is free | Yours |
| 9 | Hold the standing prefix still mid-session | Unknown until tested | Yours to test |

---

## 6. What I can do, if you want it

**I can count the standing context and give you the real numbers.** The harness,
every skill, the DSRD set, and anything else that rides on a turn, measured
rather than estimated, in one table. That is item 2's first half and it is
mechanical work on files I can already open. Say the word in FROM Chat.

**I can run the prompt audit method over the harness and the skills** and file a
report: every dated instruction, where it is, what pattern it matches, why it is
obsolete for Fable 5, and a proposed cut, with the confidence marked on each so
you can take or leave them one at a time. I would propose, never apply. The
harness is Kain's and yours, and Rule 8 puts it out of my hands regardless.

**What I will not do:** touch any of these documents. This is a research note
and an offer, not a change.

*No em or en dashes in this file; checked before writing.*
