First line of need: Chat, write Kain's S162 simplifications of the hero's date line, the contents panel and the section titles into the owning documents for the article, book note, quote page and workbook page.

# RULING: the date line, the contents panel and the section titles, simplified (theme session, S162)

**From:** Claude Code, theme session S162, 13 October 2026. **Ruled by:** Kain, in the sitting, on the rendered pages in Safari (`previews/hero-s162/` in the theme folder). **Session:** theme. **Board card:** the four content page templates. **Read from the vault first:** none fit. Follows RULING__Hero_Direction_Soft_Light_Picked_S162.

## 1. The date line carries the word count, not the type's home (Kain: "take the word count from the article's table of contents, and place that where currently it says articles at Achology")

- Article: "1 October 2026 · 7 Min Read · 1,294 words". Book note: the same, with "View on Goodreads" kept before the count. Quote: "24 September 2026 · 4 Min Read · 700 words".
- The word count is the contents panel's own number, read, never typed. "Articles at Achology", "Book Notes at Achology" and "Wise Quotes at Achology" leave the line. (The breadcrumb still links to each type's list.)
- **The workbook's banner has no date line** (Kain: "take it out for now, then we'll figure out where we're going to place that once we get back to designing this actual page"): no date, reading time or "Practical Workbooks". Where it lives is open, for the workbook page's design.

## 2. The contents panel loses the line under its heading (Kain: "our goal here is to lose the line underneath table of contents completely")

"8 sections · 1,294 words" goes on all three page types: the sections are evident, and the words moved to the date line.

## 3. One device for the section titles, no numbers (Kain: "we don't have numbers above the section titles ... place the Achology bubble logo subtly with a layer of transparency centralised behind the first word in each title, edging its way out of the container a little bit ... we build a layer of standardisation in across all of the different articles")

- The small orange numbers above the section titles on book notes and quote pages are removed (they were counters in book-note.css and quote.css).
- A faint Achology bubble mark (the theme's 176 wide mark, about 12 per cent strength, 84 wide) stands behind the first word of every section title in the writing, centred on it and reaching a little out past the writing's left edge. The same on articles, book notes and quote pages.
- **The contents list's own 01, 02 numbers go too** (Kain: "yes"), so the three page types match; the entries take the whole row, as the article's already did.
- Built as a small server-side wrap of each section title's first word, so it holds on every page that is imported; a title that opens with a tag is left as it is.

## 3A. The contents panel's lines (Kain, S162: "the behind option is really quite nice ... the ecology bubble needs to be a lot smaller ... we need to lose the ecology bubble that's kind of popping in the bottom of the table of contents block")

- Four options were rendered (marker, behind, on the rail, quiet); Kain chose **behind**. The card's bottom hairline, the thin rail beside the list and the faint large watermark at the foot of the contents are removed. The entry being read has a small Achology bubble (about 30 wide, faint) behind its first word, kept inside the panel (a first try reached past the panel's edge and was cut off). It follows the reading, in place of the orange bar.

## 3B. The foot is full width, with no side panel (Kain, S162: "at the bottom of each page ... course cards and explore more articles ... consume the whole container without a side panel ... those two bottom sections underneath the actual article are full container width and don't come with a side panel")

- The side panel ends where the reading ends, with its last item (the Amazon button on book notes and quote pages) at the foot of the reading. The author row (name and share icons), "Explore More ..." and "Ready to Take Your Learning Further?" with its course cards then run the whole 984 container, with no panel beside them.
- **This reverses Kain's S146 ruling** that on a quote page the panel floats down to the hairline closing "Explore More Quote Articles" and runs across the right column; the panel's closing lines (knowledge-hub.js "0b" and the `--to-close` rules) go with it.
- The small number above "Explore More ..." titles on book notes and quote pages goes too (the same numbers as the section titles).

## 4. Also confirmed, S162

The hero list as a set, the 984 container, and the right-hand floating column staying: "I 100 per cent approve the container width. Um, I also think we still have opportunity to keep the right-hand floating column in place." Next, Kain wants the other components on these pages brought into the same alignment, one by one.

OWED BACK: the owning documents updated (DSRD 9 sections 22, 32, 37 and the quote page's), and a note in FROM Chat for the theme session when done.

*No em or en dashes in this file; checked before writing.*
