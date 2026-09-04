# REPORT: the recurring component-gate failure is the checker, not the theme

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Follows:** S100's own closing note, which found the same symptom and named it "not investigated."

---

## What happened

`h5_completion.py`'s Stop hook blocked twice this session on `component_gate.py` runs against `BUILD_SHEET__book-note-card.md` and `BUILD_SHEET__global-impact-block.md`, both armed because I edited `style.css` (a version bump, unrelated to either component). Neither file was touched this session.

## What I checked, not assumed

Ran the exact same armed-sheet set twice in direct succession, on unchanged code:

- **Run 1:** 46 passed, 17 failed. Every failure read as an unstyled page: `Times` for the font family, `rgb(0, 0, 0)` for every colour, `0px` for every measured spacing. That is the signature of the specimen page loading with no CSS at all, not a design disagreement.
- **Run 2, seconds later, same files, same command:** 16 passed, 39 failed. A different failure set entirely: real brand colours this time (`rgb(53, 65, 73)`), but sizes out by exactly 10x (`200px` sheet value measured as `2000px` built), and different properties failing than run 1.

Two runs of the same check against the same code cannot honestly disagree with each other and both be measuring something real. This is the gate's own browser-driven specimen measurement failing to load or render consistently, most likely raced by whatever else is running locally at the time (this session had a heavy concurrent page-check running throughout).

## Why this isn't in component_gate_waivers.md

That file is for a real, standing disagreement between the theme and a signed sheet, and its own opening line says "nothing here is a pass." What I found is not a disagreement at all: it is the same code measured twice returning two contradictory answers. Writing it up as a waiver would misrepresent noise as a known design gap.

## What this needs

Not mine to fix this session (`component_gate.py` is a theme file; this is not the theme session, and nothing was ruled in a sitting to authorise the edit). Named here so it stops costing every session's close the way it cost S100's, and so nobody reads a future red run against these two sheets as a real regression without re-running it first.

---

OWED BACK: nothing from Chat. Carried as a named, diagnosed infrastructure gap for whichever theme session next touches component_gate.py's specimen measurement.

*No em or en dashes in this file; checked before writing.*
