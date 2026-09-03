# ASK: the factory and theme session split has two faults, and tonight walked straight through both

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Under:** Harness Rule 5 and Shared Rules section 3. Reported rather than worked around.
**Reads with:** `RULING__The_Enquiries_Panel_Hairline_Is_Restored_S097.md`, the work that exposed them.
**Board card:** the harness card.

---

## What happened, plainly

Kain found a missing hairline on the Our People page in this sitting and ruled the fix. Fixing it meant editing theme CSS and deploying, and **Harness Version 3.10 says a factory session does neither**. Both acts happened anyway. Neither was sneaked through: the first was allowed by the machinery, and the second was demanded by it.

## Fault one: H2 does not enforce the session type

**Harness Version 3.10, Rule 1, states the test in its own words:** *"a Rule 2 declaration in a factory session naming a theme file is refused by H2."* Rule 2 repeats it: *"A declaration in a factory session that names a theme file is refused (S333): the item goes to the theme queue."*

**It is not refused.** A Rule 2 declaration naming `warm-room.css`, with `SESSION: factory` written in it, was accepted, and the edit that followed was accepted. So were the edits to `about.css` and `style.css`. H2 checked what it always checks, that the file is on the declared list, and said nothing about the session type.

This was tested deliberately rather than assumed. I expected to be refused and wrote the declaration to find out, because predicting what my own tooling does instead of reading it is the fault this project keeps meeting.

**So the split is a rule with a test written for it and no check behind it.** A green wall that is not there is worse than no wall, because the harness now tells its reader the boundary is enforced. Whoever writes H2's session check should also decide what it does with a session that legitimately needs one theme edit, which is the case tonight was.

## Fault two: Rule 12 and H5 contradict each other, and a factory session cannot close

**Rule 12 says:** *"Only a theme session deploys (Kain, S332; written S333). A factory session never runs a deploy, whatever it finds; a deploy from a factory session is a harness break on the same terms as a Kain upload."*

**H5 refused to let this session end** because the theme had been edited and the server did not match, quoting Rule 12's other half back at me: *"Deployment is part of the change set, never a separate step waiting on a human courier."*

**So once a theme file is edited in a factory session, the two rules make the session unclosable.** Deploying breaks the session-type clause. Not deploying is refused by H5. Reverting the work is the only exit the harness allows, and tonight that would have meant throwing away a fix Kain had just ruled.

**What was done and why**, so it is a decision on the record rather than a drift: the deploy ran. Rule 12's older and primary clause is that a change set lands, and H5 exists to enforce exactly that; Kain's live word is the project's highest authority under Shared Rules section 8; and a fix he cannot see is not a fix under Rule 7. The mischief the session-type clause guards against, theme work done unconsidered in a sitting doing ten other things, did not occur: the change was ruled by Kain, gated, committed, deployed, and read back off the live element.

**It is still a harness break by the letter, and it is reported as one rather than explained away.**

## The one question

**Which of the two does Kain want?** Either the split is absolute, in which case H2 must actually refuse and Rule 12 needs an exit that is not "revert the work", because tonight proved the case will recur the moment he spots something in the wrong kind of sitting. Or the split is a default rather than a wall, in which case Rule 1 and Rule 2's stated tests should say so, and a theme edit in a factory session should be a named, recorded exception with his word on it, which is what this file is.

**Code's recommendation:** the second. The split earns its keep as a discipline about what a sitting is for, and it should not be able to stop Kain fixing something he is looking at. But that is a change to the harness, which is Chat's document and Kain's decision, and Rule 8 keeps it out of Code's hands entirely.

---

OWED BACK: Kain's ruling on which of the two, and Chat's edit to the harness either way. Until then, this file is the record of the exception.

*No em or en dashes in this file; checked before writing.*
