# QUESTION: what should decide whether boundary spacing is "inside a component"?

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**Asked because Chat asked for it**, in `RULING__Gate_Check_4_Authorised_And_Icon_Sweep_Answers_S263.md` section 1: "That is a real design fault in the instrument, but the fix is a different question from tonight's exemption... Write it up as its own question when you next have room and Chat will bring it to Kain properly."
**Nothing is changed by this file.** The authorised hairline-owner exemption is built and shipped; this is the second finding, unbuilt.

## What I checked before asking

DSRD 7 section 4.3's "Applies to" paragraph, DSRD 8 sections 6 and 12, Chat's S227 ruling as quoted in the checker's own comment, and the checker's implementation. The question survives all four, which is why it is here rather than answered.

## The question in one sentence

**Chat's S227 ruling says check 4 should "fail only on spacing declared outside a DSRD 8 component", and the checker implements that by harvesting class-shaped strings out of DSRD 8's prose with a regular expression, which is not the same test.**

## Why the current test cannot be right

The checker reads DSRD 8, pulls out every string that looks like a class name, and asks whether the declaring selector contains one. Tonight that yields **exactly 61 names**, and membership depends on whether the document happens to spell a class rather than on anything structural.

Three consequences, all live:

1. **`.about-grid` and `.about-proof__strip` pass** only because DSRD 8 section 12.1's table lists them. That table is titled "Page-Local Blocks (NOT LIBRARY COMPONENTS)", so the check is passing them on the strength of a table that exists to say they are not components.
2. **`.gi-block--rule-above` failed** even though DSRD 8 section 21 IS the global impact block, a named, built, approved component. The section describes it in words and never writes the class.
3. **`.pp-group` failed** because Our People has no section 12 table at all. Nothing about the block changed; only whether a document mentioned it.

## And the ground has moved underneath the test

The S257 component truth ruling made DSRD 8 a **decision-history document**. A component's values now live in its prototype and its build sheet. So the checker is deciding component membership by string-matching against a document that, by ruling, is no longer where a build reads values from. That is the deeper reason this needs settling rather than patching: the test was reasonable in the world it was written for and that world is gone.

## What I am NOT proposing

I have not picked a replacement, deliberately. Three are available and choosing between them is a decision about what a component IS, which is not mine:

- **By artefact.** A class is component-internal when the component has a build sheet in Component Design Prototypes naming it. Truthful under S257, and today it would recognise seven components and nothing else, so most of the site would fail.
- **By stylesheet.** Spacing declared in the component's own stylesheet counts. Cheap and mechanical; it would bless anything in `global-impact.css` and `people.css`, including a genuine page-local mistake.
- **By registry.** A short explicit list of component class prefixes, maintained deliberately as part of DSRD 8 or the build sheets. Honest and readable, and it costs a maintenance step nobody currently owns.

## One thing worth saying about how much this now matters

**Less than it did this morning.** The authorised hairline-owner exemption removed twelve of the thirteen boundary-owner failures across the built pages, and the one that survives on `/help/` is a genuine defect that any of the three options above would still catch. So this is not urgent. It is a correctness question about an instrument that is currently giving the right answers for a reason that will not hold.

## What I need back

**A ruling on which test replaces the regular expression**, or a decision to leave it as it is with the reasoning recorded so the next person does not rediscover this. Either is a real answer. What should not happen is the current test staying in place unexamined, because it passes and fails page-local blocks according to whether a sentence somewhere happens to spell their class name.

*No em or en dashes in this file; checked before writing.*
