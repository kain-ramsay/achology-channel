CHAT DISPOSITION, S310: read. Superseded by HOLD__The_Body_Face_Is_Reopened_S084; stays until Kain rules the face in Safari, then closes with the DSRD 7 rewrite.

# RULING: the body face is Literata. DSRD 7 section 3 needs rewriting.

**Ruled by:** Kain, in session, Claude Code S084, 25 August 2026.
**Filed under Harness Rule 14** in the same session the ruling was given.
**Shipped:** theme v0.102.0, deployed and proved, live on every page.

---

## His words, quoted

> "Literata! I wish i'd known this existed sooner - it's perfect for Achology."

## What he was looking at when he said it

Not a description. **Four whole pages of his own copy, each one rendered twice**, in Safari: a help article, the Man's Search for Meaning book note, About, and the Trust Statement policy page. Same page, same content, same Como headings, one thing different.

The comparison was built by capturing each live page as the server serves it and re-serving it with the body face swapped on the computed face of every element that is not Como. Headings, labels and the logo lockup were untouched in both, so what he judged was the pairing and not the headings.

**It was flagged to him before he looked**, in these terms: it touches every page, it shifts spacing, and DSRD 7 section 3 needs rewriting if he takes it.

## What was changed in the theme, and it is smaller than it sounds

**One token and one font request.**

`base.css` has carried a `--font-body` token since before this session, and **every other mention of Source Sans 3 in all fourteen stylesheets is inside a comment.** That was checked before the token was touched, not assumed. So:

- `base.css`: `--font-body: 'Literata', Georgia, 'Times New Roman', serif;`
- `functions.php`: the Google Fonts request now asks for Literata as the variable font across 400 to 700, upright and italic, with its optical size axis. Caveat still rides the same request, unchanged.

Every weight the theme sets is now a real cut rather than one the browser synthesises, and the optical size axis is what makes the face hold at 16px, which is the whole reason it was the candidate.

`css_gate.py` passes on all stylesheets. Verified on the rendered live pages, not in the source.

## WHAT CHAT OWES, and this is the part that matters

**DSRD 7 section 3's pairing sentence is superseded.** It currently reads, quoted from the canonical file tonight:

> "Font pairing: Como (headings/labels) + Source Sans 3 (body text). Como self-hosted (licence held, all 8 weights). Source Sans 3 from Google Fonts."

Its rewrite is yours. Section 3.2 is titled "Source Sans 3 Styles" and every row in it names the face; so do rows in sections 12 and 14 and the count-label line at the foot. **I have changed none of them**, because Code never edits a DSRD.

**Section 4 needs re-ruling too, and it is the consequence nobody would notice.** Section 3 is not the only place the old face is load-bearing. Quoted from section 4:

> "A page of continuous prose sets its column so a line runs 45 to 75 characters. 620px is the value that delivers it at 16px in Source Sans 3, measuring 72 to 77 characters across the ten pages it now governs."

**That 620px was tuned for a face the site no longer uses.** Measured on the rendered comparison, the reading line shortens by roughly a tenth in Literata:

| Page | Source Sans 3 | Literata |
|---|---|---|
| Help article | 135 | 119 |
| Book note | 119 | 104 |
| About | 115 | 101 |
| Policy page | 96 | 85 |

So a column tuned to land at 72 to 77 characters now lands nearer 65, which is still inside the 45 to 75 band but is no longer the value the sentence claims. **The number needs re-deriving against Literata, and it is a design ruling rather than a measurement I should take.**

## What this ruling does not carry

**No prototype fold-back.** Rule 14's fold-back applies where a ruling approves how a component looks; this is a design foundation, so its record is this file plus your DSRD 7 rewrite, and there is no component folder for it to land in.

**Nothing about weights or the type scale.** He ruled the face. The nine-step scale, the weight rule and the responsive rule are untouched and stay where they are.

## One thing worth your eye at the next Safari sitting

Every DSRD 6 record on this site that carries a passing accessibility or visual-consistency line was read against the old face. **None of those lines is now wrong on its face**, because nothing about size, weight or colour moved. But the rendered pages they judged no longer look the way they looked, so a page whose record was closed on appearance is worth a second look when it next comes up rather than a re-run of everything now.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
