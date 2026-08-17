# REQUEST: the button standard needs a design session with Kain, with rendered options

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Read with:** `AUDIT__Every_Button_On_The_Site.md` in this folder, which carries the
measurements and the contradictions in full. This file is the handover, not a repeat.

## Why this is coming to you rather than being built

Kain raised the button inconsistency himself, from his own eye, and asked for a
site-wide sweep as a priority. I audited it, found the code conforms and the documents
disagree, and stopped under Rule 8. Then I made a mistake worth naming: I put the
remaining decision to him **in words**, asking whether every button should be one size
or whether chrome buttons should stay smaller.

His answer, and it is the instruction here:

> "you just dump me walls of words, and I'm visual. So I need visual context for making
> this decision, which means this is gonna have to be a chat planning design session...
> I can't give an answer to your words without seeing anything."

He is right and this is a standing lesson, not a one-off. **A size decision cannot be
made from a description.** You can render; I can only render a real page after the
decision is already made. So this belongs with you.

## What the session has to settle

**One question, in visual terms: how many button sizes does this site have, and where
does each one belong?**

Everything needed to answer it is measured and in the audit file. The short version:

- DSRD 7 §5.1 defines a button's font, weight, radius and colours, and **never states a
  padding**. That single missing line is the root cause.
- Four different paddings are specified across the documents: 12px 24px (the `.btn`
  base in code), 9px 22px (§18.6 Sign In), 8px 16px (§18.12 nudge CTA), 12px 28px
  (§19.7 footer CTA).
- Two radii are specified: 10px in §5.1, §18.6 and §19.7, but **8px** in §18.12, with
  no exception noted anywhere.
- Two font sizes: 14px in §5.1, 13px in §18.6, again with no exception noted.
- §19.7 specifies the label "Start Your Trial ›" with a typed chevron, while §5.2 says
  every icon slot uses a named Lucide icon and improvised marks are prohibited. This is
  on the most-seen button on the site.

## What Kain needs to see, not read

My suggestion for the session, offered because you asked me to send outcomes rather
than opinions, and freely ignorable:

1. **The same page rendered twice**, once with every button at one single size, once
   with a standard size plus a smaller chrome size. Real page, real header and footer,
   not swatches. That is the actual decision and it is invisible in a table.
2. **The footer card button both ways**, with the typed chevron and with the Lucide
   arrow, side by side at real size. It is a small difference that repeats on every
   page of the site, which is exactly the kind of thing he reads instantly and I cannot
   describe.
3. **The header strip at its real height**, because the argument for a smaller chrome
   button is entirely about whether a full-size one fits and breathes there. That is a
   looking question.

## What I will do afterwards

One pass. Whatever he settles becomes §5.1's missing line plus a named variant list,
you reconcile §18.6, §18.12 and §19.7 to it or record each as an exception with its
reason, and I bring the code to the result and re-gate every page it touches. The code
is currently correct against its own specs, so nothing is urgent and nothing is broken
while this waits.

## One thing already settled, so it does not get reopened

The help article's "Was This Article Helpful?" Yes and No controls are a **registered
exception** and stay outside the button system: pill shaped, quiet, Como. Ruled by Kain
this session and filed in `RULING__Helpful_Strip_Stays_Quiet_And_Takes_Como.md`.

*No em or en dashes in this file; checked before writing.*
