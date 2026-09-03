> **CHAT DISPOSITION, S337: DONE, your OWED BACK line closed.** (Parked at S325 and unmoved since.) Your ruling's decision section is now DSRD 8 section 13.8, carrying both decisions, what would change the second one, the census finding, and the S053 self-link guard, which no design document held until today. DSRD 7 section 4.4 gains its named users, and the Policies index cards are named there with it. The "strongest duplication case" claim is corrected in `000__THE_FOUR_CHROME_COMPONENTS.md` and in `COMPONENT_REGISTRY.md`, both of which now carry the mention-versus-copy finding in plain words. **The census itself is not yet taught the difference; that is a change to `component_census.py` and it is yours, not Chat's.** It is named in the S337 handover rather than left inside an archived file.

# RULING: the Where next panel holds as built, and the duplication case does not exist

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Authority:** Kain, in session, in Safari, on four whole rendered pages.
**Closes:** sitting 3 of the four chrome sittings, `COMMISSION__The_Four_Chrome_Components_Are_Safari_Sittings_S282` and `BRIEF__The_Four_Chrome_Sittings_Are_Unparked_S302`.
**Filed under:** Harness Rule 14.

---

## What he was shown, and what he said

Four whole pages in Safari, live, at desktop: **About, the Manifesto, Reviews and Member Testimonials.** Not a component on a blank page, and no reconstruction.

He was asked the one question the commission allows: **does the panel hold as it is?**

**Yes.**

---

## The second question, and the answer is no

The commission and the component registry both name this as **the strongest duplication case in the whole component census**: `.policy-next` declared across four separate stylesheets, 38 rules.

**It is not duplication and there is nothing to collapse.** All four files were read this session rather than counted:

| File | What is actually in it |
|---|---|
| `components.css` | **the component**, declared once: margin, padding, background, radius, and every row and card rule beneath it |
| `help.css` | **two named variants**, both ruled by Kain on 2026-07-16: `--bubble` outdents the panel and paints the Achology bubble behind it at 6 per cent; `--no-mark` keeps the outdent and drops the mark on the Manifesto, where the Aristotle watermark already occupies that corner |
| `about.css` | **one line**, `.pfq + .policy-next--pair { margin-top: 0; }`, a gap between two adjacent blocks on one page |
| `book-note.css` | **one line**, `.bn-page .policy-next { margin-top: 0; }`, the same kind of thing, added at S050 after `page_gate` caught 64px stacking on a hairline's 48 |

**Not one of the three redeclares a single property of the base component.** No background, no padding, no radius, no grid, no typography.

**Measured on the rendered pages, which is the evidence rather than the reading of the files.** The panel is identical on all four: 944 wide, left edge 248 at a 1440 viewport, background `rgb(243, 244, 244)`, padding 32px, radius 12px. The only value that differs is `margin-top`, and that is precisely the page-relationship line the two one-line files exist to set.

### The finding underneath it, and it is the second time this exact mistake has cost a sitting

**The census counted selector OCCURRENCES and reported them as declarations of the component.** That is the same fault that made the breadcrumb look like two components at S080, when it was one component with a misleading wrapper name. Both sittings were booked to have Kain rule on a duplication that was never there.

**A count of mentions is not a count of copies.** Worth carrying into the census itself, because it will do this again on the next component with variants.

**What would change the answer:** a second file declaring the panel's own appearance. None does today. If one appears, it is duplication and it collapses into `components.css`.

---

## Two things recorded that no document currently holds

**One. The outdent is the site's own mechanism, not this panel's.** The panel is 944 because it is the 880 reading column plus a 32px bleed each side, switching on at 1040 rather than 1024. That is DSRD 7 section 4.4. **Section 4.4 names no users**, and it now has two: this panel, and the Policies index cards, which Kain ruled onto it in the same sitting. Worth naming them there.

**Two. The self-link guard, added S053.** A panel on a page never offers that page as somewhere to go, matched on the request path rather than on `is_page()`. It is behaviour rather than appearance, so no design document holds it, and it is in the data file's gate block as a rendered check.

---

## What was filed on this side

The prototype, the data file with its gate block, and the folder README, all in the Where Next Panel folder inside the Component Design Prototypes folder.

**The gate block is worth one line to you**, because three of its five checks are rendered rather than property checks and each names why: the outdent is a relationship between the panel and its page's column; the bubble watermark is a `background-image` rule that passes a property check while the file 404s, which is the S089 lesson exactly; and the self-link guard is behaviour.

## Where the count sits now

Two of the four chrome components are signed as of this session, the breadcrumb and this panel. **The footer is the one that remains**, and the header was signed at S080.

OWED BACK: this ruling's decision section into DSRD 8 §13; DSRD 7 §4.4 gaining its two named users; the "strongest duplication case" line corrected in `000__THE_FOUR_CHROME_COMPONENTS.md` and in the component registry; and the census taught the difference between a mention and a copy.

*No em or en dashes in this file; checked before writing.*
