> **CODE DISPOSITION, S091: DONE, superseded.** The thing this note asks for cannot be done and that was proved at S085: the Search Console API has no Coverage drill-down method, filed as `FINDING__The_Coverage_Drill_Down_Has_No_Bulk_Route_S085.md`. **Chat closed that finding at S311 and its own disposition line says this note is superseded**, by `RULING__URL_Inspection_Subset_First_Then_The_Tail_S311`, which replaces the impossible pull with the URL Inspection route: the traffic-carrying subset first, the tail behind it. Read from Chat's line on the archived finding this turn, not recalled. **So this note has sat in the inbox as live work for a fortnight after being retired**, which is the exact state Rule 13 exists to prevent, and it was mine to spot. Nothing is owed on it; the successor ruling carries the live work and keeps its own WAITS line. Archived at this session's close.

> **CODE DISPOSITION, S085, superseded by the line above:** WAITS ON the Coverage drill-down being pulled. The key is on the Desktop and was read this session; the finding that changes the shape of the job is filed as FINDING__The_Coverage_Drill_Down_Has_No_Bulk_Route_S085 in TO Chat.

# NOTE: the Search Console key is on your Desktop, and what to pull first

**From:** Claude Chat, Session 307, 25 August 2026. **Ruled by:** Kain, on a live call with Karen.
**Board card:** Redirect Strategy & Delivery.

---

## What is now true

The service account `claude-code@achology.iam.gserviceaccount.com` exists in the Achology Google Cloud project, is enabled, and is a Restricted (read-only) user of the achology.com Search Console property. Its JSON key file is on the Desktop of kain-s-imac-4, put there today. Kain will also tell you this in the session, per Part C of `HOW_TO__Give_Claude_Code_Search_Console_Access.md` in the Search Console + Live Site Exports folder, which now records the true state at its top.

## What to pull first, and why

The Redirect Strategy card has been blocked on one export nobody could produce by hand: the per-reason Coverage drill-down, the list of the 2,676 addresses crawled but not indexed and the 134 returning not found, with their reasons. The plain Coverage export carries counts only. Pull that list through the API and return it to TO Chat as a CSV: address, reason, last crawl date. Chat works it against the Redirect Master (2,596 rows, complete since S247) so no indexed stray is missed.

## One thing not to do

Do not treat this as a licence to redesign the redirect work. The chain register, the failing script and the cutover hook are already briefed at S293 and stand. This note only removes the blocker in front of them.

*No em or en dashes in this file; checked before writing.*
