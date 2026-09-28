**Needs from Chat:** put the one yes-or-no question at the foot to Kain, and record the answer on the board.

# REPLY: can this week's page builds run in the cloud on the $250 credit? Not safely, as things stand

**From:** Claude Code, S135 (theme), Monday 28 September 2026. **Answers:** `BRIEF__Run_This_Weeks_Code_Sessions_In_The_Cloud_On_The_250_Credit_S385.md`. Anthropic facts read from https://code.claude.com/docs/en/claude-code-on-the-web and https://code.claude.com/docs/en/cloud-environments this session; our side read from the machine.

## The short answer

A cloud session could write theme code, but it would build pages with none of our safety checks running, no specs to read unless set up specially, no way to put the page on the test site, and no way to show Kain. Every page would have to come back to the Mac to be checked, fixed and shown anyway. For this week's page builds the saving is small and the risk is ungated work. **Code recommends keeping page builds local.**

## The five questions

1. **GitHub:** yes. The theme (`kain-ramsay/achology-theme`), the channel (`achology-channel`) and the project record with the DSRDs and design folders (`achology-record`) are three separate GitHub repositories. Docs: "The cloud VM clones your current directory's GitHub remote at your current branch".
2. **What a cloud session lacks:** the Harness hooks are wired in the record repo's `.claude/settings.json`, but they all call `~/.claude/achology_hook.py`, a file on the Mac only. Docs confirm a cloud session gets the repo's settings but not the user's own `~/.claude`. So no hook would run. The theme repo alone has no DSRDs, no signed specs and no design folders; those live in `achology-record`. Skills and memory are personal setup and do not travel.
3. **Deploy:** stays on the Mac. Deploy is SSH to SiteGround on port 18765 with a private key that exists only on the Mac. Docs: cloud network access is "limited by default" to package registries and allowlisted domains, with no mention of SSH to an outside server. Putting the site's private key into a cloud environment is a security decision, and Code does not recommend it.
4. **Does the Harness bind a cloud session:** no, not today. It could be made to by moving the hook launcher into a repo, but the hooks read across all three repos and the channel, so a cloud session would need all three cloned. That is a real piece of work and a change to the harness itself, which is Chat's and Kain's to rule.
5. **Which builds fit:** none of this week's page builds is self-contained. Each one needs the gate (a live browser on the test site), the deploy, and Kain in Safari.

## The credit

Anthropic's documentation does not mention a $250 cloud credit, a 7 October claim date or a 4 November expiry. The help centre shows only an Enterprise activation credit. Kain says he has claimed it, so it exists on his account; the terms are simply not in the public docs.

## The closest workable version

Use cloud sessions for self-contained work that touches no page and needs no deploy: reading and summarising, drafting channel answers, research, and scripts that are checked on the Mac afterwards. Keep theme builds, gates, deploys and every Safari sitting local.

## The one decision for Kain

**Keep all page building on the Mac, and use the cloud credit only for research and paperwork jobs?** Yes means that is the rule this week. No means Code scopes the work to make the Harness run in the cloud first.

## OWED BACK

Kain's yes or no. The test in the brief was not run, because the read above shows a cloud page build could not pass its own gate.

*No em or en dashes in this file; checked before writing.*
