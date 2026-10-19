> Chat: Kain asked that no article reach the site without passing Achology's stances. Needs from you: a decision on what happens to the flagged pages (listed in the CSV beside this note).

# NOTE: the stance check, every staged page (Code, S171, 18 October 2026)

The worker's writer and fact checker were never given the stance notes, so "ready" never meant "right on stance". At Kain's order I built `api_worker/stance_check.py`: it reads each staged page against all 24 stance notes plus What Achology Believes (copies from the Data Labs handover folder; the vault is not on this Mac) and flags only clear contradictions, quoting the page sentence and the stance sentence. It rewrites nothing.

- **1,105 pages checked, 117 flagged (147 flags), 0 unreadable. Cost about $16.57** (running total about $117 of $200).
- **91 of the 117 were marked ready**; 26 were already needs_chat.
- By kind: articles, book notes and others 81 of 425; instructor articles 10 of 48; quote pages 20 of 300; Help answers 6 of 323; seven beliefs 0 of 9.
- Most flagged stances: The Achology Stance 25, Helping People 17, Mental Health 16, Beliefs and Perception 14, Human Identity 13, Emotional Health 11, Communication 9.
- Two real examples from the 20-page trial: a Help answer telling the reader to practise a communication technique on five people (the Communication stance forbids it), and an article crediting Frankl with the line the Personal Efficiency stance says is Nietzsche's.
- The flags are for a person to judge; the checker can be wrong. Full list: `EXPORT__Stance_Check_Every_Staged_Page_S171.csv` (every page, flagged or ok, with the stance it reflects).

**Proposed next step (Kain's rule: nothing on the site without this process):** rewrite each flagged page with the relevant stance text in front of the writer, then re-check; and give the writer and fact checker the stance notes on every future run. Say yes and I start with the 91 flagged pages that were marked ready.

OWED BACK: your yes or changes.

*No em or en dashes in this file; checked before writing.*

**Update, 18 October: the repair rounds (Kain said yes).** New tool `api_worker/stance_fix.py` replaces only the flagged sentences (checked against headings, links, quotations and the six-word rule; a page that fails those is left as it was) and `stance_check.py` re-reads the result.
- Round 1: 91 flagged "ready" pages, 83 repaired, 8 left (a link would change, a fragment, a reply unreadable, one the writer said did not contradict). The recheck flagged 30 of the 83, on sentences the first pass had not flagged: one pass does not catch everything.
- Round 2: 30 pages, 26 repaired, 4 left. Recheck: 10 still flagged.
- **Where it stands: of the 91 that were marked ready, 69 now read clean on the stance check and 22 need a person** (8 + 4 + 10). With the 26 already needing Chat, **48 pages need a person**; the list with the sentence and the stance is `EXPORT__Stance_Pages_Still_Needing_A_Person_S171.csv`. Some are whole-page questions (an article built on persuading someone who disagrees; pages on diagnoses), not sentence fixes.
- The repaired pages are the newest staged copies in `api_worker/runs/stancefix_*/out/`, each with a "Stance fixes" list at the foot. Total stance work about $22; total spend about $122 of the $200 cap.
- A clean stance check is not a promise: the checker found different sentences on each pass. It narrows the risk; Chat's read and Kain's signature still decide. The writer and fact checker on the main queue still do not receive the stance notes; I have not changed that (say yes and I add them).

**Update, 19 October: the read-only stance check of the 281 records that have no staged copy** (signed or protected records, the 51 biographies, the 20 workbooks): **20 flagged, 0 unreadable, cost about $4.55.** Quote pages 11 of 132, field authority articles 3 of 12, Help answers 2 of 52, biographies 1 of 51, book notes 1 of 3, hub question articles 1 of 9, workbooks 1 of 20. Full list: `EXPORT__Stance_Check_281_Unstaged_Records_S171.csv`. Nothing was changed.
- **One needs your attention first: Rick Hanson's biography is one of the 13 I updated on the build site on 17 October, and two sentences state in the page's own voice how the brain works (the stances forbid it).** It is on the build site as updated; say if you want it corrected there.
- **The worker now gives the writer the stance notes on every run, and no page is called ready until it passes the stance step** (check, two repair rounds, recheck; a page that still contradicts a stance goes to Chat with the sentence named). Self-test passes with a case for it.
- Total spend about $127 of the $200 cap.

**Hand-off, 19 October (Kain's instruction): this review is Chat's, in a Chat session, not Kain's.** Kain does not judge sentences remotely and, by his S427 rule, is never asked what Achology believes. Chat has two lists to work through: (1) the 48 pages the repair rounds left for a person, `EXPORT__Stance_Pages_Still_Needing_A_Person_S171.csv`; (2) the 19 flagged records that have no staged copy, `EXPORT__Stance_Check_281_Unstaged_Records_S171.csv` (the Rick Hanson biography is already corrected on the record and on the build site, 19 October, read back). For each page: read the sentence in its paragraph, decide fix, keep or drop, and write the reply; Code applies sentence replacements from Chat's reply the same way (script, checks, update route) and does not ask Kain.
Code did not put the remaining pages to Kain and will not.
