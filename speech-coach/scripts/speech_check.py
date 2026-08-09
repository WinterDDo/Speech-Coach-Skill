#!/usr/bin/env python3
"""
speech_check.py — mechanical smoke test for a speech draft.

Reports estimated runtime, per-section timing against budget, sentence-length
distribution, sentences too long to say in one breath, cliche and filler hits,
number density, and rhythm variance.

This is a smoke detector, not a judge. It measures what a machine can measure.
It cannot tell you whether the story is any good, whether the throughline holds,
or whether the room will care. Read the output; don't obey it. The read-aloud
checklist in references/language.md covers everything this script cannot see.

Usage:
    python3 speech_check.py draft.md
    python3 speech_check.py draft.md --wpm 140 --target-minutes 10
    python3 speech_check.py draft.md --json

Stdlib only. Python 3.8+.
"""

import argparse
import json
import re
import statistics
import sys
import unicodedata
from pathlib import Path

# --- Pacing defaults ---------------------------------------------------------
# Rules of thumb. Have the speaker calibrate: read 200 words aloud, time it.
#   Conversational / demo ........ 150-165 wpm
#   Standard prepared talk ....... 135-150 wpm
#   Formal / ceremonial .......... 110-130 wpm
DEFAULT_WPM = 140
DEFAULT_CPM = 220          # CJK characters per minute (Chinese/Japanese speech)
MAX_SENTENCE_WORDS = 25    # practical ceiling for one spoken breath
BUDGET_FRACTION = 0.85     # every speech runs long live

# --- Phrases that are dead on arrival (see references/language.md) -----------
CLICHES = [
    "without further ado", "in today's fast-paced world", "in todays fast-paced world",
    "webster's dictionary", "websters dictionary", "as you can see on this slide",
    "as you can see from this slide", "at the end of the day", "it goes without saying",
    "i won't bore you", "i wont bore you", "to be honest with you", "needless to say",
    "last but not least", "thinking outside the box", "low-hanging fruit",
    "move the needle", "boil the ocean", "circle back", "synergy", "paradigm shift",
    "game changer", "game-changer",
    "i'm excited to be here", "im excited to be here", "before i begin",
    "can everyone hear me", "can everybody hear me", "that's it, thank you",
    "thats it, thank you", "any questions", "i think i'm out of time",
    "i know i'm running short on time", "let me unpack that", "deep dive",
]

FILLERS = [
    "basically", "actually", "literally", "obviously", "essentially",
    "just", "really", "very", "quite", "somewhat", "kind of", "sort of",
]

WEAK_OPENERS = [
    "so,", "so ", "well,", "now,", "um", "uh", "okay,", "alright,", "right,",
]

# Latinate words with shorter Anglo-Saxon equivalents
WORDY = {
    "utilize": "use", "utilise": "use", "implement": "do / build",
    "terminate": "end / stop", "facilitate": "help / run", "leverage": "use",
    "optimize": "improve", "optimise": "improve", "commence": "begin",
    "endeavor": "try", "endeavour": "try", "procure": "buy / get",
    "approximately": "about", "subsequent": "after", "prior to": "before",
    "in order to": "to", "at this point in time": "now",
    "in the event that": "if", "due to the fact that": "because",
    "a significant proportion of": "most", "with regard to": "about",
    "additionally": "also", "furthermore": "also", "therefore": "so",
    "however": "but", "utilization": "use", "methodology": "method",
}

PASSIVE_RE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being)\s+"
    r"(?:\w+ly\s+)?"
    r"(\w+ed|born|done|made|given|taken|seen|known|shown|held|told|found|"
    r"left|kept|built|sent|brought|written|driven|chosen|put|set|lost|won)\b",
    re.IGNORECASE,
)

# Statistics spelled out as words. Speech scripts SHOULD spell numbers out, so a
# digits-only detector silently reports zero on exactly the drafts written correctly.
# Targets figures, not quantities: "thirty-one percent" counts, "two engineers" does not.
NUM_WORD_RE = re.compile(
    r"\b(?:"
    r"(?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
    r"(?:[-\s](?:one|two|three|four|five|six|seven|eight|nine))?"
    r"|(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen)"
    r"\s+(?:percent|per\s?cent|thousand|million|billion|trillion)"
    r"|hundreds|thousands|millions|billions"
    r")\b",
    re.IGNORECASE,
)

CJK_RE = re.compile(r"[一-鿿㐀-䶿぀-ヿ가-힯]")
STAGE_DIR_RE = re.compile(r"\[([^\[\]]*)\]")
HEADING_TIME_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:min|minutes|mins|m)\b", re.IGNORECASE)


# --- Parsing -----------------------------------------------------------------

def strip_markup(text):
    """Remove markdown chrome and stage directions. Returns (clean, directions).

    Headings, table rows and rules are dropped entirely rather than unwrapped:
    they are structural labels, not spoken words, so counting them would inflate
    the runtime estimate and glue section titles onto the first real sentence.
    Every dropped or list-item line becomes a blank line so that blocks stay
    separated for sentence splitting.
    """
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)      # frontmatter
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)           # html comments
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)            # code fences
    text = re.sub(r"`([^`]*)`", r"\1", text)                           # inline code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)                  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)               # links -> label

    directions = [m.group(1).strip() for m in STAGE_DIR_RE.finditer(text)]
    text = STAGE_DIR_RE.sub(" ", text)                                 # stage directions

    out = []
    for line in text.split("\n"):
        s = line.strip()
        if (not s
                or re.match(r"^#{1,6}\s", s)                           # heading
                or re.match(r"^[-*_]{3,}$", s)                         # horizontal rule
                or s.startswith("|")):                                 # table row
            out.append("")
            continue
        s = re.sub(r"^>\s?", "", s).strip()                            # blockquote
        m = re.match(r"^(?:[-*+]|\d+[.)])\s+(.*)$", s)                 # list item
        if m:
            out.extend([m.group(1).strip(), ""])                       # own block
            continue
        out.append(s)

    text = "\n".join(out)
    text = re.sub(r"(\*\*|__|\*|_|~~)", "", text)                      # emphasis
    return text, directions


def split_sections(raw):
    """Split on markdown headings. Returns [(title, body, target_minutes|None)]."""
    parts = re.split(r"^(\s{0,3}#{1,6}\s+.*)$", raw, flags=re.MULTILINE)
    if len(parts) == 1:
        return [("(whole draft)", raw, None)]
    sections, i = [], 1
    if parts[0].strip():
        sections.append(("(preamble)", parts[0], None))
    while i < len(parts) - 1:
        title = re.sub(r"^\s{0,3}#{1,6}\s+", "", parts[i]).strip()
        body = parts[i + 1]
        m = HEADING_TIME_RE.search(title)
        sections.append((title, body, float(m.group(1)) if m else None))
        i += 2
    return sections


def split_sentences(text):
    """Heuristic sentence split. Handles abbreviations, CJK stops, and blocks.

    Blank lines are hard boundaries: a paragraph break in a script is always a
    sentence break, and honouring it stops unpunctuated lines from fusing into
    phantom mega-sentences.
    """
    out = []
    for block in re.split(r"\n\s*\n", text):
        block = re.sub(r"\s+", " ", block).strip()
        if not block:
            continue
        protected = block
        for abbr in ["Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "St.", "vs.", "etc.",
                     "e.g.", "i.e.", "Inc.", "Ltd.", "Co.", "Jr.", "Sr.", "No.",
                     "U.S.", "U.K.", "a.m.", "p.m."]:
            protected = protected.replace(abbr, abbr.replace(".", "\x00"))
        protected = re.sub(r"\b([A-Z])\.", lambda m: m.group(1) + "\x00", protected)
        # Full-width stops need no trailing space; Western stops do.
        for p in re.split(r"(?<=[。！？])|(?<=[.!?…])[\s　]+", protected):
            p = p.replace("\x00", ".").strip()
            if p and re.search(r"[A-Za-z一-鿿]", p):
                out.append(p)
    return out


def count_units(text):
    """Returns (english_words, cjk_chars)."""
    cjk = len(CJK_RE.findall(text))
    stripped = CJK_RE.sub(" ", text)
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", stripped)
    return len(words), cjk


def sentence_length(s):
    """Length in native units: words for Latin script, characters for CJK."""
    w, c = count_units(s)
    return w + c


def duration_minutes(words, cjk, wpm, cpm):
    return (words / wpm if wpm else 0) + (cjk / cpm if cpm else 0)


def sentence_seconds(s, wpm, cpm):
    """Spoken cost of a sentence, in seconds.

    Length thresholds must be measured in time, not units: 25 English words and
    25 Chinese characters are nowhere near the same breath. Seconds are the only
    unit that compares across scripts.
    """
    w, c = count_units(s)
    return duration_minutes(w, c, wpm, cpm) * 60


def fmt_time(minutes):
    total = int(round(minutes * 60))
    return f"{total // 60}:{total % 60:02d}"


# --- Checks ------------------------------------------------------------------

def find_phrases(text, phrases, whole_word=False):
    low = text.lower()
    hits = []
    for p in phrases:
        if whole_word:
            n = len(re.findall(r"\b" + re.escape(p) + r"\b", low))
        else:
            n = low.count(p)
        if n:
            hits.append((p, n))
    return sorted(hits, key=lambda x: -x[1])


def analyze(raw, wpm, cpm, max_sentence, target_minutes):
    clean, directions = strip_markup(raw)
    words, cjk = count_units(clean)
    est = duration_minutes(words, cjk, wpm, cpm)

    sentences = split_sentences(clean)
    measured = [(sentence_length(s), sentence_seconds(s, wpm, cpm), s) for s in sentences]
    measured = [m for m in measured if m[0] > 0]
    lengths = [m[0] for m in measured]
    secs = [m[1] for m in measured]

    # One breath, expressed as time so the test works in any script.
    breath_seconds = max_sentence / wpm * 60
    long_sentences = sorted(
        [m for m in measured if m[1] > breath_seconds], key=lambda x: -x[1]
    )

    # per-section timing
    sec_rows = []
    for title, body, target in split_sections(raw):
        body_clean, _ = strip_markup(body)
        w, c = count_units(body_clean)
        if w + c == 0:
            continue
        d = duration_minutes(w, c, wpm, cpm)
        share = (d / est * 100) if est else 0
        sec_rows.append({
            "title": title, "words": w, "cjk": c,
            "minutes": round(d, 2), "share_pct": round(share, 1),
            "target_minutes": target,
            "over_by": round(d - target, 2) if target else None,
        })

    digits = re.findall(r"(?<![\w.])\d[\d,.]*\s*(?:%|percent|million|billion|k\b)?", clean)
    spelled = NUM_WORD_RE.findall(clean)
    numbers = digits + spelled
    passive = [m.group(0) for m in PASSIVE_RE.finditer(clean)]
    wordy_hits = [(w, r, len(re.findall(r"\b" + re.escape(w) + r"\b", clean.lower())))
                  for w, r in WORDY.items()
                  if re.search(r"\b" + re.escape(w) + r"\b", clean.lower())]
    wordy_hits = sorted([h for h in wordy_hits if h[2]], key=lambda x: -x[2])

    return {
        "words": words,
        "cjk_chars": cjk,
        "estimated_minutes": round(est, 2),
        "estimated_time": fmt_time(est),
        "wpm": wpm,
        "cpm": cpm if cjk else None,
        "target_minutes": target_minutes,
        "budget_minutes": round(target_minutes * BUDGET_FRACTION, 2) if target_minutes else None,
        "unit": "chars" if cjk > words else "words",
        "sentences": len(measured),
        "sentence_mean": round(statistics.mean(lengths), 1) if lengths else 0,
        "sentence_median": round(statistics.median(lengths), 1) if lengths else 0,
        "sentence_max": max(lengths) if lengths else 0,
        "sentence_stdev": round(statistics.pstdev(lengths), 1) if len(lengths) > 1 else 0,
        "sentence_cv": round(statistics.pstdev(lengths) / statistics.mean(lengths), 2)
                       if len(lengths) > 1 and statistics.mean(lengths) else 0,
        "sentence_mean_seconds": round(statistics.mean(secs), 1) if secs else 0,
        "breath_seconds": round(breath_seconds, 1),
        "long_sentences": [{"units": n, "seconds": round(sec, 1), "text": s}
                           for n, sec, s in long_sentences],
        "long_sentence_pct": round(len(long_sentences) / len(lengths) * 100, 1) if lengths else 0,
        "sections": sec_rows,
        "cliches": find_phrases(clean, CLICHES),
        "fillers": find_phrases(clean, FILLERS, whole_word=True),
        "wordy": [{"word": w, "use": r, "n": n} for w, r, n in wordy_hits],
        "passive_count": len(passive),
        "passive_examples": passive[:8],
        "number_count": len(numbers),
        "number_digits": len(digits),
        "number_spelled": len(spelled),
        "stage_directions": len(directions),
        "max_sentence_threshold": max_sentence,
    }


# --- Reporting ---------------------------------------------------------------

def bar(n, scale, width=30, ch="#"):
    return ch * max(0, min(width, int(round(n / scale * width)))) if scale else ""


def report(a, path):
    W = 72
    out = []
    p = out.append

    p("=" * W)
    p(f"  SPEECH CHECK  ·  {path}")
    p("=" * W)

    # Runtime
    p("")
    p("RUNTIME")
    p("-" * W)
    unit = f"{a['words']:,} words"
    if a["cjk_chars"]:
        unit += f" + {a['cjk_chars']:,} CJK chars"
    rate = f"{a['wpm']} wpm" + (f", {a['cpm']} cpm" if a["cpm"] else "")
    p(f"  {unit}  @  {rate}")
    p(f"  Estimated runtime : {a['estimated_time']}  ({a['estimated_minutes']} min)")

    flags, notes = [], []
    if a["target_minutes"]:
        budget = a["budget_minutes"]
        p(f"  Limit             : {a['target_minutes']} min")
        p(f"  Budget (85%)      : {budget} min")
        delta = a["estimated_minutes"] - budget
        if delta > 0:
            over_words = int(delta * a["wpm"])
            p(f"  >> OVER BUDGET by {round(delta, 1)} min (~{over_words} words)")
            flags.append(f"Over budget by {round(delta,1)} min — cut a whole beat, don't speed up")
        elif a["estimated_minutes"] < budget * 0.6:
            p(f"  >> Well under budget ({round(budget - a['estimated_minutes'],1)} min spare)")
            notes.append("Well under budget — room to develop a beat, not to add one")
        else:
            p("  >> Fits budget")
    p("  Note: estimate excludes pauses, laughter, questions, and tech delay.")
    p("        Live runtime is almost always longer. Calibrate your own rate:")
    p("        read 200 words aloud and time it.")

    # Sections
    if len(a["sections"]) > 1:
        p("")
        p("SECTIONS")
        p("-" * W)
        mx = max(s["minutes"] for s in a["sections"]) or 1
        for s in a["sections"]:
            title = s["title"][:30].ljust(30)
            line = f"  {title} {s['minutes']:>5.1f}m {s['share_pct']:>5.1f}%  {bar(s['minutes'], mx, 18)}"
            if s["target_minutes"]:
                ob = s["over_by"]
                line += f"  [target {s['target_minutes']}m, {'+' if ob >= 0 else ''}{ob}]"
                if ob > 0.5:
                    flags.append(f"Section '{s['title'][:30]}' runs {ob} min over its beat target")
            p(line)

    # Sentences
    p("")
    p("SENTENCES")
    p("-" * W)
    u = a["unit"]
    p(f"  Count   : {a['sentences']}")
    p(f"  Mean    : {a['sentence_mean']} {u} ({a['sentence_mean_seconds']}s)"
      f"     Median : {a['sentence_median']} {u}")
    p(f"  Longest : {a['sentence_max']} {u}      Variation (CV) : {a['sentence_cv']}")
    p(f"  Over one breath (~{a['breath_seconds']}s) : {len(a['long_sentences'])} "
      f"({a['long_sentence_pct']}% of sentences)")

    if a["sentence_mean_seconds"] > 20 / a["wpm"] * 60:
        flags.append(f"Mean sentence {a['sentence_mean_seconds']}s — too long for the ear. Split them")
    if a["sentence_cv"] and a["sentence_cv"] < 0.35 and a["sentences"] > 8:
        flags.append(f"Low rhythm variation (CV {a['sentence_cv']}) — uniform sentence length "
                     "flattens into drone. Land beats on short sentences")
    if a["long_sentence_pct"] >= 20:
        flags.append(f"{a['long_sentence_pct']}% of sentences exceed one breath")
    if a["long_sentences"] and a["long_sentences"][0]["seconds"] > a["breath_seconds"] * 1.5:
        worst = a["long_sentences"][0]
        flags.append(f"Longest sentence runs {worst['seconds']}s — roughly "
                     f"{worst['seconds'] / a['breath_seconds']:.1f} breaths. Split it")

    if a["long_sentences"]:
        p("")
        p("  Longest — hard to say in one breath:")
        for item in a["long_sentences"][:5]:
            txt = item["text"]
            txt = txt[:100] + "..." if len(txt) > 100 else txt
            p(f"    [{item['units']}{u[0]} / {item['seconds']}s] {txt}")

    # Language
    p("")
    p("LANGUAGE")
    p("-" * W)
    if a["cliches"]:
        p("  Cliches / dead phrases (cut on sight):")
        for ph, n in a["cliches"][:10]:
            p(f"    {n:>2}x  \"{ph}\"")
        flags.append(f"{len(a['cliches'])} cliche phrase(s) present")
    else:
        p("  Cliches      : none found")

    if a["wordy"]:
        p("  Latinate words with shorter equivalents:")
        for h in a["wordy"][:8]:
            p(f"    {h['n']:>2}x  {h['word']} -> {h['use']}")
    else:
        p("  Diction      : clean")

    if a["fillers"]:
        top = ", ".join(f"{p_}({n})" for p_, n in a["fillers"][:8])
        p(f"  Fillers      : {top}")
        total_fill = sum(n for _, n in a["fillers"])
        if a["words"] and total_fill / a["words"] > 0.02:
            flags.append(f"Filler density {round(total_fill/a['words']*100,1)}% — "
                         "cut 'just', 'really', 'very', 'basically'")

    p(f"  Passive-ish  : {a['passive_count']} (heuristic — expect false positives)")
    if a["passive_examples"]:
        p(f"                 e.g. {', '.join(repr(x) for x in a['passive_examples'][:4])}")
    if a["words"] and a["passive_count"] / max(a["sentences"], 1) > 0.3:
        flags.append("High passive-voice rate — name the actor. Fatal in an apology")

    density = a["number_count"] / a["estimated_minutes"] if a["estimated_minutes"] else 0
    p(f"  Numbers      : {a['number_count']} total "
      f"({a['number_digits']} as digits, {a['number_spelled']} spelled out), "
      f"{round(density,1)}/min")
    if density > 6:
        flags.append(f"Number density {round(density,1)}/min — the ear stops processing "
                     "after three in a row. Round, compare, or move to a slide")

    p(f"  Stage cues   : {a['stage_directions']} [bracketed] "
      f"({'excluded from runtime' if a['stage_directions'] else 'none — add PAUSE marks'})")
    if a["stage_directions"] == 0:
        notes.append("No [PAUSE] marks found — speakers who don't plan pauses don't take them")

    # Verdict
    p("")
    p("FLAGS")
    p("-" * W)
    if flags:
        for f in flags:
            p(f"  !  {f}")
    else:
        p("  None. Mechanically clean.")
    for n in notes:
        p(f"  -  {n}")

    p("")
    p("-" * W)
    p("  This script measures only what a machine can measure. It says nothing")
    p("  about whether the throughline holds, whether the story is true, or")
    p("  whether the room will care. Now read it aloud, standing up:")
    p("  see the read-aloud checklist in references/language.md.")
    p("=" * W)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(
        description="Mechanical smoke test for a speech draft.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="A smoke detector, not a judge. Read the output; don't obey it.",
    )
    ap.add_argument("file", help="draft file (.md or .txt)")
    ap.add_argument("--wpm", type=int, default=DEFAULT_WPM,
                    help=f"speaking rate, words/min (default {DEFAULT_WPM}; "
                         "conversational 150-165, prepared 135-150, ceremonial 110-130)")
    ap.add_argument("--cpm", type=int, default=DEFAULT_CPM,
                    help=f"CJK characters/min (default {DEFAULT_CPM})")
    ap.add_argument("--target-minutes", type=float, default=None,
                    help="the hard time limit; budget is 85%% of it")
    ap.add_argument("--max-sentence", type=int, default=MAX_SENTENCE_WORDS,
                    help=f"long-sentence threshold in words (default {MAX_SENTENCE_WORDS})")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a report")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        sys.exit(f"speech_check: no such file: {path}")
    raw = path.read_text(encoding="utf-8", errors="replace")
    raw = unicodedata.normalize("NFC", raw)
    if not raw.strip():
        sys.exit(f"speech_check: {path} is empty")

    a = analyze(raw, args.wpm, args.cpm, args.max_sentence, args.target_minutes)
    if args.json:
        print(json.dumps(a, ensure_ascii=False, indent=2))
    else:
        print(report(a, path.name))


if __name__ == "__main__":
    main()
