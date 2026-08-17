# RULING: the course row is three across on desktop, two on tablet, two on phone, and carries three cards

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Filed under Harness Rule 14.** Acted on in v0.40.1, live and rendered.
**Owning documents:** DSRD 8 §7.0 (the phone tier) and DSRD 9 §32.1 item 6 (the card count).

## What Kain said

Looking at the built Book Note page:

> "These course cards look really, really bad, like, really bad. These course cards are not okay at all. I don't know if you've checked the actual specifications or whether you just guessed. These course cards are not what I signed off with Claude within chat a long time ago. They're stretched."

And then the ruling itself:

> "I think from a responsiveness level, we need three course cards on desktop, two on iPad, and probably two on mobile."

## What was actually wrong, which is worse than the ruling

He was right that they were stretched, and right to ask whether I had read the spec. **The spec was open in front of me and I did not apply it.**

DSRD 8 §7.0 already says, word for word: "**Grid:** 3 columns desktop (≥ 1024px), 2 tablet (768 to 1023px), 1 mobile (< 768px) (per DSRD 7 §4.1). Gap 24px."

That grid was already built, in `cards.css` as `.product-section__grid`, and **no template had ever used it.** I wrote a two-column grid of my own instead. Each card rendered at 540px wide against a card designed at roughly 368px, which is what he saw. Now 352px at desktop and 406px at tablet, from the spec's own grid.

So one half of this file is a defect report, not an amendment: the page should have been three across from the start and nothing needed ruling to make it so.

## The amendment that IS his ruling, after I got it wrong once

I first read "two on mobile" as two COLUMNS and built a two-up phone grid. That made each card 156px wide and 702px tall, and he sent it straight back: "you've made an absolute mess here." He meant two CARDS. His clarification, in full:

> "From desktop, responsiveness is three cards across the screen. From iPad, you go to two course cards across the screen. And when you go into mobile, you're gonna go two course cards, one on top of the other."

**So DSRD 8 §7.0's columns need no amendment at all.** 3 / 2 / 1 is already exactly what he described, and the page now takes that grid untouched. Worth recording plainly, because I have now written two different overrides to a rule that was correct as it stood, which is twice more than it needed.

**The one real amendment is to DSRD 9 §32.1 item 6, the card count, and it is per tier:**

| Tier | Columns (DSRD 8 §7.0, unchanged) | Cards |
|---|---|---|
| Desktop, 1024px and up | 3 | 3 |
| Tablet, 768 to 1023px | 2 | 2 |
| Phone, below 768px | 1 | 2, stacked |

§32.1 item 6 currently reads "Explore related learning paths: section header plus two course cards", and brief §3 row 7 says the same. It becomes three at desktop, two below. The third card is withdrawn under 1024px in CSS, which is what stops three cards leaving an orphan on a two-column row and a three-deep stack on a phone.

## Measured on the rendered page, all three tiers

| Width | Columns | Cards visible | Per row | Card width |
|---|---|---|---|---|
| 1440px | 3 | 3 | 3 | 352px |
| 900px | 2 | 2 | 2 | 406px |
| 375px | 1 | 2 | 1, 1 | 335px |

No horizontal scroll at any width, and the card keeps its designed proportions at all three, which is exactly what it lost when I stretched it to 540px.

## The thing he raised that is not mine

> "It might mean I need to kinda have a a brand new cards session with Claude in chat."

That is his call and yours. Flagging it so it is on your side of the road: he is not certain the card as built is what he approved, and the approved prototype for THIS page carries a prototype rendition of the card rather than the real component, so the two have never been compared side by side on a rendered page.

## Two other things fixed in the same change set, from your S252 instruction

**Card CTAs now use the real checkout.** Per `INSTRUCTION__Replace_Invented_Course_Data_On_Article_Template_S252.md` item 4 and DSRD 4's rule, "Every Buy/Enrol/Join button links to a community.achology.com/checkout/ URL". All 28 URLs are copied one by one from DSRD 4's table rather than derived, because the checkout slug is not derivable from the course slug: `life-coaching-certificate-course`, `hypnotherapy-practitioner-course`, `the-goal-setting-and-strategic-action-planning-masterclass` and `authentic-confidence-identity-and-self-esteem-masterclass` all diverge from both the course name and the DSRD 1 URL.

**Learn More keeps the DSRD 1 §2.3 course page address.** It 404s until those 28 pages exist, and the page gate reads it as planned-not-built rather than broken. Say if you would rather it pointed at the checkout too in the meantime.

## One conflict I did not resolve

DSRD 7 §1.0 requires a visible `ExternalLink` arrow inside every external link's label. Enrol Now is now external. DSRD 8 §7 is a **LOCKED** card and §7.1 fixes its CTAs as two plain buttons. Adding the glyph would change an approved component's appearance to satisfy a site-wide rule; leaving it out breaks §1.0. The button carries `target`, `rel="noopener"` and the visually hidden "opens in a new tab", and no arrow. Your ruling either way.

*No em or en dashes in this file; checked before writing.*
