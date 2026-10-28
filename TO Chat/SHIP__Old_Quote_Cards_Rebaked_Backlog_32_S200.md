**For Chat. What this needs from you:** strike Backlog: Code line 32 on the board; nothing else.

# SHIP: the 268 old quote cards re-baked at the current design (Code S200, theme side session, 28 October 2026)

**Authority.** Kain's go in the sitting, "yes please do", on Backlog: Code line 32 (RULING__Signed_Lines_Written_And_Three_Gate_Rulings_S425: "re-baking them at the current design is now Backlog: Code line 32 (theme session)"). The card design was not touched: every card was drawn by the theme's own card maker from the card already on the page.

**What changed.**
- **Re-baked: 268.** Every published quote page that still carried the old card design (a550389032b5) now carries a card at the current design (cbbdd1cf055c): the share picture (WebP, through the library's one door) and the Download picture (the 2400 by 1260 JPG), each read back on the install, the page stamped with the design it was baked against.
- **Repointed: 268.** Each page's Download now hands out its new JPG. Read back across the install: 293 of 293 published quote pages stamped cbbdd1cf055c, 293 of 293 Download files present on disk. Checked on the build site on helping-is-not-about-fixing: its share picture and its Download are the new files.
- **Moved to holding: 268.** The old Download JPGs are in the dated holding folder 2026-10-28-old-design-quote-cards beside the S184 one, outside the web root, with MANIFEST.md5 (268 of 268 checksums verified after the move). Nothing deleted.
- **The Bin.** The 268 replaced share pictures went to the Media Library Bin through the theme, as designed; the Bin now carries 275 items, 26.1 MB, for Kain to empty when he chooses.

**The media gate after:** `old quote card set 0, 0.0 MB`, `loose files 0`, `not used anywhere 0`, `duplicate groups 0`, and the report ends CLEAN.

**One register line.** make_quote_cards.py was re-hashed in H9's reviewed register (theme commit 3ad4b89a, pushed). Its one change since its S132 review was the local browser launch (S167); no line that reaches the install moved.

**Noted, not fixed (no theme edit in this job).** Twice in the run the card maker's route into the host was answered from the host's page cache instead of the card page: one run stopped part way, and one page refused until the cache was purged. The card maker purges the cache only at the end of a run; a second run picked up every page. No wrong card reached the install, because every card is proved before it is written.

*No em or en dashes in this file; checked before writing.*
