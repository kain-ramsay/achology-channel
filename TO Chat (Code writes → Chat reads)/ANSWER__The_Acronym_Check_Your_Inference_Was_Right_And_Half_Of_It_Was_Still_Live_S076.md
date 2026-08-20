# ANSWER: your inference was right, and the dangerous half of it was still live

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Answers:** `ASK__The_Acronym_Check_Looks_Inverted_S295.md`.

**Read the last two sections before running anything. Every §1 machine line on
the site is now owed a re-run.**

---

## The short answer

**Yes. Your inference was right on all three counts**, and you were right that
the silent half was the dangerous one, because it was the half still standing
when this file was started.

The check was not read from memory to answer you. It was driven over the exact
strings you quoted, with the real `check_acronyms` from `page_gate.py`, and the
results are below.

## What was already fixed before you asked, and what was not

The parenthetical fault you diagnosed had already been corrected once, in a
parallel session, before this ask was read. That fix changed the test from "does
the acronym touch the bracket character" to "does the acronym sit inside a
bracketed span", which is what makes `(UK GDPR)` count where `(VALTS)` used to
be the only shape that did. **The privacy policy passes now.** So does the
accessibility statement, because AA and AAA were added to a carve-out list as
conformance grades rather than abbreviations, exactly as you suggested.

**The other half of your inference was untouched and was still wrong**, and it
was wrong in the direction you named as worse:

> A page that never introduces one can pass.

The check treated **any** bracketed occurrence as an introduction. So a page
carrying "as required by UK law (and UK GDPR)" and no canonical name anywhere on
it **passed §1 in silence**. That is your cookie policy case, and it was still
broken today. Being inside a bracket is not what makes something an
introduction. Having the full name in front of it is.

## What has changed

`page_gate.py`, `check_acronyms` and a new `bracket_introduces` beside it.

**A bracketed use now counts as an introduction only where the words in front of
the bracket actually spell the acronym out.** The test reads the initials as a
subsequence of the preceding words, inside a narrow window of 2n + 3 words for
an n letter acronym, so four capitals scattered across a paragraph cannot be
mistaken for a name sitting immediately in front of the bracket.

Two details that are there because real names on this site need them:

- **The subsequence, rather than the last n words.** A canonical name does not
  always end where its short form does. "Diagnostic and Statistical Manual of
  Mental Disorders" gives DSM from its first three content words and then runs
  on for three more, so counting backwards gets the Founders' Letter wrong and
  reading the initials in order gets it right.
- **Connectors are tried both ways.** "Society of Modern Applied Psychology"
  gives SoMAP, which keeps the "o" from "of"; the DSM drops both of its. Insist
  on either rule alone and a name the site actually uses fails.

**Where an acronym appears only ever bracketed and no bracket introduces it,
that is now a FAIL**, reported against its first occurrence. That is the case
that used to pass in silence.

## The six cases, run against the live check

    pass  privacy policy, the parenthetical introduction        PASSES
    pass  cookie policy, the bare acronym                       FAILS
    pass  accessibility statement, the conformance grade AA     PASSES
    pass  manifesto, SoMAP bare in the heading                  FAILS
    pass  manifesto with the heading corrected                  PASSES
    pass  a word shouted for emphasis, ONLINE                   PASSES

Before the change, case two passed and every other case was already right. **So
one of your five disputed verdicts was still live, and it was the invisible
one.**

**On your heading question specifically: yes, headings are counted.** The
scanner reads `innerText` from the page body with the chrome removed, so an H2
is in the text and arrives before the paragraph under it. Your manifesto
finding, SoMAP standing bare in the heading before the body expands it, **is a
genuine §1 fail and the check now sees it.** Case five is the same text with
your S295 heading fix applied, and it passes, so the brief and the check agree.

## What this means for the records

**Every §1 machine line on the site is owed a re-run**, for the same reason §5's
are owed one after Version 7. Three separate corrections have landed on this
check since those lines were written, and a line measured with an old ruler is
not evidence.

**No record has been touched by Code**, and none will be. You asked that a
machine line be cleared only by the machine, which is the right rule, so the
re-run rewrites them rather than a hand edit.

**Your two disputes should stand until the re-run, not be withdrawn.** They are
correct, they are the reason this was found, and the re-run is what clears them.

## The sequencing you asked about

Your policy-family brief says to re-run §1 **after** the acronym check is
settled, so both halves are measured with the same ruler. **It is settled now.**
The order is therefore: apply the approved copy fixes, then re-run §1 across the
family, then read the machine half against your human half on the same text.

**One caution, and it is why this file does not claim more than it should.** The
six cases above are the disputed strings driven through the real function. They
are not the eight rendered pages. **The re-run against the actual pages is what
proves this on the site, and it has not been done yet**: the video run holds this
machine at present and a page sweep queues behind it.

*No em or en dashes in this file; checked before writing.*
