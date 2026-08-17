# ANSWER THESE FIVE. Code is stopped until you do.

**From:** Claude Code · **27 July 2026, 21:40** · **Read this one first.**

Five questions. One line each is enough. Nothing else is needed from you, and
nothing moves until they land. Everything else in this folder is a report, a
reply or a delivery: this is the only file that needs you.

---

**1. Does `page_gate` come before or after the nine policy records?**

You ruled it after page 1 and before page 2. Your later ruling then turned
page 1 into nine records. **`page_gate` is now built and its first policy-page
printout is filed**, so the only live question is whether the nine records wait
for a full map of every built page first.

→ **BEFORE** (run it across every page, file one map, Kain picks the order by
what it shows) or **AFTER** (file the nine records first, attach printouts to
them afterwards)?

---

**2. Is the breadcrumb-to-header junction a block boundary?**

On `/policies/refund-policy/` there is no hairline between the breadcrumb and
the page header. The 48px spacing is correct at all three widths; the line is
absent.

DSRD 9 §26 calls the breadcrumb "the first content row", which reads as the
page's opening rather than a block. If that is right, no line is wanted and
`page_gate` must stop counting the breadcrumb as a block. If it is wrong, nine
policy pages need a line added.

→ **BOUNDARY** (add the line to all nine) or **NOT A BOUNDARY** (change the
checker)?

---

**3. How strict is the boundary-padding check?**

DSRD 7 §4.3: "a block that adds its own padding at a boundary is a defect". I
can measure padding and read which element declares it. I cannot mechanically
judge "owner" where a boundary falls between two DSRD 8 components that each
legitimately carry internal spacing under the carve-out.

→ Fail on **ANY** padding at a boundary, or only on padding declared **OUTSIDE**
a DSRD 8 component?

---

**4. Do the 53 CSS gate findings fold into the walk, or are they a sweep?**

`css_gate.py` still fails on 8 files, 53 findings, unchanged from your S223 run.
Working them in one pass means editing eight stylesheets at once, which your own
standing instruction calls unreviewable and forbids.

→ **FOLD IN** (each file's findings are fixed when the walk reaches the page
that owns it) or **SWEEP** (authorised as one separate pass, now)?

---

**5. Does the collapse brief run now, or behind the walk?**

`BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md` is accepted and
not started. It is the only commissioned item that touches no page a visitor
sees, so it is the safest thing to run while the walk waits on question 1.

→ **NOW** (take it first, while the walk is blocked) or **AFTER THE WALK**?

---

## One thing that is not a question, so it does not get lost

**No page on the site declares a canonical address.** I checked the Trust
Statement, About and Our People as well as the policy pages: none carries one,
and Rank Math holds no canonical setting at all. DSRD 6 §3.3 requires it on
every page.

This is **one Rank Math configuration change, not twenty page defects.** I have
deliberately kept it out of the walk so it does not get "fixed" nine times over.
It belongs in the Rank Math runbook already filed here. No answer needed; I am
telling you so it is on your file.

## And one thing coming at you next session

Kain has set the next session to open on **Rank Math scores in bulk**: all 249
Help articles scored without him opening a single one, plus the theme-built
pages whose editor is empty by design and which therefore score 4/100 while
being finished and live. That is mine to solve, not yours. Flagging it because
it will change what the walk's metadata chapters can assert.
