# PROPOSAL: the permissions allow list, for Kain's approval before installing

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Answers:** `BRIEF__Permissions_Allow_List_To_Stop_Approval_Prompts.md` (Chat, S235).
**Nothing is installed.** The brief says the rules are proposed first and Kain approves them, so this file is the proposal and the install waits on his word.

## Where the settings live

`/Users/kainramsay/Documents/CLAUDE | Anthropic Ai/.claude/settings.json`

It is **local to this machine and committed nowhere**. That folder is not a git repository, so nothing in it reaches the theme repo or anywhere else. Kain owns this file, and it is the one place to look if a prompt reappears.

Beside it sits `.claude/settings.local.json`, which Claude Code writes itself every time Kain clicks "don't ask again". It has grown to **338 entries**. It is machine-local too.

## First, the actual cause, because the allow list alone will not fix it

An allow list already exists in that file, and it already contains `Bash(grep *)`. Kain was still prompted for a read-only grep. That is worth understanding before adding more rules to a list that is demonstrably not working.

**Permission patterns match the whole command string, and almost every command I run is a compound one.** A command like

    cd "/Users/.../005. Notes for Claude Chat" && grep -rn "..." .

does not match `Bash(grep *)`, because the string does not begin with `grep`. It begins with `cd`. Every `cd X && Y` I run is unmatched, whatever Y is, and that is most of what I do. It is also why the local file has accumulated 338 one-off approvals: each one is a whole compound string, approved once and never matching again.

So the fix has two halves, and the second is mine, not Kain's:

1. The lists below.
2. **I stop writing `cd X && Y`.** The working directory persists between commands and absolute paths work everywhere, so the compound form buys nothing and costs a prompt every time. That is a habit change on my side and needs no approval.

Without the second half, adding rules will not stop the prompts.

## The proposed lists, in the exact syntax

### allow, runs silently

```json
"allow": [
  "Read(//Users/kainramsay/Documents/CLAUDE | Anthropic Ai/**)",
  "Glob(//Users/kainramsay/Documents/CLAUDE | Anthropic Ai/**)",
  "Grep(//Users/kainramsay/Documents/CLAUDE | Anthropic Ai/**)",
  "Edit(//Users/kainramsay/Documents/CLAUDE | Anthropic Ai/**)",
  "Write(//Users/kainramsay/Documents/CLAUDE | Anthropic Ai/**)",
  "Bash(grep:*)",
  "Bash(rg:*)",
  "Bash(find:*)",
  "Bash(ls:*)",
  "Bash(cat:*)",
  "Bash(head:*)",
  "Bash(tail:*)",
  "Bash(wc:*)",
  "Bash(sort:*)",
  "Bash(diff:*)",
  "Bash(sed -n:*)",
  "Bash(awk:*)",
  "Bash(echo:*)",
  "Bash(which:*)",
  "Bash(git status:*)",
  "Bash(git diff:*)",
  "Bash(git log:*)",
  "Bash(git show:*)",
  "Bash(git add:*)",
  "Bash(git commit:*)",
  "Bash(python3 css_gate.py:*)",
  "Bash(python3 page_gate.py:*)",
  "Bash(python3 article_gate.py:*)",
  "Bash(python3 harness/:*)"
]
```

One line each, in plain words:

- The first five: read, search and edit anything inside the project home, and nowhere else.
- `grep`, `rg`, `find`, `ls`, `cat`, `head`, `tail`, `wc`, `sort`, `diff`, `sed -n`, `awk`, `echo`, `which`: read and search only. None writes anything. `sed -n` is the print-only form, and plain `sed` is deliberately not allowed, because `sed -i` edits files in place.
- `git status`, `diff`, `log`, `show`: read the repository, change nothing.
- `git add` and `git commit`: local only, and required twice per change set by harness Rule 9. Neither publishes anything.
- The four gate scripts **by name**, rather than `python3 *`. This is a deliberate **tightening** of what is there now: the current list allows `Bash(python3 *)`, which is permission to run any Python at all, including a script that deletes files or opens a network connection. Naming the scripts keeps the gates silent without leaving that door open.

### ask, stops for Kain every time

```json
"ask": [
  "Bash(rm:*)",
  "Bash(rmdir:*)",
  "Bash(mv:*)",
  "Bash(cp:*)",
  "Bash(git push:*)",
  "Bash(git checkout:*)",
  "Bash(git reset:*)",
  "Bash(git restore:*)",
  "Bash(git stash:*)",
  "Bash(git rebase:*)",
  "Bash(git clean:*)",
  "Bash(curl:*)",
  "Bash(wget:*)",
  "Bash(scp:*)",
  "Bash(rsync:*)",
  "Bash(ssh:*)",
  "Bash(pip install:*)",
  "Bash(pip3 install:*)",
  "Bash(npm:*)",
  "Bash(brew:*)",
  "Bash(python3:*)",
  "Bash(zip:*)",
  "Bash(chmod:*)",
  "Bash(sudo:*)"
]
```

- Everything that deletes or moves: `rm`, `rmdir`, `mv`, and `cp`, because a copy overwrites its destination.
- `git push`, because it publishes.
- **`git checkout`, `reset`, `restore`, `stash`, `rebase`, `clean`.** These matter more than they look. They rewrite working-tree files with no edit tool involved, so no hook sees them and no gate runs on what lands. That is the one real hole in the harness, it exists today, and keeping these in the ask list is the cheapest cover until it is ruled on properly.
- `curl`, `wget`, `scp`, `rsync`, `ssh`: anything reaching the network or the live and build sites, including the SSH access I use for linting. This is another **tightening**: the current list allows `ssh -i ~/.ssh/achology_siteground *` silently, on a machine that can write to the build site.
- Package installs, `chmod`, `sudo`.
- A `python3` catch-all, so any Python that is not one of the four named gate scripts still stops.
- `zip`, because the theme zip is a real artefact Kain then uploads.

### deny, never runs at all

```json
"deny": [
  "Read(//Users/kainramsay/.ssh/**)",
  "Read(//Users/kainramsay/.aws/**)",
  "Read(//Users/kainramsay/**/.env)",
  "Bash(rm -rf /:*)",
  "Bash(sudo rm:*)"
]
```

Credentials I never need to read, and two commands with no legitimate use here.

**Bypass mode is not proposed and not used**, per Kain's ruling on the record.

## The harness is unaffected, and here is the evidence

Confirmed in one line, as the brief asks: **nothing in these lists can make it possible to write into the DSRD folder, to edit `000__THE_HARNESS.md`, or to touch a file outside the declared scope**, because the hooks are a separate mechanism from the permission system. Permissions decide whether a tool call may be attempted; the hooks run on the attempt itself and refuse it regardless of what the permission system said.

The acceptance evidence is this session, unprompted and unarranged:

- **H2 blocked a write** to a throwaway parse harness in the scratchpad, purely because the path was not on the declared file list, even though the scratchpad sits outside the project and the file was disposable.
- **H4 blocked two edits** that had already been written: an em dash inside a PHP comment, and two hand-typed shadow values in CSS.
- **H6 blocked three edits**, each time because Chat had written a new file into FROM Chat mid-session. Every one of them changed the work in hand, including the addenda that unblocked half the build.

All six fired while accept-edits mode was on, which is exactly the point: the permission system was never consulted and the hooks refused anyway.

## Definition of done, where it stands

Filed, waiting on Kain's approval. Once he approves I install exactly these lists, stop writing compound `cd` commands, and confirm in one line after a session runs without a prompt for a read-only command.

*No em or en dashes in this file; checked before writing.*
