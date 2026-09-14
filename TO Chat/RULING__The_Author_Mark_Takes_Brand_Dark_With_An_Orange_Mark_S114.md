# RULING: the drawn author mark takes the brand dark with an orange mark, and the section-colour idea is withdrawn

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Filed under Harness Rule 14.** Supersedes section 4 of `RULING__Kain_Approves_The_Drawn_Author_Mark_S114.md`, filed earlier this session, which named the colour as the one value still open.
**Shipped:** Theme 0.394.0, deployed and verified on the live install.
**Board card:** Book note page template; Book author portraits.

---

## 1. Kain's words

The mark shipped at 0.393.0 drawing a blue. He asked:

> "Why would we use blue instead of colours from our brand pallette - like our own orange?"

Three grounds went to him on the live Tara Brach book note, one variable between the tabs, everything else held identical. He ruled:

> "Brand dard with an orange mark looks great - lets go with this one!"

## 2. What is approved, and it is live

The site's own dark into the darker footer tone, with the orange doing what the orange does everywhere else on this site: marking rather than filling. The ghosted initial is the orange at twenty percent, the short rule is the orange at full strength, and the name is the warm cream.

Every value is in `BUILD_SHEET__bn-author-mark.md`, updated this session in the Book Note Page folder. Every colour in the component is written as a token through `color-mix`, never as an rgba of its numbers, so a change to the brand's dark or orange reaches the mark rather than leaving it behind.

## 3. The reasoning is written into the CSS, deliberately

Two sentences sit in the component's own comment block so that a later session reaching for more brand colour finds out why it should not:

**A solid orange plate sits directly beside the reading, and orange on this site means a link or a button**, so a block of it competes with every real button on the page.

**And the name reads far better on the dark.** Computed from the tokens rather than judged by eye: warm cream on the brand dark is 10.08 to 1, brand dark on the primary orange is 3.32, and warm cream on the primary orange is 3.04, against a bar of 3 for large text. The orange option was not unreadable. It was close to the line and loud.

## 4. Where the blue came from, so the mistake is on the record and not just the fix

It was the Mental Wellness school's own pair, carried over from an idea that each plate would take the colour of the section its note sits in. **That idea had nothing behind it:** no mapping from a Knowledge Hub category to a school colour exists anywhere in this project, and the two sets are not the same seven.

So the blue reached twenty one live pages as a leftover rather than as a decision, and it was Kain who spotted it rather than the session that shipped it. **The section-colour idea is withdrawn entirely**, and section 4 of this morning's ruling file, which named the colour as an open question awaiting him, is closed by this one.

The first draft of the sitting that carried the three options also stated three of its four contrast figures from memory, and all three were wrong. They are computed from the tokens now and printed when the builder runs, so the numbers in front of Kain are the numbers.

OWED BACK: nothing. This closes the colour, and with it the last open value on the component. What remains outstanding on the mark is only the prototype export named in section 5 of this morning's ruling file, which is Chat's call.

*No em or en dashes in this file; checked before writing.*
