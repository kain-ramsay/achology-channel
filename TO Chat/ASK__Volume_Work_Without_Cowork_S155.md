**Needs from Chat: one decision with Kain, before anything else (his words: "I really don't want to focus on anything apart from solving this one problem"): where Cowork's volume work now runs so it works unattended. Code's facts and proposal are below. For the factory session.**

# ASK: volume work without Cowork, run unattended (Code, S155 close)

**From:** Claude Code, S155, Thursday 8 October 2026. **For:** Chat. **Board card:** none yet (Project Delivery System).

## The problem, in Kain's words

"what we need to happen is for Cowork to be given a task, she'll put agents towards it and then deliver, because we have hundreds of articles to edit and write. So this isn't a manual thing that I need to sit and watch ... when a Cowork item is run in chat now, if I leave that chat, it ... says, I don't have access to the computer anymore ... Chat cannot deliver a Cowork session of volume work."

## What changed (news reports, read S155; Chat to confirm against Anthropic's own announcement)

Cowork was folded into the normal Claude chat: no separate mode, Claude decides the tools per request; existing Cowork chats, projects, connectors and skills stay; rolling out account by account. The capability that matters here, a long task that keeps running while Kain is elsewhere, is what breaks when it runs inside a chat window.

## Code's proposal: volume work runs in Claude Code, which is built for exactly this

1. **A Claude Code session keeps working when Kain leaves it.** In the desktop app several Code sessions run side by side; Kain can talk to Chat or to another Code session while a lane works. Nothing needs watching.
2. **One Code session can put agents on a batch.** It can split a batch across sub-agents working in parallel (Code's agent and workflow tools; a workflow runs only when Kain asks for one), then gather, check and deliver: Cowork's own pattern.
3. **Two places a lane can run:**
   - **On the iMac Pro, as local Code sessions (Lanes A, B, C).** The machine must stay awake. The record and channel arrive by git, as today.
   - **In the cloud, as Claude Code cloud sessions.** They run on Anthropic's machines against the GitHub record (`achology-record`), keep going with both Macs asleep, and return branches to merge. Kain's $250 cloud credit (expires 5 November 2026) is meant for exactly this. Code recommends trying one lane in the cloud on a small batch first, and comparing it with a local lane.
4. **Chat stays where it is**: planning, the board, the channel, reading the lane reports.

## The voids Code sees, each needing a decision

1. **One road for files.** The project folder sits in iCloud-synced Documents and is also a git repository autosaved hourly. If lanes on another machine or in the cloud also write, two roads touch the same files. Proposal: git is the only road for the lanes; nothing writes content through iCloud.
2. **The rules must load in a lane.** The hooks call `/Users/kainramsay/.claude/achology_hook.py` on iMac 4; on the iMac Pro they fire only if that launcher exists at that path, and in the cloud they do not exist at all. The Cowork Production Harness must be in what the lane reads at open (a CLAUDE.md in its folder), and the content gates must run as commands the lane calls, not as hooks.
3. **The run list.** Cowork read `000__NEXT__What_Cowork_Runs_Next.md` in TO Cowork. Each lane needs its own line in it, so two lanes never take the same batch.
4. **Reporting.** Each lane writes its batch report into the channel (git), so Chat reads it and marks the board, exactly as now.

## The one question

Does Chat agree that volume work runs as Claude Code lanes (local on the iMac Pro, or cloud, tested side by side on one small batch), with git as the only file road and the Cowork Production Harness loaded as the lane's CLAUDE.md? If yes, Code writes the lane set-up for Kain's one-click start in a fresh session.

## OWED BACK

Chat's yes or no, with any void Code has missed.

*No em or en dashes in this file; checked before writing.*
