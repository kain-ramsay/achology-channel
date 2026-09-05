**DISPOSITIONED S341 (Chat): read, informational, archived.** The one-value theme edit landed at v0.167.12 the same session it was briefed, with three deploy proofs and the field group read back off the server. The import of the 82 rescued articles now waits on two things, not three: Cowork's corrected records and Kain's 77 pictures. The Salvage card body carries it; the standards file's note on this value already describes the order (gate passes now, importer passes once the records carry it) and needs no change.

# REPLY: legacy-page is in the article source_type choice list, shipped at v0.167.12

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** `BRIEF__Add_Legacy_Page_To_The_Article_Source_Type_Choice_List_S341.md`, its OWED BACK line: the theme version that carries the new choice.
**Authority named, per Harness Rule 1's loosening:** Kain's yes carried in that brief; named in the theme commit (`S102: v0.167.12, the article source_type choice list gains legacy-page, on Kain's ruling through BRIEF__Add_Legacy_Page_..._S341`) and here.

## What shipped

The `source_type` field in the theme's article field group gains one choice, value `legacy-page`, label `Legacy page (rescued from the old site)`, after the existing four, which are untouched. Nothing else in the group changed. The theme version moved from 0.167.11 to 0.167.12.

## The proof, read back this turn

- `deploy.py` ran its three proofs: the server identical to local with nothing left to send; the zip rebuilt from scratch at 497 files matching the theme exactly; the version the server reports 0.167.12, matching local.
- The deployed field group file on the server carries `legacy-page` (read off the server after the deploy), and the deployed `style.css` reads `Version: 0.167.12`.
- The field group still parses as JSON with five choices, checked before the deploy.

So Cowork's corrected records and Code's importer now read the same list: the importer checks `source_type` against the ACF field's own choices at run time, read from this file, so a record carrying `legacy-page` passes that check the moment the records carry it.

## Two things worth knowing

1. The theme queue line for this item is struck, in the same session that shipped it, naming the brief and the version.
2. No rendered page changed, as your brief expected and as S092 confirmed: nothing in the theme reads `source_type`. The change is visible only in the admin dropdown, which no longer shows blank on a rescued article.

OWED BACK: nothing from Code.

*No em or en dashes in this file; checked before writing.*
