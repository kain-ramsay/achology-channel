# BRIEF: teach the content gate two things the workbook standard needs

**From:** Claude Chat, Session 325. **Date:** 1 September 2026.
**Ruled by:** Kain, S325, in the sitting, on a rendered comparison of two options.
**Files:** `content_gate.py` and `content_gate_standards.json`, both at the root of the Content Production Factory folder.

## What happened, so this stands alone

The workbook template was written into DSRD 2 section 3.4 this session. Its shape:

- Five fixed headings, word for word, in order: About This Workbook, Self-Assessment, Core Content, Consolidation, Next Step. Fixed because the gate reads them.
- Content-named sub-headings are allowed inside Core Content and nowhere else.
- The whole workbook sits inside a band of 700 to 2,000 words.
- The five per-section guides add up to exactly those two ends: 75, 100, Core Content 350 to 1,650, 100, 75.
- **One rule sits on top: Core Content is at least half the whole workbook.**

The evidence it was ruled on is the worked example, The Ladder of Inference workbook, at 684 words with Core Content at 349, which is 51 per cent.

A `workbook` entry is already written into `content_gate_standards.json`, with its own `_gate_support_required` note saying what follows. It parses; I re-read the file after writing it to prove that.

## The two things the script cannot do

**1. A section guide that is a range.** `run()` reads each section's guide as a single number and tests `abs(n - guide) <= max(guide * tol, 25)`. Core Content's guide is `[350, 1650]`, because DSRD 2 gives it a range rather than a figure. As the script stands, that entry would raise rather than measure.

**2. The half rule.** The standard carries `"section_min_share": {"Core Content": 0.5}` and nothing reads it. It is the rule that actually protects the type: a workbook that spends more words framing than working has failed its own purpose, and every other check can pass while that happens.

## What I am asking for

Teach `run()` both, in the same shape you used for `section_count` at S090:

- Where a section's guide is a two-number list, pass when the count sits inside it inclusive, and report `n words (standard lo to hi)`. Where it is a single number, nothing changes.
- Where the standard carries `section_min_share`, check each named section's word count against that share of the counted body total, and report the share as a percentage so a near miss is readable.

Both are additive. No existing type carries either key, so no existing record's result moves.

## How to know it worked

Run the gate against the worked workbook, which is exhibit 03 in the Educational Publishing System folder's worked example folder. It is not a content record and carries no fields, so the field checks will complain; the two lines that matter are the Core Content section line, which should pass at 349 inside 350 to 1,650 or fail by one word and prove the range is genuinely being read, and the new share line, which should read 51 per cent and pass.

**If it fails by that one word, do not move the standard to fit it.** Tell me, and Kain rules whether the floor is 350 or 340. The number came from the render he approved and it is his.

## What is not being asked

Nothing about the workbook's landing page, its upload columns, or its import. No workbook record exists yet. The `workbook` entry's `required_fields` list is my reading of the type and is not confirmed against the built theme; when the first workbook is ready to import, its column contract goes through `upload_contracts.json` and is confirmed with you then.

*No em or en dashes in this file.*
