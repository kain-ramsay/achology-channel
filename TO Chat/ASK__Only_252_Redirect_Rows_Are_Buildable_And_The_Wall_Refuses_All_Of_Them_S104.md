CHAT DISPOSITION, S346, 6 September 2026: acted on. The 252 buildable figure is written into the S346 handover's numbers block, superseding 757 as the count that matters. Clearance route ruled: publish_gate.py gains a redirect mode, Code's own option 1. The `/` to `/` row carries no redirect at all, NOT action gone, which is a 410 and would have taken the homepage off the internet. Answered in FROM Chat as RULING_AND_REPLY__The_89_Is_Written_And_Nine_Of_Your_Open_Lines_Are_Answered_S346. Board card: Redirect Strategy and Delivery.

# ASK: only 252 of the 757 redirect rows are buildable, and the publishing wall refuses every one of them

**DOCUMENT TYPE:** ask, from Claude Code, Session 104, factory session. **Date:** 6 September 2026.
**Answers:** `BRIEF__The_Redirect_Maps_Remaining_Build_Chain_Register_Through_Staging_S339.md`, steps 1 and 4 delivered, steps 2, 3 and 5 stopped with the reason named.
**Board card:** Redirect Strategy and Delivery.
**Read this cold.**

---

## Why this session ran the redirect work rather than the publishing run

Kain opened S104 as the publishing session on the 85 article drafts, and named its two conditions himself: the DSRD 6 section 5 item 11 exception recording his ruling that these articles publish at 89, and whether DSRD 2 section 3.2 or section 3.8 governs them. **Neither has arrived.** Read this turn rather than recalled:

- **DSRD 6 is at Version 14 and section 5 item 11 carries two page-type exceptions, the help answer's 81 and the book note's 88.** There is no field-authority article exception and no 89 anywhere in the item. `RULING__The_Articles_Publish_At_Eighty_Nine_And_Are_Never_Padded_To_Cross_The_Step_S103.md` is still sitting in TO Chat unanswered; `RULING_AND_REPLY__Book_Notes_Take_88_And_Every_S103_File_Answered_S344.md` predates it by four hours and does not reach it.
- **DSRD 2 section 3.2 and section 3.8 both stand unchanged and neither claims this set.** Section 3.8 is written for the 63 planned school-page field-authority articles and says nothing about the rescued salvage set, whose records were all drafted and gated to section 3.2's 2,000 words. `COMMISSION_NOTE__Kain_Rules_The_Eighty_Five_Articles_To_2100_To_2300_Words_S103.md` in TO Chat is the file that owed this.

His own instruction for that case was to say so and build redirects instead, so that is what this session did. **The gate was not loosened.**

## 1. The chain register is run fresh, and the 757 is not 757

**Step 1 of the brief, delivered.** `redirect_chain_register.py` ran against the live build install this session and wrote its five columns back onto every block tab. The printout is in the run, and its own headline: **235 of 1,051 distinct destinations carry all five chain facts. 816 have an incomplete chain.**

Read against the rows rather than the destinations, which is the number that matters for building:

| | Rows |
|---|---|
| Total rows in the map | 2,596 |
| Status `ruled`, the ones the handover called buildable today | 757 |
| **Status `ruled` AND destination chain complete** | **252** |

**So 505 of the 757 are not buildable today.** Why, counted across those 505: 328 point at an address that returns HTTP 404 on the build site; 502 are absent from the sitemap; 195 carry no schema for their page type; 192 carry no route to a course or the free tier; 2 are not indexable.

The 328 that 404 are almost entirely the pages nobody has built yet: `/academy/` and all 28 course pages under it, the school pages, and most `/learn/` category addresses. That is not a fault in the map. It is the map correctly showing that a redirect cannot be built to a page that does not exist.

**Where the 252 sit:** 213 help articles, 15 help categories, 14 core pages, 7 pen-name authors, 3 miscellaneous. The 213 help articles are the traffic-carrying half of the whole map, so the buildable set is small but it is the valuable part.

**One number for the board, so the card stops carrying 757 as the buildable figure.** 757 is the count of rows Chat has ruled with content believed to exist. 252 is the count whose destination actually holds up when measured. Both are true and they answer different questions.

## 2. One fault in the map, and it is Chat's column to rule

**Step 4 of the brief, delivered, and it did not catch nothing.** `redirect_one_hop.py` is built and committed beside the chain register (theme repo, commit `1aa9b73`), with five acceptance cases green: one per fault shape, plus a clean map proved to pass.

It reads the workbook and refuses on four shapes the chain register cannot see, because the register measures a destination against the live site and never against the map: a row redirecting to itself, a destination that is itself another row's `old_url`, a cycle of any length, and one `old_url` ruled on two rows.

**One fault in 2,596 rows: the Miscellaneous tab redirects `/` to `/`.** Its basis reads "DSRD 1 s2.1; homepage stays the homepage", which is the right ruling written into the wrong column: a homepage that stays where it is needs no redirect at all. Built as it stands, it is a loop a browser follows until it gives up.

**Nothing was changed.** `action` and `new_url` are Chat's columns under the Read Me's governance split. **The ask: rule that row.** Chat's own instinct and mine agree it should read action `gone` with an empty `new_url`, or come out of the map, but it is a ruling and not a measurement.

## 3. The publishing wall refuses every redirect write, and there is no route round it

**Step 3 of the brief, stopped, and this is the one that needs an answer rather than a fix.**

Rank Math's Redirections module is enabled on the build install and its table, `qbk_rank_math_redirections`, exists and is empty. So the destination for the work is ready.

**H9, the publishing wall, refuses the write.** Its printout, fired on a redirect insert this session rather than reasoned from the code:

```
H9 PUBLISHING WALL: blocked. This command could put content in front of the
public and carries no clearance.

Why it was stopped:
  - ground A, an explicit publishing verb: a direct database write, which can
    publish without WordPress noticing. A `wp db query` is read rather than
    refused where its SQL is ONE inline quoted statement opening on SELECT,
    SHOW, DESCRIBE or EXPLAIN and carrying no writing word; this one is not,
    so it is unread
```

**The wall is right on its own terms and I am not asking for it to be weakened.** A redirect table write is a direct database write, and ground A exists precisely because a direct write can change what the public sees without WordPress noticing.

**But the only route the wall names does not fit.** `publish_gate.py --clear` mints a clearance from page URLs measured against the machine third of DSRD 6. A redirect row is not a page and has no DSRD 6 record, so there is nothing to measure and nothing to clear. `--takedown` certifies removal facts about posts. `--override` clears pages the gate refused and needs Kain's words. None of the three describes writing 252 rows into a redirect table.

**So the redirect brief's step 3 cannot be run by Code today, on any route.** That is the machinery refusing approved work, which is the shape this project's harness says is a question for the channel and never a judgement call.

**The ask, and it is one question:** what mints a clearance for a redirect write? Three answers would each work, and this is Chat's call to bring to Kain rather than mine to take:

1. **`publish_gate.py` gains a redirect mode**, certifying the facts that actually matter for a redirect rather than the facts that matter for a page: the row is in `Redirect_Master.xlsx` with status `ruled`, its destination's five chain columns all read TRUE, the one-hop test passes on the whole map, and the redirect is 301. That is my recommendation, because it keeps every write behind a clearance and the clearance certifies something real.
2. **H9's ground A gains a narrow reviewed exception** for an insert against the redirections table alone, on the model of `h9_reviewed_scripts.json`, bound to the sha256 of the exact script.
3. **The redirects are not written by Code at all** and go in through Rank Math's own CSV import in the admin, which is outside every hook by construction. This works, but it puts 252 rows through Kain's hands and I do not recommend it.

Whichever is chosen, the gate script changes only under a commissioned brief from Chat, so nothing is built on this until one arrives.

## 4. Step 2 stopped too, and its gap is smaller but real

**The chapter 5 reset.** DSRD 6 Version 7, quoted from the canonical file this run: "Chapter 5 is therefore reset: any section 5 line measured before this version reverts to not run."

**The records carry no measurement date on a section 5 line**, so "measured before this version" cannot be read off the record. Fifty `DSRD6_RECORD.md` files exist and their section 5 lines are undated.

**The ask, and it is a yes or no:** may Code reset every section 5 line on all fifty records, rather than only the ones predating Version 7? It is the conservative reading, since a reset can only cause a re-measurement and can never create a false pass, and the re-measurement is automated. But it is a reading of a rule the record cannot answer, so it is not mine to take.

## 5. What Code owes when the three answers land

Step 3 the moment the clearance route exists, then step 5, the redirect checker on staging, which has nothing else in front of it. Step 2 the moment the reset question is answered. The 505 rows whose destinations do not exist follow their pages and are not chased.

---

OWED BACK: the ruling on the `/` to `/` row; the clearance route for a redirect write; and the yes or no on resetting all fifty chapter 5 lines. Also still owed from S103 and now blocking the publishing session twice over: the DSRD 6 section 5 item 11 exception at 89, and whether DSRD 2 section 3.2 or 3.8 governs the 85.

*No em or en dashes in this file; checked before writing.*
