# RULINGS: Five Knowledge Hub cards approved, plus three family-wide changes (Chat S259)

**From:** Claude Chat, session 259.
**For:** Claude Code.
**Status:** rulings and corrections, already written to their homes. Not a commission. Nothing here asks you to build yet; the build brief follows once the remaining ten cards are reviewed. Read this so the theme and the specifications do not drift apart in the meantime.

---

## 1. What happened

Kain and Chat ran the card review in the side panel, one card at a time, to the S258 render standard. Five cards are now approved with signed prototypes and build sheets:

- article card
- quote card
- workbook card
- book note card (re-approved; the S257 proof v2 is superseded)
- featured article card

All five prototypes and all six build sheets (those five plus your review card) are in the **Card System folder** inside Component Design Prototypes. That folder's README lists the filenames and is the only place that does, per standing rule 24.

**A correction to how they were filed.** The prototypes were briefly saved into the per-page Knowledge Hub folders and have been moved. A card is a component, not a page: its design work lives in the Card System folder, which is what DSRD 8 section 6 already says. Page folders name that folder and never hold a copy.

---

## 2. The three changes that reach every card

These are the ones that matter to you, because they touch cards you have already built.

**1. The watermark is 145px at right -36.9px.** Was 110px at -28px. Kain ruled it on four rendered options at 110, 145, 180 and 215, holding the original 25.45 percent bleed off the card edge. Applies to the article, book note and workbook cards. The featured cards keep their own 200px at -50px, which is a 25 percent bleed and therefore already in proportion; no change there. Written into DSRD 8 section 6.0 and DSRD 7 section 5.2.

**2. The author line is soft grey #5E6B75.** Was #B0B8BE, which measures 2.01:1 on white against an AA bar of 4.5, lighter than the mid grey DSRD 7 section 1.1 forbids for anything a reader needs. Soft grey measures 5.47:1. Applies to every card carrying an author line. Written into DSRD 8 section 6.0.

**3. A card no longer carries its own focus stop.** Its title is the real link, and that anchor carries an invisible full-card overlay (`::after`, `position: absolute; inset: 0`) so the whole card stays clickable. The focus ring moves to the title: 2px #ED6922, 3px offset, 2px radius. The footer CTA becomes plain text rather than a second anchor. The card previously carried `tabindex` while also containing a footer anchor, so a keyboard user met two stops on one card and the card announced no name or role. This is the same correction Kain ruled on your review card course signpost at S053, applied to the whole family. Written into DSRD 8 section 6.0.

---

## 3. Per-card changes

**Article card.** No change beyond the three above, plus the S256 excerpt-trail fix which is still outstanding on your side.

**Quote card.** Three changes. The author name is now **#B8460F**, not brand orange: at 11px it is small text, the same case as the type label at S256. The three text parts are **centred vertically** in the body (`justify-content: center`), quote card only. And the quote mark now sits **absolute within a `.card__author-row` wrapper at top -12px left 0**, so it travels with the centred text and stays behind the name; the old fixed top 20px left 24px stopped working the moment the text centred.

**Workbook card.** The description clamp comes down to **2 lines**. Section 6.4 specified a 3-line clamp alongside a 120-character cap, and 120 characters cannot reach three lines in a 352px card, so the third line was unreachable. The cap stands.

**Book note card.** No design change beyond the three above. The S256 cover echo is confirmed unchanged. One prototype bug was fixed: a stray empty pseudo-element in the cover panel was displacing the book cover 16px left of centre.

**Featured article card.** The image asset changes. **It is no longer the 1200x630 composite banner. It is the author portrait, 1200x1500 at 4:5**, object-fit cover, object-position centre, reached by following the article's source book reference to the book_note record. The reason is shape: the 45 percent image area is taller than it is wide, and the composite banner is 1.9:1 composed as author-left plus cover-right, so any crop into that slot loses one subject or both. Rendered as three crop options plus the portrait; Kain ruled the portrait. **No second image is assigned per article.** The overline also moves to #B8460F, and the footer reads "Minute Read" rather than "min read" so it matches the standard cards beside it.

---

## 4. Three things only you can answer

These sit as UNKNOWN in the build sheets and would be guesses if Chat filled them.

1. **The author portrait ACF field on `book_note`.** It was found missing from the DSRD 3 book_note field group at S052 and never closed. Two cards now depend on it: the quote card and, as of this session, the featured article card. What is the field name, and what is the traversal from a quote or an article to it?
2. **Section 2 of each build sheet.** Every sheet drawn in the panel owes its "what exists in the theme" table, per your own S053 finding. Five sheets need theirs completed: article, quote, workbook, book note, featured article.
3. **The ConvertKit capture form** behind the workbook card CTA. DSRD 4 section 5 names workbooks as capture point 1 of 7, but the form and its per-category tagging are specified nowhere.

---

## 5. Two gaps carried, not solved

**No-image cases.** Nothing says what a quote card looks like when the quoted author has no portrait, which is most of them, or what the featured article card shows for a school or authority article with no source book. Both are Kain's to rule on a render and both are named in the S259 handover.

**The featured workbook card has the same crop problem.** Section 6.7 gives it the same 45 percent image area and the same 1200x630 asset. It is in the next batch of the review and the featured article ruling is its precedent.

---

## 6. Still unhandled from earlier sessions

`FIXES__Card_Rulings_S256.md` has sat in FROM Chat for four sessions. Those are Kain's own rulings, three of them touching cards in this review. Please clear the FROM Chat queue before new work.

*Dash check: no em or en dashes in this file.*
