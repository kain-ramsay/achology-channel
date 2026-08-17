# RECORD: the field is retired, the Amazon field is named, and there is a second course field

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `RULING__primary_recommended_course_Is_Retired_S255.md`, both items.

## 1. The retirement is done, and the page did not move

Out of the ACF field group entirely, not merely left unread: the group now
carries 14 fields and `primary_recommended_course` is not among them. Out of
`single-book_note.php` too, along with the three docblock passages that
explained a dependency which no longer exists.

**Verified the way your ruling asked.** You said: "Nothing renders from it
today, so nothing should change on any page: if something does change, that is
a finding worth a note back rather than a fix."

```
rendered book note, before and after: 0 changed lines
```

Byte for byte identical. Nothing to report as a finding on that count.

**One slip of mine, said rather than hidden.** My first deploy put the field
group's JSON at the theme root instead of inside `acf-json/`. Nothing read it
there and no page changed, but a stray copy of a field group beside the real
one is exactly the second-copy problem we spent today removing. Spotted on the
next check, deleted from the server, redeployed to the right path, both
checksums confirmed against local afterwards. The theme root now holds no
`.json` file at all.

Commit `84c36a8`.

## 2. Your question: the Amazon field is `amazon_url`

Read from the field group itself, not inferred from a template's usage.

**`amazon_url`** is the live field. Label "Amazon URL", type `url`, and its own
instructions already say what DSRD 2 §5.1 says: "The plain Amazon product URL,
amazon.com/dp/{ISBN10}, with no affiliate tag: OneLink applies the tag and the
visitor's own store." It is the one the template reads, at
`single-book_note.php` line 59.

**`amazon_genius_link_url` still exists in the field group**, and this is the
part worth your attention: **no template refers to it, by that name or any
other.** It is already self-documenting as dead, its instructions reading
"RETIRED, do not fill. The Geni.us plan was retired at S231 and the site now
uses Amazon OneLink, so there are no per-book links."

So DSRD 3 §2.3 should name `amazon_url`. And the retired field is in exactly
the state `primary_recommended_course` was in an hour ago: present, unread,
labelled retired, waiting for someone to notice. **Say the word and it goes the
same way, in one edit, with the same byte-identical proof.** I have not touched
it, because it was not what you ruled on.

## 3. The finding: there is a second hand-picked course field, and it is the live one

Your ruling's reasoning was that DSRD 1 §5.7 fills the cards from tags, so "no
course is hand-picked for a book note", and that two mechanisms for one outcome
is the drift the source-of-truth rule exists to stop.

**That reasoning applies to `recommended_course` as well, and that is the field
actually doing the work.**

| Field | Type | Populated? | Renders? |
|---|---|---|---|
| `primary_recommended_course` | post_object | **never**, 0 of 620 | no. Now retired |
| `recommended_course` | text | **all 620 rows**, from `prod_recommended_course_name` | **yes.** It is the hero's recommended course today |

The field you retired was the dead one. The live one is still there, still
editorially chosen, still a course picked by hand for a book note.

**I have not retired it, deliberately.** You named one field, and retiring the
other would change what renders in the hero on every book note, which is a
visible change on a page Kain approved. That is his eye, and a decision rather
than a tidy-up.

**The question it raises, which is yours:** does §5.7 replace the hero's
recommended course too, or is the hero's course a deliberate editorial choice
that survives while only the cards below it come from tags? DSRD 2 §3.1's fifth
body section, as you have just rewritten it, says card one is "derived from the
row's tags at draft time rather than chosen", which reads as though the answer
is yes and `recommended_course` should follow. But the hero is not card one,
and I would rather ask than infer my way into changing 620 pages.

*No em or en dashes in this file; checked before writing.*
