> Code: the worker's repair step is printing duplicate sentences into pages marked ready. No article goes on the signed list until the fix below lands and the saved replies are replayed. The 14 met biographies are on the list for Kain's signature; apply your three biography fixes.

# RULING: the first stock-take read (Chat, S428, Thursday 15 October 2026, 23:00)

Read this turn: QUEUE_LOG, FAILS_LOG, QUEUE_STDOUT, both article runs (`run_20261015_185647`, 16 records; `queue_second_batch_psychology_S426_20261015_215143` and its replay `_222530`, 32 records), both biography reports, and eight article pages whole: Little Albert, Split Brain, Invisible Gorilla, Zimbardo Deindividuation, Monster Study (first run); Aaron Beck, Rosalynn Carter, Two Factor Models (second run). One biography read whole: Erich Fromm. The queue was 45 minutes old at the read; Q001 to Q031 had not returned. Nothing here needs STOP: the writing and fact check replies are saved, so the fix is replayed at no API cost.

## 1. The defect that holds every article (fix first)

When the fact check names a sentence, the script puts the original sentence back. Where the writer had split, merged or moved that sentence, the original now sits beside the writer's version, so the page says the same thing twice, or loses the half that made the next line make sense. A six-word check over all 48 found it in 7 pages, two of them marked **ready**:

- Robbers Cave (ready): "Two groups of white, Protestant, socially well adjusted 11 year old boys..." appears twice in one paragraph.
- Zimbardo Deindividuation (ready): "A related study, run with a colleague named Wallbom, found the other side of the same effect. A related study, run with a colleague named Wallbom, found something else. Nothing else about the setting changed." The mirror finding itself is gone, and the next paragraph still says "doesn't need a mirror in the room".
- Also: Strange Situation, Harlow, 10 Ethically Dubious, 20 Cognitive Biases (needs_chat already). Two Factor Models (ready) has a broken join of the same kind: "His supervisor there was Cyril Burt. Patients in his study varied along two clear dimensions."

The fix, Code's to design: after repairs, a free check that **blocks** when any sentence in a paragraph shares its first six words with another, or when a repaired sentence's original overlaps a neighbouring sentence; and a repair that swaps the writer's whole changed span for the original span, not one sentence. Then replay both runs with `--replay` style re-evaluation at no cost, and re-stage. Done when the six-word check reports 0 across all 48 and the 7 named pages read clean.

## 2. Three false blocks (fix in the same pass)

1. **Reader questions read as the writer speaking.** "What evidence do I have, and what category did I reach for without thinking?" is a question the reader is told to ask, inside quotation or after "ask yourself". It blocked Blue Eyes, Hawthorne, Strange Situation and Harlow. A first-person line inside a question the reader is told to ask is never a block. The "I still remember reading..." line in 10 Ethically Dubious is a real writer line and stays a block.
2. **"A link changed. Missing: []. New: []."** Blocks with nothing missing and nothing new (10 Ethically Dubious, Gardner). Same rule as your biography fix: compare addresses as sets.
3. **Fact check unreadable (end_turn)** on the same four records every run (From Roots to Revolution, How Philosophy Illuminates, Freud's Defence Mechanisms, Lucifer Effect). Raise the fact check's output limit for long records and retry once in a fresh batch.

Also: the fact check repairs lines it says are fine ("Not a change from the original; no issue" in 10 Ethically Dubious). A reply that says no issue is never repaired.

## 3. Three writing faults the writer must stop making (one line each in the writer's rules)

1. **The focus keyword is forced in.** Aaron Beck says "revolutionized cognitive psychology" 12 times; Rosalynn Carter uses "Rosalynn Carter and mental health stigma" as a subject; Little Albert prints "the little albert experiment" in lower case throughout. The writer uses the keyword where the gate needs it (title, first tenth, one heading) and writes natural words elsewhere; a person's name always has its capitals.
2. **A comma splice with a capital:** "more than the other, That leaning" (Split Brain).
3. **Number style inside one page:** "sixty-eight years" and "68 years" (Monster Study). One style per page, as the Standard sets.

## 4. Two facts to put right in the records (not the worker)

- **Zimbardo Deindividuation:** "He also ran a larger replication on 102 Belgian Army soldiers, and the same pattern held." Zimbardo's own chapter reports the Belgian soldiers in hoods gave *fewer* shocks, not more, which he put down to the soldiers already being deindividuated in uniform. The line comes from the original record. Correct it to what the chapter says, from the chapter, and add the reversal as one sentence; it strengthens the page's own argument.
- **Aaron Beck:** the Canady (2021) link reads `onlinelibrary.wiley.com/ai/10.1002/mhw.32883`; `/ai/` should be `/doi/`. Also in the original record.

## 5. The biographies

- **Your question, ruled:** "padding" and "detail adds no understanding" findings are notes, not holds, for biographies. One good pass and a fact check is the standard; a checker that finds new small points each round does not converge.
- **Holds that stay holds:** unsupported facts (Newport, Gladwell, Burchard, Taleb, Grayling), unlisted drops (Nietzsche, Thich Nhat Hanh), pronouns with no clear referent (de Botton, Ruiz, James Allen, Maxwell, Dewey, Beck, Pressfield, Gardner), ties between the author and Achology (Aristotle, Thich Nhat Hanh), changed quotations (Gardner and the other). Repair these on the worker by script where a fact check named the sentence, one writing pass where it did not, then the same fresh check. Grayling and Manson also show the duplicate pattern from section 1 (Grayling in its notes, Manson in the body); run the six-word check on biographies too.
- **Your three small fixes (de Botton, Schopenhauer, Duhigg openers; Duhigg's fixed line):** apply as staged.

## 6. The list for Kain's signature this week

Signed by Kain, then imported by Code at his next factory session, with Content Records stamped:

**14 author biographies (met on the fresh check; Fromm read whole by Chat, clean):** Schopenhauer, Ariely, Goleman, Fromm, Erikson, Mate, Yalom, Piaget, J S Mill, Campbell, Plato, Hanson, Greene, William James. Before import, run the six-word check on all 14; any hit comes off the list.

**Not on the list, and why:** all 48 psychology articles (section 1); the 16 from the first run, including the 6 staged and the 10 ready, which are the same records; Q001 to Q031 (not back yet). The replayed 48 come to Chat's Friday 16:30 read, with five pages per batch read again after the fix.

## 7. The queue's restarts

QUEUE STARTED appears four times in 45 minutes (21:49, 21:51, 22:25, 22:30), each re-collecting the psychology batch at no cost. If these are your tests, ignore this line; if launchd is restarting a crashed run, the cause belongs in TO Chat with the fix.

## 8. Backlog: Lanes, settled without Kain (Shared Rules section 8, Rule C)

- Book note titles under 50 characters: add "by {Author}". Written into PACK_02 at the next pack edit.
- Workbook images: settled at S427 (thirteen shapes approved; the drawing tool first). Line removed.
- Seven quote records placing call, and the two-person opening on about 289 quote records: PACK_03, signed, governs both; no programme change before launch. Lines removed.

OWED BACK: one DONE when sections 1 to 3 are fixed and both runs replayed, with the six-word count; the two record facts in section 4; the biography repairs in section 5.

*No em or en dashes in this file; checked before writing.*
