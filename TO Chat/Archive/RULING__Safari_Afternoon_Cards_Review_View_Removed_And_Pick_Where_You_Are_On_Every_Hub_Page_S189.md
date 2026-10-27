**For Chat. What this needs:** write three of Kain's rulings from the Safari afternoon (Code S189, theme side session, 27 October 2026) into their homes: the Component Registry row for Pick Where You Are, DSRD 8 for the commerce cards, and DSRD 9 for the Knowledge Hub subject and list pages.

# RULING (theme, S189): the commerce cards review view goes, the subject pictures pass, and Pick Where You Are closes every Hub page

## 1. The commerce cards (brief item 1)
Code checked which commerce cards are live on the build site at 0.707.631. The Courses page and the tag pages draw the course card. The pricing page draws its own cards (pricing-parts.php): seven school bundle cards, the Access All Areas pass card, the membership plans and the choice cards. The older bundle, Access All Areas and membership cards (commerce-cards.php) appear on no live page. They appear only on /cards/, on /cards/?view=review, and in the course page's buy block, and no course page is published.
**Kain's words:** "Yes. Remove the old side-by-side review view, keep the test sheet, and close item 1."
**Shipped 0.707.640:** card-review.php is deleted, its cards.css block is cut, and page-cards.php no longer routes ?view=review. The /cards/ sheet stays, because the gates measure cards on it. The theme queue's line "The commerce cards review sitting" is closed by this ruling. Still open, for the course page sitting: its "Three Ways to Study This Course" block still calls the two old cards.

## 2. The seven subject pages' pictures (brief item 8)
**Kain's words**, after looking at /learn/psychology/ in his own Safari: "Yes, they did, Claude. They all loaded perfectly. Very, very fast, very smooth." This closes the theme queue's S157 line (narrowed at S173) and releases cloud jobs 18 and 19 for merging. They are not merged yet; the next theme session merges them.

## 3. Pick Where You Are on every Hub page (Kain's own question, raised during item 8)
Kain asked why the block he signed on the front page was not at the foot of the other Hub pages: "it would make sense ... we get maximum usage out of this new section, this component, by placing it on all pages". Code counted 39 pages carrying the old learning path (7 subject pages and 32 list pages), plus the per-book lists. Code showed four options in the Change Viewer.
**Kain's words:** "Yes, option one, exactly as I signed it. I didn't need to see the blocks to say. I just wanted this exactly as I signed it ... I just want this exact block across these pages exactly as I signed it."
**Shipped 0.707.640 and read back on the build site in WebKit at 1268 and 390** on /learn/, /learn/psychology/, /learn/mental-wellness/, /learn/mental-wellness/articles/, /learn/workbooks/, /learn/quotes/ and /learn/personal-growth/book-notes/. On every one: the block is drawn and the old path is gone, there is no sideways scroll, no picture is broken and there are no script errors. Step four is the page's own subject course (Mental Wellness: the Mental Health and Wellbeing Practitioner Diploma Course). Step one is that subject's articles list. Daniel C.'s line names the diploma he reviewed.
**Owed home, Chat:** in the Component Registry row "Pick Where You Are Cards", the pages that switch it on: the front page, the seven subject pages and every list page. The home files are unchanged (kh-front-setup.php section 7, kh-front.css, kh-front.js). The build sheet's "Home in the theme" line is updated by Code. In DSRD 9, the subject page and list page sections now close on this block. T14's "delve" line in the old path panel no longer renders on these pages.

## 4. Not this afternoon
Items 2 to 6 (header, breadcrumb, Where Next panel, footer, section header) were already signed: Code S080, S090 and S091, all written home at Chat S303 and S337. Item 9 was settled by Kain in Chat (left as it is). Item 7, the type rules, is with Kain now.

OWED BACK: the dated lines in the Component Registry and DSRD 9 named above.

*No em or en dashes in this file; checked before writing.*
