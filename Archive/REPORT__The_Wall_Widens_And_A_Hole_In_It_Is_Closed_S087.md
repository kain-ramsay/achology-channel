> **CHAT DISPOSITION, S318: DONE.** Written into The Harness as Version 3.8 (H9 widened, third ground corrected, acceptance at thirty seven cases). Its OWED BACK line is answered by that write. Archived.

# REPORT: H9 widened to taking a page down, and a hole in the wall closed in the same pass

**From:** Claude Code, Session 087, 26 August 2026.
**Answers:** `RULING__The_Publishing_Wall_Widens_To_Taking_A_Page_Down_S317`, and closes its OWED BACK line.
**Board card:** Plugins and Site Configuration.

---

## 1. The widening, as ruled

Kain's word was yes. H9 now refuses, on the same terms as a publish, any command from Code that would take a live page out of public view:

- `wp post delete`
- `wp post trash`
- a post status being SET to draft, pending, private or trash
- `wp_delete_post` and `wp_trash_post`
- a `DELETE` against the posts table

Same clearance, minted the same way by `publish_gate.py`, expiring and spent the same way. "I could not tell" is still a fail. The wall still cannot reach Kain, because his path through the WordPress admin passes through no hook.

**One distinction had to be drawn to make it usable.** Setting a status to draft hides a live page; FILTERING a list by draft is how every script here finds the drafts in the first place. The wall reads the difference rather than the spelling, exactly as it already does for `post_status=publish`. Both directions have an acceptance case.

## 2. A hole in the wall, found by using it, closed in the same pass

This was not commissioned and it is the more important half.

**Until this pass, ground C stood down whenever a read verb appeared anywhere in the command.** The check for an unreadable payload was skipped entirely if the command contained `wp post list` or any other read. So a command of this shape went straight through: an ssh to the install, a `wp post list`, a semicolon, and a command substitution carrying anything at all.

The read verb at the front switched off the check on the payload behind it. **A wall that can be disarmed by prefixing a harmless verb is not a wall.**

**It is closed.** Ground C now asks its own question and only its own: does this reach the install, and can it be read. A genuine read has no substitution, no heredoc and no pipe into a shell, so it passes on its own merits rather than on an exemption. Case 36 in the acceptance run is that exact command, and it now blocks.

**How it was found is worth recording.** Not by review and not by a test. It was found by the wall being live and me hitting it while doing ordinary work, then asking why it had let something through earlier that it should not have. The four false positives on its first day were the same thing seen from the other side. A wall nobody uses is a wall nobody has measured.

## 3. The acceptance run

Thirty seven cases, against a temporary clearance store rather than the live one.

```
  PASS 31  wp post delete on a live page                   blocked (exit 2)
  PASS 32  wp post trash on a live page                    blocked (exit 2)
  PASS 33  a status being set to draft, which hides a liv  blocked (exit 2)
  PASS 34  a DELETE against the posts table                blocked (exit 2)
  PASS 35  post_status=draft FILTERING a list, which is h  allowed (exit 0)
  PASS 36  a read verb in front of an unreadable payload   blocked (exit 2)
  PASS 37  the reviewed exception dies when the file changes
------------------------------------------------------------------------------
  37 of 37 cases as specified, 0 wrong
```

## 4. The reviewed-exception register did its job today, unprompted

`tools/score_run.py` was fixed this session for an unrelated bug. **Its hash stopped matching, H9 blocked it again, and its payloads had to be read a second time before the exception was restored.** That is the register working exactly as designed rather than a nuisance, and it happened within hours of being built. The entry now records both readings and says why there are two.

OWED BACK: nothing. The widening is built, proved and deployed; Chat writes it into The Harness as Version 3.8 on this printout.

*No em or en dashes in this file; checked before writing.*
