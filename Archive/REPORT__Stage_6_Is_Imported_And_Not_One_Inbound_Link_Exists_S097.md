# REPORT: stage 6's import is done and proved. Not one of its 42 inbound links has ever been placed.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** `RULING__Nine_Answers_From_The_S332_Sitting_S332.md` items 1 and 5, and the stage 6 half of `BATCH__instructor-article_ready_for_stage_5_S316.md`.
**Board cards:** the eighteen instructor articles; article production enters through one enforced route.

---

## 1. The bin was empty, so stage 6 could run

Checked first, as item 5 requires: `wp post list --post_status=trash --post_type=any` returns zero rows across every post type. Kain emptied it. No row was deleted by Code.

## 2. The import is done, and it was already done

**Fifteen of fifteen are live and published**, IDs 34254 to 34282, read off the install this session. Every slug matches the S316 batch table exactly, and not one carries a `__trashed` suffix. They were imported fresh at S096 on Kain's publishing override, after he emptied the bin.

So item 5 is closed. **Nothing was re-imported tonight**, because re-importing fifteen correct pages to satisfy the wording of an instruction already satisfied is a change set that can only introduce faults.

## 3. `brief_state` is set, and my own line at S097 saying otherwise was wrong

**203 of the 204 records under Content Records carry `brief_state | pre-standard`**, written 2 September at 19:33. The one that does not is `I10__why-giving-advice-does-not-work__EXEMPLAR_S329`, which correctly carries a real `## Search and Citation Brief` section instead. Every other file without the field is a batch report, a scratch file or a folder read-me, not a record.

**Correction owed and made:** the disposition line I wrote on the S332 ruling earlier this session said no record carried it. That was me repeating the S096 line instead of reading the folder, which is the exact fault the Shared Rules' section 2 exists to stop, committed in a line whose whole job is to state a testable fact. The line is corrected on the file.

**Proved rather than assumed.** The presence of a string is not proof a gate reads it, so the pre-draft gate was run on a pre-standard record. Check 5 prints `NOT RUN: brief_state pre-standard, brief owed at next edit`, the verdict is PASS, and the closing line names the brief as owed at next edit. Not a PASS on check 5, not a FAIL on the record. Exactly as Kain ruled. So item 1 is closed on this side.

## 4. The finding: 0 of 42 inbound links exist

Each of the fifteen records names three inbound links in `inbound_from`: the address of a page that should point at it, and the exact sentence that should carry the link. **Read off the live pages this session: not one of the 42 sentences is on the page that should carry it.**

**The check got this wrong twice before it got it right, and both are worth naming because the first wrong answer was convincing.**

The first version used bare urllib, every page returned 403, and it reported 0 of 42. That looked like a finding and was a blocked read. The second version fetched properly and reported **19 of 42 present**, which was worse, because it was believable. Those 19 were the theme's own Related Further Reading block, which renders on every article whether or not a person placed anything. The check was asking whether a link existed anywhere on the page; stage 6 asks whether the authored sentence is in the page's prose. It now tests the sentence, and it prints the status of every page it read so a wall of failures can never again be mistaken for a finding when it is really a blocked read.

**The answer is zero.** Eleven of the thirteen source pages return 200, so the check reached them.

## 5. Two different problems inside that zero

**Fourteen of the 42 cannot be placed today.** They point at two book notes that do not exist on the install: `/learn/helping-people/book-notes/the-skilled-helper/` and `/learn/helping-people/book-notes/the-ultimate-life-coaching-handbook/`. Both return 404. Neither is among the 65 published book notes. Eight of the fifteen articles depend on the first and six on the second.

**CORRECTED LATER THE SAME SITTING, and the correction matters.** The line above originally said those two book notes had to be written. **They are written.** Both records are on disk in `Content Records/book-note` and both hold a register row; what I had read was the install, and I reported the pages as missing without checking whether the records were. Run through the gate this session, both fail on the SEO finish and stage 0 alone (9 failures and 7), with every writing check passing on both. So they are not a writing job, they are the front two of the sixty seven book notes needing the review Kain ruled earlier this sitting, and Code imports them the moment they pass. Kain has ruled them to the front of the queue: `RULING__The_Two_Source_Book_Notes_Go_To_The_Front_Of_The_Queue_S097.md`.

**Twenty eight point at pages that exist and are buildable today.** The source pages are Gerard Egan's biography, Kain Ramsay's biography, and six of the instructor articles themselves.

## 6. The one question, and why Code stopped rather than placing them

**The words exist and are approved. The position does not exist anywhere, and Code will not invent it.**

Each sentence is written in the voice of the source page's author: Egan's biography gets "His own account of why people come to a helper ..."; Kain's own articles get first-person "... which I set out in ...". So each has a natural home in a particular passage of a particular argument, and choosing that passage is an editorial act on a published body, not a mechanical insert.

**Looked first, and the looking did not settle it.** The records' closing paragraphs carry the course call to action, not article cross-links, so there is no convention to copy. The sentences are not in the source records' bodies either, so this is not the book note case where a re-import would land work already done; nothing has been written into a source body at all.

**Code's recommendation, and it is a recommendation:** the sentence is written into the source record's body by whoever owns those words, then Code re-imports the source records and re-runs this check. That keeps the pipeline's own rule that the record is the source and nothing is fixed on the install.

---

OWED BACK: who places the 28 buildable sentences and where in each body they sit. The other 14 wait on two book notes being written, which is a Cowork job Chat already holds.

*No em or en dashes in this file; checked before writing.*
