**For Chat. What this needs from you:** rewrite the Reading progress line row in COMPONENT_REGISTRY.md to Kain's pick, with its home files and the pages that switch it on (below), and its dated line in DSRD 8. For the theme session.

# RULING: the reading line is one site component, the Knowledge Hub line (Kain, Code's founder pages sitting, S181, 26 October 2026)

**Kain's words:** "Yes, the Knowledge Hub line for the whole site." Chosen in the shared Change Viewer from the site's two existing lines, each copied exactly from its own code and shown on an article, a Help answer and the Founders' Letter (previews/components-s181, round-reading-line.js; picks in previews/components-s181/PICKS.md). The first pick under the components register (COMPONENT_REGISTRY.md, "Shared features: one home each").

**The component.** The Knowledge Hub line exactly as signed (S147 tab 2 of four; 1px at S163): brand orange on a hairline-grey track over the header's bottom hairline, filling as the writing is read, empty while the writing is below the header and full once its last line is on screen. Note for the row: its current text says "2px"; the signed and live value is 1px (Kain S163, "subtler").

**For the registry row:**
- Home files: reading-line.css and reading-line.js (theme root). Class prefix: `reading-line`. No other stylesheet or script may draw a reading line; the old `kh-progress` and `help-progress` classes are retired.
- Switched on by: functions.php, which loads both files on single articles, book notes, quote pages and workbooks now, and single Help answers once they join (below). reading-line.js names each page kind's writing once (its WRITING list).

**Built so far (theme commit d1fee49b, not yet deployed):** the component on articles, book notes, quote pages and workbooks, with the old copy removed from knowledge-hub.css and knowledge-hub.js. Measured on a mirror of the build site at 1280 and 390 on an article, a book note and a quote page: place, size and colours identical to the line live today (the fill varied by the same few pixels between two loads of the live page itself, from pictures loading).

**Next:** the Help answer page joins the component and loses its own 4px top-edge line (help.css touch 1 and the bar in help-article.js, from Kain's S180 Help answer touches), agreed first with the Help session working in help.css. That is a visible change on every Help answer, by Kain's pick: the thick top line becomes the thin line at the header's foot. Whether the founder pages carry a reading line at all is a separate question for Kain, not taken here.

OWED BACK: the registry row and the DSRD 8 line, dated.

*No em or en dashes in this file; checked before writing.*
