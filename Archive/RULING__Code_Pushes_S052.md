# RULING: Code pushes. The 28 commits are on origin.

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Filed under Harness Rule 14:** a ruling from Kain in session is authority, and
is filed the same session so Chat writes it into the owning document.
**Answers:** the second half of `SHIP__S051_Sixteen_Changes_And_One_Version_Question.md`,
and the open item left in `RULING__The_Version_Is_0_42_0_S052.md`.

## Kain's words, quoted

> "push the 28 commits"

## What was done

| Step | Result |
|---|---|
| Remote | `git@github.com:kain-ramsay/achology-theme.git`, the repository already in use |
| Before | `main` ahead of `origin/main` by 28 |
| Push | `bfcb283..9b74bf9  main -> main` |
| After, read back with a fresh fetch | `## main...origin/main`, level, nothing ahead |

The 28 run from `4bbff9b`, the Book Note page template at S251, through to
`9b74bf9`, this session's version bump. The backlog that had been growing since
the repo first fell 11 behind is cleared.

## The standing ruling, given minutes later in the same session

I put the recommendation to Kain that pushing should join the change set rather
than stay a per-instruction act. His answer:

> "Yes, Claude. We must make cushion part of every single change set."

Read as pushing, which is what the word answers and what the sentence was about.
I am recording the reading here rather than silently correcting him, so Chat
writes the rule from the meaning and not the keystroke. If the reading is wrong,
this is the line to come back to.

**In force from S052: the closing push is part of every change set.** A change set
now ends with its closing commit, its deploy, and its push, and none of the three
waits to be asked for.

**What Chat writes, and where.** This belongs inside Rule 12 beside the deploy,
not as a fifteenth rule. Rule 12 already says deployment is part of the change set
and never a separate step waiting on a human courier; the push is the same claim
about the same step, and the Chat Harness's growth governor prefers a rule
tightened over a rule added. Rule 9's second sentence, "the repo is never more
than one change set behind the theme on disk", is the sentence this makes true of
`origin` and not only of the local repo, so it may be the cleaner home. Chat's
call which; the substance is the same either way.

Code cannot make the edit: Rule 8 puts this document out of bounds and the harness
is Chat's to version. Until it is written in, I hold the rule from here.

**Worth considering, not asked for.** H5, the completion gate, already blocks
finishing when the gates have not run clean since the last edit. An unpushed
commit is the same shape of miss and the check is one line of git. If Kain wants
the rule enforced mechanically rather than remembered, commission it and I will
build it to a specification.

## One thing I have not touched

`previews/.php-cache/` sits untracked in the working tree. It is build residue,
not source, and it is unrelated to this ruling. It gets swept when the previews
retirement in `RULINGS__Previews_Link_Ceiling_Keyphrases_S245.md` section 1 runs,
which is still open work.

*No em or en dashes in this file; checked before writing.*
