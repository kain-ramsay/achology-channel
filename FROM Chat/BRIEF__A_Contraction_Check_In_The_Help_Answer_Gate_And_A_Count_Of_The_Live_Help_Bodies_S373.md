# BRIEF: a contraction check in the help answer gate, and a count of the live help bodies

**From:** Claude Chat, Session 373, Monday 21 September 2026. **To:** Claude Code. **Approved by Kain in session, S373** ("yes, please do those four items right now"; this is item 4). It does not jump Kain's stream ruling: it waits its turn behind the pricing page unless he says otherwise.

## Why this exists

Kain read a new help answer at S373 that passed every count and ruled it robotic: hard, dry and abrupt. The rewrite he approved ("absolutely perfect") is now the voice exemplar for the whole Help section: `HELP__cbt-practitioner-vs-cbt-therapist.md` in the help-answer folder of Content Records. The standard is written into DSRD 2 section 2.24 item 6, the `help-answer` skill (rule 7, handed to Kain for upload) and Recipe 7 of the Cowork Production Harness, Version 22.

Most of what makes the approved answer warm cannot be measured by a machine. One part can: The Achology Base Voice says "contractions throughout", and the stiff draft had none. Chat then looked at the two help exemplars approved before today (What is Achology?, and the Carl Rogers thinker answer): neither carries a single contraction. An old export of 200 live answers (July) shows 147 of 200 with none. Today's 250 have not been counted. You can do that in seconds; Chat cannot.

## Part one, read only: the count (please answer this first, it is small)

Across every live help answer body, from the records in the help-answer folder of Content Records (the source of truth, not the install):

1. How many bodies carry no contraction at all?
2. For each body: the count of contractions (it's, you'll, isn't, don't, they'd, that's, here's and the rest) and the count of the uncontracted forms a person would normally contract in speech (it is, you will, is not, do not, does not, cannot, you are, that is, there is, will not). Link text and quoted titles excluded.
3. The same two numbers by help category.

Return it as one ANSWER file to TO Chat, worst first. Kain decides from that count whether the live section gets a softening pass; nothing is rewritten on the strength of this brief.

## Part two, the build: one new check in the help answer entry of the shared gate

In `content_gate_standards.json`'s help-answer entry, read by `content_gate.py`:

- **Fail** a help answer body that carries no contraction at all.
- **Flag, never fail,** any H2 section of the body that carries none, and any body where the uncontracted forms listed above outnumber the contractions. A flag is for a person to read, on the fail-or-flag split the Base Voice already uses.
- Exclude link text, quoted article titles, canonical course and document names, the UKRLP line and the Related questions block, because those are other people's wording or fixed wording.
- The three categories that carry policy and money (privacy-and-legal, refunds-and-billing, pricing-and-payments) are held to the fail line only, never the flags: Kain's S373 ruling keeps them calmer, contractions yes, idiom no.

Prove it on two records and print both results: the approved exemplar above must pass clean, and `HELP__what-is-achology.md` is expected to fail the no-contraction line as it stands today. That second result is information for Kain, not a defect to fix.

## Definition of done

The ANSWER file with the count is in TO Chat. The check is in the gate, proven on the two records named, with the printouts in your session report. No help body has been edited.

*No em or en dashes in this file; checked before writing.*
