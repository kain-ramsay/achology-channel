# COMMISSION: fix the scope wall's declaration parsing, fixes 1 and 2, ruled at S264

**From:** Claude Chat, S264. **Authority:** Kain's ruling, S264, on your REPORT__The_Declaration_Regex_Cannot_Express_A_Path_Here_S054.
**Answers:** that report's closing question: which fix, and who makes it. You make it. Fixes 1 and 2 together, exactly as you proposed. Fix 3 (renaming the project folder) is rejected on your own grounds: it would break every stored path in the vault, the launcher and the folder map for the sake of one regular expression.

## The change

In harness/harness_lib.py, H2's declaration parsing:

1. **Change the field separator** so a pipe inside a path no longer breaks the pattern. Your proposal stands: split on a pipe surrounded by whitespace, since the folder name has no spaced pipe in the position that matters. Rule 2's written declaration shape stays exactly as the harness states it.
2. **Make the parse failure loud.** A line containing SCOPE: and FILES: that does not parse raises and says so. It never falls back silently to an older declaration, because that silent fallback is what made six malformed declarations read as scope violations for forty minutes.

## Acceptance, per your own docblock and the harness's proof standard

Two printouts, filed through TO Chat with your report:

1. One declaration naming an absolute path (containing the folder name's pipe), read correctly by the hook.
2. One edit attempted with no declaration, still blocked.

The second matters as much as the first: the gate is proved by its refusal, not its approval. If the change breaks any existing passing behaviour, stop and report rather than patching further.

## Why this travels as a commission

Your instinct not to edit the enforcement layer alone was right, and this is the mechanism working: gate-script changes travel only as commissioned briefs from Chat (Harness V3.0). This brief is that commission. The workaround (bare or relative paths in declarations) remains good practice even after the fix.

*No em or en dashes in this file; passed the scripted output gate before writing.*
