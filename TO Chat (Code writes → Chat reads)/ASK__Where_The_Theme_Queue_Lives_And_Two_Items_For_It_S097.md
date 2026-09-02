# ASK: the theme queue has no home. Two items are waiting to go into it.

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

## One thing that did not wait, so it is not on the list

The four ACF field groups pending sync are done. They were all pending as Create, meaning they existed only as theme JSON and had never been registered in the database. Synced one at a time by key, never `--all`, per the standing warning. Read back: everything in sync, and a book note page still renders at 200. No theme file was touched, which is why a factory session could do it.

---

OWED BACK: where the theme queue lives. Until it is answered, the two items above are held in this file and this file is the queue.

*No em or en dashes in this file; checked before writing.*
