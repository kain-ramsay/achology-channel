> **CHAT DISPOSITION, S342: STAYS, on one named fact: Kain's yes or no on this proposal.** He asked at S337 to see it before anything is built, so it is his to read and rule, and S342 was ruled a board session; it is put to him at the S342 close if there is room, otherwise first in S343's channel session. Nothing is built until he says.

# PROPOSAL: how the skill library joins the instruction drift check

**From:** Claude Code, Session 102. **Date:** 5 September 2026.
**Answers:** `RULING__The_Skill_Library_Joins_The_Instruction_Drift_Check_S337.md`, whose OWED BACK is this proposal. Kain ruled the library into the check and asked to see a proposal before anything is built; this is that, and nothing is stamped, swept or touched by it.
**Board card:** the harness and instruction sets.

## The shape in one paragraph

Every skill file gets the same marker line the two instruction documents already carry, a twelve character content hash of everything below it, placed on the first line after the file's front matter. `instruction_drift.py` grows one list entry per skill (read from the library folder, never typed), stamps and checks them exactly as it does the two documents today, and prints the result in a shape a person will read: every drifted or unstamped skill by name, and one line for the rest. Chat reads the marker off each live copy at `/mnt/skills/` and compares it with the list the check prints, which is the same comparison Chat has run twice on the two documents. Kain carries the fix across, as now, one upload per drifted skill.

## Question 1: does a marker survive the upload?

Three facts decide it, and two of them are already proven.

1. **The marker is a Markdown comment**, `<!-- CONTENT HASH: 9cedeee92fba | everything below this line | regenerate with harness/instruction_drift.py --stamp, never by hand -->`. A comment is content: an upload through a file picker keeps it byte for byte, and a paste through a text box keeps it as text. The Achology Project Instructions have travelled this way twice and come back matching, so the paste route is proven on the exact marker.
2. **A text box may change line endings and trailing spaces, and the hash already forgives both** (acceptance case 6), while a deleted line still drifts (case 7). Nothing in a skill file needs more forgiveness than an instruction document did.
3. **The one new thing is the front matter.** A skill opens with a YAML block between two `---` lines (name, description, triggers). A comment inside that block would break the YAML, so the marker goes on the first line after the closing `---`, and the hash covers everything below the marker, which is the whole skill body. The front matter above it is not hashed, on purpose: it is the part the skills interface itself reads and could re-serialise, and a hash that covered it would cry drift at a reordered key nobody typed. Whether the interface ever rewrites the body is the one thing not yet proven, and the proposal proves it before the sweep rather than after: **one skill is stamped, Kain uploads that one, Chat reads its marker back.** If the marker comes back intact the design holds for all of them; if it does not, we know on one file rather than fifty two.

Two acceptance cases are added with the build: case 8, a stamped skill with front matter still parses as YAML and checks as MATCH; case 9, the same file round-tripped through a text box (CRLF, trailing spaces, a blank line added at the end) still checks as MATCH, and with one word changed in the body reads DRIFTED.

## Question 2: what fifty two of them look like on the page

The library folder holds 52 skill files (measured this turn; the ruling said forty eight), beside the folder's read-me, the skill to PRD map and a working-docs folder. A wall of 52 MATCH lines at every session open is a receipt nobody reads, so the printout inverts: **what is wrong is printed, what is right is counted.**

    INSTRUCTION DRIFT, 5 September 2026
      MATCH     Operating Instructions           9cedeee92fba
      MATCH     Achology Project Instructions    7cf99a6d8757
      skills: 50 stamped and current, 0 drifted, 2 not yet stamped
      NOT STAMPED   achology-building            (stamp it, then Kain uploads it once)
      NOT STAMPED   ai-collaboration

    and on the day something moves:

      skills: 49 stamped and current, 1 drifted, 2 not yet stamped
      DRIFTED   rank-math-90                     marker says 3a91c0de7b12, content is 8f0e2c4a91d7
                (the file changed after its last stamp; --stamp it, then Kain uploads it)

The two documents keep their own lines because there are two of them and Chat reads both every session. A skill that has never been stamped is named, never folded into the count, because an unstamped file cannot be checked and a count that hid it would say "current" about something nobody measured. The full 52 line list stays available behind `--all` for the session that wants it.

**Where the hashes go for Chat.** The check already prints the file-side hash for the two documents and Chat compares by eye. For 52 skills a by-eye comparison is the receipt nobody reads again, so the check also writes `SKILL_HASHES.txt` beside the library (name and hash, one per line, regenerated on every stamp). Chat reads the markers off `/mnt/skills/*/SKILL.md` and compares them against that file in one pass, and reports only the names that differ. That is the same work Chat does today, at a size a person can still do.

## What it costs, said plainly

Stamping 52 files changes 52 files, and a marker in the file is worthless until the same marker is in the live copy, so **every skill has to be uploaded once after stamping.** That is 52 uploads by Kain, in one sitting or spread over the sessions that touch each skill. The proposal does not hide it, and offers the smaller road: stamp the whole library on his yes, upload the one test file first (question 1), then the rest as he has time, with the printout naming what is still unstamped until he has. A skill uploaded after stamping is checkable from that day; one not yet uploaded is simply named as not yet stamped, which is true.

## What is not proposed

No change to what any skill says. No sweep of the library's content. No marker in the front matter. No check that reads the live copy from Code's side, because Code cannot reach it and the brief's condition stands: the check reports, Kain carries the change across.

OWED BACK: Kain's yes or no, through you. On yes: Code adds the library to `instruction_drift.py` with the two acceptance cases and `SKILL_HASHES.txt`, stamps the one test skill first, and reports; the full stamp follows the moment the test file comes back matching.

*No em or en dashes in this file; checked before writing.*
