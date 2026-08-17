# GUIDANCE: how to think about standardising the type across the whole site

**From:** Claude Chat, session 269. **Date:** 2026-08-12.
**Written on Kain's instruction**, after he read your typography census and asked what standards should govern the tidy-up.
**Follows:** `REPORT__The_Typography_Census_S056.md`.

**This is guidance, not a commission and not a ruling.** Nothing here is approved yet. Kain rules from the specimen page; this is the frame Chat suggests he rules inside, sent now because you are in the work.

---

## 1. The order, which matters more than any single rule

**Reduce, then decide what each value means, then tokenise, then enforce.**

There is no point turning 122 styles into tokens. That would enforce the mess rather than fix it. The set has to shrink first, and only the survivors become tokens.

Doing it the other way round is the common failure: a beautiful token file that faithfully encodes every accident.

## 2. Reduction: what earns a place

**A size stays if it does a job no other size does.** Not because something currently uses it.

Your finding that eleven distinct sizes sit between 10px and 20px carrying 232 declarations, in twelve consecutive pairs one step apart, is the whole argument. That is not a scale, it is a continuum, and a continuum means the same job was solved twice by two different people on two different days.

**Three different kinds of choice are hiding in that list, and only one of them is Kain's to look at.**

**The invisible ones are decided, not shown.** Five sizes within two pixels of each other at the top of the range, and eight watermark sizes tuned to two decimal places, have no visible difference between them on real text. Putting those to Kain would spend his eye on a choice with nothing in it. The project's own rule says so in as many words: where there is nothing to see, make the call, say what was decided, and move on.

**The genuinely near neighbours are his.** 14px against 13px, 12.5px against 12px. Those may or may not read differently on real words at real widths, and that is exactly what the specimen page is for, side by side on the same content.

**The genuinely distinct roles just stay**, and should not be presented as a question at all.

## 3. The finding Chat would act on first, and it is not on the specimen page

**108 declarations set no weight at all.** That is nearly half the type on the site inheriting whatever it lands in.

This is more consequential than any size decision, and it is invisible on a specimen page because inherited type still renders as something. A page can look entirely correct and have no weight decision behind half of it.

**So: decide what each weight means on this site, then set it explicitly everywhere it applies.** Your census already shows the shape of the answer, with 600 carrying 97 declarations across 59 class families and clearly doing the heading and label work, and 400 carrying the reading.

Once each weight has a stated meaning, an unstated weight becomes a defect a gate can find, rather than a thing nobody can see.

## 4. Tokens, and why they are the point rather than the polish

**Three type values on this entire site are written through a custom property, and all three belong to one component.** Everything else is a literal number typed into a rule.

Without tokens the register is a document somebody has to remember. With them it is a constraint. That is the difference between tidying once and staying tidy, and it is the only part of this work that survives the next person who adds a page in a hurry.

**So once the surviving set is agreed, each survivor becomes a named token, and a literal type value in a rule becomes the thing that fails.** You already named this as what a mechanical check would need.

The naming should carry the role rather than the number, because a token called by its size is a literal with extra steps and goes stale the moment the value moves.

## 5. Two more standards worth setting in the same pass

**Responsive is a gap in both the register and the code, not a drift between them.** You framed that correctly. 28 of 32 sizes are identical on a phone and a desktop, and the register only states responsive behaviour for four styles. So nobody has been wrong; nobody has decided. That is a design question for Kain, and the specimen page's three columns are what make it answerable at a glance.

**Line height belongs to a role, not an element.** Tight for display type, loose for reading. Eighteen distinct line-height values exist because it has been set per element by whoever was building that element. Deciding it by role is what stops the eighteen coming back.

## 6. One thing to fold in while this pass is open

**The section header supporting line measures 3.19 against white, site wide, below the accessibility bar of 4.5.**

Found at Session 268 by Chat's own self-critique rather than by Kain's eye, on every section header on the site. It has no home yet and it is not on the census. **It is a text standard problem and this is the pass that should carry it**, rather than waiting for its own turn and being fixed in isolation later.

Not commissioned here. Named so it is not solved twice or forgotten once.

## 7. What this does not touch

**Nothing here overrides a value Kain has already approved by eye.** Where a size, weight or colour was ruled on a render, it stands until he rules again on a render, and a standardisation pass is not a licence to quietly bring it into line with a scale.

The two recorded exceptions in the block heading standard are the precedent: his specific wording stood, and the general standard did not silently overwrite it.

*No em or en dashes in this file; checked before writing.*
