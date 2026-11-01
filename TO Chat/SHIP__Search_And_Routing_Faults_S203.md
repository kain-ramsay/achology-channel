# SHIP 0.707.669: search words, search links, the Help back link and two soft 404s (theme, S203)

First line: nothing needed from Chat beyond moving the S202 review's search and routing lines on Backlog: Code; one row stays with the whole-site search brief.

What changed, each from the S202 cloud review, section 3:
1. Search words are counted in letters, not bytes (`kh-search-setup.php`), so an accented or curly-apostrophe search no longer blanks every title and snippet; if a pattern ever fails, the plain text shows. Read back from the server: "Freud’s" finds 32 results with "Freud" marked in the snippets.
2. The kind and sort links encode the search words, so "stress & anxiety" stays whole. Read back: `?s=stress%20%26%20anxiety&ach_kind=article`.
3. A Help answer's "More Questions in this Category" link takes the primary category, the one its breadcrumb and address use (`single-faq_article.php`).
4. `/learn/anything/articles/` and a book under a category that is not its own now answer 404 (`knowledge-hub-setup.php`). This also ships item 2 of the S169 four-decisions branch (Kain's yes, S169). Read back from the server: those two 404; the real book listing, `/learn/mental-wellness/articles/` and `/learn/articles/` still 200.

Not done here: row 9 (a search page number past the end answers an empty 200). The list pages by its own query, so the fix belongs in BRIEF__Site_Search_One_Search_For_The_Whole_Site_S448; the queue line now says so.

Not verified: item 3 on a live two-category answer whose first category differs from its primary; the change is one line and the page parses on the server. Verified 3 of 4 on the build site.

A note for the record: reads from this Mac after the deploy met SiteGround's bot check (202), so the read-back ran from the server itself.

Deploy: local, server and zip agree at 0.707.669. Theme commit 9e61c1ae.

OWED BACK: nothing.
