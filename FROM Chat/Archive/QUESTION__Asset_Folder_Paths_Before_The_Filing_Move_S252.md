# QUESTION: does anything you own reference paths in the two asset folders about to dissolve?

**Written S252 by Claude Chat. Read-only question. Nothing is being commissioned here.**

## What is happening

Kain has approved a filing strategy for `000. www.achology.com | All Website Assets`. Two of its folders are about to be dissolved and their contents redistributed. **No file has moved yet, and none will until you answer this.**

The two folders dissolving are:

- `000. www.achology.com | All Website Assets/04. Single Page Template Assets/`
- `000. www.achology.com | All Website Assets/05. Website Images (High-Res MASTERS)/`

The `03. Como The Achology.com Font` folder is also moving, becoming a subfolder of the new Website-Wide Assets folder.

## The shape it becomes

`000` drops from five top-level folders to three:

```
01. The Achology WordPress Theme        unchanged, same path
02. Website-Wide Assets                 logos, favicons, bubble, Como font, default share image
03. Achology Website Pages              renamed from "02. Page + Components (HTML Design Files)"
```

Every page folder inside `03` gains a `Page Images` subfolder holding that page's images. Course images land in `Course Page/Page Images`, school images in `School Page/Page Images`, and so on. Data files (the help and FAQ CSVs, the testimonial transcripts, `transcripts.json`, `countries-110m.json`) leave `000` entirely for `007. Spreadsheets | Data | CSV Files`. `qc_gate.py` leaves for project tooling.

Note that `01. The Achology WordPress Theme` does not move and its path does not change.

## The question

**Does the theme, or any script, tool, config file or automation you own or run, reference a path inside any of these three folders?**

Specifically:

1. Anything reading from `04. Single Page Template Assets`, at any depth. The help and FAQ CSVs and `qc_gate.py` are the likeliest candidates, since they look like import and quality-gate inputs.
2. Anything reading from `05. Website Images (High-Res MASTERS)`. The course, school and people image sets are the likeliest candidates, if any upload or media-library sync reads from them.
3. Anything reading from `03. Como The Achology.com Font`, including the base64 stylesheet.
4. Anything reading the current name `02. Page + Components (HTML Design Files)`, which is being renamed.

**A "no" is as useful as a "yes".** If nothing you own touches these paths, say so plainly and the moves go ahead.

If the answer is yes, give the exact file and the exact path string in each case, so the reference can be updated in the same pass as the move rather than discovered broken later.

## Why this is being asked rather than checked

Chat can read the theme's files but cannot search their contents, and cannot see scripts or tooling that live on your machine outside the repository. The S251 tidy already moved two paths you had cited, and they were caught only by accident. That is the failure this question exists to prevent.

## What is not being asked

Nothing is being commissioned. Do not move, rename or edit any file in response to this. Kain owns the moves and Chat is executing them once you answer.

---

## A second question, added S252 after Kain's calls

**Which course and school image variants does the live site actually use?**

Every course exists in four versions (PNG and SVG, with and without the KYP logo), which is 112 files, and the schools carry a similar spread plus mega-menu icons and white and grey logos.

Kain has ruled that all variants move into the page folder, with the versions the site does not use going into an `Archive` subfolder inside it. Only you can say which those are.

So: **name the variants the theme or the media library actually serves.** Everything you do not name goes to Archive.

*No em or en dashes in this file; checked before writing.*
