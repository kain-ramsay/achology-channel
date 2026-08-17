# Plan for Chat — Testimonials (video) page structure (agreed with Kain, 2026-07-24)

From: Claude Code. Kain and I worked through the testimonials-page structure in a
Code session and agreed the proposal below. Per our standing rule, planning docs
live with you: please take this as the canonical testimonials-page plan, document
it in your structure, and Kain will pick it up with you next session. NOTHING is
built. Structure only.

## Not the reviews page
- **Testimonials page** = prerecorded member videos (this doc).
- **Reviews page** = 4,517 written reviews (separate plan already filed).
Testimonials is intentionally NOT a CPT.

## Purpose (locked)
On-site trust and conversion: the highest-trust human proof, real faces and voices,
the page you point a hesitating visitor to and that course/sales pages link out to.
NOT a search-traffic play like reviews. It still earns strong SEO/GEO as a bonus
(video schema + transcripts + first-hand E-E-A-T), but that is upside, not the job.

## The source data (canonical = Notion)
Notion database **"Testimonial Videos"** under the Achology Review Bank.
- Database id: `9beec85f-6eaf-49e5-be77-273b19351632`
- Data source: `collection://9dd00b95-98b2-482f-b248-29011f310ddc`
- **46 videos total. All have Vimeo URLs** (live in Notion; treat Notion as the
  single source of truth, don't copy the 46 URLs around).
- **10 members, each answering the same 5 questions on camera** (9 answered all 5;
  Max answered Q4 only). None flagged "Featured" yet.
- Members + countries: Alec Wells (Scotland, UK), Andrew "Andy" Nelson (Chile),
  Beatriz "Bea" Fernández García (Netherlands), Brian Boyle (Northern Ireland, UK),
  Derek Seller (England, UK), Jonathan "Jon" Frost (England, UK), Max Winner
  (England, UK), Peter Welch (England, UK), Sarah Furnell (Italy), Stacy Anderson
  (England, UK).

## The five questions (the spine, verbatim)
- Q1: How have you benefited from studying Achology training courses?
- Q2: What is the main lesson you've learned that's added most value to your life?
- Q3: What value have you found in studying within a collaborative peer-learning environment?
- Q4: What would you say to anyone who's thinking about studying with Achology?
- Q5: What are the 5 things you value most about the Achology community?

## The proposal (agreed)
1. **Framing intro** — short, confident: real Achology members, unscripted, each
   answering the same five honest questions. The lack of scripting IS the point.
2. **One hero video opens the page** — an immediate real face + voice. (Which video
   leads is an open pick; "Featured" flag is currently unused.)
3. **Spine = the five questions.** Five sections, each headed by the actual
   question, each showing the members answering it. **Lead with Q4** ("what would
   you say to someone thinking about studying with Achology?") — it's the exact
   question in a hesitating visitor's head, and ten real people answering it in
   turn is the most persuasive thing on the site. Convergence closes doubt.
4. **Each video shows its person: name + country.** Country IS shown here (unlike
   the reviews page, where per-item country was dropped) because this is real,
   consented data these named people gave on camera. The international spread is an
   asset ("people like you, everywhere").
5. **Transcripts beneath each video** — the real spoken words, pulled from the
   audio. This is the SEO/GEO engine and an accessibility win. It makes the page
   the definitive answer to "what is Achology like / is it worth it," which is what
   people type and what LLMs cite.
   - **Deliberately NOT a mini-article per video.** 46 short texts of 10 people
     answering the same 5 questions = thin, near-duplicate content that Google
     penalises. The transcript lives as supporting text on the one rich page.
6. **Schema:** VideoObject per video (title, transcript, thumbnail, uploadDate,
   embed) — clean video markup + real transcribed experience is exactly what
   Google rewards on this page type. Plumbing mirrors the About videos
   (Vimeo, click-to-play so the page stays fast). Code's domain.

## The bonus (optional, later)
Once transcripts exist, we're one step from **ten substantial per-person "member
story" articles** (each weaving that member's 5 answers into one rich, unique
piece). Ten strong articles, NOT 46 thin ones. The page is complete without them;
the door is simply open.

## Open items (for build / Kain)
- Pick the hero video + any "Featured" ones.
- Prove the transcript pipeline on ONE video before scaling to 46 (Vimeo may
  already hold auto-transcripts; else transcribe the audio). Code to verify.
- Confirm section order (recommend Q4 first, then Q1, Q2, Q3, Q5).
- Decide if/when to build the 10 per-person story articles.
- How the video data gets into the theme at build (Notion remains source of truth;
  likely an export step like the reviews CSV).

## What I need from you
Document this as the canonical testimonials-page plan and hold the open items for
Kain next session. Ping the channel if you want anything verified — I have the
Notion data and live WP-CLI access to the build site.
