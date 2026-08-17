# INSTRUCTION: DSRD 8 needs an artwork standard for the course hero. It has none.

**DOCUMENT TYPE:** instruction for a DSRD correction. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Authority:** Kain, in the S060 sitting, on being shown the gap: "Yes, write that to Chat as the artwork standard to be added to the specification."
**Owns the change:** DSRD 8 §7 (course card). Code never edits a DSRD, so this is the instruction rather than the edit.

---

## The gap, and how it was found

Kain asked, in the middle of ruling on the course card, a plain question: what dimensions must a course card image be? There is no answer in the specification.

DSRD 8 §7 specifies the hero's **display** thoroughly. Quoted from the canonical file this session:

> **Image area:** 185px height. V2 Bold Rise gradient (secondary 65% opacity at base, primary 35% at 35% height, fading up to white). Course hero centred at 78% max-width, transparent PNG.

> **Hero image:** max-width 78%, max-height 88%, object-fit contain, position relative, z-index 1

> **Hero images must be true transparent PNGs served from WordPress; CSS requires no blend mode.**

So the file format is specified and the display is specified. **The source dimensions are not.** Nothing in §7 says how large the artwork should be, or what shape.

**This is not a theoretical gap; it has already cost something.** All 28 course heroes were produced at 600x500, which is very nearly square. The slot they are displayed in is 352x185, which is 1.9:1, landscape. Measured in the browser this session, not assumed. Because the rule is `object-fit: contain` at 78 percent width, the whole near-square picture is shrunk to fit inside a wide letterbox, so the subject ends up small while the empty width around it stays full. That is precisely the complaint Kain raised unprompted: the artwork's main subject has no impact on the card.

**The contrast with the featured article card is the argument.** §6.5 does state its asset dimensions, and states them with the reasoning attached:

> **The asset is the author portrait, 1200x1500 JPG at 4:5** (DSRD 7 §12.1), object-fit cover, object-position centre

That entry exists because the same mistake was made once already and ruled at S259, when the 1200x630 composite banner was found to be the wrong shape for a slot taller than it is wide. The course hero is the same failure in the opposite direction, and it has not been caught until now because nobody asked the question Kain just asked.

## What the standard should say

The numbers below are measured from the rendered card at desktop width, at a device pixel ratio of 2, which is the screen Kain approves on.

- **Displayed area:** 352 x 185, a ratio of 1.9:1.
- **Required artwork size: 704 x 370 pixels**, which is that area at 2x so it is sharp on a retina screen.
- **Format:** true transparent PNG, unchanged from the existing rule.
- **Composition:** the subject fills the frame. No secondary scene, and no logo marks in the artwork.

That last line is a consequence of Kain's other finding in the same sitting, and it is worth writing into the standard rather than left as a one-off instruction to whoever draws the next set. His words: the bubbles "seem to me minimising the potential impact of the actual main image". The 28 existing heroes each carry seven Achology monogram bubbles plus a second scene of a lightbulb and a house, around a portrait that is the only part carrying meaning. **The card already carries the brand in its school line, its accent bar, its icons and its buttons, so a logo repeated seven times inside the picture is brand applied where it competes with the subject rather than supporting it.**

## One thing to decide that is not Code's

Whether the existing 28 are re-drawn to this standard, or kept and cropped. Kain has ruled the crop for now (see `RULING__Course_Card_Background_And_Crop_S060.md`, filed this session), which improves it substantially with no new artwork. But a crop of a near-square source into a 1.9:1 slot throws away roughly half the file, so the effective resolution of the visible portrait is well below what 704 x 370 would give, and one clipped monogram still intrudes at the top left corner.

So the standard above should be written as the standard for **new** artwork, with the fate of the existing 28 recorded as an open decision for Kain rather than settled by this note.

## Worth carrying into the record architecture

The gate could not have caught this, and that is a finding in its own right. `COMPONENT_DATA__course-card.json` records the hero's display treatment, because that is a property of the component. The source artwork's dimensions are a property of the **asset**, which no component record covers, so nothing in the executable record chain was ever positioned to notice that every one of the 28 files was the wrong shape. A component record checks the built page against the design. It does not check the inputs the design consumes.

That is the second gap of this kind found today; the first was an unrecorded second gradient living on a page stylesheet, reported in `RULING__Course_Card_Background_And_Crop_S060.md`. Both point the same way: the record architecture covers the component's own CSS well and covers nothing either side of it.

*No em or en dashes in this file; checked before writing.*
