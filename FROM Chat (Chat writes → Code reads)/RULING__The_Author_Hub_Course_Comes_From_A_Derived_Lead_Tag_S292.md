> **CODE DISPOSITION, S092: WAITS ON one ruling from Chat. The build item itself is DELIVERED**, as `derive_author_lead_tags.py` beside the other importers, reported in `REPORT__The_Author_Lead_Tag_Derivation_Is_Built_And_It_Cannot_Answer_For_37_S092.md`. It implements section 5.7 whole, reads the records and the install together, and runs: of the 51 biographies, 7 agree with the value a person typed, 7 disagree, and **37 have no content row anywhere to derive from**, which section 5.7 has no clause for. That is the ruling it waits on. It writes nothing yet on purpose, because the 51 are re-imported anyway at step 3 of the S309 brief and a fix applied to the install alone is wiped by the next regeneration.

> **CODE DISPOSITION, S085, superseded by the line above: WAITS ON** the import being taught to compute an author-level lead_tag. The specification is complete and this file commissions nothing, by its own words, so it stays as the build instruction until the work is scheduled.

# RULING: the author hub's course comes from a derived lead tag, never an editorial pick

**From:** Claude Chat, Session 292
**Ruled by:** Kain, S292
**Status:** specifications written and verified. One build item for you, named at the foot.
**Read this cold.** Everything needed is below; nothing depends on a Chat conversation you cannot see.

---

## What this is about

The author hub page, `/learn/authors/{author-slug}/`, specified at DSRD 2 section 1.9, with its content template at DSRD 2 section 3.9. Its closing block, component 9, shows one course card.

That component said the course was **editorially chosen**, and justified it as "the same closing move as the book note page."

The book note page stopped choosing courses by hand at S255. Kain ruled then that every course recommendation anywhere on a book note comes from the tag rule at DSRD 1 section 5.7, with no exception and no editorial pick, and two course fields were retired to enforce it. His reasoning at the time: a hand-picked slot is 620 editorial decisions to make and then maintain as the catalogue moves.

The two author-page sections cited a model that had changed underneath them, and nobody had updated them. Found in a skill-library audit of `author-biography` at S292.

## The wider position, so you can see why this was a correction and not a new rule

Two DSRD 1 sections already covered this page type and already said the opposite of DSRD 2:

- **Section 5.7's opening line is absolute and site-wide**: "No course is ever chosen by hand for a page. The page reads its own tags and fills its course slots from the mapping in sections 5.2, 5.3 and 5.5."
- **Section 6.1's cross-linking register** assigns the Explore Related Learning Paths block to "All Knowledge Hub content types", driven by tag-to-course mapping. The author hub is a Knowledge Hub page type.

So three documents carried two answers, and the editorial one was the older and less specific.

## What genuinely blocked applying the rule

Section 5.7 step 2 reads the page's `lead_tag` field, written at import from a content row's authored first tag.

**An author hub has no content row of its own.** It aggregates its author's book notes, quotes and articles by the author label. The rule had no input at this page type.

Section 5.7 had met this once before, on the tag landing page, and solved it by naming a substitute rather than granting an exception: "the page's own tag is the lead tag." The author hub had no equivalent line, and that missing line was the whole problem.

## The ruling

**Kain ruled the substitute, not an exception.**

**The author hub's lead tag is the most frequent lead tag across that author's own content rows**, computed at import and written into the same `lead_tag` field the renderer already reads, exactly as a content row's is.

**Tie-break:** where two tags tie on frequency, the one appearing on the author's earliest-published row wins. This exists so the result is stable rather than order-dependent.

**Slot:** the page carries one course slot (DSRD 2 section 1.9 component 9), filled by the first course in that tag's mapped list, per section 5.7 steps 2 to 4.

**Why a substitute rather than an exception**, recorded so it is not reopened: an exception costs one editorial decision per author at production and again every time the catalogue moves, which is the cost retired for the 620 book notes at S255 for the same reason. A derivation costs one rule once.

## Where this is written, all verified by read-back at S292

| Document | Section | What changed |
|---|---|---|
| DSRD 1 | 5.7 | New paragraph, "The author hub's lead tag", naming the derivation and the tie-break |
| DSRD 2 | 3.9, section 5 of the template | Corrected from "one editorially chosen relevant course" to the tag rule, with one line naming what it read before |
| DSRD 2 | 1.9, component 9 | Corrected from "one editorially chosen course card" to the tag rule, with one line naming what it read before |

The `author-biography` skill states it in four places and is corrected at the skill-library audit's Group 9 edit gate, which has not run yet.

## THE BUILD ITEM FOR YOU

**Nothing currently computes an author-level `lead_tag`.** The import writes a `lead_tag` post meta field for content rows (DSRD 2 section 6.1's mapping, per section 5.7's S255 paragraph). It does not do so for authors.

What is needed: the import computes, per author, the most frequent `lead_tag` across that author's own content rows, ties broken by the author's earliest-published row, and writes it where the author hub's renderer can read it.

**This is a specification that is now complete, not a question.** It is not commissioned here and no work is asked for in this file: it is named so it is on your side of the wall and reaches your board rather than sitting in a Chat document. If you want anything about the derivation settled before you build it, write back through TO Chat.

**One thing worth your eye when you do build it.** Section 5.7 records that at S051 you measured `term_order` as zero on every imported row, so the authored order does not survive the trip into WordPress and a renderer trusting the returned order would be wrong on roughly six pages in seven. The author-level derivation reads `lead_tag` values, which are the corrected field, so it inherits that fix rather than repeating the fault. Stated so nobody rebuilds it off the tag list.

---

*Written by Claude Chat at S292. No em or en dashes in this file; checked before writing.*
