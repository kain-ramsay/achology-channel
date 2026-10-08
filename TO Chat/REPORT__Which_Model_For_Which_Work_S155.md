**Needs from Chat: read before the S416 decision; Kain wants a rule for which Claude model does which work ("I don't know if we're working optimally yet from a token usage perspective"), to write into the Project Instructions and the lane set-up on his yes. For the factory session.**

# REPORT: which model for which work (Code, S155 close)

**From:** Claude Code, S155, 8 October 2026; research by a read-only agent from Anthropic's own documentation only, fetched today (sources below). **For:** Chat and the S416 joint session. **Board card:** "Volume work without Cowork" (Project Delivery Systems).

## The answer

Use **Opus 5.5 at medium effort** as the main working model. Hand bulk and routine work to **Sonnet 5.5**, and quick lookups and mechanical jobs to **Haiku**. Keep **Fable 5.1** for rare, very hard, multi-hour problems: on Max it "use[s] them faster than other Claude models" and is capped at 50% of the weekly limit; on Pro it is billed to usage credits. **A correction to the model list:** Anthropic released **Haiku 5.5 on 7 October 2026**; Haiku 4.5 is now legacy, and in Claude Code the `haiku` alias points to Haiku 5.5 from version 2.1.293. Usage in claude.ai and Claude Code comes out of one shared allowance.

## What the docs say (API prices per million tokens, input then output)

- **Fable 5.1:** "demanding reasoning and long-horizon agentic work". Slowest. $10 / $50. 1M context.
- **Opus 5.5:** "long-running agentic coding and knowledge work". $4 / $20. 1M context. Default effort medium. "performs at the level of Claude Fable 5.1 on most work".
- **Sonnet 5.5:** "best combination of speed and intelligence". Fast. $2 / $10. 1M context. Opus is "clearly stronger at complex, open-ended work requiring sustained judgment".
- **Haiku 5.5:** "high-volume, latency-sensitive tasks". Fastest. $0.10 / $0.50 up to 100K input tokens, $0.50 / $2.50 above.

| Kind of work | Model | Why (Anthropic's words) | How it is set in Claude Code |
|---|---|---|---|
| Theme coding with careful visual work | Opus 5.5, medium; high for tricky bugs | "start at `medium`"; `high` for "fixing a bug in an existing codebase" | `/model opus`, `/effort medium`; or `"model"` and `effortLevel` in settings |
| Volume content lanes and workflows | Sonnet 5.5 for the writing agents; Opus 5.5 only as the lead that plans and merges | "content creation" is a Sonnet use; "Use Sonnet for teammates"; a strong lead with Sonnet workers measured 47% to 55% lower cost | `CLAUDE_CODE_SUBAGENT_MODEL=sonnet` in settings `env` (with `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` to force it), or `model: sonnet` in each agent file |
| Mechanical edits, renaming, link fixes, reading and summarising | Haiku 5.5 | "quick lookups, simple edits, or high-volume scripted runs"; "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent" | `model: haiku` in the agent file |
| Reviewer passes against the long Standard | Sonnet 5.5; Haiku only where the check is pass or fail | Haiku fits work "with checkable outputs" (85% against Opus's 91% on one test); above 100K input tokens Haiku's price rises fivefold | `model: sonnet` in the reviewer agent |
| Planning and briefs in claude.ai | Opus 5.5 at lower effort; Fable only for the hardest decisions | "start with Claude Opus 5.5 for most workloads"; "Choose a lower effort level for routine tasks" | The claude.ai model picker |
| Research agents | Sonnet 5.5; Haiku for simple lookups | Anthropic's research measurements ran workers on Sonnet | `model: sonnet` in the agent file |

A hybrid exists: `opusplan` "uses `opus` during plan mode, then switches to `sonnet` for execution". `workflowSizeGuideline` caps how many agents a workflow aims for.

## What it could save

Per token, Sonnet 5.5 is half the price of Opus 5.5, Fable 2.5 times Opus, Haiku 5.5 a twentieth of Sonnet for inputs under 100K. Opus 5.5 at medium matched Fable on one coding test "for about a fifth of the cost per solved task". Agent teams "use approximately 7x more tokens than standard sessions". **The saving on Kain's plan cannot be quantified from the docs** (the support article says only "Opus costs several times more per turn than Sonnet, and Sonnet more than Haiku"); Anthropic warns a mixed setup that looks cheaper "often cost more than that same model at lower effort". Test one batch and read `/usage`, which shows the share used by subagents.

## Could not verify

Kain's plan tier and Claude Code version (the `haiku` alias means Haiku 5.5 only from 2.1.293; iMac 4's Claude Code is 2.1.293, read at S155); whether the claude.ai picker offers Haiku 5.5 yet; any separate Sonnet-only weekly limit on Max; Sonnet 5.5's default effort (the overview says high, Claude Code's docs say medium); no announcement page for Fable 5.1 found.

## Sources

platform.claude.com/docs/en/about-claude: models/overview, models/choosing-a-model, models/optimizing-for-cost-and-intelligence, pricing; code.claude.com/docs/en: model-config, sub-agents, workflows, costs, commands; anthropic.com: news, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5; support.claude.com articles 15424964, 11049741 (Max plan), 8325606 (Pro plan), 14552983 (models, usage and limits in Claude Code), 11647753 (usage and length limits), 11145838 (Claude Code with Pro or Max).

OWED BACK: Chat folds a model rule into the S416 decision and, on Kain's yes, the Project Instructions; Code sets the lane agents' models in the lane set-up.

*No em or en dashes in this file; checked before writing.*
