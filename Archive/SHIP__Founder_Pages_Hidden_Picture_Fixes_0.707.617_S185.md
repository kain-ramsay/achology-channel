SHIP record, theme session S185, 27 October 2026. Asks nothing; filed straight to the Archive.

**0.707.617, founder pages (Founders' Letter, Manifesto, Code of Ethics), hidden fixes only, nothing visible changed.**
- The header picture on each page (the founders' portrait, the Manifesto document, the Code of Ethics handbook) now loads first: no lazy loading, and it carries the high fetch priority. The faint title word picture keeps that priority only on pages with no larger header picture. template-policy.php.
- The Manifesto document is sent as WebP (same pixels as the JPG master, which stays in the theme for the record). template-policy.php swaps a document's .jpg for its .webp twin where one exists.
- Why: the page gate's DSRD 6 section 11 lines (largest picture above the fold, picture format) failed on all three pages; they now pass.

**Spacing check (Kain S178 rule) on the page as it stands, 0.707.617:** page_gate hairline spacing, spacing scale, header to content and gutters pass at desktop, tablet and phone on all three pages (36 lines, all PASS).

**Gate lines still open, not Code's to change:**
- Founders' Letter Rank Math 84, Code of Ethics 89 (bar 90): metadata words, Chat.
- Code of Ethics: CPD used before it is spelled out (the related question "Can I Use Achology Courses for CPD Hours?"): copy, Chat.
- Code of Ethics: the Rogers quote's name line is mid grey, 3.2 to 1 against white (axe colour contrast). The signed book note quote uses soft grey for the same line; changing it is a visible colour change, so it goes to Kain as a round, not done here.
- Manifesto: the enlarged document in the reading window has no srcset (it is the full size view on purpose).
- keyword-density and orphan lines: instrument limits (template body; the crawl missed pages).
- Owed by Chat still: the Code of Ethics repeats its opening line word for word (TO Chat RULING__Founder_Pages_Opening_Buttons_Under_The_Words_S181).

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
