# INSTRUCTION: end the permission popups for routine commissioned work

**From:** Claude Chat, S227. **Authority:** Kain, ruled this session.
**Why:** Kain is being asked to approve individual actions ten to a hundred times a session on work he has already commissioned. That approval theatre is now redundant: the harness hooks are the real guard, and they fire regardless of permission mode.

## The work

Configure your permission settings (`.claude/settings.json`, the permissions block) so that routine work inside this project runs without prompting Kain:

**Pre-approved, no popup:**
- Reading any file in the project folders and the channel.
- Editing and writing files inside the theme repository and the channel folders (the scope wall H2 and forbidden-ground H3 already govern which files, mechanically).
- Running the gate scripts, the hooks, and python.
- Git add, commit, status, diff, log inside the theme repository.
- The established SSH read commands against achologytest.com.

**Still prompts Kain, every time:**
- Any deletion of files or data.
- Any write outside the project folders.
- Any command that changes the live or build site's database or uploads (writes over SSH).
- Anything not covered above.

## The safety argument, stated so it is on record

The popups were the only guardrail before the harness existed. They no longer are. H2 and H3 are PreToolUse hooks, and a blocking PreToolUse hook fires in every permission mode, so widening permissions does not widen what you can actually touch: an undeclared file, a DSRD path, or this document's path is refused whether or not a popup would have appeared.

## Definition of done

The settings are in place, and you prove the guard still holds under the new settings by re-running the H2 and H3 acceptance tests (attempt an undeclared edit and a DSRD write with the new permissions active) and filing both blocking printouts to TO Chat. One line in that report tells Kain roughly how many popups per session this removes.
