> CODE DISPOSITION, S130: WAITS ON a factory session: article-sitemap1.xml and book_note-sitemap1.xml returning 200 on the build install. Read in full mid-session in a theme sitting on the quote page; it names no page, so it is factory work and nothing in it touches the quote work in hand.

BRIEF, from Claude Chat to Claude Code, Session 377. Approved by Kain in session ("Yes please"). A small configuration job on an existing card, not a new commission of work.

# Switch On The Article And Book Note Sitemaps

## Why

The Plugins and Site Configuration card (Notion, 3aa4da19af35813b8643d7895e0eb148) has carried this line since S087, confirmed sharper at S339: on the build install, sitemap_index.xml names only the page and faq_article sitemaps, and article-sitemap1.xml and book_note-sitemap1.xml both return 404. The whole Knowledge Hub has never had a sitemap entry. The card records it as a Rank Math configuration gap, not a theme fault. At launch the sitemap is submitted to Google Search Console and Bing Webmaster Tools (PRD Pr2.8 and D9; DSRD 3), so without this fix Google and Bing are never told the Knowledge Hub exists.

## The work

1. In Rank Math's Sitemap Settings, switch on the post type sitemaps for `article` and `book_note`. While there, check every other public Knowledge Hub post type the theme registers (for example `quote` and `workbook`, if they carry published records) and switch those on too; leave off anything that should not be indexed.
2. Leave indexing behaviour exactly as it is today: the noindex meta tag still holds the build site out of the index until cutover. This job is only about the sitemap listing the right post types.
3. Load sitemap_index.xml and each new child sitemap and confirm they return 200 and list real published records.

## What to send back

One REPORT in TO Chat with: the post types now in the sitemap index; each child sitemap URL with its HTTP status and its URL count; and any post type you deliberately left out, with the reason. Update the card's sitemap line to done with the date and your session number.

## Out of scope

Search Console connection, Bing registration and submission, and the Rank Math Analytics dashboard (added to the same card this session, DSRD 3 section 6.4) are separate lines on the card and are not part of this brief.

*No em or en dashes in this file; checked before writing.*
