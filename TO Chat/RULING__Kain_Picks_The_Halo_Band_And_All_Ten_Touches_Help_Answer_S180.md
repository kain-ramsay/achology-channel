**For Chat. What this needs from you:** write Kain's S180 Help answer ruling home: rewrite DSRD 1 section 8.2b (the category picture no longer sits in the answer; it ends the Halo band beside the title), add the Help answer page's layout to DSRD 9's help section, confirm or replace the enquiry line's words, and rule on the two gate exceptions below. Answers BRIEF__One_Sitting_With_Kain_On_The_Help_Answer_Pages_Look_And_Feel_S445 (its OWED BACK).

# RULING: Kain picks the Halo band and all ten touches for the Help answer page (Code, S180 Help answer side session, 26 October 2026)

## Kain's words
"F2 Halo. Can we go with that, please? And then, yeah, I think all of the touches are absolutely great." Earlier in the sitting, on the picture in the answer: it "looks absolutely terrible ... it looks dumped on the page", and on the band he wanted: the picture "is larger than the band. It literally exists outside of the band", and the band "cannot come beyond it".

## What shipped, and where
Live on the build site at theme **0.707.531** (built at 0.707.530; 0.707.531 moved the enquiry line into the vote strip). Commits f6da9822 and ee1cb9ab. Rendered: /help/achology-basics-and-identity/what-is-achology/
1. **The Halo band.** A slim slate band holds the title in white; the category picture, 216 round with a white keyline, is bigger than the band, sits on top of it and ends it: the slate stops at the picture's centre and no slate shows beyond it. Faint white rings spread from the picture across the slate. The band bleeds 32 left so the title sits on the answer's edge (DSRD 7 section 4.4); the picture's outer edge is the answer's right edge. On a phone the band runs edge to edge and the picture sits on its top edge, half above. The picture is lifted out of the rendered answer by the template; every answer's editor content keeps it, so no answer was edited and Rank Math still reads it.
2. **All ten touches:** 1 Reading Line, 2 Picture Arrives, 3 Answer Unfolds, 4 Living Links, 5 Orange List Dots, 6 Listen Glow, 7 Thumbs Answer Back, 8 Questions You Feel, 9 Questions Arrive, 10 Enquiry Line. All stop for readers who ask for less motion.

## Later the same sitting: the facts move into the band, and Listen comes off (live at 0.707.532)
Kain asked how the band carries two and three line titles, and why the line under it looked unbalanced. Measured on all 302 published answers at the band's own width: on a computer 258 take two lines, 32 three, 12 one; three is the most on a computer or tablet, four on a phone. His K10 (S422) had already taken the Listen control off every Help answer before launch; the quote pages carried it out at 0.707.234 and these pages never had. Shown both ways on real one, two and three line answers, he ruled: "Yes, put the facts inside the band and take Listen off." Commit d5d8d202.
- The date, word count and reading time sit in the band under the title, as on the quote and article pages; the reading bar, its hairline and the Listen control are gone. Touch 6, Listen Glow, retires with the control (nine touches stand).
- The band's floor is 152, so a one-line title takes the two-line band and the picture stays 32 clear of the answer.
- Declined: the facts on their own line under the band.
- **This closes the S422 ruling's Help half** (RULING__Listen_Bar_Off_And_The_Content_Packs_Hold_S422, its OWED BACK: "one line in TO Chat when the listen bar is gone at three widths"): gone at 1280, 834 and 390 on three answers (verify.py, no_listen true at every width). The recordings stay in the uploads folder for the Post-Launch card.
- page_gate on a two-line answer at 0.707.532 adds one line this change made: hairline-present at the band to the answer (48, 32 on a phone). The gate carves out a card that draws its own border as its own boundary, held to the same 48 outside it; a filled band is the same case and the gate does not yet know it. An instrument line for the factory session, not a page fault.

## For the specifications
- **DSRD 1 section 8.2b** is overturned in its place and size: the picture no longer opens the answer at 200 / 130 (240 / 156 since S110); it ends the Halo band at 216, 96 on a phone. The file set and the one-picture-per-category rule are unchanged.
- **DSRD 9:** the page's layout is in the design folder's new build sheet, BUILD_SHEET__help-answer-page.md, matched by PROTOTYPE__Help_Answer_Page_S180.html (Help Design Prototypes, FAQ Article Page folder). That is the fold-back under Harness Rule 14.
- **The enquiry line's words** are the main session's recommendation as Kain saw them: "Can't find your answer? Send us an enquiry", linking to /enquiries/. Confirm or replace them; Code changes the words in one line of the template.

## Proof
WebKit at 1280, 834 and 390 on two answers, each with its own title and with the longest of the 375 real titles: the title on the answer's edge, the picture full size on the right edge, no slate past the picture at 1280 and 834 (on a phone the full-width band is by design), the picture gone from the answer, the enquiry line present, no script errors (theme previews/help-answer-s180/verify.py and band_end.py). css_gate passes on help.css; the template lints clean on the server's PHP.

## page_gate on what-is-achology, 0.707.531: 51 passed, 20 failed
**Two exceptions this ruling makes, for Chat to record or rule against:**
- breadcrumb-below (all three widths): the crumbs to the title are now 112 (24 to the band, then the band's own air), against the site-wide 48 (Kain, S080). The title sits inside the band he picked, so the 48 cannot be kept without the picture covering the crumbs.
- spacing-scale: the band's 56 above (the header carried the same 56 before; it is what lets the picture rise 52 and stay clear of the crumbs).

**Already failing before today, untouched by this work:** the related questions card's spacing (boundary 6, 24 against 48; on a phone the vote strip to the card, 80 against 32), the body to the vote strip with no hairline (32), the phone's listen line to the body (24 above, 48 below), a heading's 18 gap (now named help-rise because touch 3 adds that class to every answer part; flagged to Chat at S142), the body paragraph owning boundary 4, the WCAG acronym, keyword density 0.19 per cent, the orphan crawl, the picture's missing srcset, and the record's own lines.

## Declined or set aside, so nothing is put to Kain twice
- Picture places A Beside the Title, B Before the Title, C Above the Title.
- Bands D1 Warm Band, D2 Picture Leads, D3 Slate Band, D4 Picture Fills the End, D5 Picture Ends the Band, D6 Designed Whole.
- E1 to E5 (the picture bigger than the band, the band running past it; Kain refused the band passing the picture).
- F1 Medallion, F3 Sunrise, F4 Slate Ring, F5 Two Layers.
- Three whole-page directions (Editorial, Charcoal Masthead, Warm Paper) drafted from a design brief Kain pasted mid-sitting; never shown, set aside by his pick. That brief also asked whether the word count earns its place on the reading line; it is unchanged and the question is open.

## Found, not a design matter
On what-is-achology the first related question carries no one-line excerpt while the other three do; that is the linked answer's own excerpt field.

*No em or en dashes in this file; checked before writing.*
