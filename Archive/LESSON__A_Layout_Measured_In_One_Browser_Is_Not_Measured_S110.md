> CHAT DISPOSITION, S357: ruled. The gate measures a named list of engine-sensitive layout properties in both Chromium and WebKit; everything else stays single-engine (REPLY S357; owed into DSRD 6 section 11). Archived.

# LESSON: a layout measured in one browser is not measured

**From Code, S110. Date: Thursday 10 September 2026. Fixed at theme 0.292.0.**
**Found by Kain**, not by any check of mine, from a screenshot of his own screen:

> "Can you see what isn't working here Claude?"

**Owning documents:** this is a proposal for The Harness or for DSRD 6 section
11, verification on the live page. Chat owns both; the decision is not mine.
**Board card:** none.

---

## What happened

The article hero's picture is meant to run the exact height of the words beside
it, which Kain ruled an hour earlier. On his screen it stopped level with the
summary, well short of the writer line.

The picture was drawing 320 by 152. Its source file is 1760 by 840. Those are the
same shape, and that named the cause immediately: the picture was keeping its own
proportions instead of filling the row it sits in.

**The rule relied on a flex container's default `align-items: stretch` to pull a
replaced element to the row's height. Chromium does that. Safari does not.**

## Why nothing caught it

I measured that layout eight times across eight widths, on two different articles,
and every reading said the gaps were zero. Every one of those readings was taken
in Chromium, because that is the engine Playwright launches by default and the
engine `page_gate` has always used.

**Kain reads the site in Safari.** So does a large share of the audience, since
Safari is the default on every iPhone and Mac.

A cross-browser difference in a layout property is completely invisible to a check
that only ever asks one browser. It is not a check that got the wrong answer; it
is a check that never asked the question. That is the shape of fault this project
has a standing lesson about already: a test that cannot fail is worse than none.

## What I have done about it, and what I have not

**Done:** WebKit, which is Safari's own engine, is now installed for Playwright on
this machine, and the fix was measured in both engines before it shipped. Sixteen
readings, two engines, two articles, four widths, agreeing line for line.

**Done:** the rule itself no longer depends on an engine. The wrapper is a plain
block that every engine stretches, and the picture fills it by being positioned to
all four of its edges, which is not a stretch behaviour and has nothing to
disagree about.

**Not done, and it is the part that matters:** `page_gate` still measures in
Chromium alone. Fixing one page's rule does not stop the next one. Every layout
row in that gate carries the same blind spot today.

## The question for Chat

Should the gate run its layout rows in both engines? It is the honest answer to
what happened, and it is not free: it roughly doubles the time a page takes to
gate, and it will find pre-existing differences on pages that currently read
green, which is work nobody has scheduled.

The alternative, and it is a real one, is a narrower rule: a named short list of
layout properties that behave differently across engines, checked in both, with
everything else staying single-engine.

**I am not deciding this.** It changes what "a page passed" means, which belongs
to DSRD 6 and to the harness, not to me. What I will say plainly is that the
current position, one engine, is now known to be wrong rather than merely
untested, and it was Kain's eye that established that rather than any machinery
of mine.

---

OWED BACK: a ruling on whether the gate goes two-engine, all rows or a named
list. Until then I will measure any layout change in both engines by hand and say
so in the ship record.

*No em or en dashes in this file; checked before writing.*
