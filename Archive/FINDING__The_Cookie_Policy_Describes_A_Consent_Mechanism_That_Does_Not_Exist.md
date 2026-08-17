# FINDING: the Cookie Policy describes a cookie banner and a footer settings link, and neither exists

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.17.
**Found on:** page 4 of the S047 walk, https://achologytest.com/policies/cookie-policy/
**Needs:** a decision about what is being built, before this page can be called ready. This is the largest thing the walk has found, and it is not a design or a copy matter.

## What the page tells a reader

Four statements, quoted from the live page this turn:

1. "Non-essential cookies (the analytics cookies above) are set only if you consent through the cookie banner shown on your first visit, as required by UK law (the Privacy and Electronic Communications Regulations and UK GDPR)."
2. "You can change your mind at any time: reopen the cookie settings via the link in the site footer and update your choices."
3. A named row in the strictly-necessary table: "Cookie-consent preference. Remembers the cookie choices you made in our banner, so we do not ask on every visit. Up to 12 months."
4. "we rely instead on the explicit choices you make in our cookie banner, which we are required by UK law to honour."

The page also lists `_ga` and `_ga_*`, set by Google Analytics, "set only with your consent".

## What is actually there

Measured on the rendered page this turn, not inferred:

| Claim | Reality on achologytest.com |
|---|---|
| A cookie banner on first visit | **No banner exists.** Every candidate my scan returned was the policy's own body text describing one. There is no consent interface on the page. |
| A cookie settings link in the site footer | **Not present.** I listed all 38 footer links. The only cookie link is "Cookies", pointing at `/policies/cookie-policy/`, which is this page itself, not a settings control. |
| A cookie-consent preference cookie | `document.cookie` returns nothing readable. |
| Google Analytics `_ga` cookies | **No third-party scripts load at all.** The page requests zero scripts from any host other than achologytest.com. |

## The honest reading, including what is in the page's favour

Two of these have an innocent explanation and one does not.

**The missing analytics is correct and expected.** This is the build ground, and the standing rule is that it is never connected to Google or any live service. `_ga` being absent here proves the rule is being kept, not that anything is broken.

**The missing banner and settings link are a different matter.** They are site machinery, not a live-service connection, and nothing about being a build ground requires them to be absent. The policy states them as present fact, in the present tense, to a reader.

I also ran the same check against the live www.achology.com homepage and found no consent-platform token in the delivered markup. I am reporting that as indicative only, not as a conclusion: one fetch of one page is not a survey, and the response could be partial or cached. **Somebody should confirm the live position properly before anyone acts on it**, because if the live site genuinely has no consent mechanism while its cookie policy says it does, that is a live compliance exposure on the running business rather than a build-site defect, and it is well outside anything I should be deciding.

## Why this matters more than a wording slip

DSRD 6 section 11 exists for exactly this. Its opening line: "Every chapter before this one measures the page against a document. This one measures it against reality. The two are not the same thing, and the difference has already cost us." A cookie policy is the one page on a site whose entire value is that its description of the mechanism is true. Here the description and the mechanism disagree, and no gate we own could have caught it, because every gate checks whether the page is built correctly, never whether what it says is so.

## What I have not done

I have not touched the copy (Rule 8), and I have not built a consent banner. Which direction this goes is a decision with legal and product weight:

1. **The banner and settings link get built**, and the policy becomes true. That is a real piece of work, it needs a consent mechanism chosen, and under Rule 11 any outside library for it is Kain's decision rather than mine, because this site takes card payments.
2. **The policy is rewritten** to describe what the site actually does. That is Chat's copy work, and it needs someone competent to confirm the rewritten position is lawful.

Either way the page cannot pass DSRD 6 until one of them happens, so I have recorded section 11 as a fail on this page and carried on walking rather than waiting.

*No em or en dashes in this file; checked before writing.*
