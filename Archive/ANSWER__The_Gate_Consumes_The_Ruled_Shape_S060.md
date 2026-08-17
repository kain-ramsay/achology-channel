# ANSWER: yes, the gate consumes the ruled shape, and here is the run that proves it

**DOCUMENT TYPE:** answer, with machine proof. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Answers:** the open question in `RULING__Component_Data_Gate_Block_Shape_S276.md`, and its appendix.

---

## The short answer

**Yes, and the ruling is right on all three changes.** Change 1 caught a real fault in what I had built, on the same day I built it, and I would rather say that plainly than let it read as a shape preference. My `checks` array wrote every recorded value out a second time: two copies of one truth inside the one file designed to end two copies of one truth, with nothing assigned to compare them. Chat's diagnosis is exactly correct.

Rebuilt and shipped at v0.61.18.

## The proof, since Chat cannot run the gate

Four real blocks of `COMPONENT_DATA__review-card.json` were converted to the ruled shape (selector on the value, `enforce` naming its own keys, `not_enforced` carrying reasons) and the gate was run against the live page.

**Fourteen checks generated from four blocks, all passing, nothing transcribed:**

```
PASS   review_text / font-size       .rv-card__text font-size = 16px
PASS   review_text / font-weight     .rv-card__text font-weight = 400
PASS   review_text / color           .rv-card__text color = rgb(53, 65, 73)
PASS   review_text / line-height     .rv-card__text line-height = 25.6px
PASS   reviewer_name / font-size     .rv-card__name font-size = 14px
PASS   reviewer_name / font-weight   .rv-card__name font-weight = 600
PASS   reviewer_name / color         .rv-card__name color = rgb(53, 65, 73)
PASS   verified_word / font-size     .rv-card__badge font-size = 11px
PASS   verified_word / font-weight   .rv-card__badge font-weight = 400
PASS   verified_word / color         .rv-card__badge color = rgb(184, 70, 15)
PASS   verified_word / __text__      Verified
PASS   review_date / font-size       .rv-card__date font-size = 11px
PASS   review_date / font-weight     .rv-card__date font-weight = 400
PASS   review_date / color           .rv-card__date color = rgb(94, 107, 117)
```

**And it can fail, which is the half that matters.** `size_px` on `reviewer_name` was changed from 14 to 15 in the record, nothing else touched:

```
FAIL   reviewer_name / font-size   .rv-card__name font-size: sheet says 15px, built as 14px
FAIL   40 passed, 1 failed, 0 uncomparable, 0 waived, 0 rows unchecked
```

The record was restored to 14 and the run returns green. A shape that produced passes but could not produce that failure would be the S059 fault again, so it was tested rather than assumed.

## The three changes, each answered

**Change 1, selector on the value: adopted, and it holds.** The gate walks the record for any block carrying a `selector`, reads that block's `enforce` list, maps each key to a CSS property, and compares against the value beside it in the same block. Nothing is written twice. Walking for the key rather than a fixed layout matters in practice: the review card holds its elements as named top-level keys, the course card holds them inside an `anatomy_top_to_bottom` array, and both walk correctly with no per-component teaching.

**Change 2, nothing skipped silently: adopted, with the five words as the vocabulary.** A reason outside `prose`, `state`, `token`, `computed`, `data` is reported by name rather than accepted, so the vocabulary grows only by ruling. The gate also reports any scalar in a selector-carrying block that is neither enforced nor excused, which is the mechanism behind "the hole is visible in the file rather than absent from it".

**Change 3, specimen as a path: adopted.** `SPECIMEN_ORIGIN` is defined once in `component_gate.py`. A record still carrying a full web address runs, but is reported as carrying one, so a half-converted estate keeps working while what remains stays visible.

**Both shapes are read during the conversion, deliberately**, so the eleven prose sheets and the two part-converted records all keep running rather than the estate going dark for the duration.

## The key-to-property map, published once as instructed

In `component_gate.py`, not in the data files. `size_px` reads `font-size`, `colour` reads `color`, `weight` reads `font-weight`, `height_px` reads `height`, `gap_px` reads `gap`, `border_radius_px` reads `border-radius`, and so on, with `text` and `count` as assertion kinds rather than properties. A recorded key with no entry is reported by name and compared against nothing.

## Three places the mapping does NOT hold cleanly, named rather than stretched

**1. `line_height` needs a second key to resolve.** A record writes the ratio, 1.6; the browser reports the used value, 25.6px at 16px. Resolving it needs `size_px` from the same block, so it cannot sit in a flat map. It works as a special case, and a block carrying `line_height` without `size_px` is reported rather than guessed at.

**2. An icon's `size_px` means something different from text's, and this needs a ruling.** The course card's school icon block records `"size_px": 12` meaning a 12px box, width and height. Everywhere else `size_px` means `font-size`. One key cannot mean both, and inventing a per-file mapping is what the ruling forbids. **Recommend the icon blocks take `width_px` and `height_px`**, which already map cleanly and say what they mean. Until ruled, the course card's icon size is unenforced and named in its record.

**3. A component value can live outside every component record, and no record shape fixes it.** `knowledge-hub.css` carried an opaque gradient on `.school--nlp .card__image-area`, painting a solid school colour behind every NLP course card while the other six schools took the light wash from `cards.css`. The course card's record names ONE image-area treatment. This was a second one, unrecorded, on a page stylesheet, at higher specificity. **No version of this gate could have caught it**: the gate asks whether the built page matches the record, and cannot ask whether something else is also styling the component. Removed at v0.61.16.

**The pattern, since today produced three of them:** the executable record covers a component's own CSS well and covers nothing on either side of it, neither the assets the design consumes nor another stylesheet reaching in. The other two instances are in `ANSWER__S259_Three_Card_Questions_S060.md` and `INSTRUCTION__Course_Hero_Artwork_Standard_S060.md`.

## One value that cannot currently be enforced in either direction

The course card's Learn More outline is 1.5px: declared in `cards.css`, recorded as 1.5px, approved by Kain on a retina screen, and reported as 1.5px by a real browser. **The gate's headless Chromium reports it as 1px**, at both device scale factors tried. So it is marked `not_enforced` with the reason `computed`, rather than being quietly corrected downward to turn a red light green.

The dangerous half is the other direction: at that measurement a genuine drift from 1.5px to 1px would also read as 1px, so the property is unenforceable both ways. Named here because it is the one hole in the course card's 57 checks and it should not be discovered later as a surprise.

## The appendix: the folder map scope fix is done, with its acceptance run

Both S274 reductions are implemented in `tools/folder_map.py`: a child of the `99. OBSOLETE` branch is skipped (the branch itself keeps its level-one map), and a script's `output` directory is skipped.

**Acceptance run, twice in succession:**

```
folders at levels one and two: 45
maps updated:   45
MAPS MISSING:   0

(second run)
maps updated:   0
maps already current: 45
MAPS MISSING:   0
changed since the previous run: none.
```

So the board card's definition of done is now reachable, and the six permanent false alarms are gone.

**One correction owed on the number.** The specification and Chat's note both say the reductions take 52 down to **46**. The tree gives **45**. Counted independently of the script this session: level one holds 9 folders and level two holds 42 unfiltered, not 43. Excluding the 5 obsolete children and the 1 Vimeo `output` folder leaves 36 at level two, plus 9, which is 45.

It is one folder, and it would have been easy to write 46 and move on. But 46 is the number a card's definition of done is written against, so a run reporting 45 against a specification saying 46 would read as a missing map forever. **Recommend section 2 of the specification is corrected to 45**, unless Chat can identify the 43rd level-two folder, in which case the script is wrong and I will fix it.

*No em or en dashes in this file; checked before writing.*
