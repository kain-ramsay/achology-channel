> CHAT DISPOSITION, S357 (arrived during the close): STAYS. Waits on Chat's two rulings at S358: the first-publish deadlock in publish_gate.py (section 5: a preview-address route, or the override named as the honest first-publish route with the re-gate as the real check) and the stage 5 versus stage 2A cover order; plus a route for the five orphan attachments (section 6). Board card: Book notes backlog (seven more published, 72 on the install).

# RULING: Kain rules that the seven book notes blocking seven biography pages go up

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 113, factory session. **Date:** Sunday 13 September 2026.
**Given by Kain live in the S113 sitting**, after being shown what was blocking eight of the fifty one biography pages.
**Filed under Harness Rule 14.** Acted on in the same session, and the work is done.
**Owning documents for Chat to write it into:** The Publish Ready Pipeline (stage 2A and stage 5's third check), DSRD 8 section 20.2.

---

## 1. His words, verbatim

> "yes, put those 7 book notes up please"

Given in answer to this question, put to him after the seven were named: "May I put those seven book notes on the site, so the seven biographies unblock?"

## 2. What he was told before he ruled

That seven of the fifty one author biography pages carry an in-body link to an Achology book note; that each of those seven book notes was written, carries a full record marked `post_status: publish`, and had never been imported to the install; that the link therefore lands on a page that does not exist; and that the publishing wall refuses to touch a live page carrying a link that resolves to nothing, which is what held those seven pages back from taking his five new headings.

The seven book notes: Resilient, Shyness, The Beck Diet Solution, Identity: Youth and Crisis, Multiple Intelligences, The Origins of Intelligence in Children, and Yes! 50 Scientifically Proven Ways to Be Persuasive.

The seven biography pages: Rick Hanson, Philip Zimbardo, Judith Beck, Erik Erikson, Howard Gardner, Jean Piaget, Robert Cialdini.

## 3. What was done on it, in order, all in the same session

1. Stage 5's three import checks ran on the seven records. Checks 1 and 2 passed on all seven. Check 3 failed on all seven: the cover image each record names was on no attachment on the install.
2. The seven cover files were found on disk, in the Book Cover Images folder, under exactly the filenames the records name. They had never reached the server.
3. `book_note_import.py --write` wrote the seven bodies into the master and regenerated the upload sheet from it. The master held 681 before and holds 681 after: seven existing rows updated, seven bodies written, none added.
4. `book_note_import.py --push` created the seven as drafts and uploaded their seven covers through `book_covers.py`, which is the one home for that question.
5. `publish_gate.py --clear` refused all seven, with eighteen checks failed each. **Every one of those refusals is the 404 of a page that is still a draft.** The wall runs `page_gate` against the public address, and a draft has no public address, so a first publish of any page cannot be measured before it happens. This is a real deadlock in the tool and is named in section 5 below.
6. The clearance was minted under `--override`, carrying Kain's words above, which is the route the gate itself provides for exactly this and which records every refused check by name on the clearance rather than showing a pass that never happened. Clearance `840da796df9ea662`.
7. The seven were published. All seven addresses return 200. The Resilient cover was read back off the rendered page and its file loads, 203,372 bytes.
8. The seven biography pages were then cleared for update on their own merits, with no override: `a8736697f2f0d523`, seven of seven cleared, `links-resolve` now passing because the book notes exist.
9. The five headings were pushed onto those seven. Read back off the rendered pages: **50 of the 51 live biography pages now carry all five.**

## 4. The one page still not carrying them

`/learn/psychology/articles/jordan-b-peterson/`. The wall refuses it for a different reason: its rendered body carries no external link, which DSRD 6 section 5 item 11 move 6 requires. That is a record fault and goes back to the record, never onto the install. It is the only one of the fifty one still on the old wording.

## 5. Two things this exposed that are not Code's to decide

**A first publish cannot be measured, by construction.** `publish_gate.py --clear` measures the public page. A page being published for the first time has no public page. So the full gate that a first publish is supposed to hold can never actually be held, and the only route through is the override, which means every first publish on this site is an overridden one. The gate's own comments say a first publish holds the whole set; in practice it holds none of it. Chat should decide whether the wall gains a preview-address route, or whether the override is named as the honest first-publish route and the re-gate afterwards becomes the real check.

**Stage 5's third check and stage 2A disagree about who uploads a cover.** Stage 5 refuses a record whose named image is not already an attachment on the install. `book_covers.py` uploads the cover itself at import. So stage 5 will fail every new batch on check 3 until stage 2A has run, and stage 2A sits inside the import that stage 5 guards. The order as written cannot be satisfied.

## 6. One thing Code got wrong in the middle of it, recorded rather than tidied away

Before reading `book_covers.py`, Code uploaded the seven covers by hand with `wp media import`. Five of the seven came back with scrambled library names, and the correction was refused by H9, correctly. The importer then uploaded them properly through `book_covers.py`, which is what should have been used from the start. **Five orphan attachments remain in the media library under scrambled names** (post ids 36199, 36201, 36202, 36203, 36205). They are unreferenced. Code did not delete them because H9 refuses a delete without a clearance, and a clearance is minted from page addresses, which an attachment does not have. This is named here rather than left to be found: it is one short job under its own declared scope, and it needs a route for removing an orphan attachment that the wall will accept.

OWED BACK: Chat's ruling on section 5's two items, and a route for section 6's five orphans.

*No em or en dashes in this file; checked before writing.*
