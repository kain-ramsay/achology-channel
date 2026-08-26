CHAT DISPOSITION, S317: DONE. H9 written into The Harness Layer 2, Version 3.7, and read back. Kain ruled yes to widening the wall to taking a live page down; filed as RULING__The_Publishing_Wall_Widens_To_Taking_A_Page_Down_S317 in FROM Chat. Archived.

# RULING: the publishing wall, ruled by Kain in session. Write H9 into The Harness.

**From:** Claude Code, Session 087, 26 August 2026.
**Ruled by:** Kain, in the S086 sitting and restated at the S087 open, directly in session.
**Filed under Harness Rule 14**, which makes a ruling given in a Code session authority at once and requires it to reach its owning document in the same session.
**For Chat to write into:** `000__THE_HARNESS.md`, Layer 2, as H9. Code never edits that document (Rule 8), which is why this file exists.

---

## Kain's words, quoted rather than summarised

At the S087 open, naming the job and the three things that would stop it working:

> "First job: build the publishing wall and the missing runner as one job. DSRD 6's eleven search checks have no runner at all, and nothing in the harness guards content going live. Remember the three things that would stop it working: 'I could not tell' must be a fail rather than a pass, it must not block me for pages Kain publishes himself, and Chat writes the rule into the harness, not you."

## What is now true

**H9, the publishing wall, is built, wired and accepted.** It sits on the Bash PreToolUse hook beside H7. It refuses any command from Code that could put content in front of the public unless that command names a live clearance minted by `publish_gate.py`, and a clearance is minted only where every named page passed the machine third of DSRD 6 and its record carried no failing line.

The full account, with the acceptance printout, is `REPORT__The_Publishing_Wall_And_The_Search_Runner_S087.md` beside this file. This file is the ruling and does not repeat it.

## The three conditions, and how each is met

**One. "I could not tell" is a fail, never a pass.** The wall refuses on three grounds, not one: an explicit publishing verb; a project script capable of publishing, worked out by reading the scripts rather than from a list somebody keeps; and a command that reaches the install and cannot be statically read. The third ground is the widest and it is the one that matters, because publishing is a sentence spoken to a server and a shell command can hide its verb behind a substitution, a pipe or a script.

**Two. It cannot block Kain, by construction rather than by a rule.** It is a hook on Claude Code's own shell. Kain publishes in the WordPress admin in his own browser, and nothing in that path passes through any hook. He is never prompted, never delayed, never asked for a clearance, and there is no switch for him to reach for because nothing here reaches him.

**Three. Chat writes it into the harness.** This file is that request. Nothing in the harness document was touched from this side, and H3 would have refused it if it had been tried.

## What Chat is asked to write

One entry in Layer 2, in the shape the other hooks carry, naming: the event it sits on, what it refuses, the clearance route through `publish_gate.py`, the "could not tell is a fail" rule as its governing principle, and the fact that it cannot reach Kain. The acceptance line, in the shape H8's carries: thirty one cases green in `harness/h9_publishing_wall_acceptance.py`, run against a temporary clearance store rather than the live one, deliberately, because a regression test that spends real clearances damages the thing it tests every time anybody runs it.

## One thing for Kain to rule, named here rather than decided

**The wall covers publishing and not unpublishing or deleting a live page.** That is the same class of unguarded public-facing change and it is a real gap. It was left out on purpose: Kain commissioned a publishing wall, and widening it unasked is the "while I am in here anyway" failure Rule 3 exists to stop. It is a small extension to the same hook if he wants it.

OWED BACK: H9 written into The Harness Layer 2 as a new version, and Kain's word on whether the wall should also cover taking a live page down.

*No em or en dashes in this file; checked before writing.*
