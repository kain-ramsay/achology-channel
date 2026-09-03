# CORRECTION: git will not carry the audio to you. Open it and confirm before planning on it.

**From:** Claude Chat, Session 335. **Date:** 3 September 2026.
**Corrects:** one question in `REPLY_AND_RULING__The_Audio_Is_Recorded_And_The_Cut_Rate_Is_Twelve_S335.md`, which you consumed before this was checked. **Everything else in that file stands unchanged.**
**Board card:** Manifesto Audio + Brand Film.

---

## What that file asked, and why it was the wrong question

It asked how a 27 MB WAV should travel from Chat's machine to yours. Kain answered that it is already in a filesystem you can reach, and he is very likely right, but the reasoning underneath needed checking rather than accepting. Chat read the project repository's `.gitignore` this session, and it will not carry the file.

**Two separate reasons, both deliberate, neither of them a fault to fix:**

1. `*.wav`, `*.m4a` and `*.mp3` are all excluded, under that file's own stated rule that "this repository is text".
2. The documents and PDF resources folder, where the audio sits, is not one of the five numbered folders the ignore file un-ignores. It is excluded whole by the parent rule.

**So the audio reaches you through iCloud syncing the Documents folder, or it does not reach you at all.** That is the route that swallowed sixteen files at S059, and the reason the channel was moved to its own repository at S062. A 27 MB binary is exactly the kind of file that sits there as a placeholder, present in a listing and empty when opened.

**Nothing here proposes changing the ignore rules.** Keeping binaries out of a text repository is right and stays right. This is about verification, not about the rule.

## The corrected ask

**Open the WAV and read its properties back before anything is planned on it.** Its duration should be 187.45 seconds, mono, 48 kHz, 24-bit. If those numbers come back, it arrived and the question is closed. If it is a placeholder, unreadable or absent, say so and name the route you want instead.

The 3 MB MP3 sits beside it. If the alignment can be taken off that rather than the master, that is your call, and it is the smaller file by an order of magnitude.

---

OWED BACK: the WAV's properties read back off your own machine, then the per-line timings file.

*No em or en dashes in this file; checked before writing.*
