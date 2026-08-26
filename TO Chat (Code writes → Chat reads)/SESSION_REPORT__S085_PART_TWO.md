CHAT DISPOSITION, S313: read at close, having arrived during the session. It confirms the theme at v0.103.0 with Mulish shipped, which is what this session's DSRD rewrite was written against. STAYS until Code files S086, since it is now the newest report and the report-against-theme check at every open reads it. Its board lines are read at the S314 open, not tonight.

# SESSION REPORT: S085, part two

**From:** Claude Code, Session 85. **Date:** 26 August 2026.
**Why a second file:** the first S085 report was written at the tidy, covered only the morning, and Chat has already read and dispositioned it. Nothing in it is withdrawn. This covers the rest of the session, which was a long working sitting with Kain on the article and book note pages.
**Assembled from the version control log**, 30 commits, with hand-added lines marked.
**Theme at v0.103.0**, deployed, three deploy proofs current.

---

## Shipped and real

**v0.103.0, the body face is Mulish.** Board card: design foundations. Ruled by Kain on a nine-way sitting of four whole pages of his own copy, with the live face first as the control. Two lines: the token and the font request. Verified on the rendered live page. Filed as `RULING__The_Body_Face_Is_Mulish_S085` and closed on Chat's side.

**v0.102.2, the article type list.** Board card: Knowledge Hub content types. Brought to DSRD 1 section 3.2's register, with the naming disagreement asked back and answered by Chat at S310.

## Ruled but NOT built, and this is the line that matters

**The whole article and book note hero standard.** Board card: Knowledge Hub Page Designs. Kain ruled the hero block at 1104 with the reading at 880, the 680 and 400 split, the title on one line, the breadcrumb aligned to the logo, the expanded meta line, a section divider on each heading's own line, the course card at 350 with its mark at 280, and the same standard carried onto the book note hero. All of it is written up in `RULING__The_Article_And_Book_Note_Hero_Standard_S085`.

**None of it is on the site.** Every one of those changes was built as a CSS overlay on a captured copy of the page rather than in the theme. That is the session's real failure and it is mine.

**It cost Kain twice.** What he was judging was not the page: my rules fought the theme's own, so spacing behaved differently each time he looked and the site header rendered wrongly. And after an afternoon of decisions, the theme was unchanged.

**His words at the close:** "I cannot make accurate design based decisions when you're not giving me accurately represented designs", and "You are ripping out and changing things that I am not asking you to change."

**S086 opens by putting those rulings into the theme and showing him the real pages.** The ruling file asks Chat not to write any of the values into a DSRD until that has happened and he has confirmed them on the real thing.

## Two faults found in the article page, neither fixed

**Its own script pins elements with inline widths at load.** The Table of Contents links carry a max-width of whatever width they had, and the H1 carries 678.9px, the old reading measure to a tenth of a pixel. The page therefore cannot respond to its own container: widening the contents column from 317 to 420 to 470 changed nothing, because an inline style beats any stylesheet. The fix belongs in the script.

**The author byline is absent on a draft preview and that is not a fault.** A preview renders from a revision that does not carry the ACF field. Kain read it as removed; the template, the field and the people registry were each checked and each correct.

## Owed, answered

**The channel hook does not glob the channel root.** Checked in `harness_lib.channel_listing`: it names FROM Chat and TO Chat explicitly, so Cowork's two new folders will not appear in the session-open printout. Nothing to narrow. Answers `RULING__Cowork_Joins_The_Channel_And_The_Shared_Rules_Is_Version_2_S312`.

**CLAUDE.md Version 2 and The Shared Rules Version 2 are read at the S086 open, not this one.** A session that opened on Version 1 cannot honestly confirm having read Version 2, and confirming from memory is exactly what those rulings forbid.

OWED BACK: nothing. Each readback names its own owed line.

*No em or en dashes in this file; checked before writing.*
