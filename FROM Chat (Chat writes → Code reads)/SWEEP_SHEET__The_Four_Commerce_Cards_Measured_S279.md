# SWEEP SHEET: the four commerce cards and the product section, measured against the four settled standards

**DOCUMENT TYPE:** sweep sheet, for the Safari sitting. Not a page spec and not a ruling.
**From:** Claude Chat, Session 279. **Date:** 17 August 2026.
**Reads with:** `HANDOVER__Card_Standards_Settled_On_The_Course_Card_S060.md`, which is where the four standards were settled, and `REPORT__School_Colour_Text_Safe_Sweep_S061.md`, which measured the colour half.
**Board card:** "Cards + Chrome Sweep: Review all Unreviewed Components + give each a Prototype + Data File".

Everything below was read from `cards.css` and `page-cards.php` in the theme working copy at style.css v0.64.1, this session. Nothing is from memory.

---

## The finding that has to be settled before anything is ruled

**All four remaining commerce cards have a stylesheet and no live component.** `page-cards.php` names three of them on its own face under "Registered, but with no live component", and Code confirmed the bundle card two ways at S061: no template emits the class, and no published page in the live database contains it.

| Component | CSS in the theme | Template that emits it |
|---|---|---|
| School bundle card | `cards.css` 1380 to 1650, `.card--bundle` | none found |
| Access All Areas card | `cards.css` 1660 to 1880, `.card--aaa` | none found |
| Membership card, monthly | `cards.css` 1900 to 1960, `.card--membership--monthly` | none found |
| Membership card, annual | `cards.css` 1960 to 2200, `.card--membership--annual` | none found |
| Product section block | `cards.css` 2210 onward, `.product-section__*` | `page-cards.php` renders the grid only |

**The scope of Chat's own check, stated honestly.** Chat read four of the theme's PHP files (`page-cards.php`, `shared-parts.php`, `courses-setup.php`, `functions.php`) and found no emitter in any of them. The whole-theme search is Code's, and one line of `page-cards.php` is already known to be stale: its §14 entry says the review card has no CSS and no template, when the review card is approved at proof v3 and `page-reviews.php` renders it. So the table above is treated as strong rather than settled until Code confirms it against the whole theme.

**What this means for the sitting.** Kain's own rule is that a component already built in the theme is judged live in Safari, never in a panel. These four are not built: they are stylesheets. So there is nothing to open in Safari and nothing to rule. Building them is a component build with its own review, not a sweep's business.

---

## The four standards, restated so each verdict below is checkable

1. **School colour.** `--school-accent` for fills, bars and decorative marks. `--school-text` for anything a reader reads.
2. **Artwork.** Every image slot has a stated source size and shape, recorded in DSRD 8. A design ruled against artwork that does not exist at that size cannot be built.
3. **Type.** The nine approved steps are 12, 14, 16, 18, 21, 24, 28, 33, 42.
4. **Icons beside text.** Align from the baseline, then lift by half the difference between icon height and cap height. Como's cap height is 0.676em.

---

## Standard 1, school colour: two sites open, both on the bundle card

Code's S061 sweep closed five of seven sites and left two, both measured and both marked in the stylesheet with the reason beside them.

| Site | Line | Ground | Contrast if swapped | Bar |
|---|---|---|---|---|
| `.card--bundle .card__hour-pill` | 1535 | its own school colour at 10 per cent | 4.03 to 4.26 | 4.5 |
| `.card--bundle .card__summary-strip .strip-text` | 1571 | its own school colour at 8 per cent | 4.13 to 4.26 | 4.5 |

The text-safe tokens were derived against a white card. On a tint of the text's own colour the ground rises toward the text and contrast is lost on both sides at once, so the swap moves these two from failing to still failing.

**One ruled exception stands:** `.card--bundle .card__tick-circle svg` at line 1512 keeps the accent, because DSRD 7 section 2.1 gives the accent to decorative marks and a tick is one.

**The Access All Areas and membership cards carry no school colour on any text.** `.card--aaa .card__school-name-text` at line 1789 is `--color-dark`. Verified this session.

**The open question this raises, which is a standard rather than a card decision.** Either school-coloured text never sits on a tint of itself, or a second darker step per school is added for tinted grounds. The first needs no new tokens.

---

## Standard 2, artwork: one slot, no stated source size

| Component | Image slot | Stated source size |
|---|---|---|
| School bundle card | `.card--bundle .card__hero-image`, line 1393, `max-width: 78%`, `max-height: 88%`, `object-fit: contain` | **none.** DSRD 8 section 8 does not state one |
| Access All Areas card | none | not applicable |
| Membership cards | none | not applicable |

This is the same fault that produced the course card sitting: 28 near-square files drawn for a landscape slot because no source size was ever specified. The bundle card's slot needs its size settled before its artwork is drawn, not after.

---

## Standard 3, type: 41 of 64 font sizes in `cards.css` are off the approved scale

**27 of the 41 sit on the four unreviewed commerce cards and the product section.**

| Component | Off-scale sizes, with lines |
|---|---|
| School bundle card (7) | 20 school-name 1445; 12.5 stat 1465; 13 course-name 1518; 10.5 hour-pill 1526; 12.5 strip-text 1566; 15 anchor-price 1596; 13 guarantee 1621 |
| Access All Areas card (9) | 13 overline 1678; 26 header-title 1691; 20 name 1741; 12.5 stat 1760; 13 school-name-text 1789; 10.5 course-count-pill 1797; 12.5 strip-text 1819; 15 anchor-price 1846; 13 guarantee 1866 |
| Membership cards (10) | 26 header-title 1925 and 1969; 13 overline 1933; 20 name 2022; 12.5 stat 2042; 13 feature-text 2083; 10.5 included-pill 2092; 12.5 strip-text 2122; 20 price-qualifier 2164; 13 price-sub 2192 |
| Product section block (1) | 32 heading 2218 |

**And 14 of the 41 sit on cards Kain has already approved by eye.** This is the part worth naming rather than absorbing, because it means the type scale sweep will reopen signed records:

| Signed record | Off-scale sizes |
|---|---|
| Shared card base | 11 type-label 98; 17 title 110; 13 footer-info 201 |
| Quote card (approved S259) | 11 author 423; 17 quote-text 435; 13 source 453 |
| Featured book note card (approved S261) | 11 overline 599; 20 title 622; 15 excerpt 631 |
| Featured quote card (approved S263) | 22 quote-text 736 |
| Mini card (approved S266) | 11 type-label 857 |
| Course card (approved S060 and S061) | 12.5 stat 1282; 13 price-qualifier 1319; 11 guarantee-pill 1328 |

**One thing to notice inside that.** The shared `.card__title` is 17px while the course card's title was ruled to 18px at S060. Whether the rest of the family follows the course card up, or the course card is the exception, is a family decision nobody has taken.

---

## Standard 4, icon alignment: only the course card follows it

`align-self: baseline` with a lift appears once in the whole stylesheet, at line 1195, on the course card's school-line icon.

| Icon rule | Line | Alignment |
|---|---|---|
| `.card--course .card__school-line .icon-school` | 1194 | **baseline, 1px lift.** The ruled one |
| `.card--course .card__stat .icon-stat` | 1287 | default. Off standard on an approved card |
| `.card--bundle .card__academy-line .icon-school` | 1435 | default |
| `.card--bundle .card__stat .icon-stat` | 1473 | default |
| `.card--bundle .card__guarantee .icon-shield` | 1626 | default |
| `.card--aaa .card__academy-line .icon-school` | 1732 | default |
| `.card--aaa .card__stat .icon-stat` | 1765 | default |
| `.card--membership .card__academy-line .icon-school` | 2013 | default |
| `.card--membership .card__stat .icon-stat` | 2047 | default |

Eight icon rules sit beside text on the default line-box alignment, which is the exact fault Kain caught by eye on the course card at S060. One of the eight is on the course card itself, so the S060 ruling was applied to the school line and not carried across to the stat row beside it.

---

## What is asked, and of whom

**Of Code.**

1. Confirm the whole-theme search: does any template anywhere emit `.card--bundle`, `.card--aaa`, `.card--membership`, or their product section wrapper? The table at the top is Chat's four-file read plus your S061 bundle confirmation, and it should be settled properly rather than half-checked.
2. Correct the stale §14 line in `page-cards.php`: the review card has CSS in `reviews.css` and is rendered by `page-reviews.php`.

**Of Chat.**

3. State the bundle card's hero source size in DSRD 8 section 8 once the slot is settled, and fold the general standard (every card image slot states its source size) into DSRD 8 section 6.
4. Correct DSRD 8 sections 8.4, 8.5, 8.6 and 8.10, which still specify the bundle card's academy line and stats as "school primary colour" and count six school colour touchpoints. The theme is right and the document is stale, per Code's S061 report.

**Of Kain, and these are the two rulings the sitting exists for.**

5. The tinted-ground standard: does school-coloured text never sit on a tint of itself, or does a second darker step per school get added?
6. Whether the four commerce components get built so they can be reviewed, or the sweep moves to the chrome and the commerce cards wait for the pages that carry them.

*No em or en dashes in this file; checked before writing.*
