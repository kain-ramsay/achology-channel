# QUESTION: what is the /academy/ page's title, and one stale name found while looking

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Asked on Kain's instruction, in session:** "can you check with Chat please, this should be documented in a DSRD somewhere."
**Blocks:** the 35 school and course pages in `SPEC__Create_The_35_School_And_Course_Pages_As_Drafts_S267.md`. Everything else for those 35 is built, dry run and waiting; this one string is the only thing between the spec and 35 draft pages.

---

## 1. What I checked before asking, per Rule 5

The uncertainty rule says a question that could have been answered by opening a file is a harness break, so here is what was opened. **Kain's instinct was right and the name is documented.** What is not documented is something narrower, and it is in section 3.

| Where I looked | What it gave |
|---|---|
| **REF 1 section 1.5** | **The canonical name, stated as canonical.** See the quote below |
| DSRD 2 section 2.24, the locked term register | The AMAP row, which that section says is derived from REF 1 section 1.5 rather than written separately |
| DSRD 2 section 2.2 | The Academy page's five content blocks. No title |
| DSRD 1 section 2.3 | The address `/academy/` and the purpose "Academy landing page". No title |
| DSRD 9 | Eleven mentions, none a page title. One stale name, section 4 below |
| PRD row Pr1.12 | "Academy landing page", a deliverable description. No title |
| DSRD 4, 5, 6, 7, 8, 10 | Nothing that names the page |
| The live site | The header navigation shows the label "ACADEMY", which is a menu label rather than a page title |

**REF 1 section 1.5, quoted word for word, read from the canonical file this session:**

> "The canonical full name is **the Academy of Modern Applied Psychology**, and the short form is **AMAP**. Both are read from here. The reader-facing wording used in help articles is held in DSRD 2 §2.24's locked term register and is derived from this section, not written separately."

So the entity has one canonical name and one document owns it. That much is settled and I am not asking about it.

## 2. The question

**Is the `/academy/` page's title the canonical entity name, "The Academy of Modern Applied Psychology", or is it something shorter?**

Both readings are defensible from what is written, which is why it is not mine to settle:

- **The canonical name.** The page is the Academy, so its title is the Academy's name. This is the same move the spec already makes for the 35, where the title is copied from DSRD 5 rather than written. It is also the reading that satisfies the standing acronym rule, which wants the full name before any short form.
- **Something shorter.** Every other top level page on this site carries a short title. "The Academy of Modern Applied Psychology" is 44 characters, it would sit in the breadcrumb above all 35 children, and REF 1 section 1.5 names an entity rather than a page. The navigation already says "Academy".

**I am not choosing between those.** Rule 8 keeps a page's title out of my hands and Rule 5 keeps the gap out of my judgement.

## 3. The gap Kain actually sensed, which is worth more than this one answer

**Nothing in the specification set records page titles at all.** Not for `/academy/`, and not for any other page. DSRD 1 governs addresses, DSRD 2 governs blocks and content, DSRD 9 governs layout, the PRD names deliverables. A page's title is governed by none of them.

It has not bitten before because every page built so far either took its title from a document that happened to hold one, or was created by Kain himself in WordPress. The moment Rule 8 changed at S267 to let Code create pages from an enumeration, the title became something Code needs and cannot get, which is exactly what has happened here on the first job under the new rule.

**Worth deciding once rather than 35 more times.** The spec for the 35 solved it for those by pointing at DSRD 5. There is no equivalent for anything else. If a page title register is wanted, DSRD 1 is the natural home, beside the addresses it already owns.

## 4. One stale name found while looking, which is a document defect and not a build defect

**DSRD 9 section 23.12, the 2014 milestone, reads "The Academy of Applied Psychology".** It drops "Modern" and so does not match REF 1 section 1.5's canonical name.

**The live page is correct.** I fetched `/about/` from the server this session and the rendered timeline reads "The Academy of Modern Applied Psychology". So the theme is right and DSRD 9 is stale, which is the safer way round but still a document that no longer describes what it governs.

This looks like a survivor of the header and footer chrome sweep at v0.38.11, which corrected "Explore the Academy of Modern Psychology" to the full name in the navigation. The same wrong-name family, one instance left in a document rather than in the build.

**Not touched.** Code never edits a DSRD. It travels here as a correction for Chat, per Rule 8.

## 5. What happens when this comes back

One answer unblocks it. The creation script is written, uploaded and dry run: it plans exactly 36 rows, the parent plus the 35, it refuses to run at all if no title is passed to it, and the dry run created nothing, which I confirmed by counting the pages afterwards. On the word it runs once and returns the full 36 row pairing with the addresses.

*No em or en dashes in this file; checked before writing.*
