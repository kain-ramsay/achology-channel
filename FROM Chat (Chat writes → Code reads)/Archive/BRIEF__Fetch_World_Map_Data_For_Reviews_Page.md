# BRIEF: fetch the world map data file for the Reviews page

**From:** Claude Chat, S240. **Date:** 2026-08-04.
**Type:** one-command fetch job. Ten seconds. No build work, no theme changes, no decisions.

## Context, standalone

S240 is designing the Reviews page (/reviews/) in Chat. Its global impact block (DSRD 4 s14.2 Variant 1, V2B Dark Band) needs the real-geography world map. The production requirement already on record is that the map is generated from real geographic land data with accurate coastlines, built once and shared. The design renders in Chat need the same source data, and Chat's machine has no network access, so the raw data file must land on disk where Chat can read it. Kain tried saving it from the browser twice; both attempts produced a screenshot image rather than the file, so this travels to you.

## The job, exactly

Download this file:

https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json

Save it, byte for byte, unmodified, as:

/Users/kainramsay/Documents/CLAUDE | Anthropic Ai/Claude Code (Projects)/Achology Website Upgrade 2026/000. www.achology.com | All Website Assets/04. Single Page Template Assets/The Review Page/countries-110m.json

One curl command with Kain's approval is the whole job. Verify the saved file starts with `{"type":"Topology"` and is roughly 100 to 110 KB, then confirm in one line to TO Chat that it is in place.

## What this is and is not

- It IS the raw Natural Earth TopoJSON (public domain) that the approved Session 15 prototype drew its map from, and the same source the production map component will be generated from at build time.
- It is NOT the production map build. That comes later, through the signed Reviews page spec, per DSRD 4 s14.2.
- Do not add it to the theme, the repo, or anywhere other than the exact path above.

## Note for the folder

There is already a `countries-110m.png` in that folder. It is a browser screenshot from the failed save attempts, not an asset. Leave it; Chat will flag it to Kain for deletion.

*No em or en dashes in this file; checked before writing.*
