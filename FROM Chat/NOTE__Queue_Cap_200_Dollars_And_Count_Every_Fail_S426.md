> CODE DISPOSITION, S170: DONE. The $200 total cap is set (TOTAL_CAP_USD, summed from every run's cost log) and FAILS_LOG.csv is written with time, batch, slug, round, source and line.

First line of need: Code, factory session: two settings for the weekend queue. Set the money cap at $200 in all, and log which gate line or check sent each page back.

# NOTE: the queue's cap, and counting every fail (Chat, Session 426, Thursday 15 October 2026)

**1. The cap (Kain, S426).** Stop rule 2 in BRIEF__The_Weekend_Queue_..._S426 stops the queue when everything spent from Kain's API credit since the first batch reaches **$200**. That is the credit loaded now. Kain and Chat take stock on Friday evening, about 24 hours after the queue starts. Kain tops the account up then if it is needed, and Chat sends you the new figure in one line.

**2. Count every fail (Kain, S426: "get on top of these fails ... some are coming from rules that don't need to be rigid").** For every page the queue sends back, log the exact gate line or free check that sent it, with the record and round, in `queue_S426/FAILS_LOG.csv`. Columns: time, batch, slug, round, source (gate, local check, checker), line. At Friday's stock-take Chat totals it. Every rule that sends pages back is then named for Kain as one of two things: a real fault, which stays a fail, or a rule that should only be a NOTE. Kain rules on the second group, and you change the gate. No gate line changes before then.

OWED BACK: one line in your queue DONE: the cap set, and the fails log working.

*No em or en dashes in this file; checked before writing.*
