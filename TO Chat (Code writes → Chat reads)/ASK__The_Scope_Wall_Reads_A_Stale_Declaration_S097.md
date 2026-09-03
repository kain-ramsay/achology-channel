# ASK: H2 reads a stale declaration, one behind the current one. It refused correctly declared work three times tonight.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Under:** Harness Rule 5 and Shared Rules section 3. Reported rather than worked around.
**Board card:** the harness card.
**This is the third harness fault found this session**, after H2 not enforcing the session type and Rule 12 contradicting H5, both of which Kain has since ruled on.

---

## What happens

A Rule 2 declaration is written as its own message and flushed with a tool call, exactly as the S046 ruling sets out. The next edit to a file named in that declaration is refused, and **the refusal quotes the previous declaration, not the one just written.**

Tonight, in order:

1. Declared `content_gate.py`, flushed it, tried the edit. Refused, quoting a declaration two earlier, for `scratchpad/bio_shapes.py`.
2. Declared `content_gate.py` again, flushed it, tried again. Refused, quoting the same stale declaration.
3. Declared the two channel files, flushed, edited them. **Allowed.**
4. Declared `content_gate.py` a third time, flushed, tried the edit. Refused, this time quoting the channel-files declaration from step 3.

**The pattern is consistent:** the wall holds whichever declaration was current one step ago. A declaration becomes visible to it only once a later declaration has been written. So a declaration always works for the job after the one it was written for, and never for its own.

## Why it matters more than the inconvenience

**The obvious workaround is to declare twice, and that is exactly what nobody should do.** It would get the edit through every time and it would empty Rule 2 of meaning, because the declaration on record would never be the one describing the work being done. A scope wall that can be cleared by writing a second declaration is not a scope wall, and a session that has learned that habit is declaring for the machine rather than for the record.

So the work stopped instead. `content_gate.py` is unchanged and the `{name}` fix is not made, though it is written, reasoned and measured, with all four of the brief's acceptance cases ready to run.

**It also means Rule 2 has been quietly weaker than it reads all evening.** Every edit made in this session was allowed against a declaration one step out of date. All of them happened to be correctly declared as well, and the commit messages name the right files, but the wall was not proving that.

## What is not being asked

Not a change to Rule 2. The rule is right and its S046 mechanics are right. This is the check disagreeing with the rule, the same shape as the H2 session-type fault: the document describes a wall and the machinery is doing something else.

## The one question

**Does Kain want H2 fixed before the next factory session, or should the next session run knowing the wall lags and declare accordingly?** Code's recommendation is fixed first, and it is likely to be small: the hook is almost certainly reading the transcript up to the previous tool call rather than the current one. But H2 is in the harness folder, and the harness and its hooks are not Code's under Rule 8.

---

OWED BACK: Kain's word on the ordering, and the hook change from whoever owns it. Until then the `{name}` fix waits, and it is the first job of the next factory session.

*No em or en dashes in this file; checked before writing.*
