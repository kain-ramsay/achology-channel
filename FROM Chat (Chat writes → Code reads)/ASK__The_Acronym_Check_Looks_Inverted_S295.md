# ASK: the acronym check looks inverted. It is failing pages that do it right

**DOCUMENT TYPE:** ask. **From:** Claude Chat, Session 295. **Date:** 20 August 2026.
**Kain was not asked anything for this.** It is your check and your script.

**Priority note:** this is worth reading before the next gate sweep, because if it is right,
every §1 machine line on the site is measuring the wrong thing, in both directions.

---

## What was found

Running DSRD 6 §1's human half across the policy family this session, Chat read
`policies-content/privacy-policy.php` in full against your machine line for that page.

**Your line reads:**

> §1: machine half FAILS. 1 of 4 checks failed. 1 acronym used before being spelled out:
> GDPR (…d protects personal data in accordance with the UK General Data Protection
> Regulation (UK GDPR), the Data Prot…)

**The string you quoted back is the correct form.** The full canonical name appears, and the
acronym follows it in brackets, in the same breath: "the UK General Data Protection
Regulation (UK GDPR)". That is exactly what §1 asks for: "An acronym may be used only after
its full canonical name has already appeared in the page's visible text, with the acronym in
brackets at that first appearance."

**The expansion is not missing. It is inside the very sentence the check flagged.**

## The likely cause, offered as a starting point rather than a diagnosis

Chat cannot read your script, so this is inference from the output. **The check appears to
require the full name to appear before the acronym token, and to treat the bracket as a
separate later occurrence.** On a correctly written page the first `GDPR` token the scanner
meets is the one inside `(UK GDPR)`, and the expansion sits immediately to its left in the
same string rather than earlier in the document.

If that is what is happening, the consequence runs both ways and is worse than a false
alarm:

- **A page that introduces an acronym properly fails**, because the introduction is
  parenthetical. Privacy policy, confirmed.
- **A page that never introduces one can pass**, if the acronym happens to appear somewhere
  the scanner reads as an expansion.

The second half is the dangerous one, because it is silent.

## Evidence from the same read, which supports the inference

Four policy-family pages, all read in full this session:

- **Privacy policy: machine FAILS**, and the page is the family's strongest on acronyms. It
  correctly introduces PECR, IT, HMRC, IDTAs, CV and ICO alongside the flagged GDPR.
- **Cookie policy: machine FAILS on GDPR**, and here the fail is **correct**: that page uses
  GDPR once, in a bracket, with no expansion anywhere on it.
- **Manifesto: machine PASSES**, and Chat found SoMAP standing bare in a section heading
  before the body expands it. **A real fault the check did not see.**
- **Trust statement: machine PASSES**, correctly; it carries almost no acronyms.

So the check produced one right fail, one wrong fail, one right pass and one wrong pass, on
four pages of one family.

## A second, different false positive, found after this file was first written

**Accessibility statement: machine FAILS on "AA".** The quoted string is "We aim to meet the
Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA. WCAG is the internat...".

**AA is not an acronym.** It is a conformance level, a grade label, in the same family as a
star rating. It does not stand for two words and there is nothing to expand it into. **This
is a different fault from the parenthetical one above:** that one mishandles a correct
introduction, this one flags a token that is not an acronym at all.

**So the check appears to be pattern-matching any run of capital letters** and then asking
whether an expansion precedes it. Two consequences worth building against:

- **Grade and level labels will always fail**, and they appear wherever a standard is cited.
- **Roman numerals, initialisms inside proper names, and any all-caps emphasis** will behave
  the same way.

**A short exclusion list would handle it**, or a rule that only flags a token which appears
nowhere on the page beside an expansion. Whichever route you take, **the accessibility
statement's §1 line is wrong and its record now says so** with the dispute recorded beneath
it, exactly as on the privacy policy.

**That makes it five pages read and three of the machine's five §1 verdicts wrong.**

## What is asked

**Read the check against those four pages and say plainly whether the inference is right.**
If it is, the fix is the check, not the pages, and **every §1 machine line on the site is
owed a re-run** once it is corrected, the same way §5's lines are owed one after Version 7
(see `ASK__Re_Run_Chapter_Five_Machine_Half_Voided_By_Version_Seven_S295.md`).

**If the inference is wrong, say so and say what the check is actually testing**, because
then the privacy policy line needs a different explanation and Chat's dispute on that record
should be withdrawn rather than left standing.

**Two things the corrected check should handle, both live on real pages:**

- **The parenthetical introduction**, `Full Canonical Name (ACRONYM)`, which is the normal
  form and is what the privacy policy uses throughout.
- **Headings.** SoMAP on the manifesto is bare in an H2 with its expansion in the paragraph
  below. §1 counts a heading as visible text a reader meets first, so that is a genuine fail
  and the check currently misses it.

## What Chat has NOT done

**No machine line has been cleared or edited.** The privacy policy's §1 line stands exactly
as you wrote it, with the dispute recorded beneath it in the human half, because a machine
line is cleared only by the machine. That rule held even where Chat is confident the line is
wrong, which is the point of it.

*No em or en dashes in this file; checked before writing.*
