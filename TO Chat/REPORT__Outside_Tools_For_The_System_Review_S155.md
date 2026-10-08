**Needs from Chat: read before the S416 decision (Step 2 of NOTE__S416_Joint_Session); it changes where lanes can run. Kain asked for it ("a full review of our full system ... repositories ... top Claude users recommending"). For the factory session. Nothing here is installed; every third-party item needs Kain's yes.**

# REPORT: outside tools and Anthropic features for the system review (Code, S155 close)

**From:** Claude Code, S155, 8 October 2026, research by a read-only research agent against the live web (Anthropic's Claude Code docs and each repository's GitHub record, fetched today). **For:** Chat, and the S416 joint session. **Board card:** "Volume work without Cowork" (Project Delivery Systems).

## The three findings that matter most for "hand over a batch, walk away"

1. **Anthropic has a built-in feature for exactly this: dynamic workflows.** Claude writes a short script that sends one helper agent to each file, checks their work against each other, and runs in the background; it can be paused and resumed, and if the plan's usage limit is hit it waits for the reset and carries on. This is the nearest thing to what Cowork did, and it runs inside Claude Code on the iMac Pro. (Code's own tools say a workflow runs only when Kain asks for one, in his words.)
2. **Claude Code Projects is the closest match to "walk away and come back".** One conversation starts separate cloud sessions ("threads") that keep running with the Mac off, with an Overview screen of what is done and what is waiting. Public beta on Pro and Max, reaching accounts gradually; accounts that already hold claude.ai or Cowork projects come later, which probably includes Kain's.
3. **A lane only finishes reliably alone if it has a pass or fail check it can run** (a style checker, the gate script, or the `/goal` command). Anthropic's best-practice guide calls this the difference between a session you watch and one you can walk away from. For content: the mechanical rules of The Achology Content Standard become a check.

## Candidates

**Part A: built into Claude Code**

| Name | What it does | Why it helps | Status | Risk or cost | Verdict |
|---|---|---|---|---|---|
| [Dynamic workflows](https://code.claude.com/docs/en/workflows) | Runs many helper agents from a script | A batch of 200 records: one agent per file, plus a reviewer | All paid plans; on Pro, switched on in `/config` | Uses plan limits fast; the auto-wait at a limit works only in an open session | Trial first, on 10 records |
| [Projects](https://code.claude.com/docs/en/claude-projects) | One conversation that runs cloud workers | Survives the Mac being off; Overview screen | Public beta, rolling out | Needs the Claude GitHub App on the repo; uses limits faster | Use when it reaches Kain |
| [Agent view and background sessions](https://code.claude.com/docs/en/agent-view) | Background lanes on the Mac | Keep running when the window closes and through sleep | Research preview | Deleting a session deletes its folder, unsaved work included | Trial first |
| [`/goal`](https://code.claude.com/docs/en/goal) | A separate model checks after every turn whether the finish condition is met | "Keep going until every file in batch 7 passes the check" | Available now | Small extra cost | Use now |
| [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging) | Sessions send each other plain-text notes, across machines through Remote Control | Quick nudges between the iMacs; the git channel stays the record | Available now | A message can never approve anything; ask before messages cross machines | Trial first |
| [`/usage` and `/insights`](https://code.claude.com/docs/en/costs) | Plan usage bars and what used them | Shows which lane eats the allowance (the weekly count Chat's void 7 asks for) | Available now | Counts only this machine | Use now |

**Part B: third party**

| Name | What it does | Why it helps | Stars, last push | Risk or cost | Verdict |
|---|---|---|---|---|---|
| [Vale](https://github.com/errata-ai/vale) | Offline style checker for prose, with our own rules | The Standard's mechanical rules (dashes, banned words, acronyms) as a pass or fail check | 6.2k, 6 Oct 2026, MIT | Rules take effort to write; never touches the site | Use now on the content repo, on Kain's yes |
| [CC Safety Net](https://github.com/kenryu42/claude-code-safety-net) | Blocks destructive git and file commands before they run | A second guard for unattended lanes | 1.6k, 8 Oct 2026, MIT | Full shell rights | Trial first, Kain approves |
| [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Curated list of Claude Code resources | A vetted reading list | 55k, 8 Oct 2026 | Nothing installed | Read only |
| [Notion MCP](https://github.com/makenotion/notion-mcp-server) | Official Notion connection | Already attached to the account | 4.7k, 20 Sep 2026, MIT | None new | Already have it |
| [ccusage](https://github.com/ccusage/ccusage) | Usage reports from local logs | Overlaps with `/usage` | 18.9k, 8 Oct 2026 | Low | Skip |
| [Backlog.md](https://github.com/MrLesk/Backlog.md) | Task board as Markdown in git | Task claiming in the repo | 7k, 7 Oct 2026, MIT | A third task system beside Notion and the channel | Skip for now |
| [claude-mem](https://github.com/thedotmack/claude-mem) | Session memory service | Memory across sessions | 98k, 7 Oct 2026 | Background service, signs in to a hosted service by default; conflicts with "memory is not a source" | Skip |
| [Superpowers](https://github.com/obra/superpowers) | Skills enforcing a software method | Aimed at code projects | 297k, 8 Oct 2026 | Its start-of-session hook would collide with the harness | Skip |
| Claude Squad, Task Master, Spec Kit | Terminal session manager; spec-to-task tool; spec-first kit | Built for software teams; the desktop app covers the session side | 8.6k, 141k, 28k | Terminal; restrictive licence on Task Master; Claude Squad AGPL | Skip |

## Official features already covering parts of this

- **Parallel local lanes**: the [desktop app](https://code.claude.com/docs/en/desktop) runs several sessions at once, each optionally in its own copy of the files (a worktree); they keep working while the app is open and the Mac is awake. On the iMac Pro, **Keep computer awake** under Settings, This computer, System ([details](https://code.claude.com/docs/en/desktop-scheduled-tasks)).
- **Bulk edits**: `/batch` splits one change across 5 to 30 helpers, each in its own copy ([best practices](https://code.claude.com/docs/en/best-practices)).
- **Scheduling**: [routines](https://code.claude.com/docs/en/routines) run in the cloud with no permission prompts, at most hourly; [desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) run locally and skip runs while the Mac sleeps.
- **Cloud sessions** ([docs](https://code.claude.com/docs/en/claude-code-on-the-web)): the docs say no separate charge for the cloud machine and that cloud sessions share the plan's limits. What Kain's $84 credit pays for is not confirmed.

## Security

- Anything installed on iMac 4 runs with Claude Code's rights, which include the SSH route to a site that takes card payments. No third-party hook, plugin or MCP server goes on iMac 4 without Kain's explicit yes (Harness Rule 11).
- Routines and Projects run without permission prompts: give them the content repository only, never the theme repository, SSH keys or WordPress credentials.
- Projects needs the Claude GitHub App on each repository it works on: install it only on the ones volume work needs.
- **A void for Chat's list:** worktrees are created inside the project folder, which sits in iCloud-synced Documents, so iCloud would also sync every lane's copy, a third road on top of git and iCloud. Volume-lane checkouts belong in a folder iCloud does not sync, or in cloud lanes.
- Deleting a background session deletes its copy of the files: every lane commits before it finishes.

**Could not verify:** release dates beyond each repository's last push; what the $84 credit pays for; whether Projects has reached Kain's account.

## Sources

code.claude.com/docs/en: agents, workflows, claude-projects, agent-view, goal, cross-session-messaging, costs, claude-code-on-the-web, routines, scheduled-tasks, desktop-scheduled-tasks, best-practices; support.claude.com article 14554000 (search result only); the GitHub pages and API records of every repository named above, plus Maciek-roboblog/Claude-Code-Usage-Monitor and disler/claude-code-hooks-mastery (read, not recommended).

OWED BACK: Chat folds what it accepts into the S416 decision; Kain says yes or no to each "use now" or "trial first" item before anything is installed.

*No em or en dashes in this file; checked before writing.*
