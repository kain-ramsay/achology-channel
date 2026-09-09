> **DISPOSITION, Chat S355:** acted on. All eight rulings written home. The two-zone structure, the deleted repeat blockquote, the audio becoming the article, the share row moving into zone one, and the new caption and standfirst components are all in DSRD 2 section 1.1, rebuilt whole. The DSRD 7 section 4.3 exception is recorded as exception 4, with the button-versus-line finding kept in full. The DSRD 9 meta line exception is recorded under section 22.4. Declan Fitzpatrick reading the whole Knowledge Hub is recorded at DSRD 2 section 2.24 item 5. The listen bar has a component registry row, with its class prefixes marked for Code to confirm. The adjacent-sibling finding is carried to Code rather than written into a specification. No board card moved. Archived S355.

# RULING: the quote page becomes two zones, and seven more rulings with it

**DOCUMENT TYPE:** ruling, from Claude Code, Session 108, theme session. **Date:** 9 September 2026.
**Follows:** `RULING__The_Quote_Card_Is_Settled_S108.md` and `RULING__The_Quote_Page_Carries_The_Course_Slot_S108.md`, both filed earlier the same day.
**Board cards:** Quote page template; 50 instructor book quote pages.
**Read this cold.**

---

## 1. Why this file is long

Kain designed the top of the quote page with me across one sitting, and he was explicit about why it was worth the time: the answer gets multiplied by tens of thousands of quotes. Eight rulings came out of it. Three of them change what a DSRD says.

Every one was given on a rendered page or on baked files, never on a description.

## 2. The structural ruling, which the rest hang off

**The page is two zones.** His words: *"this kind of top, very top segment of the page just needs to be the quote. The quote within the page with all of its sharing options... I think the main page title, with the date and the author and all that, needs to be moved down so that the article is a separate section."*

Zone one is the quote: the card, its share controls, and nothing else. Zone two is the article: the title, the standfirst, the meta strip, the interpretations and the foot. The listen bar is the boundary between them.

**What started it.** The top of the page said the same sentence twice, once on the card and again written out beneath it. Both were specified, DSRD 2 §1.1 items 2 and 3, so it was not a mistake. It was still wrong on the rendered page, and it is exactly the class of fault only a render shows. Kain's word for it was "stutter".

## 3. The three rulings that change a DSRD

**3.1 DSRD 2 §1.1 item 4 is overturned. The audio is the article, not the quote.** The section reads *"single clip, one control (Listen/Pause/Resume), no timings file, the unit is seconds long"*. Kain: *"listen to this quote needs to be listen to this quote ARTICLE, because we want the quote article to be run through RunPod, not the quote within itself."* The reason is worth keeping with the ruling: a fifteen second clip does not earn a control on a page, and the interpretations are the part anybody would want read to them. The button reads "Listen to this quote article".

**3.2 DSRD 2 §1.1 item 3 is deleted for this page. The quote is not written out a second time.** With the quote given its own zone at the top, that block had no work left to do.

**3.3 DSRD 7 §4.3 gains a registered exception on this page, and this one is worth reading in full because the finding is general.**

Kain: *"it just looks a little bit crammed and unbalanced... the listen to this article line is just a little bit cramped too neatly in between the quote image and then the article."*

He was right and so was the number, and they were measuring different things. Section 4.3 measures 48 to the LINE, and the bar delivered exactly that. But the object an eye sees is the BUTTON sitting on that line, which is 37px tall and eats 18px out of the gap from each side. Measured before: 48 to the line, 30 to the button.

Thirty is fine on a help answer, where the bar's neighbours are a page header and body text. It is not fine between a 1200 by 630 card and a 33px title. **The rule did not change; what changed is what stands either side of it, and a rule written for one context met a second one.**

The bar now takes 48 of margin on this page instead of 28: the button gets 50 of clear air and the line sits at 68. Kain accepted the trade on the render. **Section 4.3 wants this recorded as a named exception**, in the same way the About story block and the About header hairline already are.

## 4. The five other rulings

**4.1 The share controls.** Settled across three rounds of options, each shown one at a time in the identical screen position. Where: on the card, *"On the card wins"*. Which corner: bottom right, *"that's definitely what I want"*. How: joined into one object carrying words, *"3. Joined words"*. Three controls, every one a verb: Download, Share, Copy.

This closes **DSRD 2 §1.1 item 12**, which has asked for a share row since the beginning and which no page on this site has ever carried. **It moves up to zone one, beside the thing being shared, rather than sitting at the foot where §1.1 lists it.**

Two things behind the design, both from research done this session rather than from taste. Only two mobile visitors in a thousand ever tap a custom share button, **but they are twenty times more likely to when they arrived from a social network**, which is precisely what a quote page is for. And more than three controls lowers the interaction rate, while a control carrying a verb beats a bare logo.

**Instagram is the download.** Instagram has no share-a-link route from the web, so the only way anybody posts one of these is to take the picture and upload it.

**4.2 Declan Fitzpatrick reads the whole Knowledge Hub.** *"We only want one single voice for the whole Knowledge Hub, which leads me to think, it might as well be Read by Declan Fitzpatrick. There's no reason to change this at all."* The persona fronting all 250 help answers now fronts the Hub. One name, one photograph, whatever the piece and whoever wrote it. **DSRD 2 §2.24 item 3a's attribution rule now reaches beyond /help/.**

**4.3 The author leaves the meta strip on a quote page, and only on a quote page.** *"So that names aren't competing with names, we just move Frederick's name out of the article info bar and just leave his name in the article author card underneath the article."* The quote page is the one page carrying two names within a few lines: "Read by Declan Fitzpatrick" sits directly above that strip. The writer is still credited in the signature card at the foot. **DSRD 9's meta line wants this exception recorded**, since the article page keeps its author and has no clash to resolve.

**4.4 The standfirst moves into the article zone**, under the title and above the meta strip. *"I am questioning its placement. Currently I feel it is taking away from the quote card."* He is right for a better reason than the one he gave: the sentence describes the article, not the picture. It was only a caption because when he first ruled it down the page, the title still sat above the card. **DSRD 2 §1.1 has no standfirst component and now needs one.**

**4.5 The course slot stays**, filed separately this morning.

## 5. Two things worth having beyond this page

**5.1 The listen control is now a shared component and is not in the component register.** It was moved out of the help pages into `components.css` and `listen.js` at Kain's word, rather than copied. He asked whether it becomes "another one of our design tokens"; it becomes a component rather than a token, and **the register is Chat's and Kain's to write, not Code's**. It wants a row.

**5.2 An adjacent-sibling selector is a silent trap, and it cost a visible defect today.** The article page gets the gap under its meta strip from `.kh-article__meta--body + p`, which assumes a paragraph follows the strip. On the quote page a wrapper follows it instead, so the selector never matched and the gap measured exactly zero: the first sentence ran into the date line. Nothing errored and nothing warned. **Kain caught it by eye.** Worth knowing wherever a second page adopts a first page's block.

---

OWED BACK: the section 4.3 exception recorded; the three DSRD 2 section 1.1 corrections (items 3, 4 and 12, plus a standfirst component); the DSRD 9 meta line exception; section 2.24 item 3a widened to the Knowledge Hub; and a component register row for the listen bar.

*No em or en dashes in this file; checked before writing.*
