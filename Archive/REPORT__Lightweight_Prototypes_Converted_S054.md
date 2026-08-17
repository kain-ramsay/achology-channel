# REPORT: every Card System prototype is now stored lightweight

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**Answers:** `COMMISSION__Lightweight_Prototypes_Across_The_Card_System_Folder_S261.md`, its five steps and its acceptance.

## The counts

**Ten files converted. 2,185 KB saved.** Two more were already lightweight, written by Chat at S261. Two are deliberately not converted, for a reason below.

| Where | Converted | Already lightweight | Deliberately not converted |
|---|---|---|---|
| Card System | 5 | 2 | 2 |
| Archive (Superseded) | 5 | 0 | 0 |

The Archive files gained most in proportion: five records of 232 to 238 KB each are now 8 to 14 KB. They were the least-read and heaviest files in the folder, exactly as the commission said.

## Every conversion is diff-verified, and the verification runs before the write

Step 4 asked for re-injection and a diff against the original before the original is discarded. It is stronger than that in practice: **the script re-injects the extracted block, compares the result to the original in memory, and refuses to write the file at all unless it is byte-identical.** An unverifiable conversion of a signed record leaves the heavy file alone rather than producing a light one nobody can trust. No file was refused.

## The canonical Como CSS, and where it lives

**`Component Design Prototypes/_assets/como-fonts.css`, 224,183 bytes.** Recorded in the Card System README in one line, as step 2 asked.

**All ten converted files carried the identical Como block**, checked rather than assumed: the script collects every extracted block and writes the canonical file only if they are all the same. Had they differed there would be no single "standard Como CSS" and re-injection would not be reversible, so it would have reported that instead of writing.

**It is stored beside the prototypes rather than in the Website-Wide Assets font folder, and the reason is a finding.** Step 2 suggested extracting from the theme, which would have been cleaner. It is not available: **every file in `02. Website-Wide Assets/The Como Font/` is an un-downloaded iCloud placeholder stub of 163 to 174 bytes.** The fonts are not actually on this Mac. Worth knowing beyond this job, because the S262 filing card asked about exactly this class of problem and this is a second instance, thirty-six files this time.

## The two files deliberately not converted

Neither carries embedded base64, so neither has weight to save, and filling their placeholder with the eight-weight block would change how a signed record renders.

- **The review card proof** loads Como by URL from the live theme.
- **The featured quote card proof** loads it by relative path from the font folder above. Its README entry says it therefore renders "true straight from disk with no injection step". **That claim is currently false on this machine**, because of the iCloud stubs. Recorded, not fixed: the file is Chat's and the fonts are Kain's to download.

## The README is updated

The last-updated note now reads S054, and the folder carries a new section stating how Como is stored, where the canonical copy is, why it is there, and which two files are exempt. The two prior update notes are kept beneath it.

One thing added beyond this commission, flagged rather than assumed: **the global impact block's build sheet is filed in this folder too**, under the S262 icon sweep's "plus one export", with a README row saying why a non-card component lives among the cards.

*No em or en dashes in this file; checked before writing.*
