**DISPOSITIONED S306: read in full. Superseded by S082's rulings (the page is now signed) and the Harness-rule request is closed (Version 3.5, Rule 3 tightened). Historical record, no further action. Board card: Knowledge Hub Page Designs.**

# RULINGS: everything Kain settled on the article page at S081

**From:** Claude Code, Session 81. **Date:** 24 August 2026.
**Authority:** Kain, in the sitting, on rendered pages in Safari, one variable at a time.
**Shipped:** theme v0.85.0 through v0.93.2, each deployed and verified.
**Board card:** Knowledge Hub Page Designs, line 1.
**Reads with:** `RULING__The_Article_Reading_Column_Is_Centred_S081.md`, filed earlier the same session and not repeated here.

**The page is NOT signed.** It is close, and Kain stopped the session to preserve context rather than because it was finished. What is below is settled; what is still open is at the foot.

---

## 1. The reading column, and the trail with it

Filed separately at `RULING__The_Article_Reading_Column_Is_Centred_S081.md`. DSRD 9 §22.3 and §27 are owed the correction recorded there.

## 2. The opening paragraph runs one step larger

The article's first paragraph takes the 18 step against the body's 16. Ruled on a tabbed render at one step up and two. It is selected as the body's first paragraph rather than by a class, so nothing has to be remembered when an article is written.

## 3. A heading that folds is split about 65/35

His words: "when a sentence carries over onto a second line, the whole sentance gets split 60/40-ish, 60-70% of the heading on the above line, and 30/40% on the beneath line", then "apply this to every heading that folds", then the contents card's section names as well.

**This SUPERSEDES a ruling he gave hours earlier the same session**, that titles should split evenly. `text-wrap: balance` shipped at v0.88.1 and came out at v0.91.0: balance aims for equal lines and this is deliberately unequal. No browser can express a ratio, so it is measured in `knowledge-hub.js`.

## 4. The bubble watermark, and where it may sit

The motif reaches every article page. **Not the arrangement the Help pages use**: no mark sits behind the title, because this page puts an 880 by 420 photograph under it and the bubble read as a mark on the image. The three run down the article BODY, hosted on that element so their positions are proportions of the writing. His condition, and the reason it is built that way: "so long as the bubbles are somehow baked into only the article body, and not by the specific measurement of one article, as all artcles will be different lengths." Recorded at components.css §3a.

## 5. The contents and share block

New. Approved across the sitting: an off-white card floated at 40%, then 36%, of the reading column with the text wrapping it; the numbers inline with the titles; the headings at the 21 step and the section names at 14; a hairline before Share this Article in a colour that can actually be seen; six share controls filling the row; and finally moved to the LEFT of the column with the DSRD 7 §4.4 outdent, Share this Article down to the 18 step, and the icons at 32px.

**One thing he rejected that had shipped:** a light orange ground behind the share half. He had asked to try it, did not rule on it, and moved on; that was read as approval and it was not one. His words: "I didnt approve this ... Fully grey background with the hairline we can see."

## 6. The DiMAP advert

New. A brand dark card at 45% of the column, floated right, breaking the column edge under §4.4, its top level with the third SECTION's heading. His copy, unedited. The whole card is the link. On hover the bulb behind it lights, the course name gains a weight, and the arrow arrives.

## 7. The top of the page is one rectangle of three parts

The headline across the full width, then the picture and the contents card sharing the row beneath. **DSRD 9 §22.5 is superseded**: the picture is no longer 880 wide and 420 tall. Measured: the block was 1005px and is now 548px.

---

## What DSRD 2 and DSRD 9 are owed

- **§22.1's block order** does not include the contents block, the DiMAP card, or the top grid.
- **§22.2's silence on horizontal position**, closed by the centring ruling filed separately.
- **§22.4's mid grey meta line**: it fails the contrast bar and moved to the soft grey.
- **§22.5's featured image**: superseded whole by the top grid.
- **§22.6, §22.7 and §22.9's 17px, 13px and 17px** are not steps on the nine-step scale; the theme renders 16, 12 and 16.
- **§22.8's three-card row**: see the open items below.
- **DSRD 2 §1.5** carries neither new block.
- **DSRD 7 §5.2** is owed three marks used and not registered: `link`, `lightbulb`, and the WhatsApp brand glyph.
- **DSRD 7 §12.2 set 8 and DSRD 8 §24.2** both say no Know Your Psychology SVG exists and nothing can ship from that set. All seven lockups are on disk as PNG, @3x PNG, SVG and WebP, dated 18 August. Both rows are stale.

## What is still open, for the next sitting

1. **Related Further Reading at three cards.** Measured: at three, every one of the real titles is truncated; at two, none is. §22.8's own stated reason for three is that it avoids exactly that. Put to Kain, not yet ruled.
2. **The reordered foot**, rendered and liked but not built: courses, hairline, the related reading as two columns of four plain names, then the enquiries panel. Its cost is that the Where next panel carries the source-author back link DSRD 1 §6 requires, and the enquiries panel does not.
3. **Q2, Q5, Q6 and Q7** on the page's build sheet, unchanged.
4. **The generic Know Your Psychology lockup** has never been exported, and the brain-and-constellation artwork in his mockup does not exist anywhere in our assets.

## One thing owed back to Chat

`RULING__List_Derived_Artefacts_Before_Any_Bulk_Replacement_S305` asks Code to add the rule to `000__THE_HARNESS.md`. **Harness Rule 8 says "Code never edits this document", and CLAUDE.md repeats it.** The rule itself is right and is being followed; where it is written needs settling by someone who can edit that file.

*No em or en dashes in this file; checked before writing.*
