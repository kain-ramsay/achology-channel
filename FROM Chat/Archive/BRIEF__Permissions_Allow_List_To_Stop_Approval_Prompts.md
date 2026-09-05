# BRIEF: install a permissions allow list so Kain stops approving safe commands

**From:** Claude Chat, S235. **Date:** 2026-08-03. **Approved by Kain in session.**

## The problem, in Kain's words

He is being asked to approve a command every couple of minutes and it is wrecking his concentration. The prompt that triggered this was a read-only `grep` across the channel folder: harmless, and exactly the kind of thing that should never have reached him. Accept-edits mode is already on, which covers file edits but not Bash, which is why the prompts keep coming.

## What to install

A permissions allow list in Claude Code's settings for this project, so safe read-only work runs silently and only genuinely consequential actions stop for Kain.

**Allow, silently:** reading and viewing files anywhere in the project and channel folders; searching (`grep`, `rg`, `find`); listing (`ls`); reading file contents (`cat`, `head`, `tail`, `wc`); read-only git (`git status`, `git diff`, `git log`, `git show`); running the existing gate scripts (css_gate, page_gate, article_gate) and the dash check; running Python scripts already inside the project.

**Keep asking, every time:** anything that deletes (`rm`, and any destructive move); `git push` and anything that publishes; any deploy or upload to the live or build site; anything reaching the network (`curl`, `wget`); package installs; anything writing outside the project and channel folders.

**Do not use the bypass mode that skips all permission checks.** Kain's ruling, and the reason is on the record: this machine has direct SSH access to the live site, so a blanket skip is not a productivity setting, it is a risk transfer.

## Constraints

**Propose the exact rules before you install them.** Write the proposed allow, ask and deny lists into TO Chat as a file, in the exact syntax you would use, with one line per rule saying plainly what it permits. Kain approves the list, then you install it. This is a permissions change on his machine, so it goes through him, not through your judgement about what is safe.

**The harness is unaffected and stays unaffected.** Hooks H1 to H6 are independent of the permission system and must keep firing exactly as they do now. In particular H2's scope wall and H3's forbidden ground stay live: nothing in this allow list may make it possible to write into the DSRD folder, to edit `000__THE_HARNESS.md`, or to touch a file outside the declared scope. Confirm in one line that you have checked this, with the acceptance evidence, when you propose the rules.

**Say where the settings live.** Name the exact file the rules go into and whether it is committed to the repo or local to the machine, so Kain knows what he owns and where to look if a prompt reappears.

## Definition of done

The proposed rules are filed in TO Chat, Kain approves them, they are installed, and one session runs without a permission prompt for a read-only command, confirmed by you in one line. Nothing is installed before his approval.

No em or en dashes in this file, checked before writing.
