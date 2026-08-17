# REPORT: what the standing machinery costs, and what it has actually caught

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Commissioned by Kain in session:** "yes, measure it please", answering my offer
to measure what the standing machinery costs per turn and which of its
obligations have never once caught anything.

**This report corrects my own note filed earlier today**,
`NOTE__Token_Efficiency_Checks_And_Disciplines_For_Fable_5_S052.md`, which named
the standing context as my primary suspicion for the token burn. On Code's side
that guess was wrong by a wide margin and I say so in section 1. On Chat's side
it was right in kind but I had no idea of the scale, and the scale is the whole
story. Section 3 is the finding that matters.

---

## 0. Method, and what is estimate versus what is measured

**The cost figures are estimates.** There is no `ant` and no API key on this
machine, so `count_tokens` could not be called. Every token figure below is
characters divided by 3.8, the usual ratio for English prose with markdown.
Treat them as accurate to within about fifteen per cent, which is well inside
the margin that would change any conclusion here.

**The firing figures are measured**, from 53 session transcripts. A hook block
is counted only where the text appeared in a tool result carrying the hook
script's own invocation envelope. Two things are deliberately excluded: text
inside files I wrote, and printouts I quoted into reports. Without that filter
the raw count for the scope wall was 257; the true figure is 90. Most of the
difference was me quoting hook output into records like this one.

**I got the detector wrong twice before it was right**, and both errors would
have produced a confident false result, so they are worth recording. The first
version keyed on an error flag and reported that the gate hook had never fired
in the project's life. The second matched only the newer invocation envelope and
under-counted every hook that predates the launcher. Both times the check was
green and the thing it checked was broken. The numbers below come from the third
version, which reconciles against the raw counts.

---

## 1. What Code carries on every turn, and it is not the problem

| Standing item | Estimated tokens |
|---|---|
| MEMORY.md, the memory index | 3,286 |
| CLAUDE.md, project instructions | 2,437 |
| The Harness, Layer 1, which is what H1 prints | 2,112 |
| The channel listing H1 prints | 178 |
| **Carried on every turn** | **8,013** |

At Fable 5's input price that is **eight pence a turn**, and about **$8 across a
hundred turns**. On Opus 5 it is half that.

**That is not a token problem and I should not have implied it was.** The whole
standing harness on Code's side costs less than a single mid-sized document. The
notable detail is only that the memory index is now the largest single item,
larger than the harness itself, and it is the one nobody has ever pruned.

The ceremony I add is smaller still: a real status line from this session is 87
tokens and a real scope declaration is 39. Forty messages of status line is
about 3,500 output tokens, which is seventeen pence on Fable. The case against
the status line, if there is one, is not the money.

---

## 2. What each hook has actually caught, measured across 53 transcripts

| Hook | Times it fired | Sessions | Reading |
|---|---|---|---|
| H6 channel check | **91** | 12 | Doing the most work of anything here |
| H2 scope wall | **90** | 12 | Almost all of it real, see below |
| H7 unanalysable shell | **25** | 9 | 25 permission prompts Kain never saw |
| H3 forbidden ground | 1 | 1 | Boundary guard, see below |
| H4 gates | 1 | 1 | Caught one dash-ban violation |
| H5 completion gate | 0 | 0 | Boundary guard, see below |
| H5 push check | 0 | 0 | Built an hour ago, no history to have |

**The scope wall's 90 blocks split 84 to 6.** Eighty-four were "this file is not
on the declared list" and six were "there is no declaration at all". That split
matters: the hook is overwhelmingly stopping an edit to a file that was not in
scope, which is the sweep it was built to prevent, rather than nagging about
paperwork. What the count cannot tell you is how many of those eighty-four would
have been genuine damage and how many were me about to do something sensible
that I had simply not declared. I can measure that it stopped me. I cannot
measure what it saved.

**The channel check's 91 blocks are the clearest win in the set.** That hook
exists because four messages arrived from Chat mid-session during the 249
article rewrite and two of them forbade exactly the work in progress, and nobody
saw them until the close. It has now stopped that from recurring 91 times across
12 sessions.

**Zero is the correct score for two of these.** H3 blocks writes into the DSRD
folder and H5's completion gate blocks finishing with gates unrun. A guard whose
job is to make something impossible is working perfectly when it never fires,
and its value is that the boundary is not left to my restraint. Counting catches
is the right measure for something that creates friction and the wrong measure
for a boundary. So the honest verdict on H3 and H5 is "no evidence either way,
and cheap enough that the question does not need answering".

**The part with genuinely no measurement is the ceremony.** There is no way to
tell from any transcript whether the status line or the declaration ritual ever
prevented anything. The status line's stated purpose is that Kain's whole check
is reading one line, and whether that works is something only Kain can answer,
because it depends on whether he reads it and whether it has ever told him
something he would otherwise have missed. I am not going to pretend that is a
measurement.

---

## 3. The finding that actually matters, and it is on Chat's side

The live DSRD set, excluding the superseded archive, is **814,671 characters,
which is roughly 214,000 tokens.**

That is **twenty-six times Code's entire standing context.**

| Document | Estimated tokens |
|---|---|
| DSRD 2, Content Production and Knowledge Standards | 36,200 |
| DSRD 8, Component Library | 33,200 |
| DSRD 9, Page Layout Specs | 30,700 |
| REF 1, Community Development Reference | 23,600 |
| DSRD 7, Design Foundations | 21,500 |
| The remaining six, plus the README | about 69,000 |
| **Live total** | **about 214,000** |

The top three alone are 100,000 tokens.

**If Chat carries that set in project knowledge and it is loaded whole on every
turn, then Chat pays about $2.14 in input on every single turn on Fable 5**, and
roughly **$86 across a forty turn session**, before writing a word. That is a
completely different order of magnitude from anything on Code's side, and it
would explain "burning through tokens unusually fast" on its own.

**The one thing I cannot determine, and it decides everything.** I have no way
to read how claude.ai assembles a conversation. If project knowledge is loaded
whole every turn, the number above is real. If it is retrieved selectively, or
if the stable prefix is cached at roughly a tenth of the price, the true figure
could be nearer $8 a session than $86. That is a tenfold spread and it is the
first thing anyone should establish, because it decides whether this is an
emergency or an inefficiency.

**It is testable, and the test is Chat's, not mine.** Compare the cost of a
session held entirely inside the project against one where the same questions
are asked with only the one relevant DSRD attached. If the two are close, the
knowledge is being retrieved selectively and this is a non-issue. If they differ
by an order of magnitude, it is loaded whole and the fix follows immediately.

**And if it is loaded whole, the fix is not to cut the DSRDs.** They are the
specification and they are correct. The fix is that Chat should not carry all
ten at all times. Most sessions need one or two. A working session on the
Reviews page needs DSRD 8 and 9; it does not need the Community Development
Reference, and it certainly does not need DSRD 2's content standards.

---

## 4. What I would do, in order

1. **Settle the loading question first.** Everything else is guesswork until
   somebody knows whether project knowledge rides on every turn. One session of
   testing answers it.
2. **If it does ride on every turn: attach per session rather than per project.**
   Carry the two or three documents the session needs. This is the whole of the
   saving, and it costs no standard and no rigour.
3. **Leave Code's standing harness alone.** At eight thousand tokens a turn it
   is not worth the risk of touching, and three of its hooks are demonstrably
   doing real work.
4. **Prune the memory index**, which is now the largest thing Code carries and
   has never been reviewed. Small, but it is the one item here that is pure
   accumulation.
5. **Leave the status line to Kain.** It costs almost nothing and its value is
   entirely in whether he reads it. That is not a question a transcript can
   answer.

*No em or en dashes in this file; checked before writing.*
