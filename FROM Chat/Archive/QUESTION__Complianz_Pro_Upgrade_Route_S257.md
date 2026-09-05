# QUESTION: how do we move achologytest.com onto the paid Complianz licence?

**From:** Claude Chat, Session 257. **Date:** 2026-08-10.
**Asked on Kain's instruction, in this session.** This is a question, not a commission: it asks for the route and its risks, and nothing is installed or changed until Kain has read your answer and said go.

## The situation

Kain has **already purchased Complianz Pro**. The licence is bought and in hand. What is not clear to him is how the upgrade is actually performed from inside WordPress: whether the free plugin takes a licence key and unlocks in place, whether Pro is a separate plugin that installs alongside or replaces the free one, what happens to the existing configuration during the swap, and whether any step needs doing in a particular order to avoid losing what is already set up.

He has no technical background, so the answer needs to arrive as plain steps with the risky moments named, not as a link to documentation.

## Why this is not a small question

The consent mechanism on the build site is **already built and verified**, and its status is recorded in DSRD 3 section 6.5 (Code S047, theme v0.38.21). Open that section and read it before answering, because it is the thing at risk. The footer's Cookie settings control is also involved: DSRD 8 section 19.8 records it as a ninth policy-row item, and DSRD 10 section 16 item 7 records the shortcode trap that made it work, where the wrong markup silently suppresses the banner site-wide.

So a plugin swap here is not a routine update. It touches a verified compliance mechanism, a footer control with a known trap behind it, and the GTM blocking behaviour. If the upgrade resets or migrates the configuration, everything DSRD 3 section 6.5 records as verified has to be re-verified afterwards, and the answer should say so.

## What I need back

1. **The route**, in plain steps Kain can follow or you can execute, whichever you recommend and why.
2. **What happens to the existing configuration** at each step: preserved, migrated, or reset.
3. **The licence key itself.** Say plainly who enters it and where. Kain enters his own credentials and licence keys; neither of us handles them.
4. **The risky moments**, named: anything that could take the banner down, unblock GTM, or break the footer control, and what the recovery is if it happens.
5. **What must be re-verified afterwards**, expressed as the checks in DSRD 3 section 6.5 that would need to run again, so we know the cost of the upgrade before it starts rather than after.
6. **Whether it should happen at all right now**, in your judgement. If the free version is doing everything the site actually needs and Pro's additions are not required before launch, say so: a verified working mechanism has real value and "not yet" is a legitimate answer.

## What not to do

Do not perform the upgrade in the session you answer this. Report the route, and wait: Kain decides whether and when, and his go travels back to you through FROM Chat as an approved brief. This is the same boundary as any other question through this channel.

*No em or en dashes in this file; checked before writing.*
