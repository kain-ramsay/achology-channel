> WITHDRAWN, Code S183, same day: Kain, on seeing it live at 0.707.550: "How these things are loading onto the page is not what I approved, signed off, or ever wanted." The signed Rise in turn (0.707.434/438) is back unchanged at 0.707.551 (commit 64e27a86). Nothing to write home; DSRD 9 section 39.10 stands as it was.

**For Chat. What this needs from you:** write Kain's S183 ruling home: the Rise in turn timings on every Knowledge Hub wall are now the quicker set below (DSRD 9, the wall standard, and wherever BRIEF__Rise_In_Turn_On_Every_Knowledge_Hub_Wall_S440's timings were recorded).

# RULING: the quicker card arrival is the standard on every Knowledge Hub wall (Kain, Code S183, theme main session, 26 October 2026)

**Kain's words.** Signing off the front page's look: "a lot of the cards are really quite slow in loading. So it does seem to me that the page is a lot slower than what it potentially could be." Then, after comparing the two on one Safari page with two tabs (now, quicker): "Yes, make the quicker card arrival the standard on every Knowledge Hub wall."

**What was found.** Measured in WebKit by the kh-front-page session at 0.707.547: every wall picture had downloaded 1 to 10 seconds before its card came into view. The wait was the arrival effect: a card started only once 8% inside the screen and 12% visible, faded over 0.6 s, each 0.07 s after the last with no cap; a typical card was fully there 1.2 s after reaching the screen, the slowest 2.5 s.

**What is now the standard (live 0.707.550, commit 706ecf9a).**
- A card starts the moment it touches the screen (no inset, no visibility share).
- The fade and rise take 0.35 s (was 0.6 s); the rise distance is unchanged.
- The stagger is 0.05 s a card and stops after the fourth, so a whole row is in within half a second.
- Unchanged: cards already in view are simply there; nothing plays under reduced motion; only the card moves.

Files: kh-subject.js section 5, kh-subject.css (Rise in turn block). Checked in WebKit on /learn/ live: a waiting card's fade reads 0.35 s.

OWED BACK: the dated line in the owning document.

*No em or en dashes in this file; checked before writing.*
