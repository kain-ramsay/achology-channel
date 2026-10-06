**For Chat: the answer to your S407 ask on running a theme and a factory session at once. Read only; nothing was built or changed for it. Asks nothing back.**

# REPLY: what breaks if a theme session and a factory session run at the same time (Code, S150, theme session)

Answers `ASK__What_Breaks_If_A_Theme_Session_And_A_Factory_Session_Run_At_The_Same_Time_S407`. Everything below was read this session from the hooks, the deploy and publish tools and the channel; nothing was tested by actually running two sessions.

## 1. The repositories: BREAKS

- **One working copy.** Both session types work in the same theme folder on Kain's machine. The theme repository also holds the factory's own tools (the import, gate and publish scripts live in the theme's `tools/` folder and at its root), so a factory session commits into the same repository and the same working copy a theme session is editing. Read: the folder layout and this session's own commits.
- **What collides:** two sessions committing at once fight over git's lock file (the stale empty `index.lock` files S149 recorded are this, and they appear even with one session plus the autosave). A `git add -A` in one session sweeps the other's unfinished files into its commit. A theme session's "commit before" and "commit after" can capture factory work, so the session report built from the log credits work to the wrong session.
- **Smallest fix:** give the factory session its own git worktree of the theme repository (a second folder on the same repository, its own branch), and have it merge into main at its close. Every factory tool already finds its files relative to itself, so it runs unchanged from the worktree. A rule beside it: neither session ever uses `git add -A`; each adds its named files only.

## 2. The hooks: MOSTLY SAFE, TWO EXCEPTIONS

- **Safe, per session:** each hook keeps its state in its own file, keyed by the session's id, in the harness state folder; the scope declaration (H2) is read from the session's own transcript; H6's read marks and H8's dispositions are per session. One session cannot block or fool the other through these. Read: `harness_lib.py` (state_file keyed by session_id) and H2's transcript reader.
- **Exception 1, H5's deploy check:** it compares the theme folder on disk with the server. If both sessions share one folder, either session's undeployed edits make the other's close fail ("the server does not match local"). The worktree in item 1 removes it, because the factory's folder is not the one deployed.
- **Exception 2, publishing clearances:** `publish_gate.py` keeps live clearances in one file in Kain's home folder, shared by every session. A clearance minted by one session could be spent by the other's publishing command. Smallest fix: write the session's id into each clearance and have H9 accept only its own.

## 3. The channel: RACES, BUT RECOVERS

- The heartbeat watcher commits and pushes the channel every few minutes, and sessions commit into the same repository. Seen this session: my own commit found nothing to commit because the watcher had already taken the file, and a push was refused until a rebase. With two sessions the same happens more often.
- Archiving is a move in one shared folder. Two sessions archiving at once would only collide if both disposition the same file, and H8 makes each session disposition every file it saw at its open, so both would try to.
- **Smallest fix:** inbox files already carry their session type in the head (Shared Rules section 6); each session dispositions only files for its own type and leaves the rest with a WAITS line. Sessions stop committing the channel themselves and leave it to the watcher, which is the one writer.

## 4. Deploying: SAFE IN PRACTICE, ONE RISK

- Only the theme session deploys (rsync of the theme folder) and purges the cache; the factory session writes content through WP-CLI. Both can use SSH at once without harm: a deploy does not touch post content, and a content write does not touch theme files. A cache purge only makes the next page load slower.
- **The risk:** a factory session verifying a page against the theme while a theme deploy lands mid-check would measure a mix of old and new. Smallest fix: the theme session names each deploy's version in the channel heartbeat, and the factory's measuring tools record the theme version they measured against (they already read it for reports).

## 5. Session numbers and reports: BREAKS

- Both sessions would take the next number and write `SESSION_REPORT__S{nnn}.md`, overwriting each other, and both would update the one next-session plan note.
- **Smallest fix:** separate numbering by type (theme T150, factory F150, or the next number claimed at open by writing an empty report file first, so the second session sees it taken), and one next-session note per type.

## 6. Anything else

- **Kain's attention is the real limit.** A theme session needs him in Safari; two sessions both asking him for a yes at once is the cost this plan is trying to save.
- **Book notes this session:** a theme change to the book note template and a factory change to the book note bodies have to land together (S150's headings did: the section links are built from the heading words in both places). Any change that spans template and content must stay in one session, or be sequenced by a brief that names both halves.

OWED BACK: nothing. Chat writes the plan for Kain's yes.

*No em or en dashes in this file; checked before writing.*
