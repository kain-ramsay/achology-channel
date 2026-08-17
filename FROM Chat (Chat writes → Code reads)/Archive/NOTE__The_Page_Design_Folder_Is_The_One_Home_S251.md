# NOTE: the page design folder is now the one home for every page's prototype and brief

**From:** Claude Chat, S251. **Date:** 2026-08-06.
**Read once, then work to it permanently.** This changes where you look for briefs.

## The short version

Every page on Achology.com now has its own folder, and everything about that page lives in it: the prototype Kain approved by eye, the developer brief written from it, its artwork, and its superseded versions in an `Archive` subfolder.

```
000. www.achology.com | All Website Assets/02. Page + Components (HTML Design Files)/
  000__HOW_THIS_FOLDER_WORKS.md
  Knowledge Hub Design Prototypes/
    Book Note Page/
      Book_Note_Page_S250_FINAL.html
      BRIEF__Book_Note_Page_Template_S251.md
```

Read `000__HOW_THIS_FOLDER_WORKS.md` at that path. It carries the rule, the folder-per-page shape, and all 35 folders mapped one to one against PRD §5.1 rows Pr1.1 to Pr1.35.

## What changes for you

1. **Briefs are not in the channel any more.** FROM Chat carries a pointer file naming a brief's exact path. Read the brief at that path.
2. **Never copy a brief or a prototype anywhere.** One home, never mirrored, exactly as the DSRDs work. A file held in two places is two copies of one truth, and the first edit to either makes them drift while both still look right.
3. **The prototype is the authority.** Where a brief and its prototype disagree, the prototype is correct and the brief is the thing to fix. Tell me; do not choose.
4. **Everything you produce about a page goes in that page's folder,** not to the project root and not beside the theme.

## Why

Two failures this week, both the same shape. S250 approved six versions of the Book Note page and named the final one in its handover; S251 opened, searched the whole project folder, and could not find it, because it had never been saved anywhere. And a folder restructure the same day broke three path references written an hour earlier, because those paths were scattered rather than pointed at one place.

Kain's structure fixes both: one folder per page, saved in the turn a design is approved, referenced by one path everybody uses.

## What is already in place

- All 35 page folders exist, created from the PRD's own list.
- `Book Note Page/` holds its approved prototype and its brief.
- DSRD 2 §1.6 and DSRD 9 §32 both point at that folder.
- The `page-design-brief` skill carries the pattern as its Step 6, so neither of us has to remember it.

Several pages already live on the build site were approved before this folder existed: the About family, the Policies family, Our People, the instructor profiles. Their folders are empty on purpose. If one of them is reconciled or redesigned, its prototype and brief land in its folder like any other page's.

*No em or en dashes in this file; checked before writing.*
