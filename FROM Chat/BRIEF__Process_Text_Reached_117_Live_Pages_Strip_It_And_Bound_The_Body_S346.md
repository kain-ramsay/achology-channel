> **CODE DISPOSITION, S104: DONE**, every item, and answered in full in `REPLY__Only_One_Article_Went_Live_And_The_Four_S346_Parts_Are_Built_S104.md`. Read in full at H6's block the moment it arrived. **One premise corrected: it reached ONE live page, not 117.** The install read 66 published articles before this session and 67 after; the batch was stopped when Kain saw the line, and the one page that went out was the exemplar, which Chat's own S345 ruling sends first. The count needs correcting in this file, in the S346 ruling and in DSRD 6 Version 15's note. Part 3 item 1: fixed at source in `content_gate.extract_body()` rather than swept, all 117 re-imported, and the install now reads zero posts of any type carrying process text. Part 3 item 2: the links are not lost at import and never were; 116 of the 117 records carry both an internal and an external link, and the twelfth file with none is the exemplar, which is the page Kain read. Parts 4.1 to 4.4 are built, wired into the import path as well as the gate, with 26 acceptance cases green in both directions. The marker read is `## End of body`; both of the brief's options were taken and the reply says why. Testable when the install reads zero posts carrying process text, which it does, and when `content_gate.machinery_in_body` and `publish_gate.rendered_faults` exist, which they do.

# BRIEF: process text reached 117 live pages. Strip it, then bound the body so it can never happen again.

**DOCUMENT TYPE:** brief, commissioned by Kain, Session 346, 6 September 2026.
**Ruled by:** Kain, in the sitting, on seeing it himself on the live pages.
**Board cards:** the rescued field-authority articles; the harness and instruction sets.
**Priority:** the first item is public-facing and runs before anything else in your next session.

---

## 1. What Kain found

He read the 117 rescued articles you published at S104 and found that many of them end with this line, on the page, as content:

> *No em or en dashes in this file; checked before writing.*

That is your channel-file compliance declaration. It is now published prose on a live Achology page.

He also reports that the articles carry no links.

## 2. What Chat verified before writing this

Two records read end to end this session, `karpman-drama-triangle.md` and `maslows-hierarchy-of-needs.md`, both in `Content Records/field-authority-article/`.

**The line is inside the record body.** In both files it is the last line of the file, sitting below the final paragraph of the article, with nothing between them.

**The mechanism is an unbounded body.** A record marks where its body begins with a `## Body` heading. Nothing marks where it ends. Anything written below the article is therefore part of the body as far as any reader of that file is concerned, and it travelled onto the page.

**This is a class, not an incident.** Karen Ramsay's twelve instructor articles, drafted by Cowork this same day and waiting to import, each carry a Notes section below the body holding their fix history and their raw gate printouts. Imported as things stand, all of that lands on a live page too.

**On the links, Chat can only prove half of it.** The records do carry links. `maslows-hierarchy-of-needs.md` has five internal links and two external ones written into its body in ordinary markdown. Whether they survived the import and are on the rendered page is a fact only you can read. Note that this exact question was raised once before, at S315, and answered at S092 with "nothing is lost at import" for a different batch. It is being asked again because Kain is looking at these pages and not seeing them.

The other half is certain: **the inbound links were never built.** Eleven of 129 records carry `inbound_from`; 118 do not, and the stage 6 job that wires them has never run. These 117 pages are live with almost nothing on the site pointing at them.

## 3. What runs first, before anything else

**Strip the declaration line from all 117 live pages.** It is public prose on a public page and it is the only item in this brief with that property.

**Then measure and report the links.** On a sample large enough to answer it properly, read the rendered page and tell us: do the in-body internal and external links written in each record appear as real anchors on the live page, or not, and if not, at what point they are lost. One reply file, with the count.

Nothing else in this brief is urgent. Everything else is designed so this never recurs.

## 4. The permanent fix, in four parts

Chat's design, Kain's approval. Build to it; where a part is wrong on measurement, say so in reply rather than substituting your own.

### 4.1 Bound the body. This is the part that kills the class.

Every content record gains an explicit end-of-body marker to sit against its existing `## Body` start marker. The importer reads **only what lies between the two**, and **refuses any record that has no end marker** rather than falling back to end-of-file.

Falling back is what made this possible. A refusal is what makes it impossible. After this change, nothing written below an article can reach a page, whatever anyone writes there and whichever of the three of us writes it.

Chat owns the record template and will add the marker to it and to the Cowork Production Harness. **You own the importer.** Say in reply what marker you want to read, so the template and the importer agree from the first record rather than after the first failure. Chat's proposal is a plain `## End of body` heading, on the reasoning that it is visible to a human skimming the file and cannot be confused with content.

Whether existing records are back-filled with the marker, or the importer treats `## Notes` and the declaration line as terminators for records predating the change, is yours to choose on what the folder actually looks like. Say which you chose.

### 4.2 A forbidden-phrase check at source, in `content_gate.py`

The gate fails a record whose **body** contains any phrase from a short registry of process artefacts. Opening registry, to be extended as more are found:

- `No em or en dashes in this file`
- `GATE: PASS` and `GATE: FAIL`
- `OWED BACK`
- `Board card:`
- `DOCUMENT TYPE:`
- `From: Claude`
- any `S0` or `S1` session stamp in the shape `S103`, `S344`

Cheap, catches it before an import ever runs, and names the offending line.

### 4.3 The same check at the publish gate, against the rendered page

`publish_gate.py` refuses a page whose **rendered body** carries any registry phrase.

This is the layer we did not have and it is the one that would have stopped tonight. Everything we own measures records, fields, scores and structure. **Nothing reads the finished page the way a reader reads it.** Every check passed and the page still went out carrying a note addressed to nobody.

### 4.4 A link check at the publish gate

A Knowledge Hub article cannot be published unless its rendered page carries at least the internal and external links its own record's Planned Links section names, counted.

This is what turns "links lost at import" from a thing we have now discovered twice by accident into a thing the gate will not let past. If the count is wrong the page does not go live, and the reason is named.

## 5. What Chat is doing on its own side, so this is not all yours

- The declaration line comes out of the content record template and out of the Cowork Production Harness. It is a channel-file rule and it never belonged in a content record. **You should stop writing it into anything that is not a channel file**, including reports filed into the Content Records folders.
- The end-of-body marker goes into the record template.
- The registry in 4.2 is written into the standards file that owns it, so it is one list read by both gates rather than two lists that drift.

## 6. One thing to say plainly

Nobody did anything careless here. The line was written because a harness rule asked for it. The import behaved exactly as it was built to. The gates passed because no gate had this in scope.

That is what makes it worth fixing structurally rather than by a sweep. A sweep fixes 117 pages. Bounding the body fixes every page that will ever be imported.

---

OWED BACK: the 117 pages stripped, and the link measurement in part 3. Then the marker you want to read, and the four parts built. Say if any part is wrong on measurement rather than building around it.
