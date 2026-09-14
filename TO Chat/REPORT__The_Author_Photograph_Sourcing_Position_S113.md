> CHAT DISPOSITION, S358: STAYS, and Chat writes nothing on it. Kain is working the author image solution directly with Code. Section 3's three options were put to him at S358 and he took none of them: he wants the author faces drawn as original Achology artwork rather than sourced. Chat named the copyright position (a stylised version of a photograph is a derivative of it, so the 36 do not become usable by being drawn) and the free tooling that exists (APDrawingGAN2, DrawingBotV3), then held. **No brief travels to Code on this from Chat.** Archived when Kain says the solution is settled.

# REPORT: where the book author photographs stand, and the one command that says so

**DOCUMENT TYPE:** report, filed by Claude Code, Session 113, factory session. **Date:** Sunday 13 September 2026.
**Answers Kain's question at the close:** "How will you know, in the next session, that you have a solution for sourcing all of these author images?"
**The answer is that nobody will know it. A command will say it,** and that command already exists.

---

## 1. The test, so this is never recalled

```
python3 tools/absent_book_author_portraits.py
```

It reads every published book note off the live install, takes the author slug each one actually carries rather than deriving one, and prints four numbers: notes published, distinct authors with a portrait, distinct authors without, and notes carrying no slug at all. **It is the only claim about this that counts.** A number in a handover, a memory note or a message is not evidence, including the numbers in section 2 of this file, which are that command's output at this close and nothing more.

**It was rebuilt this session because it was lying.** It reported 99 notes carrying no author slug when every one of them had carried it all along: `wp post meta list` takes one post id and was handed 99, and a silent `returncode == 0` absorbed the failure. It reads one SELECT now, and a read that fails stops the report instead of becoming its answer. The correction is why the number below can be trusted at all.

## 2. Where it stands at this close

| | |
|---|---|
| Book notes published | 99 |
| Distinct authors with a portrait | 62 |
| Distinct authors without | 26 |
| Notes carrying no slug | 0 |

Plus **seven held back deliberately**: they came through the fetcher's name-search route rather than a chosen portrait, and its own header records that this route fetched a different James Allen and a US Army general called Howard Gardner, both with the right name in the filename and a clean licence. They wait on a human looking at the face, which is five minutes of somebody's time and not a job for a script.

## 3. The part that is not a sourcing problem, and this is the answer to his question

**114 book authors were asked for. 78 were found. 36 had nothing free anywhere.** Re-running the fetch will not change that number, because it is not a search that failed: it is the licence answering no. Almost every one is a living author whose publicity photograph belongs to the photographer who took it, and DSRD 7 section 12.5's own words govern it: a file whose licence cannot be read is skipped and named, because "I could not tell" and "it is free" are different answers and only one of them is safe.

So there is no fetching solution left to find for those. **What is left is a decision, and it is Kain's:**

1. **Leave them blank.** The page draws no portrait and loses nothing else; the route has fallen through cleanly since S278 by design.
2. **Draw them.** The `ach-book` brief already commissions a drawn treatment for covers; a drawn or abstract author mark is the same kind of answer and would cover every author at once, including the 36.
3. **Buy or commission them.** Real money, real time, and only worth raising because the other two cost neither.

**Nothing in this file recommends one.** It is a money and brand decision and it is his.

## 4. What this means for the next session, in one line

The next session runs the command in section 1 before it says anything about author photographs. If it reads 62 and 26, nothing has moved. The 26 and the 36 do not move by fetching again, so a session that re-runs the fetch expecting a different number has misread this file.

OWED BACK: Kain's choice between the three in section 3, and a look at the seven held faces.

*No em or en dashes in this file; checked before writing.*
