# WITHDRAWN BEFORE IT WAS ACTED ON. DO NOT BUILD TO THIS.

**Withdrawn by Claude Chat, Session 335, minutes after it was written, on 3 September 2026.**

This brief asked Code to extend the book-note contract, teach `book_note_import.py` to carry the three Rank Math fields, and re-import so the 65 live book notes gain their search words.

**Every part of that was already done.** Code's own `REPORT__The_Sixty_Five_Book_Notes_Already_Had_Their_Words_S097.md` records that the importer's meta map was fixed at S087 and has carried the three keys since, and that the three fields were written onto all 65 live posts in the S097 session itself, read back off the install as 65 of 65 carrying a focus keyword, up from zero. Building to this brief would repeat finished work.

**How the mistake happened, recorded so it is not repeated.** Chat read the S096 ruling out of the TO Chat inbox and wrote a brief against it without first checking the channel Archive for a superseding file. That file existed: Code's S097 report, already carrying a CHAT DISPOSITION line from S334. The inbox is not the whole channel, and a ruling in it can already have been answered. Check the Archive for the answering file before commissioning anything against an inbox item.

**What is actually open**, per the S334 disposition on Code's report: no keyword is replaced on its own, because on these pages the keyword and the body are one thing. The next move is the Search Console table asked for in `ASK__What_Each_Old_Book_Page_Already_Earns_S334.md`, after which the 65 split into keyword stands, keyword changes with its body rewritten in the same pass, or no old page and a fresh stage 0 check. No Cowork commission is written until that table is read.

---

*The withdrawn text follows, kept only so the record is complete.*

---

# BRIEF: the book notes already have their search words. Carry them to the install.

**From:** Claude Chat, Session 335. **Date:** 3 September 2026.
**Approved by:** Kain, this session, in the room.
**Answers and partly overturns:** `RULING__The_Sixty_Five_Book_Notes_Come_First_And_Need_Their_Search_Words_Written_S096.md`, which is still in TO Chat and is dispositioned by this brief.
**Board card:** the book notes card.
**Harness:** The Harness, at the channel root. Build to this brief only; where it is silent, stop and ask through the channel rather than filling the gap.

---

## The correction, and it is the whole reason this brief exists

Your S096 ruling reads, correctly, that sixty-five live book notes carry no focus keyword, and concludes that the work is stage 0 and stage 2 of the pipeline for sixty-five pieces, written by Cowork under a Chat brief. Kain approved commissioning exactly that today.

**Before writing it, Chat measured the records. The words already exist.** Every one of the 108 book note records in `Content Records/book-note/` carries all four fields, checked one file at a time this session, not sampled:

| | |
|---|---|
| Records with a slug (`post_name`) | 108 of 108 |
| Records with `prod_rm_focus_keyword` | 108 of 108 |
| Records with `prod_rm_seo_title` | 108 of 108 |
| Records with `prod_rm_seo_description` | 108 of 108 |

The register risk you flagged as the thing to size honestly is also already handled. The 108 focus keywords are unique among themselves, all 108 are already claimed in `KEYWORD_REGISTER.csv`, and none collides with anything else on the site, including the 55 field-authority articles written this session. Zero collisions across 521 register rows.

**So the writing is done and the commission does not go to Cowork.** What is missing is the last mile: the records hold the words and the install does not. That makes this a contract and importer job, which is yours.

## What is actually wrong

`upload_contracts.json` was read this session. The book-note contract carries **15 columns and not one Rank Math column**. Two sibling contracts in the same file already carry exactly the three that are needed:

- `types.author-biography.columns` (15 columns) carries `rm_focus_keyword`, `rm_seo_title`, `rm_seo_description`.
- `types.instructor-article.columns` (25 columns) carries the same three.

So the pattern is established, proven on two live content types, and this is a matter of extending it to the third rather than inventing anything.

Your own ruling names the other half: `book_note_import.py` writes no Rank Math field at all, so it needs teaching to carry them.

## The work

1. **Extend the book-note contract** in `upload_contracts.json` with `rm_focus_keyword`, `rm_seo_title` and `rm_seo_description`, following the author-biography contract's shape exactly rather than a new one.
2. **Teach `book_note_import.py` to carry them.** The mapping is: record field `prod_rm_focus_keyword` becomes contract column `rm_focus_keyword` becomes the WordPress meta key your own S096 query used, `rank_math_focus_keyword`; and the same for title and description. Confirm the two meta keys for title and description off the install rather than assuming them, since only the keyword key is named in your ruling.
3. **Regenerate the sheet from the records** and re-import, so the fields land on the sixty-five live pages.
4. **Score the pages and write the table**, per `rank-math-90` Part B. That table is the only place a score is ever written.
5. **Report back** through TO Chat: the contract change, the importer change, how many pages now carry all three fields, the score table, and every page that still fails with its failing tests named.

## Two things this brief does not decide, because they are not Chat's to decide alone

**One: there are 108 records and 65 live pages.** Forty-three book notes are written, gate-passing and unpublished. This brief covers carrying the search words to what is live. Whether the other forty-three are imported and published in the same pass is Kain's call, and it should be put to him with what you find rather than assumed either way. If importing all 108 is materially the same work as importing 65, say so, because that changes his answer.

**Two: whether any of the 108 keywords should change.** They were written earlier and are unique and claimed, but they were not proven against live demand this session, and Chat is not asserting they were. If the score table shows a phrase failing for a reason that is the phrase's fault rather than the page's, name it and it comes back to Chat rather than being fixed on the install.

## Definition of done

The sixty-five live book notes each carry a focus keyword, a Rank Math SEO title and a Rank Math SEO description read from their own record; Rank Math can see and score them; the score table exists in your report to Chat; and the contract and importer changes are committed so the next book note import carries these fields without anyone remembering to ask.

## What is not in scope

No body text is rewritten. No keyword is changed. No record is edited on the install. Nothing about the forty-three unpublished records is published without Kain's word.

---

OWED BACK: the report named at step 5, to TO Chat.

*No em or en dashes in this file; checked before writing.*
