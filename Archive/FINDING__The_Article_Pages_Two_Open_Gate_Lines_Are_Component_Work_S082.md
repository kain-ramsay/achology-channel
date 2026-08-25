**DISPOSITIONED S306: read in full. Chapters 5 and 7 addressed in RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md (grey-text sweep commissioned, orange button put to Kain in Safari, meta-description tracking noted). Board card: Author Biography Articles / Knowledge Hub Page Designs.**

# FINDING: the article template's readiness record is run, and its two failing lines are not the template's

**From:** Claude Code, Session 82. **Date:** 25 August 2026.
**Record:** `DSRD 6 Records (pages with no design folder yet)/Single Article/DSRD6_RECORD.md`.
**Measured against:** DSRD 6 Version 7, page_gate v8, axe 4.10.2, on the live page.
**Board card:** Knowledge Hub Page Designs, line 1.
**Reads with:** `RULING__The_Article_Page_Rulings_S082.md`, which records the page being signed.

---

## What the run says

Nine of the eleven chapters pass their machine half. **Ten of the eleven are split between a machine and a human runner**, so a machine pass cannot close one on its own; those chapters stay open waiting on Chat and on Kain, which is the separation of duties DSRD 6 §0 requires and not a gap in the work.

Two chapters fail on their machine half. **Neither failure is inside this template**, and both were opened out node by node rather than left as the one-line summary the sweep writes, because that summary is not actionable and the record is what Chat and Kain read.

**One line was closed by fixing my own tooling rather than the page.** §11 was failing as "Firefox could not start", which was Playwright's Firefox not being installed on this machine. Installed, re-run, and the chapter's machine half now passes five checks. Recording it because a tooling failure sitting in a page's record reads exactly like a page failure, and this one had been doing so since 24 August.

## Failure 1: §3, the metadata. Content, not template.

The meta description measures **170 characters** against DSRD 6 §3.2's limit. The meta title passes at 47.

This is the specimen article's own Rank Math description, written into its content record, so it belongs to the content production side rather than to the page. **Nothing in the template can close it.** Flagging it rather than trimming it, because published words arrive through the channel (Harness Rule 8) and are not Code's to edit.

**Worth checking at the same time:** if this record's description ran long, others may have. It is one line of a query against the eighteen imported instructor articles and the 41 biographies about to be imported, and it is cheaper to find now than after publication.

## Failure 2: §7, the accessibility scan. Two components, neither of them this page.

One rule, colour-contrast, on **seven nodes**. Every one was read from axe directly. Four sit inside the course card, twice over because the page renders two of them, and one is the site-wide header.

| Node | Measured | Needs | Owner |
|---|---|---|---|
| `.site-header__cta` (the Sign In button) | 3.16, #ED6922 on white, 13px | 4.5 | the site-wide header |
| `.card__price-qualifier` ("for Lifetime Access") | 3.18, #8A9199 on white, 13px | 4.5 | the course card, on both cards |
| `.card__guarantee-pill` ("Money Back Guarantee") | 2.89, #8A9199 on #F3F4F5, 11px | 4.5 | the course card, on both cards |
| `.btn--enrol` ("Enrol Now") | 3.16, white on #ED6922, 14px | 4.5 | the course card, on both cards |

**The article page's own copy, chrome and foot raise nothing.**

### Why Code has not simply fixed them

Both are components that render on many pages. Harness Rule 3 puts a change reaching more than one page behind a signed sweep brief, and Rule 4 puts a component's values behind its approved prototype and build sheet, not behind whichever page happens to notice a fault. Fixing them inside this page's change set would have been the exact failure both rules exist to stop.

### Two of the three are the same fault, and it has a name

`.card__price-qualifier` and `.card__guarantee-pill` are both **mid grey #8A9199 carrying words a reader is meant to read**. That is the fault Kain already ruled on at S280, in `RULING__Supporting_Lines_Move_To_The_AA_Safe_Grey_S280.md`: supporting lines move to the AA-safe soft grey, because DSRD 7 §1.1 is explicit that mid grey is "never used for anything a reader needs". The ruling's mechanical pass named `.kh-section__subtext` "and every sibling supporting-line style"; these two are siblings by that description and were not swept. **So this is an unfinished ruling rather than a new decision**, and the same sweep is the fix.

`.btn--enrol` is different and is genuinely a decision. White on the brand orange is 3.16, and the brand orange is Kain's. The choices are a darker orange for button grounds, a heavier or larger label, or a recorded exception under DSRD 6 §0 with his approval. **None of those is Code's to take**, and the same white-on-orange appears on the enquiries panel's own button and on the site header's, so it is a site-wide question rather than a card one.

### What this blocks, and what it does not

It does not block the article template, which Kain has signed. It does block **every page that renders a course card or the site header from ever closing §7**, which is most of the site, so it is worth taking as its own piece of work rather than meeting it again on each page's gate.

## What Code suggests, and it is Chat's and Kain's to rule

1. **Sweep the two mid grey supporting lines to the soft grey**, as the completion of the S280 ruling rather than as a new one. A signed sweep brief naming the course card would let it run.
2. **Put the white-on-orange button to Kain** as one question with rendered options, since it reaches the card, the header and the enquiries panel together.
3. **Check the meta description length across the imported content**, before the 41 biographies publish rather than after.

*No em or en dashes in this file; checked before writing.*
