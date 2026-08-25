**DISPOSITIONED S306: read in full. The page is signed; the outstanding items (DSRD 9/8/7 corrections, the two accessibility defects) addressed or backlogged in RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md. Board card: Knowledge Hub Page Designs.**

# RULINGS: everything Kain settled on the article page at S082, and the page is signed

**From:** Claude Code, Session 82. **Date:** 24 to 25 August 2026.
**Authority:** Kain, in the sitting, on the rendered live page in Safari, one variable at a time.
**Shipped:** theme v0.94.0 through v0.99.5, each deployed and verified.
**Board card:** Knowledge Hub Page Designs, line 1.
**Reads with:** `RULING__The_Article_Page_Rulings_S081.md`, which this closes out.

**THE PAGE IS SIGNED.** His words, before the final tidy: "I am 100% happy with this template page now". Every item the S081 file left open is settled below, except the ones open by their own nature, which are recorded at the foot rather than quietly dropped.

The two machine lines that still fail on its readiness record are filed separately as `FINDING__The_Article_Pages_Two_Open_Gate_Lines_Are_Component_Work_S082.md`. Neither belongs to this template.

---

## 1. The foot, built at last

The reorder Kain approved by eye at S081 is built (v0.94.0). The order is: author signature, hairline, the course row, hairline, Related Further Reading, the source block, then the enquiries panel closing the page.

**Three things it supersedes**, each named in the code beside the change:

- **§22.1's block order.** The thirteen-item list puts Related Further Reading above the source block and the course row below both. This inverts the two halves. The source block stays beside the related reading, because §22.1 has always treated items 8 and 9 as one zone and his order does not name it. That placement is Code's call, overturnable on sight.
- **§22.8's card row and its S302 count.** A list of names is not the compact card, so both rulings go with it rather than being adjusted. The measured fault that reopened the count at S081, every real title truncated at three cards, cannot occur in a list. **The three-or-two question the S081 file left open is therefore dead rather than answered.**
- **§22.10a's closing panel.** The Where next panel is off the page.

The enquiries panel is the site's own `achology_warm_room`, with its copy taken unchanged from the pages already running it. `about.css` owns `.warm-room`, so the article page now enqueues that stylesheet rather than a second copy being written (DSRD 3 §2.6).

## 2. Where the source-author back link went, and it costs nothing today

§22.10a records that the Where next panel's row 1 "closes the source-author back link DSRD 1 §6 requires of every article, quote and book note, which this page had nowhere else". The enquiries panel does not carry it.

**Measured before it was called a cost: that row has never rendered on any article on the site.** It wants the source author, which DSRD 1 §3 defines as a different person from the byline, and no field on an article carries one. §3.4 says the label is "assigned at production" and nothing does. It was derived from the source book note, and no article resolves one. So the rule was already unmet and removing the panel does not make it more so.

**Where the link goes when the field exists stays Q6 on the build sheet**, which is already open and already owns exactly this question. It was not answered by guessing at a home for it.

## 3. The contents and share card

Settled across the sitting, in this order, each on the rendered page:

- **A mark before each heading, on the same line as the words.** Built first as a rule above the heading with the Achology bubble on it, which was the wrong reading; corrected the same sitting on his words, "I mean to place them on the same line before the actual text".
- **The bubbles are replaced by real marks.** `list-ordered` before Table of Contents, because the entries are numbered on the page, and `share-2` before Share this Article. **Both are new to the theme's icon registry and DSRD 7 §5.2 is owed both rows**, alongside `link`, `lightbulb` and the WhatsApp glyph, which S081 already left owing. Both drawings were copied from Lucide's own published source, lucide-static 1.34.0, not written from memory.
- **Table of Contents comes up one step, 21 to 24**, and gains 24px of air under it. Share this Article stays at 18 and keeps its 16.
- **The share circles: reverted, then quieted.** They were tried white with bubble-orange marks and he rejected it on sight: "revert back to what they were please". The 10% orange tint and the AA-safe orange are back. The marks inside came down from 16 and 18 to 14 and 16. **Size rather than colour, deliberately:** on that pale ground the AA-safe orange is already close to the 3:1 floor DSRD 6 §7 gates against, so lightening it would have bought subtlety by failing the scan.
- **The circles came down again to 28px**, from 32, so the card could be narrowed.
- **One orange in the block.** His words: "standardise your use of orange colour in this block, it looks a bit of a jumbled up mess of different colours now." The two heading marks were the only thing on the brighter #ED6922; everything else was already on the AA-safe #B8460F. The marks moved. The 10% wash behind the circles is a background rather than a mark and is untouched.
- **The heading marks sit at 0.85em**, about the cap height of the words beside them. At the 1.05em the bubble had used, an outline glyph stands taller than the capitals and reads as parked beside the words rather than on the line.
- **The numbers match their titles.** 12 to 14, the title's own size, with tabular figures so every title starts at the same point down the list. His words: "the two are not currently aligned with each other and this is visually obvious." They were already on the same baseline; two sizes on one line read as a misalignment whatever the baselines do.

## 4. The card is back at the 36% it was ruled to, and it had never been there

Asking for the card to be narrowed found a fault rather than a preference. The top grid ran `1.45fr 1fr`, and its own comment claimed that gave "about 320, which is the width the card was already ruled to at 36% of the column". Measured on the page: 880 less the 24px gap is 856, and 856 over 2.45 is **349**. The card had been 32px wider than the ruled width since the top grid was built, and the arithmetic was never checked against a render. It is `1.7fr 1fr` now, which lands at 317, and 36% of 880 is 316.8.

## 5. The author signature block: the band goes

Ruled on four renders of the whole page in tabs: the band gone, the card at half width, the block removed entirely, and the page as it was. His words: **"The band goes - a simple and clean solution. Much better!!"**

The off-white ground, the 10px corner and the 20px padding are withdrawn; the portrait, name, role and bio all stay, and the portrait comes to 44px. The block went from 92px tall to 47 without losing anything in it. **§22.7's card anatomy is superseded for this page and is owed the correction.**

**Scoped to this page and not to the component**, because the same block renders at the foot of the book note page, which Kain approved separately and did not rule on here. The two pages now differ, which is a real cost and is named rather than hidden. It belongs to `APPROVED__A_Fifth_Chrome_Sitting_The_Author_Signature_Block_S303`, the sitting this block has been waiting for.

## 6. A lead-in that lived for one version

He asked for the opening five words to be set larger in the heading face, saw it, and ruled the same sitting: **"UNDO THIS COMPLETELY PLEASE!!!!"** The function, its call and its stylesheet rule all came out together. Recorded so the idea is not proposed again as though it were new.

## 7. The course card's hero shows its whole picture now

His words: "The course card images I created last week are not fully contained within the course cards, please correct this so the full image is used, this will make the cards feel 'less busy'."

He is right and it measured. The artwork is delivered at 704 by 370, the standard set at S060. The picture box was a fixed 185px tall, which matches that shape at exactly 352px wide, the width the card was drawn at, three across the 1200px frame. On the article page the row is two cards inside the 880px column, each 428px, so 40 pixels of every course image, 18 per cent of its height, was being thrown away top and bottom.

The box now takes the artwork's own aspect ratio. **At the width the card was approved at it renders to the pixel as before**, verified on the cards sheet at 352 by 185; every other width now shows the whole picture. **This touches `cards.css` and therefore every page that renders a course card**, which is why it is filed rather than folded into the page's own note.

## 8. Both section headers, and the copy on them

**The icon box spans the two lines beside it.** His words on a screenshot: "this is completely disjointed and needs the top of the top line of text, and the bottom of the bottom line of text to align within the icon box sitting before it." Measured before: a 36px box against a 50.6px text block cannot align by any placement. The box is stretched to the row and its width written as the same sum, 50.65, with a 24px mark inside. **Above the phone only**, where the supporting line wraps and a square box would reach 90px. **Scoped to this page**, so the same header on the category hubs and listing pages still carries the small box; whether the site-wide pattern follows belongs to the section header component's own sitting.

**Both headers take new copy, written by Kain in the sitting and copied character for character:**

| Block | Title | Line beneath |
|---|---|---|
| §22.10 | `Discover Related Learning Paths` | `These two enlightening online courses expand on the ideas covered throughout this article.` |
| §22.8 | `Related Further Reading` | `Click on the links below for more reading on this fascinating topic.` |

**Both supersede DSRD 9's registered copy** and both sections are owed the correction. The §22.8 line also closes a real fault: it said "cards" after the cards had gone.

**One thing worth Chat knowing about the §22.10 line: it states a number out loud.** "These two enlightening online courses" is the only sentence on the page that does. §22.10's count is two at every width, ruled S302, so the words and the row agree today. If that count ever moves, this sentence moves with it.

## 9. The reading list's shape

His words: "change the 2 columns of four links, for three columns of three links (on desktop), two columns of three links on tablet, and 4 links only on mobile." Nine at desktop, six at tablet, four on a phone, verified at all three widths. This supersedes the two-of-four he ruled at S081 the day before.

## 10. A hairline before the closing panel, and the space above it

The hairline was asked for and built, then he caught what it exposed: "correct the space above the hairline that you just placed."

**Measured.** Every block on the page ends on its own edge, so the hairline's 48px reads as 48. This one did not: each reading link carried 10px of padding, so the block's box ran 10px past its last line of text and the white above the hairline read as 58 against 48 everywhere else. **The box was right and the ink was wrong, which is why it measured clean and looked wrong, and why only his eye caught it.** The row spacing moved from padding on each link to a grid row gap. The same 10px had also been pushing the first link away from its heading, so the header's registered 20px was reading as 30. Both corrected.

## 11. The tidy pass, and what it found still shipping

Asked for at the close: "see if there are any ways that you need to tidy up the code in this page".

- **The category pill's stylesheet rules were still live.** Kain removed the pill site-wide at S080; no template has emitted `.kh-article__pill` since, and fourteen declarations and a hover state were still being sent to every reader. Deleted.
- **The old card row's count step-down was still live**, for the same reason: the class left the markup at S081 and its rules did not.
- **The reading list carried two stacked comments** describing two different layouts, one of them superseded the same day. Collapsed into one.
- **Both deletions were proved rather than asserted.** `css_deletion_proof.py` served the before and after stylesheets to the same page in the same browser and compared every element's computed style at nine widths and both motion settings: zero differences, with the control returning zero first. The template itself has no unused variables.

---

## What DSRD 9, DSRD 8 and DSRD 7 are owed from this session

Everything the S081 file listed still stands, plus:

- **§22.1's block order**, superseded by the foot reorder in §1 above.
- **§22.7's card anatomy** for the author signature block: ground, corner and padding withdrawn on this page.
- **§22.8's card row, count and subheading copy**, all three superseded.
- **§22.10's title and subheading copy**, superseded.
- **§22.10a's closing panel**, off this page, with the back-link consequence measured in §2 above.
- **§22.4's category pill**: its stylesheet rules were still shipping and are now deleted. The pill itself went at S080.
- **DSRD 7 §5.2** is owed `list-ordered` and `share-2`, in addition to `link`, `lightbulb` and the WhatsApp glyph.
- **DSRD 8 §7** is owed the course card's hero shape, now the artwork's own ratio rather than a fixed height.
- **DSRD 9 §20.7** is owed the section header's icon box on this page, stretched rather than 36 square.

## What is still open on the build sheet, and why none of it blocks the page

- **Q2**, what Related Further Reading does with nothing to relate to. Currently hidden, which was Code's call and should not have been. Not reached this session.
- **Q5**, the source block for a course-derived article. No video-derived article exists, so nothing renders and nothing is blocked.
- **Q6**, where the source-author back link lives. See §2 above: it now has more reason to be answered, not less.
- **Q7**, whether the Author Hub page wraps this template or replaces it. **This one is about to matter**, because the 41 author biographies are being imported next.

*No em or en dashes in this file; checked before writing.*
