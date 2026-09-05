# INSTRUCTION: apply the auto-margin correction now, before the cards session

**Written S252 by Claude Chat. Date: 2026-08-07.**
**Answers your `FINDING__Course_Card_Price_Block_Takes_The_Auto_Margin_S050.md`.**
**Releases the hold in `RULING__Course_Card_Enrol_Button_No_Arrow_S252.md`, for this one correction only.**

## Apply it

Your recommendation is accepted and your reasoning is the reason:

```
.card--course .card__price-area { padding-top: 16px; }
.card--course .card__ctas      { margin-top: auto; padding-top: 16px; }
```

**This is a defect fix, not a change to the card.** DSRD 8 §7.2 says "Price to CTAs: margin-top auto + 16px padding-top", the `auto` belongs on the CTAs, and `cards.css` has had it on the price area since the card was built. Restoring it needs no ruling from Kain because he already ruled it when he approved §7.2. Nothing else about the card moves.

**The hold stands for everything else.** Build nothing new on the course card, change no value that is not this one, until the cards session settles.

## Why before rather than after

You are right, and this is the sentence worth keeping: judging the card with a defect in it risks Kain redesigning around a fault instead of seeing the card he actually approved. One line, one re-render, and the session starts from the real thing.

## What the cards session gets from you

Two things, and they shape it:

**1. The comparison has never been done.** The Book Note page's approved prototype draws its own rendition of the course card in prototype classes, not the real `.card--course` component. So the card Kain approved by eye at S239 and the card the theme renders have never been put side by side on a rendered page. That comparison is the session's first act, before any redesign is discussed.

**2. Your honest note that the correction may change nothing visible on this page**, because all three Book Note titles wrap to two lines and there is no slack to redistribute. That is worth Kain hearing plainly rather than discovering. It matters on pages where course titles differ in length, which is most of them.

So the session opens with a real question rather than an assumption: **is the built card actually wrong, or was Kain reacting to a stretched two-column grid and a misplaced margin, both of which are now fixed?** Neither of us knows, and the render will say.

## Recorded

The three `cards.css` one-offs Kain approved (two focus-ring radii at 2px, the `#6b7078` missing-cover placeholder) are being written into DSRD 7 §4.5's exception register alongside the five stack points recorded earlier this session.

Your distinction in that file is the right one and is worth stating back: **citing a value that a specification already names is recording provenance, which is yours to do. Annotating a value that no specification names is approving an exception, which is Kain's.** That is why the four DSRD 8 §6.2 and §6.9 values took citations from you and the three one-offs waited for him.

`testimonials.css` and its 24 issues get the same one-question treatment when someone is next in that file. Not swept, not quietly cleared.

*No em or en dashes in this file; checked before writing.*
