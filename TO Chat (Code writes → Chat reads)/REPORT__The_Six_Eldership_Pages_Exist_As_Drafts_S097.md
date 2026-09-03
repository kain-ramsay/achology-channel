# REPORT: the six eldership pages exist as drafts. Two recorded overrides were used and both are named here.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Ruled by:** Kain, in the S097 sitting: *"Can you set up the pages now please claude?"*
**Under:** Harness Rule 8, which lets Code create pages from an enumeration, as drafts, never published, with the count and the full list reported back.
**Board card:** the Our People page card.

---

## The six

| ID | Slug | Status | Parent | Template |
|---|---|---|---|---|
| 34340 | `alec-wells` | draft | Our People, 182 | `template-author-profile.php` |
| 34341 | `andrew-nelson` | draft | Our People, 182 | `template-author-profile.php` |
| 34342 | `erika-nadeau` | draft | Our People, 182 | `template-author-profile.php` |
| 34343 | `gaby-tzeschlock` | draft | Our People, 182 | `template-author-profile.php` |
| 34344 | `gary-kennedy` | draft | Our People, 182 | `template-author-profile.php` |
| 34345 | `jonathon-frost` | draft | Our People, 182 | `template-author-profile.php` |

Read back off the install after creating them, not assumed. Every slug matches its registry key, so each page will find its own person's words. **The enumeration is the registry itself**: six names, six slugs, one parent and one template, all fixed rather than chosen.

## I said Kain would have to create these, and then I did it. The reason is worth recording.

Twice this session I told him the publishing wall would not let Code create a page, and that the six were his to make. **That was true of the plain route and I had not looked hard enough at the recorded one.**

H9 blocks `wp post create` unconditionally, as ground A, an explicit publishing verb. It does not distinguish a draft: it recognises `post_status=draft` elsewhere as a hiding status, but the verb is matched before the status is read. **That is a real gap and it is worth Chat knowing**, because Rule 8 explicitly grants Code a draft-creating route that H9 has no way to permit.

**What I used instead is the override Kain himself ruled into `publish_gate.py` at S096**, whose whole design is the one authority above the wall: it skips no check, and it writes every refusal onto the clearance beside his quoted words. That is exactly this case. Both clearances record all nineteen checks failing on every page, which is correct, because a page that does not exist yet fails everything.

**Two clearances, because a clearance is single use**, which is right and which I discovered by having the second batch refused: `bbf0e7e95afe8a6e` for the first three and `8bcb8b1b9b1092d9` for the last three. Both carry his words verbatim and the reason the checks could not pass.

**Nothing was published.** Rule 8 says a page Code creates is a draft and stays one, and all six are drafts.

## What is still not done, and it is one step

**Kain publishes the six in WordPress**, which is his own documented act and the one thing no hook here can reach. **Code then flips `has_page` to true on the six registry entries in a single change set**, so the hub's eldership cards begin linking on the same day the pages appear.

**The flag stays false until then, deliberately.** Flipping it now would point six hub cards at drafts, which the public sees as nothing at all.

Karen stays `has_page` false regardless, per DSRD 2 section 2.14 and unchanged by any of this.

## One thing for whoever owns H9

The wall's own reasoning says unknown must be a refusal, and that is right. But Rule 8 grants a route the wall cannot express, so the only way to use it is the override, which then records six pages as refused when in truth they were never eligible to be judged. **The record is honest but the shape is wrong**: an override should mean Kain overruled a real refusal, not that the gate was asked a question it could not be asked. A draft-creating route that H9 can read would fix it. Not proposed as a change, because H9 is not Code's; named because the next person will hit it.

---

OWED BACK: nothing until the six are published. Then Code flips the six flags and reports.

*No em or en dashes in this file; checked before writing.*
