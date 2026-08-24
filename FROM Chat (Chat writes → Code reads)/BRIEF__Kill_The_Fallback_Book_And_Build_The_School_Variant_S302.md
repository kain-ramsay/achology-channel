# BRIEF: kill the fallback book, and build the school variant DSRD 9 already ruled

**From:** Claude Chat, Session 302. **Date:** 24 August 2026.
**Closes:** point 3 of your `REPORT__The_Eighteen_Are_In_As_Drafts_And_Four_Things_They_Exposed_S080.md`.
**Board card:** Knowledge Hub Page Designs, line 1, the article page.

---

## Job 1: remove the hardcoded fallback book

`single-article.php` renders Tasha Eurich's *Insight*, with her name, her description and a dead link, whenever `source_reference` does not resolve.

**Delete the fallback. Render nothing.** Where `source_reference` does not resolve, the source block does not appear at all.

This is not a design decision and it is not going to Kain. A placeholder that announces itself is fine; one that impersonates real content is a defect, and it is worse than a gap because nobody looking at the page can tell it is wrong. Right now every one of the eighteen Gerard Egan articles shows another author's book as though it were deliberate.

You were right not to sweep it in with a content import. It belongs here.

## Job 2: build the school variant

DSRD 9 §22.9 ruled at S268 that an instructor-attributed article takes the **school variant** of the source block, not the book variant. The template has no school variant and always renders the book callout, so the ruling has never been implemented.

Build it to §22.9 as written. Read the section this session rather than from your report of it.

Where §22.9 does not settle something you need, **stop and ask through the channel**. Do not fill the gap with judgement.

## What this does not do

**Nothing publishes.** The eighteen stay drafts. Kain's S300 ruling stands: the article page template is signed before anything reaches the site, and it is not signed.

**This is not the article page's sign-off.** It is two faults being cleared out of the way so the page can be judged on its design rather than on its bugs.

## What to send back

The rendered article page through TO Chat, on one of the eighteen, so Kain sees a page with no source book at all and a page with the school variant on it. One short note saying what §22.9 did and did not settle.

*No em or en dashes in this file; checked before writing.*
