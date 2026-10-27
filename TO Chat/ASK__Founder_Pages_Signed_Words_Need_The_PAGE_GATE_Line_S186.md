**For Chat. What this needs from you:** the PAGE GATE line at the foot of RULING__Place_The_Signed_Words_Of_The_Three_Founder_Pages_S448 (or a DOCUMENT TYPE line declaring it copy, not a page spec), so the theme session can place the words. Kain is waiting on it in the sitting now.

# ASK (theme session, S186): the founder pages' signed words are refused by the page gate intake

The harness hook H2 (spec_intake) arms on every edit to a file in the policies-content folder and reads the spec the declaration names. It refused the placing of the Founders' Letter's signed words:

> H2 PAGE GATE INTAKE: blocked. The spec governing this page carries no PAGE GATE line at its foot. (A document with no DOCUMENT TYPE line is treated as a page spec, ruled by Kain S266.) RULING__Place_The_Signed_Words_Of_The_Three_Founder_Pages_S448.md

What was checked: the Manifesto has a signed spec with its PAGE GATE line (About + People Design Prototypes, Manifesto Page, 000__SIGNED_SPEC__Manifesto_Page_S446); the Founders' Letter and the Code of Ethics have no signed spec anywhere in the project. The ruling itself has neither a PAGE GATE line nor a DOCUMENT TYPE line.

Nothing has been placed: one partial was changed before the hook fired, and that change was reverted (git checkout), so all three partials are as built at 0.707.625.

The fix is Chat's, not Code's (the hook says so): either add the PAGE GATE line to the ruling, or declare its DOCUMENT TYPE as copy so the intake knows it is not a page spec. The moment either lands, Code places all three pages and sends the DONE with the Rank Math scores.

OWED BACK: the line added to the ruling (a field a machine can test: the ruling's foot carries "PAGE GATE:" or its head carries "DOCUMENT TYPE:").

*No em or en dashes in this file; checked before writing.*
