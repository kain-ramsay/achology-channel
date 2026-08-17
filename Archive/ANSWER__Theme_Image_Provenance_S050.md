# ANSWER: where every image in the theme came from

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Answers:** `QUESTION__Where_Every_Theme_Image_Came_From_S252.md`.

## How I answered this, and what that limits

Not from memory. Every line below comes from one of two things I can open today: the git history of the theme, which records the commit that first added each group and what that commit was doing, and the files themselves.

**What that tells me reliably:** when an image entered the theme, under what work, and whether it is derived from something else.

**What it cannot tell me:** what was on Kain's desktop before he handed a file over. Where the honest answer is "supplied by Kain and I do not know what he made it from", I have said so rather than guessed a folder. Those are the ones worth him confirming.

## Part 1 and 2: the groups, their source, and the page each serves

| Group | Files | Where it came from | Page it serves |
|---|---|---|---|
| `about/` | 12 plus the subfolder | Supplied by Kain for the About build (v0.37.15, S044). Photographs and Canva compositions, no on-disk original I can point to | About Landing Page |
| `about/testimonials/` | 5 | The five member-story video posters, supplied with the About build | About Landing Page (member stories block) |
| `code-of-character/` | 29, `page-01` to `page-29` | **DERIVED.** Flattened pages of `011. Achology Documents + PDF Resources/Code of Character and Conduct Handbook/Code of Character and Conduct Handbook.pdf` | Code of Ethics Page (the Code of Character reader) |
| `code-of-ethics/` | 42, `page-01` to `page-42` | **DERIVED.** Flattened pages of `011. Achology Documents + PDF Resources/The Achology Code of Ethics Handbook/Achology Code of Ethics Handbook.pdf` | Code of Ethics Page (the handbook reader) |
| `courses/` | 56, `course-001` to `course-028` plus `-icon` variants | Kain's Canva masters, baked in at v0.23.5 and v0.23.6. DSRD 5 §8 says the masters are "stored locally by Kain and in the Achology Canva account" | Course Page, and every course card anywhere |
| `favicon/` | 6 | Generated at v0.34.14 from the phi mark, alongside `achology-logo-mark.webp` | Website-wide |
| `people/` | 11 | The eleven profile portraits, supplied by Kain | Our People Page and Instructor Profile Page |
| `schools/` | 14, a `hero-` and a plain file per school | Kain's Canva masters, baked in at v0.23.5 with the course set | School Page, and school cards |
| `testimonials/` | 91, an `avatar` and a `bg` per member per question | The member video posters, added with the Testimonials template at v0.36.28 | Video Testimonials Page |

**The two you named specifically:**

- **`code-of-character` (29 pages)** belongs to the **Code of Ethics Page**, not to a page of its own. That page carries two handbook readers side by side, the Code of Ethics and the Code of Character, which is why one page folder owns two page sets.
- **`prospectus-cover.webp`** belongs to the **About Landing Page**. Added at v0.21 during the About working build.

## The ten loose files at the images root

| File | Where it came from | Page it serves |
|---|---|---|
| `achology-logo.webp`, `achology-logo-dark.webp` | Present since the first theme backup, v0.6.6 | Website-wide |
| `achology-logo-mark.webp` | Generated at v0.34.14 with the favicon set, from the phi mark | Website-wide, mobile header |
| `achology-bubble.webp` | Added v0.15 when the phi character was retired site-wide; it is the favicon artwork | Website-wide |
| `achology-bubble-mark.webp` | **DERIVED.** A trim of the bubble, cut at v0.31.3 to fill the closing panel | Help pages, closing panel |
| `aristotle-watermark.webp` | **DERIVED.** Kain's marble render with orange drape, recompressed to 67KB webp from a roughly 1MB original at v0.34.14 | Manifesto Page |
| `bookshelf-book-notes.webp` | Kain's own photograph, staged v0.21.10 | Book Note Page, hero and closing panel |
| `manifesto-document.jpg` | Added v0.27.0 with the quiet about-pages | Manifesto Page |
| `cursor-zoom-orange.png` | Added v0.27.0, the zoom cursor for the handbook readers | Code of Ethics Page |
| `prospectus-cover.webp` | Added v0.21 with the About working build | About Landing Page |

## Part 3: the empty page folders, and the Founders' Letter

**The Founders' Letter has no images of its own, and that is the whole answer.** It uses two files from the About set, and I read this off the page's own source rather than recalling it. `policies-content/founders-letter.php` line 59 loads `images/about/kain-and-karen-ramsay-achology-founding-partners.webp` and line 237 loads `images/about/achology-customer-support-team.webp`. Nothing else.

So its page folder should get the short note you describe, naming those two theme paths, not copies. A duplicate would be a second copy of a truth the About folder already holds, which is the thing the reorganisation exists to stop.

**The other empty page folders.** Most are genuinely empty because those pages are not built yet, so no image has ever existed for them. The built pages whose images live under another page's name are: the Founders' Letter (above), and the Policies family, whose ten share images already have a home in `Policy Page` with the spare set archived, per your S252 record.

## Your closing question: which images are derived, so the theme file is the master

Four answers, and they matter because for these there is no better original to go and find:

1. **`code-of-ethics/` (42 files)** and **`code-of-character/` (29 files)**. The master is the PDF in `011.`, not an image. The page folder should say that rather than hold 71 webp files a reader would mistake for masters.
2. **`achology-bubble-mark.webp`**. A crop of `achology-bubble.webp`. The bubble is the master.
3. **`aristotle-watermark.webp`**. Recompressed from an original roughly fifteen times its size. Its commit records the original existed; I cannot see it on disk today, so if Kain still holds it, that is the master and it is worth filing before it is lost.

Everything else is a copy of a file that exists elsewhere, and the theme's version is a working copy rather than the record.

## What I have not done

Nothing was moved or copied, as the question asked. The theme's `images/` folder is untouched.

*No em or en dashes in this file; checked before writing.*
