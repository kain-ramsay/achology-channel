# RULING: the three unnamed cards.css values are approved one-offs

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Filed under Harness Rule 14.** Applied in v0.40.4, deployed, `css_gate cards.css` PASS.
**Owning document:** DSRD 7 §4.5's approved-exception register, alongside the five stack points recorded at S252.

## What Kain said

Put to him as one yes or no, after `cards.css` was left failing its gate rather than tidied away:

> "yes, record those three values as approved one-offs so cards.css passes clean"

## The three

| Selector | Value | Why it had no rule |
|---|---|---|
| `a.card__footer-cta:focus-visible` | `border-radius: 2px` | A focus ring on a text link. DSRD 7 §5.3's tiers govern surfaces, and **no focus-ring radius is written anywhere in DSRD 7**, so this value never had a rule to follow. It traces the link's own text box; a 10px corner bows away from a short label. |
| `a.card__footer-info:focus-visible` | `border-radius: 2px` | The same ring on the footer's secondary link. |
| `.book-cover--placeholder` | `background: #6b7078` | Deliberately outside the palette. It marks a book note with no cover, which DSRD 8 §20.2 calls "a data error that blocks the page, never a rendered fallback". A brand colour would read as a design choice; this should read as nothing, so a missing cover gets noticed and fixed. |

All three are annotated in place with the reason, the approver and the date, which is DSRD 7 §4.5's own pattern for an annotated one-off.

## Why they waited for him rather than being annotated at S049

Because you confirmed the reading at S252 and it held here: **annotating an exception is the act of approving it, and approval is Kain's.** They sat failing the gate for a session rather than be quietly cleared by the person who found them. That is the rule working, not friction.

## The gate now

13 of 14 stylesheets PASS. `testimonials.css` still fails with 24 pre-existing issues. Those were not touched this session and are not mine to annotate either, for the same reason. They need the same one-question treatment when someone is next in that file.

## Two other things settled in the same stretch, both recorded here so they are not lost

**1. Four values were cited, not approved.** The DSRD 8 §6.2 book cover radius and shadow, and the §6.9 mini thumbnail radius and shadow, are all named in the spec. The gate could not tell them from one-offs without a citation, so they now carry one. That is recording provenance, which is mine to do, and it is a different act from approving an exception.

**2. The auto-margin correction did not do what I hoped, and the record should say so.** Moving `margin-top: auto` from the price block to the CTAs restores DSRD 8 §7.2 exactly, and it matters wherever course titles differ in length. On the Book Note page's three cards it changes nothing visible, because all three titles wrap to two lines and there is no slack to redistribute.

**So the card now matches §7.2 on every measurable value, and Kain still does not like it.** That is worth putting in front of him plainly at the cards session: what he is reacting to is the design, not a build fault, and no further correcting by me will move it.

*No em or en dashes in this file; checked before writing.*
