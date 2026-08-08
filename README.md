# Speech Coach

An agent skill that takes a rough idea and walks a person to a delivery-ready piece of
public speaking: a **framework**, a **script written for the ear**, and a **slide-by-slide
storyboard**.

A speech is not a document read aloud, and not a deck with a person standing next to it.
It's a sequence of moments in time that changes what an audience believes, feels, or does.
Most speaking advice is a list of tips. This is a workflow, with gates, built on what the
best practitioners independently converged on.

---

## What it produces

| Stage | Deliverable |
|---|---|
| 1. Brief | A one-page brief: throughline, the audience delta, the room, the constraints |
| 2. Material | An inventory of the speaker's real stories, numbers, people, and scars |
| 3. Architecture | A beat sheet with time budgets and a visible tension curve |
| 4. Draft | A script written for the ear, with pause marks and pre-planned cuts |
| 5. Sharpen | A mechanical check plus the read-aloud passes only a human can do |
| 6. Storyboard | What is *said* against what is *shown*, slide by slide — or a recommendation to use no slides |
| 7. Rehearsal | Pause map, timing checkpoints, the five hardest questions, contingencies |

---

## Install

```bash
git clone https://github.com/WinterDDo/Speech-Coach-Skill.git
cp -r Speech-Coach-Skill/speech-coach ~/.claude/skills/
```

Or for one project only, copy it into `.claude/skills/` in the repo.

Then just describe what you have to say:

> "I have to present our Q3 numbers to the board in ten minutes and I need them to approve
> two more engineers."

> "My sister's wedding is in three weeks and I'm the best man."

> "Here's my draft — it's boring and I don't know why."

The skill triggers on speeches, talks, keynotes, pitches, all-hands remarks, launches,
toasts, eulogies, panels, and on "help me with my slides."

---

## The method

Seven stages, but three ideas do most of the work.

**Structure is decided before prose.** Stages 1–3 are where quality is determined. The
skill will not write sentences until you've approved a throughline and a skeleton, because
revising prose built on a broken structure wastes your time and produces a polished version
of the wrong speech.

**It will not invent your life.** The single most valuable thing in any speech is material
only you have — the night the line went down, the customer who said the thing, the number
that surprised you. A language model can supply structure, rhythm, and craft; it cannot
supply those, and this skill is built to ask rather than fabricate. Where personal material
is missing, it writes a labeled placeholder instead of a plausible lie. A speaker who
discovers on stage that their own anecdote isn't true has been harmed, not helped.

**Different occasions need different skeletons.** Ten archetypes, selected by what the
audience actually has to *do* in the room. Using a TED shape for a board update is a common
and expensive mistake.

---

## What's inside

```
speech-coach/
├── SKILL.md                      the workflow, gates, and quality bar
├── references/
│   ├── principles.md             what the masters share — and where they disagree
│   ├── archetypes.md             10 occasion-specific skeletons with beat sheets
│   ├── material-mining.md        extracting the speaker's real material
│   ├── language.md               writing for the ear: rhythm, diction, devices, ban list
│   ├── openings-closings.md      7 openings and 6 closings that work, and what never does
│   ├── deck.md                   slides, data, and the storyboard spec
│   ├── delivery.md               rehearsal, nerves, Q&A, virtual, recovery
│   └── teardowns.md              5 canonical speeches, structurally dismantled
├── assets/                       fill-in templates for each deliverable
└── scripts/
    └── speech_check.py           runtime, pacing, sentence length, cliché detection
```

The checker is stdlib-only Python 3.8+, no dependencies:

```bash
python3 speech_check.py draft.md --wpm 140 --target-minutes 10
```

It measures runtime against budget, per-section pacing, sentences too long for one breath
(in *seconds*, so it works across languages), cliché and filler density, passive voice, and
number density. It's a smoke detector, not a judge.

---

## Where the method comes from

Aristotle's *Rhetoric* and Cicero's five canons. Dale Carnegie on earning the right to
speak. Monroe's Motivated Sequence. Barbara Minto's Pyramid Principle. Nancy Duarte's
work on narrative tension. Chris Anderson's TED framework. The Heath brothers on
concreteness, and Paul Slovic's research on why one named person outperforms a statistic.
Churchill's own 1897 essay on the mechanics of rhetoric.

And the practice of Lincoln, Churchill, King, Jobs, and Obama — five speeches taken apart
in `references/teardowns.md`, including what *not* to copy from each.

Where the popular advice is shakier than its confidence suggests — the "7-38-55 rule,"
power posing — the skill says so rather than repeating it.

---

## Status and roadmap

**v1, English.** The framework is the priority; the language layer comes next.

- [ ] Multilingual versions. The architecture anticipates this: the laws are portable, the
      *conventions* are not, so each language gets its own rhetoric toolkit and cliché list
      rather than a translation. `principles.md` already flags where the Anglo-American
      canon doesn't travel — directness of the ask, self-deprecation, conclusion-first
      ordering, personal disclosure. The checker already handles CJK pacing and sentence
      segmentation.
- [ ] More teardowns, drawn from outside the Anglo-American canon.
- [ ] Worked end-to-end examples per archetype.

Issues and pull requests welcome.

## License

Not yet chosen — see the note in the repository discussion. Until one is added, default
copyright applies.
