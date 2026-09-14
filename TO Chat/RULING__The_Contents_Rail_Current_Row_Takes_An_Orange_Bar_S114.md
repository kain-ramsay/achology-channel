> CHAT DISPOSITION, S360: CLOSED, ARCHIVED. Recorded at DSRD 8 §31, both the S110 and S114 reasoning kept side by side as the S110 file itself asked. §27's own anatomy line ("a discreet arrow") is now stale against this ruling; named rather than silently edited, per §31's own note.

# RULING: the contents rail marks the row being read with an orange bar, and the S110 arrow is withdrawn

**DOCUMENT TYPE:** ruling, filed by Claude Code, Session 114, theme session. **Date:** Monday 14 September 2026.
**Filed under Harness Rule 14.** **Supersedes Kain's S110 ruling** that the mark on these rows points down rather than right.
**Shipped:** Theme 0.395.0, deployed and verified on the live install.
**Board card:** Book note page template; Article page template. It is the shared Knowledge Hub sidebar, so it reaches every page type that carries a contents rail.

---

## 1. Kain's words

He asked to be shown the sidebar's parts against each other, then ruled on the mark:

> "With the orange bar looks much better!"

## 2. What changed

The down arrow is gone from the markup. The row being read now carries a two pixel orange bar on its left edge, square ended, in `--toc-copper`, which is the brand orange. The cream panel and the orange words on that row are unchanged.

A hover on any other row shows the same bar at just over a third strength. That is not decoration: the arrow was the only feedback a hover had on these rows, so removing it alone would have left the list dead under the pointer.

The row's grid loses its third column with the arrow. An empty `auto` track is harmless but untrue: it says a thing sits there when nothing does.

## 3. Why an S110 ruling was superseded, since a ruling of Kain's is not overturned lightly

**S110 was right about its own question.** He caught the mark pointing right and ruled it down, because a right arrow means away, to another place, while every one of these links jumps to a heading on this page. Down was simply true and nothing here overturns that reasoning.

**What changed is the job the mark was doing.** It was drawn only on the row being read, so it had long stopped describing where the link goes and was marking where the reader is. A down arrow cannot carry that meaning: sitting on a row with a filled panel behind it, it is the common sign for "this opens", so the section being read looked like a dropdown waiting to be expanded.

It was also the third marker on one row, behind the cream panel and the orange text. Three signals for one state is two too many.

**Both readings are kept in the markup**, the S110 reasoning in full beside the S114 correction, because a superseded ruling that vanishes reads later like a value that drifted.

## 4. How this arrived, which matters for what comes next

Kain asked whether the sidebar's parts complement each other and brought a list of eight suggestions from ChatGPT. **The sidebar was measured rather than judged from a picture**, and the measurement moved the answer:

- Three of the eight were real, and this is the first of them.
- Three were not. The contents block is already sticky at `top: 96px`. The contents text is already the brand dark at weight 500, not the light grey a compressed screenshot suggested. And the proposed spacing pair would have quietly overruled Kain's standing rule of forty eight above and below every hairline.
- Two are decisions rather than faults, and both are his: renaming the heading, which is copy and travels to Chat, and what happens to the Know Your Psychology graphic.

**One remains of the three**, and the other was withdrawn by Code before it was built. What remains is the Amazon link, which already has a button's border and padding and also carries a link's underline, so it reads as neither.

## 5. The gap under the contents is withdrawn, and the withdrawal is the point

Code proposed giving it a fixed step, on the reading that it was whatever `justify-content: space-between` had left over and therefore arbitrary. **Kain agreed to that, and it was wrong.** Reading the rule before touching it found the reason it is there, in the stylesheet's own comment: the panel is a screen-height box that travels, with the contents at its top and the Know Your Psychology mark at its bottom, so the mark sits at the foot of the reader's screen. That effect is Kain's, from S112, and it survived two fixes that session, the one where the mark scrolled up behind the contents and the one where it stopped hard against the hairline.

So the space is not left over. It is the distance between a thing held to the top of the screen and a thing held to the bottom of it, and fixing it at a step would have quietly undone an effect he asked for twice.

**Three claims Code made this session about the sidebar were wrong and were caught by measuring rather than by reading a screenshot**, which is worth recording because two of them were about to become changes: the contents text being faint (it is the brand dark at weight 500), the sidebar running out partway down a long article (the article is 3,467 tall and the column 3,419, so it runs the full length), and this one.

**Nothing about the mark or the gap is asked of Chat.** It is recorded here so the next session does not rediscover the same idea and build it.

OWED BACK: nothing on this one. Chat records it against DSRD 8's entry for the Knowledge Hub sidebar and strikes the S110 line as superseded.

*No em or en dashes in this file; checked before writing.*
