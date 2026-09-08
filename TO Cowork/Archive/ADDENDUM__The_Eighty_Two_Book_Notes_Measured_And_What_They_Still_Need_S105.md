# ADDENDUM: the eighty two book notes measured off disk, and the four things every one of them still needs

**From:** Claude Code, Session 105. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Amends:** `BRIEF__Rewrite_The_Eighty_Earning_Books_As_Book_Notes_S319.md`, in this folder, and its `ADDENDUM__..._S335`. Both still govern. This file adds a measurement and Kain's priority, and changes no recipe.
**Signed by:** Kain, in the S105 sitting, in his own words: **"i want all articles that are in the backlog to be publishes and to meet our titling and rank math standards - this backlog of articles cannot extend beyond the next session"**, and then, on being shown the measurement below and told one session is not achievable: **"set next session up that way, and put the two requests to Cowork and Chat now so they are working while we are not"**.
**Board card:** Book Notes: the psychologist expansion.

---

## 1. Why this file exists

Kain wants the unpublished backlog cleared and publishable. I measured it rather than estimate it, and told him plainly it cannot be done in one session. **The single biggest reason is this set.**

**128 pieces on disk have no page on the install at all. 82 of them are yours: book notes.** The other 46 are quote pages, which are blocked on a page design that does not exist yet and are Chat's problem, not this file's.

## 2. What I measured, and how

`stage5_import_checks.py` against `Content Records/book-note`, all 149 records, this session. It reads fields, body shape and named files. Nothing was written and nothing was imported.

**All 149 fail all three checks.** Not 82 of them: all of them, the 67 already published included. So this is not a fault in the 82 that are waiting, it is the shape of the whole folder.

**The typical failure, taken from `atomic-habits-clear.md` and representative of the set:**

- **fields complete:** missing `kh_tag_order`, `featured_image`, `featured_image_alt`, `inbound_from`
- **body shape:** notes outside the body
- **named files:** `featured_image` names nothing

**One caveat I will not hide.** The same check also reports `article_type`, `source_type` and `destination_course_name` missing on every book note. Those look like article fields being demanded of a book note, so that part of the failure may be the checker rather than the records. **I have not chased it down and you should not fix records on the strength of it. The four fields named above are real.**

**108 of the 149 predate the Search and Citation Brief standard and are dated as such.** Their five S329 fields are owed at the next edit, never in a backfill, per Kain's S332 ruling. **Not a failure and not counted here.** But if you are editing one of the 82 anyway, that IS its next edit, so those five come with it.

## 3. What every one of the 82 needs before Code can import it

1. **A cover image that exists**, named in `featured_image`, with the file actually on disk under that name. Right now the field is empty or names nothing.
2. **`featured_image_alt`**, real descriptive text, not the title again.
3. **`kh_tag_order`**, alongside `kh_tag`.
4. **`inbound_from`**, at least one real internal link from a page that already exists. Across all 400 records on disk only 23 carry this at all, so it is the thinnest field in the factory.

**Plus the body shape fix**: the check reports notes sitting outside the body on every record, which is what published our own working notes as prose once before.

## 4. What is not being asked

**No rewriting of anything already published.** The 67 live book notes are not in scope here; `BRIEF__Fix_The_Seventeen_Substantive_Book_Note_Failures_S318` owns the known problems in those.

**No new titles.** Kain's S318 order stands: what already earns is brought to standard before anything new is drafted.

**No change to Recipe 1**, the five headings, or anything in the S319 brief or its S335 addendum.

## 5. The one thing worth knowing about pace

Kain's aim is that this stops being a backlog. **He was told, and accepted, that it is more than one session.** So there is no value in speed that costs quality here: a record that arrives missing its image is a record Code refuses at the gate, and that round trip is slower than drafting it complete the first time. **Complete records, at whatever rate they come, is the thing that actually shortens this.**

---

OWED BACK: nothing to me directly. When a batch is complete to the four fields above, it imports on the normal route and I will report the count. **If the `article_type` question in section 2 turns out to matter to you, ask Chat rather than guessing, and I will fix the checker if it is mine.**

*No em or en dashes in this file; checked before writing.*
