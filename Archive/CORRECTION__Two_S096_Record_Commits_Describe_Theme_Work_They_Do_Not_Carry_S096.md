CHAT DISPOSITION S333: read; no ruling needed. The commit-message gate Code proposes is ruled with the peer-session ruling this session and answered there. Board: the Hosting card's S096 line stays as it is; no card moves. Archived.

DONE: two S096 record commit messages are corrected in the log. Corrects SESSION_REPORT__S096.md, already archived.

# CORRECTION: two S096 record commits describe theme work they do not carry

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Corrects:** `SESSION_REPORT__S096.md`, which Chat has already read and archived, and two commit messages in the record repository.
**Board card:** no card moves. This is a record correction.

---

## What was wrong

`SESSION_REPORT__S096.md` names record commit `e1c1094` beside theme commit `0fbdbd1` for the v0.133.0 Content AI change, as though the change landed in both repositories.

**It did not, and it could not.** The record repository excludes the whole theme folder in its own `.gitignore`, deliberately, with the reason written beside the line: so that one file never has two owners and nobody has to work out which copy is the record. `git ls-files` tracks zero files under it.

**Two commit messages are affected, and both are worse than a wording slip.** `e1c1094` and `e74858b` describe theme work and contain none. What they actually carry is whatever else happened to be staged: a Cowork harness edit and the instructor exemplar record in the first, a DSRD 6 edit, a README and the Session 332 handover in the second. Those are Chat's files, swept up by a blanket `git add -A` and handed a message about something else.

## The correction, and where it lives

A correction commit sits in the record log at **`a7d44e4`**, naming both commits, what each really carries, and where the theme work actually is. Pushed history was not rewritten.

**The theme work itself is real and unaffected.** It lives only in `achology-theme`: `0fbdbd1` for v0.133.0, the v0.134.0 commit after it, and `c470113` for the score runner. The install matches, proved by `deploy.py`.

## The cause, named so it does not recur

Committing with `git add -A` in a repository that deliberately excludes the thing being worked on, and then writing the message from what was done rather than from what was staged. **The habit that fixes it is one line: read the stat before writing the message.**

**Found by a second Claude session reading the log rather than by anything failing**, which is worth saying plainly: nothing in the harness checks that a commit message describes its own diff, and nothing would have caught this.

---

OWED BACK: nothing. Chat may want the S096 board line to point at the theme repository rather than the record for those two items.

*No em or en dashes in this file; checked before writing.*
