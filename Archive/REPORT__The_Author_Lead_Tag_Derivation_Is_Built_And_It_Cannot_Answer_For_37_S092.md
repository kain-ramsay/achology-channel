> **CHAT DISPOSITION, S328:** ruled by Kain, authored lead tag stands marked authored for the 37; written to Code in `RULING__Four_Rulings_From_S328_And_Job_Six_Is_Chat_s_S328`. Archived.

# REPORT: the author lead tag derivation is built, it runs, and it cannot answer for 37 of the 51

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Answers:** the build item at the foot of `RULING__The_Author_Hub_Course_Comes_From_A_Derived_Lead_Tag_S292.md`, and carries one question back under Rule 5.
**Built:** `derive_author_lead_tags.py`, beside the other importers in the Content Production Factory folder. It prints and compares. **It writes nothing**, on purpose: see the last section.

---

## 1. The rule it implements, quoted

DSRD 1 section 5.7, the author biography paragraph, read this turn in its S326 wording:

> Its lead tag is the most frequent lead tag across that author's own content rows, computed at import and written into the same `lead_tag` field the renderer already reads, exactly as a content row's is. Where two tags tie, the one appearing on the author's earliest-published row wins ... Where none of the author's rows are published yet, so there is no publish order to break the tie, the tie is broken alphabetically by tag slug (ruled S304).

**Nothing computed it before today.** `import_author_biographies.py` writes `lead_tag` straight out of the record, so every value on the site is one a person typed. That is what the S292 ruling named as still owed, and it was right.

## 2. What it reads, and the one place it had to make a choice

**A content row's lead tag** is its authored first tag, per section 5.7 step 2. The book note records carry no `lead_tag` field, so a book note's lead tag is the first entry of its `kh_tag` list. The quote records carry `lead_tag` outright and it is taken as written.

**It reads the records and the install together**, deduplicated on `post_name`. The install rows matter: all 65 book notes on the site carry `author_slug` and `lead_tag` as real meta, read this turn, and deriving from the records alone would compute a frequency over one wave of drafting and call it an author's whole body of work.

**A book note names its author by slug and a quote does not.** A quote carries only `quote_author`, a display name. Those are matched by slugifying the name, and any quote whose slug matches no biography is printed rather than dropped, because a row silently excluded from a frequency count changes the answer without anybody seeing it happen.

## 3. The result, and it is not what either of us would have guessed

| | Authors |
|---|---|
| Derived value agrees with the value written in the record | **7** |
| Derived value disagrees | **7** |
| **No content row exists anywhere that names the author** | **37** |
| Total biographies | 51 |

### The seven that disagree

| Author | Written | Derived | On what |
|---|---|---|---|
| alfred-adler | understand-your-mind | overcome-self-doubt | clear winner, 1 row |
| erik-erikson | grow-self-awareness | navigate-life-changes | tie, broken on date |
| gerard-egan | learn-counselling | help-others-grow | clear winner, 1 row |
| jean-piaget | understand-your-mind | help-others-grow | clear winner, 1 row |
| judith-s-beck | break-negative-thinking | build-self-discipline | tie, broken on date |
| philip-zimbardo | understand-your-mind | improve-social-confidence | clear winner, 1 row |
| rick-hanson | understand-your-mind | build-mental-resilience | clear winner, 1 row |

**Five of the seven are not close calls.** The author has exactly one content row, that row's lead tag is unambiguous, and the written value is a different tag. The rule says the row decides and the row was not read.

**The A. C. Grayling record predicted this in its own notes**, and it is worth quoting because it is the system working: "understand-your-mind was picked by row order as a stand-in, not derived from any real ranking signal. This is Claude's assumption for Kain to confirm or override, not a settled fact." The S304 alphabetical rule now settles exactly that case. Grayling himself lands in the 37 below, because none of his book notes exist as rows yet.

### One caution on the two ties

The tie-break reads "the earliest published row". Both ties above resolved on `post_date` values that read 26 August 2026 within a minute of each other, because that is when the batch was imported rather than when anything was published. **So on a tie the rule is currently breaking on an import timestamp.** It gives an answer and the answer is stable, but it is not the signal the rule intends, and the S304 alphabetical fallback does not catch it because these rows are published rather than unpublished. Worth a sentence in section 5.7 when you are next in it.

## 4. The finding that matters more than the seven

**Thirty seven of the fifty one biography subjects have no content row anywhere.** Not a book note, not a quote, on disk or on the install. Freud, Frankl, Gladwell, Holiday, Peterson, Seligman, Pinker, Plato and twenty nine others.

That is not a fault in the biographies and not a fault in the derivation. It is what the catalogue is: the 65 book notes and the 51 biographies were drawn up for two different sets of authors, with an overlap of fourteen.

**Section 5.7 has no clause for it.** It tells me what to do with one row, with several, and with a tie. It does not say what an author's lead tag is when the author has no rows at all, and the answer decides what course appears at the foot of thirty seven published pages.

**Under Rule 5 that is a stop and ask rather than a judgement, and this is the ask.** My recommendation, so you have something to rule on rather than an open question: **where an author has no content row, the authored value in the record stands, and the record says in its notes that it is authored rather than derived.** The alternative, deriving from the biography's own `kh_tag` first entry, would be a derivation in name only, since that tag was typed by the same hand as the lead tag it is meant to check.

## 5. Why it writes nothing yet

Two reasons, both about landing it once rather than twice.

The 51 biographies are re-imported anyway at step 3 of the S309 Rank Math brief, behind your two writing passes. Correcting seven values on the install now would be a fix applied to the install alone, which the pipeline's own section 4 names as the S082 failure: wiped by the next regeneration.

And the seven corrections are corrections to records, which are yours. The derivation is the machine half and it is built; wiring it into the import is one function call and it goes in when the import next runs.

OWED BACK: the ruling on the 37, and a word on whether the seven disagreements are corrected in the records before the re-import or left for Kain's eye.

*No em or en dashes in this file; checked before writing.*
