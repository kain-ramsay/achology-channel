# ANSWER: GitHub CLI versus the GitHub MCP, on this machine

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Answers:** `QUESTION__GitHub_CLI_Versus_MCP.md` (Chat, S235). Assessment only. Nothing installed, switched or reconfigured.

## 1. What is actually installed and running

**Plain `git`, and nothing else.** Checked this session rather than recalled:

- `git` 2.37.1 (Apple Git-137.1) at `/usr/bin/git`.
- `gh` is **not installed**. `which gh` returns nothing.
- A GitHub MCP server exists in this session's connector list but is **not authorised**, so none of its tools can be called. It is listed as needing authentication, and a headless session cannot run the sign-in flow.
- The remote is `git@github.com:kain-ramsay/achology-theme.git`, over **SSH with a key**, so no token is involved in what I do today.

So the explainer's premise does not apply here yet. There is no MCP server to replace: the choice is between plain `git` as now, and adding `gh` alongside it.

## 2. What `gh` would change, concretely

`gh` does not replace `git`. Commits, branches, diffs and pushes stay `git` either way. What `gh` adds is the GitHub **API**: pull requests, issues, releases, Actions runs, repository settings.

- **Token use:** this is the real change. Today my only GitHub credential is Kain's SSH key, which can push code and do nothing else. `gh` authenticates with an OAuth token that by default carries `repo`, `read:org` and `gist`, which is a much wider grant than pushing commits. That is a security decision, and under Rule 11's reasoning, Kain's.
- **Speed:** no difference to the work we actually do. Rule 9's two commits per change set are local `git` operations and take milliseconds.
- **What it would let me do that I cannot now:** open and merge pull requests, read and comment on issues, cut releases, and read Actions results. We use none of these. The theme has no CI, no pull request workflow and no issue tracker; the repo is a single-branch history that Kain never reads directly.
- **What we would lose:** nothing functionally. We would gain a token on the machine that can reach every repository on the account.

## 3. The hooks, which is the part that matters

Neither route touches the five hooks, and both are equally safe on that count, for one reason: **the hooks fire on file edits, and neither `git` nor `gh` edits working-tree files in the course of what we do.**

- **H2's scope wall and H3's forbidden ground** intercept the edit tools. Anything that wrote files outside them would be a gap, and this session has already proved the wall holds even on a throwaway file in the scratchpad: it refused a temporary parse harness because the path was not on the declared list.
- **H4's gates** run after edits, on the changed files. `git commit` changes no file, so nothing is skipped.
- **The one real gap either route could open** is a command that rewrites the working tree behind the hooks: `git checkout`, `git reset --hard`, `git stash`, or `gh pr checkout`. Those replace file contents with no edit tool involved, so no hook sees them and no gate runs on what lands. That gap exists **today**, with plain `git`, and `gh` neither widens nor narrows it.

That last point is worth a ruling on its own, separately from this question. It is also why the permissions allow list I have proposed keeps every destructive and history-rewriting command in the ask-every-time list.

## 4. Recommendation, one line

**Stay on plain `git`; do not install `gh`,** because it buys us nothing we use and puts a broad-scoped GitHub token on a machine that also holds live-site SSH access, which is a worse trade than the convenience is worth.

If Kain later wants pull requests, releases or Actions, that reverses cleanly and `gh` is the right tool for it then. Nothing here is urgent and nothing is blocked.

*No em or en dashes in this file; checked before writing.*
