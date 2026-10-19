# BRIEF: finish the 25 quote records' metadata. Demand evidence on every one, and two to four outcome tags where each carries one.

**From:** Claude Chat, Session 342. **Date:** 5 September 2026.
**Authority:** Kain, in Chat this session ("Yes, definitely" to holding DSRD 1 section 5.1's two-to-four outcome tags on quotes and fixing the 25 inside this run). The demand_evidence half was named as a brief of its own by the S341 handover and Code's S102 importer report.
**Run under:** the Cowork Production Harness (Version 17); the rank-math-90 skill, Part A, steps 1 to 3 (the stage 0 method, not restated here); Rule 5 (never open the master file); Rule 7 (your outbound tray is FROM Cowork). A metadata run: no body is opened unless section 3 says so.
**Input:** the 25 records in `Content Records/quote-page/` in the Content Production Factory folder (Q07009 to Q07032 from The Ultimate Life Coaching Handbook, plus Q04251). Their author keys and image_quote_text were corrected at S341 (`Batch_Report__Quote_Keys_S341.md`); the two faults below are what remain, and the gate names both on every printout.
**Board cards:** the Quote page template; the 50 instructor book quote pages.

## 1. Why this run exists

Code's quote-page importer (draft-only, registered) refuses all 25 records on two lines: no `demand_evidence` (they were drafted at S300, before stage 0 existed), and an outcome-tag count under the band (DSRD 1 section 5.1 says two to four; every record carries one). Nothing publishes on the quote page template until records can import, so these two fields stand between the template build and its content.

## 2. The demand evidence, per record

Run rank-math-90 Part A step 1 on each record's focus keyword exactly as written: the seed is the record's `rm_focus_keyword`; read the autocomplete, the People Also Ask questions, and one AI assistant's framing. Write the evidence line into `demand_evidence` in the record's field table: one line naming the three sources checked and what each showed, with the pastes kept in your run notes. Where the evidence holds up the existing keyword, that is a result and the keyword stands. Where it does not, do not change the keyword: mark the record `keyword not supported by evidence` in its `notes` field and list it in the batch report for Chat, because a changed keyword on a quote page reopens its title, its description and its register row, and that is a decision for Chat with Kain.

## 3. The outcome tags, per record

Each record's `kh_tag` list goes to between two and four tags, all from DSRD 1 section 5.6's 36 locked slugs (the same register the S341 retag run used, and `content_gate_standards.json` refuses anything outside it). The first tag stays as it is: it is the record's `lead_tag` and chooses the course cards, and it is not moved. Add the one to three tags that the quote's own words earn, read from the quote and its reading, never from the book's subject in general; a quote about listening earns `communicate-effectively` before it earns `help-others-grow`. Where `kh_tag_order` is a required field on this type, write it to match. Reading a record's body to choose its tags is the one body read this brief permits; no body is edited.

## 4. How to know it worked

Run `content_gate.py` on each of the 25 after both edits and attach the printouts to your batch report, `Content Records/quote-page/Batch_Report__Quote_Metadata_Finish_S342.md`. The two lines this brief owns must read PASS on all 25; every other line is reported as it prints, not fixed. Then one DONE file to FROM Cowork in the shape of `DONE__Retag_And_Keys_Run_S341.md`, naming the report and any records marked for Chat.

## 5. What this brief does not cover

The 25 records from The Skilled Helper that were never drafted; the quote page template build; anything in a record's body. All three have their own homes.

*No em or en dashes in this file; checked before writing.*
