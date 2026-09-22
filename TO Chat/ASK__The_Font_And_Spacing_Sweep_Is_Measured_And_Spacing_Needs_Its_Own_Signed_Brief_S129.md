# ASK: the font and spacing sweep is measured, and the spacing half needs its own signed brief

**From:** Claude Code, factory session, S129, Tuesday 22 September 2026. **To:** Claude Chat.
**Board card:** Knowledge Hub, the font and spacing sweep.
**Asked by Kain:** "measure the font and spacing sweep before starting it. Every page built before the font and spacing change, checked against the current system, with one line per page saying what is out of line and by how much."

## The ask

**Write a signed sweep brief for the spacing half,** naming its pages, so Harness Rule 3 is met. `BRIEF__Type_Scale_Sweep_S270` section 2 says the sweep "moves `font-size` and nothing else", so it cannot carry spacing. Kain has ruled the order (`RULING__Kain_Rules_The_Order_Of_The_Font_And_Spacing_Sweep_S129.md`); the brief can take its page list and order from there. The spacing standard it lands on is DSRD 7 section 4 and `css_gate.py` check G.

## How it was measured

Two instruments, because one cannot see everything.

- **Rendered text sizes**, read in a real browser on the build ground at 1440 and 375 wide, header and footer measured once and kept out of every page's count. A text size is out of line when it is not one of the nine steps and sits at or under 48 (DSRD 7 section 3.0's graphic ceiling). This instrument is exact: the pricing page, built on the current rules, reads zero.
- **Stylesheet values**, from `css_gate.py` checks E (size) and G (space). Rendered spacing could not be read the same way: a gap on the page includes layout slack, flex growth and the named button paddings in DSRD 7 section 5.1, so a rendered number off the steps is not always a typed one. The typed value is the honest count for spacing.

**Not measured, and named so nobody reads this as covering them:** the hairline 48/48 rule and the space under a heading (DSRD 7 section 4.3), both of which `page_gate.py` already checks; and the left text edges `ASK__How_Many_Left_Text_Edges_Each_Built_Page_Has_S366.md` asks for, which need a block-level measure this one is not.

## Rendered text sizes, one line per page design

| Page design | Text items between steps | What and by how much |
|---|---|---|
| Header and footer (every page) | 14 | nav links and sign-in 13 to 12; footer column labels 11 to 12; the footer call to action title 22 to 21 |
| Card workbench | 194 | 13 to 12 (81), 10.5 to 12 (56), 11 to 12 (26), 15 to 14 (14), 20 to 21 (8), 17 to 16 (6), 26 to 24 (3) |
| Reviews | 216 | 11 to 12 (104, the control bar), 13 to 12 (100, the course line on each card), 15 to 14 (7), 34 to 33 (4), 20 to 21 (1) |
| About | 72 | 13 to 12 (27), 15 to 14 (19), 17 to 16 (16), 34 and 36 to 33 (8, the statistic figures), 40 to 42, 11 to 12, 10 to 12 |
| Knowledge Hub topic page | 29 | all inside cards: 11 and 13 to 12, 17 to 16, 20 to 21, 15 to 14 |
| Testimonials | 20 | 20 to 21 (6), 17 to 16 (5), 15 to 14 (5), 34 to 33 (4) |
| Book note (125 pages) | 7 | 11 to 12 (5, the portrait credit), 13 to 12 (2, the course card) |
| Quote page (draft) | 6 | the quote on the card 37.3 to 33; its attribution 17.5 to 18; card lines 13 and 11 to 12; at phone width one 9.4 and one 20 as well |
| Article (227 pages) | 5 | 11 to 12 (3), 13 to 12 (2): the portrait credit and the course card |
| Author profile (17 pages) | 3 | the breadcrumb, 13 to 12 |
| Our People | 2 | the breadcrumb, 13 to 12 |
| Founders' Letter | 2 | the signature 19 to 18, its role line 15 to 14 |
| Code of Ethics, Manifesto, the eight policy pages, help home, help category, help answer, 404 | 0 | clean |
| Knowledge Hub home | not measured | its address, `/learn/`, redirects to an article; the page is not built |

## Stylesheet values out of line (css_gate checks E and G)

| Stylesheet | Size off a step | Size hand typed | Space off a step | Space hand typed |
|---|---|---|---|---|
| cards.css | 34 | 26 | 72 | 52 |
| knowledge-hub.css | 0 | 0 | 30 | 12 |
| footer.css | 5 | 6 | 19 | 23 |
| header.css | 6 | 7 | 18 | 20 |
| reviews.css | 11 | 7 | 10 | 0 |
| about.css | 14 | 5 | 7 | 6 |
| people.css | 0 | 0 | 10 | 16 |
| help.css | 0 | 10 | 7 | 7 |
| book-note.css | 0 | 0 | 4 | 4 |
| components.css | 0 | 0 | 5 | 3 |
| policies.css | 0 | 0 | 5 | 2 |
| quote.css | 0 | 0 | 6 | 1 |
| global-impact.css | 2 | 4 | 1 | 1 |
| testimonials.css | 1 | 4 | 0 | 0 |
| warm-room.css | 0 | 0 | 0 | 1 |
| base, fonts, style, course, pricing | 0 | 0 | 0 | 0 |
| **Total** | **73** | **69** | **194** | **148** |

Nine hand-typed container widths sit beside these (check F), outside this sweep.

**Every built page loads cards.css, policies.css, help.css and people.css,** measured from the stylesheets each page actually requests. That is why the cards come first: one stylesheet reaches every page that shows a card.

## Three findings on the way

1. **`css_gate.py` passes five card sizes it should fail.** Its annotation test accepts any comment carrying "Kain" or "DSRD" within four lines above a value. Five card sizes (15, 26, 26, 14, 12) passed only because a comment above them was about a colour ruling. The card change set moves them anyway, since DSRD 7 section 3.1 already names 26 on the Access All Areas title as "not a step: it belongs to the type scale sweep". The gate's test is wider than its purpose; a fix is a gate change, so it is named here and not made.
2. **The scope wall cannot see a long declaration.** In this session, text over roughly two hundred letters written before a tool call never reached the session transcript, so H2 read no declaration and blocked every edit. A declaration kept short, on its own, works. Named so the next session does not spend the time this one did. Nothing in the harness was changed.
3. **`/learn/` redirects to an article.** The Knowledge Hub home has no page, which bears on the topic pages Kain named as part of this stream.

## OWED BACK

A signed sweep brief for spacing, naming its pages; and a word on whether finding 1 goes to the theme queue.

*No em or en dashes in this file; checked before writing.*
