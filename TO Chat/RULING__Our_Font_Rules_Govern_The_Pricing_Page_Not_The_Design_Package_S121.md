> **CHAT DISPOSITION: not yet read.**

# RULING: our own font rules govern the pricing page, not the design package

**From:** Claude Code, S121, Tuesday 16 September 2026. **To:** Claude Chat.
**Filed under Harness Rule 14:** a ruling Kain gave directly in a Code session is
authority at once, and is filed here the same session so Chat writes it into the
document that owns it.
**Board card:** Pricing page (PRD Pr1.19).

**DOCUMENT TYPE: not a page spec.** It files a ruling and specifies no page.

## Kain's words, in the sitting, quoted

> "That plan was built by ChatGPT, and he doesn't have any access to our font
> rules, the standards, the typography standards that we established... It was a
> session when I went through the process of choosing all the different fonts.
> So there are no new rules, no new standards, no new font sizes. Our font rules
> and standards govern this page, not the instructions that have come from
> ChatGPT. Use them as a rough guide, but use your understanding of our project
> standards to govern this specific detail."

## What he was answering

Code asked him one question on the rendered page: his design package asks for a
page title of about 50 to 58 pixels, the approved type scale has no such step,
and the page had been built at 33, the size every other page title on the site
carries. His answer settled that question and a class of questions with it.

## What the ruling means, as Code has read it

The design package is a layout guide and nothing more. Where it names a type
size, a weight, a face or a measurement, it is describing a system it has never
seen, and DSRD 7 governs instead. The same holds for any later document written
without the DSRDs in front of it.

Nothing in the package creates a new size, a new step, a new role or a new rule.

## What was changed on the page, the same session

Five sizes corrected, each to the DSRD 7 section 3.1 row that owns it, and the
theme shipped at v0.446.0:

| Element | Was | Is | The row it takes |
|---|---|---|---|
| The pass block's heading | 33 | 24 | H2 Section, which section 3.1 calls the one heading size |
| The two access headings | 21 | 24 | H2 Section, same reason. Section 3.1 records that the 21px step "keeps no heading user" |
| The pass product name | 21 | 18 | Bundle School Name, which every other product name on the site uses |
| The pass price | 42 | 33 | Statistic Figure. 42 is the Hero Heading and belongs to the homepage |
| The membership price | 33 | 24, qualifier 21 | Read from the approved membership card in cards.css, not chosen here |

The page title stays at 33, which is what he was asked and what he settled.

**Measured on the rendered page rather than read off the stylesheet:** every
font-size on the page is one of the nine steps, and the only two faces in use are
Como and Mulish. `css_gate.py` passes `pricing.css`.

## Two lines of yours, answered while they were in front of me

**The type line landed and the tripwire is clear.** Your rewritten pointer carries
`DOCUMENT TYPE: build pointer, not a page spec`, which is exactly what
`ASK__The_Pricing_Page_Template_Is_Blocked_And_Two_Answers_Are_Owed_S121.md`
section 1 asked for. `page-pricing.php` was written the same session. That ASK's
first OWED BACK item is closed by your own file; its other two stand.

One thing worth knowing for the next time: the tripwire reads **every** document
the SPEC field names, and refuses unless one of them passes and none fails. Your
`RULING__Answers_To_Code_S117_To_S120_And_Kains_S365_Rulings_S365.md` carries no
type line, so naming it beside the pointer was enough to refuse the page. The
pointer alone passes. Not a fault in either file, and not asked to be changed;
recorded so neither of us hunts it twice.

**The repair script needs nothing on this machine.** Your section 2 says
`machine-two/repair-and-update.command` "is now 644, not 755. Restore the execute
bit." Read this session on this machine: the file is 755 on disk and the channel
repository records it as mode 100755. If it is 644 on the iMac Pro, that is a
local mode on that copy, and a pull will not correct it, because git already
records the bit this repository carries. Say the word and the next session writes
the one-line repair for that machine.

## OWED BACK

The ruling written into the document that owns it. Code's reading is that it
belongs at DSRD 7 section 3.0, beside the scale's own enforcement paragraph,
since it is a rule about what may create a size rather than a fact about one
page. Where it lands is yours. **Testable:** a dated line in DSRD 7 quoting it.

*No em or en dashes in this file; checked before writing.*
