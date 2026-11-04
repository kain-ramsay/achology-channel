**For Chat. What this needs from you:** move the Redirect Strategy card to show 755 of 2,594 built and verified, and rule on the 1,837 rows that wait on pages not yet built. Code, factory session, S460, 4 November 2026.

# DONE: the redirect map, bulk mode built and 755 forwards written and proved on the build site

**Why the old road stopped.** `publish_gate.py --write-redirect` took every pair on the command line. A full map hits the operating system's argument-length limit, which is the crash recorded at S145. It also read the whole redirect table and made seven SSH calls for every row.

**What was built.** `publish_gate.py --write-redirects-from FILE` (commit 652829d5, pushed). It reads SOURCE tab DEST pairs from a file, reads the redirect table once, asks the server about every source and destination in a few connections (nothing is fetched from this Mac), inserts in batches of 200 over stdin, clears the caches once, then proves every written row by asking the server, redirects not followed. `--dry-run` plans and writes nothing; `--results FILE` records the fate of every pair. Its rules are the old writer's rules applied to the whole set: no redirect to itself, no silent repoint of an existing redirect, a source must answer 404 today so no live page is hidden, a destination must answer 200 and not the placeholder, and a destination that is itself redirected is refused as a chain (DSRD 1 section 11.0, one hop).

**Proof.**
- Logic test, ten cases, one per rule: all pass (test_plan_bulk.py, kept in the session scratchpad).
- Dry run on all 2,594 pairs from the workbook: 755 to write, 1,837 refused because the destination answers 404, 2 refused because the source already answers a redirect.
- Live write of the 755: proved 755 of 755 written, 0 not proved. The install went from 515 to 1,270 active redirects.
- Independent re-run of the full dry run afterwards: 755 already there, 0 to write, the same 1,839 refused. The one hop rule held: no written forward points at another redirect.
- Workbook: the 755 rows now read "verified" in Redirect_Master.xlsx.

**What waits.**
- 1,837 rows point at pages that do not exist on the build site yet (the old quote and author pages, about 1,100 and 500, plus unbuilt articles, book notes and courses). They are not faults. They are written when their pages exist, by running the same command again on the full file.
- Two rows refused: `/about-us/achology-code-of-ethics/` already answers 301 and `/dashboard/` already answers 302. Someone rules whether those two existing redirects stand.
- Not done: the five chain facts columns in the workbook were last measured on 27 October, so they are stale; the register run (`redirect_chain_register.py`) measures one address per SSH call and should be run in a daytime sitting. Not run this session.

OWED BACK: your ruling on the two existing redirects and on whether the 1,837 are written as their pages land.

*No em or en dashes in this file; checked before writing.*
