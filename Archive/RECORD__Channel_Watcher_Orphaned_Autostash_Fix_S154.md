# RECORD: the channel watcher's orphaned autostash fix (S154)

**From:** Claude Code, theme session S154, with the separate local session that wrote the fix, 7 to 8 October 2026. **Asks nothing of anyone**, so it is filed straight into the Archive (The Shared Rules, section 6).

## What went wrong

Twice on 7 October this Mac's channel clone stopped syncing. An interrupted pull left `.git/rebase-merge` holding only the file `autostash`, with no `head-name`. Git then refused every rebase ("there is already a rebase-merge directory"), and `git rebase --abort` refused too, so the watcher reported "rolled back cleanly" every cycle while the clone stayed shut. Chat's FROM Chat files stopped arriving, and hook H10 wrongly called the far machine silent, because this clone's copy of its heartbeat was stale. Code cleared it by hand both times: the autostash was filed into the stash list, then the folder removed.

## The fix

In `machine-two/channel_watch.sh`, step 0 (recover): when `.git/rebase-merge` holds only `autostash`, the hash is filed into the stash list first, so nothing is lost, and only then is the folder removed; if the hash cannot be filed, nothing is touched and the cycle stops on a FAIL naming it. The self-update step now writes the new copy beside the running one and moves it into place, because copying over the file a run is executing made that run read the new file from the old offset. Channel commits 2a5aa90be, 0ff7de73c, 0f3645843, 11ead14b3. The theme's copy, `tools/channel_watch.sh`, matches it on branch `claude/watcher-autostash-fix-01anrm` (b4d2bb6), not yet merged to the theme's main.

## Proof, and what is not proved

- The running copy (`~/.claude/achology_channel_watch.sh`) is byte for byte the channel's fixed version (read at S154).
- Both machines reported OK at 23:25 to 23:26 UTC on 7 October: "Nothing to send. Channel and origin agree."
- The fixing session tested the recovery against a real stuck folder (its own report).
- **Not done:** the throwaway-clone test this commission asked for, in a scratch copy under `/private/tmp/claude-501`. Code began it at S154 and stopped it unfinished when Kain closed the session: the copy is 1.2 GB and was still cloning, and this session's publishing guard (H9) refuses to run any shell script, so the watcher could not have been run against the copy here in any case. It needs a factory session to run the script with `HOME` pointed at a scratch folder whose `achology-channel` clone has a local bare repository as its origin, so nothing reaches GitHub.

*No em or en dashes in this file; checked before writing.*
