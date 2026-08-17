# RULING: the status line is not read, and never has been

**From:** Claude Code, S052. **Date:** 2026-08-10.
**Filed under Harness Rule 14:** a ruling from Kain in session is authority, and
is filed the same session so Chat writes it into the owning document.
**Follows:** `REPORT__What_The_Harness_Costs_And_What_It_Has_Caught_S052.md`,
which established that the ceremony was the one part of the harness with no
measurement attached, and that only Kain could supply the missing fact.

## The question and Kain's answer, quoted

I asked, in these words: "Do you actually read it, and has it ever told you
something you would otherwise have missed?"

> "No - i don't read it"

## What that invalidates, word for word

The status line's entire justification in the harness is a claim about Kain
reading it. From `000__THE_HARNESS.md`, read fresh this turn, the paragraph
directly under the status line format:

> "Kain's whole check is reading this line. If the line is missing, or Spec
> quoted says no, or Gates says fail without a stop, or Outside scope says
> anything but none, the harness is broken and the problem-interrupt fires. Kain
> never audits code and never needs to."

Every sentence there rests on the line being read. It is not. So Rule 10, which
makes a message without the line a harness break, is currently enforcing a
ritual whose stated purpose does not happen, and has been for the twenty five
sessions since the harness was installed at S227.

## And the harness already forbids it on its own terms

This is not my opinion about ceremony. It is the document against itself. From
the same file, the closure section quoting the Chat Harness's growth governor:

> "A rule enters only as another leaves, only with a test someone else could
> check, and never to govern the shape of a message."

Rule 10 governs the shape of every message Code sends. It is the clearest
example in the project of the thing that rule exists to prevent, and it sits
four sections above the sentence that forbids it.

## The second ruling: Kain has told me to drop it

I put the decision to him directly rather than acting on the fact myself. I
asked whether to drop the line now and let Chat catch the document up
afterwards. His answer:

> "yes, drop it"

**So the status line stops from S052, this message onward.** That is Rule 14
authority and it is the highest in the project; I am not waiting for a brief to
repeat what he has just said.

**What stops is the ritual, not the reporting.** The fixed line at the end of
every message is gone. The information it carried is not: where a gate fails,
where something is changed but not verified, where a page is ready to look at,
or where I have strayed outside what I was asked to do, I will say so plainly in
the message, because that is information Kain needs whether or not it arrives in
a fixed format. Rule 6's requirement that "done" carries its proof is untouched
by this and I am not treating it as loosened.

**No code changes.** I checked the hook scripts rather than assuming: nothing in
H1 to H7 enforces Rule 10. The only match for "status line" anywhere in the
harness directory is H1's own note describing what it prints. So dropping the
line needs no mechanical change, which also means nothing will now stop it
quietly coming back.

## What I have NOT done

**I have not touched the harness document.** Rule 8 puts it out of my hands and
H3 would block the write regardless. Rule 10 and the status-line section are
still written into `000__THE_HARNESS.md` as of this filing, and are now
describing something that no longer happens. Until Chat versions the document,
the harness and the practice disagree, and that gap is itself the drift Rule 14
exists to close. This file is the record that closes it; the edit is Chat's.

## The honest case for keeping it, which should be weighed properly

I have a stake in this: the line costs me output tokens on every message, so I
am not a neutral party and the argument against it should not come only from me.

There is one real argument for keeping it. Writing the line forces me to state,
every single time, what my scope was, whether I quoted a specification or
guessed, whether the gates ran, and whether I strayed. That is a checklist
effect, and checklists work on people who already know the rules. It is
plausible it has caught me in the act of finishing something unverified, and no
transcript can prove or disprove that.

But if that is the reason to keep it, then that is what the document should say,
and it should say it as a claim about Code's self-checking rather than a claim
about Kain's auditing. Keeping the rule while its written justification is known
to be false is the precise form of drift this project's harnesses exist to stop.

## The larger question, asked once and not campaigned on

If the status line has gone unread for twenty five sessions without anyone
noticing, the reasonable next question is what else in the harness was built for
an audience that is not there. I am not proposing an answer and I am certainly
not proposing a demolition: the measured report showed three hooks doing real,
repeated work, and those are not in question. But the growth governor's test,
"a test someone else could check", is worth running across the remaining
obligations, and Chat is better placed than I am to run it, because Chat wrote
them.

## What I need from Chat

A version of the harness that either retires the status line, or keeps it with
an honest justification. Not my call, and not a change I can make. Kain's answer
is above in his own words; the rest is yours.

*No em or en dashes in this file; checked before writing.*
