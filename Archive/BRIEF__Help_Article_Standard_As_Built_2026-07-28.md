# BRIEF: the Help article standard, as actually built on 49 articles

**From:** Claude Code · **Date:** 2026-07-28 · **Authority:** Kain, ruled live during the session
**For:** folding into `help-answer`, and wherever `house-copy-standards` needs to carry it

## Why this exists

Kain read a sample of the 49 Help articles imported on 27 July and called them thin, lazy
and evidently machine-written. Walking them one at a time with him produced a set of rules
that are sharper than anything currently in the skill. All 49 are now rebuilt to them and
live on achologytest.com. This brief hands you the standard so it stops living in a
conversation.

His own words on the result: "written human", and "about ninety five percent ready to take
to launch."

---

## The five rules, in the order they were ruled

### 1. Open in the reader's own words

The first line restates the reader's question back to them in the second person, and the
answer follows immediately in the same paragraph.

> **So how do you move up from Achology Member to Achologist?** Three things: complete one
> Practitioner Certification course, attend six live group training sessions, and receive
> six one-to-one coaching sessions as a client.

Kain called this "gold dust" and the thing that makes an article "feel warm, as if actually
written by a real person speaking to a real person."

Constraints learned in the building:
- **One sentence only.** The answer must still land inside the opening paragraph, which is
  what keeps the page liftable by a search or AI engine. A two-line preamble breaks that.
- **Write it; never convert the title mechanically.** Roughly half the titles are already
  personal ("How can I…", "Do I need…") and convert cleanly. The impersonal ones ("What are
  the six levels?") read stiff when converted and need a line written for them.
- **Never open on a short form the article has not yet spelled out.** Write around it: the
  session-length article opens on "one of Achology's live training sessions", not "a VALTS".

### 2. Spell out every short form before it is ever used

Full canonical name first, short form in brackets after it, and only then may the short
form stand alone. Never `SHORT (Full Name)`. Never a bare short form on first contact.

Kain: "these words don't mean anything to me… more cryptic than anything else."

Exceptions that had to be built in, each learned by breaking something:
- **Headings are left exactly as they are.** Spelling the term out in an H1 or H2 makes it
  long and clumsy. Kain ruled this at the same moment.
- **Never alter a canonical course, event or document name to comply.** "The CBT Toolkit",
  "Group Facilitation + VALTS Host Training", "The DiMAP Course Upgrade", "Achology CPD
  Handbook". Where the short form only ever appears inside such a name, write a defining
  clause alongside it instead.
- **Never rewrite a quoted article title inside link text.** That is the other article's
  wording.
- **Watch the grammar the expansion creates.** "a Virtual Achologist Led Training Session
  (VALTS) credit" needs the singular. "the Society of Modern Applied Psychology" needs its
  article. An attributive use ("SoMAP-accredited") takes none.

Canonical expansions in use: VALTS = Virtual Achologist Led Training Sessions; PALS =
Peer-Peer Applied Learning Sessions; CIPS = Competency Improvement Practice Sessions;
CCaC = Code of Character and Conduct; SoMAP = Society of Modern Applied Psychology;
DiMAP = Diploma Course in Modern Applied Psychology; CPD = continuing professional
development; UKRLP = UK Register of Learning Providers.

Applied across all 249 on 2026-07-28; 72 articles changed, then 10 hand-written where a
name blocked the mechanical fix.

### 3. Say "member of Achology", not "Achology member"

Kain's own simplification, and it solves a real ambiguity rather than papering over it:
"member of Achology" reads as a person, which leaves the capitalised **Achology Member**
free to mean the first level on the pathway. Any sentence about membership should carry
enough context that a first-time visitor knows what is being joined.

### 4. Attach every fact to the altitude it serves

**This is the rule that matters most, and it is what "thin" actually meant.** An isolated
fact is a defect however accurate it is. Every article climbs from its narrow answer to the
thing that answer belongs to, and says why that matters.

Kain: "so long as we can attach every small principle, every small idea, every small fact to
the higher purpose that it serves, then this knowledge hub becomes a hugely informational
signposting piece."

The ladder, worked on the session-length article:

- ninety minutes
- one of six live session types, all the same length
- the live sessions are where competence is built, because a technique only becomes yours
  once tried on a real person with honest feedback
- which is why the pathway requires them rather than treating them as optional
- and why a verified level means something to someone outside Achology

Corollary he gave for orphaned ideas: a single event type is explained as **one of many that
run every week and are open to every member of Achology**, never as a standalone curiosity.

Length follows from the climb being real. It is never padding. The 49 went from a median of
268 words to 402, and the ceiling is still the 500 to 1,500 guide in DSRD 2 §3.0.

### 5. Link like a vault, and never invent a link

Kain's stated goal: the Knowledge Hub as "the equivalent of a public-facing Obsidian vault,
strongly internally linked, informative, helpful, useful and shareable."

- Every named thing gets a link to its own article.
- **Every link is checked against what exists before it ships.** Where no article exists,
  the gap is logged and the thing is named without a link, never linked hopefully.
- The 49 went from roughly 4 links each to 358 across the set.

---

## The gate

Because a warning gets skimmed, the rules were made executable. `article_gate.py` fails an
article on: no opening line; under 320 words; a link target that does not exist; a short form
used before its full name; banned vocabulary; machine-written tells; em-dashes; first person;
"Achology member"; unbalanced brackets; an unterminated link; a lower-case paragraph opening.

It earned its place. It stopped an invented URL, a claim about Aristotle that was not
accurate, a mechanical sweep that would have broken "The CBT Toolkit" into nonsense, another
that deleted "Personal Growth and Development" from the learning-paths article, and one that
swallowed a `</a>` and would have unterminated a link on three live pages.

**Recommendation:** the gate belongs in the skill as the definition of done for a help
answer, not as a Code-side convenience.

---

## State: the whole section is finished

**All 249 rebuilt and live**, and the gate now reports zero failures across the section.

- median 372 words, shortest 320, longest 571
- 2,057 internal links, none broken and none pointing at a page that does not exist
- 249 of 249 open in the reader's words
- no em-dashes, no first person, no banned vocabulary, no undefined short forms
- **One accepted exception:** article 10050 uses VALTS inside "Group Facilitation and VALTS
  Host Training" before the expansion, because the event's name cannot be reordered. It is
  glossed in the same sentence.
- **The production note is gone.** One of the 49 had shipped with an internal build
  annotation published in bold at the foot of the article.
- **The 200 are done too.** Every one carries its opening line and has been rebuilt to the
  same standard as the 49.

## The gap register

Articles named in the text that do not exist. Logged rather than linked hopefully.

| Named in | Missing article | Why it matters |
|---|---|---|
| What is the duration of an Achology VALTS session? | **Principle-Based Reflective Discussion** | One of the six live session types. The other five each have their own article; this is the only item in that list that cannot be linked. |

## What I need from Chat

1. **Fold rules 1 to 5 into `help-answer`**, and put the gate in as its definition of done.
   The skill currently asks for "answer first, scannable detail, 500 to 1,500 words" and says
   nothing about the opening line, the altitude climb, short forms, or link verification.
2. **Rule on the gap register**: whether missing articles like the Principle-Based Reflective
   Discussion get written, and in what order.
3. **DSRD 2 §2.24** should carry the opening-line rule if it is to bind future page builds,
   since that is where the FAQ article structure is canonical.

Kain is separately working a set of acronym rules with you. Send them through this folder and
I will run them as a final sweep over the finished writing rather than alongside it.
