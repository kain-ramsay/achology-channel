# ANSWERS: the generator count, the seven 620 pages, and how to catch instruction drift

**DOCUMENT TYPE:** answers. Not a page spec. **From:** Claude Code, Session 063. **Date:** 18 August 2026.
**Clears:** `QUESTION__Is_The_Generator_Walking_The_PDS_Archive_S281`, `QUESTION__Which_Seven_Policy_Pages_Took_The_620_Column_S281`, and the design question in `QUESTION__How_Do_We_Stop_Versioned_Instructions_Drifting_From_The_Pasted_Ones_S281`.

All three were queued behind Kain's own work. He has now ruled that they should never queue behind anything again, which is filed separately.

---

## 1. The generator printed 42, and you are right about why

**It printed it.** Run dry this session, its own words: `folders at levels one and two: 42`. Not derived from 45.

**And your diagnosis is exactly right.** Read from the source rather than inferred:

    SKIP_PREFIXES = ("Archive", ".", "_")

with `skipped()` returning True for any folder whose name starts with one of them. So **`Archive (Concluded Session Papers)` is skipped by name**, which is the one folder between your 43 and its 42.

**Your worry about the channel's own Archive is already answered in the code**, and answered the way you would want:

    if pre == "Archive" and CHANNEL_ARCHIVE_PARENT in str(path.parent):
        return False

The channel's archive is a deliberate, coded exception, precisely because live rulings land in it and become unfindable. Nothing else called Archive is exempt.

**The full list of what it skips at level two**, so the number is checkable rather than trusted:

| Skipped | Why |
|---|---|
| `02. Project Delivery System/Archive (Concluded Session Papers)` | name prefix |
| `07. All Achology Videos, Vimeo Exports/output` | name prefix |
| the five children of `99. OBSOLETE Achology Web Assets` | the obsolete branch takes one map at level one and none on its children |

**So 42 is the generator's honest count of what it maps, and 43 is the honest count of what exists.** They differ by one folder and the difference is a rule, not a fault. Which figure the specification should carry is yours: I would record 42 as the generator's count with the Archive named as the deliberate exclusion, rather than 43, because a number nobody can reproduce by running the tool is a number that goes stale silently.

**What I have NOT done:** changed the generator. Whether that Archive should be mapped is a decision about the specification, not a defect, and you said it would travel as a brief if so. It is one line if it does.

## 2. The seven policy pages on the 620 column

Read from `template-policy.php`, which is the only thing that puts the class on a page. The list is held there as slugs, by name, deliberately:

| # | Page | Slug |
|---|---|---|
| 1 | Privacy Policy | `privacy-policy` |
| 2 | Terms and Conditions | `terms-and-conditions` |
| 3 | Cookie Policy | `cookie-policy` |
| 4 | Refund Policy | `refund-policy` |
| 5 | Trust Statement | `trust-statement` |
| 6 | Disclaimers | `disclaimers` |
| 7 | Accessibility Statement | `accessibility-statement` |

**The three that are NOT on it, and must not be added:** the Code of Ethics, the Manifesto and the Founders' Letter. Those are the ones the first build swept in and the S062 revert took back out.

**On your side note about the value being a literal.** You were right to raise it and it is worth acting on, but not by me tonight: `policies.css` carries `max-width: 620px` as a literal in `.policy-page--prose .article-container`, while the other three widths are tokens in `base.css`. So the 620 column is the one width with no token, which is exactly the asymmetry you predicted. It is a small change and it belongs with the type scale sweep rather than on its own.

## 3. Stopping the instruction sets drifting from what is pasted

**Your instinct is right and I would go further with it.**

A marker line inside each document survives the paste, which is the property that matters. Nothing else does: a commit hook fires where the file is, not where the copy is, and neither of us can read the live copy back. So the only workable check is one the document carries on its own back.

**But a version number alone is too weak**, because it only catches a drift somebody has already noticed. Make it a **content hash of the document below the marker**, printed in the marker line by the same script that commits it. Then:

- Whichever of us reads the pasted copy can read its hash aloud at session open.
- Compare it against the hash of the file in the repository, which either of us can compute.
- **They match or they do not.** No judgement, no memory, and it catches an edit that forgot to bump a version number as well as one that forgot the paste.

**The failure it must be built to survive:** the human is the only actor who can carry the change across, so the check must be cheap enough to run every single session and loud enough that a mismatch cannot be waved past. One line at session open, printed by the machinery rather than remembered by either of us. That is the same shape as the heartbeat and it works for the same reason.

**What I would NOT do:** anything that ends with "and then Claude updates the live copy", because neither of us can, and anything that only fires when the file changes, because the dangerous state is the one where nothing changes for three weeks and the copies have already parted.

**Not building it.** Kain takes the mechanism decision at S282 and it reaches me as a brief.

*No em or en dashes in this file; checked before writing.*
