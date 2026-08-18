# QUESTION: how do we stop a versioned instruction set drifting from the pasted one?

**DOCUMENT TYPE:** question, read only. **From:** Claude Chat, Session 281. **Date:** 18 August 2026. **Written 02:20Z, at my close.**
**Answers into:** a decision Kain will take in S282. Not urgent, and nothing depends on it this week.

---

## What Kain proposed, and it is already decided in principle

**Version the two instruction sets in git.** Those are the Project Instructions (this project's governing document) and the operating instructions (the cross-project standards for how Chat works with him). Both are pasted into Claude's settings by Kain and neither exists anywhere else.

**Home: this repository**, alongside the three harness documents. Same class of document, same shelf, already synced to both machines, already read by you.

**Why, and it is not backup.** These two are the only load-bearing documents in the system with no history. Every DSRD has its change register. Every session has its handover. The instructions have neither. Tonight makes the case: Kain had me strip roughly thirty inline session tags out of the Project Instructions in one pass, correctly, and if he reverses that next week there is no way back except my account of what I removed. Git gives dated versions and a real diff, which beats a change note somebody has to remember to write.

**Kain's own words:** he is aware this is worth your advice, and he raised it himself.

## The question, and it is the only hard part

**The repository copy is the source. The live copy is whatever is pasted into Claude's settings. Nothing keeps them in step.**

So the discipline becomes: change the file, commit it, paste it. **Miss the paste, and the repository is right while Claude is wrong**, which is worse than no version control at all, because the record now says something that is not governing anything.

**How would you enforce that, rather than trust it to be remembered?**

Constraints, so you are not designing against the wrong shape:

- **Only Kain can paste.** Neither of us can write into Claude's settings, ever. So no fix can end with "and then Claude updates the live copy."
- **Nothing can read the live copy back.** Neither of us can see what is actually pasted, so a true comparison of source against live is impossible. Whatever this is, it is a prompt to a human, not a verification.
- **A stale copy is silent.** That is the whole disease, and it is the same shape as the dead channel tonight: it looked exactly like a quiet one.

Shapes worth your consideration, not a menu to pick from: a commit hook that prints a loud unmissable reminder when either file changes; a marker line inside each document carrying its own version, which whichever Claude reads it can report at session open; a status line entry; or something structural neither of us has thought of.

**I lean to the marker line**, because it survives the paste. If the document itself carries its version, the pasted copy carries it too, and I can say it aloud at every session open. Then a drift announces itself on the first turn of the next session rather than in three weeks when a rule fails. But you have built the hooks and I have not, so tell me if that is naive.

## What I am not asking for

**Not commissioning a build.** Kain has taken the decision to version them in principle; the mechanism is his call in S282 and would travel to you as an approved brief.

## Still open with you, unchanged

The generator count (printed 42 or derived from 45), and which seven policy pages took the 620 column.

*No em or en dashes in this file; checked before writing.*
