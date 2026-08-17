# Question for Code — can you read the DSRDs at their real home? (from Chat, S220, 2026-07-24)

From: Claude Chat. One question, plus one finding you need to know about. This is a
read-only request — nothing is being commissioned here.

## The finding (this is the important part)

Your `CLAUDE.md` currently says:

> The specifications live in the theme repo at `docs/`. DSRDs 1–10 are mirrored
> there. Before building anything, open and read the DSRD section that governs it.

**That `docs/` mirror no longer exists.** It was created at v0.35.1 and removed at
v0.35.2, and the standing rule since then is that a DSRD is never mirrored into the
theme — the DSRDs have exactly one home and copies are treated as drift.

So your standing instruction points at a folder that is not there. We think this is
why, when Kain asked you about Knowledge Hub page specifications, you could only
find two: you were not reading DSRD 9 at all.

For the record, DSRD 9 currently holds three locked Knowledge Hub layouts — §20
Category Hub, §21 Listing Pages (32 pages, one template), §22 Individual Article —
each with a `Page Structure (top to bottom)` block list.

## The one home

    /Users/kainramsay/Documents/CLAUDE | Anthropic Ai/Claude Code (Projects)/
    Achology Website Upgrade 2026/003. DSRD's | Achology Specification Documents/

Each DSRD sits in its own subfolder there, e.g.
`DSRD 9. Design Spec Document (Page Layout Specs)/DSRD_9__Design_Spec_Document_Page_Layout_Specs.md`.

That path is on the same machine you run on, and Chat reaches it directly through
the Filesystem connector — that is where every DSRD edit this session was written.

## The question

**Can you read absolute paths outside the theme repository — specifically that
DSRD folder — from your normal working directory?**

Please answer with:

1. Yes or no, and if there is a sandbox or permission boundary, where it sits.
2. If yes: confirm you can open the DSRD 9 file at the path above and report its
   §20.1 block list back, so we know the read genuinely works rather than
   theoretically works.
3. If no: tell us what access you would need, so Kain can decide how to give it.

## Why it matters, and what happens next

If you can read that folder, the fix is a one-line change to `CLAUDE.md` — point it
at the real home instead of the dead `docs/` path — and you have all ten
specifications permanently, with no mirror to keep in sync and no copies to drift.

If you cannot, Kain will decide between granting the access and some other route.
Either way, do not recreate a `docs/` mirror in the theme; that is the failure mode
the one-home rule exists to prevent.

Any change to `CLAUDE.md` is yours to make and Kain's to approve — this note asks
the question only.

## Related change you should know about

Kain has also adopted a standing practice this session: **whenever Chat changes a
DSRD, a note goes into this channel naming what changed and why.** Two such notes
are already here from today (the locked listing breadcrumb trails in DSRD 1 §9, and
the icon rule in DSRD 10 §7). Read the channel before building against a
specification you last read some sessions ago.
