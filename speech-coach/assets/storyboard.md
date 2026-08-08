# Storyboard — [Title]

**Throughline:** [one sentence] · **Runtime:** ___ min · **Slides:** ___

*Stage 6 deliverable. This is a specification, not a deck. Hand it to the `pptx` skill, a
deck tool, a designer, or build it by hand.*

---

## Do we need slides?

**The test:** does any beat require the audience to *see* something — an image, the shape
of data, a live demo, a face, a physical comparison?

- [ ] **No** → recommend no slides, or one title card. This is a legitimate answer.
- [ ] **A few beats do** → slide only those. Blank the rest.
- [ ] **Most beats do** → full deck.

**Decision + reason:**

---

## The storyboard

| # | Beat | Time | What you SAY | What's ON SCREEN | Why this slide exists | Note |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

**Column rules**

- **SAY** — the gist in one line, not the script. Full words live in the script file.
- **ON SCREEN** — precise enough to build without asking. *"Full-bleed photo of the actual
  14-page onboarding form, shot flat on a desk"* — not *"image of paperwork."*
- **Why this slide exists** — **if you can't fill this in, delete the row.** This column is
  the entire point of the format.
- **Note** — build steps, `[BLANK — press B]`, demo cues, "hold 90 seconds."

---

## Headline audit

*Strip the deck to headlines and read them in order. They should tell the whole argument.
If they don't, the argument has a hole — you just found a narrative bug with a design check.*

| # | Headline | Assertion, or just a label? |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

*Labels are weak: "Q3 Churn." Assertions are strong: "Churn is concentrated in month two."*

---

## Design spec

| | |
|---|---|
| **Template / brand** | |
| **Aspect ratio** | 16:9 / 4:3 — *confirm against the actual projector* |
| **Type scale** | Headline ___ pt · Body ___ pt · **floor 24 pt** |
| **Colors** | |
| **Image sourcing** | *real photos from the actual work > stock, always* |
| **Data charts** | see `references/deck.md`; for palettes and chart types use the `dataviz` skill |

---

## Final checks

- [ ] One idea per slide. Anything needing an "and" is two slides
- [ ] Every headline is an assertion, not a label
- [ ] No slide repeats the speaker's words *(redundancy effect — it subtracts)*
- [ ] Every slide passes the glance test: 3 seconds to comprehend
- [ ] No slide is held under ~20 seconds
- [ ] Roughly 1 slide per 1–2 minutes for an argument-driven talk
- [ ] Readable from the back of the actual room
- [ ] Every "why this slide exists" cell is filled
- [ ] Blank screen (`B`) marked at the moments that need full attention
- [ ] Builds only where sequence carries meaning; no decorative animation
- [ ] PDF fallback exported

---

## Leave-behind

*A deck sparse enough to present is too sparse to read alone. A deck dense enough to read
alone is too dense to present. Decide explicitly — don't build a hybrid that fails at both.*

- [ ] Live deck only
- [ ] Live deck + separate written memo *(recommended when the read-alone version matters)*
- [ ] Live deck + appendix
- [ ] Density lives in speaker notes; export notes view

---

## Handoff

**Build with:** `pptx` skill / `ppt-master` / designer / by hand
**Template file:**
**Assets still needed:**
