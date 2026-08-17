# RULING: the translation becomes a control the visitor chooses, not a block beneath the review (Kain, S059)

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Filed under:** Harness Rule 14, a ruling given directly in a Code session, acted on and filed the same session.
**Supersedes:** the English ruling in `COMMISSION__Reviews_Editorial_Pass_Two_All_897_S264.md`, which is Kain's own earlier ruling.
**Shipped:** theme v0.61.0, deployed and verified live.

## The ruling, in Kain's words

He proposed it himself, unprompted, after being told the 87 translations were the next piece:

> "Would it be possible to just simply have a 'Translate this text' option, which gives the website visitor the option to be autonomous and only translate the text if they wish to read it. This is a common feature I see in sites like TikTok (for example), when a comment is made in a non-english language, and beneath the text, is a 'translate' option."

And on the proposal that came back:

> "Yes, please do Claude, this is a great plan."

## What it supersedes, exactly

The S264 ruling said the student's words stay displayed "with an English translation beneath it, plainly marked". **The translation is no longer shown by default.** What survives unchanged: the student's words are never replaced, and a translation is always plainly marked as one.

## The one place the build departs from TikTok, and why

TikTok fetches the translation from a translation service at the moment of the click. **This does not.** The 87 translations are written once and stored on the review, and the click reveals text already in the page.

The reason is Harness Rule 11 rather than convenience: a live translation service is outside code on a page of a domain that takes card payments, which is a security decision and Kain's alone. Storing the text avoids the question entirely, and it is also faster, free per click, and cannot fail at the moment a reader wants it. Put to Kain in those terms and accepted.

## What was built

| | |
|---|---|
| Reviews carrying a translation | **87** |
| Languages | Spanish 27, Portuguese 22, Italian 13, Dutch 9, German 8, Polish 3, Turkish 2, French 2, Indonesian 1 |
| New fields | `review_translation`, `review_language` |
| Reviews whose own words were touched | **0** |

**Two language labels were corrected by hand**, because the label is visible to the reader: 32727 and 32795 were both detected as other languages and are Dutch. The stopword detector is good enough to find the 87 and not good enough to be trusted with what the page says, so every label was read before it was stored.

**The control degrades to the S264 behaviour rather than to nothing.** The markup ships with the translation open and the button hidden; the script closes the translation and reveals the button. A visitor with no JavaScript therefore reads the translation beneath the review, which is exactly what the superseded ruling asked for. Verified in the served HTML before any script runs.

## Verification, on the live page

Opening one control: the card grows from 520px to 789px, the masonry reflows from 8456px to 8558px, the label becomes "Show original" and `aria-expanded` becomes true. Closing it returns both the card and the grid to the pixel. The student's own words remain the first thing in the card throughout. No console errors. `css_gate` and `component_gate` both pass, and `deploy.py` proves local, server and zip agree at v0.61.0.

## The design is approved too, and the fold-back is written

**Kain ruled the appearance on the rendered live page in the same sitting**, after it was opened for him in Safari:

> "Claude, I love it, it looks great and functions exactly as I hoped it would."

So this is not only a mechanism ruling. Under Rule 14's fold-back, tightened at S258, the signed record belongs to whoever rendered the approved artefact, and here that is Code. **Both writes were made in this session:**

1. **`achology-review-card-proof-v3.html`**, in the Card System folder, is the new signed record. It supersedes v2 for this one addition and is an export rather than a redraw: the markup is the live page's own output and the CSS is the theme's own stylesheets at v0.61.0, the version he approved. Four cards carry the control and two do not, so the card is judged both ways, and the toggle is live in the file rather than drawn. **v2 has moved to Archive (Superseded)** per the folder's rule 1, and the folder README records both changes.
2. **`BUILD_SHEET__review-card.md`** gains twelve rows covering the control, the panel, the label, the fields behind them and the no-JavaScript behaviour, each marked RULED S059. Every pre-existing row is untouched and keeps its S053 approval.

So the Rule 4 chain has its top for this component: prototype, then sheet, then theme code, all three agreeing and all three carrying the same ruling.

**What is left for Chat:** DSRD 8 §14 is the decision history and does not yet mention the control. That is Chat's document, not Code's, which is why this file exists.

One thing worth carrying into it: **§14 already records that the site has no link-hover standard**, named as a gap when the course name became this card's first real link at S053. This control is its second, and it uses an underline on hover rather than a colour change, so it borrows nothing it cannot keep when that standard is finally set. The gap is now two components wide and is worth a ruling rather than a third workaround.

*No em or en dashes in this file; checked before writing.*
