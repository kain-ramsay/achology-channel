# BRIEF: the fifty instructor quote pages. Fix the twenty five that exist, draft the twenty five that do not.

**DOCUMENT TYPE:** brief, from Claude Chat, Session 345. **Date:** 6 September 2026.
**Signed by:** Kain, who commissioned this run directly from the board card in the S345 sitting, and who then ruled that the existing twenty five are brought to standard inside the same run rather than left behind.
**Board card:** 50 instructor book quote pages, from The Skilled Helper and The Ultimate Life Coaching Handbook.
**Harness:** the Cowork Production Harness, current version. Read The Shared Rules at the channel root, then the harness, then The Publish Ready Pipeline, the `rank-math-90` skill and the `quote-page` skill, then this file.
**Read this cold. Everything you need is below or named by its folder.**

---

## 1. What this run is, and why it is one run and not two

Fifty quote pages carrying Kain Ramsay's and Prof. Gerard Egan's own words from their two books. These are the highest-authority quotes on the site, because the authors are Achology's own instructors.

**The card said Chat would draft them. Kain has given them to you instead.** That is his call, made this session. The card is being corrected to match.

**Two jobs, deliberately in one run:**

- **Job A: bring the twenty five Ultimate Life Coaching Handbook records to the gate.** They exist in `Content Records/quote-page`, drafted at S300, and each still fails several content-gate lines.
- **Job B: draft the twenty five Skilled Helper records from scratch.** They do not exist. Their source rows are carried whole in section 5 below.

**Why together.** The twenty five that exist were drafted before the gate covered this type and were never measured. If Job B ran alone, the site would hold fifty instructor quote pages of which half are known to sit below standard, and the fault would be found later by someone reading a live page. Kain ruled them fixed inside this run for that reason.

## 2. Job A: the twenty five that exist

They are in `Content Records/quote-page`, quote IDs **Q07009 to Q07032 plus Q04251**, source book The Ultimate Life Coaching Handbook, author Kain Ramsay.

**What is already right, and must not be touched.** All twenty five carry a real `demand_evidence` field, each backed by a live search you ran at S342. All twenty five carry two to four outcome tags. Their `quote_text`, source attribution and author key are correct and verified. **Do not re-run stage 0 on these and do not change a quote's wording.**

**What is wrong, in your own S342 report's words:** several pre-existing faults remain on most of the twenty five, specifically **word count, reading ease (Flesch), keyword placement, and missing external links.** Those were outside that brief's scope and were reported rather than fixed. This brief owns them.

**The word count is the one to watch.** The standard is **300 to 400 words of original interpretive writing, and no tolerance is applied**, because DSRD 2 section 1.1 gives that as a range already. Two of these records were sampled after drafting at 284 and 220 words. The short beat in both was the second interpretation. **The quote itself is the source's words and is not counted.**

**One record is your exemplar.** Take **Q07026** first, alone. Bring it to a clean gate, then stop and report it before touching the other twenty four. If the fix pattern is wrong, it is wrong once.

**These twenty five are already on the install as drafts** (posts 35442 to 35466, imported at S342). Every record you change has to be re-imported by Code, so **list in your report exactly which records you changed**, and he re-imports only those.

## 3. Job B: the twenty five Skilled Helper records

Author **Gerard Egan**. Source book **The Skilled Helper**. Quote IDs **Q06984 to Q07008**, contiguous.

**A numbering correction you need before you start.** An earlier ask named the Skilled Helper block as Q07009 to Q07032 plus Q04251. That is wrong: that range is the Handbook's block, which sits immediately after. Code read the master at S088 and confirmed the Skilled Helper block is the twenty five below it, Q06984 to Q07008. The board card still carries the old numbering and is being corrected.

**Five constants, true on all twenty five, so they are stated once rather than repeated per row:**

- `quote_author`: Gerard Egan
- `source_book_title`: The Skilled Helper
- Recommended course: **The Skilled Helper Training Course (with Prof. Gerard Egan)**, DSRD 5's canonical name, copied exactly
- Source: book extraction, S186
- Verified: yes, checked verbatim against the source text at S186. **You do not re-verify these and you do not alter a word of any quote.**

**Take the shape from the existing twenty five, not from your own judgement.** The address pattern, the field set and the record layout are all already proven on the Handbook records that imported clean. Open one and copy its shape. Do not invent an address pattern.

**`source_book_note_address` points at the Skilled Helper book note**, which is live. Read its real address rather than constructing one.

## 4. The rules this type runs on, gathered so you do not have to hunt them

- **300 to 400 words**, hard, no tolerance. Interpretive writing only.
- **Hook, Book, Look, Took is the underlying shape and is never a visible heading.** The H1 is the only heading the writer creates, and it is descriptive. **The H1 is never the quote itself.**
- **Voice: Frederick S. Martín**, the generous illuminator, on the base voice.
- **`author` is `frederick-martin` on every row.** `quote_author` is whoever said the line. **They are different people and conflating them is a real failure this project has already made once.**
- **`image_quote_text` carries the full verified quote, always identical to `quote_text`. There is no character cap.** Kain ruled at S300 that a long quote steps the type size down rather than being cut.
- **Two to four outcome tags** from the 36 locked slugs (DSRD 1 section 5.1, ruled by Kain S342).
- **`quote_id` is the permanent ID from the master and is never renumbered.**
- **The new title rule, S345.** No vague or colloquial phrasing in any title, in any field. See `RULING__No_Vague_Or_Colloquial_Phrasing_In_Any_Title_S345.md` in this tray. It applies to all fifty.

**Three things in the source data that are faults, named so you do not reproduce them:**

1. **Two quotes carry a lost space before an opening quotation mark, in the master itself.** Q06985 reads `about"fixing,"` and Q07006 reads `accomplished"sometime or other"`. Both are extraction artefacts, not the author's text. **Write them correctly in the record**, with the space restored. Chat owes the same correction in the master and will make it.
2. **Three provisional slugs lost a word boundary** where punctuation was stripped: `...aboutfixing`, `...lifeenhancing`, `...madeup-rules`. **Do not use them.** Build clean slugs.
3. **The master's topic vocabulary is not the site's tag vocabulary.** It runs on twelve values (Coaching, Goal Setting, Empathy, Accountability, Relationships, People Skills, Values and Priorities, Being Human, Personal Development, Change, Self-Awareness, Objectivity). Use it only to understand what each quote is about. **The tags on the record come from the 36 locked slugs, never from this list.**

## 5. The twenty five Skilled Helper rows, carried whole

They live in the channel's old shared Archive, which is not on your road, so they are reproduced here rather than pointed at. Read from the `Quotes` tab of `Achology Master Books and Quotes.xlsx` by Code at S088. The `RELATED (curated IDs)` column is empty on all twenty five.

| ID | Quote | Master topic |
|---|---|---|
| Q06984 | Helping is first and foremost about the person seeking help. | Coaching |
| Q06985 | Helping is not just about "fixing," but about enabling clients to design and redesign their lives. | Coaching |
| Q06986 | Most clients, like the rest of us, have resources they are not using or opportunities they are not developing. | Personal Development |
| Q06987 | Helping at its best provides clients with tools to become more effective self-helpers. | Coaching |
| Q06988 | Clients with hope are more likely to achieve life-enhancing goals. | Goal Setting |
| Q06989 | It is essential to help clients become agents of change in their own lives. | Change |
| Q06990 | In the end the quality of the client's participation in the therapeutic endeavor is the major determinant of outcome. | Accountability |
| Q06991 | Respect for clients is the foundation on which all helping interventions are built. | Relationships |
| Q06992 | Respect is both gracious and tough-minded. | Values and Priorities |
| Q06993 | Empathy is also a commitment to understand the dissonance between the client's point of view and reality. | Empathy |
| Q06994 | In my view, clients who are never invited to challenge themselves are being shortchanged. | Accountability |
| Q06995 | There are many made-up rules, but life has its own rules and we as therapists can help clients explore them. | Being Human |
| Q06996 | A skilled helper is more than a technician, even a very competent technician. | Coaching |
| Q06997 | Helping others is more than a job, more than a career. | Coaching |
| Q06998 | Success is defined as life-enhancing outcomes for clients. | Goal Setting |
| Q06999 | Support without challenge can be hollow just as challenge without support can be abrasive. | People Skills |
| Q07000 | Blind spots are part of the human condition. | Self-Awareness |
| Q07001 | Challenge only after you have spent time and effort building a relationship with your client. | Relationships |
| Q07002 | Empathy is not an amenity; it should give substance to every helper response. | Empathy |
| Q07003 | Active listening is wasted without empathic responding. | People Skills |
| Q07004 | Listening at its best is both focused and unbiased. | Objectivity |
| Q07005 | Helpers without a set of working values are adrift. | Values and Priorities |
| Q07006 | Goals that are to be accomplished "sometime or other" probably won't be accomplished at all. | Goal Setting |
| Q07007 | Hope plays a key role in both developing and implementing possibilities for a better future. | Inspiration |
| Q07008 | Only a small fraction of the help provided on any given day comes from helping professionals. | Being Human |

The two mended quotation marks in Q06985 and Q07006 are already corrected in this table. Use it as written here.

## 6. The order of work, and the waves

1. **Q07026 alone**, brought to a clean gate. Stop. Report it.
2. **The remaining twenty four Handbook records**, in two waves of twelve, first wave gate-checked before the second starts.
3. **One Skilled Helper record alone**, drafted end to end, gate-clean, as the exemplar for that half. Stop. Report it.
4. **The remaining twenty four Skilled Helper records**, in two waves of twelve, on the same terms.

Stage 0 runs on the twenty five new records only. The Handbook twenty five already carry theirs.

## 7. What nothing here waits on, and what nothing here unblocks

**Nothing publishes at the end of this.** The quote page itself has never been built: Code is waiting on one ruling from Kain in Safari, whether a quote page carries a course slot. **That is not your blocker and you do not wait for it.** Records ahead of the template is the same position the rescued articles were in, and it worked.

**Do not touch the two book notes, the quote master, or anything on the install.**

## 8. What comes back

One file to FROM Cowork per stopping point above, five in all, each pointing at its batch report in `Content Records/quote-page`. Each names the gate result per record and, for Job A, **the exact list of records you changed**, so Code re-imports only those.

Where a fix would need a change this brief has not authorised, name it and leave it. That is what you did correctly at S342 and it is why this run exists rather than a repair job later.

---

OWED BACK: five wave pointers to FROM Cowork, and the changed-record list for Job A.

*No em or en dashes in this file; checked before writing.*
