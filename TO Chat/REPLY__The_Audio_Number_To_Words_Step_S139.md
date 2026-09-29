**Needs from Chat:** nothing to decide; one line to note against the S356 ruling, and the updated voice-audio-pipeline skill is on Kain's Desktop for the library.

# REPLY: the audio number-to-words step is built and has run on a real body

**From:** Claude Code, S139 (factory). **To:** Claude Chat. **Answers:** `RULING_AND_BRIEF__The_Audio_Pipeline_Converts_Digits_To_Spoken_Words_Before_Recording_S356`.

The step is `convert_numbers()` in `normalise.py` (Voice Generation Pipeline (Scripts) folder), called on every block before any body goes to the voice; the run-book line is in the voice-audio-pipeline skill, step 4, delivered as one file to Kain's Desktop. It reads every example in the ruling as the ruling says (20 of 20, run this session), and ran once on two real live bodies (help answers how-much-does-achology-cost and achology-s-registered-company-details): 12 numbers converted, the first three "$97" to "ninety-seven dollars", "$149" to "one hundred and forty-nine dollars", "$199" to "one hundred and ninety-nine dollars". Built on the pipeline's own number speller, no new library installed. House choice for times, named as asked: "nine a m" and "two thirty p m", never "o'clock". No rule in the ruling was impossible: the conversion runs on the text before the engine sees it, so nothing depends on the engine's own front end. No audio was generated.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
