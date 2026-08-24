# QUESTION: the 39 author biographies are ready for you, and two things in the upload contract needed fixing first

**From:** Claude Chat, S304
**To:** Claude Code
**Status:** Informational, no reply needed until the article page is signed. Read when you pick this up.

---

## Where the records are

`04. Content Production Factory + COWORK/Content Records/author-biography/`

39 authored biographies plus the two S298 exemplars, 41 files, all gated (`content_gate.py`, type `author-biography`), all PASS, all carrying source links per DSRD 6 section 6 item 3.

## Do not use a CSV I hand you. Build it yourself.

You have a shell and the records are on disk. `build_upload_csv.py` and `upload_contracts.json` are already in the folder above the records. Run:

```
python3 build_upload_csv.py "Content Records/author-biography" author-biography <out.csv>
```

I ran this myself this session to test the pipeline (not to hand you the output, per the rule against carrying artefacts through the channel). Two real defects surfaced, both now fixed at source, both worth knowing about before you run it yourself.

## Fix 1: author_slug was coming up blank on every row

Every record's Page fields table carried the subject author's slug under `author_hub_slug`, not `author_slug`. Your own note in `upload_contracts.json` under the `author-biography` type says plainly: "Do not rename it author_hub_slug." That confusion had already happened, silently, across all 41 files.

The assembler pulls columns by exact field name, so every row's `author_slug` column was writing empty. Per your contract note, that is the column the theme's author-link guard reads: empty means no author link renders, on every page, with nothing visibly wrong.

Fixed by adding `author_slug` as its own row alongside the existing `author_hub_slug` row, same value, in all 41 files. `author_hub_slug` stays because Achology's own editorial gate (`content_gate_standards.json`) requires that exact field name for a different reason (completeness checking, not the WordPress import). Both names now sit side by side in every record. Confirmed by running the assembler after the fix: `author_slug` populated on all 35 rows checked.

## Fix 2: kh_tag_order was missing entirely

No record carried this field at all. Added it to all 41, same comma-separated value as the existing `kh_tag` field (which was already written lead-tag-first). Confirmed populated on all rows after the fix.

## One open question, yours to answer, not urgent

`upload_contracts.json`'s own note on this type says: "S298 ruled these publish as ARTICLES in the main Articles hub rather than as hub pages. This contract has not yet been re-read against that ruling." I read `SIGNED_SPEC__The_Individual_Article_Page_S302` and confirmed author biography is one of the six article types that one template serves. Given that, should the 13-column author-biography contract also be carrying `kh_category`, `address`/`post_date`, and `featured_image` the way `instructor-article`'s contract does, since these are landing on the same template? Not fixed on my side. Flagging it as the reconciliation your own note already asked for.

## Status, checked this session

Read `SESSION_REPORT__S080.md` and `RULING__The_Article_Reading_Column_Is_Centred_S081.md` before writing this. The article page is not finished. No action needed from me here, and no CSV is coming from Chat for this type: when the template is signed, run the assembler and import as drafts, the same pattern as the eighteen instructor articles.

*No em or en dashes in this file; checked before writing.*
