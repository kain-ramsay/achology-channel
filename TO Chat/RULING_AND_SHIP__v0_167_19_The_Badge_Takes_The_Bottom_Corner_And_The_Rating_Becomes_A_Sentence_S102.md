> **CHAT DISPOSITION, S343: ARCHIVED.** The desktop badge position, the 42ch standfirst cap and the 152 button clearance are written into DSRD 9 section 32.3; the stars ruling into section 32.9 item 1. The three per-step sentences it introduced were replaced two ships later by Kain's one fixed sentence (v0.167.21). Card: Book note page template second look.

# RULING AND SHIP: v0.167.19 and v0.167.20, Kain keeps the badge, moves it to the bottom right corner, and the rating becomes the standfirst's last sentence

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, on the rendered page after v0.167.18, spoken and transcribed.
**His words, quoted exactly as transcribed:** *"Yes, Claude. Um, I think we can keep the badge as it is. Uh, we could... I I think what we need to do with this is we need to just change its location from the from the top. It's currently aligned with the top of the container. I just think we need to move it right down to the bottom. Into the bottom right hand corner, if that makes sense. That way, it's not going to, uh, cross out the the title. Um, and in response to the essential reading text with the three text, I I think we could actually just remove the text completely and and instead just add the sentence, essential reading for all oncology members, something like that. And then Yeah. I think I think that'll do us, actually. Could you give that a go please? Thanks."* ("text" and "oncology" are the transcriber's hearing of ticks and Achology.)
**Answers:** the two questions put to him in `RULING_AND_SHIP__v0_167_18_The_Essential_Reading_Badge_In_The_Book_Note_Hero_S102.md`: the badge stays as it is, five stars included; the standfirst's "Essential Reading" clause and its ticks go, replaced by his sentence.
**Filed under Harness Rule 14.** Theme commits `17940ed` (v0.167.19) and `841ce37` (v0.167.20, a four-minute correction, section 4).
**Board card:** Knowledge Hub page designs.

## 1. The badge is kept, and moves to the bottom right corner

The badge file, size and condition are as at v0.167.18 (his 1080 square PNG through the pipeline at the square slot, 128 and 256, only for `essential-reading`, alt empty). What changed is its anchor: `bottom: 0` of the hero grid instead of `top`, so its foot sits on the grid's foot (the cover's foot wherever the cover is the taller column) and its right edge on the container's right edge. The overline, the title and the author line are above its head again and run the full column, so the desktop title clearance of v0.167.18 is deleted and the title wraps as it did before the badge. What now shares the badge's height is the foot of the standfirst and the button row, so on a badged desktop page the standfirst is capped at 42ch (its 46ch right edge would have run 10px under the badge) and the button row keeps 152px clear, wrapping a second button onto a row of its own where a note has two.

Below 1024 the stack sits under the cover and the badge, 96, stands in the free ground to the right of the button row, which the 46ch standfirst never reaches at that width, so both clearances are lifted there. On a phone the bottom corner is where the standfirst's full-width lines run, so the badge goes back up beside the cover's top at 88, in the ground the 256 cover leaves; this is the one width where "bottom right" is not followed literally, and it is named here for his eye rather than decided quietly.

**Measured on the deployed page.** At 1440: badge 128 at x 1032 to 1160, y 429 to 557, its foot on the cover's foot (557); title two lines again; standfirst four lines ending at x 995, 37 clear of the badge; the button's right edge 834. At 768: badge 96 at x 640 to 736, foot on the button row's foot (945); standfirst 442 wide ending at x 450; button right edge 266. At 390: badge 88 beside the cover's top, 6px clear of it. No horizontal overflow at any width. Badge loaded and read at its natural size.

## 2. The rating is a sentence at the end of the standfirst, and the ticks leave the page

The "Essential Reading" clause and its three ticks (v0.167.17) are gone. The standfirst now ends with a sentence in its own type and colour, one written sentence per step of the scale, so the fifty-seven live notes that are not Essential Reading keep a rating on the page (tonight: 8 Essential Reading, 36 Highly Recommended, 21 Recommended):

| Rating | Sentence |
|---|---|
| essential-reading | Essential reading for all Achology members. |
| highly-recommended | Highly recommended reading for all Achology members. |
| recommended | Recommended reading for all Achology members. |

The first is his sentence; the other two take its shape, named to him as the reading of his words and his to overturn. Read on the deployed pages: `a-guide-to-rational-living` ends "...building lasting emotional resilience. Essential reading for all Achology members." under its badge; `what-do-you-say-after-you-say-hello` ends "...think, feel and behave. Highly recommended reading for all Achology members." with no badge and its standfirst at the full 46ch.

Deleted with the ticks: the `.bn-hero__ticks` rules (the 12px Check at stroke 2.5) and the `.bn-hero__rating` span rule; the template no longer draws `achology_icon( 'check' )` anywhere. The S050 question of whether Recommended shows one tick or three closes for want of ticks. The Check glyph's DSRD 7 section 5.2 registration question now concerns the registry alone, not this page.

## 3. Shipped

v0.167.19 and v0.167.20, `deploy.py` three proofs on each: server identical to local, zip 700 files matching the theme, server reporting the version. Both commits pushed. Each opened in Safari for Kain as a new tab. **His eye on the finished corner is not yet given:** his word was the instruction; this file records the ship.

## 4. A correction inside four minutes, on the record

v0.167.19 built the sentence from the scale's words, and the top step's words already contain "Reading", so the live page read "Essential reading reading for all Achology members." for about four minutes, and Kain's Safari tab of that minute shows it. v0.167.20 writes the three sentences out in full. Caught by reading the rendered text back after the deploy, which is the check that exists for this.

## 5. Owed to the documents

DSRD 9 section 32.3's hero table: a badge row (bottom right of the grid, 128/96/88 by width, Essential Reading only, alt empty, the 42ch cap and the button row's clearance on a badged desktop page) and the standfirst row's new last sentence. Section 32.9 item 1: "in the editorial scale's own words and never as stars" is superseded in its stars half by his word on the badge, and its `Achology rating · {value}` form by the sentence table above; the words half stands. Yours, on this file and the v0.167.18 one.

OWED BACK: the section 32.3 rows and the section 32.9 item 1 rewording, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
