**For Chat. What this needs from you:** write Kain's two S183 quote card rulings home into DSRD 9 section 20.0h (the one wall) and wherever BRIEF__One_Wall_For_The_Whole_Knowledge_Hub_And_The_Quote_Card_Family_S442 item 9's shapes were recorded.

# RULING: upright quote cards fit their words, and a quote card is never stretched to level a wall (Kain, Code S183, theme main session, 26 October 2026)

**Kain's words.** On the front page wall: "on the quote cards, like, it's like you have a standardized length for each quote card. So there's literally a gap underneath the quote ... and the bottom of the card. There's like literally dead space inside of the actual quote images." Then, to "quote cards are never stretched; the other cards in the column take the height": "Yes, please go ahead, Claude." Then, shown one Safari page with two tabs (the signed one shape, and the cards fitting their words): "Yes, tab 2. Make the quote cards fit their words on every wall."

**What is now the standard.**
1. **The upright quote card fits its words.** No fixed 4 by 5 shape (the S180 record's "upright at least 4 by 5" is withdrawn). The wide card keeps the signed 1200 by 630. The card itself is otherwise unchanged (cream canvas, mark, toned portrait, words, name, logo, Read This Quote Article at the foot). Live 0.707.557, commit 7ab354e7, kh-subject.css.
2. **A quote card is never stretched to level a wall while another card in its column's run can take the height** (kh-subject.js share()). Live 0.707.556, commit 7565a25d. On the front page and the seven subject pages, no quote card is stretched at 1280, 834 or 390; every foot level within 1 px.

**One case open, put to Kain in the same sitting.** On the Quotes list walls every card is a quote, so to end level the wall still stretches some quote cards (live 0.707.557: up to 14 a wall, most 74 px at 834). Kain's answer, the same sitting, to "should a stretched card's spare space sit evenly above and below its words?": "yes". Live 0.707.560, commit 17fcbeca: a stretched quote card centres its words (kh-subject.css .kq.is-grown; the wall marks the cards it grows); measured in WebKit on /learn/quotes/ at 1280, 834 and 390, the space above and below is equal on every stretched card (0 px difference).

OWED BACK: the dated lines in DSRD 9 section 20.0h.

*No em or en dashes in this file; checked before writing.*
