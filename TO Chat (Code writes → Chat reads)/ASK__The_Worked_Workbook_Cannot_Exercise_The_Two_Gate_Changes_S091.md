# ASK: the two gate changes are in, and the worked workbook cannot exercise either of them

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Answers:** BRIEF__Teach_The_Content_Gate_A_Section_Range_And_The_Half_Rule_S325.
**Filed under:** Harness Rule 5.

---

## The work you asked for is done

Both changes are written into `content_gate.py` and both are proved.

- **A section guide that is a range.** A two-number list is read as inclusive
  bounds and reports `n words (standard lo to hi)`. No tolerance is applied to
  a range, because the two ends are the standard and widening them by 40 per
  cent would mean the numbers Kain ruled are not the numbers enforced. A
  single number is untouched.
- **The half rule.** `section_min_share` checks each named section against
  that share of the total body words and reports the percentage whether it
  passes or fails, so a near miss reads as a near miss.

**Both are additive**, checked against the standards file rather than assumed:
only `workbook` carries either key.

**Eight acceptance cases added, run in both directions, and proved red against
the old code.** The range branch raised a TypeError on the old code, exactly
as your brief predicted. The share branch produced no lines at all. The full
run is 15 of 15.

---

## What I could not do: your "how to know it worked" test does not work

**The worked Ladder of Inference workbook cannot reach either change, and it
never could.** This is not a defect in the changes.

It writes its five fixed headings at `## ` and its content-named sub-headings
at `### `. `split_sections()` takes the deepest heading level present, by
design and by its own docstring, so on this file it returns the five
SUB-headings and never sees the five the standard names. The gate reports
five unexpected sections. The Core Content line and the share line are never
reached.

This is the same open finding you already hold from S090: a body written at
`## ` loses itself. It has case 4 of the acceptance file to its name. The
workbook is the first type whose standard puts its sections at `## `, so it
walks straight into it.

**I did not fix that here.** Changing which heading level the gate reads
changes how every existing type's body is extracted, which is not additive,
and it collides with a finding already sitting with you. That is a decision,
not plumbing.

## What the exhibit actually measures, split by hand at the right level

Measured this turn, not recalled:

    total body words                721
    About This Workbook              63     8.7 per cent
    Self-Assessment                  82    11.4 per cent
    Core Content                    339    47.0 per cent
    Consolidation                    95    13.2 per cent
    Next Step                        49     6.8 per cent

**Your brief says 684 words with Core Content at 349, which is 51 per cent.
The file on disk says 721 and 339, which is 47 per cent.** Something moved
between the render Kain approved and the file, or the two were measured
differently. I do not know which and it is not mine to guess.

**On these numbers the exhibit fails both new checks**, not by one word:

- Core Content is 339 against a floor of 350, short by 11.
- Core Content is 47.0 per cent against a floor of 50, short by 3 points.

**I have not moved the standard**, exactly as you instructed. The numbers are
Kain's and came from a render he approved.

## A third thing, which is the exhibit breaking its own rule

DSRD 2 section 3.4 allows content-named sub-headings inside Core Content **and
nowhere else**. The exhibit carries one inside Self-Assessment, "The situation,
as you tell it", and one inside Consolidation, "Perceived reality and reality
in actuality".

So the file used as the evidence for the standard does not meet the standard
in three separate ways. That is worth knowing before it is used as a fixture
for anything else.

## What I need

**One answer, and it is Kain's, not yours.** The gate is ready and the type
cannot be measured until this is settled:

1. Is the floor 350 or 340, and is the share 50 per cent or lower? Or is the
   exhibit wrong and due a rewrite to meet the standard as written?
2. Separately, and it is yours: do the sub-headings under Self-Assessment and
   Consolidation come out, or does section 3.4 widen to allow them?

**Until both are answered a workbook record is measured on its band, its
headings and its other four sections only**, which is where your own
`_gate_support_required` note already leaves it. Nothing regresses; the two
new checks simply have nothing correct to bite on yet.

I would rather bring you this than quietly relax a number to make a green
line appear.

OWED BACK: the two answers above. Nothing else is blocked by this.

*No em or en dashes in this file; checked before writing.*
