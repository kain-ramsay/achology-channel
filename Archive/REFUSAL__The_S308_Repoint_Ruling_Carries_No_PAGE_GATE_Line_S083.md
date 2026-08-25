> **CHAT DISPOSITION, S308: ACTED ON AND ARCHIVED.** The DOCUMENT TYPE line is now at the head of `ASK__The_Facts_Only_The_Install_Holds_S308_Board_Audit.md` (ask and rulings, not a page spec). The repoint can proceed on the same file. JavaScript error noted as unexplained. Board cards moved: none.

# REFUSAL: the S308 repoint ruling cannot be built as written, and here is the one line it needs

**From:** Claude Code, Session 83. **Date:** 25 August 2026.
**Refuses:** `ASK__The_Facts_Only_The_Install_Holds_S308_Board_Audit.md`, section 3.
**Returned through the channel** because the Harness requires a refusal to travel this way rather than be worked around.

---

## What was asked, and it is accepted on its merits

Section 3 rules that replacing the duplicated enquiries panel markup in `page-about.php` and `template-our-people.php` with a call to `achology_warm_room()` is component work under DSRD 8 §12.3 step three, not a page edit, and that no page spec is needed.

**No argument with any of that.** It is the right call and it is what I asked for.

## Why the edit would not land

The scope wall refuses it, and it is right to.

> H2 PAGE GATE INTAKE: blocked. The spec governing this page carries no PAGE GATE line at its foot.
> (A document with no DOCUMENT TYPE line is treated as a page spec, ruled by Kain S266: forgetting to declare gets you refused, never waved through.)
> ASK__The_Facts_Only_The_Install_Holds_S308_Board_Audit.md

**The file has no DOCUMENT TYPE line**, so the machinery reads it as a page spec, and a page spec without its PAGE GATE line at the foot is mechanically unbuildable. The ruling's own words, that this is component work and not a page edit, are exactly the thing the missing line would have told the machine.

**This is not mine to fix by editing your document**, and the Harness says so in as many words.

## The one line it needs

Either a DOCUMENT TYPE line declaring the file is an ask and a ruling rather than a page spec, or the section reissued as its own file carrying that line. Whichever is cheaper at your end.

**Both templates are marked "waiting on the DOCUMENT TYPE line" and nothing else on the S308 file is held up by this.**

## Nothing is broken while it waits

The stopgap enqueue shipped at v0.100.0 keeps both pages correct: `functions.php` loads `warm-room.css` for About and Our People explicitly, and both pages were opened and looked at after deploy, not only measured. The component styles gate passes on all five standing pages.

The only cost of the wait is that the duplication survives, which is a tidiness debt rather than a live fault, and the gate will catch it the moment it becomes one.

## The other two lines from section 3, answered

**`/enquiries/`.** Understood: PRD row Pr1.31, never built, on the Commercial Page Designs card, not mine to invent. The button stays pointed at the address it will have. Removed from my open-faults list.

**The JavaScript error on every page.** Not identified. What is ruled out, measured: every one of the theme's own script files parses clean, and so does every third-party script on the page. The remaining candidates are the inline blocks, and the four my check flagged are `application/ld+json` data rather than executable script, so they are false positives from my own test rather than the cause. Recorded as unexplained rather than guessed at. It breaks nothing visible on any page checked.

*No em or en dashes in this file; checked before writing.*
