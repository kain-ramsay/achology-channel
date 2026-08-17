# QUESTION: the About header hairline. Two written positions conflict, and both are Kain's.

**From:** Claude Code, S048. **Date:** 2026-08-06. **Status: going to Kain on screen, not to Chat on paper. Chat is not blocked by this.**

**Route corrected at the close of S048.** I first filed this as a question for
Chat. That was wrong. It is a look-and-feel question about a line on a page, and
the standing rule is that Kain judges those by looking, never from a
description: "Never describe two appearances and ask him to pick." So S049 opens
by rendering both versions of the header at full width and letting him choose in
seconds. **Chat's part begins after that:** whichever he picks, DSRD 7 §4.3
needs either a correction or a recorded exception, and `page_gate` needs to
learn it. The evidence below is what Chat will need to write that up.
**Blocks:** the hairline chapter of About's DSRD 6 walk, and the same failure on /testimonials/.
**Nothing changed.** I have not touched either rule.

## What the gate says

```
/about/         FAIL  hairline-present  desktop boundary 2 (policy-header | policy-body): no hairline, gap 48.0px
                FAIL  hairline-spacing  mobile  boundary 2: 1.0 above, 32.0 below (want 32/32)
/testimonials/  FAIL  the same two, at policy-header | tm-answers
```

## What is actually on the page

The hairline is not missing. It has been moved off the header block and onto
the header's inner text column, so it stops where the floated photograph
begins. Read from the rendered page at 1440:

```
.policy-page--about .policy-header--doc          border-bottom: 0; padding-bottom: 0;
.policy-page--about .policy-header--doc .policy-header__text
                                                 border-bottom: 1px solid var(--color-hairline);
                                                 padding-bottom: var(--sp-2xl);
                                                 width: calc(100% - 312px - var(--sp-2xl));
```

## The conflict, in the two files' own words

**policies.css says the full-width line won:**

> "The document header carries the standard block separator inherited from .policy-header, full width at the block boundary: DSRD 7 4.3 rulings 1 and 2 (Kain S224) supersede the 2026-07-15 under-text hairline; the conformance was approved by Kain on 2026-07-29."

**about.css says the under-text line won, and for a reason that is not drift:**

> "That is the fix to the spacing Kain called broken (S238): while the header owned it, the 48px sat below the TALLER of the two columns, which is the photograph, so the gap from the button down to the line measured 77px instead of 48. DSRD 7 §4.3's one-owner rule settles it: 'The element carrying the hairline owns the full measurement.' The copy block carries the line, so the copy block owns the 48 above it, measured from the button, and the header's margin owns the 48 below. Ruling 4 holds at every width again."

So the S238 override came **after** the 2026-07-29 full-width conformance and
deliberately reinstates what that conformance superseded, to rescue ruling 4.

**Each position satisfies one ruling by breaking another:**

| | Ruling 1 and 2, a full-width line at every block boundary | Ruling 4, 48px above and below, nothing else |
|---|---|---|
| Full-width line on the header | passes | **fails**, the gap reads 77px because the photograph is the taller column |
| Under-text line, as built | **fails**, the gate reads no hairline at the boundary | passes |

DSRD 7 §4.3 has no sentence covering a block whose two columns are different
heights, which is what makes this a gap rather than a mistake.

## What I need, in one line

**Which ruling wins when a header block carries a floated figure taller than
its text?**

Three ways it could go, and I am not choosing between them:

1. **Ruling 1 wins.** The line goes back to full width on the header block, and
   the 77px gap is accepted or solved another way. About and Testimonials pass
   the gate. Kain sees the spacing he called broken return, so this needs his
   eye on the rendered page, not just a ruling on paper.
2. **The S238 fix stands** and DSRD 7 §4.3 gains a recorded exception naming
   this case: a header with an uneven second column carries its separator on
   the text column. `page_gate` then needs teaching that exception, or it will
   keep failing every such page forever.
3. **Something else**, if the 77px has a fix neither of us has thought of, for
   example the figure not participating in the block's height.

**My reading, offered and not acted on:** option 2 looks right, because the
S238 note is the more recent and the more specific, and because it was made in
response to Kain seeing the rendered result rather than reading a rule. But it
is only complete if the gate learns the exception, otherwise every future walk
files this same failure again.

## Scope note, so whoever fixes it does not trip Rule 3

The two rules are shared: the selectors carry `.policy-header--portrait`
alongside `.policy-page--about .policy-header--doc`, and `--portrait` is the
Founders' Letter's header. `.policy-page--testimonials` uses `--doc` too. So a
change here touches **three pages**, and needs a sweep brief rather than
riding on About's turn in the walk.

*No em or en dashes in this file; checked before writing.*
