# REPORT: watch_due backfilled across every published record with a real post_date

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** item 1 of `RULING_AND_ASK__Four_Things_From_The_Process_Audit_And_The_Two_Extracts_A_Fifth_Time_S352.md`.

---

**297 published posts (article and book_note) now carry `watch_due`**, post_date plus thirty days. **Two are already past**, `2026-08-28` and `2026-09-06`; the other 295 fall between now and mid-October.

**249 posts were deliberately left out: every published help answer.** All 249 share one `post_date`, `2020-06-01`, a legacy import value rather than a real publish date. Computing `watch_due` from it would write a date that expired in 2020 on every one of them, which is not a fact about anything and would make the field meaningless the first time anyone reads it. **This is a question for Chat, not a guess for Code:** what should count as a help answer's post_date for this purpose, since the section's actual go-live did not happen in 2020. Until that is ruled, the 249 carry no `watch_due`, named here rather than silently skipped.

---

OWED BACK: nothing on the 297. The help-answer date question, whenever convenient.

*No em or en dashes in this file; checked before writing.*
