# QUESTION: GitHub CLI instead of the GitHub MCP, and what changes if we switch

**From:** Claude Chat, S235. **Date:** 2026-08-03. **A question only. Nothing is being changed on this until you answer.**

## Context, standalone

Kain saw an explainer arguing that Claude Code should work through the GitHub CLI (`gh`) rather than a GitHub MCP server, and asked whether that holds for this project. Chat cannot answer it, because the answer depends on what your environment actually has and how you actually touch the repo today. The repo is `github.com/kain-ramsay/achology-theme`, currently around v0.36.x, and harness Rule 9 requires one commit immediately before and one immediately after every change set.

## The question

1. What do you use for GitHub work today, `gh` on the command line, a GitHub MCP server, plain `git`, or a mix? Name what is actually installed and running, not what could be.
2. If a switch to `gh` is available to you, what concretely changes: token use, speed, what you can do that you cannot do now, and anything you would lose.
3. Does either route interact with the five hooks, particularly H2's scope wall and H4's automatic gates? A route that writes files outside the hooks' reach would be a harness gap, and Chat needs to know that before anything moves.
4. Your recommendation in one line, with the reason.

Answer through TO Chat whenever a Code session next runs. This blocks nothing.

## One thing to be clear about

This is a request for your assessment. Do not install, switch, or reconfigure anything. If your answer is that a switch is worth making, it comes back to Kain as a decision, and any change to how the repo is touched is a harness matter that Chat writes with his approval.

No em or en dashes in this file, checked before writing.
