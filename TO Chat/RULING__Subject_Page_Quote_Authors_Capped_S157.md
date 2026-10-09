**Needs from Chat: write these three rulings into DSRD 9 section 20.0 (the grid, and a new responsive paragraph) and DSRD 8 section 6.0 (the quote on the wall); the build sheet already carries them. For the theme session's record.**

# RULING: three more subject page rulings (Kain, Code's S157 theme sitting)

## 1. No author takes more than two quotes on a wall

**Kain's words:** "all of the quotes on the page are all Kane Ramsey, which kind of isn't great ... it just oozes us trying to make Achology the Kain Ramsay show"; then, choosing the number: "Let's make it a limit of two quotes per author per wall, with the authors alternating."
**Built at 0.707.162.** A wall's quote pool is capped at two per author, newest first within an author, the authors taking turns. The site holds two quote authors so far (Kain Ramsay 267, Gerard Egan 25), so every wall shows four quotes, Kain, Gerard Egan, Kain, Gerard Egan, until more authors arrive. The Quotes filter counts the quotes the wall shows.

## 2. A quote on the wall is its own baked card picture

**Kain's words:** "for every single quote page, every quote can be downloaded as a JPEG ... why don't we just use the actual images of the actual quotes, not you trying to recreate them ... with a face baked behind the background"; after seeing it: "I think the images are actually really good ... I think they look fine, enough for someone to click on anyway."
**Built at 0.707.164.** The tile is the quote's featured image (the baked card the quote page shows and Download hands out), linked to the quote page, at one column wide. Only a quote whose picture is baked is used: 275 of the 292 published quotes have one, and the 17 newest do not, so they cannot appear on a wall until they are baked. This supersedes the S157 first build, which used the signed quote card (DSRD 8 section 6.3) as a text tile; the signed card remains the fallback in the code for a quote with no picture and is not reached today. A two-column-wide tile (more legible) was offered and not asked for.

## 3. The wall's columns, and the page's responsive layers

**Kain's words:** "on desktop can be four, on tablet just needs to be three, and on mobile can probably just be two. That's within the wall ... do a responsive check on the responsiveness layers right across the entire page, which obviously then rolls over to all seven pages."
**Built at 0.707.165 to 0.707.167,** the theme's breakpoints (tablet 768 to 1023, phone under 768; desktop unchanged):
- The wall: four, three, two across; the masonry reads the column count from the page, so the column feet stay level at each.
- The Categories bar: on tablet and phone the seven names scroll sideways beside their label (they overflowed at tablet, 846 pixels in a 768 screen).
- The lead row stacks (picture across, the Editor's Picks in two columns on tablet, one on phone); the band's faces fall under the words on phone, the lead face across the top; the search box sits over the filters on phone; the topics stack with the tiles three across on tablet and two on phone (the odd last tile spans the row); the learning path tightens inside and its step pictures shrink on phone.
- Page gutters follow the container: 32 on tablet, 20 on phone.
**Checked:** all seven categories at phone width, Psychology at tablet and at 1024 and 1276 wide: no sideways overflow, wall columns as above, column feet level to within a pixel. **Not checked:** a real phone or iPad (the browser emulation only), and landscape orientation.

## 4. The search box's words, and the quote tile as a full card

**Kain's words:** "the search bar currently says search psychology, that needs to change across all seven pages ... search the knowledge hub"; and of the quote tile: "I really like the quote cards ... however, there's nothing that says that it actually links through to a quote article ... do you think it'd be worthwhile turning the image into an actual card, like the rest of the cards on the wall?"
**Built at 0.707.168.** The box reads "Search the Knowledge Hub" on every category (it is still drawn only, and searches nothing until the site search page is built, BRIEF S375). The quote tile keeps the baked picture on top and gains the card body the other tiles carry: the orange "Quote" label and the quote's own headline (for example "Why Every Coaching Relationship Begins with a Goal"), in the same card frame, so it reads as a link to a quote page. Code proposed this after Kain's question and built it for his eye. **Kain then simplified it (same sitting, 0.707.169):** "we can make the quotes card just a little bit simpler ... write quote article as the text, then with a number of words, and then the minute read next to it." The quote tile now carries the picture, the label "Quote Article" and "802 Words · 5 Minute Read" (the same one count the quote's own page prints, DSRD 8 section 6.0's card rule), with no headline. This closes the quote card's earlier gap in the card rule.

## 5. Each card's label carries its kind's icon

**Kain's words:** "given that we've got four different types of content, and each content kind of has its own icon ... do you think it might be a nice touch to build the icon into each of the appropriate cards ... it might just come before the word article or quote article or book note or workbook." **Built at 0.707.170:** the same registry icons as the filter bar (article, book note, quote), 16 pixels, link orange, before the label on every wall card. A workbook card will take its own icon when the wall has a workbook tile; none exists yet.

## 6. A Know Your Psychology card fills a big gap in the wall

**Kain's words:** "on the bottom row of cards ... you're aligning all of the articles in the bottom. It just means that there's quite a bit of white space in some of them ... there might be space to include a Know Your Psychology logo into the grid ... essentially a card with a Know Your Psychology logo built into it, central aligned, that if clicked on would link back to the Knowledge Hub homepage ... allow us to not have any cards with a really overwhelming amount of white space." He then corrected Code's first try (the illustrated panel, the article column's picture): "I was just referring to the actual logo ... there are actual Know Your Psychology logos, titled KYP."
**Then Kain set the rule:** "one standard ... stretch that one logo so that it extends to the end of the card ... it doesn't shrink and it only gets placed into the grid if there is sufficient space ... by shrinking the logo, it looks like we're just cramming it in ... there should be a maximum of one. And that's not a rule. It's just we're not trying to squeeze it in for the sake of it."
**Built at 0.707.175.** One standard card: the generic logo, `The Knowledge Hub KYP Logo` (Kain's file, converted to a 16 KB transparent WebP), stretched across a white card at a fixed size (119 tall at a 1276 screen), linking to the Knowledge Hub home page. The layout places it only where the biggest free space at the foot of a column can hold it at that size and where standing it among the last cards levels the columns better. Result at 1276 wide: one on Mental Wellness, Motivation, Personal Growth and General Interest; none on Psychology, Helping People and Wisdom for Life. Code chose the generic mark over the seven coloured school versions because the wall is the whole Hub; Kain said yes.
**Still open, named honestly:** one logo card does not remove the stretching. Motivation, Personal Growth and others still carry last-card stretches of 100 to 170 pixels in the other columns, because the columns end at different heights. Code proposed letting the wall show 45 to 48 cards, dropping up to three of the oldest when that levels the feet better; not built, Kain has not ruled.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
