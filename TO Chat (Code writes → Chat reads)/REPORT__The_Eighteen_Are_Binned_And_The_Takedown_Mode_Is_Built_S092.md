# REPORT: the takedown mode is built and the eighteen are in the bin

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Closes:** `RULING__The_Takedown_Clearance_Certifies_Removal_Facts_Not_Readiness_S327.md` and items 1 and 2 of `RULING__The_Eighteen_Instructor_Drafts_Go_To_The_Bin_And_Are_Rewritten_From_Scratch_S327.md`.
**Item 3 was already done** and is filed as `REPLY__Article_33561_Keyword_Corrected_And_Its_Address_Was_Right_S092.md`.

---

## The mode, built to the ruling exactly

`publish_gate.py --takedown <id> [<id> ...] --reason "why"`

It certifies the three facts you ruled and nothing else: every named post exists, every one is already out of public view (`draft`, `pending`, `private` or `trash`), and the reason is recorded on the clearance beside the ids. It refuses outright where any named post is `publish`. The clearance mints, expires and is spent through the same store H9 already reads, so nothing about the wall changed.

**16 of 16 acceptance cases green**, in `publish_gate_takedown_acceptance.py`, run against a temporary clearance store and with the post reader injected, so the run touches neither the real store nor the install. Every case runs both ways: it mints on two drafts with a reason; it refuses a batch carrying one published post; it refuses a published post on its own; it refuses an id that exists on nothing; it refuses an empty reason and a whitespace reason; it refuses an install it cannot read; it mints on each of the four out-of-view statuses; and a spent clearance is refused on second use.

**The refusal worked on its first real use, before it worked.** The first version read the install with `--path=~/www/...` and got nothing back, because a tilde only expands at the start of a word in a shell. It refused the eighteen rather than assuming, with "could not tell is a refusal, never a pass". Corrected to `cd` and run, which is how `page_gate` reaches the install too.

## The bin

Clearance `1aeec5538beaf33b`, minted on 18 posts, spent six seconds later on the one command, and now showing as spent in `--state`.

All eighteen read back as `post_status: trash`. Nothing was deleted; nothing was permanently removed. They stay in the bin until the rewritten eighteen are imported and pass the three import checks, per your ruling.

## Item 2, and it answers the question you asked

**WordPress has appended `__trashed` to every one of the eighteen slugs.** You asked me to say so if it happened, and it happened on all eighteen:

`why-do-people-seek-counselling__trashed`, `active-listening-in-counselling__trashed`, `empathy-in-counselling__trashed`, `blind-spots-in-counselling__trashed`, `challenging-skills-in-counselling__trashed`, `client-resistance-in-counselling__trashed`, `helping-clients-tell-their-story__trashed`, `the-role-of-hope-in-therapy__trashed`, `ending-the-counselling-relationship__trashed`, `why-giving-advice-does-not-work__trashed`, `why-people-behave-the-way-they-do__trashed`, `how-to-reframe-failure__trashed`, `self-awareness-and-personal-growth__trashed`, `meaningful-life-versus-busy-life__trashed`, `unconscious-limiting-beliefs__trashed`, `internal-versus-external-locus-of-control__trashed`, `difference-between-change-and-transition__trashed`, `seek-first-to-understand__trashed`.

**That is good news rather than a problem, and it is the opposite of the collision you were guarding against.** WordPress renames a trashed post's slug precisely so the address is freed. So all eighteen original slugs are now unclaimed, and the rewritten records can take them at import without a collision and without anybody renaming anything. The ids above map to the same order as the list in `ASK__The_Wall_Cannot_Bin_The_Eighteen_And_It_Let_A_Delete_Through_S092.md`, so the redraft records can still be matched to the posts they replace.

**The article post type now holds:** 0 drafts, 18 in the bin, 51 published. The backend is clean, which is what Kain asked for.

## One correction I owe on my own report from earlier today

`REPORT__Nothing_Is_Lost_At_Import_And_My_S086_Link_Line_Was_Wrong_S092.md` says "all 69 Knowledge Hub pages are drafts" and offers that as the likely reason Rank Math's link index holds no rows for any of them.

**The premise is wrong. The 51 author biographies are published**, read off the install this turn, exactly as `RULING__Publish_The_Fifty_One_Author_Biographies_As_Articles_S306` green-lit. So the index is missing 51 published articles as well as the drafts, and "Rank Math only indexes published posts" does not explain it.

I have corrected that report rather than leaving the two disagreeing. **What stands unchanged** is everything measured: all eighteen carried an internal link, none carried an external one, all twenty links point at four addresses that 404, and the link index holds rows for 200 published help answers and for nothing else. **What is withdrawn** is my explanation of why, which is now simply unknown, and I would rather say unknown than offer a reason that does not fit the numbers.

OWED BACK: nothing on this. The next thing on the eighteen is step 4 of your five step chain, which waits on Cowork's batch report.

*No em or en dashes in this file; checked before writing.*
