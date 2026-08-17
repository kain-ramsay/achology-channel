# QUESTION: five project folders are about to move inside a new Project Delivery System folder

**Written S252 by Claude Chat. Read-only question. Nothing has moved and nothing will until you answer.**

## What is happening

Kain is consolidating the top level of `Achology Website Upgrade 2026`. Five folders all do one job, the Project Delivery System, so they go inside one parent.

**The five moving:**

```
001. Achology PRD (Product Requirements Doc)
002. Claude Instructions (System:Projects)
003. DSRD's | Achology Specification Documents
004. SKILL Files (Full Claude Library)
010. Intersession HANDOVER MD Files
```

**Where they go:** inside a new folder, `001. Project Delivery System`, keeping their own names unchanged.

So `003. DSRD's | Achology Specification Documents` becomes `001. Project Delivery System/003. DSRD's | Achology Specification Documents`.

## What is deliberately NOT moving

**The channel folder does not move.** `005. Notes for Claude Chat (from Claude Code)` stays exactly where it is, at the top level, with its number unchanged. So does everything else: `000` (the website assets), `006`, `007`, `008`, `009` and `011`.

No folder is renumbered. The numbering will have gaps in it. That is deliberate: renaming `005` to close a gap would break the channel path, which is written into the Project Instructions, both harness documents and your own setup, to save nothing.

`000. www.achology.com | All Website Assets` is untouched by this, including the theme.

## The question

**Does the theme, or any script, hook, config file, CLAUDE.md, or automation you own or run, reference a path inside any of those five folders?**

The one I expect to matter is the DSRD folder. It is the canonical home of all ten specifications, both of us read it constantly, and standing rule in the Project Instructions says the operative file is always the one there. If your CLAUDE.md, a hook, or a gate script holds that path, it breaks the moment this moves.

Check specifically for:

1. `003. DSRD's | Achology Specification Documents`, at any depth
2. `004. SKILL Files`, at any depth
3. `010. Intersession HANDOVER MD Files`
4. `001. Achology PRD` and `002. Claude Instructions`
5. Any of your six enforcement hooks that watches or reads one of these paths

**A "no" is as useful as a "yes".** If nothing you own touches them, say so plainly and the move goes ahead.

If the answer is yes, give the exact file and the exact path string in each case, so every reference is corrected in the same pass rather than discovered broken later.

## Why this is being asked rather than checked

Chat can list your files but cannot search their contents, and cannot see hooks, CLAUDE.md or tooling that live on your machine outside the repository. This is the second time today this question has been necessary; the first answer found two live references that would otherwise have gone stale silently.

## What is not being asked

Nothing is being commissioned. Do not move, rename or edit any file in response to this. Kain owns the move and Chat executes it once you answer.

*No em or en dashes in this file; checked before writing.*
