# BRIEF: the body and citation pass on the unpublished book notes, in batches of twenty

**From:** Claude Chat, Session 353. **Date:** Tuesday 8 September 2026.
**Harness:** the Cowork Production Harness at the root of the Content Production Factory folder. Read it first, then The Shared Rules, then this file.
**Job type:** correction to existing records, body edits permitted within the four fixes named below and nowhere else. This is the pass your S349 report named as the natural next job; Kain commissioned it at S353.
**Board card:** Book Notes.
**Order:** after `BRIEF__Bring_The_Masters_Title_Column_And_The_Unpublished_Records_To_The_Ruled_Title_Form_S353.md`, because that brief moves `post_title` on the same records and the two edits should not cross. Then this, before the 24-article plan.

---

## 1. Why these records and nothing else stands between them and a reader

Code measured the install at his S106: every instructor article, author biography and rescued article that is written is live. The whole remaining backlog is book notes and quote pages. The quote pages wait on a design sitting nobody but Kain can run. The book notes wait on nothing but this pass: your S349 work put the keyword and the demand evidence right on all of them, and each still fails the content gate on one to three body lines your brief did not let you touch.

## 2. The set

Every record in `Content Records/book-note/` whose page is not live on the install. Read the live list from the install itself (the REST API for the book note post type, the same route you used for the help answers at S351), never from a record's own `post_status`, which your S105 report proved is not a live indicator on this type. Match slugs; the unmatched records are the set. Name the count in your first report; Code's S106 close put it at 57 before his 25 published, so expect the low fifties.

## 3. The four fixes, and only these

For each record, run `content_gate.py <file> book-note` first and read the real failing lines. Then:

1. **Keyword verbatim in the opening tenth of the body.** The focus keyword is the book's title (Kain, S349, S350; now DSRD 2 section 3.1). Put it in the first paragraph as one natural clause, the way the published 92 carry it. Never bend a sentence to do it; if the title cannot sit naturally in the opening, name the record and leave it.
2. **One external link to the source.** In the body, one link to the book's or author's own reference page: the publisher's page for the book, the author's own site, or an encyclopaedic entry on the author or the book. Never an affiliate or shop link in the body; the Amazon addresses are fields, not citations. Where the record's Sourcing record already names such a page, use that one. Where no reputable page exists, name the record rather than linking to anything.
3. **Paragraphs over 120 words.** Split at the natural seam. No words added or removed by the split itself.
4. **Anything else the gate names on the body** that is mechanical in the same way (a five-sentence paragraph, a stray dash). Not the words, not the argument, not a heading.

**Density.** Where fix 1 lands the keyword in the opening and the gate still reads density under band, leave it and record the number; a lacing pass is not in this brief. Where a natural second mention exists in the close, take it, and no more.

## 4. What you must not do

- Do not change any heading, the section order, or a single fact. Where a fact looks wrong, name it in the report; the seventeen taught us that a body fault is Chat's escalation, not a Cowork rewrite.
- Do not touch `post_title` (the other S353 brief owns it), `rm_seo_title`, the slug or `demand_evidence`.
- Do not touch the published 92, and do not touch `stoicism-and-the-art-of-happiness`, which Kain closed at S349.
- Do not add the "No em or en dashes" declaration inside any record.

## 5. Batches and reporting

Twenty records per batch, gated as each finishes, with every record's final gate printout in its own Notes block. After each batch, one DONE in FROM Cowork: `DONE__Book_Notes_Body_Pass_Batch_N_S353.md`, carrying the list of records that now print GATE: PASS, the list that still fail with the exact failing line and why you left it, and the count against section 2's total. Report after each batch rather than at the end, so Code imports in waves; Chat carries each batch's list to him.

**Stop conditions.** A record that needs a fact changed, a heading changed, or a sentence rewritten to place the keyword is left and named. Two records in one batch stopping for the same reason means stop the batch and report; the pattern is Chat's.

OWED BACK: the batch DONE files, until the section 2 count is accounted for in full.

*No em or en dashes in this file; checked before writing.*
