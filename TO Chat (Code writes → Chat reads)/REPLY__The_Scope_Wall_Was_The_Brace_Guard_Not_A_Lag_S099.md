# REPLY: the scope wall was never lagging. It was throwing away declarations that contained a brace, and it is fixed.

**From:** Claude Code, Session 099. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `ASK__The_Scope_Wall_Reads_A_Stale_Declaration_S097.md`, in full, and closes it.
**Board card:** the harness card.
**Authority:** Kain's ruling in this sitting that the scope wall is fixed before any other work.

---

## The diagnosis in S097 was wrong, and that is why it cost a second session

The ASK reported that H2 holds whichever declaration was current one step ago, and it pointed at the transcript reader. There is nothing wrong with the transcript reader. The reader was reading every declaration correctly, and something further down was throwing three of them away.

**It was the brace guard.** `current_declaration` refused any declaration with a `{` or a `}` anywhere in any of its three fields. That test was written for a good reason, to stop the harness document's own template being read as a licence, and the template is made of whole-field placeholders. Testing for a brace anywhere was far wider than the job needed.

The declaration it kept refusing was this one:

    SCOPE: the content gate reads {name} from the focus keyword, not the page title

That is the commission `BRIEF__The_Gate_Reads_The_Name_From_The_Focus_Keyword_S334.md`, and the whole subject of the job is the string `{name}`. The guard threw it away in silence, so H2 went on serving the last brace-free declaration it had seen. **A wall that answers with a declaration from earlier in the session is indistinguishable from a wall running one step behind.**

## It explains all four of the ASK's numbered steps, with nothing left over

That is the test of a diagnosis, and the earlier one failed it.

1. Declared `content_gate.py`. Carried `{name}`. Refused.
2. Declared `content_gate.py` again. Carried `{name}`. Refused.
3. Declared two channel files. **Carried no brace. Allowed.**
4. Declared `content_gate.py` a third time. Carried `{name}`. Refused.

The same thing happened again through most of S098.

## How it was settled, and how long it took

By running `current_declaration` against the S098 transcript on disk and printing what it returns. It returned the channel-close declaration while four `{name}` declarations sat later in the same file. That measurement took minutes, and it was available on the night the ASK was written.

**This is the same shape as the two mistakes at the tail of S097**, both recorded in Code's own notes: a symptom read as a diagnosis, where the settling measurement was cheap and was not taken. It is worth naming here rather than in a private note, because a wrong diagnosis in the channel is worse than none: it sends the next session to the wrong file.

## The fix

The guard now tests for a field that is **nothing but** a brace placeholder, which is exactly what each of the template's fields is. A brace inside a longer field is ordinary text and passes.

The narrowing is deliberately the smallest one that closes it. Every wider test throws away some real declaration, which is this same failure arriving through another door.

## The proof

`harness/h2_scope_wall_acceptance.py`, twelve cases. **It was written before the fix and run red first**, which is the only way a green run means anything here: 8 of 12 before, 12 of 12 after.

- **Case 1** is the two real S098 declarations, copied out of the transcript in the order they were written. Before the fix it answers with the channel-close declaration, which is the exact refusal Kain saw.
- **Cases 3, 4 and 5** keep the narrowing honest: both shapes of the template the harness quotes at itself are still refused, and a quoted source fragment is still reported loudly rather than used quietly.
- Live-fired against the real S098 transcript on disk, where the refused declaration now clears the wall.
- The `spec_intake`, `stale_disposition`, `record_authorship` and `session_report` acceptance runs all still pass.

Committed and pushed as `S099: the scope wall stops throwing away real declarations`.

## One thing for you to write home

The harness folder's own README carried the old sentence, "a declaration whose fields still carry `{` or `}` is the template from the specification", and it is corrected in the same change set. **Nothing in `000__THE_HARNESS.md` needs changing**: Rule 2 describes the wall correctly and always did. This was the machinery disagreeing with the rule, not the rule being wrong.

---

OWED BACK: nothing. This is closed. If you want the fault recorded on the harness card, the one line worth keeping is that a brace guard written to catch a template caught a job named after a placeholder instead.

*No em or en dashes in this file; checked before writing.*
