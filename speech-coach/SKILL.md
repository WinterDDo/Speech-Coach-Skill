---
name: speech-coach
description: "Turn a rough idea into a finished piece of public speaking: a structured framework, a script written for the ear, and a slide-by-slide storyboard. Use this skill whenever the user needs to prepare anything that will be SPOKEN to an audience — a speech, talk, keynote, presentation, pitch, conference talk, all-hands or town-hall remarks, investor pitch, product launch, sales narrative, board or exec update, teaching session, panel appearance, toast, wedding speech, eulogy, award acceptance, or commencement address. Trigger even when the user only says things like 'I have to present next week', 'I need to say a few words', 'help me with my slides', 'write my talk', 'how should I open this', or 'make this sound less boring'. Also use it to diagnose, restructure, or tighten a draft speech or the narrative of an existing deck."
---

# Speech Coach

A speech is not a document read aloud, and not a deck with a person next to it. It is a
sequence of moments in time that changes what an audience believes, feels, or does. This
skill builds one — from a one-line request to a delivery-ready package.

The method is synthesized from where the great practitioners independently converge:
Aristotle and Cicero, Dale Carnegie, Monroe's Motivated Sequence, Barbara Minto, Nancy
Duarte, Chris Anderson's TED framework, and the working habits of Lincoln, Churchill,
King, Jobs, and Obama. `references/principles.md` holds that synthesis, including the
places where they genuinely disagree.

## Operating rules

These are hard constraints, not preferences.

1. **Never invent the speaker's life.** Do not fabricate anecdotes, people, numbers, or
   experiences and present them as the user's. If a beat needs a personal story that
   hasn't been supplied, write `[YOUR STORY HERE — needs: a moment when X happened to
   you, ~40 seconds]` and keep going. A speaker who discovers on stage that their own
   story isn't true has been actively harmed. This rule outranks completeness.
2. **No prose before the skeleton is approved.** Drafting an unapproved structure wastes
   the user's revision budget on sentences that are about to be deleted.
3. **One idea.** If the throughline can't be said in one sentence under 15 words, the
   speech isn't ready to be written. Fix the idea, not the wording.
4. **Time is a hard constraint, not a target.** Budget words against the clock from the
   start (see pacing below) and mark optional cuts in the script.
5. **Say what's uncertain.** Marked contested claims in the references (delivery science,
   in particular) stay marked. Don't launder rules of thumb into facts.

## Workflow

Seven stages. Stages 1–3 are where the quality is decided; do not rush them to get to
prose. Gates marked **[GATE]** require the user to confirm before continuing.

### Stage 1 — Brief

Ask these six questions in a single batch. Tell the user that "I don't know" is a valid
answer to any of them and you'll help work it out.

1. **The room.** Who's in the audience, how many, and what's their relationship to you?
2. **The container.** How long, what format (stage / boardroom / video call / no slides
   allowed), and where in the agenda?
3. **The delta.** What must be different when you sit down — what do they think, feel, or
   do that they didn't before?
4. **The resistance.** What do they currently believe or feel about this? What's the
   objection you're most afraid of?
5. **Your standing.** Why you and not someone else? (Lived it / studied it / accountable
   for it.)
6. **The rails.** Anything you must include, must not say, or must be careful about?

Then write the throughline and test it:

> **Throughline test.** Under 15 words. Contains a verb. Makes a claim a reasonable
> person could disagree with. "Our Q3 results" fails. "We should stop selling to
> enterprise" passes.

Produce the brief using `assets/speech-brief.md`. **[GATE]** The user confirms the
throughline before anything else is written. If they hesitate, the idea is wrong — keep
working on it here, where changes are cheap.

### Stage 2 — Material

Raw material is what separates a real speech from competent filler, and the user is the
only source of it. Read `references/material-mining.md` and run the extraction prompts.

**[GATE]** Do not proceed to Stage 3 with fewer than **two concrete, first-hand items**
(a named person, a scene, an object, a scar, a number that surprised the speaker). If the
user can't supply them right now, say plainly what the draft will be missing, then
proceed with clearly marked placeholders.

### Stage 3 — Architecture

Read `references/archetypes.md`. Select the structural archetype that fits the occasion —
different occasions need genuinely different skeletons, and using a TED shape for a board
update is a common and expensive mistake.

Produce a beat sheet using `assets/beat-sheet.md`: every beat gets a purpose, a time
budget, the material it uses, and a **stake level (1–5)** so the tension curve is visible
as a shape. A flat curve is the most common structural defect; look for it explicitly.

Pacing (rule of thumb — have the user calibrate by reading 200 words aloud and timing it):

| Register | Words/min | 5 min | 10 min | 18 min |
|---|---|---|---|---|
| Conversational / demo | 150–165 | ~800 | ~1,600 | ~2,900 |
| Standard prepared talk | 135–150 | ~700 | ~1,400 | ~2,500 |
| Formal / ceremonial / emotional | 110–130 | ~600 | ~1,200 | ~2,100 |

Budget to **85% of the time limit**. Every speech runs long live.

**[GATE]** The user approves the skeleton before drafting.

### Stage 4 — Draft

Read `references/language.md` and `references/openings-closings.md`. Write the script for
the ear, not the page:

- Open with one of the tested opening moves — never with agenda, apology, or credentials.
- One idea per sentence. Vary sentence length deliberately; land beats on short ones.
- Concrete before abstract. Every abstraction owes the audience one instance.
- Mark delivery in the script: `[PAUSE]`, `[SLOW]`, `[look at the CFO]`, `[CUT IF SHORT]`.
- Close on an image or a specific ask. Never on a summary.

### Stage 5 — Sharpen

Run the checker:

```bash
python3 scripts/speech_check.py path/to/script.md --wpm 140 --target-minutes 10
```

It reports estimated runtime, per-section timing against budget, sentence-length
distribution, unspeakably long sentences, cliché and filler hits, and number density.
It is a smoke detector, not a judge — read its output, don't obey it.

Then do the passes that only a reader can do:

- **Read it aloud.** Any sentence you stumble on is broken. Fix it, don't excuse it.
- **Cut 15–20%.** Nearly every draft improves. Cut whole beats before trimming words.
- **Throughline check.** Would someone who heard this once say your sentence back tomorrow?
- **Plant the callback.** A phrase from the opening, returned in the close, makes the
  speech feel finished in a way nothing else does.

### Stage 6 — Storyboard

Read `references/deck.md`.

First decide whether slides are needed at all. The test: does any beat require the
audience to *see* something — an image, the shape of data, a demo, a face? If no beat
does, recommend no slides, or a single title card. Recommending zero slides is a valid
and sometimes correct output of this stage.

If slides are warranted, produce a storyboard using `assets/storyboard.md` — one row per
slide, mapping what is *said* against what is *shown*, plus why that slide exists. The
storyboard is a specification, not a deck. Hand it to the `pptx` skill, a deck tool, or a
designer to build. Keep this skill's job as narrative, not file production.

### Stage 7 — Rehearsal

Read `references/delivery.md`. Produce a rehearsal plan using `assets/rehearsal-plan.md`:
what to memorize verbatim (opening and closing only), the pause map, the timing
checkpoints, the pre-planned cuts if running long, the five hardest questions with PREP
answers, and the room/tech checklist.

## Fast track

For low-stakes or very short asks — a two-minute toast, a stand-up update, "how do I open
this" — don't run seven stages. Ask questions 1–3 from the brief, pick an archetype, and
deliver a beat sheet plus draft in one pass. Offer the full workflow if the stakes turn
out to be higher than the phrasing suggested.

## Diagnosing an existing draft

When the user brings a draft or a deck instead of a blank page, don't rewrite first.
Diagnose against `references/principles.md` and report in this order: (1) what the
throughline appears to be and whether it survives, (2) where the tension curve goes flat,
(3) where abstraction has no concrete instance, (4) the opening and closing, (5) sentence
mechanics. Then propose the smallest set of changes with the largest effect. Most weak
speeches have one structural problem, not fifty line-level ones.

## Bundled resources

Read these on demand, not upfront.

| File | Read it when |
|---|---|
| `references/principles.md` | Diagnosing a draft; justifying a structural call; user asks *why* |
| `references/archetypes.md` | Stage 3 — always |
| `references/material-mining.md` | Stage 2 — always |
| `references/language.md` | Stage 4 — always; also for line-level editing |
| `references/openings-closings.md` | Writing or fixing an open or a close |
| `references/deck.md` | Stage 6 |
| `references/delivery.md` | Stage 7; nerves; Q&A; virtual delivery |
| `references/teardowns.md` | Showing the user how a master solved the same problem |
| `assets/*.md` | Templates for each deliverable |
| `scripts/speech_check.py` | Stage 5 |

## Quality bar

Before handing anything over, check all eight. Any "no" is rework, not a caveat.

1. Can the throughline be said in one sentence under 15 words, and does the whole speech serve it?
2. Is there a real gap — a problem, tension, or question — open within the first 60 seconds?
3. Has the speaker's standing been established early, from their own experience?
4. Does every abstraction have at least one concrete instance attached?
5. Does the stake level move? Is there an actual shape, not a flat line?
6. Does it end on an image or a specific ask, not a recap?
7. Does it fit in 85% of the time limit, at the speaker's measured rate?
8. Is every personal detail either supplied by the user or explicitly marked as a placeholder?
