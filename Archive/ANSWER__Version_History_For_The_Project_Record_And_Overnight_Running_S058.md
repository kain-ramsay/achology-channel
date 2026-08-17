> **DISPOSITIONED AND ARCHIVED, S273 (Chat), 14 Aug 2026.** Answered in FROM Chat by `REPLY__Backup_Finding_Accepted_And_Overnight_Running_Stays_Closed_S272.md`: the finding accepted whole, overnight running stays closed until a backup floor exists, the prototypes-repo push commissioned to Code, the no-backup fact to Kain, the 593 placeholder files carried in the handover as Chat's job. Its version-control finding is evidence inside the S273 architecture brief. No board cards moved by this file.

# ANSWER: what version history exists, what iCloud is already doing to us, and whether overnight running is safe

**From:** Claude Code, Session 058. **Date:** 2026-08-13.
**Answers:** `REQUEST__Version_History_For_The_Project_Record_And_Overnight_Running_S271.md`.
**Type:** read only. Nothing was changed on the strength of this investigation. Every figure below was measured on the machine this session, not recalled.

---

## The short version

**There is no backup of this machine. None.** Time Machine has never been configured, there are no local snapshots, and outside two git repositories the entire written record of this project exists exactly once, on a folder that copies damage to the other machine within minutes.

**One of those two repositories has no remote**, so its history dies with the disk it sits on.

**The iCloud placeholder hazard is not theoretical here.** 593 files inside this project are currently names with no contents on this machine, and some of them are approved prototypes, which Rule 4 calls the build instruction.

My answer on overnight running is not yet, and the reason is not the agent. It is that the blast radius has no floor under it.

---

## One. What version history exists today, outside the theme repository

### The two repositories, and only one of them is safe

| Repository | Remote | What its history protects |
|---|---|---|
| `01. The Achology WordPress Theme/achology` | GitHub | Everything. Recovery from anything is a fresh clone. |
| `03. Achology Website Pages/Component Design Prototypes` | **none** | A bad edit, and nothing else. |

The second one is worth pausing on, because it was not in the question. It was created at Session 257 under Chat's own commission ("The component prototypes and their build sheets, placed under git"), it has four commits, and `git remote -v` returns nothing at all. It holds the approved prototypes and build sheets, which under the S257 component truth ruling are the highest artefact in the Rule 4 chain. Its history exists on one disk, inside the synced folder, with no copy anywhere else. Giving it a remote is a ten minute job and would be worth doing whatever is decided about everything else here.

### Backup on this machine

- `tmutil destinationinfo` returns "No destinations configured." Time Machine has never been set up.
- `tmutil listlocalsnapshots /` returns nothing. There are no APFS local snapshots.

So there is no local backup of any kind, and there never has been.

### Does iCloud keep restorable versions of these file types

Not in any way I would rely on, and I want to be exact about why rather than repeat folklore.

The macOS versions store exists on this volume (`/System/Volumes/Data/.DocumentRevisions-V100`). It only ever holds versions for documents saved by applications that opt into that mechanism, which in practice means Apple's own apps and a handful of others. Every specification document in this project is written by Chat's filesystem connector or by my scripts. Neither goes through that mechanism, and I could not produce a restorable earlier version of a single `.md` file in this project.

What iCloud genuinely does give is **Recently Deleted, thirty days**. That is real and it is worth knowing.

**So the two damage cases have completely different answers, and only one of them is covered:**

- **A file deleted tonight:** recoverable for thirty days, from Recently Deleted, by Kain, in Finder or on iCloud.com.
- **A file overwritten tonight with wrong contents:** gone. The overwrite syncs to the other machine within minutes and the good version exists nowhere. This is the case that matters, because it is the one an agent working unattended actually produces.

**Name what could be recovered if a specification document were damaged tonight:** if deleted, itself, for thirty days. If overwritten, nothing. The DSRDs, the channel, the handovers and the PRD are all in the second category.

---

## Two. Does the iCloud folder already put the theme repository at risk

### The placeholder mechanism is already biting this project

I found **676 iCloud placeholder stubs** in the project home, **593 of them inside this project**, of which **283 sit inside the website assets folder**. A placeholder is the case the channel README describes: the name is there, the contents are not on this machine.

Most are images and zips, which is exactly what Optimise Mac Storage is for and no cause for alarm. These are not:

```
Knowledge Hub Design Prototypes/Category Hub Page/category-hub.html
Knowledge Hub Design Prototypes/Category Hub Page/quotes-section-v2.html
Knowledge Hub Design Prototypes/Listing Page/listing-page-responsive-review.html
About + People Design Prototypes/About Landing Page/timeline-corrected.html
Academy + Courses Design Prototypes/Schools Landing Page/achology_mountain_component_claude_brief.md
```

Those are prototypes and a component brief, in live design folders, not the Archive. Under Rule 4 an approved prototype is the build instruction. So this is not only a storage question: **several build instructions are, on this machine right now, a filename with nothing behind it.** They will download on demand when something opens them, so nothing is lost, but a script that reads a folder and finds a stub does not always know that is what it found.

**The fix is already demonstrated inside this project.** The Component Design Prototypes folder has zero placeholders, and its own git history says why: commit `b82670b`, "Replace the iCloud placeholders with the real files". Putting that folder under version control is what pulled its contents back onto the disk and has kept them there.

### The theme repository specifically

No damage found today. `git status` is clean, the log reads end to end, and there are no conflicted or duplicated filenames anywhere inside the theme.

But the shape of the risk is measurable and it is larger than I expected:

- The theme folder is 364 MB, of which **`.git` is 326 MB**.
- `git count-objects -v` reports **3,208 loose objects and no packfile at all** (`in-pack: 0, packs: 0`).

So iCloud is currently syncing 3,208 small files that are the repository's internals. The moment git repacks (it does this on its own schedule), thousands of those files are deleted and one large file appears. A bulk delete-and-replace inside a folder that two machines are syncing is the exact operation that goes wrong, and it will happen without anyone asking for it.

### One more mark, recorded honestly

There are **137 files named `*.timings 2.json`** in the audio folder. A trailing " 2" is the name iCloud gives a file it could not merge. I cannot prove that is what made them, because a script that ran twice would leave the same trace, so I record it as consistent with the mechanism rather than as evidence of it. There are no such duplicates in the DSRD folder or in the channel.

### My recommendation on moving the working copy

**Yes, move it, and it costs almost nothing.** GitHub holds the true copy, so the move is a clone to a local path outside the synced folder and a deletion of the old working copy. It takes 326 MB and 3,208 files out of iCloud's hands entirely, and it removes the one part of the record that is already safe from the one place that can corrupt it.

The reason it is Kain's call and not mine is not technical: it changes where the theme folder appears in his Finder, and my standing instruction is that anything changing what he sees goes to him.

---

## Three. If a private repository is the right answer, what it covers and what it costs

### In

| What | Size | Why |
|---|---|---|
| `02. Project Delivery System` | 4.2 MB | The DSRDs, the PRD, the skills library, the handovers. The irreplaceable half of the project. |
| `03. Notes for Claude Chat` | 9.7 MB | The whole channel, including its Archive. Every ruling, commission and report either Claude has written. |
| The text artefacts under `03. Achology Website Pages` | ~2 MB | 105 markdown, HTML, CSS and SVG files: the prototypes, the build sheets, the folder READMEs and the DSRD 6 records. |
| The folder map and the organising READMEs at the project root | tiny | The one "where does this go" guide. |

**Roughly 15 to 20 MB.** It stays small because it is text, and because the large folders are excluded by name rather than by a size threshold that will drift.

### Out, and why

- **Every image and video folder.** The design prototype folders are 134 MB and almost all of that is page images: Proof and Funnel 58 MB, Academy and Courses 38 MB, About and People 27 MB. The prototypes themselves are kilobytes.
- **`04. Content Production Factory` (678 MB), `06. Audio` (318 MB), `07. Videos`, `99. OBSOLETE` (382 MB).** Bulk, replaceable or already superseded.
- **The theme.** It has its own repository and its own remote. Nesting it would be a mistake.
- **`achology.zip`.** A build artefact, rebuilt after every push.
- **Anything holding a credential.** The Desktop credential the channel README names stays exactly where it is. It never enters a repository, private or otherwise, and I would add a check that refuses a commit containing anything that looks like a key.

### Where it sits

**Inside the synced folder**, and this is forced rather than chosen. Chat reaches the project through a filesystem connector into that folder. Move the working copy out and Chat can no longer read the channel or write the DSRDs, which ends the project.

That is fine, because the protection comes from the remote and not from the location. A 15 MB text repository produces a small `.git` with little churn, so it does not carry the theme's 3,208-loose-object problem. The theme is the opposite case, which is why my answer differs for the two.

### Is there a better answer than a repository

I considered three and I would take two of them.

**A whole-folder cloud backup** (Backblaze, Arq, or similar) would cover all 1.4 GB including the media, restore by date, and need no discipline from anyone. But it returns a file as it was at a moment. It cannot tell you what changed, when, or why. For a record whose entire value is the reasoning behind decisions, that is the weaker artefact.

**Time Machine to an external disk** is the obvious missing thing and it is free. It keeps hourly versions for a day, so unlike iCloud it does cover the overwrite case. It needs Kain to plug a disk in once.

**My recommendation is both, in this order:** the private repository first, because it is the only thing that gives the written record a history rather than a copy, and because it also fixes the placeholder problem for the folders it covers. Time Machine second, because it costs one disk and one switch and it covers the 1.4 GB the repository will never hold.

---

## Four. What would trigger a commit

Three candidates, and I would build two of them.

**My session close.** Already a fixed point in every session I run: it writes the memory note and the session report. Adding a commit there is the cheapest possible build and it produces a real message, because at that moment I know what changed and why. It captures nothing Chat does, and Chat writes the DSRDs, which is half the record.

**A scheduled job on this machine** (a launchd agent, hourly or nightly), committing whatever changed with a stamped message. This catches Chat's writes and Kain's own edits, needs nobody at the machine, and is the only option that covers the case this request is actually about. Its cost is a commit message that says nothing useful.

**Both, which is what I would build.** The scheduled job as the floor, so nothing is ever unrecorded; the session close commit on top of it, carrying the message that explains the change. A record with a hundred meaningless commits and thirty good ones is far better than a record with thirty good ones and gaps between them.

**What needs Kain at the machine:** creating the private repository under his GitHub account, once, and deciding it should exist. After that, nothing at all. The scheduled job runs whether he is there or not, and pushing uses a credential of the same kind the theme already pushes with.

---

## Five. My honest view on overnight running

**Not yet, and the missing piece is smaller than it looks.**

The reason is not the agent and it is not the permission prompts. It is that there is currently no floor under the blast radius. Fifteen megabytes of irreplaceable text exists in one copy on a folder with no backup, no snapshots and no usable version history, and it syncs damage to the second machine faster than anyone would notice it. That is an unacceptable position to be in whether or not I ever run a single unattended minute, and it is what I would fix first regardless of the overnight question.

**What I would want in place first, in order:**

1. **The written record has a remote.** This is the whole of the condition, and it is one evening's work.
2. **Time Machine configured.** There is no local backup of any kind on this machine.
3. **The queue genuinely decision free.** Chat has already established this and I have nothing to add to it.
4. **One further thing Chat has not named: the queue in small separately committed jobs, not one long one.** If a night goes wrong, the morning's recovery should be reverting one commit, not unpicking eight hours of interleaved work.

**What I would refuse to do unattended whatever else is true:**

- **Anything that writes to achology.com.** I deploy to the build ground. The live site is not the build ground and a night is a long time to be wrong on it.
- **Any bulk change across the 249 help articles or the 897 reviews.** The lesson from the article rebuild stands: a bulk content change silently invalidates everything derived from that content, and no gate catches it. The person who finds out is Kain, the next morning, on a page.
- **Any deletion whose reversal has not been proved before the first write.**
- **Anything needing a ruling.** Rule 5 stops me and files a question, which is the correct failure, but it means a night is worth whatever sits in front of the first gap. That is an argument for queue order, not against overnight running.

**And one honest thing about my own machinery, since the request asks what I know about it.** The hooks refuse actions; they do not supervise judgement. H2 stops an edit I did not declare. Nothing stops a declared edit that is wrong in a way I cannot see, and twice in the last three sessions I have attached a confident explanation to something I had not measured. Both were caught the same day, one by a gate and one by re-running the same job twice and finding the two runs disagreed. Overnight does not create that failure mode; it lengthens the time between the failure and someone noticing it, from minutes to a morning. Small separately committed jobs are the mitigation, and they are cheap.

---

## What I did not do

Nothing here was acted on. No repository was created, no folder moved, no scheduled job installed, no setting changed. The two things I would do first if this is approved are the private repository with its remote, and a remote for the Component Design Prototypes repository that already exists and has none.

*No em or en dashes in this file; checked before writing.*
