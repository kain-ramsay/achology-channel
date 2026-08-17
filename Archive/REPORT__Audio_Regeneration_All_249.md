# REPORT: all 249 help-article recordings regenerated from the current text, and live

**From:** Claude Code, S230. **Date:** 2026-07-29.
**Answers:** your S229 rulings, section 3 item 1: "The stale audio first. Agreed and urgent for exactly the reason you gave: it is the only place the live site currently tells visitors something untrue. Regenerate all 249 from the current text with the S226 pronunciation set."

Done and verified. Every article's recording now speaks the words on its page.

## The staleness, measured rather than assumed

Before generating anything I pulled the current published text of all 249 articles and hashed each one the way the pipeline does, then compared against the recordings' own manifest. **Not one article matched.** All 249 texts carry a modified date of 28 July; the recordings were 15 and 27 July. The manifest also turned out to hold only 200 entries, because the 49 imported articles were voiced in a separate run whose manifest was never merged. So the honest count was: 200 recordings of text that had since been rewritten, and 49 with no manifest record at all.

## What was generated

- **249 recordings, 11.1 hours of audio, 308MB**, plus a per-article timings file for the follow-along highlight, plus a merged manifest.
- Kain's locked calm read, unchanged: exaggeration 0.35, cfg_weight 0.3. The watermark stays on, so a synthetic version of his voice is still marked as synthetic.
- One rented GPU, three worker processes sharing it, about six hours, **$4.46 (roughly £3.50)**. The pod is terminated.

**The voice reference had to be rebuilt.** The trimmed reference WAV from July was gone from the disk, so it was rebuilt from Kain's original recording: same trim points, 50.7 seconds, mono, 48kHz, peak -2.9 dBFS, which matches the banked file's measurements exactly. Kain listened to a generated sample before the run and approved it in his own words: "That's that's pretty good. I'm happy to go with that."

## The pronunciation set, S226, now fully applied

Two rulings in that answer were not in the generator and are now:

1. **The gloss rule (section 2).** A glossed acronym is spoken as the gloss, then "or", then the acronym: "the Peer-Peer Applied Learning Sessions, or PALS". This fires on 218 bracketed acronyms across the corpus. Before this run the bracket was simply read as it stood.
2. **AMAP is said as a word**, "ay-map", per your section 1 table. The old code dropped the bracket entirely.

Everything else in the table was already in place: VALTS, PALS, CIPS, SoMAP and DiMAP as words, the spelled-out set left in capitals, membership roman numerals spoken as numbers, "Ackology" fed to the engine, and the Code of Character and Conduct never voiced as an acronym in any position.

**Three terms in the copy are not in the S226 set and were not guessed at:** the HOT Seat (17 articles), DMAP (1), ALTs (4). They are filed as `QUESTION__Three_Unruled_Spoken_Terms.md`, the run used the engine's plain reading, and a ruling regenerates only those articles for a few pence.

## The quality check

Every recording was transcribed back with Whisper and compared word for word against its article, using the corrected scoring from the July run: word-level comparison, autojunk off, brand spellings folded on both sides.

- **Median match 0.973 across all 249. Five articles scored below 0.90.**
- All five are the price articles. The recording says "ninety seven dollars"; the transcriber writes "$97". Re-scored with numbers set aside on both sides, those five land at 0.915, 0.947, 0.950, 0.962 and 0.972, which is the normal range.
- **Nothing needed hand-listening and nothing needed regenerating.**

That number artefact is the same one that faked a disaster in July. It is a property of the checker, not the audio.

## Delivery, verified on the live site

The 249 recordings and their timings replaced the old files in `wp-content/uploads/help-audio/` on achologytest.com. Verified after upload, not assumed:

- 249 MP3s and 249 timings files present, 308MB, sizes matching the local masters.
- The MP3 serves: HTTP 200, `audio/mpeg`, 1,143,405 bytes for the spot-checked file, byte-identical to the master.
- The timings file serves: HTTP 200.
- **The proof that the staleness is actually gone:** the first timed sentence of the spot-checked article reads "What does it mean to be an Achologist Adept?" and the live article's title is "What does it mean to be an Achologist Adept?". They agree, which is exactly what was untrue yesterday.
- The article page renders and references both new files.

The local master folder `Help Article Audio Master (249 MP3's)` holds the same set, with the superseded July recordings deleted rather than left beside them.

## One thing that follows from this for the register

The lesson from the July rewrite holds and is now proven twice: a bulk content change silently invalidates everything derived from that content. The recordings were the derived thing this time. The check that caught it is cheap and should be standing practice: hash the source, compare against the derived artefact's own manifest, and report the count before doing anything else.

*No em or en dashes in this file; checked before writing.*
