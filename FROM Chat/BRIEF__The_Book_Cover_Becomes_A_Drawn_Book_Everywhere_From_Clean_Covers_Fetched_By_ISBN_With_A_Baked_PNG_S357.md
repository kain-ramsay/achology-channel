# BRIEF: the book cover becomes a drawn book, everywhere a cover appears, from clean covers fetched by ISBN, with a baked PNG for the places CSS cannot run

**DOCUMENT TYPE:** brief, from Claude Chat, Session 357. **Date:** Sunday 13 September 2026.
**Authority:** Kain, live in Chat: the web-sourced covers on the book note heroes "look terrible"; he wants each hero to "actually look like a book, rather than an image that's evidently been scraped from the web", automated, and the same on the book note cards, "at volume". Chat's shaping accepted in full. Signed here by Chat.
**Board card:** the book note page template card (Kain's second Safari look is pending on it); the card gains this as a line at close.
**Session type:** theme, with one factory step (the cover fetch).
**PAGE GATE:** the book note page is finished only when it passes DSRD 6 with its per-chapter record returned; this brief ends at Kain's Safari ruling on the rendered book and the bake running clean.
**Read this cold.**

---

## 1. The problem, in one line

Two faults compound: the cover files are low-quality scrapes, and they sit flat on the band. Fix both, and fix them once so every book note, present and future, gets it for nothing.

## 2. Half one: clean covers, fetched by ISBN

1. Read each book's ISBN from the master workbook (the Books tab, per DSRD 2 and `content-factory`). Where a record has no ISBN, list it; do not guess one.
2. Fetch the cover at the largest size from the Open Library Covers API (`covers.openlibrary.org`, by ISBN), falling back to the Google Books API where Open Library returns nothing. Both are built for this use; no scraping of retailer pages.
3. Store and process per DSRD 7 section 12 (format, sizing, naming): the fetched original kept, the served derivative produced by the image pipeline. Replace the current cover on each record's `cover_image` (or whatever the field is named in the contract; read it, do not assume).
4. Report: covers fetched, covers not found (with the book named), and the before-and-after file sizes.

## 3. Half two: the book is drawn, not pictured

1. **Build one component, `ach-book`**, in components.css and `shared-parts.php`, that takes a cover image and draws a three-dimensional book: the cover wrapped on the front, a spine, page edges and a soft shadow, all by CSS. The technique is Sébastien Castiel's `book-cover-3d` (MIT, `github.com/scastiel/book-cover-3d`; `getCssForSettings` exports plain CSS from a settings object). Read it, take the technique, write it in our tokens: no library dependency ships in the theme.
2. **The component is sealed** on the reading bar's rule (DSRD 8 section 26): a page passes only the cover image and its alt; the angle, thickness, shadow and radius are the component's, set once for the site, never per page. It draws at whatever size its container gives it, so the hero, the book note card (DSRD 8 section 6, the book note card variant), the Knowledge Hub homepage and the author biography's book list all use the one component at their own sizes.
3. **Under rule 16's render standard, the look is Kain's, ruled in Safari, tabbed.** Render the real book note hero and a populated six-card grid of real book notes (six different real titles and blurbs) at desktop, tablet and phone, with the book drawn; then tabs for the three variables only, one changing at a time: the angle (three options), the thickness (three), the shadow (three). Kain picks by eye. Until he has ruled, nothing ships.
4. Fold the ruling back per standing rule 16: prototype into the component's design folder, build sheet, RULING to TO Chat; Chat records it in DSRD 8 as section 31.

## 4. The bake, for the places CSS cannot run

The share image (OG), and anything that leaves the site, needs a flat picture. Run the same bake the quote card uses (DSRD 8 section 30): open each book note in the browser by script, photograph the drawn book at the OG size, stamp it with the component's design id, and store it as the record's share image. One pass over every book note on the install; the same pass on any new one at import. Publish nothing on the strength of it; `publish_gate.py` treats a stale stamp as it does for quotes.

## 5. Order

After the type sweep and the three imports in your tray, unless Kain says otherwise: this touches the same three page families the sweep is on, and two sweeps on one family at once is drift.

## 6. Acceptance criteria

Every book note record carries a fetched cover or is named as not found. One `ach-book` component, sealed, drawing on the hero, the book note card and every other place a cover shows, with no per-page values. Kain's Safari ruling on the tabbed render, folded back. The bake run clean over every book note with stamps. The book note page's DSRD 6 record updated.

## 7. What this brief does not authorise

Any per-book handmade image. Any cover scraped from a retailer page. Shipping the component before Kain's ruling. Touching the quote card's own bake.

OWED BACK: the fetch report; then the RULING from the Safari sitting; then the bake report.

*No em or en dashes in this file; checked before writing.*
