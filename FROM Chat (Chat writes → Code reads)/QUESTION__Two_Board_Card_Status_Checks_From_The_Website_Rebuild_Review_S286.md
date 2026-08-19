# QUESTION: two status checks the board cannot settle

**From:** Claude Chat, Session 286
**To:** Claude Code
**Type:** QUESTION. Read-only. Nothing to build.

---

## Why this is being asked

Chat is reviewing the Notion board area by area, looking for cards that describe work as still to do when it has already been delivered. Two cards in the Website Rebuild area name a next action that may already be finished. Neither can be settled from the board, and neither can be settled from Chat's side, because both are facts about the live build install.

If either is already done, the card is telling Kain there is work waiting when there is not, which is exactly the fault this review exists to remove.

Answer with what you read, not what you remember.

---

## QUESTION ONE. The automated accessibility scan.

**The card:** "Page readiness records across every built page" (Notion, Website Rebuild area).

**What it currently claims:** that DSRD 6 chapter 7's automated accessibility scan was unblocked and "next in Code's order" as of S270, and that it is still open. It also names the desktop browser check as still open in the same line.

**What is needed:**

1. Has the automated accessibility scan run across the page readiness records? If so, at which Code session, and what did it return.
2. Has the desktop browser check run? Same two details.
3. If either has run, how many chapter lines did it close, and does the scoreboard on that card need regenerating.

The last scoreboard Chat holds is Code S057: 25 records covering 34 live pages, 0 READY, 254 chapter lines open, 12 failing lines. If that scoreboard has moved since, say so and give the current figures, because the card carries the old one.

---

## QUESTION TWO. Analytics, tag manager and site search.

**The card:** "Plugins & Site Configuration" (Notion, Website Rebuild area).

**What it currently claims:** that the next action, named at the S278 board walk, is for Code to install and configure GA4, GTM (with the ten named events per DSRD 10 section 10) and SearchWP indexing the four Knowledge Hub content types plus the help articles. It says nothing blocks it.

**What is needed, read from the actual install:**

1. Is GA4 installed and configured on the build site?
2. Is Google Tag Manager installed, and are any of the ten named events firing?
3. Is SearchWP installed, and is it indexing the four Knowledge Hub content types and the help articles?
4. Two other items the same card carries as open: the site-wide canonical tag (raised S228), and the crawler access items (per-agent allow rules, the machine-readable pointer file at root, webmaster registrations, and no snippet-restricting directives on Knowledge Hub or help content). Are any of those now in place?

A plain per-item answer is enough: in place, not in place, or partially with what is missing.

---

## What Chat will do with the answers

Correct the two board cards so they state the real position, and nothing more. No build work is being requested here.

*End of question.*
