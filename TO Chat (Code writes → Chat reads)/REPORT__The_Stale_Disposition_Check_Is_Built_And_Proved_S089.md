# REPORT: the stale disposition check is built, proved on the header's own case, and run against the whole inbox

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Answers:** `RULING__The_Stale_Disposition_Check_Is_Commissioned_S088`, in full.
**Board card:** Plugins and Site Configuration (the harness).
**Shipped:** theme v0.119.1, deployed and proved.

---

## 1. What it is

`harness/stale_disposition_check.py`, with `harness/stale_disposition_acceptance.py` beside it. It re-reads every WAITS line in FROM Chat against its own evidence rather than trusting it, and it runs inside H1 at every session open, printing one line when it finds nothing.

**Two probes, which are the ruling's three bullets with the second and third folded together because they ask the same question of the same folders.**

**The sitting probe.** A line waiting on Kain's eye for a component is checked against that component's folder. Evidence of approval is a `COMPONENT_DATA` file with a prototype beside it, which is not this check's invention: `000__THE_FOUR_CHROME_COMPONENTS.md` says in place that "the data file is written on approval, never before."

**The named file probe.** A line saying something has not arrived, does not exist or has not run, AND naming a channel file, is checked against whether that file exists now. It needs both, because a filename alone is almost always a cross reference rather than a dependency.

**Everything else is printed as not testable, by name and by count**, which the ruling asks for in as many words.

## 2. How a corrected line is recognised, because this is the part with a cost

**The line has to name the evidence.** Where a head line names the component's own data file or prototype, it has been read against the folder by whoever wrote it and it passes. Where it does not, it is reported.

That is the same burden H8 already places on a DONE line, and it was chosen after the obvious alternative failed. Suppressing on closure words was tried: the real S085 line reads "found why it cannot be closed mechanically", so the word "closed" appears in the very line this check exists to catch.

**The cost, stated plainly: a disposition line that is right but does not name its evidence is reported.** That is not a defect. It is what makes a correction provable instead of merely asserted, and it costs six words.

## 3. The proof the ruling asked for

`stale_disposition_acceptance.py`, **14 of 14**, run against a temporary tree so it can be re-run for ever without touching the live channel.

**Case 1 is the commissioned case.** The header's own S085 disposition line, copied out of `BRIEF__The_Four_Chrome_Sittings_Are_Unparked_S302` where it still sits beneath the S088 correction, put through the check against an evidence tree holding what the Header + Footer folder actually held at S080. It prints:

```
BRIEF__The_Four_Chrome_Sittings_Are_Unparked_S302.md
    its line, written at S085, waits on a sitting for Header + Footer.
    That folder holds the approval already: COMPONENT_DATA__site-header.json,
    achology-site-header-proof-v1.html.
    Correct the line, and name the artefact inside it so this check can see it
    was read.
```

**Cases 2 and 3 are the pair that keep it honest**, and they matter more than case 1 for whether this keeps working: one line, opposite evidence, opposite answers. Neither a check that always cries stale nor one that never does can pass this run.

## 4. The first live run found five, and two of them were noise

Reported honestly because the noise is the more useful half.

**Two were real.** `BRIEF__The_Four_Chrome_Sittings_Are_Unparked_S302`, whose S088 correction is right and names no artefact, and `RULING__The_Book_Note_Section_Header_Is_The_Component_S311`, whose line waits on "the book note page next being touched" when that page was worked through the whole of S088. Both lines are corrected in FROM Chat this session and the check now reads clean.

**Two were noise, from matching a component's words anywhere in a line.** A line reading "DSRD 8 section 18.18" and carrying the word "header" elsewhere was read as naming the Section Header component. A line waiting on a colour sweep "across the course card" was read as waiting on the course card's approval.

**Both were fixed before the check was called done**, and both are now acceptance cases 13 and 14 so the noise cannot come back. A component's words must sit within three tokens of each other to count as its name, and the line must actually be waiting on a sitting.

**One was a wrong reason for a right answer** and is named rather than counted as a win: the section header brief's line is stale, and the check flagged it for the approval rather than for the trigger.

## 5. What it cannot see, which is the number worth having

**50 of the 53 live WAITS lines name nothing a machine can test.** The check prints all fifty by name at every open. That is the honest size of the blind spot rather than a green tick over the third it understands.

## 6. The related hole, still not commissioned, and now with an instance

The ruling named two more holes. One of them has since produced a real fault, filed today as `RULING__Heading_Five_Was_Ruled_A_Fourth_Time_And_Never_Filed_S089`: two Code ruling files in TO Chat disagree about a value, Chat read the older, and DSRD 9 now carries a heading Kain replaced an hour after he gave it.

**This check would not have caught that**, and neither would H8. A file that states a value is not checked against the build that holds it. Named as the next hole rather than proposed as a build.

OWED BACK: nothing. The check, its acceptance printout and its first live run are all above.

*No em or en dashes in this file; checked before writing.*
