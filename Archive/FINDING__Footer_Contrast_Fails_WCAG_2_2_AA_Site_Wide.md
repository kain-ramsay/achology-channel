# FINDING, CORRECTED: the footer contrast, one item withdrawn and one restated

**From:** Claude Code, S047. **Date:** 2026-08-05.
**Corrects:** the version of this file filed earlier today at page 1 of the walk, which asked Kain to rule on two items. **One of those two is already ruled and documented, and I should not have raised it.** This version replaces it in full.

## The correction, first, because it changes what you were asked to decide

I filed two failing items. I measured both correctly and I read neither against the document that governs them before filing. DSRD 7 section 5.1 says, word for word:

> "**Accepted AA exception (Kain, 2026-07-16):** primary buttons keep white-on-#ED6922 (3.16:1 at 14px, below AA) as a deliberate brand decision. Documented here so audits stop re-flagging it."

That is the "Start Your Trial" footer button exactly: white on #ED6922 at 14px. The document even records the same 3.16:1 I measured. **It is a deliberate, recorded, Kain-approved exception, and the document says in terms that it exists so audits stop re-flagging it. I re-flagged it.** Withdrawn. Nothing is owed on it and it needs no design session time.

This is the failure Rule 4 exists to prevent: I quoted a measurement instead of the spec. The measurement was right and the conclusion was wrong.

## What actually stands: the four footer column headings

This item is real, but it is not an unruled defect either, and its shape is different from what I first described.

**Measured on the rendered page, alpha composited:** the four footer column headings, brand orange #ED6922 at 11px/600 on the #354149 footer, give **3.32 to 1**. At that size and weight WCAG 2.2 AA requires 4.5 to 1.

**What the document says about them.** DSRD 8 section 19 addresses this colour in this exact place, and rules it:

> "In the dark footer the span renders brand orange `#ED6922`, inheriting the heading colour, not the quieter `#C64E14` of section 13.2. The section 13.2 value exists because brand orange fails large-text AA on the off-white panel; **the dark footer is the opposite context, where brand orange is the required and accessible rendering.** Ruled S235 (Kain), on Code's S043 question."

So there is a ruling, and I should have found it before filing. But the ruling rests on a stated factual premise, that brand orange on the dark footer is "the required and accessible rendering", and **measurement does not support that premise at this size**: 3.32 to 1 against a 4.5 requirement. Brand orange on the dark footer is better than brand orange on white (3.16), but it does not reach AA for 11px text.

## What I am asking for, which is smaller than before

Not a design decision from scratch. One factual correction, and then Kain's call on whether it changes anything:

1. **DSRD 8 section 19's sentence is inaccurate as written.** "The required and accessible rendering" is true of the colour choice relative to the alternative, and not true against the AA threshold at 11px. That sentence should be corrected whatever else happens, because it is currently the reason a future audit will be told not to look.
2. **Then Kain decides**, knowing the real number, whether the headings stay as ruled (which is entirely open to him, exactly as the primary-button exception is, and would be recorded the same way) or move. If they stay, it wants recording as an accepted exception in the same form as section 5.1's, so the next walk does not raise it either.

Either way this stops being a live defect on twenty-three pages and becomes one line in a document.

## What this changes in the walk records

Pages 1 to 5 each record section 7 as failing by reference to this file. That reference now points at one item, not two, and at a documented ruling rather than an open question. I will restate section 7 in those records as: **the page's own accessibility is clean; the single outstanding chrome item is the footer column heading contrast, ruled S235 on a premise this walk has measured as inaccurate.** No page's own verdict changes.

*No em or en dashes in this file; checked before writing.*
