> CODE DISPOSITION, S116: WAITS ON the new preview folder existing in the web root, outside anything `deploy.py` touches, with one preview built inside it and still reachable after a deploy. Read in full the moment it arrived, mid-session, under the channel wall; it is a change set of its own and this sitting was inside the responsive layer when it landed. Testable: this file goes DONE when that folder exists on the server and a preview address inside it survives a deploy.

# RULING: previews move off the theme, to their own folder in the web root

**DOCUMENT TYPE:** ruling, filed by Claude Chat, Session 360. **Date:** Monday 14 September 2026.
**Answers:** `ASK__The_Preview_Route_And_The_Deploy_Delete_Each_Other_S114.md`, section 4's three options.
**Kain's word, given live in chat this session:** "option 1 makes good sense."

---

## What is ruled

**Route 1 of the three.** Previews move out of the theme folder entirely, into their own folder in the web root, outside anything `deploy.py` touches. A preview built tonight survives every deploy that follows it, and Kain can reopen a sitting days later rather than finding a 404.

**Route 2 (taking `previews/` off `--delete-excluded`) is ruled out.** It would reopen the exact hole S093 closed on purpose: an excluded file already on the server staying there forever with nothing to clean it up. Not worth trading for this.

**Route 3 (leave it, document the expiry) is superseded by this ruling.** It was the cheapest option and cost nothing to build, but it meant a preview link was usually dead by the time Kain next opened it, since deploys run most nights on this project. Kain's "yes" to route 1 closes that cost.

## What this asks of Code

1. A new folder in the web root, outside the theme, to hold previews. Named however fits the site's existing structure; `deploy.py` never lists it, excluded or otherwise, so it is never touched by a deploy in either direction.
2. `previews/README.md` (or wherever the preview route is documented) rewritten to describe the new location and to drop the old warning about a preview dying with the session, since that is no longer true under this route.
3. Every existing preview address Kain has been sent changes shape under this move. Nothing is owed to hunt down old links in past channel files; this is a going-forward change, not a retrofit of history.
4. Confirm the fix by building one preview, deploying once, and checking the preview is still reachable afterwards. That is the test the ASK file's own reasoning calls for: a guard nobody has seen refusing a real request is not proven, and the same is true in reverse here, a fix nobody has seen surviving a real deploy is not proven either.

---

OWED BACK: confirmation once built, and the test in point 4 run and reported.

*No em or en dashes in this file; checked before writing.*
