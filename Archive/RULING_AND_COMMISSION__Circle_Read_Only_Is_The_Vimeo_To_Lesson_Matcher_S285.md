# RULING AND COMMISSION: Circle is the Vimeo to lesson matcher, read only. And one obstacle you must test before it is trusted.

**DOCUMENT TYPE:** ruling plus a read-only commission, from Chat to Code. **From:** Claude Chat, Session 285. **Date:** 18 August 2026.
**Read this cold.** Everything you need is here.
**Standing constraint unchanged:** the Drive rename stays halted at 015-032, and nothing writes to Vimeo or to Circle.

---

## THE RULING

**Kain ruled at S285: the Vimeo to lesson matcher is Circle, read only.** This closes the fresh eyes review's Finding 4, which found that nothing anywhere stated how a Vimeo video gets joined to a lesson, and that the whole replacement plan sat on top of an undesigned join.

**What the ruling permits:** reading Circle through its Admin API, with a token Kain generates for the session. Nothing in Circle is created, changed or deleted. Karen's ruling that Circle needs no work is honoured, because reading is not touching.

**Duration matching is demoted to the corroborating check,** not the matcher. It still needs the Drive durations captured (the review's Finding 3), and that pass is still owed before any replacement plan is agreed.

---

## THE OBSTACLE, WHICH IS WHY THIS IS AN INVESTIGATION AND NOT YET A DATA PULL

**The project's own Circle API reference says the Vimeo ID is not in the lesson payload.** The skill file `Circle-API-Reference-SKILL.md`, in the skill library folder inside the Project Delivery System, records from Session 28 that `body_html` carries the lesson description text only, that videos are handled through Circle's featured media system, and that Vimeo URL mapping is classified "known unavailable / unresolved". Its Step 5 says the mapping is a separate unsolved task.

**Three things make that finding worth retesting rather than accepting.** It was recorded in March 2026 and Circle's Admin API v2 has had five months to change. The lesson record does carry `is_featured_media_enabled`, so featured media plainly exists as a concept in the payload, and nothing in the note says the featured media object itself was fetched and found empty. And the reference itself instructs that current observed behaviour outranks remembered behaviour.

---

## THE COMMISSION: find the join, read only, on three routes in this order

**Route one, the lesson payload.** Pull one course's sections and lessons and dump one complete lesson record whole, every field, not just the documented ones. Look for any featured media object, media ID, embed URL or Vimeo ID anywhere in it. **Report the raw field list**, because the skill file's field list may be stale.

**Route two, the featured media resource.** If the lesson record points at featured media by ID rather than carrying the URL, follow that pointer with a GET and report what comes back.

**Route three, the rendered lesson page.** If neither route carries the Vimeo ID, the ID is certainly present in the HTML the student's browser receives, because the player has to be told what to play. Read one lesson page as a signed-in reader and report whether the Vimeo ID is recoverable from it. This is a read of a page Kain already has the right to view.

**Then stop and report.** Do not pull all 2,146 lessons on whichever route works. Prove the join on one course, report which route carried it and what the record looks like, and the full pull is commissioned separately once Kain has seen that it works.

**Read the skill file before you start.** It carries the working authentication (`Bearer`, never `Token`), the same-origin constraint (the browser must be on `app.circle.so`), the pagination rules, and the twenty eight course IDs already mapped to our course numbers. It exists so this is not rediscovered.

**Token handling, from that same file, unchanged:** Kain generates an Admin V2 token for the session, it is never written into any file, and it is regenerated afterwards.

## WHAT YOU REPORT BACK

1. Which route carries the Vimeo ID, or that none of the three does.
2. One complete lesson record with its full field list, token and anything sensitive removed.
3. Whether the join is one Vimeo ID per lesson, cleanly, or whether any lesson carries none or several.
4. Your estimate of what a full 2,146 lesson pull would cost in time and calls.

*No em or en dashes in this file; checked before writing.*
