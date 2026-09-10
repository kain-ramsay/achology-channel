# RULING_AND_BRIEF: the audio pipeline converts digits to spoken words before any body is recorded. Build the step; the page keeps its numbers

**DOCUMENT TYPE:** ruling and brief, from Claude Chat, Session 356. **Date:** Thursday 10 September 2026.
**Authority:** Kain, live in the S356 sitting.
**Board card:** none of its own; it is a fixed step in the voice-audio-pipeline run-book, carried in the S356 handover until your line lands.
**Read this cold.**

---

## The ruling

Kain found that the voice engine on the RunPod recipe does not speak digits reliably ("28" and the like). He considered a copy rule that every number is written out in words on every help answer and quote page, and ruled against it: prices, years, times and reference numbers want digits on a page, for the reader and for search.

**So the fix lives in the pipeline, not in the copy.** Before any body goes to the voice, a step converts digits to spoken words under fixed rules. The page keeps its numbers. The page rule itself is written into The Achology Base Voice (vault, item 12): one to nine in words, ten and above in digits, always digits for money, years, times, percentages and reference numbers.

## What to build

One pre-processing step in the voice-audio-pipeline run-book, run on every body before generation, with these rules:

- Cardinal numbers read as words: 28 becomes twenty-eight; 1,250 becomes one thousand two hundred and fifty (British form, "and" included).
- Years read as years: 2017 becomes twenty seventeen; 2026 becomes twenty twenty-six.
- Money read as money: $34.50 becomes thirty-four dollars fifty; $7 becomes seven dollars; $2,995 becomes two thousand nine hundred and ninety-five dollars.
- Percentages read out: 52.5% becomes fifty-two point five per cent.
- Ordinals read as ordinals: 1st, 2nd, 21st.
- Reference and ID numbers read digit by digit: UK Provider Number 10099815 becomes one zero zero nine nine eight one five. A number of seven or more digits with no separators is treated as an ID.
- Times read as times: 7pm becomes seven p m; 09:00 becomes nine o'clock or nine a m as the house prefers; say which you chose.
- Number ranges: 60 to 70 becomes sixty to seventy; a hyphenated range is read the same way.
- Everything else untouched.

A well-used library covers most of this (num2words, with the British flag), and the rest is a short rule set on top. Print, on every run, the count of numbers converted and the first three conversions, so a wrong reading is caught on the quality check rather than on the live page.

## What comes back

One line in TO Chat when the step is in the run-book and has run once on a real body, with the three printed conversions. If any rule above is impossible in the engine's own front end, say which and what the engine does instead.

OWED BACK: that one line. Nothing else.

*No em or en dashes in this file; checked before writing.*
