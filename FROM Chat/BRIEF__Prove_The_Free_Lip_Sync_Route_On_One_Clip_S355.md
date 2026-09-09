# BRIEF: prove the free lip-sync route on one clip, before anything is built

**From:** Claude Chat, Session 355. **Date:** Wednesday 9 September 2026.
**For:** Claude Code.
**Authority:** Kain, live in the S355 sitting. He ruled the video route free only, and ruled that the research happens before any build.
**Board card:** The Achology Video Family.
**Project folder:** 0011. The Achology Video Family. The options paper `OPTIONS__The_Avatar_Tool_S355.md` sits at its root and carries the reasoning behind everything below.
**Read this cold.**

---

## 1. This is a proof, not a build. Read that twice.

**You are being asked to run one clip through one model once, and report what came out.** You are not being asked to build a pipeline, write a tool, wire it into anything, or produce a finished video.

The reason: thirty seven videos depend on whether a real clip of Kain can convincingly be made to say new words. If it cannot, everything downstream is wasted, and finding that out costs an afternoon rather than a project.

**If you finish the proof and the answer is obvious, stop anyway.** The next step is Kain's.

## 2. What the finished thing will eventually be, so the proof makes sense

An explainer video for each of the twenty eight courses and seven schools. Kain speaking to camera, ninety seconds, from a script.

**Nothing about him is generated.** There are over a thousand hours of him talking to camera across all twenty eight courses, plus further non-curriculum courses, in the Vimeo exports. The plan is to take one real clip and change only the mouth to match new audio.

**His voice is already solved.** The voice-audio pipeline clones his voice and has run. That audio is the input, not a new voice clone.

## 3. The model

**LatentSync 1.6, ByteDance, Apache 2.0.** `github.com/bytedance/LatentSync`, weights on Hugging Face at `ByteDance/LatentSync-1.6`.

Read from the repository this session: it edits the mouth in an existing video to match new audio, using audio-conditioned latent diffusion. Version 1.6 was retrained on 512 by 512 video specifically to fix the blurry teeth and lips people reported in 1.5. Inference is documented at about 6.5 GB of VRAM for the standard route, with the 512 route reported around 18 GB. It generates a cropped face region rather than a full frame.

**The fallback, if installation proves awkward:** MuseTalk, Tencent, MIT licence, lighter at 8 to 12 GB of VRAM, but a 256 by 256 face region against LatentSync's 512. **Use it only if LatentSync will not run**, and say so plainly rather than switching quietly.

**Where to run it.** The RunPod setup the voice pipeline already uses. This is the same machine rented for a few more hours, not a new cost centre. Google Colab's free tier is the zero-cost alternative if RunPod is inconvenient.

## 4. What the proof is, exactly

1. **Pick one clip.** From the Vimeo exports, one where Kain is talking to camera, well lit, fairly still, with no cuts. Thirty seconds is plenty. **Name which clip you used, by course and lesson number**, so the result can be judged against its source.
2. **Take one piece of his cloned voice** saying something the clip does not say. Any text. It does not need to be a real script, because no script exists yet.
3. **Run it through LatentSync 1.6.**
4. **Return the output file**, alongside the original clip, so Kain can watch them one after the other.

## 5. What to report back

Short and factual. What ran, what it cost, what it produced.

- The clip used, by course and lesson.
- The model and version, and whether it was LatentSync or the fallback, with the reason if it was the fallback.
- Where it ran, and the actual money spent, to the penny.
- How long it took to install, and how long to render.
- **Your own honest read of the output.** Does the mouth look right, or does it look like a mouth that has been edited? You will see it before Kain does.
- Anything that would break at volume. Thirty seven videos is not one video, and problems that are trivial once are not trivial thirty seven times.

**Both video files come back through the channel** so Kain can watch them. That judgement is his, not yours and not Chat's.

## 6. What is not in scope

The typography over the video. That is a separate step in a free editor, DaVinci Resolve or Canva, and it is decided after this.

Any script. Cowork is drafting the first one now, and this proof deliberately does not wait for it.

Choosing the base clip for the real videos. With a thousand hours to choose from that is Kain's selection, made by watching, and it happens after the proof says the route works.

Building anything.

---

OWED BACK: the two video files and the short report. Nothing else.

*No em or en dashes in this file; checked before writing.*
