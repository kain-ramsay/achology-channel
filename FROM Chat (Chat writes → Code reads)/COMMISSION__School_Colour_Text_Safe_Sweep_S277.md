# COMMISSION: the school colour text-safe sweep, delivered whole in one sitting

**DOCUMENT TYPE:** commission. Approved by Kain, S277, 17 August 2026.
**From:** Claude Chat, S277. **To:** Claude Code, next session.
**Board card:** "School Colour Text-Safe Sweep: Every School Colour Carrying Text Moves To Its AA Token" (Website Rebuild, Urgent and Important, Pre-Launch).
**Standing on:** your own S060 ruling, `RULING__Course_Card_Signed_Off_S060.md`, where you named this and correctly refused to fix it in passing.

---

## What Kain has asked for, in his own terms

He approved the card on one condition, and it is the reason this file exists rather than a scoping request: **the card comes back Done in the next session.** His words at S277: the board is getting much bigger and not much is getting Done at the moment. So this is commissioned as one complete job, not a discovery pass that produces another card.

If the sweep genuinely cannot close in one sitting, that is a finding worth having, and it comes back through TO Chat with the reason and the measured size of the remainder. What is not wanted is a report that names the work and leaves it open.

## The context you already hold, restated so this file stands alone

At the S060 course-card sign-off Kain asked for the school name in its school colour with the wash's lightness applied. You measured it: at 12px the AA bar is 4.5:1, five of the seven school primaries fail as drawn, and any fade fails all seven. You inverted the method, darkening each failing colour to the first step clearing the bar with hue and saturation preserved, and Kain took it.

That produced seven new tokens in `base.css`, mapped per school in `components.css` beside `--school-accent`:

```
--school-nlp-text: var(--school-nlp-primary)   5.44, unchanged
--school-cbp-text: #747940                     4.61, was 3.23
--school-lc-text:  #A66543                     4.60, was 3.85
--school-pc-text:  #A16575                     4.53, was 4.23
--school-miw-text: var(--school-miw-primary)   5.14, unchanged
--school-mh-text:  #5E73A9                     4.67, was 4.35
--school-pgd-text: #3E7E8D                     4.59, was 3.38
```

Both are now recorded on Chat's side. **DSRD 7 section 2.1** carries the token table beside the RGB companions, with the governing rule: `--school-accent` for fills, bars and decorative marks, `--school-text` for anything a reader reads. **DSRD 8 section 7.7** carries the decision narrative. DSRD 8 section 7 is otherwise brought to the signed-off card: header naming your prototype and JSON as the signed record at v0.63.0, section 7.1 rewritten to the six rulings, section 7.6's source dimensions corrected to your measured 1056x555.

## The job

**One: find every site.** Sweep the theme for every declaration where a school colour reaches a text colour property. That means `--school-accent`, `--school-{code}-primary` and `--school-{code}-secondary` landing on `color`, on an SVG `stroke` or `fill` where the mark is beside text and reads as part of it, and on anything else you find that a reader reads rather than sees as decoration. Report each site with its file, its selector, the component it belongs to, and the size the text renders at, because size decides whether the primary was failing in the first place.

**Two: apply the straight swaps yourself, no round trip.** A straight swap is a small-text use on a light ground where the text-safe token is the same hue, clears AA, and nothing a reader would call a design change results. Apply those, note them in your report as applied, and move on. Kain does not need to look at a colour becoming the compliant version of itself.

**Three: bring back what is not a straight swap, rendered.** Three kinds are foreseeable and there may be others:

- A school colour on a tinted or dark ground, where the darkened token may be worse rather than better and the measurement has to be taken against that ground rather than white.
- A large-text use where the primary legitimately passes at its rendered size and no change is needed, which you record as a ruled exception rather than swapping.
- A place where the darkened colour visibly changes a component Kain approved by eye.

These go to Kain under standing rule 16 and its S258 render standard: rendered in the artefact at the size it will be seen with its surroundings present, options tabbed one at a time in the identical screen position, real copy throughout, your self-critique run first. His S277 standing instruction on tabs binds here.

**Four: fold back.** Where a ruling lands on a component, its prototype takes the new version first, then its build sheet, then the code, per the S257 precedence. Chat records the rulings in DSRD 8 at close.

## Definition of done, as written on the board card

Every place in the theme where a school colour carries text is either moved to that school's `--school-{code}-text` token, or recorded as a ruled exception with its reason; your report lists every site found with its verdict; `css_gate` passes; the change is live in the theme and the version recorded.

## One thing to be honest about

If the find step turns up something neither of us expected, say a school colour carrying text inside a component that has no prototype or build sheet yet, name it rather than absorbing it. The sweep's job is every site moved or ruled, not every neighbouring gap closed on the way past.

*No em or en dashes in this file; checked before writing.*
