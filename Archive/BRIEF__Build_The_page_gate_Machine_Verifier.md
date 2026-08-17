# BRIEF (approved, Kain, S224): build the machine gate that verifies every page

**From:** Claude Chat · **Date:** 2026-07-27 · **This is a commissioned build, not a question.**

## The product

Extend your existing qc gate script into one command: `page_gate`, run against any URL on achologytest.com. It measures the rendered page against the locked standards and prints one PASS/FAIL line per check, then an overall verdict. No judgement, no interpretation: numbers measured, numbers compared.

## The checks it runs (source of each value in brackets; read them fresh, do not hardcode from this brief)

1. A visible hairline exists at every block boundary within the page; none at page top or bottom edge (DSRD 7 §4.3).
2. Every hairline measures 48px above and 48px below at desktop and tablet width, 32/32 below 768px; same at tinted-band edges (DSRD 7 §4.3).
3. No block contributes its own padding or margin at a boundary; the owner element supplies all of it (DSRD 7 §4.3).
4. First content row sits 48px below the header (32 phone) (DSRD 9 §26).
5. Content width is exactly 1200 or 880, nothing else (DSRD 9 §27).
6. H1 is 32px weight 700, exactly one per page (DSRD 7 §3).
7. Page gutters 20/32/48 by breakpoint (DSRD 7 §4.2 / D2).
8. Meta title present, unique, ≤60 characters; meta description present, ≤155 (DSRD 6 §3).
9. Zero em dashes (U+2014) and en dashes (U+2013) anywhere in rendered content (house standard).
10. Existing qc checks (banned vocabulary, UK spelling, link validation) fold in unchanged.

## The standing rule this creates

From the day page_gate exists, every DSRD 6 record you file in TO Chat includes its printout for that page. A record without the printout is incomplete and comes back. Add this to CLAUDE.md alongside the two lines already ordered in the standing instruction.

## Definition of done

The script exists in the theme repo, runs with one command against any URL, its printout for one policy page is filed in TO Chat as proof, and the CLAUDE.md line is installed. Deliver this BEFORE starting page 2 of the bring-to-standard order, so every subsequent page record carries machine proof.
