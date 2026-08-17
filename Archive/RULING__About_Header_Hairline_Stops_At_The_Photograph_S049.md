# RULING: the About family's header hairline stops where the photograph begins

**From:** Claude Code, S049. **Date:** 2026-08-06. **Filed under Harness Rule 14.**
**Closes:** `QUESTION__About_Header_Hairline_Two_Written_Positions_Conflict_S048.md`, which is the full evidence and is not repeated here.
**Chat owes one thing:** the DSRD 7 §4.3 wording. Everything else is executed and verified.

## Kain's words

Put to him at the open of S049 as two whole rendered About pages side by side at
full width, not as a description, because the standing rule is that he judges a
line on a page by looking at it. His answer, verbatim:

> "B - the line stops where the photograph begins. This is what is live now."

Option A was the same page with the separator returned to the header block at
full width. He looked at both and chose B.

## What that settles

The S238 treatment stands and is now ruled, not inherited. Nothing on any page
changed: the build was already B. What changes is the record and the instrument.

The conflict the question set out was real, and both positions were his: DSRD 7
§4.3 rulings 1 and 2 want a full-width line at every block boundary, and ruling
4 wants 48 above and 48 below and nothing else. On a header block carrying a
floated figure taller than its text, satisfying one breaks the other. Read from
the rendered page this session at 1440: with the line on the header block, the
gap from the button down to the line measures 78px. With the line on the text
column, it measures 48. §4.3 has no sentence covering a block whose two columns
are different heights, which is what made it a gap rather than a mistake.

## What Chat writes into DSRD 7 §4.3

A second recorded exception, in the same shape as the S238 story-block exception
already in that section. The governing sentence it rests on is §4.3's own, read
from the canonical file this session:

> "One owner supplies the space; every block touching it supplies zero. The element carrying the hairline owns the full measurement."

The text column carries the line, so the text column owns the 48 above it,
measured from the button, and the header's margin owns the 48 below. Ruling 4
holds at every width, and a visible separator still sits at the boundary; it is
drawn to the edge of the copy instead of the edge of the block.

**Pages it covers:** /about/, /testimonials/ (both `.policy-header--doc`) and the
Founders' Letter (`.policy-header--portrait`), which share the two rules.

Also worth correcting while §4.3 is open: `policies.css` still carries a comment
saying the full-width line superseded the under-text one and was approved on
2026-07-29. That sentence is now wrong. It is a code comment and therefore not a
source, but the next person to read it will be misled exactly as I was. I will
correct it when a change set legitimately touches that file; flagging it here so
the record and the comment do not drift apart again.

## What the gate learned, executed this session

`page_gate.py` is at v6. Two corrections, both verified.

1. **The uneven-columns exception.** The gate read the built line as no line at
   all and failed both About and Testimonials on a boundary that has a visible
   separator. It now recognises the pattern and reports it as a named CARVE-OUT
   row, never a silent pass, so no record can show it as an ordinary result.
   Detection is three conditions together: the block itself draws no line,
   exactly one direct child does, and a floated descendant reaches below that
   child's content edge. Proved on the rendered page against all three ways of
   losing the line, and it refuses every one:

   ```
   as built                              recognised
   line removed from the text column     refused
   figure shorter than the text          refused
   float removed                         refused
   ```

2. **An out-of-flow element is no longer a content edge.** Separate defect,
   found while measuring this one. At phone width the same photograph becomes a
   decorative backdrop filling the header (about.css §6: position absolute,
   inset 0, pointer-events none, opacity 0.12), so it ended 1px above the line
   and the gate reported "1.0 above" on a boundary where the copy in fact
   measures 32. §4.3's verification note reads: "Any other number means a second
   element contributed space; that element is the defect, not the hairline." An
   absolutely positioned element contributes no space, so it can never be that
   element. This was a false failure, not a page defect.

## The printout

Before, on /about/:

```
FAIL  hairline-present  desktop boundary 2 (policy-header | policy-body): no hairline, gap 48.0px
FAIL  hairline-spacing  mobile  boundary 2: 1.0 above, 32.0 below (want 32/32)
FAIL  34 passed, 2 failed
```

After:

```
CARVE-OUT hairline-present  desktop boundary 2: the line is drawn on the header's text column
                            and stops where the floated figure begins, which is the recorded
                            uneven-columns exception, not a missing line
PASS      hairline-spacing  desktop boundary 2: 48 above, 48 below
PASS      hairline-spacing  mobile  boundary 2: 32 above, 32 below
PASS  37 passed, 0 failed, 1 carved out
```

Regression checked across five pages, none of which should have moved:
/about/ PASS, /about/founders-letter/ PASS, /policies/ PASS,
/policies/privacy-policy/ PASS. /testimonials/ still fails four rows, and they
are a different, pre-existing matter: `.policy-closing, .policy-related` declare
boundary spacing in about.css, outside any DSRD 8 component. That belongs to
Testimonials' own turn on the walk and is not touched here.

*No em or en dashes in this file; checked before writing.*
