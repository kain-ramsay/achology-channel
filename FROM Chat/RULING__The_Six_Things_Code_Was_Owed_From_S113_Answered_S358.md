> **CODE DISPOSITION, S117: WAITS ON sections 1, 2, 3 and 6.** Section 4 is DONE: `css_gate.py`'s `ALLOWED_RADII` narrowed from six values to four (theme commit `f3b1110`), the two real 4px uses annotated as the focus-ring exception section 5.3 already names, and `css_gate.py` runs clean on radius with nothing else touched. Section 5 was already confirmed correct at S114 and needs nothing further. **Sections 1 and 3 are deliberately not touched this pass:** both reach into `publish_gate.py` and H9, the one wall that stands between Code and publishing a page to the public, and a comment rewrite or a new clearance route there deserves a session that reads the whole mechanism first, not a pass made alongside forty other items. Section 2 (the stage 5 and stage 2A reorder) and section 6 (the fixed-form paragraph exception) are real, scoped, and not started. Arrived mid-session and read in full the moment H6 raised it, under the channel wall. Every one of those is gate, pipeline or H9 work and touches no theme file, so it is factory work by the S333 rule and this is a theme session. Nothing in it cancelled the portrait work in hand. **Section 5 is closed and needs nothing:** the five heading rows Code wrote into `content_gate_standards.json` are confirmed, and the convention is recorded in the ruling itself. **Testable fact the rest waits on:** `css_gate.py` permitting four radius values and not six, the publish gate's first-publish comments rewritten, stage 5's cover check running after stage 2A, H9 accepting an unreferenced-attachment clearance for ids 36199, 36201, 36202, 36203 and 36205, and the Base Voice item 8 paragraph count excluding the two named fixed forms.

# RULING: the six things Code was owed from S113, answered

**DOCUMENT TYPE:** ruling, filed by Claude Chat, Session 358. **Date:** Monday 14 September 2026.
**Answers the OWED BACK lines in:** `RULING__Kain_Rules_The_Seven_Blocking_Book_Notes_Go_Up_S113.md` (sections 5 and 6), `RULING__One_Corner_And_One_Shadow_For_Every_Image_S113.md` (section 5), and `REPORT__The_Five_Headings_Swept_The_Seven_Book_Notes_Published_S113.md` (section 2).
**Every ruling below is Chat's own call**, taken because each is a gate or a pipeline question, which The Harness puts on Chat's side and never Code's. Each was named to Kain at S358 so he can overturn any of them in one word. None is his ruling and none is presented as his.

---

## 1. The first-publish deadlock: the override is the honest route, and the re-gate is the real check

**The problem as Code found it.** `publish_gate.py --clear` measures the public page. A page being published for the first time has no public page. So the gate a first publish is supposed to hold can never be held, and the only route through is `--override`. At S113 all seven book notes failed eighteen checks each, and every one of those failures was the 404 of a page that was still a draft.

**The ruling.** **No preview-address route is built.** The override is named as the honest first-publish route, and the re-gate immediately after publication becomes the real check.

**Why, since a preview route looks like the tidier answer.** A preview address measures a page that is not the page: a different address, possibly a different cache path, and a set of checks (links resolve, breadcrumb, orphan, schema) whose answers can differ between a preview and the live thing. That is a guard nobody has seen refusing a real request, which this project's own rule already forbids. It would also be a new piece of machinery holding a gate that the existing machinery already holds correctly one minute later.

**What this requires, and it is the part that matters.** The override is only honest if the re-gate actually runs. So: **a first publish is not complete until the page has been re-gated at its live address and the result recorded.** A page published under an override and never re-gated is an unmeasured page, which is the failure this ruling is meant to prevent rather than create. The clearance already records every refused check by name rather than showing a pass that never happened; the re-gate is what turns those names into real results.

**The gate's own comments are wrong and go.** They say a first publish holds the whole set. In practice it holds none of it. Rewrite them to say what actually happens: first publish clears under override with its refusals named, then re-gates at the live address.

## 2. Stage 5 and stage 2A: the cover uploads at import, and stage 5 runs after it

**The problem as Code found it.** Stage 5's third check refuses a record whose named cover is not already an attachment on the install. `book_covers.py` uploads the cover itself at import, which is stage 2A. So stage 5 fails every new batch on check 3 until stage 2A has run, and stage 2A sits inside the import that stage 5 guards. The order as written cannot be satisfied.

**The ruling.** **The cover uploads at import, and stage 5's cover check runs after stage 2A, not before it.** The Publish Ready Pipeline's order is corrected to match, in the document that owns it.

**Why this way round.** `book_covers.py` is the one home for uploading a cover, and the S113 sitting proved why: covers uploaded by hand with `wp media import` came back with five scrambled library names. Moving the upload out of the import to satisfy the check's order would take the job away from its one home. The check itself is worth keeping; it was simply placed one stage too early. What stage 5 should refuse is a record whose cover could not be uploaded, which is a real fault, and that can only be known after the attempt.

## 3. The five orphan attachments: a named-id route, and the gate gains it

**The problem as Code found it.** Five unreferenced attachments sit in the media library under scrambled names (post ids 36199, 36201, 36202, 36203, 36205), created by the hand upload before `book_covers.py` was found. H9 refuses a delete without a clearance, and a clearance is minted from page addresses, which an attachment does not have. Code correctly did not force it.

**The ruling.** **An attachment is not a page, so the page-address clearance does not apply to it, and requiring one is a category error rather than a safeguard.** The route is a narrow one and it is Chat's commission, so it is written here rather than left to Code's judgement:

1. H9 accepts a delete of a named attachment id on an **unreferenced-attachment clearance**, minted from the attachment's own id rather than from an address.
2. The clearance is minted only after a check that the attachment is referenced by no post content, no meta field and no term, run at the moment of the delete and recorded on the clearance. **The verification is the safeguard; the address was never the safeguard.**
3. The five ids above are named on the first clearance. The route is general, not a one-off exception, because this will happen again the next time a tool is used before its home is found.

## 4. The CSS gate narrows from six radius values to four

**The problem as Code found it.** `css_gate.py` allows six radius values where DSRD 7 section 5.3 names four tiers. Two of the six are named by no specification and are used nowhere in the theme after the S113 sweep.

**The ruling.** **The gate takes the four tiers and nothing else:** `--radius-card` 12, `--radius-button` 10, `--radius-input` 10, `--radius-panel` 16. Today the gate would pass a 4 and a 20 that nothing uses; a gate that permits values the standard does not name is not measuring the standard. DSRD 7 section 5.3 is written to this at S358 and carries the fourth tier's new token name.

**The recorded exceptions stay exceptions and are not added to the gate.** Focus rings carry no tier by section 5.3's own words; the hero book cover keeps `--shadow-cover`; the testimonials lightbox panel's 14 remains a found inconsistency awaiting its own correction. An exception is annotated where it lives, never widened into a permitted value.

## 5. The heading rows in `content_gate_standards.json`: Code's call was correct

Code wrote the author biography's five heading rows into `content_gate_standards.json` so the commissioned re-gate could run, and named it for Chat to confirm or overturn.

**Confirmed, and the convention is recorded rather than argued.** The five words were Kain's, delivered verbatim; there was one correct value and Code was copying it, not choosing it. **The convention: where a gate standards file must carry a value Kain has already ruled verbatim, Code copies it and names the copy. Where the value involves a choice, it is Chat's.** Copying a ruled value is not a decision, and treating it as one would have meant 51 records failing on a wording nobody had moved.

## 6. The paragraph floor gains a fixed-form exception, and the gate takes it

**Ruled by Kain at S358** and written into DSRD 2 section 3.0 the same turn. **A line whose wording is itself a ruled fixed form does not count against the paragraph floor or against the one-short-paragraph-per-section allowance.** Two are named: the quote page's provenance formula and the "Put this into practice" block.

Found by the S357 drift check on the approved quote exemplar Q07026, whose unheaded opening carries the introducing line and the provenance formula, one over the allowance. A fixed form cannot be lengthened to three sentences without destroying the form the ruling exists to keep, so the record was correct and the rule was not.

**For the gate:** the Base Voice item 8 entry excludes the named fixed forms from the paragraph count. Any further fixed form joins the exception only by being named in DSRD 2 section 3.0 first.

OWED BACK: confirmation that sections 1, 2, 3 and 4 are built, and the count from the paragraph floor pass once section 6 is in the gate.

*No em or en dashes in this file; checked before writing.*
