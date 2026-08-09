# A worked example, end to end

Read this when you want to see the whole workflow run once, or when a stage's output is
unclear in the abstract.

> ### This example is constructed
>
> Priya, Marcus, the company and its numbers are **invented for teaching purposes**. They
> are not a real speech and nothing here should be reused as if it happened.
>
> This matters more than the usual disclaimer, because the skill's first operating rule is
> never to invent a speaker's experience. That rule is about *the user's* material. A
> labeled teaching example is a different object — but if any of this ever ends up inside a
> real user's draft, the rule has been broken.
>
> **In a real session, everything in Stage 2 comes from the user's mouth.** That is the
> entire difference between this and a template.

---

## The request

> **User:** "I've got 8 minutes at the leadership offsite Thursday to ask for engineering
> headcount. I have a deck already but it's not landing."

Two signals worth catching immediately: there's a **deck already** (so this is the
deck-first entry path — reverse-engineer, don't edit), and *"not landing"* is a diagnosis
the user has already made without knowing the cause.

---

## Stage 1 — Brief

**Asked two questions:**

> Who's in the room, and what needs to be different when you sit down?
> How long do you have, and what's the setting?

> **User:** "Eleven people — exec team plus the two founders. CEO and CFO are the ones who
> decide. I need them to approve two engineers on loan to my team. Eight minutes, boardroom,
> I'm fourth on the agenda after the revenue review."

**Everything else was inferred and handed back for correction:**

| Field | Draft | |
|---|---|---|
| Occasion | Internal proposal for resources | `[assumed]` |
| Archetype | Persuasive Case — they must decide, so Need has to be built | `[assumed]` |
| What they believe now | Ops asking for headcount again; every function wants engineers | `[assumed]` |
| The objection | *"Why can't this wait a quarter?"* — from the CFO | `[assumed]` |
| Standing | Accountable for it — it's your function | `[assumed]` |
| Position risk | Fourth after the revenue review; the room will be tired and financially framed | `[assumed]` |
| Interpreted | No | `[assumed]` |

> **User's corrections:** "Objection is right but it comes from the CTO, not the CFO — his
> engineers get borrowed constantly and he's protective. CFO's objection is different, she'll
> want to know why we can't hire contractors. And I'd say I'm not just accountable, I
> approved the thing that caused this."

That last sentence is the most valuable thing in the exchange, and it only appeared because
there was a wrong guess to push against. A blank "what's your standing?" would not have
produced it.

### The throughline

**Attempt 1:** *"Customer Operations needs more engineering support."*

Fails the test. It has no verb doing real work, nobody in the room disagrees with it in
principle, and it frames the talk as a department asking for something — which is exactly
the frame the CTO will resist.

**Attempt 2:** *"We're paying twelve people to do what one tool could do."*

Eleven words. Real verb. Genuinely disputable — the CTO can and will argue the tool won't
work. That's the sign of a live throughline: **it gives the room something to disagree
with**, which means it gives them something to decide.

---

## Stage 2 — Material and voice

Four questions from `material-mining.md`, and what came back:

| Prompt | Answer | Grade |
|---|---|---|
| When did you get this wrong? | "I approved the manual process two years ago as a temporary fix." | **A** — a scar, first-hand, and it disarms the "Ops wants more" frame |
| One specific person affected? | "Marcus, support lead. Maintains a 40-tab spreadsheet by hand, every week." | **A** — named, concrete, sympathetic |
| The number that surprised *you*? | "I audited it. Thirty-one percent of my team's hours go to reconciliation. I expected bad, not that." | **A** — surprised the speaker, which is why it will surprise the room |
| Anything you could hold up? | "Marcus printed the spreadsheet for me when I asked how bad it was." | **A** — a physical object |

Four A-grade items. That's a rich session; two would have been enough to pass the gate.

**Voice profile**, extracted from how she answered rather than from a separate interview:

| Dimension | Priya |
|---|---|
| Sentence length | Short. Clipped. |
| Register | Professional plain, unadorned |
| Pronoun | "my team" / "we" — rarely "I," except to take blame |
| Humor | Dry, sparse |
| Figurative language | None. Stays literal |
| Directness | States numbers plainly, states the ask plainly |
| Signature | "I want to be clear about that" |

**Consequence for drafting:** no metaphors, no rising cadence, no tricolons for their own
sake. The teardowns in `teardowns.md` are the wrong model for this speaker — a Churchillian
peroration in a boardroom from someone who talks like this would read as a performance, and
this room's trust in her is her main asset.

---

## Stage 3 — Architecture

**Archetype:** Persuasive Case (`archetypes.md` §1). The room's job is to decide, so Need
must be built before the solution appears.

**Beat sheet** — first pass, with the problem visible in the stake column:

| # | Beat | Min | Stake | Material |
|---|---|---|---|---|
| 1 | Attention | 0.5 | 3 | The printed spreadsheet + the confession |
| 2 | Need | 2.0 | 5 | 31%, Marcus's Tuesday |
| 3 | Satisfaction | 1.5 | 3 | The tool, scoped |
| 4 | Visualization | 1.5 | ~~2~~ | *(originally: a description of the better future)* |
| 5 | Action | 1.0 | 4 | Two engineers, six weeks |

**The flat spot.** Beat 4 sat at stake 2 — lower than the beat before it. A Visualization
that only shows the good future has nothing at risk in it, so the curve sags exactly where
the room should be leaning in. Fixed by adding the **negative** future, and putting it
second so it's the one they carry:

> *Nothing breaks. That's the problem.*

Stake goes to 4, and the curve now peaks at the close rather than in the middle.

**Q&A planned here, not at rehearsal** — the two hardest questions are the two objections
already surfaced in Stage 1. The CTO's ("my engineers get borrowed constantly") is answered
*inside* the speech, by naming the six-week boundary and the May report-back. The CFO's
("why not contractors?") is left for Q&A, deliberately, because answering it in the talk
would drag the argument into procurement.

---

## Stage 4 — Draft

Full script. Note what it does *not* do: no metaphor, no rhetorical questions, no tricolon.
Priya's register, throughout.

```
## Attention

[Hold up the printed spreadsheet. Say nothing for two seconds.]

This is one file. Forty tabs. [PAUSE]

A support lead named Marcus maintains it by hand. Every week. He has done it for two years.

I'm the reason it exists. Two years ago I approved it as a temporary workaround, and I want
to talk to you about what temporary cost us. [PAUSE]

## Need

Last month I audited where my team's hours actually go. I expected the number to be bad. It
was worse than bad.

Thirty-one percent of Customer Operations hours go to reconciling data between systems that
don't talk to each other. [PAUSE — let it sit] Not answering customers. Not fixing problems.
Copying numbers from one place to another and checking they match.

Here's what that looks like on a Tuesday. Marcus opens the file at nine. He pulls the ticket
export. He pulls the billing export. He compares them line by line, because when they
disagree, a customer gets billed for a service we already cancelled. By eleven he's found
four mismatches. By noon he's fixed them. Then he does it again on Thursday.

Marcus is one of our best people. We hired him to solve customer problems. He spends two
days a week being a database.

And it is getting worse, because the thing that makes reconciliation necessary is volume,
and volume is the thing we are all trying to increase. Every deal the sales team closes
this quarter adds to Marcus's Tuesday. [SLOW] We are scaling the manual work at exactly the
same rate we are scaling the business.

## Satisfaction

The fix is not more people. I want to be clear about that, because the obvious read on this
is that Ops is asking for headcount.

The fix is one screen. One place where ticket data and billing data are already matched, so
the mismatches surface automatically instead of being hunted. Engineering has scoped it.
It's not a platform and it's not a roadmap item. It's a read-only view over two databases
we already have, and they estimate six weeks. [look at the CTO]

## Visualization

Six weeks from a yes, Marcus opens one page on a Tuesday morning, sees four flagged
mismatches, fixes them before his coffee is cold, and spends the rest of the day on the
enterprise escalation queue that currently waits until Wednesday.

If we say no, here is what happens instead, and I want to be honest that this is the more
likely version. Nothing breaks. That's the problem. Nothing breaks, the thirty-one percent
holds, and next year I come back to this room asking for three more headcount to do
reconciliation at the new volume — and that request will be much easier to approve than
this one, because it will look like growth. [PAUSE]

## Action

I'm asking for two engineers for six weeks. Not a budget line. Not a committee. Two people,
six weeks, starting after the release freeze in March.

If it works, my team gives back thirty-one percent of its capacity and I don't come back for
headcount next year. If it doesn't work, we've spent six weeks and I'll tell you exactly
that in this room in May.

[PAUSE. Hold up the spreadsheet again.]

Marcus printed this for me when I asked how bad it was. He didn't complain about it. He was
almost proud of it — it's a genuinely impressive piece of work. [PAUSE] I'd rather he was
proud of something else.
```

**Callback:** the spreadsheet opens and closes the talk, and the last line reframes it —
from evidence of a problem into a portrait of a person. The close is an image, not a recap.

---

## Stage 5 — Iterate

Actual output of `speech_check.py` on the draft above:

```
RUNTIME

  543 words  @  140 wpm
  Estimated runtime : 3:53  (3.88 min)
  Limit             : 8.0 min
  Budget (85%)      : 6.8 min
  >> Well under budget (2.9 min spare)
  Note: estimate excludes pauses, laughter, questions, and tech delay.
        Live runtime is almost always longer. Calibrate your own rate:
        read 200 words aloud and time it.

SECTIONS

  Attention                        0.4m   9.4%  #####
  Need                             1.4m  35.9%  ##################
  Satisfaction                     0.6m  14.7%  #######
  Visualization                    0.8m  20.8%  ##########
  Action                           0.7m  19.2%  ##########

SENTENCES

  Count   : 50
  Mean    : 10.9 words (4.7s)     Median : 7.5 words
  Longest : 45 words      Variation (CV) : 0.83
  Over one breath (~10.7s) : 2 (4.0% of sentences)

  Longest — hard to say in one breath:
    [45w / 19.3s] Nothing breaks, the thirty-one percent holds, and next year I come back to this room asking for thre...
    [41w / 17.6s] Six weeks from a yes, Marcus opens one page on a Tuesday morning, sees four flagged mismatches, fixe...

LANGUAGE

  Cliches      : none found
  Diction      : clean
  Fillers      : actually(1)
  Passive-ish  : 1 (heuristic — expect false positives)
                 e.g. 'being hunted'
  Numbers      : 4 total (0 as digits, 4 spelled out), 1.0/min
  Stage cues   : 9 [bracketed] (excluded from runtime)

FLAGS

  !  Longest sentence runs 19.3s — roughly 1.8 breaths. Split it
  -  Well under budget — room to develop a beat, not to add one
```

**Reading it, rather than obeying it:**

- **"Well under budget" is not an instruction to write more.** Eight minutes on the agenda,
  four minutes of speech: the remaining four go to Q&A, which is where this decision is
  actually made. Padding the talk to fill the slot would trade the strongest part of the
  session for the weakest. **Kept as is, deliberately.**
- **The 19.3-second sentence is real.** Fixed by splitting: *"Nothing breaks. [PAUSE] That's
  the problem. Nothing breaks, the thirty-one percent holds, and next year…"* — and the
  split makes the beat land harder, because "Nothing breaks" now gets said twice.
- **Need at 36% of runtime is right** for a Persuasive Case. If it had come in at 15%, that
  would be the finding.
- **Numbers at 1.0/min** — low, and correct. Four figures in a four-minute talk, each one
  alone in its beat.

### A revision round

> **User:** "The middle feels slow."

**Diagnosed before editing.** "Slow" in the middle is a Stage 3 symptom, not a word problem
— but the checker says Need is proportioned correctly and the stake curve is at 5 there. So
this one is genuinely a *density* problem rather than a structural one: Marcus's Tuesday is
narrated at nine, eleven, and noon, which is three timestamps to carry one point.

Fixed at the line level by cutting one clause, not by restructuring. **This is the
exception, not the rule** — most "it's slow" reports go back to the beat sheet. The reason
it didn't here is that the beat sheet had already been fixed at Stage 3.

---

## Stage 6 — Slide brief

**Do we need slides?** Two beats require the audience to *see* something: the 31% and the
before/after. The rest is a person talking to eleven people in a boardroom.

**Three slides. Screen blank the rest of the time.**

| # | Beat | Hold | The point | Must be visible | Speaker says |
|---|---|---|---|---|---|
| 1 | Attention–Need | — | *(no slide — she's holding the object)* | `[BLANK — press B]` | The spreadsheet, the confession |
| 2 | Need | 40s | Nearly a third of Ops capacity is spent on reconciliation, not customers | One number: **31%**. Nothing else on the slide. No chart, no title, no logo | The audit finding |
| 3 | Need | 60s | The manual work scales at the same rate as the business | Two lines on one axis, volume and reconciliation hours, rising together. Annotate where they cross this quarter | "Every deal adds to Marcus's Tuesday" |
| 4 | Satisfaction | 45s | The fix is one screen over data we already have | Wireframe of the single view — one screen, four flagged rows | The scope |
| 5 | Visualization–Action | — | *(no slide — the close is the object again)* | `[BLANK — press B]` | Both futures, then the ask |

Note slide 2: a single number, alone, held for 40 seconds. The instinct to add a title, a
source line, and a logo is the instinct that would destroy it.

The completed brief goes to the `pptx` skill or a designer **whole and unedited**. It says
nothing about palette or typography on purpose.

---

## Stage 7 — Rehearsal

- **Memorize verbatim:** the first four lines and the last three. Nothing else.
- **Pause map:** after "Forty tabs"; after the 31% figure; after "Nothing breaks"; after the
  final line. Four pauses, two to three seconds each.
- **Timing checkpoint:** at minute two she should be at "The fix is not more people."
- **If running long:** cut the Tuesday narration to two timestamps. Pre-marked. Never cut
  the close.
- **Five hardest questions**, drafted at Stage 3: contractors instead (CFO), why not next
  quarter (CTO), what happens if six weeks becomes twelve, who maintains it after, and why
  Ops rather than Engineering owns the request.
- **Close Q&A on her own terms:** re-deliver the ask in one sentence after the last answer.

---

## What to notice

1. **The best line came from a wrong guess.** "I approved the thing that caused this" was
   volunteered while correcting an inference. Guessing specifically and being corrected
   beats asking open questions.
2. **The throughline changed the whole frame.** "Ops needs support" is a request. "We're
   paying twelve people to do what one tool could do" is a claim about the business — and it
   is what let a headcount ask stop sounding like a headcount ask.
3. **The structural fix was one beat.** Adding the negative future to Visualization did more
   than any amount of line editing would have.
4. **The checker's loudest flag was the one to ignore.** "Well under budget" was correct and
   irrelevant; the four spare minutes were already allocated to the part that decides the
   outcome.
5. **The register is unremarkable, on purpose.** There is no memorable phrasing in this
   speech. There is a named person, a number, an object, and an ask. That is enough, and for
   this speaker in this room it is more than enough.
