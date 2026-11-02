ARCHIVED, Chat S452 (2 November 2026): cloud jobs 18 and 19 struck on Backlog: Code; job 20 remains there.

**Needs from Chat: mark these lines on the board from this file; nothing here waits on a decision. For the theme session's record.**

# SHIP: hidden fixes, pictures and the two cloud jobs (theme side session, S203, 1 November 2026)

Every change below is invisible to a visitor, or is a cloud job Kain released at S189. Only the theme main session deployed; each version was read back from the server over SSH after its deploy.

## What shipped

1. **0.707.672, cloud job 19.** The checklist tick on the bundle, Access All Areas and membership cards is drawn by the icon registry (`achology_icon( 'check' )`) at stroke 3, not from the cards' own local array (DSRD 7 section 12.4). Reviewed against main before merging. Read back: the deployed commerce-cards.php carries six registry ticks and none of the old ones. No page on the build site draws these cards yet (/cards/ answers 404 and no course page exists), so there is nothing to see.
2. **0.707.674, the S167 page gate picture line.** Measured again first, and three parts were already true: the course quote covers carry their 224 and 448 copies; the book note's More by block draws no covers since Kain S179; pete-walker.webp's alt reads "Pete Walker". Shipped: the Know Your Psychology column logo offers 280 and 560 copies; the article and quote page hero offers WordPress's own sizes (or a theme picture's copies); course-quote-cover-001.webp is 60,344 bytes, under its 60 KB budget. Read back on a quote page: both srcsets present, the new files answer 200.
3. **The sky-less re-exports.** The Pick Where You Are Cards prototype and the Knowledge Hub Homepage prototype were re-exported from /learn/ at 0.707.673 by tools/fold_back.py, and the cards' build sheet's sky row now reads plain white (Kain S190, DSRD 9 section 39.15). Nothing on the site changed.
4. **0.707.676, the S202 review's Low script rows.** reviews.js: labels lead to the visible control; on the last batch, focus moves to the first new card; the wall reads every height in one pass. kh-tag.js: "Link copied" is said in a status line, and a refused copy no longer shows success; the two-line titles redo their split at most once a frame, only when the width changes. workbook.js: the page behind the full-size viewer is inert. enquiries.js and kh-front.js: the torchlight effects measure first, then paint. knowledge-hub.js: a reader's Show or Hide choice survives the phone-width crossing. index.php: the archive fallback has its one h1, in WordPress's own words. functions.php: the Kit plugin's editor button (its quicktags script, stylesheet and the hidden template with the empty h1) is off the front end; Kit's forms are untouched. Read back: every change is in the deployed files, and a book note's source carries no Kit template and no empty h1.
5. **0.707.679, cloud job 18.** WebP copies of the 45 member avatars (150 and 220) and 45 video backgrounds (460), offered by srcset and image-set with the JPGs kept as fallback. This closes the S102 member card avatars line (the names were already lower case since S117). One fault fixed at the merge: the portrait srcset went through esc_url as a whole, which turns its spaces into %20; each address is now escaped on its own. Read back: see the line at the foot of this file.

## Theme queue lines

Struck: the S167 picture line (0.707.674), the commerce cards' tick glyph (0.707.672), the S169 Kit empty h1 and the S119 empty h1 (0.707.676), the S102 member card avatars and the S157 jobs 18 and 19 line (0.707.679). Narrowed: the S202 review line; still open there are the founders-letter.php guard, the struck-price words, get_term_link, the course empty block, the book note reading_lead, the import batch constant and the pricing h2 levels (pricing-parts.php belongs to another session).

## Reach

These are fixes of named faults, not polish, so no sweep is proposed. The hero srcset reaches every article and quote page through the shared hero, and the Kit trim reaches every page.

## Read back of 0.707.679

Deployed by the theme main session and read back from the server on /testimonials/: nine member portraits carry the 150 and 220 WebP srcset with no %20 in it, nine cards carry the WebP face image-set, and the avatar and background copies answer 200 (jon-q4: 2,170, 3,524 and 5,586 bytes). The main session's S203 lightbox fix in testimonials.js is kept.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
