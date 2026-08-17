> **DISPOSITION, Session 267, 12 August 2026.** Closed by the fix that followed it. The defect it reported is repaired: the scope wall now separates fields on the next field's name rather than on a bare pipe, and an unreadable declaration is reported loudly instead of falling back to a stale one. Its third option, renaming the project folder, is not taken and is not recommended. Archived.

# REPORT: the scope wall cannot read a declaration that names a full path

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**A defect in the enforcement layer, not a request to change a rule.** Harness Rule 8 keeps the harness document out of my hands and I have not touched it. The hook is code, and Chat's own S263 word on the `declaredBy` bug is the precedent: "a defect in an instrument rather than a change to a standard". This one I am reporting rather than fixing, because unlike `declaredBy` it sits in the enforcement layer itself, and quietly editing the thing that polices me is not a call I should make alone.

## What happens

H2, the scope wall, reads the declaration out of the session transcript with this pattern, in `harness/harness_lib.py`:

```
SCOPE:\s*(?P<scope>[^|]+?)\s*\|\s*FILES:\s*(?P<files>[^|]+?)\s*\|\s*SPEC:\s*(?P<spec>.+)
```

`[^|]+?` means the FILES field may not contain a pipe. The pipe is the field separator.

**The project home is named `CLAUDE | Anthropic Ai`.** So every absolute path in this project contains a pipe, and any declaration that names one is unreadable to the hook: the pattern breaks at the folder name, and the declaration is silently not found. The hook then keeps reporting whichever earlier declaration it could parse.

## What it cost tonight

Six blocked edits and roughly forty minutes, spread across two jobs. The failure is silent and it looks exactly like a scope violation: the hook reports a stale declaration and says the file is not on the list, so the obvious reading is "write the declaration again", which produces the same result every time. I concluded the wall was stuck and told Kain so, which was wrong; the wall was working and my declarations were malformed.

**It has almost certainly cost time before and read as something else.** Any declaration naming a full path has always been invisible; only declarations using bare filenames or relative paths have ever registered. Those work because `declared()` matches on basename and path suffix, which is why the failure has stayed hidden: the correct habit and the broken habit look identical until you use an absolute path.

## The workaround, which holds today

**Declare with bare filenames or relative paths, never absolute ones.** `declared()` already accepts a bare filename, a relative path, a directory, or a glob, and matches on suffix, so nothing is lost by dropping the prefix. Every declaration in this session's second half uses that form and every one has been read correctly.

## Three fixes, for whoever takes it

1. **Change the separator or the field pattern.** Splitting on a pipe that is surrounded by whitespace (` | `) would let a path's own pipe through, since the folder name has no spaced pipe in the position that matters. Smallest change, and it keeps Rule 2's written shape exactly as the harness states it.
2. **Make the failure loud.** If a line contains `SCOPE:` and `FILES:` but does not parse, say so, rather than falling back to an older declaration. A silent fallback to a stale declaration is what made this look like a scope violation for six attempts.
3. **Or rename the project folder.** A pipe in a folder name breaks more than this: it is a shell metacharacter, it is why the H7 hook exists in the form it does, and it has to be quoted in every command. That is Kain's decision and it has a cost, so it is named here rather than recommended.

**My preference is 1 and 2 together, and not 3.** Renaming the project home would break every stored path in the vault, the launcher and the folder map for the sake of one regular expression.

## What I need back

**A decision on which fix, and who makes it.** I have not edited `harness_lib.py`. If Chat wants me to, say so and I will, with the acceptance test the hook's own docblock asks for: one declaration naming an absolute path, read correctly; one edit with no declaration, still blocked.

*No em or en dashes in this file; checked before writing.*
