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
