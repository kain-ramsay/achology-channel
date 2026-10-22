DISPOSITION, Chat S442 open (22 October 2026): WRITTEN HOME AND ARCHIVED. DSRD 3 section 9.8 and DSRD 9 section 38.9 items 12 and 13; the topic pill at 13 on a phone is a family job for Backlog: Code. No board card moved.

STAYS, Chat S441 close (22 October 2026): arrived during S441 while the session ran long; carried unread for room, named in the S441 handover as Session 442's first act (written home, then archived).

# NOTE: the search page's SearchWP setup as found, and its full font and spacing scan (Code, S178, 22 October 2026)

For Chat: two answers Kain asked for in the sitting, filed so the record holds them. Nothing here is a ruling yet.

## 1. SearchWP, as found on the build site (read only, wp-cli)

The search results page (/?s=) is the theme's own page (search.php, kh-search-setup.php); every result comes from SearchWP 4.6.1.1 (active, licensed), its "Default" engine, never WordPress's own search. A second engine, "Help", serves the Help answers.

Default engine: sources article, book_note, quote, workbook; stemming on. Weights on every source: title 300, slug 300, author 300, content 1, excerpt 1, every custom field ("*") 1. No taxonomy is an attribute: kh_category and kh_tag are not searched. Settings: partial matches on (why everyday misspellings still find results; eight tried, all found), suggestions on (the page does not use them), highlighting off (the page marks the words itself), quoted search off, minimum word length kept, shortcodes not parsed, index not outdated, indexer not paused.

Code's recommendations to Kain, put to him in the sitting: add kh_tag and kh_category as weighted attributes; rebalance the weights (content and excerpt far below title); replace "every custom field" with the few that carry reader words (the book's author, the quote's speaker); switch on search statistics (popular and no-result searches) to feed the A to Z and planning; add synonyms (for example CBT and cognitive behavioural therapy). His answer follows in a RULING file.

## 2. The full font and spacing scan (three pages, many, few, none, at 1280, 834 and 390, WebKit)

Type: every text uses Como or Mulish on the nine steps (DSRD 7 section 3.0), with one fault on the page, fixed at theme 0.707.481: the Warm Number was 48 (32 on a phone), now 42 (28). One shared fault named for the family, not changed here: the topic pill (.tq-pill, kh-subject.css) drops to 13 on a phone, with padding 6 and 12 (Backlog: Code, a family job).

Spacing: every block gap on the scale (48, 32 on a phone; rows 24; page numbers and dividers 48; heading to list 32). The off-scale values found are all shared or cited: the page gutter 20, the kinds bar's own insets 12 and 18, the button's 12, the page numbers' 6 gap (base.css notes it unjudged, DSRD 7 4.3), the Categories bar's 20, and the search page's cited one-offs (the mini card's 6 and 12, the field's 12 inset, S375).

*No em or en dashes in this file; checked before writing.*
