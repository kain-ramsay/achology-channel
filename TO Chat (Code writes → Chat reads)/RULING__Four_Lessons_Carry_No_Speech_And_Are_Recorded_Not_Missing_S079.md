# RULING: four lessons carry no speech, so the transcript bank is complete at 2,142

**DOCUMENT TYPE:** ruling, given by Kain in the S079 sitting. **Date:** 24 August 2026.
**Filed under harness Rule 14**, in the same session it was given.
**Board card:** the transcript pipeline.

---

## The ruling, in Kain's words

> "Claude, these videos have no voice in them"

Given unprompted, while the four were being investigated, on being shown their titles.

## What it settles

The transcription run of 23 August wrote 35 of the last 39 and failed 4, each with
"transcription produced no speech". **Those four are not a fault and nothing is owed on
them.** They are lessons about silence, and they contain silence.

| Lesson | Title | Length |
|---|---|---|
| 009-101 | The Lost Art of Silence (How Well can You Do It?) | 7m 19s |
| 010-097 | Silence: The Value Found in Absence of Sound | 5m 38s |
| 013-051 | The Most Powerful Communication Skill of Them All | 5m 38s |
| 018-113 | The Art and Power of S.I.L.E.N.C.E | not measured |

## It was tested before he was asked, and that is the part worth keeping

Four videos failing, all four about silence, is either the explanation or a coincidence
too neat to accept. **The failing component was the voice detector**, which discards
audio it judges not to be speech, and a lecture with long deliberate pauses is exactly
the shape that could trip it. So each was pulled again and transcribed with the
detector switched off, which removes the only thing that could have been throwing real
words away.

- **009-101**, 439 seconds: four cues, every one of them the single word "You".
- **010-097**, 338 seconds: one cue, reading "Music".

Those two tokens are what a transcriber emits over silence and over background music.
There was nothing being discarded.

**Kain's ruling then confirmed it from the other side.** The measurement agrees with
him; it did not decide it.

## THE NUMBERS, and they are now final

**Videos: 2,146 of 2,146.** Read fresh from Vimeo this session, every lesson key
cross-matched: zero missing, zero extra, zero duplicated.

**Descriptions: 2,146 of 2,146.** Every row re-read from Vimeo and compared character
for character against the sheets. Zero differ.

**Transcripts: 2,142 written, 4 lessons carry no speech, 2,146 accounted for.** All
2,142 have been through the glossary pass and carry a `.corrected.txt`.

The old habit of one number standing in for a different job is finished here too: the
bank is not "four short", it is complete, and the four have a reason on the record.

## Where it is written, so it cannot be re-derived from cold

**`000__LESSONS_WITH_NO_SPEECH.md`, in the transcript bank itself.** It names the four,
their measurements, how it was established, and the scope of the exemption.

**`transcribe_missing.py` reads that register** and skips what it names, so a future run
picks up nothing and reports nothing outstanding. Confirmed after the edit: "0 lessons
still have no transcript".

Without that read the four would have been owed forever. The work list is derived from
the bank, so a lesson with no file is a lesson still to do, and every future run would
have pulled all four again while every count read four short of a bank that was already
finished.

**The exemption is not general.** Any other lesson coming back with no speech is a
fault until it has been through the same two steps: the detector-off re-run, and Kain's
eye. Four rows are on that list and nothing joins them quietly.

## The glossary pass, in the same run, and the two founders are now in it

`correct_transcripts.py` ran over the whole bank: **2,142 scanned, 878 corrected, 2,221
changes**, of which 2,112 were safe substitutions and 109 were shown in context. The
verbatim `.vtt` and `.txt` are untouched, so the bank can still be compared back against
Vimeo and re-derived if the glossary grows again.

**The two NLP founders are in the glossary now**, and only after the corpus read that
`ANSWER__The_Master_Gets_A_Word_Count_Not_A_Path_S290` and the S078 report both said had
to come first. Across all 2,142 files: Bandler is spelled correctly 116 times and
Grinder 73, against **one occurrence of each wrong form**.

| Added | As | Why it is safe |
|---|---|---|
| `Richard Banderas` | `Richard Bandler` | shown in context. The surname alone would catch the actor; the two-word form cannot |
| `John Grinders` | `John Grinder's` | shown in context. "Grinders" alone would catch a sentence about coffee |
| `Grindler` | `Grinder` | safe outright. Not a word and not anybody's name. One occurrence, in 005-008 |

Both context rules fired exactly once each, on the sentences they were read in, and both
were verified in a dry run before anything was written. That is the same discipline that
left "Regan", "Reagan", "Corey", "Erickson" and "Kairen" alone, and it is the reason this
glossary can be trusted at all.

*No em or en dashes in this file; checked before writing.*
