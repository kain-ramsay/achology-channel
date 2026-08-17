# RULING: the theme version is 0.42.0, set and deployed on its own

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Filed under Harness Rule 14:** a ruling from Kain in session is authority, and
is filed the same session so Chat writes it into the owning document.
**Answers:** the question in `SHIP__S051_Sixteen_Changes_And_One_Version_Question.md`.

## Kain's words, quoted

> "First act: set the theme to v0.42.0 and deploy it, on its own, per the S051
> ship brief."

That adopts the recommendation in the S051 ship brief exactly as it was put:
`v0.42.0`, set as the first act of the next session, as a change of its own with
nothing riding on it. So versions have not quietly stopped mattering, and I will
carry on raising the number where a change set earns one.

## What was done

One change set, one file, one commit, deployed and verified.

| Step | Result |
|---|---|
| `style.css` line 7 | `Version: 0.41.0` becomes `Version: 0.42.0` |
| Commit | `9b74bf9`, the only commit in the set |
| Deploy | rsync over SSH to the build ground, 17 files moved |
| Live theme header | reads `Version: 0.42.0` |
| WordPress' own view | `wp theme list` reports `achology 0.42.0` |
| Cache | object cache flushed, Speed Optimizer assets and dynamic cache purged |
| Live page proof | `/about/` emits ten asset addresses, every one stamped `v=0.42.0`, none at `0.41.0` |

The minor rather than a patch stands for the reason given at S051: the course
selection mechanism changed and two data fields were retired.

## What this closes, and what it does not

**Closes:** the version question. The number and the deployed theme agree again.

**Does not close:** whether Code pushes to origin. That was the second half of the
S051 brief and it has not been answered. The repo now sits at **28 commits
unpushed**, one more than yesterday because of this one. Pushing is outward
facing, so I have not done it and will not until there is a ruling. If the answer
is that pushing joins the change set the way Rule 12 made deployment part of one,
say so and I will push at the close of every set from that point, and clear the
28 as the first act.

## One note for the record

Nothing about this change was visible on a page, so there is no rendered result
to look at. The proof is the live theme header, WordPress' own report of the
active theme, and the version stamp on the live page's asset addresses, all read
back from the server after the deploy rather than assumed from the transfer.

*No em or en dashes in this file; checked before writing.*
