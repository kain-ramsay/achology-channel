**Needs from Chat: write Kain's three About rulings home (the About signed spec and DSRD 8 for the member stories strip), and note that row 2 reverses the S245 brief item 4 on About only. For the theme session. Code, S209 theme main session, 2 November 2026.**

# RULING: the About page board, three rows, all yes (Kain, in the sitting, 2 November 2026)

Kain asked Code to review the About page block by block as a senior designer. Eleven points were found; eight were dropped before reaching him because they are his own earlier rulings or are locked by 000__SIGNED_SPEC__About_Page_S390 (the closed questions in orange, S044; the card icons cropped by the tile edge, S142; the bubble mark cropped in the Thinking band; timeline text in soft grey, DSRD 7 section 1; the era colours and the small 2020 dot, which are scroll states; the block order and the closing panel, locked). The other three went to him as one board in the Change Viewer (previews/about-board-s209). His answers, written by the viewer to ANSWERS-about-page.json: yes, yes, yes. His words: "I've said yes to all three."

1. **The student count on a phone sits under the chart.** At 390 the 695,578 count covered the growth line and its labels. On phones only (under 768) it now sits under the chart inside the dark card, behind a faint rule. Tablets and computers unchanged. The number keeps the site's phone size (the gate's phone rule); the preview showed it one step larger. about.css.
2. **The question under each member video is kept for screen readers only, on About.** The poster already carries the same words. The figcaption stays in the markup. This reverses, on About only, the S245 sweep brief item 4 ("a visible text label directly beneath it"); please write that into the About spec. Testimonials and the course pages, which use the same strip, are untouched. about.css.
3. **The closing line under the videos ends on the outline button.** "To hear more members share their experiences in their own words, visit our" then the button "Member Testimonials page" to /testimonials/. The info mark and the full stop after the link go; no other word changed. The line is in the page text colour. shared-parts.php (a note that ends on one link prints that link as the button; only About passes a note) and about.css.

**Shipped:** theme 0.707.719 (the three rows), 0.707.720 (the button drops the body link's orange underline, as the Founders' Letter button does). Commits 17b91f46 and the one after it. Read back off the build site in WebKit at 1280, 834 and 390: count static and under the chart at 390 only, captions 1px wide, button present with the right address, no sideways scroll.

**Reach (Kain's S179 rule):** rows 2 and 3 could reach /testimonials/ and the course pages' member stories strip. Code puts that to Kain separately; nothing changed there.

**Fold-back owed by Code:** none; these are page details on a page whose live render is the visual record (signed spec, line 4).

The About page's four faults ask (ASK__About_Page_Four_Faults_Need_A_Brief_S203) still stands: items 1 and 2 need your brief, item 3 is recorded there as Kain's S142 exception, item 4 is your copy line.

**A fourth ruling, same sitting: "What It Is, and Who It's For" on a computer.** Kain found the block bland on desktop and asked Code to make it look better. Four options went to him in the Change Viewer (previews/about-board-s209/round-pfq.js: Answer Card, Framed Panel, Connected Questions, Dark Answer). His words: "3 Connected questions please." Built at 0.707.722 in about.css, 1024 and up only: a 2px line in brand orange at 30% runs through the five question marks (each mark on a white disc), the open answer carries a 3px brand orange rule down its left side with 24px between rule and words, and the answer's first line is set in the heading font at 21, weight 600. His S043 and S044 selector rulings (orange closed questions, circle marks, weights, the open question's wash and arrow) are unchanged. Read back in WebKit at 1280 and 1024 (changed) and 834 and 390 (unchanged), no sideways scroll. Please write it into the About spec's selector line.

**A fifth ruling, same sitting: the Achology Story, seven-row board (previews/about-board-s209/board-story.js), answers in ANSWERS-about-story.json: rows 1, 2, 3, 4, 6, 7 yes; row 5 no.** Kain asked what Code would do to improve the whole Story component. His yes on rows 1, 2 and 6 overturns the About spec's lock on the Story's scroll mechanics ("nothing about its mechanics changes"); please write that into the spec and DSRD 9 section 23. Built at 0.707.723 and 0.707.724 (about.css, about.js):
1. The four-number band follows the story: about.js lifts it out of the pinned frame into its own frame after the story (without script it stays in place); the reading window is now clamp(220px, 100vh minus 620px, 640px) on desktop and clamp(220px, 100vh minus 600px, 560px) under 1024.
2. Plays on a laptop: on screens 768 wide and up but under 960 tall, the lede steps aside, the chart takes the right 62 percent of a slimmer card, and the running count sits bottom left under the era, so the story pins instead of lying flat (pinned in WebKit at 1280 by 700).
3. Years lead: each timeline year in the heading font at 24, brand dark, in its own 96px column from 768 up.
4. Counts as badges: the four timeline counts are small pills (14, orange wash) hugging their words.
6. Jump to an era: a nav of the five era names under the stage, each in its era head's colours; clicking moves the story to that era; the era being read is ringed.
7. Phone keeps its place: under 768, a slim dark bar under the menu shows the year and era being read while the story is on screen (decorative, hidden from assistive readers).
Row 5 (the closing line as a statement with an orange button) was declined; the closing line is unchanged. Read back off the build site in WebKit at 1440 by 1200, 1440 by 900, 1280 by 700, 834 by 1050 and 390 by 760: pinned at every size from 700 tall up on 768 wide and over, flat with the bar on a phone, the jump lands on the chosen era, no sideways scroll, no script error.

**Two copy points found on the same read, yours to judge:** the founders block says Achology was "founded by Kain and Karen Ramsay in 2017" while the Story opens in 2012 and has the platform founded in 2014; and several card and timeline lines set words in capitals (FREE, FULL, LOVE, ONLINE).

OWED BACK: the three rulings written home, and a line saying so, in FROM Chat.

*No em or en dashes in this file; checked before writing.*
