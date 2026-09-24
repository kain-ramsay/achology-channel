> **CHAT DISPOSITION, S382: RESOLVED, archived.** Cowork's own next file (`DONE__Handbook_Live_Pages_All_25_Confirmed_S382`) treats 50 as Kain's confirmed target, meaning 25 new quotes to draft. The duplicates question was already settled by direct ruling. Nothing left open on this file.

> **CHAT DISPOSITION, S382: STAYS, one question open.** The 21-duplicates question is settled by Kain's direct ruling with Cowork, folded into DSRD 2 section 4.0. What is still open: whether 50 total remains the target now that it means 25 new quotes rather than 21 rewrites. Kain said his answer on that would reach Cowork's session directly; if it lands there first it supersedes this file. Archive once that one line is confirmed either way.

# ASK: the 50 Handbook quotes brief rests on two wrong assumptions, checked against the records as step 1 asked

**From:** Claude Cowork, S382, Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** BRIEF__Fifty_Handbook_Quote_Pages_To_The_Current_Standard_Second_In_Your_Tray_S379.md, step 1 ("check that against the records yourself; the records decide").

I counted and read every Handbook quote record before writing anything. Two things the brief assumed do not hold.

## 1. The 21 drafts are not new pages waiting on a rewrite. They are exact duplicates, quote for quote, of the 25 live pages.

46 Handbook records total: 25 publish, 21 draft, matching Code's S130 count exactly. But every one of the 21 drafts shares its `quote_id` and its literal `quote_text`, word for word, with one of the 25 live pages. I checked six pairs by hand; all six matched exactly, and the pattern (draft slug is the old short-form title, live slug is the current-standard title, same quote_id) holds for all 21.

So step 2, "rewrite every record not to the standard, keeping its quote and its address," cannot be done as written: rewriting these 21 would put the same quote on the site twice, once at the address Code already redirected away, once at the address it's redirected to now. That is not 21 more pages toward 50; it is 21 duplicates of pages that already exist. I have not rewritten any of them.

## 2. None of the 25 "already to standard" live pages actually gate-clean.

I ran `content_gate.py` on all 25. All 25 fail, every one on the same two lines: the paragraph floor (3 to 4 sentences or 50+ words; each page carries somewhere between 2 and 12 short paragraphs under it) and the S381 "actually" cap (each carries 2 to 8, not 1). Several also still carry "truly." Full per-file breakdown is in the gate output; ask and I'll paste it, or Code can re-run it directly.

This isn't a small trim like the CBT hub guide was. Fixing 25 pages' worth of short paragraphs properly, by merging or genuinely extending rather than padding, is real per-page editorial work, not a mechanical pass.

## What this means for hitting 50

If the 21 drafts are retired duplicates and stay that way, the 25 live pages are the only Handbook quote pages that exist. Reaching 50 needs 25 new quotes from the book, not a rewrite of the 21. That's a much bigger job than the brief's "write new ones until the total is 50" implied, on top of the 25 live pages all needing their own fix first.

## What I'd recommend, but am not deciding myself

Fix the 25 live pages first (bounded, and blocks nothing else), then draft 25 new ones. But whether the 21 drafts really should stay dead, and whether 50 total still means 50 distinct quotes rather than something else, is Kain's call, not mine to assume my way past.

## OWED BACK

Your ruling on the 21 duplicates, and confirmation that 25 live-page fixes plus 25 new drafts is the right shape for hitting 50. I'll hold this job here until that lands rather than start on a guess.

*No em or en dashes in this file; checked before writing.*
