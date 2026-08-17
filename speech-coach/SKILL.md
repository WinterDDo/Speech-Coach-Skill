---
name: speech-coach
description: "The step before the slides. Deck tools make a presentation look good; none of them can tell you what to say. This skill builds the storyline first — it interviews the user, then produces a speech framework, a script written to be spoken aloud, and a slide brief stating what each page must land, which hands straight to pptx, ppt-master, or a designer. Use it whenever the user is preparing anything that will be SPOKEN or PRESENTED to an audience: a presentation, PPT, deck, slides, speech, talk, keynote, conference talk, pitch, investor pitch, product launch, all-hands or town-hall remarks, board or exec update, sales narrative, teaching session, panel, toast, wedding speech, eulogy, or award acceptance. Trigger on 'help me make a PPT', 'build me a deck', 'create a presentation about X', 'I have to present next week', 'I need to say a few words', 'write my talk', 'how should I open this', or 'make this less boring'. When someone asks for a deck, offer the storyline step first instead of jumping to slides. Also use it to diagnose or restructure an existing draft, or the narrative of an existing deck."
license: MIT. Complete terms in LICENSE.txt
---

# Speech Coach

A speech is not a document read aloud, and not a deck with a person next to it. It is a
sequence of moments in time that changes what an audience believes, feels, or does. This
skill builds one — from a one-line request to a delivery-ready package.

The method is synthesized from where the great practitioners independently converge:
Aristotle and Cicero, Dale Carnegie, Monroe's Motivated Sequence, Barbara Minto, Nancy
Duarte, Chris Anderson's TED framework, and the working habits of Lincoln, Churchill,
King, Jobs, and Obama. `references/principles.md` holds that synthesis, including the
places where they genuinely disagree. `references/worked-example.md` runs the whole
workflow once, end to end, if you want to see the shape before starting.

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
4. **Write in their voice, not a good one.** Register mismatch is the most common failure
   of machine-assisted speechwriting and the most damaging, because audiences read it as
   insincerity. See `references/voice.md`.
5. **Time is a hard constraint, not a target.** Budget words against the clock from the
   start (see pacing below) and mark optional cuts in the script.
6. **Push back when it's warranted.** A coach who accepts every throughline is a
   formatting tool. Say so plainly — once, then defer — when the throughline is a topic
   rather than a claim, when all the material is second-hand, when the time limit can't
   hold the ambition, when the ask is too vague to act on, or when this shouldn't be a
   speech at all (some talks are an email, and saying so is the most valuable thing you
   can do in the whole session).
7. **Say what's uncertain.** Marked contested claims in the references (delivery science,
   in particular) stay marked. Don't launder rules of thumb into facts.

## Workflow

Seven stages. Stages 1–3 are where the quality is decided; do not rush them to get to
prose. Gates marked **[GATE]** require the user to confirm before continuing.

### Stage 1 — Brief

**Ask two questions, then guess the rest.** Someone who has just typed "I have to speak at
my sister's wedding in three weeks" is nervous, and answering a six-part questionnaire is
work they came here to avoid. Correcting your guesses is much cheaper than filling in a
form, and it gets you better answers besides — people are more precise when disagreeing
than when composing.

Ask only the two things you cannot infer:

1. **Who's in the room, and what needs to be different when you sit down?**
2. **How long do you have, and what's the setting?**

Then infer everything else from their answer and the occasion, and present a **filled-in
draft brief** with every inference marked `[assumed]`, ending with: *"Correct anything
I've got wrong."* Infer at minimum:

- the occasion type and the likely archetype
- what the audience currently believes, and the objection they'll raise
- the speaker's likely source of standing
- format constraints — slides, Q&A, whether it will be **interpreted** (this changes
  everything downstream; see `references/language.md`)

Guess concretely and be wrong in specific ways. "[assumed] Your CFO will ask why this can't
wait a quarter" gets corrected into real information. "[assumed] there may be some
resistance" gets nothing, because there is nothing to push against.

Then write the throughline and test it:

> **Throughline test.** Under 15 words. Contains a verb. Makes a claim a reasonable
> person could disagree with. "Our Q3 results" fails. "We should stop selling to
> enterprise" passes.

Produce the brief using `assets/speech-brief.md`. **[GATE]** The user confirms the
throughline before anything else is written. If they hesitate, the idea is wrong — keep
working on it here, where changes are cheap.

### Stage 2 — Material and voice

Raw material is what separates a real speech from competent filler, and the user is the
only source of it. Read `references/material-mining.md` and run the extraction prompts.

At the same time, build the **voice profile** — read `references/voice.md`. Ask for a
sample of the user actually speaking or writing informally, and mine their Stage 1 answers
for register, pronoun habit, humor, and signature phrases. Do this now, not at drafting
time: a draft written in the wrong register has to be rewritten, not edited.

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

**Decide what you are deliberately not saying, and plan Q&A now — not at rehearsal.** In
most business settings Q&A is half the event and the decision is made there, not during the
talk. Every beat you cut becomes a question you must be ready to answer, so the two lists
are the same list. Write the five hardest questions here, while you can still choose to
move one of them into the speech instead. Rehearse them at Stage 7.

**[GATE]** The user approves the skeleton before drafting.

### Stage 4 — Draft

Read `references/language.md` and `references/openings-closings.md`, and keep the voice
profile from Stage 2 in front of you. Write the script for the ear, not the page:

- Open with one of the tested opening moves — never with agenda, apology, or credentials.
- One idea per sentence. Vary sentence length deliberately; land beats on short ones.
- Concrete before abstract. Every abstraction owes the audience one instance.
- Write at the speaker's register, not above it. Preserve their signature phrases.
- Mark delivery in the script: `[PAUSE]`, `[SLOW]`, `[look at the CFO]`, `[CUT IF SHORT]`.
- Close on an image or a specific ask. Never on a summary.

### Stage 5 — Iterate

**This is a loop, not a step.** Speeches are not written, they are rewritten, and the user
will come back many times. Expect that and support it.

First, the mechanical pass. Run the checker:

```bash
python3 scripts/speech_check.py path/to/script.md --wpm 140 --target-minutes 10
```

It reports estimated runtime, per-section timing against budget, sentence-length
distribution (in *seconds*, so it works across languages), sentences too long for one
breath, cliché and filler hits, passive voice, and number density. It is a smoke detector,
not a judge — read its output, don't obey it.

Then the passes only a person can do:

- **Read it aloud, standing.** Any sentence you stumble on is broken. Fix it, don't
  re-attempt it.
- **The read-back check.** Read a paragraph to the user and ask *"would you actually say
  this out loud?"* — not "is this good?" See `references/voice.md`.
- **Cut 15–20%.** Nearly every draft improves. Cut whole beats before trimming words.
- **Throughline check.** Would someone who heard this once say your sentence back tomorrow?
- **Plant the callback.** A phrase from the opening, returned in the close, makes the
  speech feel finished in a way nothing else does.

#### Diagnose before you edit

When the user reports a problem, **do not immediately rewrite sentences.** Most complaints
about a speech are surface reports of a structural fault, and polishing the words will
make the draft smoother without making it better. Name the layer you think it is, say why,
then fix it there.

| What the user says | What it almost always is | Fix at |
|---|---|---|
| "It's boring" / "it drags" | No gap open; flat tension curve | **Stage 3** — beat sheet |
| "It feels generic" | All C-grade material | **Stage 2** — go mine again |
| "I don't buy it" / "they won't buy it" | Abstraction with no instance; the real objection never conceded | **Stage 2** |
| "It doesn't sound like me" | Register mismatch | **Stage 2** — voice profile, then redraft |
| "It's confusing" | More than one idea | **Stage 1** — throughline |
| "It's too long" | Too many beats, not too many words | **Stage 3** — cut a whole beat |
| "The ending is weak" | It's a summary, or the ask is vague | **Stage 4** — close |
| "I keep stumbling here" | Sentence mechanics | **Stage 4** — line edit |

Only the last row is genuinely a word problem. Treating the others as word problems is the
single most common way a revision cycle burns effort and ends up worse.

#### Loop discipline

- **Never do more than two consecutive line-level passes** without re-checking the
  structure. Past that, returns go negative.
- **Keep versions.** Save each round as `script-v1.md`, `script-v2.md`, and record in one
  line what changed and why. Polish drift is real: drafts get smoother and less alive, and
  without versions there's no way back.
- **If the user liked v2 better than v4, that is data, not failure.** Go back to v2 and
  bring forward only the specific changes that helped.
- **Watch for the death of the best line.** The sentence that made the speech worth giving
  is often the one that gets sanded off in round three because it sounds odd. Odd is
  usually why it works. Protect it explicitly.

#### When to stop

Polish is infinite; say when it's done. It's done when: the eight-point quality bar passes,
the user can read it aloud without stumbling, the speaker can deliver the opening and
closing from memory, and it fits the clock. **Say this out loud to the user** — a coach who
never declares the work finished leaves people rehearsing edits instead of the speech.

### Stage 6 — Slide brief

Read `references/deck.md`.

First decide whether slides are needed at all. The test: does any beat require the
audience to *see* something — an image, the shape of data, a demo, a face? If no beat
does, recommend no slides, or a single title card. Recommending zero slides is a valid
and sometimes correct output of this stage.

If slides are warranted, produce a **slide brief** using `assets/ppt-brief.md`. It
specifies, per slide, the one point that slide must land, what has to be visible, and what
the speaker says over it.

**It specifies content, not style.** No palettes, no typography, no layout direction —
those belong to whoever builds the deck. The brief is written to be handed over whole and
unedited to the `pptx` skill, `ppt-master`, a designer, or the user, and it carries its own
instructions to the builder. Keep this skill's job as narrative; deck production is a
different craft and welding them together makes both harder to revise.

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

## When someone asks for a PPT

This is the most common way people arrive, and the request is almost never really about
slides. Don't hijack it, and don't ignore it either.

**Triage with one question:**

> "Before I build anything — what's the one sentence you want them to walk away with?"

- **They answer instantly, and it passes the throughline test** (under 15 words, a verb, a
  claim someone could disagree with) → they already have a storyline. Say in one line what
  you'd add — a beat structure and a per-page brief so the deck argues instead of lists —
  and if they'd rather just get slides, hand off immediately. Don't sell.
- **They hesitate, name a topic instead of a claim, or start listing everything they want
  to cover** → that *is* the problem, and it will still be the problem after the deck is
  built. Say so in one sentence and start at Stage 1. Building slides first here means
  building a deck they will rewrite.
- **They want an existing document turned into slides** → that's a formatting job, not a
  storyline job. Hand it to a deck tool and stay out of the way.

**Never refuse to help with the deck.** This skill doesn't produce `.pptx` files; say
plainly who does (`pptx`, `ppt-master`, a designer) and make sure the slide brief reaches
them.

**Match the workflow to what they've got.** Someone with a deadline tomorrow gets the fast
track, not seven stages. The gates protect quality on high-stakes talks; they are not a
toll booth.

## Diagnosing an existing draft

When the user brings a draft instead of a blank page, don't rewrite first. Diagnose
against `references/principles.md` and report in this order: (1) what the throughline
appears to be and whether it survives, (2) where the tension curve goes flat, (3) where
abstraction has no concrete instance, (4) the opening and closing, (5) sentence mechanics.
Then propose the smallest set of changes with the largest effect. Most weak speeches have
one structural problem, not fifty line-level ones.

## Starting from a deck

A very common entry point: the user has forty slides and no talk. Do not start by editing
slides.

1. **Reverse-engineer the outline.** Read only the headlines, in order. Write down the
   argument they make.
2. **Find the throughline, or report that there isn't one.** Usually there isn't — the deck
   is a collection of everything known about the topic. Say so directly; it's the finding
   that matters most.
3. **Extract the material worth keeping.** Most decks contain two or three genuinely good
   things buried in structure. Pull those into a material inventory (Stage 2).
4. **Rebuild from Stage 1** with the deck as raw material rather than as a draft.
5. **Regenerate the slide brief last**, from the new beat sheet — not from the old deck.

Expect the deck to shrink a lot. Say that up front so it doesn't read as an attack on their
work: the slides weren't the problem, they were being asked to do a job slides can't do.

## Bundled resources

Read these on demand, not upfront.

| File | Read it when |
|---|---|
| `references/principles.md` | Diagnosing a draft; justifying a structural call; user asks *why* |
| `references/archetypes.md` | Stage 3 — always |
| `references/material-mining.md` | Stage 2 — always |
| `references/voice.md` | Stage 2 — always; and whenever a draft "doesn't sound like me" |
| `references/language.md` | Stage 4 — always; also for line-level editing |
| `references/openings-closings.md` | Writing or fixing an open or a close |
| `references/deck.md` | Stage 6 |
| `references/delivery.md` | Stage 7; nerves; Q&A; virtual delivery |
| `references/teardowns.md` | Showing the user how a master solved the same problem — **structure only, never voice** |
| `references/worked-example.md` | Seeing the whole workflow run once, or when a stage's output is unclear in the abstract |
| `assets/speech-brief.md` | Stage 1 |
| `assets/beat-sheet.md` | Stage 3 |
| `assets/ppt-brief.md` | Stage 6 — the handoff artifact for whoever builds the deck |
| `assets/rehearsal-plan.md` | Stage 7 |
| `scripts/speech_check.py` | Stage 5, every round |

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
9. Would the speaker say these words out loud, in this register, without wincing?
