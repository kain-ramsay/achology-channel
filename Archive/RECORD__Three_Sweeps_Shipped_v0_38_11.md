# RECORD: the three signed sweeps, shipped and verified live at v0.38.11

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Closes:** `BRIEF__Sweep_Header_Footer_Chrome_Names.md`,
`BRIEF__Sweep_Help_Category_Descriptions_Sentence_Case.md`,
`BRIEF__Sweep_Phone_Tier_Shared_Separators.md`. All three archived.
**Deployed** to achologytest.com over SSH, caches flushed, active theme confirmed
at 0.38.11. Every result below was read off the rendered live page this turn, not
from the source and not from memory.

---

## Sweep 1: header and footer chrome names

Three strings changed in `header.php`, each in both the desktop dropdown and the
mirrored mobile nav overlay:

| was | is |
|---|---|
| Coaching + Professional Helping | Life Coaching and Skilled Helping |
| Personal Development and Growth | Personal Growth and Development |
| Explore the Academy of Modern Psychology | Explore the Academy of Modern Applied Psychology |

REF 1 §1.5, read this turn: "The canonical full name is **the Academy of Modern
Applied Psychology**, and the short form is **AMAP**."

**Verified on the rendered page:** all seven registered names present and correct
in the header, all seven in the footer, both corrected names present in the mobile
nav, and none of the three old strings survives anywhere in the delivered markup.
The footer already conformed and was not touched, as the brief directed.

**Definition of done item 3 is yours, not mine.** The brief asks that the §1 chrome
findings in the DSRD 6 records for About, Testimonials and the Policies index be
re-verdicted under this ruling. Those records are filed here; the build now matches
the registered set, so every one of those findings can be closed as a pass.

## Sweep 2: the 15 help category descriptions

All 15 replaced in `faq-setup.php`, casing only.

- **Before the edit:** lowercasing the old and new strings produced identical text,
  **15 of 15**, which is the mechanical verification the brief specifies.
- **After the edit:** the file's 15 strings match the brief's 15 exactly, **15 of 15**.
- **Read back from the live database after deploy:** every one of the 15 live terms
  carries its exact approved string, **15 of 15**. This is the read-back the brief's
  definition of done requires.

Proper nouns and acronyms keep their capitals: Achology, CPD, Access All Areas Pass.

Version gating followed the v0.36.10 pattern: the one-time refresh flag moved to
`_v3`, so the new copy reached the live terms once and then retired. Kain's own
admin edits can never be overwritten by it again.

## Sweep 3: phone-tier conformance on the shared separators

DSRD 7 §4.3 ruling 4, read this turn: "The measurements are 48px on desktop and
tablet, 32px on phones. Nothing else, at any width, on any page."

Both named separators had **no phone tier at all**, so both read 48/48 below 768px.

**Measured on the rendered live pages, both widths:**

| separator | desktop | phone |
|---|---|---|
| `.policy-body--ruled + .policy-body--ruled` (Testimonials) | 48 above, 48 below, 1px line | 32 above, 32 below, 1px line |
| `.help-popular` (help landing) | 48 above, 48 below, 1px line | 32 above, 32 below, 1px line |

The helpful strip's own `padding-bottom` drops to 32 with it. That side owns the
space above the line, and leaving it at 48 would have produced exactly the uneven
boundary §4.3 ruling 4 forbids.

Written as hand tiers on the components' own rules. `--sp-2xl` was not touched, per
the brief. No page-local spacing declarations were added anywhere.

**The false comment is corrected.** It claimed no other template stacks two
`.policy-body--ruled` wrappers. The rendered Testimonials page carries exactly one
such stacked pair, so the claim was untrue. The note now says so and names the three
pages that share the separator.

`css_gate`: **PASS** on `components.css` and `help.css`.

---

## One contradiction between a document and the code, for your ruling

I am not deciding this and I have not touched it.

**DSRD 7 §4.3 says:** "Use `var(--sp-2xl)`, whose standard mobile reduction produces
exactly this behaviour."

**`base.css` line 90 says:** `--sp-2xl: 48px;` and there is no mobile reduction on
that token anywhere in the file. The reductions that do exist are hand written per
rule, in the pattern at base.css line 729.

So the document describes a mechanism the code does not have, which is why both of
these separators silently read 48/48 on phones: whoever wrote them followed §4.3's
sentence exactly and got the wrong result. Any future separator written to that
sentence will have the same defect.

Two ways out, and the choice is Kain's through you: give the token a real mobile
reduction, which touches every page at once and needs its own sweep; or amend §4.3
to say the tier is hand written per separator, which matches what the code actually
does today. I recommend the second, because the first changes rendered spacing on
pages nobody has re-gated.

**Pages affected by these three sweeps, for your records:** the Policies index,
About and Testimonials via the ruled pair; the help articles, the help landing and
the 404 via `.help-popular`; every page on the site via the header and footer.

*No em or en dashes in this file; checked before writing.*
