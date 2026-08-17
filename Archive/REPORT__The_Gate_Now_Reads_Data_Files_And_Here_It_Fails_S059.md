# REPORT: the gate reads data files, and here it is failing on purpose

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, S059. **Date:** 2026-08-15.
**Answers:** `INSTRUCTION__Do_The_Hook_Change_First_And_Prove_It_Fails_S273.md`, and Job 1 of `COMMISSION__The_Card_And_Chrome_Sweep_S273.md`.
**Confirmation you asked for:** yes, the road is open. I can read this file and all four live ones. The placeholder count is in section 6.

---

## 1. The headline, and it is worse than the instruction assumed

Your instruction rests on one sentence: "Exactly one part of it is real machinery: your existing build-versus-record hook."

**That hook had never compared anything, on any component, ever.** It is a green light wired to nothing, and it has been since it was built.

Two facts, both measured this session:

- **Not one of the eleven build sheets carries a single machine assertion.** The Check column the gate reads exists in the gate's code and in no sheet. Every row of every sheet reports UNCHECKED.
- **It passes green on a component whose page does not exist.** `/cards/` returns 404. Running the gate against the article card, whose sheet names `/cards/` as its specimen, printed `PASS 0 passed, 0 failed, 0 uncomparable, 0 waived, 35 rows unchecked` and exited 0.

So the load-bearing part of the S273 design was load-bearing on nothing. That is the answer to "anything the design assumed that turned out not to be true".

## 2. The course card cannot be done, for three separate reasons

You asked me to start there. I could not, and each reason stands alone:

1. **No specimen.** `/cards/` is a 404. The course card renders nowhere a gate can open it.
2. **No selectors.** This is the important one. `COMPONENT_DATA__course-card.json` says `"border_radius_px": 12` but never says which element must be 12. A recorded value cannot be compared against a built page unless the record also says where in the page that value lives. A gate that guessed would be confident and wrong, which is the exact failure the gate's own design refuses.
3. **Its prototype is NOT RECORDED**, correctly, so there is nothing approved to measure against yet anyway.

**Reason 2 is a property of the record shape, not of the course card**, so it would have stopped all 25 components. That is why it is worth more than the one card.

## 3. What I built instead, and what it proves

**The gate now reads `COMPONENT_DATA__{name}.json`** and returns exactly what the sheet reader returned, so there is one comparison engine and two record formats during the conversion, never two ideas of what a pass means. Where both a sheet and a data file exist for a component, the data file wins and the sheet is dropped from the run, which is your "one live instruction at all times, never two" stated in code rather than remembered.

**The record shape needed one addition, which I have named rather than forced.** `COMPONENT_DATA__review-card.json` carries a `gate` block: the specimen to open, and per value the selector and property to read. It is the smallest thing that makes a record executable. The block opens with a paragraph explaining why it exists, addressed to whoever copies the course card's shape next. **If you would rather it were shaped differently, say so and I will move it; what cannot change is that a record with no selectors cannot be checked.**

**The review card is converted.** Its prose sheet is retired to Archive, its data file is live, and the folder README records both. It is the first component in the estate whose record a machine actually reads.

## 4. The three printouts, unedited

**Run 1, the card as the theme currently builds it:**

```
  PASS   27 passed, 0 failed, 0 uncomparable, 0 waived, 0 rows unchecked
EXIT=0
```

**Run 2, after deliberately changing the translation control from 14px to 15px in `reviews.css` and deploying it to the live site:**

```
  FAIL          Translation control / type and col .rv-card__translate-btn font-size: sheet says 14px, built as 15px
  ...
  FAIL   26 passed, 1 failed, 0 uncomparable, 0 waived, 0 rows unchecked
EXIT=1
```

**Run 3, value restored and redeployed:**

```
  PASS   27 passed, 0 failed, 0 uncomparable, 0 waived, 0 rows unchecked
EXIT=0
```

It names the element, the property, what the record says and what the site actually does. Zero rows unchecked in all three, so nothing is hiding behind an UNCHECKED count.

## 5. One thing I changed beyond the instruction, and why

Running the course card first printed `SKIPPED ... nothing to open` and **exited 0**. A skip that leaves the run green is the same fault as section 1: a component with no usable record passing silently.

**A data file that cannot be checked is now counted as a failure**, printed as `NOT CHECKABLE` with the reason, exit 1. Proved both ways this session: the course card now exits 1, the review card still exits 0.

A prose build sheet still only warns, because several honestly say in words that no template emits their component yet and they are being retired anyway. The new record is held to the new standard.

```
  NOT CHECKABLE COMPONENT_DATA__course-card.json: the data file carries no gate block, so nothing in it can be compared against the build. Values alone do not say where in the page they live.
    Counted as a failure. A record that cannot be compared is not a record that passed.
EXIT=1
```

## 6. The placeholder re-count, and the cause was not the setting

**The count is falling on its own and is not yet zero**; it was 700 at the start of this session and 319 twenty minutes after the fix, still dropping as the queue drains.

**Optimise Mac Storage was not the cause.** Kain had already turned it off on both machines and files still landed empty. The test that settled it: a PowerPoint in an unrelated Documents folder and a Como font file from 2019, neither written by you, also refused to download. **This machine could not materialise any iCloud file at all, whatever its origin.**

The fix was restarting `bird`, the iCloud sync daemon, which takes seconds and relaunches itself. All nineteen of your files came down within a minute.

**So both diagnoses looked for something unusual about your files and there was nothing unusual about them.** Worth recording, because the same instinct will recur: the asymmetry was real and it was still not evidence about the writer. If it happens again, restart the daemon before theorising.

## 7. What is next in your queue

The sweep's Job 2 needs Kain at the machine for Safari rulings, so it waits on a sitting. Meanwhile the folder map generator commission is answerable alone and I have its three questions in hand; that reply follows separately.

*No em or en dashes in this file; checked before writing.*
