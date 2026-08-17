# STOP: the tag order is authored, and WordPress throws it away

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `RULING__Course_Selection_Lead_Tag_Plus_Slug_Correction_S253.md`, the
closing paragraph of §5.
**Status: waiting on ruling.** Nothing has been built. `achology_course_companions()`
is untouched and still carries the school stand-in.

## The short version

You asked me to say so and stop if the master's tag order was arbitrary or
alphabetical. **It is neither. The order is genuinely authored, and §5.7 is
sound.** The problem is one layer down: the order does not survive the trip into
WordPress, so a renderer reading "the first tag" reads the wrong one.

## 1. The master's order is authored, and your worked example is right

620 rows in `Book_Note_Upload.csv`, every row carrying two or more tags.

| Test | Result |
|---|---|
| Tag order exactly alphabetical | 84 of 620, 13.5%, which is roughly chance |
| Tag order exactly reverse alphabetical | 119 of 620 |
| Distinct tags appearing first | 28 |

The distribution of first tags reads like editorial judgement, not a sort:
understand-your-mind leads 170 rows, find-purpose-and-direction 76,
build-confidence 56, and a long tail below.

`mans-search-for-meaning` in the master reads
`find-purpose-and-direction, build-mental-resilience, understand-your-mind`.
That is your worked example exactly, lead tag included.

## 2. And WordPress reorders them alphabetically on the way in

The one imported book note, id 10901, the same book. Read back from the live
database:

```
term_relationships.term_order   0   Understand Your Mind
term_relationships.term_order   0   Find Purpose & Direction
term_relationships.term_order   0   Build Mental Resilience

wp_get_object_terms( 10901, 'kh_tag' ):
   build-mental-resilience
   find-purpose-and-direction
   understand-your-mind
```

`term_order` is 0 on every row, so nothing recorded the authored position, and
the default read comes back sorted by name.

**So on your own worked example the rule would pick `build-mental-resilience`
as the lead tag, not `find-purpose-and-direction`.** Different courses, on a
page that would look entirely convincing. This is the failure mode already on
the record from S050: a result that cannot be seen to be wrong is worse than
one that breaks.

Estimated blast radius: the lead tag survives by luck only where the authored
first tag happens to sort first, which is the 13.5% above. Roughly six rows in
seven would show the wrong courses.

## 3. What I propose to do about it, which is a technical matter

Standing rule: technical decisions are mine, so I am not asking you to choose a
mechanism, only to write the one I have chosen into the import specification.

**The authored lead tag is carried into a field of its own at import.** The CSV
already holds it; the import writes the first non content attribute tag of each
row into a `lead_tag` post meta field, and the renderer reads that. The tag list
itself is unchanged, so tag pages, filtering and everything else in §5 carry on
exactly as written.

Rejected, and why, so it is not re-derived:

- **Relying on `term_order`.** It is the field built for this, but nothing sets
  it, WP All Import does not populate it by default, and a value nothing
  maintains rots silently. It would also have to be right on all 620 rows
  before a single page could be trusted.
- **Re-deriving the lead tag from the tag names.** There is no rule that would
  recover it. The order is editorial.

Cost: one column mapping in the import, and no change to the master, since the
column it reads is the one already there.

## 4. Two smaller things found in the same pass

**`primary_recommended_course` is empty on all 620 rows.** The column exists in
the master and carries nothing. It reads like an earlier mechanism that §5.7
now supersedes. Flagging it rather than acting: if it is dead it should come out
of the master before import, and that is production's call, not mine.

**Nothing needs back-filling.** Only book note 10901 is in the database and it
is already on the list to delete at import, so the fix lands with the real
import rather than needing a repair pass.

## What I need

Confirm the `lead_tag` field goes into the import specification, and I build
§5.7 against it. If you would rather Kain ruled on the mechanism, say so and it
waits; I have not touched the course block either way.

*No em or en dashes in this file; checked before writing.*
