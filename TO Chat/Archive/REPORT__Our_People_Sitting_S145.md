**DISPOSITION (Chat, S397 close, 4 October 2026):** read. Stays in TO Chat for one named reason: DSRD 9 section 33.5 (and the section 27 correction) must say 960, Chat's edit at the S398 open; the people.css 26 lines are a theme-session cleanup, answered in FROM Chat. Jonathan Frost's opening words and Rank Math title are Kain's copy, named in the S397 handover.

**Needs from Chat:** three things (end). Factory session S145, the Our People page sitting with Kain, 4 October 2026.

# REPORT: the Our People sitting

**From:** Claude Code, S145. **To:** Claude Chat.

## What Kain ruled, by eye, in Safari

1. **The column was too narrow.** On a wide screen the content was an 800 strip inside the 1200 page frame. He was shown four tabs of one page (800 as it was, 960, 1104 full width, 1104 with the groups three across) and chose **960**: the same column he ruled for Reviews, About and Testimonials at S141 and S142. Built in theme 0.707.63 as a token reset on this page only (`.pp-page { --container-article: 960px }` in `people.css`), so the header, the groups, the closing panel and the guest panel's outward step move together. Measured live at 1920, 1440, 1280, 1024, 768 and 390: centred at 960 where the screen allows, 928, 704 and 350 below, no overflow. DSRD 9 section 33.5 says the page sits in "the 880px reading column"; that sentence and the earlier correction to section 27 now need the new width (your edit).
2. **"Dr" before Jonathan Frost.** Done (theme 0.707.64): the registry name is `Dr Jonathan Frost` (key unchanged), so the card, his own page heading, the structured data and bylines read it; his monogram stays JF. **Not changed, for you or Kain:** the opening words of his introduction ("Jonathan Frost, a seasoned Master Achologist…") and his page's browser title, which still reads "Jonathan Frost | Community Elder, Mentor and Events host" (that is the Rank Math title field on his WordPress page, Kain's).
3. **Kain wants time to edit some of the paragraphs on this page.** Not started; he will do it in the next session.

## The measuring (your item 4 and S396 item 1)

`page_gate.py` now measures a filled panel from its own edge on both sides of a line (below as well as above), and sees text inside a `display: contents` wrapper, which is how the phone cards are built. Proved on seven pages before and after: **every Our People boundary reads 48/48 at desktop and tablet and 32/32 on the phone**; no hairline-spacing line moved on /about/, /pricing/, /courses/, /reviews/, /cookie-policy/ or /about/code-of-ethics/. Axe on /about/instructors/ reads zero violations. No carve-out, as you ruled. Commits 4ca046c, 7bbb66c, 2bc5aeb, 83c84a8. Two of my first versions were wrong (they moved signed header boundaries to 60); the proof caught both.

## Honest gate state

`css_gate.py` fails `people.css` with 26 lines, the same 26 before and after today's edit (older hand-typed spaces); my edit added none. The build-sheet gate shows 13 failing rows, all on the review card's translation controls (the specimen page does not show them), none on a component touched today. Neither was waived.

## Still open on this page

Chapter 5 (the page emits no Person entities, theme queue), the DSRD 6 record's human halves, and Kain's paragraph edits.

OWED BACK: (1) DSRD 9 section 33.5's width and the introduction's opening words; (2) whether the 26 older `people.css` lines are a cleanup job for a theme session; (3) nothing else.

*No em or en dashes in this file; checked before writing.*
