# NOTE: the record shape is settled, and here is what changes for you

**From:** Claude Chat, Session 273. **Date:** 14 August 2026.
**Context:** Session 273 was the specification enforcement and record architecture session you were told about in NOTE__Where_Chat_Has_Got_To_And_Nothing_Commissioned_S272. It has settled, pending Kain's final sign-off on the whole document. Nothing here commissions work. The card and chrome sweep commission follows separately once he signs.

---

## The one principle

A specification is executable, or it is not a specification. Prose leaves the build path entirely.

## What replaces the build sheet

One data file per component, `COMPONENT_DATA__{name}.json`, in the component's own folder beside its approved prototype. It carries every value the component is made of, as data. Precedence is S257 with one word swapped: prototype wins, the data file must match the prototype, your code must match the data file.

**Your gate changes from build-versus-sheet to build-versus-data, per component, as each data file lands.** Until a component's data file exists, its old sheet governs. The moment the file lands, your gate reads it and the sheet is deleted. One live instruction per component at all times, never two.

## The worked example already exists

`Card System/course-card/COMPONENT_DATA__course-card.json`, written this session from DSRD 8 section 7. Read it before the sweep so you know the shape. Its prototype slot honestly prints NOT RECORDED because Kain reopened the course card at S272; the sweep produces that prototype.

## What this means for the sweep, when it is commissioned

Each of the 25 components ends its review with three artefacts in its folder in the prototypes repository: your exported approved prototype, its data file, and nothing else. The registry becomes your census plus the grouping into the 37 named components, regenerated rather than hand-written. Records are born in this shape as the sweep runs; nothing is written twice.

## Standing instructions unchanged

Write no build sheets (they are retired, absorbed into the data files). Do not start the sweep. You never read a DSRD; that constraint held through the whole design and every answer that would have required you to start was rejected on that ground.

*No em or en dashes in this file; checked before writing.*
