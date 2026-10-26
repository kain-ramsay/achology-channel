> CHAT DISPOSITION, S446 (26 October 2026): sign-off written into DSRD 9 section 39.13; the board card moves at the next session's board consolidation. Board: moves at the next session's board consolidation.

# RULING: the Knowledge Hub front page is signed off (Kain, S180)

**What this needs from Chat:** write the sign-off home in DSRD 9 section 39 and on the board card for the Knowledge Hub front page. The look is done; the one open item, the wall's cards arriving slowly, is shared wall work with the main theme session.

**Session:** theme, the front page side session of the S180 consolidation sitting. Code wrote this.

## Kain's words, at theme 0.707.547, on the rendered page

"Yes, I'm really happy with the look of it, Claude, to be honest. Really happy with it. I think it just looks fantastic, to be honest. I think my only challenge is as I scroll down the page, a lot of the cards are really quite slow in loading."

## The fold-back (Harness Rule 14), written this session

In the Knowledge Hub Homepage design folder: the prototype `achology-knowledge-hub-front-page-proof-v1.html` (the whole page as rendered at 0.707.547, stylesheets inlined); a new last section in `BUILD_SHEET__Knowledge_Hub_Front_Page_S390.md`, "The front page as Kain signed it off", which wins over the sections above it; and `DSRD6_RECORD.md`, updated with his words, Kain's eye passed on chapters 10 and 11, and chapter 9 failed on his speed point. Project record commit 35e23073.

The three logged components (Library Banner, Mega Panel with Alphabet, Pick Where You Are Cards) are in RULING__Knowledge_Hub_Front_Page_Learning_Block_And_Three_Components_S180, their folders committed (autosave 778f5b1).

## The speed point (DSRD 6 chapter 9 fail)

Measured in WebKit at 0.707.547, scrolling at a reader's pace. Every wall picture had loaded 1 to 10 seconds before its card reached the screen, so the pictures are not the cause. The cause is the shared wall's Rise in turn: a card is held hidden until it is 8 per cent up the screen and 12 per cent shown, then fades over 0.6 seconds, 0.07 after the card before. So the median card is fully shown 1.2 seconds after it reaches the screen, and the slowest 2.5. Code's proposed fix, for the main theme session to build and Kain to see, since it changes every Hub wall: start a card's rise the moment it touches the screen, shorten the fade to about a third of a second, and cap the stagger so a whole row is in within half a second.

## Still Kain's to write

His own words for the panel's and the wall's section headers and lines (the wall's line is 11 words, the gate wants 12 to 25). The cards' heading and line are Code's stand-ins he kept; your "Where Would You Like to Begin With Achology?" has not been put to him.

*No em or en dashes in this file; checked before writing.*
