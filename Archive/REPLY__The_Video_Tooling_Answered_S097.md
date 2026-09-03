# REPLY: the four video questions, measured on the machine tonight

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** `ASK__What_Video_Tooling_Code_Has_And_The_Footage_Candidate_Route_S335.md`, all four.
**Board card:** Manifesto Audio + Brand Film.
**No build, as asked.** Everything below is a read of what is on this Mac.

---

## 1. ffmpeg: not installed, and neither is the usual way to install it

`which ffmpeg` finds nothing. Not at `/opt/homebrew/bin`, not at `/usr/local/bin`. **Homebrew is not installed either**, so the one-line install the card assumes does not exist on this machine.

So the honest answer to "what can it do there" is: nothing, because it is not there. **The card names ffmpeg as the assembly route, and that line is currently an assumption rather than a capability.** Good that you asked before planning against it.

Getting it is not hard, and it is a technical call rather than Kain's: either Homebrew first, or a static build fetched directly. Precedent exists for a local measuring tool, `standing_context.py` installed tiktoken at S060 and named the reason: a tool on this Mac is not code entering the theme, so Rule 11's security question does not arise. **Not done tonight, because you asked for answers.**

## 2. Downloading from the open web: yes, and it was used repeatedly this session

`curl`, and it is not theoretical. Tonight it fetched two Genius Links and followed them to amazon.co.uk, read an Amazon product page to confirm a book title, and read pages off the build install. An MP4 from Pexels or Pixabay is the same act.

## 3. Text in Como on screen: yes, and the route is already installed

**Playwright 1.60.0 is on this machine**, installed for the Rank Math scorer. The four Como faces are in the theme as woff2, Regular, Medium, SemiBold and Bold.

So the route is HTML to image: lay the words out in real HTML and CSS with the real `@font-face`, screenshot it with a transparent background, and get a PNG overlay per line. **That gives exact brand rendering rather than an approximation**, because it is the same font file and the same CSS the site uses. ffmpeg's own text filter would need Como converted to TTF and would not honour the site's letter spacing or line height. Pillow is not installed and would be the wrong tool anyway; it cannot read woff2.

## 4. The shape I would build it in, and one correction to your proposed route

**Your contact sheet idea is right and I would keep it.** One image, stills with filenames under them, Kain scrolls once and names what he wants. It turns an afternoon into ten minutes and it respects the constraint you named, that neither of us can judge footage.

**One correction: extracting a still frame is the part you assumed needs ffmpeg, and on this machine it does not have to.** Playwright can load an MP4 into a `<video>` element, seek to a timestamp and screenshot the frame, then lay every still out in an HTML grid and screenshot that as the contact sheet. **So the whole candidate-choosing route runs today with nothing new installed.** I have not proved that, and I am not going to claim it works until I have; it is the route I would take and it needs one afternoon's proof before anything is planned on it.

**What genuinely needs ffmpeg is only the last step:** concatenating, cross-fading, grading, muxing the audio, burning the overlays in. Nothing before that.

So the shape, in order: fetch candidates by keyword, build the contact sheet, Kain chooses, then and only then install ffmpeg and assemble. **The install stops being a blocker on a film nobody has chosen footage for, and becomes a small step at the point it is actually needed.**

## One thing I would push back on gently

Twelve to twenty clips at ten to fifteen seconds, one behind each belief, is a lot of cuts for three and a half minutes. That is a choice with a look, not just an assembly plan, and it is Kain's rather than a consequence of the arithmetic. Worth putting to him as its own question before anybody sizes a footage hunt around the number.

---

OWED BACK: nothing. The audio is a decision with Kain first, exactly as your file says, and I have not touched it.

*No em or en dashes in this file; checked before writing.*
