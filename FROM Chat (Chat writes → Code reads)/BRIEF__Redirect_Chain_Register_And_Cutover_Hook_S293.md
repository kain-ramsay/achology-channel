# BRIEF: BUILD THE REDIRECT CHAIN REGISTER AND THE CUTOVER HOOK

**From:** Claude Chat, Session 293
**To:** Claude Code
**Status:** approved by Kain in session. This is a commission, not a question.
**Governing spec:** DSRD 1 §11.0 (The Chain Register), ruled S293. Read it before you start. This brief does not restate it.

---

## WHY THIS EXISTS

The redirect map proves one thing: that an old address points at a new one. It proves nothing about whether that new address is any good as a destination.

The live site currently has 2,676 pages that Google has crawled and refused to index (Search Console Coverage export, 18 August 2026). A 301 into a page Google will not list spends the exact equity the redirect was built to preserve, and it fails silently, because the redirect itself still returns 301 and passes every test we run today.

Kain's ruling this session, now DSRD 1 §10.1: every reader-facing page on achology.com is indexable. The quote corpus specifically, because it is a major redirect destination. That ruling only means anything if something checks it, per address, and refuses when it does not hold.

---

## WHAT TO BUILD — THREE THINGS

### 1. The five destination columns in the Redirect Master workbook

The workbook lives in the Redirect Map | Master File folder inside the spreadsheets folder. Extend it. Do not create a second file.

Each existing row gains five columns, defined in DSRD 1 §11.0:

`dest_built`, `dest_indexable`, `dest_in_sitemap`, `dest_schema`, `dest_routes_to_course`

The table in §11.0 says what each records and where the answer comes from. Read it there.

### 2. The script that fills them and fails

It reads the workbook, checks each destination against the build site, writes the five columns back, and **exits non-zero where any row's chain is incomplete**.

The failing exit is the point. A register that only reports is a register that goes stale, which is how the five facts came to be missing in the first place.

Prove it the way you prove any gate: construct a row you know is broken, watch it refuse, keep that printout. A first-run pass on a check you wrote yourself is not evidence.

### 3. The cutover hook

The build site is set to hide from search engines while it is not public. That flips once, by hand, at go-live.

If that flip is missed, the entire new site publishes invisible, and nothing about the site will look wrong. Nobody would find out for weeks.

That deserves a hook on your machine, not a line on a checklist. It runs in the same sitting as the canonicals and the sitemap check (DSRD 6 §5).

---

## WHAT IS NOT YOURS HERE

The five columns and their meanings are set. If one of them cannot be checked mechanically, say so through the channel rather than substituting a different check.

---

## ONE THING THIS CHANGES ON WORK ALREADY DONE

**DSRD 6 is now Version 7, and its §5 gained item 10 in the same session as this brief.** That item is the page-level half of this commission: a page that is a redirect destination cannot be called ready until its five chain facts are recorded.

**Widening a chapter resets it.** DSRD 6's own rule, at the head of the document, says every existing pass on a widened chapter reverts to **not run**, in the same edit. Version 7 widened §5 and touched no other chapter, so:

- Every `DSRD6_RECORD.md` carrying a §5 line measured before Version 7 has that line reverted to `not run`, dated.
- Every other chapter on those same records stands untouched. This is a §5 reset, not a re-gate.
- The Reviews page is the first affected and may be the only one; you hold the records, so the count is yours to establish rather than mine to guess.

It is a handful of pages today. That is the whole reason for doing it now.

---

## ONE THING I NEED BACK

The `dest_routes_to_course` column is the one I am least sure is mechanically checkable. It asks whether the destination page carries at least one route to a course page or to the free tier signup.

If the theme emits those links in a way a script can recognise reliably, say so and build it. If it does not, tell me what it does emit and I will re-specify the check against what actually exists rather than what I assumed.

---

## ALSO WRITTEN THIS SESSION, FOR YOUR PICTURE

Six specification changes landed at S293. You do not need to act on all of them, but your next session should read a current picture:

- **DSRD 1 §10.1** — Indexing Policy. Every reader-facing page indexed. Only the internal search results page, post-signup thank-you pages, and the 404 carry noindex, all `noindex, follow`. Full per-type register in the section.
- **DSRD 1 §10** — retitled Indexing and XML Sitemap Configuration; old §10.1 and §10.2 renumbered to §10.2 and §10.3.
- **DSRD 1 §10.4** — Publication in Waves. After cutover, volume content publishes 50, then 200, then 500, then open, read against Search Console fourteen days apart, stopping where a wave indexes materially worse than the one before. Cutover itself is exempt.
- **DSRD 1 §11.0** — The Chain Register, which this brief commissions.
- **DSRD 6 Version 7** — §5 gains item 10 and chapter 5 resets, as set out above.
- **Cowork Production Harness v5** — the unique value test. No new rule; Rule 9's evaluator now grades it last and alone.

---

*End of brief.*
