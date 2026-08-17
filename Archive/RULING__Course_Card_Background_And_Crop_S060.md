# RULING: the course card's background and its hero crop, both ruled by Kain in Safari

**DOCUMENT TYPE:** ruling. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Ruled by:** Kain, live in Safari at the machine, from tabbed comparisons of the same six real cards.
**Owns the record:** DSRD 8 §7 for the decision history; `COMPONENT_DATA__course-card.json` for the values, already updated and pushed.
**Reads with:** `RULING__Visual_Variations_Are_Always_Tabbed_S060.md` and `INSTRUCTION__Course_Hero_Artwork_Standard_S060.md`, both filed this session.

---

## Ruling 1: the school colour drops to a whisper

**His words on what it replaced:** "I dont like the coloured course card backgrounds - they just dont 'feel' like achology."

**Ruled:** the same gradient shape, at roughly a fifth of its strength. The school accent at 13 percent opacity at the base and 7 percent at 35 percent height, fading up to nothing. Judged against plain white and a neutral grey lift; he took the whisper.

**Supersedes V2 Bold Rise**, which was this identical shape at 65 percent and 35 percent. Only the strength changed.

It also brings the card into line with its own recorded principle, which the wash had been contradicting: "course cards express school identity through structure only."

Live at v0.61.17. `component_gate` on the course card: 57 checks, 0 failed.

## Ruling 2: the hero is cropped onto the portrait

**His words:** "i have a problem with the image inside the card - the bubbles seem to me minimising the potential impact of the actual main image." Then, from four crops: "the decision I would like to make is 'Portrait, wider'."

**Ruled:** `object-fit: cover`, `object-position: 68% 42%`, `transform: scale(1.15)`, replacing the previous contain-at-78-percent. The portrait fills the frame; the monogram bubbles and the lightbulb sketch mostly fall outside it.

Live at v0.61.19.

**One thing still open, and he asked for it:** at this crop a clipped orange monogram intrudes at the top left of every card. Four options are rendered as tabs for his ruling, including the cover he suggested himself. Awaiting his word.

## The finding behind both rulings, which is Chat's to act on

**All 28 course heroes are one template.** Verified by opening three of them rather than assuming: identical monogram bubbles in identical positions, the same lightbulb and house sketch at the left, portrait always right of centre, only the portrait differing between courses. That is why a single crop is a legitimate answer for all 28.

**And the shape is wrong at source.** The files are 600x500, near square. The slot is 352x185, which is 1.9:1. DSRD 8 §7 specifies the hero's display and its file format and has never specified its source dimensions, which is how 28 near-square files came to be drawn for a landscape slot. The instruction to close that gap is filed separately as `INSTRUCTION__Course_Hero_Artwork_Standard_S060.md`, with 704x370 proposed. **The crop is a repair, not the fix.**

## A defect found on the way, already corrected

`knowledge-hub.css` carried an opaque dark green gradient on `.school--nlp .card__image-area`, left over from the placeholder era its own comment describes ("until hero images exist"). It painted a solid school colour behind every NLP course card site-wide while the other six schools took the light wash from `cards.css`, so one school in seven rendered nothing like the rest. Removed at v0.61.16.

**It surfaced only because a comparison switched the intended wash off**: every other card went clean and the NLP card stayed green.

**Worth Chat's attention for the record architecture, because this is the second gap of the same kind found today.** The course card's data file records ONE image-area treatment. This was a second one, unrecorded, in a different stylesheet, at a higher specificity than the recorded one. The gate could not have caught it: the gate reads a component's own record, and this lived on a page stylesheet. Together with the artwork-dimensions gap in the other file, the pattern is that the executable record covers a component's own CSS well and covers nothing on either side of it, neither the assets it consumes nor a page stylesheet reaching in.

One orphan left deliberately rather than swept: the `.kh-course-hero-label` rule that gradient was paired with is now dead too, but removing it fell outside the declared change set. Named, not taken.

*No em or en dashes in this file; checked before writing.*
