# REPORT: stage 5 passes all fifteen, and two things it found on the way

**From:** Claude Code, Session 095. **Date:** 2 September 2026.
**Answers:** BATCH__instructor-article_ready_for_stage_5_S316.md, its stage 5 half. Stage 6 has not run and is not started.
**Board card:** the eighteen instructor articles.

---

## The verdict

**Fifteen of fifteen pass all three checks.** Fields complete, body shape, named files exist. Nothing is held back and nothing needs fixing at source.

**Your stop condition does not fire.** Every one of the fifteen register rows carries the slug your table names, checked row by row against the table this turn. The register was rebuilt on 26 August and its instructor-article rows are current.

The three held records, I04, I14 and I18, were not run. They are not in your ready list.

`stage5_import_checks.py` now does this by machine, so the next batch of any type costs one command. Its acceptance run breaks a real record four ways, one fault per check, requires each to go red, then runs the untouched record as the control and requires it to pass: without that control a checker that refused everything would score full marks. Five of five.

## Two findings, and the second is the one that matters

**Every one of the fifteen carries none of the five fields section 3.1 gained at S329.** No `search_intent`, `reviewed_by`, `update_cadence`, `query_variants` or `schema_type`, on any of them. They were drafted before the standard existed.

I did not fail the batch on them, and that is a judgement I am naming rather than taking quietly. Section 3.2 now requires all five, so a strict read fails all fifteen on fields that did not exist when Cowork drafted them, which would be literally correct and would tell nobody anything. They are counted and named on their own line instead. **This is the same backfill question the S095 pre-draft gate report puts to you, and it now has a batch sitting behind it.**

**Half of check 2 was measuring nothing, and it took a deliberate look to see it.** The `instructor-article` entry in `content_gate_standards.json` rules neither a `sections` map nor a `section_count`. So the checker printed a clean structural line over bodies carrying between six and eight headed sections, having compared them with nothing at all. It now prints NOT MEASURED and says why.

**This is the S090 finding again, on a second type.** Then it was `field-authority-article`, added with a bare `section_count` the gate could not read; the fix went into the gate. This is the other half of the same hole: a type entered with no structural key at all, where both the content gate and this checker have nothing to test and both report clean. **Two types is a pattern, not an accident, and the fix is in the standards file rather than in either checker.** What shape an instructor-attributed article's body takes is DSRD 2's and yours, not mine, so the entry stays as it is until you rule.

## What stage 6 will hit, so it is not a surprise

**All eighteen instructor articles are in the trash on the build install**, checked this turn: 51 published articles there are all author biographies, and every instructor article sits at `post_status` trash with a `__trashed` slug. Whatever stage 6 does, it is not updating live pages; it is a fresh import, and the trashed rows and their old slugs will want deciding on before it runs.

**Only one article anywhere on the install carries a source book**, I14's, and I14 is one of your three held records and is also trashed. That matters beyond this batch: the signed article page spec asks Kain to see the source block's case one on a real page, and today no page on the install can show it.

## The signed article page spec is stale, and I stopped rather than build to it

Separate finding, from the same look. `SIGNED_SPEC__The_Individual_Article_Page_S302.md` sits in FROM Chat waiting on Code to build the page to it. **It should not be built to.**

Its section 2 block order and its section 3 card ruling were superseded by Kain's own later sitting. DSRD 9 §22.1 now carries the reordered foot, the course row above the reading row, the page closing on the enquiries panel, and it records the spec's order in as many words as *"the superseded order, kept as a record"*. §22.8 reads "a list of links", not three cards. §22.10a takes the Where next panel off the page. The template already matches the DSRD on all three, and the fallback book the spec asks to be deleted was deleted at S080.

So building the page to that spec would undo rulings Kain gave on renders after it was written. The spec's own standing rule 19 says build only to it, which is precisely why this needed saying rather than deciding: **the spec and the DSRD disagree, and the DSRD is the standard's home.**

What is genuinely still owed from that spec is its section 9, the sitting: Kain has never seen the real thing. That waits on the eighteen being out of the trash, which waits on this batch.

---

OWED BACK: the backfill ruling for records drafted before S329, the structural entry for `instructor-article` in the standards file, a corrected or withdrawn article page spec, and a word on whether stage 6 imports fresh over the trashed rows. The score table, the four gap answers and I13's hyphen come with stage 6 and are not owed yet.

*No em or en dashes in this file; checked before writing.*
