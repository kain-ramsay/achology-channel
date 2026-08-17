# HOW TO: the channel sitting, now one step instead of four

**DOCUMENT TYPE:** how-to, for Kain. **From:** Claude Code, Session 061. **Date:** 17 August 2026.

---

## What is already done, so nobody repeats it

You created the repository in the browser during the sitting. Everything else that was going to be on your list, I did:

- The channel is copied to `~/achology-channel`, outside iCloud, and pushed to GitHub. 673 files.
- The watcher is written, installed and running. It commits, pulls and pushes within seconds of any change, and writes a heartbeat so a dead road cannot pass for a quiet one.
- Both directions are tested end to end. A file written here reached GitHub and came back down into a fresh copy; a file pushed from elsewhere landed here and was read.
- My session-open hook now pulls the channel first and refuses to trust a quiet channel it could not pull.

**Homebrew and fswatch are no longer needed at all.** The approved plan had you installing a package manager in order to install a watcher. This Mac had neither, and macOS already does the job itself, so the whole step is gone and nothing new is installed on your machine.

## Your one step

**Add the new channel folder to Claude Chat's Filesystem connector.**

In the Claude desktop app, open Settings, then Connectors, then the Filesystem connector's configuration, and add this folder to its allowed folders:

```
/Users/kainramsay/achology-channel
```

That is the whole sitting. Until it is done, Chat is still writing into the old iCloud folder and cannot see the new road.

## How you will know it worked

Ask Chat, in its next session, to write any small file into `TO Chat` in the new folder. Within about a minute it will be on GitHub, and I will see it at my next session open. If the road is ever down, my first line of the session will say so, in words, instead of showing you an empty folder and letting us both assume it was a quiet day.

## What happens to the old folder

It stays exactly where it is until Chat has moved, so nothing in flight is lost. Once Chat's first file arrives through the new road, the old folder gets reduced to a single note saying where the channel went, and its files stop being tracked in the record repository so one truth never has two histories. That is my job, not yours, and it is the last step of the migration rather than the first.

*No em or en dashes in this file; checked before writing.*
