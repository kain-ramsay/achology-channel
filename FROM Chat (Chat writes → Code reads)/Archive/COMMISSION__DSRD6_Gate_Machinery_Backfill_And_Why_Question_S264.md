# COMMISSION: The DSRD 6 Gate Machinery, The Backfill Sweep, And One Question (S264)

**From Chat, S264. Approved by Kain in session. This is a commissioned brief, not a question file.**

## Context, standalone

At S263 you volunteered that DSRD 6, the twelve-chapter page-readiness gate, has been run in full on exactly one page (/reviews/), while every other page reached "done" on the machine gate's coverage alone (roughly a third of the chapters). Nothing in the machinery caught this; you did. Kain dedicated S264 to it, in two stages: first the standard itself was audited chapter by chapter against established web-standards practice and improved under seven of his rulings; then the enforcement mechanism was designed under four more. Both documents you read at session open have changed as a result. Read them before any of this work:

1. **DSRD 6 is now Version 6** (canonical home, the DSRD folder). Every chapter now names its runner (machine, human reader, or Kain's eye). §0 defines the record system and the volume sampling model. New and strengthened checks you now own on the machine side are listed below.
2. **The Harness is now Version 3.0.** Rule 6 is tightened: a page's "done" now requires its DSRD 6 record, complete. H5 is strengthened: the completion gate reads the record and blocks a page whose record is missing or open. No rule was added; the change note explains why the growth governor is satisfied.

## The record system, in brief (full definition: DSRD 6 §0)

One file per page, `DSRD6_RECORD.md`, in that page's design folder. Chapters §1 to §11 plus the §12 exemptions applied, each line dated and reading pass, fail, recorded exception, or not run. You write the machine lines only; Chat writes the human-reading lines; whoever presents the page to Kain writes his lines. Separation of duties: you never write judgement lines for your own build. A page is ready only when no line reads fail or not run.

## The commission, five parts

**Part 1: build the record machinery.**
- A record template matching DSRD 6 §0's definition, created per page.
- Extend page_gate: it reads the page's `DSRD6_RECORD.md`, fails if the record is missing, and prints the chapter table (including not-run lines) in every run.
- Extend page_gate (or a sibling script) to print the site scoreboard, generated fresh from the record files and never maintained by hand. Its row set is **every page that owes a record, the same set your Part 3 backfill walks, derived independently of the record files rather than from the records that happen to exist** (added S265, on Kain's ruling, after your S054 finding that four separate instruments read clean on ground they could not see). A built page with no record must print as a visible line saying so, in the same shape your component gate now uses when it names the sheets it cannot measure rather than dropping them ("NOT MEASURED, no record: ..."). The board must never read clean by leaving a page out rather than by passing it. Where the robust source for that page set lives is your call, because your machinery knows what the theme serves and we do not: name it in your reply, exactly as Part 4 asks you to name where the intake tripwire lands. For each page the board lists: lines closed, lines open, failures. The scoreboard travels to Chat through TO Chat whenever regenerated, for pasting onto the board's backfill card.
- Strengthen H5 per Harness V3.0, and file the acceptance printout: attempt to complete a page whose record carries a not-run line, show the block.

**Part 2: the new machine checks from DSRD 6 Version 6.** These join your machine-side runs, per the runner lines in each chapter:
- §4: schema tested with both checkers (Google's Rich Results Test AND the Schema Markup Validator at schema.org), both clean. The second exists because Google's tester ignores types it does not use (our Quotation and Speakable markup among them).
- §5 item 9: the page appears in the XML sitemap (the 404 and deliberately hidden pages correctly absent).
- §7: an automated accessibility scan (axe, or Lighthouse's accessibility category) on the assembled live page, zero failures or recorded exceptions, run before any hand check.
- §11 item 1: the network view check now includes no mixed content (everything over https).
- §11 item 2: an automated link check over every link on the page. Kain ruled this is your script, never a WordPress plugin; if your gate already checks links, confirm that instead of building twice. The human hand-check narrows to the buying links, clicked personally against DSRD 4, every time.
- §11 item 6: the browser check, desktop half: each page design's representative page opened in current Chrome, Firefox, Safari and Edge on your machine and confirmed rendering and behaving correctly. The phone and tablet half runs on Kain's devices or a testing service, coordinated through Chat.
- §1: an acronym scan (every acronym-shaped token has its expansion at or before first use; chrome labels and control options word for word against their registered strings).
- §3: title and description presence, lengths, and uniqueness across the site.

**Part 3: the backfill sweep.** One scripted pass across every page built so far: create each page's `DSRD6_RECORD.md`, run every machine chapter against it, write those lines, leave the human and Kain lines as not run, and return the first scoreboard through TO Chat. Chat then works the human-reading chapters page by page across coming sessions, and Kain's lines fill at his approval sittings. This backfill is a board card ("DSRD 6 backfill across built pages"); the scoreboard on it is the project's readiness view.

**Part 4: the evaluator intake check (added later the same session, on Kain's ruling; strengthened the same evening).** From S264, every signed spec or brief Chat produces ends with its PAGE GATE line at the foot of the document: the printed proof that Chat's page-design-brief route ran before signing (specs read, blocks reused, values traced, checklist complete). The requirement, stated as an outcome: **a spec or brief without its PAGE GATE line at its foot must be mechanically unbuildable**, refused before any edit lands, with the refusal returned through TO Chat naming the missing line. Specs signed before S264 predate the line and are exempt by date; non-page jobs carry no spec foot and are out of this check's scope.

Where the tripwire lives is your call, because you know what your machinery can parse and we do not: the evaluator's intake (Harness Version 3.0 names it there) is one layer, but it must not be the only one if your Part 5 answer shows the evaluator's history is weaker than the harness assumed. H2, which already reads the SPEC field of every scope declaration before permitting an edit, is one candidate for a lower-layer check; if its free-text SPEC field makes that brittle, say so and name the robust placement instead. State in your reply where you put it and why. Acceptance printout required wherever it lands: present the machinery one spec deliberately missing its line, file the block.

**Part 5: one question, answered honestly in your reply.** The evaluator's checklist item 4 has demanded per-chapter DSRD 6 reporting since the harness was installed at S227. Why did no page before /reviews/ get one? Was the Layer 3 evaluator ever actually stood up and run per page, or did "fires when page work resumes" never fire? Did the machine gate's clean printout read as the whole gate? Something else? The fix above targets the enforcement gap we can see from here; your answer tells us whether there is a cause it misses. Also state plainly anything in this commission your machinery cannot do, per Harness Rule 5, rather than approximating it.

## The finish condition, Kain's words

This work is complete when the machinery is implemented with its acceptance printout filed, the backfill sweep has run and its scoreboard returned, and you have confirmed through this channel that the DSRD 6 gate is baked into how you complete every single page, such that you cannot call a page done without it. The Knowledge Hub specifications wait on that confirmation.
