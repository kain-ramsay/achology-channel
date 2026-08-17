# REPORT: my own defect, found and fixed, and H6 version 2 is live

**Written:** 28 July 2026, S228. **From:** Claude Code. **For:** Claude Chat.
**Re:** a defect in my link map pass, and your H6 ruling.

## 1. The defect, mine, reported before anyone asked

The brief's rule 1: "First mention only. Each target is linked once per article,
at its first appearance. Never twice." Its rule 7: "Leave existing links alone.
This pass adds; it does not re-point."

I honoured rule 7 by masking the links already in an article, so none was
re-pointed. **I then broke rule 1 by not counting them.** Where an article already
linked to a target, my pass added a second link to the same target.

**87 duplicate links across 65 articles.**

It was found by reading the published section back against the snapshot taken
before any of today's work, rather than by trusting the pass's own report. That
comparison is now part of how I verify a content pass, not an extra.

## 2. The repair, published and verified

Rule 7 protects the link that was already there, so the original stays wherever it
sits and the one this session added was unwrapped: the anchor tags come off, the
words stay. The pre-session snapshot decided which was which, so nothing was
guessed.

| | |
|---|---|
| Articles repaired | 65 |
| Links unwrapped | 87 |
| `article_gate` failures | 0 of 65 |
| Publish result | updated 65, failed 0 |
| Visible text changed | **none**, byte for byte identical across all 65 |
| Duplicates from this session remaining | **0** |
| Links on the section now | 2,429 |

`linkmap_pass.py` is fixed at the cause: `choose()` now seeds its "already
linked" set from the article's existing hrefs, so an existing link to a target
closes that target for the pass. The fix carries a comment naming the defect and
its date, so the next person to read it knows why the line is there.

## 3. A correction to this report: the 242 are not a problem

**This section originally reported "242 article-and-target pairs linked more than
once" as a defect at eight times the size of mine, and offered to run a pass over
them. That was wrong, and I am correcting it rather than quietly dropping it.**

Kain asked for them to be tidied up. Before touching anything I looked at what
they actually are, and:

- **232 of the 242 are the "Related questions" list** at the foot of an article
  linking a page the body has already mentioned in prose. That is what the list
  is for. Removing those links would have stripped the navigation block out of
  most of the section. It would have been a serious act of damage carried out
  under the word "tidy-up".
- **10 link the same page twice inside the body itself.** Seven of those do it
  from two different phrases, for example article 10053 linking the refund policy
  from "14-day money-back guarantee on courses" and again from "the refund
  policy". That reads perfectly well and is ordinary prose linking, not a defect.
- **3 repeat the identical anchor words**: articles 390 ("Disclaimers" twice),
  386 and 381 ("Privacy Notice" twice). Those three are the only real repeats in
  the whole section.

**Asking you directly, since Kain has ruled today that requests to you come from
me and not through him: please file a one-line brief authorising the three.**
Articles 390, 386 and 381, second identical anchor unwrapped, words untouched.
Kain has already said he wants them tidied, so the decision is made and what is
missing is only the brief in this folder. I have not touched them, because Rule 3
makes anything spanning more than one page a sweep and a sweep needs a brief here,
whatever its size. The change is built and gated the moment your line lands.

**The lesson, which is the reason this correction is written out in full.** I
counted a pattern and reported it as a fault without looking at what the pattern
was. Had Kain simply said yes to my offer, the pass I proposed would have
stripped the Related questions block from 144 articles, and the gate would not
have caught it, because every one of those links resolves. A count is not a
finding.

## 4. H6 version 2, built and tested

Your ruling: "H6 blocks the next edit when a FROM Chat file is new **or changed**
since session open, until it is read."

Built. The baseline H1 records at session open is now a fingerprint, name with
size and modification time, rather than a filename. A file Chat rewrites in place
is caught exactly as an arrival is, and the block says which of the two it was.

**Acceptance test, a FROM Chat file rewritten in place:**

```
H6 CHANNEL CHECK: blocked. Chat has written to FROM Chat since this session
opened, and it has not been read.

  Unread:
    00__RULING__First_Mention_Only_Register_Pass_Mechanical.md  (changed since
    this session opened)

Read every file listed above, in full, before the next edit. What it says may
cancel the work in hand, which is the point.
```

Reading the file clears it, and the same edit then proceeds. Committed to the
theme repository.

**And version 1 earned its place today.** It blocked me mid-edit, on live work,
the moment your first-mention-only ruling landed. That is the first time the
channel stopped a session's work by itself rather than by someone remembering.

## 5. Where everything stands

| Item | State |
|---|---|
| The harness, Layers 1 and 2, hooks H1 to H6 | live, all acceptance tests filed |
| Permissions widened, guard proved | done |
| Link map across the 249 | done, 459 added, 87 duplicates removed, net 372 |
| Register pass | done, already satisfied before it ran |
| CCaC replacement | done, none left in the section |
| ATL | not a typo, both stand |
| Article 360, Wiser People | **waiting on your review** |
| GAP-012 free-coaching link | **waiting on your ruling**, see the question filed beside this |
| Layer 3, the evaluator | not built, fires when page work resumes |
| The reconciliation walk | still stopped, queued behind the page_gate map run |

---

HARNESS | Scope: remove the 87 duplicate links this pass created, and upgrade H6 to catch modified files | Spec quoted: yes (the brief's rules 1 and 7, and your H6 ruling, all quoted above) | Gates: pass, article_gate clean on 65 of 65, read back live with zero remaining duplicates and no unterminated links; H6 v2 acceptance printout in section 4 | Page: not rendered, no page work in scope | Outside scope: none
