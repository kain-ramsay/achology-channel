# REPORT: the Playwright frame grab is proven. The hunt is blocked on one thing, and the storyboard never named it.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** step 2 of `BRIEF__The_Twelve_Beats_Are_Approved_Hunt_The_Footage_S335.md`, as far as it can be answered.
**Board card:** Manifesto Audio + Brand Film.

---

## The frame grab is a fact now, not a route

I named it as unproven and you respected the caveat, so here is the proof rather than a claim. Chromium loaded a real 1920x1080 H.264 MP4 from disk, seeked to four points and screenshotted the video element at each. **Four of four came back as real frames**, checked by counting distinct colours rather than by the file existing, because a silent decode failure produces a perfectly valid black rectangle.

**So the contact sheet needs no ffmpeg at all.** Chromium decodes H.264 itself.

**It took three attempts and the first two failures were mine.** The page had no file origin, and then I waited for a load event that had already fired, so it hung and looked exactly like Chromium refusing a local file. It was not: `readyState` was 4 the whole time. Named because both looked like external blockers and neither was.

## ffmpeg: your ordering was right and the shortcut is not real

Playwright ships its own ffmpeg and it looked like the install could come off the plan. **It cannot.** That build is configured `--disable-everything` with only mjpeg and vp8 enabled: no H.264, no AAC, no MP4 muxing. It exists to record test videos and nothing else.

**So step 4 still needs a real ffmpeg**, exactly as you scheduled it, and it still sits behind footage somebody has chosen.

## The blocker: nothing in the storyboard says where footage comes from

Thirty five search terms across the twelve beats, and no source named. That is the one gap in an otherwise complete brief, and it matters more than it sounds, because **Achology takes card payments, so the licence has to permit commercial use.** That is a money question, not a technical one.

**Checked before asking for anything:** no stock account or key exists on this machine. The only keys here are Search Console, SearchWP and Vimeo.

**Coverr answers without a key and was tested properly rather than assumed.** It returns real records carrying a 1920 wide still, which is all a contact sheet needs. But run against the storyboard's own terms it returns **zero hits on all four tested**: its search will not take phrases of that length and its library is small and lifestyle-skewed. The three results it did give for a shortened query included "Students talking and smiling", which is close to the forbidden library the direction rules out. **So Coverr is not viable for this brief.**

**Pexels is the right source** and needs a free API key. Its licence permits commercial use with no attribution, and its documentary-style library is the one this direction actually needs. Only Kain can create the account, so it is with him.

## What is done and what waits

**Done:** the timings, the transcript, the manifesto as text, and the frame grab proved.

**Waits on the key:** fetch candidates on the thirty five terms, pull a still from each, lay them out as one contact sheet with filenames underneath, and put it in front of Kain to tick twelve.

**Waits on the tick:** the ffmpeg install and the assembly, unchanged.

## One thing worth deciding while the key is being made

**How many candidates per beat.** Thirty five terms at, say, six candidates each is 210 stills, which is a contact sheet nobody can read. My recommendation is **six per beat, seventy two in total, one sheet per beat rather than one enormous grid**, so Kain judges twelve small sets rather than one wall. Not done on my own judgement because how he wants to look at it is his call, and it is the difference between a decision he can make in ten minutes and one he abandons.

---

OWED BACK: the contact sheet, once there is a source to hunt in.

*No em or en dashes in this file; checked before writing.*
