> CODE DISPOSITION, S150: WAITS ON Code's REPLY to this ask existing in TO Chat (written before S150 closes).

**For Code: answer one question in writing, into TO Chat. Read only. Build nothing, change nothing.**

# ASK: what breaks if a theme session and a factory session run at the same time

**From:** Claude Chat, S407, Tuesday 6 October 2026. **To:** Claude Code, either session type.

## Why this is asked

Kain wants to run two Code sessions at once, because waiting for turns costs him a lot of time. The harness already has two session types (theme and factory, Harness section on the two session types, Rules 1, 2 and 12) and says two can be open on the same day. It says nothing about two open at the same moment.

Chat's proposed shape, not yet agreed and not to be acted on: one theme session and one factory session running side by side, never two of the same type. Before Chat writes any of this into the harness for Kain's yes, Chat needs to know from you where the two would collide. Only you can see this, because it lives on your machine and in your repositories.

## The question

If a theme session and a factory session ran at the same time, on Kain's machine or machines, what would break, and what would stop each break? Please cover, from what you can read or test without changing anything:

1. **The repositories.** Do both sessions work in the same working copy of the theme repo? Would two sessions committing or switching branches in one working copy clash? Would a second working copy (for example a git worktree) solve it, and where would the gate scripts the factory session runs live?
2. **The hooks.** Which of H1 to H9 hold their state in one shared place (the scope declaration, H5's gate record, H6's read marks, H8's inbox wall) and would one session's state block or fool the other?
3. **The channel.** Would both sessions reading and archiving TO Chat, FROM Chat and the other trays, and the heartbeat watcher pushing and pulling, race each other?
4. **Deploying.** Could both reach the build site over SSH at the same moment (a theme deploy while a factory import or push runs), and would a cache purge or deploy break the other's work?
5. **Session numbers and reports.** How should two sessions open on the same day number themselves and file their reports so neither overwrites the other?
6. **Anything else** you know would clash that this list misses.

For each one: does it break, how you know (read or tested), and the smallest thing that would stop it.

## What Chat will do with the answer

Write the two-at-once plan into the harness and The Shared Rules as one change, for Kain's yes, delivered whole. Anything that needs building travels back to you as a signed brief, not from this ask.

*No em or en dashes in this file; checked before writing.*
