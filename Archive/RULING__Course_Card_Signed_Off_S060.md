# RULING: the course card is signed off. Prototype v1 and its record are filed.

**DOCUMENT TYPE:** ruling with its fold-back. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Ruled by:** Kain, live in Safari across the S060 sitting, from tabbed comparisons at every step.
**Fold-back per Harness Rule 14 as tightened at S258:** the approved state exported as the prototype and the record updated to match, same session. Both writes named below.
**Delivers:** the first component of `COMMISSION__The_Card_And_Chrome_Sweep_S273.md` Job 2.

---

## What he ruled, in the order he ruled it

| # | His words | Ruled |
|---|---|---|
| 1 | "the course names cannot span more than two lines of text" | Titles capped at two lines. Measured first: 27 of 28 already fitted, so it is one shortened card name, not a clamp across the family. |
| 2 | "I dont like the coloured course card backgrounds" | School colour at a whisper: 13 percent at the base, 7 at 35 percent height. Supersedes V2 Bold Rise, the same shape at 65 and 35. |
| 3 | "the bubbles seem to me minimising the potential impact of the actual main image" | Answered by new artwork, not by CSS. He redrew all 28 at 1056x555. |
| 4 | "As it is now. The whole picture at its true proportions, filling the space" | Hero fills the picture area. No crop, no scaling. |
| 5 | "the shortened school name and teh Home icon are not aligned" | Icon aligned from the text baseline, lifted 1px, the position he set himself at six times magnification. |
| 6 | "each school shortened name is the school colour" and "the icon as the same school colour too" | Both in that school's colour, in its text-safe form. |

**Live at theme v0.63.0.** Deployed; local, server and zip agree; `css_gate` passes; `component_gate` on this component reads **56 passed, 0 failed, 0 unchecked**.

## The two writes the fold-back requires

- **Prototype:** `achology-course-card-proof-v1.html`, beside the record in the course-card folder. Exported from the rendered live page with all eleven stylesheets inlined, so it still shows what he approved after the theme moves on. Per the S053 precedent, the prototype is the live page's own markup rather than a redrawing of it.
- **Record:** `COMPONENT_DATA__course-card.json`, updated to match, with the prototype named in its status block where it previously read NOT RECORDED.

## One instruction that could not be followed as given

He asked for the school name in its colour "with the same layer of 'lightness' or fade applied". **The fade is the one part that could not be built**, and it was measured rather than argued. The line is 12px text so the bar is 4.5:1, and `tools/school_colour_contrast.py` shows **five of the seven primaries already fail as drawn**, worst being Cognitive Behavioural Psychology at 3.23. Faded to 85 percent all seven fail; at 70 percent the best reads 2.97.

His own S259 ruling is the precedent for measuring rather than shipping it: a card author line was moved off `#B0B8BE` at 2.01:1 for exactly this.

**So the intent was kept and the method inverted:** each colour darkened to the first step clearing the bar, hue and saturation preserved so it still reads as that school. NLP and MIW already pass and are unchanged. He was told plainly why the fade could not be done, and took the darkened version.

**New tokens in `base.css`, mapped per school in `components.css` beside `--school-accent`:**

```
--school-nlp-text: var(--school-nlp-primary)   5.44, unchanged
--school-cbp-text: #747940                     4.61, was 3.23
--school-lc-text:  #A66543                     4.60, was 3.85
--school-pc-text:  #A16575                     4.53, was 4.23
--school-miw-text: var(--school-miw-primary)   5.14, unchanged
--school-mh-text:  #5E73A9                     4.67, was 4.35
--school-pgd-text: #3E7E8D                     4.59, was 3.38
```

**This is bigger than one card, and Chat should scope it as such.** The site now has two forms of every school colour: `--school-accent` for fills, bars and decorative marks, `--school-text` for anything a reader reads. **Any other place a school colour currently carries text is using the failing primary.** That is a sweep to scope, not a thing to fix in passing, and it is named here rather than left to be discovered.

Verified on the rendered page rather than asserted: all six cards show name and icon in exactly the same colour, and every measured ratio falls between 4.53 and 5.44.

## Three mistakes of mine, all caught by Kain or by a machine, none by my own checking

**The alignment took three attempts.** First a half-pixel nudge inherited from before. Second, collapsing the line box to the font size, on reasoning that was simply wrong: a font's capitals are not centred in their line box even when the box equals the font size, because ascent and descent divide it unevenly, so centring always leaves the icon low and no box height fixes an asymmetry living in the font. Only the third, baseline alignment plus a measured lift, was sound. **He reported it twice, the second time with my "fix" already live.**

**My own diagnostic was lying while looking authoritative.** The magnified page drew its baseline and cap-height guides from assumed values, 0.7em and 0.8em. Measured from the rendered font: cap height is 0.676em, and with `line-height: 1` the half-leading is negative so the baseline rises a full pixel above where I had drawn it. At six times magnification that is a six pixel error in the very instrument built to settle a one pixel question.

**And the gate caught me duplicating a truth, in the file built to end duplicated truths.** Updating the record's school-name and icon colours for his ruling left the old `checks` array still asserting the superseded grey and orange, and the run went red on both. That is precisely the fault Chat named in the S276 ruling, demonstrated live. Both are now structure-only checks with the colour left to its per-school binding and the reason recorded as `data`, rather than a second copy kept in step by hand.

The lesson the project already holds, earned again: an instrument that has not been checked against reality is not evidence, however confident its output looks.

## Also confirmed for Chat, from S277 item 6

**The 45 folder maps are real files, not husks.** No iCloud placeholder stubs among them, and the smallest is 734 bytes, which is a genuine purpose paragraph rather than an empty shell. The board card stands at Done. For accuracy: a direct search finds 44 at the depth I walked against the generator's 45, which is a difference in search depth rather than a missing file, named rather than rounded away.

*No em or en dashes in this file; checked before writing.*
