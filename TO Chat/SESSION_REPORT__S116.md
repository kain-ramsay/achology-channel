# SESSION REPORT: S116, a theme session on the responsive layer, the author portrait and the drawn book

**Filed by Claude Code, Session 116. Date:** Monday 14 September 2026.
**Session type:** theme. **Shipped:** 0.416.0 through 0.425.3, twenty nine change sets, all deployed and live on the build ground, all pushed.
**Assembled from the version control log for the session**, per Harness Rule 13.

---

## Finished

**The responsive layer below 1200 on the book note and the article.** 0.416.0 to 0.418.2. Kain's shape from the close of S115: the contents becomes a strip under the hero, the cover's button rejoins the hero, the reading shelf and the Know Your Psychology mark return to the foot. The card's type and its three separations were declared inside the desktop-only block and were moved out, not copied, so one set of rules governs three widths. **Board cards:** Book note template; Article template.

**The responsive layer reworked on his instruction in the sitting**, after he called the first pass diabolical. Eleven faults, every one measured on the deployed page. The article's hero was drawing its own photograph twice, once as the band behind and once as the card on top, which is what read as an image bleeding out of its frame. The book note's cover changed sides as the window narrowed, leaving two left margins. The wash ran down the page instead of across it on a phone. Four DSRD 7 section 4.3 one-owner breaks. Three pictures declaring a shape they are not. Filed as `RULING__The_Phone_Cover_Comes_Down_To_240_And_The_Hero_Reads_Title_First_S116.md`. **Board cards:** Book note template; Article template.

**The badges.** 0.419.0 to 0.422.1. The banner badge is deleted, markup and rules, because it drew over the lower right quarter of the jacket. The closing badge went left and then back to the right on his second look. Underneath both: a floated element inside a grid is not floated, so every float in the writing had silently stopped since S112, the author photograph and the course card included. The writing is a plain column again with the strip held out of flow beside it. In the same RULING file, sections 8 and 10. **Board cards:** Book note template; Article template.

**The writer's face on articles.** 0.420.0 to 0.422.0. An instructor article and Karen's carry their author's photograph in the writing the way a book note carries the book author's, from the same block, with the person's role under the name. Placement is Kain's own rule from the sitting: the second paragraph of the section, which replaced an arithmetic fit I had built and which lands in the same place on every page tested. In the same RULING file, section 9. **Board card:** Article template.

**The drawn book, `ach-book`.** 0.423.0 to 0.425.3. Approved and locked by Kain on the rendered page. Drawn on the book note hero, the book note side column, the quote page's source block and the article's source callout. Prototype and build sheet exported at the locked state into `Book (ach-book)` in the Component Design Prototypes folder. Filed as `RULING__The_Drawn_Book_Is_Approved_And_The_Cover_Refetch_Is_Dropped_S116.md`. **Board card:** Book note page template: second look in Safari.

**The cover re-fetch is dropped, with the measurements that killed it.** Our covers are 1000 by 1500; Open Library's largest for these titles is about 320 by 500; Google Books answers 429 to every call. The S360 brief's gate line, a cover at or above 1200px from that fetch, cannot be met by the source it names. Also corrected: the brief sends Code to the master workbook's Books tab for ISBNs and there is no ISBN column there; 103 of the 153 book note records carry one. In the same RULING. **Board card:** Book note page template.

**`page_gate` on both page types.** The book note went from 24 failures to 15 and the article from 11 to 10. Everything still failing is content, asset, record or registry work rather than layout. Two chapters are decisions for Kain rather than fixes and are named in the first RULING's section 6. **Board card:** Page readiness.

## Not finished

**The quote page.** Not started; it is the next sitting by Kain's word. `single-quote.php` exists, contrary to the note written at the close of S115, and what is owed is a read of it against `RULING__The_Quote_Page_Reflection_Question_Returns_To_The_Body_Under_A_Third_Heading_S356`, then the gap. **Board card:** Quote page template.

**The workbook page.** Not started. **Board card:** Workbook template.

**The drawn book in three more places:** the book note card, the Knowledge Hub home page and the author biography's book list. Also untouched: the baked share image per book and its stamp. **Board card:** Book note page template.

**The ruling detail for 0.401.0 through 0.414.0** that `REPLY__The_Book_Note_Batch_From_S114_And_S115_Answered_S360` section 6 asks for. Not written; it blocks the prototype re-export and the book button answer by Chat's own sequencing. **Board card:** Book note template.

**The preview route move**, ruled today in `RULING__Previews_Move_Off_The_Theme_To_Their_Own_Folder_S360`. Read on arrival, not started.

**The DuckDuckGo server**, briefed today. Not installed: adding a server restarts the tooling and Kain was at the page watching changes land.

**The postbag.** Eighty five files in FROM Chat, four read this sitting, the rest named but unopened under the stream scoping. Kain asked for it cleared before the quote page; agreed, and it wants a sitting of its own because it is factory work.

## The channel

Five files arrived from Chat mid-session, all read in full on arrival under the channel wall and head-lined: the book note batch reply, the previews ruling, the CQ018 import brief, the DuckDuckGo brief, and the rewritten drawn-book brief. The last of those says "do not start yet"; Kain lifted that in the sitting and the conflict is recorded in its own RULING rather than left for Chat to find.

---

OWED BACK: nothing beyond the two RULING files, which carry what Chat needs to write home.

*No em or en dashes in this file; checked before writing.*
