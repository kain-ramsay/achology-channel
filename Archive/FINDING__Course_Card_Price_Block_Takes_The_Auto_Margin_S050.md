# FINDING: the course card's auto margin is on the wrong element, and it is what Kain is looking at

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Not fixed, deliberately.** `RULING__Course_Card_Enrol_Button_No_Arrow_S252.md` says "Build nothing new on the course card until it is settled", and the cards session is pending. This is input for that session.

## What Kain said, and what I went and measured

> "The structure is good, but they're just a little rubbish. And also the spacing within them is absolutely terrible. Like, I don't know whether this is you or whatever, but it's absolute diabolical spacing."

He asked whether it was mine. It is not the Book Note page's doing, and it is not a matter of taste. **It is one line in `cards.css`, and it has been there since the card was built.**

## The measurement

I measured the rendered card against DSRD 8 §7.2, value by value. **Everything matches except one thing:**

| §7.2 value | Spec | Built | |
|---|---|---|---|
| Image area height | 185px | 185px | pass |
| Accent bar | 3px | 3px | pass |
| Info padding | 20 / 24 / 20 / 24 | 20 / 24 / 20 / 24 | pass |
| School name to title | 10px | 10px | pass |
| Title to stats | 10px | 10px | pass |
| Stats to hairline | 16px padding-bottom | 16px, 1px border | pass |
| Hairline to price | 16px | 16px | pass |
| Price to CTAs | **margin-top auto + 16px padding-top** | margin-top 16px, padding-top 0 | **the defect** |
| Card foot | 20px | 20px | pass |

## The one line

§7.2 says, word for word: "**Price → CTAs:** margin-top auto + 16px padding-top". The `auto` belongs on the **CTAs**. `cards.css` puts it on the **price area** instead:

```
.card--course .card__price-area { margin-top: auto; padding-top: 16px; }
.card--course .card__ctas      { margin-top: 16px;  padding-top: 0; }
```

## Why that one line is what he can see

`margin-top: auto` in a flex column pushes everything from that element down to the card's foot. On the CTAs, as §7.2 specifies, only the two buttons are pushed down: the price sits directly under the stats hairline where it belongs, and any slack in a card with a short title collects harmlessly between the price and the buttons.

On the price area, as built, **the price and the buttons are pushed down together**, and all the slack collects in one visible hole between the stats line and the price. The taller the card's neighbours, the bigger the hole. On the Book Note page the three cards have titles of two, two and three lines, so every card inherits the tallest one's slack and every card shows the gap.

That is the "diabolical spacing", and it will appear on every page that ever renders a course card, not just this one.

## The fix, when the cards session releases it

Two lines swapped:

```
.card--course .card__price-area { padding-top: 16px; }
.card--course .card__ctas      { margin-top: auto; padding-top: 16px; }
```

No new value, no design decision, no token. It restores §7.2 exactly as written. I have not applied it, because the instruction says build nothing new on this card until the session settles, and because if Kain is going to look at the card properly he should look at one that behaves as its own spec describes.

**My recommendation:** apply this one correction BEFORE the cards session rather than after. Judging the card with a defect in it risks him redesigning around a fault instead of seeing the card he actually approved. One line, one re-render, and then the session starts from the real thing.

## One thing the session should know

The Book Note page's approved prototype draws its own rendition of the course card in prototype classes, not the real `.card--course` component. So the card Kain approved by eye at S239 and the card the theme renders have never been put side by side on a rendered page. That is worth doing first, before any redesign, because the answer may be that the built card is fine once this margin is corrected.

*No em or en dashes in this file; checked before writing.*
