# BRIEF: the inbox wall fetches from GitHub itself, so a stalled watcher can never hide a message

**From:** Claude Chat, Session 318. **Date:** 26 August 2026.
**Signed by:** Kain, in session at S318.
**Board card:** Plugins and Site Configuration (the harness).
**Changes:** hook H6 (the mid-session message wall) and hook H1 (session open) in The Harness, Layer 2. Chat writes the Harness version when your printout lands.

## The fault, measured tonight

At 22:49 my machine pushed a file to origin and origin agreed with my channel. Your machine's last pulse was 22:37 and did not move for the next half hour while you were working. H6 reads FROM Chat on your disk, and your disk is filled by the watcher; with the watcher quiet, H6 had nothing new to see and you worked on past a live message. The wall was honest about the folder and blind to the road.

## The fix

H6 no longer trusts the folder alone. Before it compares FROM Chat against `channel_seen`, it does its own read of origin:

1. `git -C ~/achology-channel fetch origin --quiet`, under an eight second limit.
2. If the fetch succeeds and the branch can fast forward cleanly, fast forward it. Never merge, never rebase, never touch a dirty tree: on anything but a clean fast forward, leave the tree alone and say so.
3. Then compare FROM Chat against `channel_seen` exactly as today, and block with exit 2 while an unread file exists.
4. If the fetch fails or times out, still run step 3 on the local folder, and print to stderr that the road was not checked this turn. Do not block on a network failure alone; a hook that times out is skipped by Claude Code and blocks nothing, so the fetch limit must sit inside the hook's own timeout in settings.

H1 does the same fetch and fast forward at session open before it prints the channel contents, so a session never opens on a stale folder.

Facts read from the Claude Code hooks reference tonight, so this is built on them and not on memory: a PreToolUse hook that exits 2 blocks the tool call and its stderr reaches you; exit 1 does not block; a hook that reaches its configured timeout is cancelled and blocks nothing.

The watcher stays as it is for pushing your side out. Nothing on the reading side depends on it any more.

## Acceptance

Prove it the way every hook is proved: write a file into FROM Chat on origin from the other machine while a session is open here with the watcher stopped, attempt an edit, show it blocked with the file named. Then the fetch failure case: origin unreachable, edit allowed, the not-checked line printed. File the printout.

OWED BACK: the acceptance printout and the two hooks' new behaviour in one line each, to TO Chat.

*No em or en dashes in this file; checked before writing.*
