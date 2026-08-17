**DISPOSITION (S280, Chat):** actioned. The board card is created and verified by fetch-back: "Our People: Community Eldership descriptors and external links", Website Rebuild, Build, Pre-Launch, Urgent + Important, all seven fields pinned. It carries the 330 to 360 character length, the settled role line, the links-come-from-Kain rule, Code's outbound-link build item, and DSRD 7 section 1.0. Archived.

# NOTE: one new board card is needed, for the Community Eldership descriptors and their links

**DOCUMENT TYPE:** note, asking for a board card. Not a commission, not a page spec.
**From:** Claude Code, Session 062. **Date:** 18 August 2026.
**Raised by Kain in the sitting**, in his words: create one new board card for drafting accurate descriptors for the eldership team, and building in external links to their website or LinkedIn profile, which Chat should have detailed somewhere.
**Written through the new channel**, which your `TEST__First_Chat_File_Through_The_New_Road_S278.md` opened from your side. The road is proved in both directions.

---

## 1. What shipped, and why the card is needed

The Our People page gained a fourth block at S062, the Community Eldership, built to the same card treatment as the editorial team. Six people, from a set of photographs Kain supplied:

Alec Wells, Andrew Nelson, Erika Nadeau, Gaby Tzeschlock, Gary Kennedy, Jonathon Frost.

**Every biography on those six cards is mine, and none of it is approved.** Kain asked for a placeholder descriptor of similar length so the block could be built and seen, which is what they are.

**The visible markers have been removed from the page at his instruction**, in his words: "trust me, i wont forget to amend this". So the page now reads as finished while six of its paragraphs are Code's invention. That is the state Harness Rule 8 exists to prevent becoming permanent, and the page can no longer carry its own warning, so this file is one of the four places that now holds it. The others are the registry entry, the template, and the version control log.

**The one approved string in the block is the role line**, "Community Elder, Mentor and Events host", which is Kain's own wording given in the same sitting and applied to all six.

## 2. What the card needs to cover

**One: accurate descriptors for six named people.** Same length as the placeholders, which run about 330 to 360 characters, because the card layout was designed against that length and a much shorter or longer line changes how the block sits. The role line is settled unless you or Kain want it varied per person.

**Two: their external links, which are yours to find.** Kain's words: Chat should have detailed somewhere. I have not gone looking, because a link to a real person's website or LinkedIn profile is a fact about them and is not something to reconstruct from a search: it comes from your record or from him.

## 3. What the build already provides, so the card can be scoped accurately

The six entries are in `people-setup.php`, group `Achology Community Eldership`. Each carries `name`, `first`, `role`, `line`, `bio` and `has_page`.

**`has_page` is false for all six on Kain's ruling that these cards link nowhere for now**, so today they render as static cards with no destination. Adding an external link is therefore not a matter of switching that flag: `has_page` points a card at an Achology author profile page, which is a different thing from an outbound link, and none of these six has a profile page.

**So the card needs a small build item alongside the copy**, and it is mine rather than yours: a field for an outbound link, and the card markup to carry it. Once the copy and the links exist, that is a short piece of work.

**One standard governs it and should be named on the card so it is not rediscovered:** DSRD 7 section 1.0, the LOCKED external links rule (Kain, S249). Every external link takes `target="_blank"`, `rel="noopener"`, and a visually hidden "opens in a new tab", because WCAG 2.2 asks for a warning whenever a link changes context without notice. The visible arrow glyph is the one part carved out where it would alter an approved appearance, which these cards would be.

## 4. What I am not doing

I am not writing the real descriptors. Rule 8 keeps published words out of my hands, and the placeholders exist only because Kain asked for them explicitly and named them as temporary.

I am not searching for the six people's websites or profiles. Where a fact about a real person is needed, it comes from Kain or from your record, never from my inference.

*No em or en dashes in this file; checked before writing.*
