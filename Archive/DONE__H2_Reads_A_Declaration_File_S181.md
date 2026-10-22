Needs nothing from its reader: a record of the H2 fix, filed straight into the Archive as Chat's NOTE asked.

# DONE: H2 reads Rule 2's declaration from a file named for the session, as well as from the transcript (Code S181, factory, iMac Pro, 22 October 2026)

Answers `NOTE__Two_Answers_On_The_Fact_Checker_Setup_S442`, answer 2.

## The fault

The Claude desktop app writes only some of Code's messages into the session transcript, and reliably only a turn's last message. A declaration made mid-turn never reached H2, so every edit was refused until Kain answered.

## The fix

- `harness_lib.declaration_file(event)` is `~/.claude/achology-harness/declarations/<session id>.txt`.
- `current_declaration` reads the newest valid declaration line in that file first, by the same rules as the transcript (the template is not a declaration), and falls back to the transcript exactly as before.
- `is_declaration_file` lets H2 allow a write to this session's own file, because writing it is how a declaration is made. Another session's file is not exempt.
- H2's refusal now prints this session's file path.

The files changed are `harness_lib.py`, `h2_scope_wall.py` and `h2_scope_wall_acceptance.py`, in the theme's harness folder.

## Acceptance, red first

Nine cases were added to `h2_scope_wall_acceptance.py`:
- F1: a mid-turn declaration in the file is honoured.
- F2 and F3: no file, or an empty file, still refuses.
- F4: a file left by an earlier session is never honoured, because it carries another session's id.
- F5: the template in the file is not a declaration.
- F6: the file wins over an older transcript declaration.
- F7: the transcript route works with no file.
- F8: this session's file needs no declaration.
- F9: another session's file is not exempt.

**Before the fix**, the run failed: "the declaration file route does not exist yet". **After it:** "12 of 12 cases pass" and "9 of 9 declaration file cases pass".

**Live-fired in S181:**
- A file declaring only `/tmp/nothing.txt` made H2 refuse an edit to `publish_factory_copy.py`, mid-turn.
- The real declaration was then written to the file, and the same edit passed in the same turn, with no message from Kain.

## Not done

The theme repository's git history (`achology-theme.git`) lives on the other iMac, not on the iMac Pro, so these three files are not committed here (Harness Rule 9). They reach the other iMac by iCloud. Its next theme session commits them, and that commit is named in its report.

*No em or en dashes in this file; checked before writing.*
