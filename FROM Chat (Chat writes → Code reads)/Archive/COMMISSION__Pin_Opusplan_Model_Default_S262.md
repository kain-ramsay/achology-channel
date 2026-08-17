# COMMISSION: pin opusplan as your project default model

**From:** Claude Chat, S262, on Kain's ruling this session. **Date:** 2026-08-11.
**For:** Claude Code. Approved brief, small and one-shot.

## Context, standalone

Kain ruled at Chat's S262 that Code sessions run on the opusplan model setting: the strongest model while you are in plan mode working out the approach, switching automatically to Sonnet for execution. Your work under Harness Rule 8 and standing rule 19 is execution against signed specs, which is exactly the work the economical tier is for, and every token your execution does not draw from the shared all-models cap is capacity kept for the whole project. The ai-collaboration skill on Chat's side records this routing from S262.

## The work

1. Pin `"model": "opusplan"` in this project's Claude Code settings file (`.claude/settings.json` at the project level), so it holds every session without anyone typing a command. If a settings file already exists, add the field; do not disturb anything else in it.
2. Confirm in your next TO Chat note that it is pinned and that a session opened on it.

## One escalation rule that comes with it

If a build fails its gate twice on the same piece of work, run the next attempt one model tier up before touching the approach. This mirrors the content-production escalation already ruled. Note the escalation in your session record when it fires.

## Bounds

Settings change only. No other configuration is touched.
