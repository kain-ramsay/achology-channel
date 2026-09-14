> CHAT DISPOSITION, S360: STAYS. Genuine open decision, three options on the table, none free for Code to pick (The Shared Rules section 8). Waits on the single fact this file names: Kain's choice of route 1, 2 or 3, or a fourth. Put to him this session; his answer travels to Code the moment it lands.

# ASK: the recorded preview route and the deploy delete each other, every time

**DOCUMENT TYPE:** ask, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Found by:** the completion hook refusing a session close twice today, on a real sitting Kain was looking at.
**Board card:** none yet; this is a process fault rather than a piece of work.

---

## 1. The two rules, both recorded, both Kain's

**The preview route, ruled S269** and written into `previews/README.md`: a preview goes onto the build site at the theme's own previews address, and Kain is given that link. The README gives two reasons and both are sound: a localhost address dies with the session that served it and leaves him holding a dead link, and a preview must never be opened over `file://` because Safari refuses to let one local file load another in an iframe.

**The deploy exclusion, added S093** in `deploy.py`: the developer tooling is never deployed, because the theme folder sits inside the public web root and everything rsync sends is readable over the web. `previews/` is on that list, and the flag `--delete-excluded` is on the rsync, deliberately and with its own comment explaining that without it an excluded file already on the server stays there forever.

## 2. What that combination actually does

The preview is placed at the recorded address. The next deploy deletes it.

Measured twice today, in one session. The completion hook refused the close with four lines beginning `*deleting previews/`, and the deploy that cleared the refusal removed the sitting Kain had been sent the link to. The second sitting, on the author mark's colour, is on the server now and the next deploy will remove that one too.

**So the rule is not "a preview lives at that address". It is "a preview lives at that address until the next deploy", and nothing says so.** A sitting Kain opens tomorrow morning is a 404 if any change shipped overnight, which on this project is most nights.

## 3. Why this is not Code's to settle

It is a question about where things live and what points at what, which The Shared Rules section 8 puts outside the technical choices Code takes on its own. Three answers are possible and each has a cost that is not Code's to weigh:

1. **Previews move off the theme, to their own folder in the web root.** The deploy never sees them, the link survives, and the addresses Kain has been given in past sessions all change shape.
2. **`previews/` comes off `--delete-excluded`.** One line, and it reopens the exact hole S093 closed: files in the web root that rsync will never clean up again.
3. **A preview is understood to be for the sitting it was built for, and nothing more.** No change to anything, and the README says so plainly instead of implying permanence. The cost is that Kain cannot reopen a sitting after the next ship.

## 4. What Code has done in the meantime

Nothing that pre-empts the answer. The current sitting is on the server at the recorded address and Kain has the link. **The next deploy in any session will remove it**, and that is named here rather than left to be discovered.

OWED BACK: which of the three, or a fourth. Until then every sitting Code builds carries the same silent expiry.

*No em or en dashes in this file; checked before writing.*
