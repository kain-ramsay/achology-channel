**For Chat. What this needs from you:** write Kain's two rulings below into their homes: DSRD 8 section 18.10 (the Courses dropdown's names and their look) and section 18.15 (the phone menu's Courses list), and DSRD 5 (the one place a school's full name may be shortened).

# RULING: the school names in the Courses menu, Quiet Lead-In with Kain's short topics (Code, S194 theme menu review side session, 28 October 2026)

## Ruling 1, the look: Quiet Lead-In (option 3 of four)
Shown in the one shared Change Viewer on the build site's Courses and Knowledge Hub pages, computer and phone. The four: Plain Full Name, Even Fold (Code's recommendation), Quiet Lead-In, Small Capitals. Kain's words: "we definitely need the quiet lead-in. Evenfold is just making the block way too busy."

What it is: "The School of" sits on its own line above the topic, in the same typeface and size as the name, regular weight, soft grey; the topic sits under it in the name's usual weight and colour. In the phone menu the same lead line sits one step smaller.

## Ruling 1 REPLACED the same day: Topic Alone (round 2, option 1 of four)
Kain saw the Quiet Lead-In built and asked: "Take The School of out of the menu altogether and show me that first." Four options shown in the Change Viewer, each without the lead line: Topic Alone (Code's recommendation), Orange Topic, Softer Topic, More Air. Kain's words: "Yes, option 1 Topic Alone. Build it."

What it is now: each school is shown by its topic alone, in the name's usual weight and colour, with no "The School of" anywhere in the Courses mega menu or the phone menu's Courses list. Everything else in the card is as signed. Built at 0.707.660 (commit 4273c28d); the Quiet Lead-In of 0.707.659 is gone, and both lead-line style rules are removed from header.css.

## Ruling 2, the words: the menu may shorten a school's full name
Kain's words: "we need to be flexible with our school canonical name rules as well, because what I don't want to see is especially in the mega menu, a school name rolling over into two lines. We need this to be really tidy. So this will be the area on the website where we break our own canonical name terms everywhere, because it's important that a brand new visitor to the website is just going to click on the general topic that they're interested in."

Kain gave the four short topics himself, word for word:
- Mental Health & Emotional Resilience
- Person-Centred Counselling & Psychology
- Life Coaching & Professional Helping
- Mindfulness, Applied Insight & Wisdom

The other three keep their full topic: Neuro-Linguistic Programming, Personal Growth and Development, Cognitive Behavioural Psychology. Every one reads "The School of" above it, in the computer mega menu and the phone menu alike.

## Built
Theme 0.707.659 (commit fa78fa0a), deployed from a clean copy; local, server and zip agree. header.php (the seven names in both menus), header.css (two rules, `.navcard__lead` and `.mobile-nav__lead`). Read back on the build site in WebKit: every topic sits on one line at 1120 and wider (Kain's 1268 included) and on phones from 390 to 834.

## Still open, and coming next in this session
On small laptops, 960 to 1119 wide, the grid column is too narrow and two to four topics still take two lines; at 320 Person-Centred does. No word change fixes that: Kain agreed it comes next as its own four-option round. The fold-back (Header + Footer prototype v4 and the data file) is written once after that round, since it changes the same block.

OWED BACK: DSRD 8 s18.10 and s18.15 and DSRD 5 carry both rulings; no reply needed beyond that.

*No em or en dashes in this file; checked before writing.*
