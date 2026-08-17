# REPORT: the policy pages' spacing drift was my checker, not the pages

**From:** Claude Code, S230. **Date:** 2026-07-28.
**Cancels:** item B in `DELIVERED__page_gate_Built_Plus_First_Policy_Page_Printout.md`, and your line in `00__ANSWERS__Walk_Order_Check3_And_Breadcrumb_Hairline.md`: "The closing-note 2.6px drift (your item B) is unambiguous as you said: fix it when the walk starts, inside that page's declared scope."

There is nothing to fix. The pages were right and the instrument was wrong.

## What happened

`page_gate` measures the air above and below a hairline by walking to the deepest last element above the line and the deepest first element below it, then measuring from their boxes. Where that deepest element is inline, a link at the end of a closing sentence, its box is the text box and not the line box, so it sits a couple of pixels above where the text visually ends. Every policy page whose closing paragraph ends in a link therefore reported roughly 50.6 above the line instead of 48, and roughly 49 below instead of 48.

The same fault ran the other way underneath the line. Where the block below carries the line on its own border-top, its box top IS the line, so the space below the line is that block's padding. Descending past it into its first inline child reported the text box again, not the padding.

Measured properly, at the content edge of the nearest block element and with its own padding counted, the refund policy reads 48 above and 48 below at desktop and tablet and 32 and 32 on the phone. Exactly the standard. It was never off it.

## What it cost, and what it would have cost

It cost one wrong entry in your register and one wrong entry in mine, carried since 27 July. What it would have cost is the part worth noting: the fix was queued to run inside the refund policy's declared scope, at the top of the walk. I would have moved spacing that was already correct, on the first page of the first family, and every page after it would have inherited the change.

## The correction

`page_gate` now descends through block-level children only, and measures to the content edge: box edge less that element's own padding above the line, box edge plus its own padding below. The comment in the file records why, in the same form as the other failures that shaped that script.

The whole map was re-run afterwards and refiled as `MAP__page_gate_Across_Every_Built_Page.md`. Across the built set the spacing failures fall from 37 to 16. Six of the seven legal policies come out with nothing left but the dash sweep, and the refund policy comes out with nothing at all beyond the site wide canonical you have already excluded.

## The general point, which is the reason this is a report and not a footnote

A gate that is wrong is worse than no gate, because its output is trusted and filed. This one produced a defect, that defect was written into two registers as fact, and it was one session away from being built into the pages the gate exists to protect. The three checks that caught it were not the gate: reading the raw numbers rather than the verdict, asking where a 2.6px figure could physically come from, and measuring the same boundary two ways before touching anything. Those are what I will do before trusting any new check this instrument grows.

*No em or en dashes in this file; checked before writing.*
