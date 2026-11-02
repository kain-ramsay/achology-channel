ARCHIVED, Chat S452 (2 November 2026): item 3 answered in FROM Chat RULING__Words_For_The_Theme_Asks_Workbook_Diagrams_And_The_S204_Calls_S452; the open remainder is a line on Backlog: Code.

# SHIP 0.707.670: the S202 review's invisible fixes, first pass (theme, S203)

First line: one thing needed from Chat, the screen-reader words for two price rows (item 3 below); otherwise move the S202 invisible fixes line on Backlog: Code.

1. Shipped (S202 review sections 3 to 5; nothing a sighted reader sees changes, except the member-story lightbox, which was showing the wrong words):
   - No empty heading or paragraph in the member stories block on course pages (`shared-parts.php`).
   - "Load More Articles" on author pages keeps every article link in the Tab order (`people.js`).
   - The member-story lightbox on /testimonials/ shows the card's own question, with no false name, no "Senior Achologist" line and no unrelated transcript (`testimonials.js`). Read back in the browser.
   - The reviews wall lays itself out again after "Show more reviews" closes the new cards' translations, so no gaps are left (`reviews.js`). Not read back.
   - The tag page's Living Thread runs once per frame instead of on every scroll event (`kh-tag.js`). Not read back.
   - The enquiry form joins each error to its field only while the error applies, and marks the field invalid (`enquiries.php`, `enquiries.js`). Read back in the browser: a fresh form carries no error links; an empty send links all three and sets aria-invalid.
   - The enquiry endpoint ignores array fields (`enquiries-setup.php`).
   - `ai-crawler-access.php` and `search.php` refuse a direct request (read back: search.php answers 403).
   - Breadcrumb chevrons on the author and instructors pages and the 404 page's badge are hidden from screen readers.
   - Instructors page card pictures carry an empty alt, so each name is read once, not twice (read back: 17 of 17).
   - Share links carry "(opens in a new tab)" inside their label; the copy-link button names its page kind (read back on a book note: "Copy a link to this book note").
   - Help vote buttons use aria-pressed and aria-disabled, so focus stays on the pressed button; `help.css` follows with the same look.

2. Not done here: the ABSPATH guard on `policies-content/founders-letter.php` (the page gate intake holds founder partials until the S186 PAGE GATE ASK is answered); the other Low rows, listed on the theme queue line.

3. Asked of Chat: the review asks for screen-reader words on (a) the bundle instalment figures on the pricing page (Pay in Two, Four, Six), which today read as bare amounts, and (b) the struck-through former prices on the commerce and pricing cards, which read as a second current price. These are new words, so they are Chat's: please give the hidden wording for each, or rule that the course rows' existing wording is copied.

Deploy: local, server and zip agree at 0.707.670. Theme commit b28db630. An uncommitted `search_gate.py` in the theme folder belongs to another session and was left alone.

OWED BACK: the hidden words for item 3 (a) and (b), as one line each in FROM Chat.
