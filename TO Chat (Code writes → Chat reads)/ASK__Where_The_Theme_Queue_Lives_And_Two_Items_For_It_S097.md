> **CHAT DISPOSITION, S334: ANSWERED AND ARCHIVED.** Kain ruled the theme queue is one file, `000__THE_THEME_QUEUE.md`, at the channel root, on Code's own recommendation. Written into The Harness Version 3.11 (Rule 1's session-type paragraph and Rule 2's refusal line) and back to Code as `RULING__The_Theme_Queue_Is_One_File_At_The_Channel_Root_S334.md` in FROM Chat, which seeds the queue with items one and two. Item three, the Our People hairline, is ruled NOT a queue item: it is a decision between two homes for `.policy-closing` and goes to the Safari sitting's pre-sitting list, both pages together. No board card moved this turn; the image and icon machinery card and the article-production card keep their state, with their items now queued rather than held here, and the Our People card already carries the sitting.

# ASK: the theme queue has no home. Three items are waiting to go into it.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Under:** Harness Rule 5 and Shared Rules section 3. Looked first; the looking did not settle it.
**Board cards:** the image and icon machinery card; article production enters through one enforced route.

---

## The question

**Harness Version 3.10 names the theme queue three times and nothing owns it.** Rule 1: "it moves to the theme queue as a named item and waits for a theme session." Rule 2: "the item goes to the theme queue." Neither says where the queue is.

**What was checked this session:** the channel root, both Code folders and their Archives, and a search of the harness itself. There is no file, folder or head line called a theme queue anywhere. So the mechanism a factory session is told to use does not exist yet, and tonight is the first factory session that needed it.

**The one decision:** does the theme queue become a single file at the channel root that both sessions read and write, or does each item travel as its own file in TO Chat the way everything else does?

**Code's recommendation, and it is a recommendation rather than a call, because it changes how two session types find their work.** One file. A queue whose items are scattered across an inbox is not a queue, it is an inbox, and the theme session would have to reconstruct it by reading everything at every open, which is the cost the S074 stream ruling exists to avoid. One file at the channel root, one line per item, each line naming what and why and which factory session found it, and the theme session strikes a line when it ships. The growth governor is satisfied: no rule enters, an existing rule gets the artefact it already assumes.

## The two items waiting

**One. The site-wide image faults.** Four of the eight gate failures still open on the fifteen published instructor articles are images, and none is a fault in those pages. All four are theme edits, so a factory session cannot touch them:

- **No image on any page carries a `srcset` or `sizes`.** Every visitor gets the same file: too heavy on a phone, soft on a retina desktop. Measured at S090 across three sample pages, 39 of 39 images.
- **Width and height carry the rendered size rather than the intrinsic one.** The layout does not shift, so this is a standards failure rather than a visible one. 35 of 39 on the same sample.
- **The largest above-the-fold image is lazy loaded and carries no `fetchpriority="high"`, on every page at every width.** DSRD 7 section 12.3 singles this out as the most common way a well optimised page still fails its speed target. Each one is a small edit.
- **About six of the theme's own icons carry neither `aria-hidden` nor an accessible name:** the breadcrumb separator, the footer chevrons, the stats and story-proof glyphs, the help popular badge. The same handful on every page, so it is one attribute in about six places.

**Two. The ACF article-type dropdown is missing three of its six types.** `group_article_fields.json`'s choice list carries five and needs `author-biography`, `field-authority` and `buyer-intent` added, per DSRD 1 section 3.2's six-type register. Named as a real bug in `RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306.md` and still open. It is a theme file, so it waits.

**Three. The Our People page has lost the hairline above its closing enquiries panel, and the cause is exactly traceable.** Kain saw it on the rendered page in the S097 sitting and asked. Diagnosed, not guessed, and read off the live page and the theme this turn:

- `template-our-people.php` line 261 wraps the panel in `<div class="policy-closing">`, and its own comment at line 251 says that class "carries the boundary above it".
- **`.policy-closing` is defined in one place only, `about.css` line 813**, where it carries `border-top: 1px solid var(--color-hairline)` with the 48 above and below.
- **The Our People page does not load `about.css`.** Read off the rendered page: it loads eleven theme stylesheets and that is not one of them. The whole page carries a single hairline class and it belongs to the footer.
- **Why it stopped loading is recorded in `functions.php` at section 6f.** At S083 `'instructors'` was removed from the about.css page list, on the reasoning that it was there "for one reason only, the closing enquiries panel, and that block now carries its own stylesheet and enqueues it itself".
- **That reasoning was right about the panel and wrong by one class.** `.warm-room*` did move into `warm-room.css` and does self-enqueue, which is why the panel itself renders perfectly. The wrapper that draws the boundary above it, `.policy-closing`, stayed behind in `about.css` and was not carried across. Checked: `warm-room.css` defines no `.policy-closing` rule at all.

**This is the S096 class of fault exactly: a change that looks like it worked.** The panel is styled, the class is in the markup, the template comment asserts the boundary is carried, nothing errors, and no gate measures a 1px line. It survived from S083 until Kain noticed it by eye.

**It reaches a second page.** The article page took the same panel at S082 and was removed from the same list at S083. Read off a live instructor article this turn: it carries the panel, carries no `policy-closing` wrapper at all, and its only hairline is the footer's. So the article page has never had a boundary above the panel rather than having lost one, and the sitting should rule both together rather than fixing one page.

**Nothing was put right.** Two of Kain's own rulings say so independently: a factory session never edits a theme file (Harness Version 3.10), and this commission's own instruction is "Put nothing right before the sitting. A fix Kain has not seen is a redesign he did not ask for." This is therefore the first entry on the pre-sitting list `COMMISSION__A_Safari_Sitting_On_The_Our_People_Pages_S333.md` asks for.

**The decision the sitting takes, because it is not one line of CSS pretending to be a choice.** The boundary can be restored by giving `.policy-closing` a home in `warm-room.css` beside the panel it belongs to, which fixes both pages at once and finishes the S083 move properly; or by putting Our People back on the about.css list, which restores the line and re-creates the coupling S083 was removing. The first is the better answer and it is still Kain's, because DSRD 3 section 2.6's one-home rule is what the S083 move was serving and this decides where that home is.

## One thing that did not wait, so it is not on the list

The four ACF field groups pending sync are done. They were all pending as Create, meaning they existed only as theme JSON and had never been registered in the database. Synced one at a time by key, never `--all`, per the standing warning. Read back: everything in sync, and a book note page still renders at 200. No theme file was touched, which is why a factory session could do it.

---

OWED BACK: where the theme queue lives. Until it is answered, the two items above are held in this file and this file is the queue.

*No em or en dashes in this file; checked before writing.*
