> **CODE DISPOSITION, S097: WAITS ON one fact a machine can test, that a page exists on the install at `/learn/helping-people/articles/psychological-blind-spots/`.** Read in full at H6's block and not started: Kain was live in the sitting writing the profile bios and asked for that first, so this is next in front of anything else. Nothing in it is blocked. **Your correction is accepted and mine was wrong: the inbound links are 45, not 42, and 15 point at the two missing book notes, not 14.** My count read `inbound_from` per record and missed that three records name three sources each where I had counted two; the S097 report says 42 and is superseded by this line. **The order when it runs:** rebuild the register first (all three `post_name` and `address` values moved), then import the three, then re-import the two biographies and the nine article records carrying the placed sentences, then the stage 6 check once over everything, expecting 30 of the 45 present and the other 15 waiting on the two book notes.

# BRIEF: import the three held instructor articles, and re-import the two author biographies

**From:** Claude Chat, Session 334. **Date:** 3 September 2026. **For:** a factory session. No theme file is touched.
**Approved by Kain at S334**, decision by decision: the three new focus keyphrases were put to him one at a time with their evidence and he ruled each one.
**Board cards:** the eighteen instructor articles; the search and citation layer.

---

## Why this exists

Fifteen of the eighteen instructor articles are live. Three were held at S316 because their keyphrases failed stage 0, and they have sat since. Kain's aim tonight is nine articles in his own voice and nine in Gerard Egan's, live. This closes that.

**Run the register rebuild first.** All three records changed their `post_name` and `address`, so `KEYWORD_REGISTER.csv` is stale the moment you read this. Rebuild it from the records before you import, per the S316 gap list item 4.

## The three, with what changed and why

Each was checked with a live search this session. The evidence line is written into each record's new `demand_evidence` field, and each says plainly that autocomplete and People Also Ask were not read, because Chat has no browser: three sources short of the full stage 0, named rather than implied. `keyphrase_state` reads `evidenced S334` on all three.

**I04, Gerard Egan.** Was `blind spots in counselling`, which returns the counsellor's own blind spots on every result: supervision, countertransference, the therapist's bias. Never the client's, which is what the article is about. Now `psychological blind spots`, the live phrase for the parts of a personality obvious to everyone but the person. Title, address, description, excerpt, image alt and five body mentions all moved with it. New address `/learn/helping-people/articles/psychological-blind-spots/`.

**I14, Kain Ramsay.** Was `meaningful life versus busy life`, which almost nobody writes: the live opposition is busy against full. Now `busy but not fulfilled`, the problem-side phrase for the state the article opens in, per the vault note People Search From Two Perspectives. New address `/learn/wisdom-for-life/articles/busy-but-not-fulfilled/`.

**I18, Kain Ramsay.** Was `seek first to understand`, which is Stephen Covey's habit five on every result, so the page would have sat behind a famous book collecting his readers. Now `persuade someone who disagrees`, the reader's actual situation and the question the piece answers. New address `/learn/helping-people/articles/persuade-someone-who-disagrees/`. Covey is still named and credited inside the body, which is correct: the article always rested on him and now says so without competing for his phrase.

**None of the three has ever been published**, so no redirect is owed on any of the three old addresses.

## Their gate state, measured this session rather than claimed

Chat ran `content_gate.py` on each record before and after. All three went from failing on their keyphrase to **two failures each, and both are shared with the fifteen already live**: the five S329 brief-standard fields (`search_intent`, `reviewed_by`, `update_cadence`, `query_variants`, `schema_type`), and no external link to the source. Under Kain's ruling that a record is held to the standard it was written to, they publish alongside their brothers at the same bar. Density, keyword placement, title and description lengths, headings, word bands and paragraph shape all pass.

## The two biographies, and why they need re-importing

Under Kain's S334 ruling on the stage 6 finding, Chat has written the inbound sentences into the records that own the words rather than patching them onto the install.

**`Author_Biography_Gerard_Egan_S298.md`: eight sentences placed.** **`Author_Biography_Kain_Ramsay_S298.md`: seven placed.** Each sits inside the passage it belongs to, carrying its link. Both records were gated before and after: the same failures, none new, both still inside their word bands.

Re-import both, then re-run your stage 6 inbound link check. Fifteen of the forty five should now report present.

**One correction to your S097 report, measured across all fifteen records this session:** the total is **45, not 42**, and **15** of them point at the two missing book notes, not 14. Three per record across fifteen records.

## The nine article records, added after this brief was first written

Kain ruled at S334 that Chat should place the placeable sentences rather than leave them, so the article-to-article half is done too. **Fifteen more sentences are now in nine instructor-article records**, each as its own short paragraph immediately before the closing "What Could You Do With These Ideas?" section, which is where a reader is already being pointed onward: I01 (3), I02 (3), I03 (2), I05 (1), I10 (1), I11 (2), I12 (1), I13 (1), I16 (1).

**Every one was gated before and after.** No record gained a failure. Two records improved: I01 and I02 dropped a failure each, because the added words pulled their keyword density down out of the old 1.5 to 1.8 band and into the current 1.0 to 1.5 one. Several others still fail density from ABOVE for the same reason, which is a retro-pass fact about records written to the old band and not something these edits caused.

**So 30 of the 45 are now written into their source records and ready to go live at your re-import.** The remaining 15 are the ones pointing at The Skilled Helper and The Ultimate Life Coaching Handbook, and they land when those two book notes pass the gate and import.

**Re-import all nine of those records too**, alongside the three held articles and the two biographies, then run the stage 6 check once over everything.

---

OWED BACK: the register rebuild's row count, the import result for the three, the re-import of the two biographies and the nine articles, and the stage 6 re-run showing how many of the 45 are now present.

*No em or en dashes in this file; checked before writing.*
