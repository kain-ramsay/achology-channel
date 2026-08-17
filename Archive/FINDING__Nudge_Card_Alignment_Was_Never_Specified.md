# FINDING and SHIP: the nudge card's alignment was never in DSRD 8, and the theme lost it

**From:** Claude Code, S046. **Date:** 2026-08-05. **Shipped:** v0.38.16, verified.
**Raised by Kain** from the rendered mega menu, unprompted.

## What he saw

> "in the mega menu, when I drop down under the academy, courses and knowledge hub,
> we have a grey block to the right hand side of each. That was all centered
> aligned. And for some reason, it's been knocked out. Now it is left aligned, and
> that's not correct. That was not a design I approved."

He was right that it was wrong, and right that he never approved it. He was wrong
about one thing only, and it matters: **nothing changed it. It has been wrong since
the header was first built.**

## What actually broke: one property, moved one level down

The approved prototype, `02. Prototype Design Files / Production Ready Files /
achology-header-menu.html`, read this turn:

```
line 125  .nudge-card { ... align-self: start; flex-shrink: 0; }
line 129  .nudge-cta  { display: inline-block; ... text-align: center; ... }
```

The **card** carries `align-self`. The **button** carries `text-align: center` and no
`align-self`, so as a flex item in a column card it stretches to the card's inner
width and centres its label.

The theme had it exactly inverted:

- `.nudge` carried neither `align-self` nor `flex-shrink`.
- `.nudge__cta` carried `align-self: flex-start`, which shrank it to its own text
  and pinned it to the left edge.
- The button's `text-align: center` had been dropped entirely.

**Measured before the fix:** the card stretched to 253px against 245px of content;
the button rendered 156px wide inside 172px of usable width, hugging the left.

**When it happened:** `git log -S` shows the nudge rules have **exactly one commit in
their entire history**, the v0.6.6 backup, and were never touched again. This was a
transcription error at the moment the prototype became theme CSS, not a regression.
It has been shipping wrong on every page of the site since.

## Why no gate could ever have caught it

**DSRD 8 §18.12 specifies this card's background, border-radius, padding, width,
internal gap, and every type style, and says nothing whatever about alignment.** I
checked the per-dropdown sections §18.9 to §18.11 as well; they carry content only.

A gate cannot test a value the document does not hold. `css_gate` passed this file
every time, `page_gate` had nothing to compare against, and the only instrument that
would ever have caught it is Kain's eye, which is exactly what happened, eleven
weeks after it shipped.

**Please add the alignment to §18.12**, so it becomes testable:

- Card: `align-self: start`, `flex-shrink: 0`.
- CTA button: stretches to the card's inner width, label centred, no `align-self`.

## Also cleared, and worth your attention

`header.css` failed `css_gate` on four counts before this change and **now passes for
the first time**. None of the four was drift. Every one was a value DSRD 8 specifies,
faithfully built, that simply carried no citation:

| line | value | where it is specified |
|---|---|---|
| scroll shadow | `0 2px 12px rgba(53,65,73,0.06)` | §18.4 |
| dropdown shadow | `0 12px 32px ..., 0 4px 12px ...` | §18.7, and character for character `--shadow-dropdown` |
| hover icon ring | `0 0 0 1.5px rgba(237,105,34,0.35)` | §18.13 |
| nudge CTA radius | `8px` | §18.12, Kain's S245 registered exception |

The dropdown shadow is now the token, since the value already had a home. The other
three carry their section number. No pixel moved.

**The pattern worth naming:** a specified value with no citation is indistinguishable
from drift to every instrument we have. That is four false alarms in one file, and it
is why the health check I built this session found 38 across four stylesheets. Most of
those will be the same thing.

## Verified on the rendered live page, all three menus

| card | card align-self | button width | card inner width | label |
|---|---|---|---|---|
| Try Our Community (Academy) | start | 172px | 172px | centred |
| Access All Courses (Courses) | start | 172px | 172px | centred |
| Try Our Community (Knowledge Hub) | start | 172px | 172px | centred |

`css_gate header.css`: PASS.

*No em or en dashes in this file; checked before writing.*
