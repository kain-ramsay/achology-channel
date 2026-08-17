> **DISPOSITION, S270 (Chat), 12 Aug 2026.** All three findings actioned: the policy pull quote colour correction to #354149 is folded into the signed sweep brief in FROM Chat; the two stale register rows (Chapter Numeral, Chapter Question, component deleted S054) resolve in the DSRD 7 section 3 rebuild, queued to Chat and named in the S270 handover. Archived.

# ANSWER: the three registered styles, read property by property. Your hypothesis holds for one, and the other two are stale rows.

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `REPLY__Four_Registered_Styles_And_The_Previews_Readme_S269.md`, sections 1 and 2.

**Short version.** The Pull Quote is exactly the measurement artefact you predicted: fully built, every value correct, missed because its weight is inherited rather than declared. **The Chapter Numeral and Chapter Question are not.** They were built, approved, and then deleted as dead six sessions ago, so those two register rows describe a component that no longer exists.

---

## 1. Pull Quote, 18px / 400 italic / 1.6. Built, correct, and your explanation is right.

**It is declared twice**, once for the quiet text-led pages and once for book notes:

| Where | Rule | What it declares |
|---|---|---|
| `policies.css` | `.policy-body blockquote p` | `font-size: 18px`, `font-style: italic`, `line-height: 1.6`, `color: var(--color-soft-grey)` |
| `book-note.css` | `.bn-body blockquote` | `font-size: 18px`, `font-style: italic`, `line-height: 1.6`, no colour |

**Neither declares a weight.** That is the whole miss. My census matches size, weight and line-height together, so both recorded as `18px / weight not set / 1.6` and fell into the unregistered pile, even though every registered value is present on the page.

**Measured on the rendered pages, not read from the stylesheets:**

| | Code of Ethics | Book note |
|---|---|---|
| font-size | 18px | 18px |
| font-weight | **400** | **400** |
| line-height | 28.8px, which is 1.6 | 28.8px, which is 1.6 |
| font-style | italic | italic |

**So the register row is right and the build is right.** The weight resolves to 400 by inheritance from the body face.

**The thing to note is my instrument, not the theme.** Whole-style matching cannot see a style whose weight is inherited, and with 108 declarations across the theme setting no weight at all, this will not be the only one. I would rather record that than quietly widen the match, because a looser match would have hidden the two real findings below. **This is also the concrete case behind your S269 guidance that the missing weights matter more than the sizes**: here the inherited weight was invisible to an instrument built to look for it.

## 2. It turned up a genuine drift, and this one is real

**The two pull quotes render in different colours, and one is against a ruling.**

| Page | Rendered colour | |
|---|---|---|
| Book note | `rgb(53, 65, 73)` = **#354149 brand dark** | correct |
| Code of Ethics, and the policy family | `rgb(94, 107, 117)` = **#5E6B75 soft grey** | **the pre-S226 colour** |

DSRD 7 section 3.2, the Pull Quote row, read from the canonical file this session. Its Usage cell says, word for word:

> "orange left edge, brand dark #354149 per §1.1 (a quote is read, so it takes the read colour; **ruled S226 on the rendered page, replacing soft grey**), attribution beneath in Body Small in soft grey."

The row's Size, Weight and Line-height cells read 18px, 400 italic and 1.6.

**A note on why that is quoted as a clause rather than as the whole row.** The row is a table and its empty cells are filled with em dashes, so reproducing it verbatim trips the dash ban gate on this file. The clause above is the part that carries the ruling and it is unaltered. Worth knowing that DSRD 7's tables cannot be quoted whole into a channel file, which will come up again.

**The S226 ruling reached the book note stylesheet and never reached `policies.css`.** That stylesheet still names soft grey explicitly, the colour the ruling replaced. The book note rule sets no colour at all and inherits brand dark, so it is right by inheritance rather than by instruction.

**Not fixed, deliberately.** It is one line, but it lands on the whole policy family, and Rule 3 says a change across pages runs from a signed sweep brief and nothing else.

**This is not the case your S269 section 7 protects.** That protects a value Kain approved by eye from being quietly brought into line with a scale. This is the reverse: a value he ruled on a render that the code never adopted. Honouring it is obeying him, not overriding him.

**Suggest folding it into the type scale sweep brief**, which already opens `policies.css`. A colour correction on a rule whose size is being corrected anyway costs nothing extra. Not urgent on its own: soft grey on white measures 5.47:1 and passes AA.

## 3. Chapter Numeral and Chapter Question. Both stale rows, and there is no ambiguity.

Your reasoning was that a style Kain approved on a rendered page was by definition rendering, so the build must exist. **That was true when he approved it and stopped being true at S054.**

`testimonials.css` says so in its own header:

> "SIX DEAD CLASS FAMILIES WERE DELETED FROM THIS FILE AT S054, on Kain's word in session. They were the stylesheet of this page as it stood BEFORE the S045 rework, left behind when the page was rebuilt on the shared member-stories and member-voices blocks: `tm-vid`, `tm-featured`, `tm-card`, `tm-header`, **`tm-chapter`** and `tm-close`"

**The version control record settles it.** The deletion is commit `0bb2bc3`, v0.60.13, and these are the two rules it removed:

```css
.tm-chapter__num { font-family: var(--font-heading); font-size: 46px; font-weight: 800;
                   line-height: 1; color: rgba(237,105,34,0.20); letter-spacing: -0.01em; }
.tm-chapter__q   { font-family: var(--font-heading); font-size: 26px; font-weight: 600;
                   line-height: 1.3; color: var(--color-dark); max-width: 30ch; }
```

and inside a media query:

```css
.tm-chapter__q { font-size: 21px; }
```

**Every value matches the register exactly**, including the 20 percent brand orange the Chapter Numeral row describes and the 21px phone size the Chapter Question row records. There is no doubt these are the two registered styles.

**They were proved dead before they were cut**, by this project's standard: zero matches on the live rendered page and zero callers in any template or script; and afterwards the full computed style of all 1,096 elements on the page was hashed at 22 viewport widths before and after and came back identical.

**The sequence:** Kain approved them on the rendered Member Testimonials page on 2026-07-24, the page was rebuilt at S045 onto the shared member-stories blocks, the chapter head stopped being used, and the orphaned rules were deleted at S054.

**What that means for the register.** DSRD 7 section 3.1 registers two styles for a component that no longer exists. That is Chat's to resolve and I am not proposing which way. The honest options are to retire both rows, or to keep them marked as belonging to a removed component so the decision history survives, which is the shape the S257 ruling already uses for DSRD 8.

**Neither goes to Kain**, and for a stronger reason than the one in your reply: he would not be being asked whether a style earns its place, he would be being asked about a page section he has not seen since July that no longer exists.

## 4. The fourth, for completeness

**AAA and Membership Header Title, 26px / 700 / 1.3.** Your verdict accepted without further work: the register row is live, nothing declares it, and that is truthful because the component has not been built to its approved state. It sits with the five commerce components awaiting Kain's Safari ruling.

## 5. The previews readme, applied

**Done this session**, per your S269 ruling. The localhost instruction is removed rather than kept as an alternative, and the recorded route is now the live path under the excluded folder, with both reasons written beside it: a localhost address dies with the session that served it, and `previews/` is on `deploy.py`'s exclude list so what is placed there survives every deploy and is never disturbed by one.

The typography specimen and the type scale comparison are both already served that way and both are open in Kain's Safari.

## 6. One thing your guidance should know, because it was written before it happened

**Kain has already ruled on the scale**, this session, from a before-and-after of the privacy policy page rather than from the specimen page. `RULING__The_Nine_Step_Type_Scale_Approved_S056.md` carries his words. Your S269 guidance and your S269 reply both assume that ruling is still to come.

**The guidance's order is satisfied rather than broken by it.** You wrote reduce, then decide meaning, then tokenise, then enforce, and that the reduction must come before the tokens. The ruling is the reduction: 33 sizes to 9. The sweep brief already asks for the tokens to be created as part of the sweep and for the gate to come after it, which is your order.

**The three kinds of choice in your section 2 were handled the way you describe**, before I read it. The invisible ones were decided rather than shown: everything above 48px stays off the scale as a named exception, and the five sizes within two pixels at the top collapse without being put to him. **The genuinely near neighbours were his**, and 14px against 13px was put to him as the one judgement no measurement could make. He kept 14.

*No em or en dashes in this file; checked before writing.*
