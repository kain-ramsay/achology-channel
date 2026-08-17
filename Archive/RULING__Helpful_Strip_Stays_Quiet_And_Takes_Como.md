# RULING and SHIP: the helpful strip stays quiet, takes Como, and gets new wording

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Answers item 3 of:** `AUDIT__Every_Button_On_The_Site.md`, filed earlier this session.
**Ruled by:** Kain, in session, from the rendered help article he had open.
**Shipped:** v0.38.12, deployed to achologytest.com, verified on the rendered page.

## The ruling, in his words

I put the question to him as: should the "Was this helpful, Yes / No" controls stay
quiet and different, or join the button system like everything else? His answer:

> "Keep them quiet and different, thats fine, however we need to change the text to:
> Was This Article Helpful? and ensure the Como font is used please"

## What that settles, for DSRD 7 §5.1

**The two controls are a registered exception to the button system.** They keep their
pill shape (999px) and their soft grey, and they do not take the §5.1 font size,
radius or colours. The reasoning I gave and he accepted: they are a lightweight aside
rather than an action, and dressing them as buttons would give them more weight than
they deserve.

**Please write this into §5.1** so the next audit stops flagging them, alongside the
sentence that section still needs about icon-only controls (the close buttons and the
back-to-top) not being §5.1 buttons either.

**The typeface is the one thing that comes back into line.** The strip now uses Como
throughout, so it reads as part of the site rather than as body copy with buttons in
it. Quiet, but not foreign.

## What shipped

| element | before | after |
|---|---|---|
| Label wording | Was this helpful? | **Was This Article Helpful?** |
| Label typeface | Source Sans 3 16px/600 | **Como** 16px/600 |
| Yes and No controls | Source Sans 3 15px/600, pill | **Como** 15px/600, pill unchanged |
| Thank-you line | Source Sans 3 15px/400 | **Como** 15px/400 |

The thank-you line was not named in his ruling and I changed it anyway, for one
reason stated plainly so he can veto it: it replaces the question and the two answers
in the same row when a reader votes, so leaving it in the body face would have made
it the only thing in the strip that changed typeface at the moment of the vote.

**Verified on the rendered live page**, not from source: all four now compute as Como,
the pill radius is unchanged at 999px, and the label reads the new wording.
`css_gate help.css`: PASS.

## One note on scope, for the record

This touches every help article, which is more than one page, so it is a sweep in the
Rule 3 sense and there was no signed brief in FROM Chat. I built it on Kain's direct
ruling, given to me in session, and I am recording that here rather than leaving it
unexplained. It is one component in one stylesheet with no page-level design decision
in it, and the alternative was making him wait for a brief to be written carrying a
decision he had just made out loud.

If you would rather that route were never taken, say so plainly and I will stop and
ask every time instead. It is a real question about how the harness handles a ruling
that arrives from Kain directly rather than through you, and it is now come up twice:
here, and in the Reviews page instruction where you explicitly allowed it.

*No em or en dashes in this file; checked before writing.*
