**Needs from Code:** read this before starting or setting up any more cloud work: Routines and Projects do not spend the $250 credit, and here is how to prove a run was a cloud run.

# NOTE: routines and Projects do not spend the credit, and how to prove a run was in the cloud

**From:** Claude Chat, S394, Thursday 1 October 2026. **To:** Claude Code.
**Adds to:** `BRIEF__Find_And_Commission_The_Cloud_Work_For_Kains_250_Credit_S394`. Kain asked how to confirm that the jobs really run in Anthropic's cloud, and said you are trialling a few and cannot see the credit balance.

## 1. A correction to my brief

My brief did not say this, because I had not found it yet. **Several sources report that the $250 credit is for ordinary cloud sessions only, and excludes Routines and Projects.** They quote the claim screen and Anthropic's offer terms. I could not open Anthropic's own offer page, so check the claim screen text at claude.ai/code/claim-credit yourself. Routine runs still execute as cloud sessions, but if the exclusion is as reported they draw on Kain's own plan, not the credit.

**So: do not use Routines or Projects for this work. Start plain cloud sessions.** Ways to start one, from Anthropic's documentation (code.claude.com/docs/en/claude-code-on-the-web): the browser at claude.ai/code, the Code tab in the mobile app, the desktop app with Cloud selected instead of Local, or `claude --cloud` in the terminal. If you have already set up routines, stop them until you have read the claim screen.

## 2. Local and cloud look alike. Do not confuse them.

Remote Control (`claude remote-control`) also shows up at claude.ai/code, but it drives a session running on your machine; nothing moves to the cloud and it spends the allowance. Scheduled tasks can also run locally. A session in the claude.ai/code list is not proof of cloud by itself.

## 3. How to prove a run was a cloud run (from the documentation)

- Each cloud session has a transcript URL on claude.ai.
- Commits made in a cloud session carry a `Claude-Session:` trailer holding that URL.
- Inside a cloud VM the environment variable CLAUDE_CODE_REMOTE is true and CLAUDE_CODE_REMOTE_SESSION_ID is set. The documentation says CLAUDE_CODE_REMOTE is never true locally. Ask the session to print both as its first act.

## 4. Where the credit balance shows: not found

I found no Anthropic page that says where the remaining promotional credit is displayed, and your local `/usage` is reported to count only sessions on that machine, so it will not list cloud work. One source states that whether the credit is spent before the plan allowance is not confirmed by the sources it saw; most sources say it is spent first and automatically.

**A test that gives evidence, not proof.** Read the weekly usage figure at claude.ai, Settings, Usage. Start one plain cloud session (not a routine) on Job 1. When it finishes, read the figure again. If it has not moved while the session did real work, the credit paid; if it moved clearly, the plan did. Say in your report that this is evidence, and whether the page updated at once. If the page shows a promotional credit line, say so. If nothing shows a balance, put the question to Anthropic support in one sentence: where can a Max subscriber see the remaining Claude Code cloud session credit?

## 5. Effect on the brief

Your six questions stand. Add a seventh: **do Routines and Projects spend the credit?** (Chat's reading: no.) Do not start the weekend batch until questions 2, 3 and 7 are answered from the claim screen and one tested session.

*No em or en dashes in this file; checked before writing.*
