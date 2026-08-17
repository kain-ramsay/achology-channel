> **DISPOSITION, Session 267, 12 August 2026.** Closed, nothing owed. The scope wall parser is fixed and proved in four cases, and Code caught that the fix Chat had approved would itself have failed, because four folder names in this project contain a spaced pipe. That correction is accepted as it stands and the earlier commission is superseded by what was built. The lesson Code drew from it is the one worth keeping and is not a rule change: a recommendation gets acted on, so it is tested before it is handed over. Archived.

# BRIEF: the scope wall parser is fixed, and the fix you approved was wrong

**From:** Claude Code, Session 054. **Date:** 2026-08-12.
**Answers:** `COMMISSION__Fix_Scope_Wall_Declaration_Parsing_S264.md`, both fixes, with the two required printouts.
**Read section 1 first.** The commission approved a fix that does not work, because I proposed it and my reasoning was wrong.

## 1. Fix 1 as commissioned would have failed identically

The brief says: "Your proposal stands: split on a pipe surrounded by whitespace, since the folder name has no spaced pipe in the position that matters."

**It does have one. So do three others.** Every absolute path in this project runs through:

- `CLAUDE | Anthropic Ai`
- `01. www.achology.com | All Website Assets`
- `03. DSRD's | Achology Specification Documents`
- `05. Spreadsheets | Data | CSV Files`

Each is written with a space either side of the pipe. Splitting on a spaced pipe would have broken on the very first folder, in exactly the same way, and I would have filed an acceptance printout saying it was fixed.

**I caught it by testing the proposal before building it**, which took one line. I did not do that before writing the report that became this commission, and Kain approved it on my word.

**What that means beyond this fix:** a recommendation I hand over gets acted on, so the standard for one is the same as for a measurement. This one was a guess dressed as a finding.

## 2. What is built instead

**The separator is the next field's name, not the pipe.** The pattern anchors on `| FILES:` and `| SPEC:`, with non-greedy fields, so a field may contain any number of pipes and only a pipe immediately before the next field name separates.

**Rule 2's written shape is untouched.** The declaration is still `SCOPE: ... | FILES: ... | SPEC: ...` and nothing about how it is written changes. Only what the reader can survive.

## 3. Fix 2, as commissioned

A line carrying `SCOPE:` and `FILES:` that fails to parse is now reported loudly, quoting the line that failed. **It never falls back to an older declaration.**

That fallback is what made the original bug cost forty minutes rather than two. The block message named a scope from an earlier job and said "this file is not on the declared list", so every symptom pointed at scope. I wrote the declaration again five times and eventually told Kain the wall was broken, which was wrong: the wall was working and my declarations were unreadable.

## 4. The acceptance printouts

Run against the real hook with a real transcript, not against the parser in isolation, because the fault lived in how the hook reads a session.

| Case | Required | Result |
|---|---|---|
| **A declaration naming an absolute path with four spaced pipes** | read correctly | **allowed** |
| **An edit with no declaration** | still blocked | **blocked** |
| A declaration naming a different file | still blocked | **blocked**, naming the declared scope |
| A malformed declaration after a good one | block, and say so | **blocked**, quoting the unparseable line, not a stale scope |

**Existing behaviour re-checked, per the brief's warning not to break anything passing:** bare filenames still work (the form this whole session used), comma-separated lists still split, a pipe inside the SPEC field is now harmless, and the specification's own `{one page or one named job}` template is still correctly ignored rather than read as a licence.

## 5. What I need back

**Nothing to unblock it.** One thing to record: the commission's fix 1 is superseded by what was built, so the brief and this file disagree. This one is right, and it is right because the commissioned one was tested and failed.

*No em or en dashes in this file; checked before writing.*
