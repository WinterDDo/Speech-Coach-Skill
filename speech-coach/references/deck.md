# Slides and the storyboard

Read this at Stage 6.

The output of this stage is a **storyboard** — a specification of what is said against what
is shown, slide by slide. It is not a deck file. Hand the storyboard to the `pptx` skill, a
designer, or the user's own hands. Keeping narrative separate from file production is
deliberate: the logic should survive a change of tool, a change of template, and a change
of mind about the software.

---

## First: do you need slides at all?

**The test.** Walk the beat sheet. Does any beat require the audience to *see* something —
an image, the shape of data, a live demo, a person's face, a physical comparison?

- **No beat does** → recommend no slides, or one title card. Say this out loud to the user
  as a real recommendation, not a joke. A speaker with nothing to click is more present,
  more mobile, and more listened to. Many of the best talks ever given had no visuals.
- **Two or three beats do** → those beats get slides. The rest get a held image or a black
  screen. You are not obligated to fill the gaps.
- **Most beats do** → build the deck, and apply everything below.

**The B key.** In most presentation software, pressing `B` blanks the screen to black. It
is the most underused control in the room. When you want every eye on you — the confession,
the ask, the close — blank it. Put `[BLANK — press B]` in the storyboard as a deliberate
instruction, not an accident.

---

## The governing relationship

> **You are the argument. The slide is the evidence.**

Everything follows from that. The slide is not your notes, not a handout, not a transcript,
and not a safety net. It exists to show the audience something your voice cannot carry.

There's a well-supported reason to keep them from duplicating each other: in multimedia
learning research (Richard Mayer's work is the standard reference), presenting narration
alongside *identical* on-screen text produces worse comprehension than narration alone —
the **redundancy effect**. Reading and listening compete for the same verbal channel. The
audience does one or the other, badly.

So a slide that repeats your sentence isn't neutral. It is actively subtracting.

---

## Rules for the slide itself

**One idea per slide.** If it needs an "and," it's two slides. Slides are free.

**Headline as an assertion, not a label.** This is the single highest-value change most
decks can make.

| Label (weak) | Assertion (strong) |
|---|---|
| "Q3 Churn" | "Churn is concentrated in month two" |
| "Market Overview" | "Two players hold 80% — and neither serves SMBs" |
| "Next Steps" | "We need two engineers by March 1" |

A reader who sees only your headlines should be able to follow the whole argument. Test
that: strip the deck to headlines and read them in order. If it doesn't hold together, the
argument doesn't either — and you found a *narrative* bug via a *design* check.

**Body text: two lines or none.** If you need a paragraph, you need to say it, not show it.

**The glance test.** Three seconds. Look at the slide, look away, say what it meant. If you
can't, the audience — who is also listening to you — certainly can't.

**Contrast and hierarchy.** Exactly one thing should be biggest. If everything is emphasized
(bold, colored, boxed, arrowed), nothing is. Decide what the eye lands on first and build
the slide around that decision.

**Whitespace is not waste.** It is what makes the one thing on the slide readable. The
instinct to fill space is the instinct that ruins decks.

**Font size floor.** Roughly 24pt for a room, larger for a big hall. The real test: stand
at the back of the actual room. If you can't read it there, it isn't on the slide. A useful
side effect — a 24pt floor makes it physically impossible to put a paragraph up.

**Images: full-bleed or not at all.** A small stock photo in a corner is decoration. A
full-frame image with a short line of text over it is a slide. Avoid generic stock
photography entirely — it reads as filler and costs credibility. Use real photographs of
real things from your actual work whenever you can get them.

---

## Data slides

Data slides fail more often than any other kind, and always in the same way: they show the
data instead of the point.

1. **One message per chart.** The chart answers one question. Two questions, two charts.
2. **The title states the message,** not the axes. "Revenue by region" tells them nothing.
   "Growth is entirely from two regions" tells them everything, and then the chart is proof
   rather than a puzzle.
3. **Annotate the point.** Circle it, arrow it, color that one series and gray the rest.
   Do not make the audience hunt while you talk — they will stop listening to search.
4. **Strip everything non-load-bearing.** Gridlines, borders, backgrounds, 3-D effects,
   legends that a direct label could replace, decimal places nobody needs. Tufte's
   data-ink principle: every drop of ink should carry information.
5. **Never put a spreadsheet on a slide.** If the table has more than about nine cells, it
   is a handout. Show the one row that matters, and offer the full table separately.
6. **Label directly.** Put series names next to the lines, not in a legend the eye has to
   travel to and back.

For anything beyond these basics — palettes, chart-type selection, accessible color — the
`dataviz` skill covers it properly.

---

## Builds and animation

Reveal in steps **only when the sequence carries meaning** — you're building a mechanism,
walking a timeline, or adding one variable at a time to a chart.

Never animate for interest. Fly-ins, spins, and dissolves cost credibility at a rate most
speakers underestimate, and they add unpredictable seconds under time pressure.

If a build has more than four steps, it's a slide sequence, not a build.

---

## The leave-behind problem

The most common structural mistake in business presentations: one artifact asked to be both
a live visual aid and a document people read alone afterward. Those requirements are
opposites. A slide dense enough to stand alone is too dense to present; a slide clean
enough to present says nothing on its own.

**Build two things.** A sparse deck for the room, and either a written memo or a
detailed appendix for after. It is more work and it is the correct answer. If the leave-
behind matters more than the live session, consider skipping slides entirely and writing
the memo — the Amazon approach — and using the room for discussion.

Where the user must have one artifact, put the density in the **speaker notes** and export
the notes view. That's the closest legitimate compromise.

---

## The storyboard format

Use `assets/storyboard.md`. One row per slide:

| # | Beat | Time | What you SAY | What's ON SCREEN | Why this slide exists | Note |
|---|---|---|---|---|---|---|

- **What you SAY** — one line, the gist, not the script. The full words live in the script.
- **What's ON SCREEN** — described precisely enough to build without asking: *"Full-bleed
  photo of the actual 14-page form, shot on a desk"* not *"image of paperwork."*
- **Why this slide exists** — if you can't fill this column, delete the row. This column is
  the whole point of the format; it is where redundant slides die.
- **Note** — build steps, `[BLANK]`, demo cues, "hold this slide for 90 seconds."

**Sanity checks on a finished storyboard:**

- Any slide whose "why" is "so there's something on screen" → cut it.
- Any slide where SAY and ON SCREEN are the same words → the redundancy effect; fix one.
- Any slide held for less than ~20 seconds → probably belongs merged with its neighbor.
  Rapid clicking reads as nervousness and fragments attention.
- Slide count sanity: roughly **one slide per 1–2 minutes** for argument-driven talks. A
  visual-heavy talk can run much faster. Forty text slides in twenty minutes is not a talk.

---

## Handoff

The storyboard is designed to be executed by something else:

- **`pptx` skill** — give it the storyboard plus any template, and ask for the file.
- **`ppt-master` / deck tools** — same input, different renderer.
- **A designer** — the "why this slide exists" column is exactly what they need and almost
  never get.
- **The user, by hand** — the storyboard is already the plan; they just build it.

Do not build the file from inside this skill. Narrative and production are different jobs,
and welding them together makes both harder to revise.
