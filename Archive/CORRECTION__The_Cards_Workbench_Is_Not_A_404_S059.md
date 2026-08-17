**DISPOSITION (Chat, S276, 17 August 2026): acted on and archived.** The withdrawal of reason 1 and the one blocker that still stands were written onto the board card "The Card and Chrome Sweep", verified by read-back. The stale claim that /cards/ is a 404 is struck from Chat's outstanding list in the S276 handover. The live question this file leaves open, the shape of the gate block written into COMPONENT_DATA__review-card.json, is Chat's to answer and is named to Kain in this session's opening message. Cards moved: 1.

---

# CORRECTION: the /cards/ workbench is not a 404, and the sweep is not blocked on it

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Corrects:** `REPORT__The_Gate_Now_Reads_Data_Files_And_Here_It_Fails_S059.md`, section 2, reason 1.
**Why it matters:** the corrected reason makes the card and chrome sweep startable, and the uncorrected one would have sent Chat looking to rebuild a page that already works.

---

## What I said

> "**No specimen.** `/cards/` is a 404. The course card renders nowhere a gate can open it."

## What is true

**The page exists, is published, and renders.** Post 10903, slug `cards`, status publish. Fetched with its key this session: **HTTP 200, 114,800 bytes, six course cards on it.**

The 404 is a deliberate guard, not an absence. `functions.php` defines `ACHOLOGY_WORKBENCH_KEY` and returns 404 to any request for `/cards/` that is neither logged in nor carrying the key, which is exactly right for a workbench on a public domain. **The gate already knows this and already passes the key**, at `component_gate.py` line 820 via `PG.with_workbench_key()`.

## How I got it wrong

I fetched `/cards/` as an anonymous visitor, saw 404, and concluded the page was gone. **The evidence was real and the inference was wrong**: I tested the guard rather than the page, then wrote the conclusion into a report as a fact.

The tell was in front of me. My own gate's source carries a comment explaining the key, and I had read that file the same session in order to re-point it at data files.

## What this changes, and what it does not

**Changed: reason 1 of three is withdrawn.** The course card has a working specimen.

**Changed: the sweep is startable.** Twenty five components need Kain's eye in Safari and the page they render on works today. Nothing has to be rebuilt first.

**Not changed, and this was always the load-bearing reason: `COMPONENT_DATA__course-card.json` carries values with no selectors**, so nothing in it can be compared against a built page. That is a property of the record shape rather than of the course card, and it would stop all twenty five. The `gate` block written into `COMPONENT_DATA__review-card.json` is the proposed fix and awaits Chat's word on its shape.

**Not changed: the course card's prototype is still NOT RECORDED**, correctly, because Kain reopened it at S272. The sweep produces it.

## The thing worth keeping

Four checks were read wrongly this session. Three I caught myself, by printing real output and reading it: the gate that passed on a page it never opened, the guard that refused 215 correct changes, the generator that offered to rewrite this specification.

**This one reached a filed report before it was caught**, and only because Kain asked at the close whether the next session could actually start.

The pattern is worth naming precisely, because it is not carelessness and it will recur: **a single observation, true in itself, written up as a general conclusion.** `/cards/` did return 404. It did not follow that the page was gone. The three I caught were caught because I looked at the thing itself rather than at one reading of it.

*No em or en dashes in this file; checked before writing.*
