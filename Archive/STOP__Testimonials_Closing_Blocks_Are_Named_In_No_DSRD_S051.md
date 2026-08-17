# STOP: the Testimonials page's last two blocks are named in no DSRD

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Concerns:** `INSTRUCTION__Bring_Built_Pages_To_Standard_One_At_A_Time_DSRD6_Gate.md`,
page 6 of the order, Testimonials. It is the last page on the walk.
**Status: waiting on ruling.** Nothing changed on the page.

## Where the page stands

`page_gate` on `/testimonials/`: **38 passed, 4 failed, 2 carved out.**

Every hairline, both widths, the header-to-content spacing, the two container
widths, the H1, all three gutter tiers, both metadata rows, the dash check, the
assets and all 48 links pass. **The four failures are one thing, counted four
times:**

```
FAIL boundary-owner desktop boundary 5: firstOfB_marginTop  48px, .policy-closing, .policy-related in about.css
FAIL boundary-owner desktop boundary 5: firstOfB_paddingTop 48px, same rule
FAIL boundary-owner desktop boundary 6: firstOfB_marginTop  48px, same rule
FAIL boundary-owner desktop boundary 6: firstOfB_paddingTop 48px, same rule
                    ^ DSRD 7 s4.3, declared outside any DSRD 8 component
```

## Why I cannot fix it

The check applies your S227 ruling: fail only on spacing declared outside a
DSRD 8 component, and read where the spacing is declared rather than judging
who owns it. The spacing is declared on `.policy-closing, .policy-related`.

**I searched every DSRD for both class names. Neither appears in any of them.**
Not DSRD 8, not DSRD 7, not DSRD 9, nowhere. They exist in `about.css` and in
the templates and in no specification.

So the check is not wrong and the CSS is not obviously wrong either. Two blocks
that carry a page's closing boundaries have no registered identity, and there
is no document line to quote for a fix. Item 4 of the walk instruction is
explicit about what that means: "Where no written standard covers something,
STOP and ask through TO Chat. Do not decide."

## What the ruling has to choose between

Both are yours; I am not recommending one over the other because the choice is
about what those blocks ARE, which is a specification question:

1. **Register them.** If the closing panel and the related strip are real
   components, they belong in DSRD 8 with their spacing, and the check passes
   the moment they are named.
2. **Move the spacing.** If they are not components but arrangements of
   existing ones, the boundary spacing belongs on whatever component does own
   the boundary, and these two rules come out of `about.css`.

Either way it is one edit on my side once the answer exists.

## Two things worth knowing before you rule

**About passes 37 of 37 with the same stylesheet.** The same
`.policy-closing, .policy-related` rule is live there and trips nothing,
because About's closing boundary is the warm room, a different block. So this
is not a fault in the rule everywhere; it is a fault at these two boundaries on
this page.

**This was seen at S048 and deferred to today, correctly.** The sweep record
said: "About is the very next page on that walk, and Testimonials is the last,
so both will be fixed there under the walk instruction, with the document line
quoted for each fix." About needed no fix. Testimonials does, and the document
line the sweep record promised to quote turns out not to exist. That is the
finding.

## What I am not doing

**Not filing a DSRD 6 chapter-by-chapter record for Testimonials yet.** The
machine gate is above and it is honest, but the full record the instruction
asks for includes the accessibility walk and the fresh-eyes read, which is the
policy-walk bar Kain set as the minimum. That deserves a clean run rather than
the last twenty minutes of a long session, and it cannot close while a chapter
is waiting on this ruling anyway.

The page is unchanged and live: https://achologytest.com/testimonials/

*No em or en dashes in this file; checked before writing.*
