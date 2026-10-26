DONE AND ARCHIVED, Chat S446 (26 October 2026): sign-off on the board (Courses directory, Done) and in the DSRD6_RECORD; picks in the signed spec, Amendment 5; both section 4 decisions found already ruled; section 5 lines sent to their owners in the two S446 rulings.

CARRIED, Chat S445 close (26 October 2026): landed in the channel during Session 445's night of signing and read at the close; it is the next session's first act, before any new work: Kain's Courses sign-off (0.707.525) written onto the board and the page's record, the nine picks written into the signed spec, the two section 4 decisions put to Kain, the section 5 gate lines sent to their owners. Named in the Session 445 handover with this reason.

NEEDS FROM CHAT: KAIN SIGNED THE COURSES PAGE OFF at the end of this sitting, on the page as live at theme 0.707.525: "Yes, I'm happy to sign the Courses page off." Write that onto the board and the page's record (his line); write Kain's S180 picks into the Courses page's signed spec as an amendment; rule the two open decisions in section 4 with Kain; take the gate lines in section 5 to their owners.

# RULING: Kain picks nine of ten Courses tweaks, the bolder chosen answer, and the code review fixes (S180)

**Kain's words**, in the S180 Courses theme side session, after ten tweaks were shown playing on the real page (one page of tabs, each tab the page with one tweak switched on and playing by itself at its part of the page): "yes to everything. Yes to all 10. Apart from number 7. So I do not want living pictures." On 7: "one step too much ... there's too many movements going on the card." Then, on the chosen answers: "increase the weight maybe by ... half of a size weight ... a little bit bolder, but not that much ... when selected."

## 1. What is built, live at theme 0.707.513 (commits 34db7ac7, 71a17aa1, 11bebb8d)
courses-directory.css section 8 and courses-directory.js; template-courses.php is back to its signed form plus one hidden status line. The ?courses-tweak switch and the demo are removed whole.
1. **Answers Cascade:** the fifteen answers ripple into place as the page opens.
2. **Tick Draws Itself:** the soft tick behind a chosen answer draws on from left to right.
3. **Spring Press:** an answer gives under the press and springs back when ticked.
4. **Hairline Draws Out:** the band's hairline draws out from the middle, a warm glint ahead of it.
5. **Counting Overline:** the 28 and the 7 count up and settle on Kain's words.
6. **Rich Texture:** a fine grain and a soft warm light on the band (still).
7. Living Pictures: NOT taken.
8. **Focus Pull:** each course picture comes into focus as its card rises.
9. **Best Match Shine:** the flag's light runs twice and a warm ring breathes out twice from the first card, then both rest.
10. **Follow-Along Spring:** the follow-along bar springs up and its arrow nudges down three times.
Plus: a chosen answer's words go from Mulish 400 to 500. Built first at 450 (his "a quarter or a half"); later, shown 450, 500, 550 and 600 on the page, Kain said "500 (recommended) please"; live at 0.707.525 (d9aacff9). Every movement stands still for reduced motion.

## 2. The independent code review (Codex could not run: its account is at its usage limit until 24 November 2026; a fresh Claude reviewer took the same brief, read only)
Scored the page 7 of 10. Confirmed and fixed (11bebb8d), each measured in WebKit:
- Rich Texture took the overline and breadcrumb under AA on desktop (measured worst pixel 3.5 and 3.8). The warm light now rises behind the answers at 16%, the grain is at 10%: desktop passes on every word.
- Warm Torchlight on a chosen answer, 40% to 22% at its centre: its white words now 4.6 to 5.0 under the light (were 3.9 to 4.1).
- The Best Match shine was infinite: now twice (WCAG 2.2.2).
- Answers Cascade held Spring Press still for the first 1.4s and a back-button restore made answers spring: both now per answer, from classes the script sets.
- The results no longer announced their change to screen readers (the S137 status line went with the bar's dead markup this morning): a hidden role=status line now repeats Kain's heading words after a tick, a sort or Clear.
- The Counting Overline read "0 COURSES" to screen readers while counting: they now hear the words alone.
- The Warm Torchlight handler measured and wrote per tile on every pointer move: now once per frame.
Not confirmed: the floating bar painting under the card pictures (the bar hides before the cards reach it).

## 3. Checks
- WebKit at 1280, 834 and 390, local files against the page as signed, before and after ticks: geometry identical once settled except one chosen word 1px wider (the bolder weight); reduced motion differs only on the band (Rich Texture); no script errors; no answer re-wraps when chosen; css_gate passes.
- page_gate on 0.707.513: 40 passed, 7 failed. The accessibility-scan fail (23 to 26 colour-contrast nodes, varying run to run) is the scan catching cards mid-rise: the gate's own axe 4.10.2 run on the settled page, with reduced motion, and after a tick, reads zero violations every time. The gate scans before the page's motion has settled; that is an instrument question for the theme session, not a page fault.

## 4. Two decisions for Kain (to be shown, not described)
1. **RULED, built and live at 0.707.521 (c96b6cc4).** The overline over the photograph on tablet and phone measured under AA at its worst pixel (834: 4.2, 390: 3.4; before today's work: 4.5 and 3.7). Shown three fixes on the real page at both widths, each measured to pass (a fourth, a lighter orange, was dropped because the phone breadcrumb stayed at 4.49), Kain said: "Yes, build option 1, Photo Fades Below the Title." Below 1024 the photograph now fades in from 30% to 60% of the band's height; the overline and breadcrumb measure 4.73 and 4.93 at 834 and 390, desktop unchanged. Build sheet section 1 and the prototype (re-exported at 0.707.521) carry it.
2. **RULED, no change.** Courses Rise In replays every shown card on Explore More, as he chose it; the reviewer would have had only the new cards rise. Asked whether all the cards should keep rising again, Kain said: "yes". The behaviour stands as built and as the build sheet's Courses Rise In row says.

## 5. Gate lines still open, none from today's work, for their owners
dsrd6-record (the record's own lines, Chat and Code); chain-register (8 workbook rows, dest_built and dest_in_sitemap); orphan (the crawl missed 913 pages; search_gate.py --map); rank-math 86 (accepted by Kain, Amendment 4); keyword-density (a directory with an empty body); icon-registry (the guarantee badge drawing in the shared course card). The reviewer's other notes, in the shared card and site wide: the student count read as a bare number and the card title a div (chapter 7's known card fault), Course schema without a description, :focus-within on click, and the tombstone comment and course 024's hours in courses-setup.php.

## 6. Fold-back (Harness Rule 14)
- **Build sheet updated:** BUILD_SHEET__Courses_Directory_Page.md carries a row for each pick, the chosen weight, and the torchlight and texture values as measured.
- **Prototype written:** PROTOTYPE__Courses_Directory_Page_S138.html re-exported from the deployed page at 0.707.513 (export_page.py, 13 stylesheets inlined).

*No em or en dashes in this file; checked before writing.*
