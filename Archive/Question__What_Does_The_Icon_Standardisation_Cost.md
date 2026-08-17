# Question for Code — what does the icon standardisation actually cost?

From: Claude Chat · S217 · 2026-07-23
This is a question, not a brief. Nothing is being commissioned here.

---

## The decision this unblocks

DSRD 10 §7 requires named Lucide icons only — `<i data-lucide="icon-name"></i>` — and prohibits raw SVG paths in PHP templates. The theme currently carries roughly **178 raw inline SVGs**. That gap has been sitting on Kain's decision list for several sessions and keeps rolling forward, because nobody has been able to tell him what closing it would cost.

He is not going to rule on it in the abstract. So the honest move is to ask you first, and I have carried it forward as a pending decision whose trigger is your answer.

---

## What would actually help

Rough numbers are fine. Precision is not the point — the point is whether this is an afternoon or a fortnight.

1. **The real count.** How many raw inline SVGs are there, and across how many files? My 178 is inherited from an earlier report and I have not verified it.

2. **How many are distinct.** 178 occurrences of twelve icons is a very different job from 178 different glyphs. If most are the same handful repeated (ChevronRight, House, ArrowRight), that changes the answer completely.

3. **Whether every one has a Lucide equivalent** already in the DSRD 7 §5.2 registry, or whether some are bespoke marks — the Achology bubble watermark, the rainbow stripe, anything drawn rather than chosen.

4. **What the conversion actually costs**, in your terms: is it mechanical find-and-replace, or does each site need judgement about size, stroke and colour? And does anything break — inline SVGs styled by CSS that a Lucide element would not inherit?

5. **Whether it is worth doing at all before launch.** You build these templates. If your view is that the current inline approach is fine and the rule is the thing that should bend, say so plainly — that is a legitimate answer and Kain would rather hear it than have the rule quietly ignored.

---

## Why it is being asked now rather than acted on

Kain's standing position on this is that he will not rule without knowing the cost, and I would rather ask you than estimate it myself. Two hours ago in this session I answered a question by reasoning from a document that did not govern it, and produced a confident, well-structured, wrong answer. Guessing at your build costs would be the same mistake in a different coat.

No urgency. Answer it in whatever session you next run.
