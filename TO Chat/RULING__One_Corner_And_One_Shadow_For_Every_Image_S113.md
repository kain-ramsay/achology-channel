> CHAT DISPOSITION, S358 (open): STAYS. It carried no head line at the S357 close and was not counted in that close's seven, so it went undispositioned for a session; named to Kain at the S358 open. Waits on three things, all S358's document job: DSRD 7 section 5.3 gaining the fourth tier's token name and the every-image sentence; DSRD 7 section 5.4 gaining the one image shadow with the hero cover's exception; DSRD 8 sections 6.2 and 6.9 marked superseded on their radius and shadow rows. Plus one ruling owed: whether css_gate.py narrows from six radius values to the four the standard names.

# RULING: one corner radius and one shadow for every image on the site

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 113, factory session. **Date:** Sunday 13 September 2026.
**Given by Kain live in the S113 sitting**, on the rendered book note page.
**Filed under Harness Rule 14**, with its fold-back done in the same session: the book note card's build sheet is written to the new values and the component gate passes on it.
**Theme 0.389.1 is live on the build ground and every ruling below is in it.**
**Owning documents:** DSRD 7 sections 5.3 and 5.4. DSRD 8 sections 6.2 and 6.9 are superseded. Chat writes them.

---

## 1. His words, in the order he gave them

He asked first whether a standard existed:

> "Do you have a defined site wide corner radius standard - because i think we need one!"

Told what was actually there, he ruled:

> "yes, sweep them all onto the standard please!"

Then, on the seventeen values no tier named:

> "bring them onto the 4 standard sizes please"

Then, looking at the rendered book note:

> "the corner radius's just need to be the same accross all images - look at the book image, then the author image on a book note page, have two images with different corner raduses looks silly!"

And then, on being asked nothing, he widened it himself:

> "So, why wouldn't you just be an expert AIO and apply a rule to all image radius corners? Maybe, at the same time, you could also apply a site wide standard to shadow background on images too? Are you capable of decising what this must be?"

## 2. What was actually there, measured before anything moved

**A standard existed in three places and they disagreed.** DSRD 7 section 5.3 names four tiers: cards 12, buttons 10, inputs 10, stage panels 16. `base.css` held three tokens and no name at all for the 16. `css_gate.py` allowed six values, two of which no specification names.

**And the theme kept none of them.** Of about 156 rounded corners, 47 read a token, 36 typed the exact number a token already held, and around 20 used a size no tier names.

**One book had four corners.** The same cover drew at 4 in the hero band, 12 in the column beside the writing on the same page, 3 on a card and 2 on a mini thumbnail.

**Five pictures had five shadows.** The hero cover at 0 32px 64px black 48 per cent, the card's cover at 4px 4px 16px black 30, the thumbnail at 2px 2px 8px black 30, the quote page's cover at a two layer brand dark pair, and the instructor portrait at one brand dark layer. Three of the five were pure black, on a site whose palette holds no black, which is the reason DSRD 7 section 5.4 itself gives for settling the lightbox shadow on brand dark.

## 3. What was done

1. `--radius-panel` added: the fourth tier's first name. It had been typed as a number everywhere it was used and could never move with the rest.
2. **43 corners** swapped a typed number for the token holding that same number. Nothing a reader sees changed, which was the point.
3. **11 further corners** moved onto a tier, chosen by what the thing is and never by which number was nearest: controls to the button tier, artwork inside a card to the card tier, the lightbox to the panel tier. This one does change what a reader sees: the Knowledge Hub's tags and pills and the course page's tabs were half again as round as anything else on the site.
4. **Every image** now reads `--radius-card`. `--bn-cover-radius` is retired with its reason left at its name.
5. **`--shadow-image` added, and its value is not invented.** It is the quote page source cover's own pair, which Kain approved on a render at S108, promoted from one page to every picture. Nothing was designed; one approved thing stopped being local.
6. The column portrait gains the shadow it never had, so a cover no longer loses its weight when it reappears beside the writing.

## 4. The one exception, and it is not an oversight

**The hero book cover keeps `--shadow-cover`, pure black at 48 per cent.** It sits on a dark photograph, where brand dark at 8 and 14 per cent disappears. `base.css` already carried that reason, written when the exception was first made. Applying the standard there would have deleted the shadow rather than standardised it, which is the opposite of what Kain asked for. Named to him in the sitting rather than left to be found.

**Six corners were also left.** Three are focus rings, and section 5.3 says in its own words that the tiers "govern surfaces"; section 5.1 already records that a ring radius "never had a rule to follow". Three are values Kain ruled himself on a render and are not Code's to overturn.

## 5. What Chat is owed

**DSRD 7 section 5.3** gains `--radius-panel` as the fourth tier's token name, and a sentence saying every image takes the card tier.

**DSRD 7 section 5.4** gains `--shadow-image` as the one image shadow, with the hero cover's black named as its single exception and the reason kept.

**DSRD 8 sections 6.2 and 6.9 are superseded** on their radius and shadow rows by Kain's ruling above. The book note card's build sheet is already written to the new values, with his words in the row, so the sheet and the code agree today; the DSRD does not yet.

**`css_gate.py` allows six radius values where the standard names four.** Changing what a gate checks is Chat's commission and never Code's idea, so it is named rather than changed. Today it would pass a 4 and a 20 that nothing in the theme uses any more.

## 6. Three build sheet rows found while this ran, and not touched

The completion gate surfaced three course card rows whose sheet is stale against accessibility rulings the theme does carry: two mid greys that fail AA and were moved to soft grey by the 2026-07-13 contrast audit, and the Enrol button's fill, moved to the AA-safe orange at Kain's S096. They are written into `component_gate_waivers.md` naming what they wait on. Not corrected here: Rule 4's chain runs prototype, sheet, code, and a sheet corrected to match code is a ruling being carried home rather than something Code does unasked.

OWED BACK: DSRD 7 sections 5.3 and 5.4 written to section 5; a ruling on whether `css_gate.py` narrows to the four; and the course card sheet folded to the contrast audit.

*No em or en dashes in this file; checked before writing.*
