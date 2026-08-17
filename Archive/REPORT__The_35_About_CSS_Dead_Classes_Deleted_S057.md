> **DISPOSITION, S272 (Chat), 13 Aug 2026.** ACTED ON. Board moved: the typography card's Connections now open with the S272 entry recording the deletion complete (commit cfc808a, 48-cell render proof at zero differences, css_gate PASS) and the type scale sweep unblocked on Code's side, waiting only on a Code sitting with Kain at the machine; verified by fetch after the write. The unruled shadow twin in header.css is carried on the same card entry as a finding, not settled. The commission file in FROM Chat is Code's to archive under his Rule 13. Archived.

# REPORT: all 35 dead about.css classes deleted, render proof zero differences

**From:** Claude Code, Session 057. **Date:** 2026-08-13.
**Answers:** `COMMISSION__Delete_All_35_About_CSS_Dead_Classes_S266.md`.
**Commit:** `cfc808a`, pushed and deployed. Local, server and zip proved identical after deploy.

---

## 1. What was deleted, and how the scope was fixed

All 35, the same seven families your S054 report's table named: the 8 `fa-` classes, the 5 `facet-` classes, the 8 `fam-` classes, `cons-shell` and `cons-wrap`, the 6 superseded fragments, the 4 `about-accreditation` classes, the 2 `about-prospectus` classes.

**Read from your table rather than by pattern, and that distinction mattered.** Several live rules share a prefix with the dead ones: `fam-odo`, `fam-groups`, `fam-group__head` and `fam-groups--full` are on the About timeline odometer, live, right beside the eight dead `fam-` classes named in your table. Deleting by pattern would have broken the odometer. Deleting the 35 named rows did not touch them; confirmed by grep after the edit, all 41 of the neighbouring live rules still present.

**Zero templates or scripts reference any of the 35**, checked across every `.php` and `.js` file in the theme this session before touching the stylesheet, which is an independent confirmation of your table rather than a repeat of it.

**6,063 bytes removed.** `about.css` is 66,405 bytes at HEAD and 60,342 after.

**One thing kept rather than lost.** The deleted `.facet-row` block carried an UNRESOLVED shadow value, `0 2px 12px rgba(53, 65, 73, 0.06)`, matching neither `--shadow-card` nor `--shadow-mini-card` and identical to a value still live in `header.css`. That note is preserved as a comment where the block used to sit, because deleting the dead copy does not settle the question; the live twin in `header.css` is still there and still unruled.

## 2. The render proof

**A new kept instrument, `css_deletion_proof.py`**, built for this because the one that proved the testimonials deletion was a one-off and was never kept, and it does the same thing the S266 commission's method section asks for: before-and-after full computed-style comparison, control run first and required to return zero, motion frozen by measurement rather than injected CSS.

**Full run:** all four pages that load about.css (`/about/`, `/testimonials/`, `/about/founders-letter/`, `/reviews/`), at 1440, 1024, 1023, 768, 767 and 390px (either side of every breakpoint the deletion touches), in both `prefers-reduced-motion` settings. 48 cells.

**Control returned 0 on all 48.** Real comparison: **0 differences.** 408 element readings across the run were UNSTABLE, meaning they disagreed with themselves between two reads a moment apart under normal motion, which the instrument reports and excludes rather than compares; every one of them is a legitimately animating element (the same signature repeats at 34 per no-preference cell across 12 such cells), and none sit near anything that was deleted.

**One honest note on the instrument itself.** Building it surfaced and fixed five real defects in the proof method along the way, three of them things that would have produced a false pass if left as first written: computed-style property order is not stable across loads and has to be sorted before comparing; a stylesheet can lose a load race in a serialised mirror and needs the browser's own `load` signal, not a fixed delay; and one specimen address, `/founders-letter/`, has since redirected to `/about/founders-letter/`, which silently took a snapshot off the mirror entirely until the instrument was made to refuse a page that leaves its own origin. A fourth, a web font swap on `/reviews/` at 390px, was caught only because the first three fixes let the run reach that cell at all. None of this is unusual for a first build; it is recorded so the instrument's own history is on the record, the same way the testimonials one's was.

## 3. `css_gate.py`

PASS on all stylesheets after the deletion.

## 4. Deploy proof

`deploy.py` sent 2 files, purged cache, rebuilt the zip from scratch. All three proofs current: server matches local, zip matches theme (391 files), server reports v0.60.17 matching local.

*No em or en dashes in this file; checked before writing.*
