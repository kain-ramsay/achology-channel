# RULING: yes to both inputs, and the brief that names the columns

**From:** Claude Chat, Session 331. **Date:** 2 September 2026.
**Answers:** `ASK__Feed_The_Keyword_Register_From_Search_Console_Queries_S094.md`, its OWED BACK line. Kain's ruling in the S331 sitting: yes, add Search Console's query report read by machine, and yes, take AnswerSocrates exports dropped in by hand. Nothing else in the list joins.
**Reads with:** `KEYWORD_REGISTER.csv` and `build_keyword_register.py` in the Content Production Factory folder; The Publish Ready Pipeline Version 5, stage 0 and stage 8; `content_gate.py`, which reads the register for its uniqueness and pre-draft checks.

---

## The one rule that shapes everything below

**The register stays a register of claims.** `KEYWORD_REGISTER.csv` holds one row per keyword a page has claimed, and nothing else, because `content_gate.py` reads it as exactly that: its uniqueness check treats any row whose `record_slug` differs from the record's as a clash, and its pre-draft check 3 fails a keyword with no row. A Search Console query dropped into that file as a row with no record would be read as a claim by a page that does not exist, and every later page wanting that keyword would fail. So observed demand does not go into the register. It goes beside it.

## The new file: `DEMAND_CANDIDATES.csv`

One file, beside the register, written by machine and by hand, read by Cowork at stage 0 and by Chat at stage 8. Columns:

| Column | Carries |
|---|---|
| `query` | the words as typed, lower case, exactly as the source gives them |
| `source` | `gsc` or `answersocrates` |
| `page` | for `gsc` rows, the address on our site the query landed on; blank for AnswerSocrates |
| `impressions` | for `gsc` rows, the count in the report window; blank otherwise |
| `clicks` | for `gsc` rows; blank otherwise |
| `window_start`, `window_end` | the dates the numbers cover (the Search Console report window, or the AnswerSocrates export date in both) |
| `seed` | for `answersocrates` rows, the seed word the export was run on; blank for `gsc` |
| `claimed_by` | filled by the builder: the `record_slug` from the register where the query matches a claimed keyword exactly; blank where it matches none |
| `date_added` | the run date |

A query that appears in both sources gets two rows. The file is regenerated whole on every run and never hand edited; the AnswerSocrates exports it reads are the drop files themselves, kept as they arrived.

## How the two sources are weighed, at stage 0

This is the content standard Code asked for, and it is short.

1. **A candidate with real impressions outranks a guess.** At stage 0, Cowork reads `DEMAND_CANDIDATES.csv` before running the live searches the pipeline names. Where a `gsc` row carries impressions for the seed phrase, that row's wording is the leading candidate for the title, because it is what people typed, on this site, and the autocomplete list and People Also Ask are then confirmation rather than discovery.
2. **A claimed query is closed.** A row whose `claimed_by` is filled names a page that already answers it. It is never a new page's title; where a second page wants it, the second page takes a different question, exactly as the register rule already says.
3. **AnswerSocrates rows are questions, not demand.** They show what people ask around a seed; they carry no count. They feed the supporting-questions part of the Search and Citation Brief and the `query_variants` field, and they may seed a title only when the live search at stage 0 confirms it, because an export with no numbers behind it is a list of possibilities.
4. **A `gsc` query that ranks a different page than its title promises is a retitle flag**, which is stage 8's existing rule, now fed by machine rather than by a hand read of Search Console.

## What Code builds

- One script, `pull_demand_candidates.py`, in the Content Production Factory folder beside `build_keyword_register.py`, reading the Search Analytics report through Google's own interface with the key already in use (Harness Rule 11), over a trailing 90 day window, and reading any `AnswerSocrates__*.csv` files dropped into a `Demand Exports` folder beside it. It writes `DEMAND_CANDIDATES.csv` whole and fills `claimed_by` by exact match against `KEYWORD_REGISTER.csv`.
- It touches `KEYWORD_REGISTER.csv` not at all. That file is still rebuilt from the records by `build_keyword_register.py` before every commission.
- The run is printed: rows written, rows claimed, rows unclaimed, and the ten unclaimed `gsc` queries with the most impressions, because those ten are the next commission's shortlist and Kain reads them.

## What is not built

- No Google Analytics read: it hides the search words and answers a different question, as the ASK said.
- No change to `content_gate.py`: the register's shape is unchanged, so the gate's reads are unchanged.
- No weighting formula beyond the four lines above. A score that ranks candidates by impressions times something is a hypothesis; the impressions column is the number, and a person reads it.

OWED BACK: a REPORT to TO Chat with the first run's printout and the ten-query shortlist, and any part of the four weighing lines the machine cannot read as written, named rather than worked around.

*No em or en dashes in this file; checked before writing.*
