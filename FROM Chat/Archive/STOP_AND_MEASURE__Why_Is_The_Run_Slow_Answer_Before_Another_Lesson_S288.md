# STOP AND MEASURE: the run is too slow. Before another lesson goes up, tell us why.

**DOCUMENT TYPE:** priority instruction, from Claude Chat, Session 288. **Date:** 19 August 2026.
**Raised by:** Kain, in session, mid-run: the upgrade is not going meaningfully faster than Karen doing it by hand, and at that rate it takes weeks nobody has.
**This supersedes the low priority marking on `QUESTION__Can_The_Masters_Be_Made_Smaller_Without_A_Student_Seeing_It_S288`.** That question is now the live one.

---

## Stop pushing lessons. Measure first.

**Finish or abandon whatever lesson is in flight, then stop.** Do not continue through course 028 until this is answered. A run measured in weeks is not a run we can accept, and optimising it without measuring it first is how weeks become months.

**Nothing done so far is lost.** Prior versions are retained, and the descriptions already written stay written.

## Why Chat thinks the answer may not be file size, so you test the right thing

**The library is 2.767 TB across 2,146 lessons. That averages 1.29 GB a lesson.** For a lecture of twenty to forty minutes, that is roughly a delivery grade file already, not a ProRes or high bitrate editing master. **So the re-encode idea may win 30 or 40 per cent rather than the 90 per cent that would actually change the picture.** Test it, but do not assume it is the answer.

**The number that decides everything is the achieved upload speed.** At 20 Mbps the library takes about 13 days of continuous uploading. At 100 Mbps it takes about two and a half. Same files, same code. Nobody has measured which of those we are living in.

## The six things to measure, and nothing else. Minutes, not hours.

**One. Achieved upload throughput.** Not the advertised line speed. What you actually got, in megabits per second, pushing real lessons into Vimeo just now. Measured, not estimated.

**Two. Wall clock time per lesson, broken into its parts.** How long reading the file from Drive through rclone, how long uploading to Vimeo, how long waiting on Vimeo to process, how long everything else. **The part that dominates is the only part worth fixing.**

**Three. Whether you are running one lesson at a time.** If the uploads are serial, say so plainly. **Running six or eight concurrently is the single largest lever available if the pipe is not already saturated**, and it costs nothing but a change in how the loop is written. If the pipe is already saturated at one, say that too, because then concurrency buys nothing and the answer is compression.

**Four. Whether the bytes are moving twice.** Does rclone pull the file to local disk before the upload starts, or does it stream? If it lands first, that is disk write plus disk read added to every lesson, and it may be removable.

**Five. Whether Vimeo processing blocks you.** After the bytes arrive, does your code wait for Vimeo to finish transcoding before starting the next lesson? If so, that wait is dead time that concurrency removes entirely.

**Six. The encode facts, from ten files across several courses and years.** Container, video codec, bitrate, resolution, frame rate, audio codec, audio bitrate, size, duration. **Then compute the bitrate against the resolution.** That tells us in one line whether there is real fat to cut or whether these are already lean.

## Then one test, only if the numbers justify it

If and only if the encode facts show real excess bitrate: take one lecture that is not queued for the run, re-encode it to a sensible delivery setting, and report the size before and after plus an honest look at the two side by side at full screen. **If you can see a difference, say so and the idea dies.** Kain would rather keep large files than ship softer video to paying students.

## What to send back

**One short report. The six numbers, then your own verdict in one line: what is actually slow, and the single change that fixes most of it.**

Do not send options for Kain to choose between without a recommendation. You are the one holding the measurements; the recommendation is yours to make and his to overturn.

## The context you may not have

**Vimeo On Demand stops accepting new uploads on 22 August 2026 and closes fully on 20 November 2026**, per the facts on the board card. If any part of the course library sits on On Demand rather than a standard plan, that is three days away and it changes everything about this run's urgency. **Check which it is and say so in the same report**, because if it applies we are not optimising a slow job, we are racing a door closing.

*No em or en dashes in this file; checked before writing.*
