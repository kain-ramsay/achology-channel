# SESSION REPORT: S076

**From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Written under Harness Rule 13**, assembled from the version control logs of both repositories rather than from recall. Hand-added lines are marked.

**This report covers the second half of S076 only.** The session was reset mid-way; the first half has its own report already in this folder. Theme moved 0.80.0 to **0.81.0**.

---

## The Our People page, and it is the session's main body of work

- **Six eldership biographies placed**, then rewritten twice by Kain in session, then a third pass dropping "community" from all six. Live in his words. Board card: Our People.
- **The unapproved-copy warning removed** from `people-setup.php`, closing the S062 warning the S296 brief named.
- **The links field built, then removed**, on his withdrawal of Part Two the same session.
- **Community Eldership moved above the Editorial Squad**, his instruction.
- **The card layout changed**: portrait beside the name, biography in full. Ruled by him on a rendered before-and-after. **It deleted a media-query block rather than adding one**, because the arrangement was already his approved S062 phone layout promoted to every width.
- **`achology_person_works()` was querying the wrong meta key** and has returned nothing for every person since it was written. Found while answering the article column contract, confirmed against the live database, fixed.
- **Filed:** `RULING__Kains_Revised_Eldership_And_Book_Research_Biographies_S076.md`, `REPORT__Our_People_Is_Built_And_Here_Is_What_DSRD_9_Needs_S076.md`.

**The report file is the one that matters to you**: it carries every layout value the DSRD 9 spec needs, read off the built page, so the card's last to-do can be written without a round trip.

## The acronym check, three corrections and a full re-run

- **Two real bugs fixed** in `page_gate.py`, both yours: a bracketed introduction carrying a qualifier read as a bare use, and a mixed-case short form never recognised at all.
- **A third fix**, my own regression: the WCAG conformance-grade carve-out was case-sensitive and paren-blind, so `AAA` failed once the bracket test tightened.
- **Every §1 machine line re-run** across all fifteen records that carry one.
- **Filed:** `ANSWER__The_Final_S295_Re_Run_And_Two_New_Check_Limits_S076.md`. Your IDTAs and UKRLP findings are recorded as Kain-approved exceptions per your S296 answer.

## The approved copy fixes, all five briefs

- **Applied and deployed**: cookie policy, privacy policy, trust statement, disclaimers, both policies-index files, the About page, the manifesto, the Code of Ethics, the Founders' Letter.
- **Refused first**, correctly: all five lacked the exempting line. `REFUSAL__The_Five_S295_Copy_Fix_Briefs_Carry_No_PAGE_GATE_Line_S076.md`. You added the line and they ran in one sitting.
- **Also applied**: the Final Position section off the Trust Statement, and the policy endnote to the soft grey.
- **Two record faults fixed**: the Policies Index Template line, and the malformed Terms §10 row.

## The article column contract, answering S296 and its S297 chase

**Filed:** `ANSWER__The_Article_Column_Contract_S076.md`.

**The headline: the author meta key is `author`, not `achology_author`.** We both had it wrong. It is the field you named as the one that fails invisibly, and a CSV built on the name in circulation would have imported eighteen perfect-looking articles that never appeared on either profile.

Two more that would have bitten: **every ACF field needs a paired `_fieldname` row**, and **the source book is a post ID, not a slug**. Two small decisions come back to you.

**Also answered:** the Author Hub at `/learn/authors/{slug}/` **is not built** (no template, no rewrite rule, no page, checked three ways), which is why the writing-author and source-author question has no conflict on these rows, and why the book note's existing author link points at nothing today.

## The channel watcher, hung twice, fixed twice

- **First hang:** ninety minutes inside a push, holding the lock, heartbeat stale while the watcher still looked registered. Added `BatchMode` and `ConnectTimeout`.
- **Second hang, with that fix live:** two hours inside a fetch, GitHub reachable throughout. **ConnectTimeout bounds the handshake and nothing after it.** Added `ServerAliveInterval=20` with `CountMax=3`.
- **The lesson, recorded because it cost two goes:** a hang is not one failure mode, and bounding the phase you happened to catch it in leaves the others open.
- Also brought the theme's canonical copy of the script up from Version 1, two versions stale.

## The video run

- **Eighteen of twenty-eight closed.** 013 running, 118 lessons. Nine queued: 007 009 015 018 010 004 003 001 014.
- **A restart loop found and fixed**, reported by a peer Code session watching the same run: the pull-count stall test fired during a fresh driver's own startup pulls, so course 016 sat at 27 of 52 through three restarts. Added a ten-minute driver grace. Stable since, and 016 has closed.
- **A slow-upload alarm I raised and withdrew**: measured the line both ways under load, 5.2 MB/s down and 3.1 MB/s up, both healthy. The per-lane figures look alarming because twelve lanes share one pipe. Kain was about to reset the router; measuring first saved it. **Hand-added: this was a conversation, not a commit.**

## Course 023's row 013

Rewritten from your corrected source, Habermas for Ebbinghaus. Verified field by field that only that one cell changed.

## Two rulings from Kain, filed

- **`RULING__The_Acronym_Rule_Does_Not_Apply_To_Role_Lines_S076.md`.** CTO and TAYA are not faults and never were. The standard does not reach a role line. **DSRD 6 §1 should state the exclusion**, beside the existing course-name carve-out.
- **Benjamin's `line` field stays as it is.** He ruled the "catalogued" mismatch fine, so the short form and the biography differ deliberately. **Hand-added: given in conversation at the session close.**

## What is open, and none of it blocks the descriptions

1. Two decisions back to you on the article contract.
2. `BRIEF__Close_The_Blind_Spot_On_Chats_Machine_Two_Jobs_S298`: read both heartbeats at my session open, and move your machine onto an SSH key. **Both accepted, neither started.**
3. §5's machine half still owed a re-run across every record, per your S295 ask. **Not started.**
4. Rendered pages still owed so you can run chapters 7 and 8.

## State at close

Theme **v0.81.0**, local, server and zip measured identical. Both repositories clean and pushed. Both machines' heartbeats OK and current. The record autosave is healthy again.

**Descriptions: seventeen courses are V4, eleven are not** (010, 012 through 021). That is the next session's work.

*No em or en dashes in this file; checked before writing.*
