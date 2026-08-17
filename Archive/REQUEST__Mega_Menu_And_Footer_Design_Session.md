# REQUEST: a design session on the mega menu and the footer, with the measurements ready

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Kain's own proposal**, made in session after looking at the rendered menu:

> "would this be a design call that I should deliver with Claude Chat rather than us
> iterating and trying to figure this out in here? because I can just do a focus
> session in there and maybe just review the entire mega menu layout and the footer
> in one quick tidy up session."

**I agreed, and strongly.** Everything below is measured off the rendered live page at
v0.38.16, so the session opens with facts rather than impressions.

## Why this is a design session and not a defect list

Kain raised two things about the nudge card after I restored its button. **Both of his
observations are accurate, and both describe the current design working as written.**
That is precisely what makes them his and yours, not mine:

1. **"The blocks of text on the card are still left aligned."** True. The overline,
   title and body all compute `text-align: start`. **And that is what the approved
   prototype does**: `achology-header-menu.html`'s `.nudge-card` sets no text-align.
   Centring them changes an approved design; it does not correct a fault.
2. **"There's more space underneath the button than there is on the left and right."**
   True, and he caught a 4px difference by eye. Measured: 28px below the button, 24px
   at the sides. **And that is exactly what DSRD 8 §18.12 specifies**, "Padding | 28px
   24px".

What was genuinely broken, I fixed and filed separately in
`FINDING__Nudge_Card_Alignment_Was_Never_Specified.md`: the button had lost its
stretch and its centred label. What remains is taste, and taste needs him looking.

## The measurements, for the session

The nudge card as built, all three dropdowns identical:

| property | measured | source |
|---|---|---|
| width | 220px desktop, 190px tablet | §18.12 |
| padding | 28px top and bottom, 24px left and right | §18.12 |
| internal gap | 8px | §18.12 |
| button top margin | 8px, on top of the 8px gap | **not specified anywhere** |
| button | fills the card's 172px inner width, label centred | prototype, restored S046 |
| overline, title, body | left aligned | prototype |
| card | `align-self: start`, does not stretch | prototype, restored S046 |

**Worth putting in front of him:** the button's 8px margin-top sits on top of the 8px
gap, so the space above the button is 16px while every other internal gap is 8px. That
16px is specified nowhere and was inherited rather than decided.

## What I would render for him, offered and freely ignorable

1. **The card both ways**, left-aligned as now and fully centred, at real 220px size
   inside a real dropdown. This is unanswerable in words; he told me so himself today.
2. **The padding even against uneven**, 24 all round versus today's 28/24, at real
   size. A 4px difference is invisible in a table and obvious on screen.
3. **The footer in the same pass.** Today's button work already showed the footer CTA
   card and the header chrome carry specifications that disagreed with each other, and
   §19.7 has been amended once this week already. Settling both surfaces together
   stops a third round.

## One standing lesson from today, which is why this is routed to you

Earlier this session I asked Kain to choose a button size **in words**. His answer:
"you just dump me walls of words, and I'm visual. So I need visual context for making
this decision... I can't give an answer to your words without seeing anything." That
is now permanent in my notes. Anything he would look at either gets rendered for him
or comes to you. This is the second case in one day, which suggests the routing is the
rule rather than the exception.

*No em or en dashes in this file; checked before writing.*
