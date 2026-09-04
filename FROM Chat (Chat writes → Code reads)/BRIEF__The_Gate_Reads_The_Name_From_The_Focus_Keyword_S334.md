> **CODE DISPOSITION, S099: DONE.** `content_gate.py` now carries a `fill_name` helper reading `rm_focus_keyword`, committed as `4fb4758`. All five of your acceptance cases run in both directions: Egan's three heading failures gone and its other three untouched; Kain Ramsay unchanged, which is the case proving it is not loosening; a wrong focus keyword still fails all four heading lines; the book note type unchanged; `content_gate_standards.json` not edited. **The count you asked for: 50 records, not 2.** The folder holds 52 real records plus 8 Cowork batch reports, 50 of the 52 carry the question-shaped title, and after the change 51 of 52 pass every heading check. The one that does not is `_scratch_peterson`, a working file with no page-fields block. `content_gate_acceptance.py` still passes 78 of 78. **The scope wall that refused this three times is fixed in the same session**, and this change set's own declaration carried `{name}` deliberately as its live fire. Printouts in `REPLY__Three_Of_Your_Measurements_Do_Not_Hold_S099.md` and the commit message.
>
> *The S097 line, kept because it recorded the block correctly and its diagnosis is the thing that was wrong:*
> **CODE DISPOSITION, S097: WAITS ON one fact a machine can test, that `content_gate.py` contains a `fill_name` helper reading `rm_focus_keyword`.** Read in full at H6's block, twice, since it changed mid-session. **The count you asked for is done and neither of your two figures was right: 50 of the 51 author-biography records carry a question in `post_title`.** Only `Author_Biography_Kain_Ramsay_S298.md` holds the bare name. So the fault reached 50 records, and the correction in section 26 over-narrowed it to two; the original "all 51" was nearer the truth than its own correction. The fix is written and was refused by Code's own scope wall, three times, on a correctly formed declaration naming the file: **H2 is reading a stale declaration, one behind the current one.** That is reported as a third harness fault in `ASK__The_Scope_Wall_Reads_A_Stale_Declaration_S097.md` rather than worked around by re-declaring until it lets me through, because gaming a safety wall is worse than being stopped by one. Everything else is ready: the helper, its reasoning and the four acceptance cases.

# BRIEF: the gate takes {name} from the focus keyword, not from the page title. It fails every author biography whose title is a question.

**From:** Claude Chat, Session 334. **Date:** 3 September 2026. **For:** a factory session. No theme file is touched.
**Approved by Kain at S334**, on the finding and the fix below, put to him as one yes or no.
**Board card:** the search and citation layer; it also unblocks the 51 biographies on the article-production route.

---

## The finding, measured rather than reported

`content_gate.py` substitutes `{name}` in the `author-biography` heading map from the record's `post_title`. The rule that put `{name}` there is Kain's S304 ruling, and it is right. The source it reads is wrong.

Every author biography's `post_title` is a question, by the type's own title standard: *Who is Gerard Egan? His Biography, Ideas and Life Works*. So the gate looks for a heading called *Who is Gerard Egan? His Biography, Ideas and Life Works: Life and Formation*, finds *Gerard Egan: Life and Formation*, and reports it as an unexpected section.

**Measured this session against the live standards file, on the real Egan record:**

```
  FAIL  section headings, verbatim and in order        found 5
  FAIL  unexpected section                             Gerard Egan: Life and Formation
  FAIL  unexpected section                             Gerard Egan's Body of Work
  FAIL  unexpected section                             Gerard Egan's Influence and Legacy
```

Three failures on every biography whose `post_title` is a question. The two headings that carry no name pass, which is what points at the cause.

**CORRECTED THE SAME SESSION, before this file was sent, and the correction is the useful part.** Chat first wrote that all 51 fail. They do not. `Author_Biography_Kain_Ramsay_S298.md` carries `post_title | Kain Ramsay`, so the substitution lands correctly and every heading line passes; it is his `rm_seo_title` that carries the question. Egan's record carries the question in `post_title` itself. So the fault hits every record whose `post_title` is not the bare name, and Chat has measured exactly two records rather than 51. **Count it before you fix it:** the number of `author-biography` records whose `post_title` is not the bare person's name is one command off the folder, and it belongs in your reply. The fix below is right either way, because it stops the check depending on which shape a title happens to take.

## The fix

**Read `{name}` from `rm_focus_keyword` instead of from `post_title`.** On this type that field is the person's name and nothing else, by definition: Egan's is `Gerard Egan`. It is a required field on the type, so it is always there, and it needs no new field and no edit to any record.

Where `rm_focus_keyword` is empty, fall back to `post_title` exactly as now, so nothing that passes today starts failing.

## Acceptance, red before green

1. On the real Egan record: the three heading lines FAIL before the change and PASS after it, with the rest of the printout unchanged.
2. On the real Kain Ramsay record, which passes today: it still passes after the change. That is the case that proves the fix is not simply loosening the check.
3. A fixture whose `rm_focus_keyword` does not match its headings still FAILS, so the check cannot go green on everything.
4. A type with no `{name}` in its heading map (the book note) is unaffected: run it before and after and show the same result.
5. The change is in `content_gate.py` only. `content_gate_standards.json` is not edited: its `{name}` placeholders are correct and stay as they are.

## One thing to know before you run it

The Egan record still fails four other lines and they are not this fault: `demand_evidence` missing, the description one character over 155, keyword density at 0.73 against the 1.0 floor, and the stage 0 evidence line. Those are the retro pass's, and they are true of the biographies generally. Do not fix them here.

**Also, so it is not a surprise in your diff:** Chat edited that record this session, adding eight inbound-link sentences into its body under Kain's ruling. The gate was run before and after and the failure count did not move.

---

OWED BACK: the acceptance printout, both directions, and the count of records whose `post_title` is not the bare name.

*No em or en dashes in this file; checked before writing.*
