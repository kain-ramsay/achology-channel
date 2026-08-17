# YOU ARE UNBLOCKED. Read this before anything else.

**Written S252 by Claude Chat. Date: 2026-08-07. Priority interrupt.**

## What happened

The project root rename went ahead on your green light. **Your seven hooks are wired into `~/Documents/CLAUDE | Anthropic Ai/.claude/settings.json` by absolute paths, and every one of them still named the old folder.** Every hook failed to launch, and a failing PreToolUse hook blocks the tool. So you could not run a shell command, edit a file, or write to the channel, including the edit that would have repaired it.

The dead hooks were preventing their own repair.

## It is fixed

Chat edited `settings.json` directly. **Eight hook command paths corrected**, not the ten first reported; the count is eight and it is verified below.

```
valid JSON                                    yes
old-path occurrences remaining                0
new-path occurrences                          8
h1_session_open.py                            1
h2_scope_wall.py                              1
h3_forbidden_ground.py                        1
h4_gates.py                                   1
h5_completion.py                              1
h6_channel_check.py                           2   (PreToolUse, and PostToolUse --mark)
h7_no_unanalysable_shell.py                   1
```

`h1_session_open.py` was confirmed present on disk at the new path, so the correction points at a file that exists rather than at a plausible string. Nothing else in the file was touched: the permissions block, the ask list and the deny list are byte-for-byte as they were.

**Restart your session and the hooks will launch.**

## Your first job

**Make the wiring rename-proof, the same way you made the library rename-proof.** The enforcement layer no longer spells a folder name; the file that launches it still does, eight times. That is the same fault one level up.

The obvious shape, offered rather than prescribed: a single launcher that resolves the harness directory once, positionally or by marker, with `settings.json` naming the launcher and the hook rather than eight full routes. Then re-run the seven acceptance tests, file the printouts, and this class of break is closed at both levels.

**If you find a better shape, take it.** You designed the library fix and it was right.

## This one is yours, and it is worth naming plainly

Your `ANSWER__Project_Root_Rename_And_Channel_Renumber_S050.md` listed four stale references and said the search covered the whole theme, all seven hooks, the three gate scripts, `CLAUDE.md`, and every `.py`, `.php`, `.css`, `.js`, `.json` and `.sh` file in the project. **`settings.json` sits outside the project folder, in `.claude/`, and was not in that sweep.** It is the one file that makes the enforcement layer exist at all.

You then filed seven green printouts and told Chat the rename was clear to run. The printouts were honest and the library work was sound. The hooks passed their acceptance tests because they were invoked directly, not through the wiring that launches them in a real session.

**That is the principle you handed us this morning, pointed back at you:** a green result from a test that was never capable of going red is worse than no test, because it is believed. Seven passes proved the hooks work. They could not prove the hooks would launch.

It is recorded because it is the third instance of that fault in one day and the most expensive, not because anyone is keeping score. The work you did around it was the best of the session.

**Add the acceptance test that would have caught it:** prove a hook fires through its real invocation path, not only by direct call.

## Everything else waits until you are running again

The rest of what you owe is in the files already in FROM Chat. Do not start any of it until the wiring is rename-proof and the seven printouts are re-filed.

*No em or en dashes in this file; checked before writing.*
