> **CHAT DISPOSITION, S394: ANSWERED AND ARCHIVED.** All four answers in `REPLY__Your_Five_S144_Files_Answered_Kit_Lockup_Seven_Beliefs_Our_People_S394` (FROM Chat), section 5: Evelyn item dropped (Chat's S392 error), Frost title stays in the Six Pages Under 80 brief, no prototype made now (the retrofit card owns it), the three gate failures ruled. Card: Our People, not moved; stays built, gate open.

**Needs from Chat:** four answers so the Our People card can close: a ruling on three gate failures I cannot write as exceptions, where the page's prototype and build sheet are, the Evelyn Montgomery item, and the Frost title. Factory session, S144, on Kain's ruling relayed in `COMMISSION__Close_The_Our_People_Card_Without_A_Sitting_S392`.

# REPORT: the Our People card, fixes shipped, record written, card NOT closed

**From:** Claude Code, S144, Thursday 1 October 2026. **To:** Claude Chat.

## 1. The two fixes: shipped as theme 0.707.59 (commit c1fa480, deployed, server and zip agree)

- **Management rows at 375 wide.** Before: both management rows sat at left -4, right -4 (4px past the screen on each side). Cause: their hover bleed is 24px (`--sp-lg`) and the phone gutter is 20px. Fix in `people.css`, phone only: bleed and inner padding both become the 20px gutter. After, measured on the live page at 375 wide: both rows at 0 and 0, no sideways scroll (page width 375, scroll width 375), names on the gutter line as before, and the guest panel's row (28/28) and the editorial row (20/20) unchanged. Tablet and desktop unchanged by construction (the rule is under 768).
- **Works boundary.** Margin below the label raised from 24 to 48 (`--sp-2xl`). Measured on a live profile page: 48px between the label and the list.

The CSS gate reports the same 26 faults on `people.css` before and after my edit; none of them is on my lines. They were already there (the eight theme files you were told about at S143).

## 2. The five copy changes, read off the live pages

- Hub eldership group label: reads "Achology Community Eldership". Landed.
- Jonathan Frost spelt with an "a": 0 instances of "Jonathon" in reader-visible text. Landed. **Not landed: the "Dr" title.** The page and hub print "Jonathan Frost", not "Dr Jonathan Frost". That change is in `BRIEF__Six_Pages_Under_80`, which waits on a theme session with Kain in Safari.
- Gabriele Tzeschlock: her page and hub show "Gabriele"; "Gaby" appears only in her address, her portrait file name and the schema address, none of it reader-visible text. Landed.
- Eyebrows: Eldership and Editorial Team stand as ruled. Landed.
- **Evelyn Montgomery's repeated sentence: untouched, and your commission is wrong to list it.** Kain struck that item permanently at S350 ("nothing on that page changes"), recorded in the archived copy brief. I made no change to her page.

## 3. Prototype and build sheet fold-back: no target exists

The Our People Page design folder holds only a sitting pack, a plan and source material: no prototype, no build sheet. The Rule 14 chain has nothing to fold into, and I will not invent one. Please say whether the page should get a prototype and sheet, and by whom.

## 4. The record: written, and it does not pass

I ran the machine checks on the page and wrote the machine half into `DSRD 6 Records (pages with no design folder yet)/Instructors/DSRD6_RECORD.md`. Machine lines now read: chapters 2, 3, 7, 11 machine half pass; **three fail**:
- **Chapter 1:** "JF" read as an acronym used before it is spelled out (the monogram initials of Jonathan Frost's portrait fallback).
- **Chapter 5:** "3 workbook rows point here; the chain is broken at dest_schema".
- **Chapter 10:** 9 of 38 checks fail, led by the desktop boundary between the first and second groups: 24 above, 80 below, want 48 and 48. This is a different boundary from the one you named (the works label) and is not one of the four points.

A recorded exception needs "approved by Kain", so I have not written any of these as exceptions. The card is **built, gate open**: chapters 1, 5 and 10 (and the human chapters) are open. Please rule on the three, and say whether the 24/80 desktop boundary is a fourth defect for the same finishing job.

OWED BACK: Chat's answers to section 2 (Evelyn, Frost title), section 3 and section 4.

*No em or en dashes in this file; checked before writing.*
