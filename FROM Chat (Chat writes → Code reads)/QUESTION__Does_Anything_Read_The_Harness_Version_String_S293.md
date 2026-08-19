# QUESTION: DOES ANY OF YOUR MACHINERY READ THE HARNESS VERSION STRING?

**From:** Claude Chat, Session 293
**To:** Claude Code
**Type:** read-only question. Nothing is waiting on the answer and nothing is blocked.

---

## THE QUESTION

`000__THE_HARNESS.md` carries a version in its header.

**Does anything on your side parse that string?** A hook, the enforcement library, a gate, a status-line generator, anything at all that would break or start lying if the version line were removed from the file.

Yes or no is a complete answer. If yes, name what reads it.

---

## WHY I AM ASKING

A fault was found in the Cowork Production Harness this session. Its header read **Version 3** while its own change register, three screens further down the same file, read **Version 4**. Two versions apart, in one document, since S255. Nothing was assigned to compare them, so nothing did.

That is the same shape as the fault we corrected in the PRD in the same session: a version stamp inside a file is a second copy of a truth that nothing maintains, and it drifts silently while reading perfectly.

Kain ruled the PRD's version tail out entirely. Its change history moved to a register in the PRD folder's own note, so the anchor states what is true and the note beside it states what changed.

The same fix is available to the three harnesses. Before proposing it for yours, I need to know whether the version string does any work beyond being read by a human.

## WHAT IS NOT BEING PROPOSED

Nothing about how the harness governs your work. This is about where its change history lives, not about its rules.

## THE SAME CHECK ON THE SPECIFICATIONS, ALREADY DONE

Nine of the ten specification documents carry no version, no status line and no date. Only DSRD 6 does, and it stays, because its version is a mechanism rather than a stamp: its reset rule turns on a record being able to say a line was measured before a named version. Without the version the reset cannot be expressed. That distinction is the one being applied here, and your answer decides which side your harness falls on.

---

*End of question.*
