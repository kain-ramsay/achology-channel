> **CODE DISPOSITION, S134: WAITS ON Code's answer file in TO Chat (the five questions and the one-page cloud test); queued behind the 42-article sweep finishing.**

**Needs from Code:** find out whether this week's page builds can run as Claude Code cloud sessions on Kain's $250 credit, and if so, set it up and tell Kain exactly what to do. Kain has approved this work himself, live in Chat.

# BRIEF: run this week's Code sessions in the cloud, on the $250 cloud session credit

**From:** Claude Chat, S385, Thursday 24 September 2026. **To:** Claude Code.

## What Kain wants, in his words

Kain is running low on his weekly plan allowance. Anthropic has given him a one-time $250 credit for Claude Code cloud sessions. Nearly all his Code work over the next week or so is building web pages. He is about to start a new Code session anyway, so he wants to start it in the cloud, on the credit, and keep his own weekly allowance for Chat and Cowork. He wants it made simple for him: **you find the solution and tell him the exact steps.** He is not technical; plain words, one step at a time.

## What Chat found (third party reports plus Anthropic docs, so please verify at code.claude.com and support.claude.com, not on my word)

- A cloud session runs Claude Code on Anthropic's machines. It starts from a fresh clone of a GitHub repository (or an uploaded bundle of a local repo with no GitHub remote, under 100MB, and results cannot then be pushed back to a non-GitHub host). It does not get the personal setup files on Kain's Mac.
- Ways in: claude.ai/code, the Claude mobile app, the desktop app with Cloud chosen instead of Local, and `claude --cloud` in the terminal.
- Reported credit terms: one per account, cloud sessions only, applies automatically once a cloud session starts, spent first and then normal plan limits apply again. Routine runs are reported as excluded. Reported claim deadline 7 October, credit expiry 4 November, claimed by link or `/claim-credit`. Please confirm all of that. **Kain confirmed in Chat that he has already claimed the credit (S385), so you do not need to ask him.**
- Cloud Cowork exists but is not covered by this credit as far as I can find, and local folder projects are desktop only, so Cowork stays where it is.

## What you need to find out

1. Is the theme repository on GitHub, and can a cloud session clone and push to it?
2. What does a cloud session lack that our work depends on: the channel folder, the DSRDs (their home is a folder on Kain's Mac), the skills, The Harness hooks and the independent evaluator on your machine, the gate scripts, `previews`, credits.json? For each, is it in the repo, can it be, or does the cloud session do without it?
3. Can a cloud session deploy to the live site, or does deploy stay a step only your Mac can do? Is there a safe way to pay the credit for the build and keep deploy and the Safari sitting with Kain local?
4. Does the Harness still bind a cloud session? If not, which of its checks can be moved into the repo so a cloud build still has to pass them before Kain sees a page? If a page cannot be gated in the cloud, say so plainly.
5. Which of this week's page builds are self contained enough for the cloud (a signed spec in, a built page and its DSRD 6 record out), and which need your Mac?

## The test

Before this week's work rides on it: pick the smallest page with a signed spec, run it as one cloud session, and stop before anything reaches the live site unless you can show deploy is safe. Report what worked and what was missing.

## What Kain needs back

A short plain answer in TO Chat: yes or no it can work, the exact steps for Kain to start the cloud session (numbered, no jargon), what stays local, and anything in it that needs his decision, put as a yes or no question. If it cannot work, say why and what the closest workable version is.

## OWED BACK

The answer above, and the test result.

*No em or en dashes in this file; checked before writing.*
