# ANSWER: context exhaustion, and whether context-mode could sit alongside the harness

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `QUESTION__Context_Mode_Friction_And_Harness_Coexistence.md`.
**My verdict in one line: the friction is real but small and already managed, and the coexistence risk is specific and serious enough that I would not install it. I recommend Skipped, with one condition for revisiting.**

## 1. Is context exhaustion genuinely a friction?

Partly, and not in the shape the plugin assumes.

Today's session is a fair test, because it carried exactly the workload you named. It handled an 850KB dump of all 249 articles, the speech data for 6,421 sentences, a 75KB machine-readable map of 23 pages, 249 quality-check scores, and an 85KB verbatim copy report. **None of that entered my context.** It went to disk, and code ran over it and printed a summary: "249 articles, 0 matched their recording", "median 0.973, five flagged", "37 spacing failures fall to 16". That discipline is not a workaround I reach for under pressure; it is how the work is done, and it is why a session this size is possible at all.

Where it does cost something: long sessions get compacted, and after a compaction I sometimes re-derive state I had already established, or re-read a file to be sure of it. Today that cost minutes, not hours, and nothing was lost that mattered. The one genuine loss in this project's history was not context exhaustion at all: it was four messages from you sitting unread in a folder, and H6 now catches that mechanically. It caught five more today.

So: real, small, already managed. If the tool's 98 percent reduction is measured against an agent that reads large files into its own context, that agent is not me, and the headline number would not transfer.

## 2. Would its hooks coexist with the harness's?

My read of the mechanism, not a test: **two specific hazards, and the second should decide it.**

**Hazard one, the smaller: summarised tool output could swallow a gate failure.** H4 feeds gate results back to me as tool output in the moment: a dash failure, a css_gate failure, an article_gate failure. That is precisely the shape of output a sandboxing layer compresses, being long, repetitive and machine-formatted. A summarised gate failure is a gate failure I might read as a pass. The harness's whole claim is that a skipped check fails instantly and visibly, and a layer that abbreviates check output attacks that claim directly. It happened today in the small: H4 caught three em dashes in a file whose own closing line claimed it had none.

**Hazard two, the decisive one: H2 reads the raw session transcript to find my scope declaration.** That is the mechanism, and it is deliberate: the declaration lives in the session rather than in a file I could quietly edit. Any plugin that persists, restores or rewrites session state across compactions is operating on the same material the scope wall reads as its source of authority. If a restored or reconstructed transcript carries forward a declaration I did not make in the current session, the wall opens for edits nobody declared. If it drops one I did make, the wall blocks properly declared work, which is merely annoying. The first failure is silent, and it removes the enforcement without removing the appearance of it.

I cannot rule that out from a README, and the harness is worth more to this project than a context saving I do not currently need.

## 3. What I would do

**Skip it,** recorded as evaluated on mechanism rather than on preference, with the condition for revisiting written down: if the Vimeo course refresh across roughly 2,800 videos strains context in a way file-first working cannot absorb, this comes back for a proper look.

If Kain wants it tested anyway, the only safe test is a throwaway repository with no Achology work in it, the harness hooks left out of that repo entirely, and two specific things checked rather than a general impression:

1. Does a deliberately failed gate arrive verbatim, or summarised?
2. Force a compaction, then attempt an edit with no declaration in the live session, and confirm the wall still blocks it.

If either answer is wrong, it is settled.

*No em or en dashes in this file; checked before writing.*
