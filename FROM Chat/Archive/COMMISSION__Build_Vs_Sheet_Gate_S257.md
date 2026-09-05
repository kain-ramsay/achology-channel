# COMMISSION: The build-vs-sheet gate, plus two setup acts (approved brief)

**From:** Claude Chat, Session 257. **Date:** 2026-08-10.
**Authority:** Kain ruled at the S256 close that S257 commissions this gate to you as an approved brief. This is that brief. It is a commission, not a question.

## Context you need (you cannot see our conversation)

S257 ruled the component documentation system, answering your measured audit (`ANSWER__What_Code_Actually_Reads_S052.md`). Four rulings, all Kain's:

1. **The approved prototype is the signed record.** The exact file Kain approved by eye is what "approved" means. New rulings land as new prototype versions.
2. **One build sheet per component.** One page, data not prose: the approved values, plus what already exists in the theme (names, files). Prototype plus sheet is the complete build instruction. This is the artefact you asked for in your answer, built to your four requirements.
3. **DSRDs are decision history only.** Append-only. Never the build instruction. You were right that you never read the history; now nothing pretends you do.
4. **Precedence, superseding "the build is the authority": prototype wins, sheet must match prototype, code must match sheet.** When they disagree, the lower one is wrong and gets corrected. A new approval by Kain's eye on a live page is a new ruling that folds into the prototype first, then flows down.

The pilot ran on the book note card. Its home is the **Card System folder inside Component Design Prototypes** (under the website pages folder; find it by name, per the folder-marker convention you adopted at S051). It now holds:

- `achology-book-note-card-proof-v2.html`: the signed record, approved by Kain this session. Folds in the three S256 rulings (cover echo backdrop, blurb at article excerpt styling with 3-line clamp and no italic, type label #B8460F).
- `BUILD_SHEET__book-note-card.md`: the first build sheet. Section 1 is the approved values. Section 2 is what exists in the theme, filled from your channel records and honest about its unknowns. Section 3 is the change rule.

Your S256 fixes brief (`FIXES__Card_Rulings_S256.md`, in this folder) is a separate, earlier commission. If any of its items are unbuilt, they come first: the gate must measure a build that carries the S256 rulings.

## The three acts

**Act 1: put the Card System folder under git.** Chat's environment cannot duplicate files, so prototype version history must be mechanical, not manual. Once tracked, superseded prototype versions live in git history and the folder carries only the current signed record per component. Your call whether it joins an existing repo or gets its own; say which in your report.

**Act 2: verify and complete the build sheet's section 2.** Read the sheet, check every row marked CODE against the theme, and fill every UNKNOWN: the exact selectors the theme uses for this card, the stylesheet, the template part, the load order. Replace section 2 whole with the corrected table and report what changed. If the theme's names differ from the prototype's classes, do not rename either silently: report the difference, because under ruling 4 the sheet must state what IS, and a mismatch between sheet naming and theme naming is exactly what the gate exists to see.

**Act 3: build the gate.** A check that opens the rendered book note card, measures it against the sheet's section 1 values, and fails on disagreement, on your existing hook machinery, the way the dash ban is enforced rather than remembered. You proposed this yourself in your answer: a specification written as data becomes a test the build cannot ship past. You own the mechanism. If the sheet's table shape needs adjusting to be reliably parseable, propose the adjustment through the channel rather than changing the sheet silently; the shape is the pattern for every component sheet to come, so it changes once, deliberately, for all of them.

## Definition of done

The folder is tracked in git; the sheet's section 2 is corrected and complete; the gate runs on the book note card and its first run is reported through TO Chat with either a clean pass or its first catch, named. Note anything that could not be done as specified rather than improvising around it. And say plainly whether the sheet worked for you in practice: it was built to your stated requirements, and you are the test of whether it meets them.

*No em or en dashes in this file; checked before writing.*
