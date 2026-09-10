# RULING AND SHIP: the article hero comes into the reading column, takes the writer line, and shows the picture

**From Code, S110. Date: Thursday 10 September 2026. Shipped at theme 0.290.0,
deployed, gated and measured at five widths.**
**Ruled by Kain** live in this sitting, on the band shipped an hour earlier,
which he first accepted in these words: *"you've just done the hero banner, and
I'll be honest with you, it's kinda perfect. It's exactly what we're looking for.
It's simple."* Then three changes:

> "We need to bring the breadcrumbs and the container into the 880 size. So
> essentially the entire article and this container is all at one left edge. And
> then I would say bring the written by author date and seven minute read, bring
> that just directly underneath the article mini description. And I think we're
> just about there. I think to the right hand side of the card, you could
> probably just place the actual article image over the background. I think that
> will actually look pretty good."

**Owning documents:** DSRD 9 section 22, already owed a set of corrections from
the ruling an hour earlier; this adds to them. DSRD 8's `kh-hero` entry.
**Board card:** none of its own.

---

## What is on the page

The band still runs the full width of the screen, which is what makes it a band.
Everything inside it now begins where the article begins: the trail, the overline,
the title, the summary, the writer line and the picture all sit on the 880 reading
column. The picture is an object at the right of that column, and the writer line
sits directly under the summary.

## This retires the last of the S085 hero width

That ruling gave the trail and the banner 1104 so they would share an edge with
the logo, and it was correct while the page had a wide picture block to align to.
There is no wide block now, and Kain's newer ruling is the plainer one: one left
edge for the whole page. **DSRD 9 is owed the correction**, and so is the note in
this theme that describes the trail as the site-wide exception sitting at the
1200 frame.

## The picture is in the band twice, and that is deliberate

As the ground, washed almost out, and as an object at the right. The ground gives
the band its colour; the object gives the page its picture back, at a size that
suits a hero rather than the 680 by 810 it used to occupy above the writing.

**It carries alt="" in both places.** An article's picture is atmosphere, unlike
the book note's cover, and a screen reader announcing the same decorative image
twice is worse than not announcing it. Its authored alt still belongs to the
attachment and still reaches every place the picture is used as information.

## The band restates the reading bar's colours, and the page does not

The reading bar is a sealed component whose own head says a page can say what goes
in the bar and never what the bar is. So no argument was added and no colour was
passed in. The band restates the colours, exactly as it already does for the
shared breadcrumb in components.css, and for the identical reason: the component
is built for light grounds and the band is dark.

**Its hairline comes off inside the band.** That line marked where the article's
writing began, which is a boundary that exists on white and does not exist inside
a band: the band's own bottom edge is that line now, and a second one 24px above
it would be marking nothing.

## Four faults found by measuring, every one of them after the first deploy

Worth listing because all four passed a reading of the diff and none passed a
measurement of the page.

**The writer's name carries its own colour on its own selector.** Restating the
link's colour left the name at soft grey on a dark band. Legible enough to pass
unnoticed in a diff, close to unreadable on the page.

**The writing began on the band's bottom edge, at the same pixel.** The space
below used to come from the reading bar's own 48, and the bar had moved up into
the band, so nobody was supplying it. The body supplies it now, at 48, which is
Kain's standing measurement for the space under a line across the page.

**A fixed 320 track does not shrink.** At 768 the words were down to 336 against a
320 picture, and at 390 the text column computed to ZERO and the title vanished
entirely. The columns stack below 1024, picture below the words so the order heard
matches the order seen.

**The wider crop then did nothing at all.** The tag carries width and height
attributes, as every image on this site does so a browser can hold the space
before the file arrives, and those make both dimensions definite, which makes
`aspect-ratio` inert. The picture drew 350 by 320 where 16 by 9 had been asked
for. It needed `height: auto`. Caught by measuring the rendered element after the
eye said the shape looked wrong, which is the only reason it was caught at all.

## Measured after deploy

Trail, title, summary, writer line and body all start at 280 on desktop, 32 on
tablet and 20 on mobile, and the gate's own alignment row passes at all three.
Title still 33. No sideways scroll at 1440, 1152, 1024, 768 or 390. axe reports
zero WCAG AA violations. The two rows still failing are the two the book note
fails identically.

---

OWED BACK, adding to the list from the earlier ruling this sitting:

- **DSRD 9 section 22.3:** the trail sits on the reading column at 880, inside the
  band. The 1104 hero width is retired on this page.
- **DSRD 9 section 22.4:** the hero holds overline, title, standfirst, writer line
  and the article's picture.
- **DSRD 9 section 27:** its line that the breadcrumb is the exception on every
  page type, sitting at the 1200 frame, is now wrong for this page too. It was
  already reported wrong at S081 for a different reason.
- **DSRD 8:** the `kh-hero` entry gains that the band restates the colours of
  light-ground components placed inside it, which is now true of two of them.

*No em or en dashes in this file; checked before writing.*
