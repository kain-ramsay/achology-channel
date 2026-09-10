# RULING_AND_BRIEF: the link-label standard. Links visibly distinct everywhere, every theme-written label descriptive, and a gate check for the banned labels

**DOCUMENT TYPE:** ruling and brief, from Claude Chat, Session 356. **Date:** Thursday 10 September 2026.
**Authority:** Kain, live in the S356 sitting, adopting Nielsen Norman Group's guidance on writing hyperlinks (Marieke McCloskey, "Writing Hyperlinks: Salient, Descriptive, Start with Keyword", nngroup.com, still current).
**Owning documents, written this session:** DSRD 1 section 6.4 (the four-rule standard and the design half named), The Achology Base Voice item 13 (the copy craft), `content_gate_standards.json` (`banned_link_labels`, shared).
**Board card:** none of its own; site-wide, carried in the S356 handover until your lines land.
**Read this cold.**

---

## The standard, in one paragraph

A link looks like a link. Its text says what the reader gets when they follow it, names the thing, and puts the important words first, because people read the first two words. On one page the same words always go to the same place and different places never share their words. "Here", "click here", "read more", "learn more", "this page", "this article" are banned as link text.

## Three things for you

**One: links visibly distinct from body text, everywhere, ruled in Safari.** Render the site's in-body link treatment on the quote exemplar page with the page around it, options tabbed, one on screen at a time in the same position (standing rule 16), and put it to Kain. Underlined text in a colour that reads as a link is the evidence-backed default; what he approves goes into DSRD 7 by Chat at close from your RULING.

**Two: audit every link the theme writes itself.** Cards, the related-reading and related-paths blocks, the "All quotes from this book" and "All articles from this book" blocks, buttons, the footer, the header. Any label that is "Read more", "Learn more", "View all", "See all", "here" or a bare "More" is replaced by one that names the thing ("All book notes in Helping People", "Read the book note"); where a card carries a heading and a second "read more" link, the heading becomes the link and the second one goes. Bring the changed components to Kain rendered the same way, and file the RULING for DSRD 8.

**Three: the gate check.** `content_gate.py` reads `banned_link_labels` from the shared standards and fails any link in a body whose entire anchor text matches one, case-insensitive. Build it with the closing-question and practice checks already commissioned. Then run it across every published body on the install and report the count of hits by type, so Chat can scope a correction where one is needed.

## What comes back

The two RULINGs from the Safari sittings (link treatment; component labels), and one line when the gate check is in with the site-wide hit count.

OWED BACK: those. Nothing else.

*No em or en dashes in this file; checked before writing.*
