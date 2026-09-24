# H10 (Life Coaching) drafted and gate passed

**From:** Claude Cowork, S385, Thursday 24 September 2026. **To:** Claude Chat.
**Answers:** nothing specific; continuing the "next 5" hub guide batch Kain authorised.

## What's done

H10 (Life Coaching) is drafted and `GATE: PASS`. Fed by 70 lecture spokes across two courses (009 Life Coaching Certificate, sections 1 and 4; 010 Life Coaching Blueprint, sections 1, 3 and 8), read from Table A. First hub under the Helping People category rather than Psychology, and the first fed by two courses rather than one. Carries the three H09-ruling fixes.

One finding worth flagging: the `mcp__remote-devices__Filesystem__*` connector is broken this session (a JSON-Schema-dialect error on every call, confirmed on retry). DSRD 5's course facts for 009 and 010 were still confirmed, by reading the DSRD 5 file directly through `device_bash` instead. That workaround is available for the rest of this batch too, so it is not blocking H11, H13, H12 or H08.

Also found: the `## Body` marker heading is required by `content_gate.py` to separate the field table and Search and Citation Brief from the measured body. Its absence silently makes the gate measure the whole file as body (word count, density and process-text checks all failed on the first pass for exactly this reason). Worth a line in the hub-guide drafting skill if it isn't there already.

## OWED BACK

Nothing.

*No em or en dashes in this file; checked before writing.*
