**DISPOSITION (S280, Chat):** consumed at S279. This handover drove the whole commerce card session: the bundle, AAA and membership card reviews, the sixteen corrections Kain ruled on tabbed renders, and both build briefs now in FROM Chat. Archived.

# HANDOVER: everything the course card settled, for the rest of the card sweep

**DOCUMENT TYPE:** handover of settled standards. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Written because Kain has asked to run the remaining card sweep with Chat rather than with Code**, given how long today took. His instruction: "I need the specs we have agreed on today to influence all of the other product cards; school cards etc."
**Reads with:** `RULING__Course_Card_Signed_Off_S060.md`, which carries the course card's own decisions.

---

## Why this file exists, in his words and mine

He asked whether I understood why getting this right matters. Today did not settle one card. It produced standards that did not exist anywhere before, and if the school card, bundle card, membership cards and Access All Areas card are decided without them, each family invents its own answer to the same question. The result is a site that reads as assembled rather than designed, and every family done differently has to be redone later, by which time it is in more pages.

**So this is not a summary of the course card. It is the list of things now true for every card, extracted from it.**

## 1. School colours: there are now TWO of every one, and using the wrong one is a defect

`--school-accent` for fills, bars, gradients and decorative marks. `--school-text` for anything a reader reads. They differ on five of the seven.

**Why, and it is not a preference.** The seven school primaries were measured against the 4.5:1 bar that small text must meet. Five fail as drawn, the worst at 3.23. Kain asked for the school colour on the course card's school name "with the same layer of lightness or fade applied"; a fade moves a colour AWAY from the bar, so all seven fail once lightened. Each was darkened to the first passing step, which preserves hue so it still reads as that school.

| School | accent | text | ratio |
|---|---|---|---|
| nlp | #4D7258 | unchanged | 5.44 |
| cbp | #8E944E | #747940 | 4.61, was 3.23 |
| lc | #B8704A | #A66543 | 4.60, was 3.85 |
| pc | #A8697A | #A16575 | 4.53, was 4.23 |
| miw | #7E6298 | unchanged | 5.14 |
| mh | #6278B0 | #5E73A9 | 4.67, was 4.35 |
| pgd | #4A96A8 | #3E7E8D | 4.59, was 3.38 |

Tokens are in `base.css`, mapped per school in `components.css` beside `--school-accent`, so a component asks once and gets the right one.

**The sweep item:** every other place on the site where a school colour carries text is currently using the failing primary. That is its own scope, named at the sign-off and repeated here so it is not lost.

## 2. Card artwork has a required size and shape, and the absence of one is what caused today

The course hero is **704x370 transparent**, being the 352x185 picture area at 2x. Filed separately as `INSTRUCTION__Course_Hero_Artwork_Standard_S060.md` for DSRD 8.

**The general standard for every card, which is the transferable part:** a card's image slot has a required source size and shape, and DSRD 8 must state it. DSRD 8 §7 specified the course hero's display and format thoroughly and never its source dimensions, which is how 28 near-square files came to be drawn for a landscape slot, and why the subject looked lost on every card. The featured article card has the same fault from the other end.

**So before any card in the sweep is ruled: check its slot has a stated source size, and if it has not, that is the first thing to settle.** A design ruled against an asset that does not exist at that size is a ruling that cannot be built.

## 3. Type: the scale is ruled and the cards do not follow it

The nine steps Kain approved at S056 and signed into `BRIEF__Type_Scale_Sweep_S270.md` are **12, 14, 16, 18, 21, 24, 28, 33, 42**.

The course card used 12, 17, 12.5, 18, 13, 11, 14. **Four of seven were off the scale.** He ruled the title from 17 to 18 today; the other three (12.5 stats, 13 price qualifier, 11 guarantee pill) are left to the type scale sweep rather than swept into a card review.

**Expect the same on every other card**, and it is worth checking each against the scale before he is asked to judge it. He asked today whether the typography session had been a waste of time, and the honest answer was that it had not influenced this card at all. That should not be the answer twice.

**Still unruled, and it came up today:** weight. `GUIDANCE__Standardising_The_Type_Across_The_Site_S269.md` §3 says 108 declarations set no weight at all and that weight has never been ruled. Kain raised it himself today, asking whether there were font rules. There are not, for weight. It is the largest open typography question and it is his to rule.

## 4. Icons beside text align from the baseline, not the line box

The course card's school icon is `align-self: baseline` with a **1px lift**, replacing an inherited `top: -0.5px`.

**The method, which transfers:** a font's capitals are not centred in their line box, because ascent and descent divide it unevenly, so centring an icon on the box always leaves it low. Align to the baseline, then lift by `(icon height - cap height) / 2`. Como's cap height measures 0.676em, not the 0.7 commonly assumed.

**And then let him adjust it by eye.** Geometric cap-centring computed to 1.945px; he chose 1px. That is not him overruling the arithmetic: a glyph whose mass sits off-centre in its box, like a house tapering to an apex, reads low even when measured correctly. Optical beats geometric, and only an eye can settle it.

## 5. How he wants to be shown things, ruled today and binding

**Every visual variation is TABBED.** His words: "PLEASE let this ALWAYS be our standard for when i need to rule on visual design variations on any aspect of the site - ALWAYS, do you understand?" Filed as `RULING__Visual_Variations_Are_Always_Tabbed_S060.md`.

One page, one row of tabs, one panel at a time, the thing under judgement in the same screen position in every panel. A stacked comparison makes him carry a memory down the page and judge a recollection.

**And a hard lesson from today, worth more than the rule:** he ended the sitting saying "JUST SHOW ME THE ACTUAL BLOCK for fucks sake!!!! Stop wasting my time". He was right. I had shown him magnified diagnostics, guide lines and abstractions when he had asked twice to see the real block on a real page. **Tabs are for choosing between options. Once something is settled, show him the actual thing on the actual page and nothing else.**

## 6. Two failure modes of mine that a Chat-run sweep should watch for

**A preview that is not the real thing will mislead him, and he will be blamed for it.** Two of my pages rendered in a fallback typeface because inlining a stylesheet broke the font URLs. He told me twice the text had been boldened. I measured the live page, found it unchanged, and told him he was wrong. He was right; I was checking a different page from the one in front of him. **Whatever renders options for him must be verified to be showing the real fonts, colours and assets before he is asked to judge.**

**A component record cannot see faults just outside the component.** Three today: an unrecorded second gradient on a page stylesheet overriding the card's own; artwork drawn to the wrong dimensions because none were specified; and a design ruled against a portrait asset that does not exist. In all three the component's record was correct and the fault sat beside it.

## What Code still holds, whoever runs the sweep

Kain's own standing rule is that a component already built in the theme is judged in Safari on the live page, not in a panel. The school, bundle, membership and Access All Areas cards are all built. So the split that works: **Chat for the standards and the design exploration, Code for confirming the ruled state on the real page and folding each component back into its prototype and record.** The fold-back is a harness obligation (Rule 14 as tightened at S258) and cannot move.

*No em or en dashes in this file; checked before writing.*
