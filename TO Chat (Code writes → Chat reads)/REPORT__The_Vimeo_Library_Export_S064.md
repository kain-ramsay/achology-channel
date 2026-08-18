**DISPOSITION (S284): all facts driven onto the Vimeo Course Refresh card, including the replace-path answer, the storage-neutral finding, the version-retention open question and the 788 superseded videos. The stream is paused pending the fresh-eyes review; execution decisions wait on it, then Kain. Archived.**

# REPORT: the Vimeo library is exported, the replace path exists, and the storage saving does not

**DOCUMENT TYPE:** report. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Closes:** `COMMISSION__Export_The_Whole_Vimeo_Library_Read_Only_And_Answer_The_Account_Questions_S283.md`, except Step 4, which is answered as a stop-and-ask.
**Read only throughout.** Nothing in Vimeo was changed, replaced, uploaded, renamed, deleted, moved or re-tagged. Every request was a GET.

---

## The answer you asked for in the first line

**Yes. The replace-a-file path is available on this plan.** Every video carries a `versions` connection at `/videos/{id}/versions`, currently reading `total: 1`. That is the mechanism that swaps a file while keeping the video ID, the embed and the stats, and it exists on this account. **The approach the whole stream rests on is sound.**

---

## Step 0: access

**Reached.** The account is **Achology**, `/users/71102328`, account type **`custom`**, which is Vimeo's label for Enterprise.

Kain generated a fresh personal access token today. **Its scopes are `private`, `video_files` and `public`, and nothing else**, so the token cannot write even by accident. It is read from a file on disk by the export script alone and has never been printed into a report, a command line or the conversation.

**One thing for the record:** the token that existed for the earlier transcript work is gone. It lived in a project folder, `course-video-export`, which no longer exists on the machine. That is why this had to be regenerated rather than reused.

---

## A correction, before anything is decided on it

**I told Kain in session that the Drive masters are more than twice the size of what Vimeo holds, and that replacing them would add storage rather than free it. That comparison was wrong and I withdraw it.**

I had summed the **largest single rendition** of each Vimeo video. Vimeo returns several transcodes per video and stores all of them, so the largest one is not what the account holds. **There is no `source` entry in the API's file list at all**, on any of the videos I checked: only Vimeo's own `hd`, `sd` and `hls` renditions, between three and seven per video.

Corrected, and with the renditions de-duplicated because the `hls` entry repeats the top mp4's size rather than being a separate file:

| | Largest rendition only | All renditions |
|---|---|---|
| Numbered course folders | 1.28 TB | **2.43 TB** |
| Everything else | 0.72 TB | **1.36 TB** |
| **Whole account** | 2.00 TB | **3.79 TB** |

**Google Drive, the same course lectures: 2.77 TB across 2,145 files.**

So the honest comparison is **2.43 TB in Vimeo against 2.77 TB in Drive for the same lectures**, and they are of the same order. Not double. My earlier figure compared two different things.

---

## Step 2: the storage answer, and the part that decides the money

### Karen's figure cannot be confirmed from the account, and that is a real blank

**The API returns `null` for both `space` and `upload_quota` on this plan.** Not zero, not a small number: nothing at all. Enterprise accounts appear not to expose a quota through the API, presumably because the allowance is contractual rather than metered by the product.

**So Karen's "71 per cent of seven terabytes, roughly 4.97 TB used and 2 TB free" cannot be confirmed or corrected from the account itself, and I am not going to repeat it as fact.** What would settle it: the storage panel in the Vimeo account settings in a browser, or the Enterprise contact at Vimeo.

**It is, however, consistent with what I can measure.** 3.79 TB of renditions plus the original uploads, whose sizes the API does not expose, would plausibly land near 4.97 TB. Her number looks right; it just is not machine-confirmable from here.

### The replacement will not free space, and this is the finding that matters

**A replacement does not upload renditions.** One master goes up and Vimeo re-transcodes it into the same family of renditions. So the account after a full replacement holds a new source plus a new set of transcodes for each of 2,145 videos: **roughly what it holds now, and slightly more if the new masters are larger than the old ones, which at 2.77 TB against 2.43 TB they are.**

**The hoped-for plan reduction does not follow from the replacement.** It is close to storage-neutral at best.

### The version-retention question, flagged as you asked rather than inferred

**The `versions` connection exists and reads `total: 1` today.** That endpoint's whole purpose is to hold more than one version of a video, which means a replacement plausibly creates version 2 while version 1 persists as an object. **Whether a retained prior version continues to count against the allowance is not something the API states**, and I will not infer it.

**This is the question that decides whether any saving is real, and it needs Vimeo's own answer.** If prior versions are retained and billed, then every replacement adds storage twice over. **Kain's Enterprise contact can settle it in one email, and it should be settled before 2,145 replacements run, not after.**

---

## Step 1: the export

**`Vimeo library export (18 August 2026).csv`, written into the `Course + Lesson Data | MASTER` folder.** The folder's read me now names it. **3,994 rows, one per video in the account, not only the course lectures.**

Columns: Video ID, Title, Description, Folder Name, Folder URI, Duration (seconds), File Size (bytes), Created, Modified, Released, Privacy View, Privacy Embed, Privacy Download, Privacy Add, Privacy Comments, Link, Embed URL, Text Tracks, Status, Type, Plays.

**Nothing was written into the twenty eight course CSVs. `Vimeo URL` and `Vimeo Video ID` remain empty on all 2,146 rows**, exactly as instructed, because deciding which Vimeo video is which lesson is not this commission's job.

**One caveat on the size column, given the correction above:** it holds the largest rendition, which is the single most useful per-video figure but is not that video's storage footprint. The rendition arithmetic is in this report rather than in the file.

---

## Step 3: the account facts

| Question | Answer |
|---|---|
| Plan tier | `custom`, Vimeo's Enterprise label |
| What it gates | **Not stated by the API.** Unknown, and only the contract or Vimeo can say |
| Upload allowance, per file or period | **Not stated.** `upload_quota` is null |
| API rate limit | **1,500 requests per hour**, from the live response headers |
| Replace-a-file path | **Available.** `versions` connection present on every video |
| Auto-captioning enabled | **Yes, at least in part.** 647 of 3,994 videos carry a text track; the ones I sampled are `en-x-autogen` and active, which is Vimeo's own automatic captioning |
| Does captioning regenerate on a replaced file | **Unknown.** Cannot be established without performing a replacement, which is not commissioned |

**On scale, the third figure you asked for.** The board card says roughly 2,800. The twenty eight CSVs hold 2,146 lessons. **The account holds 3,994 videos.** All three stand side by side; none of them is wrong, they count different things.

**A rate limit of 1,500 an hour is not a constraint on a 2,145-video run.** The full export took forty requests.

---

## The numbered folders match the spreadsheet almost exactly

**This was not asked for and is the most useful thing in the export.** Vimeo's course folders are numbered `001` to `028` like the sheets, and they hold **2,147 videos against the spreadsheet's 2,146 lessons.**

**Twenty seven of the twenty eight agree to the video.** One does not:

| Course | Vimeo folder | Vimeo videos | Lessons | Difference |
|---|---|---|---|---|
| 007 | 007 CBT Practitioner | 120 | 119 | **+1** |

**Every other course matches its lesson count exactly.** That is a strong independent signal that the numbering holds on the Vimeo side too, and it means the eventual three-way match has a real chance of being clean. **No matching was performed and no Vimeo ID was written anywhere**, per your instruction.

---

## Where space actually is recoverable, and it is not the replacement

**1,847 of the 3,994 videos sit outside the numbered course folders, holding 1.36 TB of renditions.** Among them are complete older copies of courses that have since been renumbered:

| Folder | Videos | Renditions |
|---|---|---|
| NLP Master Practitioner | 184 | 95.1 GB |
| Mindfulness Practitioner | 136 | 28.9 GB |
| Life Coaching Cert (2019) | 129 | 35.4 GB |
| NLP Practitioner | 126 | 60.6 GB |
| CBT Practitioner | 107 | 21.2 GB |
| Life Coaching Cert (2017) | 106 | 23.3 GB |

**That is 788 videos of superseded course material**, sitting beside the numbered folders that supersede them. **Retiring those is what would free real space, and it has nothing to do with the replacement job.** It is also a decision nobody has been asked to take, so it is named here and not acted on.

The rest of the non-course material is legitimate and varied: 168 course preview videos, 120 "Principles Into Practice" questions, several Achology Live Session sets, 106 testimonial videos across four folders, promos, onboarding, Gerry's talks, and 30 videos in no folder at all.

## Other things worth knowing before a bulk run

**Ten videos are not usable.** Nine read `uploading` and one reads `uploading_error`, and those ten are the only ones with no size. They have been sitting in that state; a bulk run should skip them rather than fail on them.

**Every video in the account has `embed: whitelist`.** Not one is open-embed. So a replacement changes nothing about embedding, but any new upload would need the same whitelist applied or it will not play on the site.

**Privacy is not uniform:** 3,624 videos are `view: disable`, 360 are `anybody`, 10 are `unlisted`. The 360 viewable ones are worth a look, since a course lecture set to `anybody` is watchable outside the paid membership.

**Only 196 of the 2,147 course videos have a caption track**, against 451 of the 1,847 non-course videos. So the transcript position is much worse on the courses than the headline 647 suggests.

---

## Step 4: the website column contract, and this one is a stop-and-ask

**I cannot answer it, and the reason is that the thing it describes does not exist yet.**

I read the theme rather than assuming. **There is no course page template, no school page template and no curriculum renderer anywhere in it.** `courses-setup.php` contains nothing that reads a lesson, a section or a curriculum. Nothing in the theme consumes this data today.

**So there is no import to state the needs of.** Any column list, order or header naming I gave you would be my invention presented as a contract, and the first real course page spec would contradict it.

**What would settle it:** the signed page specification for the course page and the school page, which say what those pages display. When those exist the contract falls out of them in a few minutes. Until then this is a genuine specification gap and I have not filled it.

**One thing I can confirm, because it is a ruling rather than a design question:** the website reads `Standardised Description` and never `Lesson Description`, per Kain's S283 ruling, and that column exists and is empty awaiting your standardisation pass.

*No em or en dashes in this file; checked before writing.*
