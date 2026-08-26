CHAT DISPOSITION, S310: read. Waits on one Kain decision: achologytest.com added to the embed whitelist on all fourteen (Code by API, or Karen). Put to Kain at the S311 open.

# DELIVERY: the fourteen banked testimonial videos, and one thing that stops the block working

**From:** Claude Code, Session 84. **Date:** 25 August 2026.
**Answers:** `ASK__The_Facts_Only_The_Install_Holds_S308_Board_Audit.md` section 2, under Kain's S308 authorisation.
**Read only on Vimeo, as authorised.** Nothing on the account was changed, and the block is not built.

---

## 1. The fourteen rows

Pulled through the Vimeo API from folder `20119371` on user `71102328` at 21:44Z on 25 August 2026. Vimeo reports the folder holds exactly 14, which matches. Titles are copied exactly as they sit on Vimeo, including their leading number and their missing apostrophes.

| # | Title on Vimeo | ID | URL | Duration |
|---|---|---|---|---|
| 1 | 1 What are the top personal benefits of regular Achology attendance | 889569815 | https://vimeo.com/889569815 | 7:14 |
| 2 | 2 What value have you found in regular VALTS attendance | 889575310 | https://vimeo.com/889575310 | 4:54 |
| 3 | 3 What have you learned from regularly engaging in PALS | 889577533 | https://vimeo.com/889577533 | 5:07 |
| 4 | 4 What are your key lessons that you've learned from regularly engaging in CIPS | 889579778 | https://vimeo.com/889579778 | 5:15 |
| 5 | 5 What role does self-awareness play in personal growth | 889581973 | https://vimeo.com/889581973 | 5:56 |
| 6 | 6 What impact does self-discipline have on coaching | 889584468 | https://vimeo.com/889584468 | 4:56 |
| 7 | 7 What is the one lesson that stands out as the most impactful for you | 889586499 | https://vimeo.com/889586499 | 5:35 |
| 8 | 8 What is your favourite Achology course & why | 889588879 | https://vimeo.com/889588879 | 5:17 |
| 9 | 9 What are your top 3 tips for brand new Achology members | 889591164 | https://vimeo.com/889591164 | 7:00 |
| 10 | 10 What happens if you disagree with something that's taught in the course | 889594475 | https://vimeo.com/889594475 | 5:52 |
| 11 | 11 What role does 'getting over yourself' play in personal growth | 889617801 | https://vimeo.com/889617801 | 5:17 |
| 12 | 12 What key factors would hinder a persons capacity to grow | 889619981 | https://vimeo.com/889619981 | 7:53 |
| 13 | 13 What are the main benefits of understanding different cultural perspectives | 889623105 | https://vimeo.com/889623105 | 5:00 |
| 14 | 14 What decision have you made this year that equated to growth | 889625291 | https://vimeo.com/889625291 | 5:33 |

Fourteen videos, 80 minutes 49 seconds in total. All were uploaded on 29 November 2023.

## 2. Three things the list itself says, which the spec will need

**The titles carry the QUESTION, never the member's name.** The ASK describes these as "one member answering one question each", and that is presumably true of the footage, but the account does not record who is in which video and the description field is empty on all fourteen. **So the spec cannot name the speakers from this list.** Whoever knows who answered which question has to supply it, or the block runs unattributed, which would be a first for this site.

**They are questions this site has not asked before.** Not one of these fourteen matches the five questions already on the Member Testimonials page. So this is a second, larger question set rather than more answers to the existing five, and the block's shape is a decision rather than a repeat of the existing grid.

**Two of the fourteen carry copy faults in the title:** "a persons capacity" (number 12) is missing its apostrophe, and "that's taught" (number 10) and "getting over yourself" (number 11) use straight quotes rather than the curly entities the site uses everywhere. If the titles become visible copy, they are Kain's to rewrite rather than mine to tidy.

## 3. THE THING THAT WOULD HAVE BROKEN THE BLOCK SILENTLY

**All fourteen are set to `privacy.view: disable` and `privacy.embed: whitelist`.** Disabled means they cannot be watched on vimeo.com at all. Whitelist means they play only in a page served from a named domain.

**The whitelist on these videos, read today, is:** `achology.com`, `cdn.iframe.ly`, `bettermode.io`, `achology.circle.so`, `kaintamsay.com`.

**`achologytest.com` is not on it.** So the block would be built, would pass every gate this project owns, would look correct in the markup, and would show fourteen dead players on the build site. Nothing in our machinery reads a Vimeo privacy setting, so nothing would have caught it.

**What is needed, and it is not mine to do:** `achologytest.com` added to the embed whitelist on all fourteen, which is an account change and therefore Kain's or Karen's. I have not made it. Say the word through the channel and I will make it as a single API pass and read it back, or Karen does it in the Vimeo interface, whichever Kain prefers.

**One more for the cutover list:** `kaintamsay.com` on that whitelist is a misspelling of kainramsay.com and is doing nothing. Noted, not touched.

## 4. The count question: the install says 45 from nine, and the old card is stale

Read from the theme this session, not from recall.

`page-testimonials.php` renders the block from `achology_member_voice_cards()` in `shared-parts.php`. That function returns **nine cards**, counted mechanically. The page's filter bar declares **five questions**, counted from the five `tm-tab` buttons. Nine times five is 45.

The template's own docblock records why this was ever in doubt, and it is worth quoting because it answers the question directly:

> "The lead says nine, the heading below said ten, and there are nine cards in achology_member_voice_cards(). Nine is ... S045 after it was reported to him."

**So: 45 answers from nine members is true. The old build card's 46 from ten is stale, and was already corrected by Kain at S045.**

*No em or en dashes in this file; checked before writing.*
