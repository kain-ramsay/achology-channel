# COMMISSION: convert every Card System prototype to the lightweight form

**From:** Claude Chat, Session 261. **Date:** 2026-08-11.
**Authority:** Kain, ruled in session S261. He wants every stored prototype in the lightweight form to keep the folder small and cheap to read; Chat recommended you as the executor because this is a local file operation on the Mac, and it pairs with the git work already commissioned to you for this folder (Act 1 of `COMMISSION__Build_Vs_Sheet_Gate_S257.md`).

## What the lightweight form is

A prototype file whose embedded Como `@font-face` block (roughly 224KB of base64 across 8 weights) is replaced by the single line:

    /* COMO_FONT_INJECT */

Everything else in the file is byte-identical to the approved render. Injecting the standard Como CSS at that placeholder reproduces the exact approved file, so the lightweight file remains the signed record: every design value in it is the approved value. Two prototypes already use this form, written by Chat this session: the featured workbook and featured book note proofs. Their header comments carry the standard wording; reuse it.

## The work

In the Card System folder (Component Design Prototypes; the folder README lists the current filenames):

1. For each current prototype still carrying an embedded Como block, replace the whole `@font-face` block set with the `/* COMO_FONT_INJECT */` placeholder on its own line where the block began, and add the standard header comment (copy the wording from either S261 prototype, adjusting the card name and approval session, which the README's table carries per file).
2. Keep one canonical Como CSS file on the Mac for re-injection, in the folder you judge right for assets of that kind, and record where it lives in the Card System README in one line. The theme already carries the fonts, so extract from there rather than from a proof if that is cleaner.
3. Do the same for the Archive (Superseded) subfolder's files, since they are kept only as records and are the least-read, heaviest files in the folder.
4. Verify each conversion by re-injecting once and diffing against the original before the original is discarded; a conversion that does not reproduce the original byte for byte is wrong. Where the folder is under git by the time you do this, the originals live in history anyway and the diff is your proof of equivalence.
5. Update the Card System README's last-updated note: all prototypes now stored lightweight, with the injection note.

## Acceptance

Every HTML file in Card System and its Archive carries the placeholder instead of an embedded Como block; each conversion diff-verified; the Como CSS location recorded in the README; the README note updated. Report back through TO Chat with the file count converted and the bytes saved.

*No em or en dashes in this file; checked before writing.*
