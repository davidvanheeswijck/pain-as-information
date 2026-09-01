#!/usr/bin/env python3
"""Structural linter for conjecture files.

A conjecture that does not state what would refute it is not a conjecture,
and this tool is what makes that a build failure rather than an aspiration.
See EPISTEMICS.md rule 4 and conjectures/TEMPLATE.md for the shape enforced
here.
"""

import argparse
import glob
import json
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "Claim",
    "Why this, why now",
    "Mechanism",
    "Forbidden observation",
    "Killer",
    "Rivals",
    "Severity",
    "What it would change",
    "References",
]

VALID_BRANCHES = {"A", "B", "C"}
VALID_STATUSES = {"draft", "in-panel", "open", "wounded", "refuted", "promoted"}
STATUSES_REQUIRING_POSTERIOR = {"open", "wounded", "refuted"}

ID_RE = re.compile(r"^C-\d{3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

NEGATION_WORDS = [
    "not", "no", "never", "cannot", "without", "fails to", "absent",
    "below", "indistinguishable",
]
COST_TIME_WORDS = ["cost", "€", "$", "month", "year", "week"]
HEDGE_WORDS = [
    "may", "might", "could", "potentially", "possibly", "perhaps",
    "suggests that", "it is thought",
]
QUANTUM_WORDS = [
    "quantum", "coherence", "entangle", "superposition", "spin",
    "radical pair", "tunnelling", "tunneling", "resonance",
]

TIME_UNIT_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:s|ms|us|µs|ns|ps|fs)\b"
    r"|\b\d+(?:\.\d+)?[eE]-\d+\s*s\b",
)
ENERGY_UNIT_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:eV|meV|J|kT|kJ/mol|K)\b",
)
NUMBER_WITH_UNIT_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:s|ms|us|µs|ns|ps|fs|eV|meV|J|kT|kJ/mol|K|Hz|kHz|MHz|GHz)\b",
    re.IGNORECASE,
)

REFERENCE_ID_RE = re.compile(
    r"10\.\d{4,9}/\S+|PMID\s*:?\s*\d+|arXiv:\S+|NCT\d{8}",
    re.IGNORECASE,
)

KILLER_QUANTITY_RE = re.compile(
    r"\d+(?:\.\d+)?|n\s*=", re.IGNORECASE,
)

SEVERITY_FLOAT_RE = re.compile(r"\b0?\.\d+\b|\b1\.0+\b")


def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".git").exists():
            return candidate
    return start.resolve()


def word_boundary_search(words, text):
    """Return the list of words from `words` that occur in `text` (case-insensitive,
    whole word/phrase match)."""
    found = []
    lowered = text.lower()
    for w in words:
        pattern = r"\b" + re.escape(w.lower()) + r"\b"
        if re.search(pattern, lowered):
            found.append(w)
    return found


def count_hedges(text):
    lowered = text.lower()
    total = 0
    counts = {}
    for w in HEDGE_WORDS:
        pattern = r"\b" + re.escape(w.lower()) + r"\b"
        n = len(re.findall(pattern, lowered))
        if n:
            counts[w] = n
            total += n
    return total, counts


def strip_html_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def parse_front_matter(text):
    """Very small YAML-ish key: value front matter reader. Returns
    (front_matter_dict, line_offsets, error) where line_offsets maps key to
    the 1-based line number it was found on, and error is a string or None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, {}, "no '---' delimited front matter block at top of file"
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, {}, "front matter block opened with '---' but never closed"
    data = {}
    line_no = {}
    for i in range(1, end_idx):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        key = key.strip()
        value = value.strip()
        data[key] = value
        line_no[key] = i + 1
    return data, line_no, None


def find_section(body, heading):
    """Find a `## Heading` section's body text (up to next `## `). Returns
    the raw section text (excluding the heading line) or None if not found."""
    pattern = re.compile(
        r"^##\s+" + re.escape(heading) + r"\s*$", re.MULTILINE,
    )
    m = pattern.search(body)
    if not m:
        return None
    start = m.end()
    next_m = re.search(r"^##\s+", body[start:], re.MULTILINE)
    end = start + next_m.start() if next_m else len(body)
    return body[start:end]


def visible_text_len(section_text):
    stripped = strip_html_comments(section_text)
    return len(stripped.strip())


def split_sentences(text):
    stripped = strip_html_comments(text).strip()
    if not stripped:
        return []
    # naive sentence splitter: split on '.', '!' or '?' followed by
    # whitespace or end of string.
    parts = re.split(r"(?<=[.!?])\s+", stripped)
    return [p for p in parts if p.strip()]


def count_rivals(section_text):
    stripped = strip_html_comments(section_text)
    subheadings = re.findall(r"^###\s+\S", stripped, re.MULTILINE)
    if subheadings:
        return len(subheadings)
    bullets = re.findall(r"^\s*[-*+]\s+\S", stripped, re.MULTILINE)
    return len(bullets)


def jaccard(a, b):
    wa = set(re.findall(r"[a-z0-9]+", a.lower()))
    wb = set(re.findall(r"[a-z0-9]+", b.lower()))
    if not wa or not wb:
        return 0.0
    inter = wa & wb
    union = wa | wb
    return len(inter) / len(union)


def parse_ledger(ledger_path):
    """Extract (id, title, body) tuples from ledger/REFUTED.md."""
    if not ledger_path.exists():
        return []
    text = ledger_path.read_text(encoding="utf-8", errors="replace")
    entries = []
    matches = list(re.finditer(r"^###\s+(C-\d{3})\s*[—-]\s*(.+)$", text, re.MULTILINE))
    for i, m in enumerate(matches):
        entry_id = m.group(1)
        title = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        entries.append((entry_id, title, body))
    return entries


class Result:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, path, line, msg):
        self.errors.append((str(path), line, msg))

    def warn(self, path, line, msg):
        self.warnings.append((str(path), line, msg))


def lint_file(path: Path, repo_root: Path, ledger_entries, result: Result):
    text = path.read_text(encoding="utf-8", errors="replace")
    front, line_no, fm_error = parse_front_matter(text)

    if fm_error:
        result.error(path.name, 1, fm_error)
        # Without front matter we cannot check id/branch/etc, but we can
        # still check the body sections below.
        front = {}

    # id
    conjecture_id = front.get("id", "") if front else ""
    if not conjecture_id:
        result.error(path.name, line_no.get("id", 1), "id missing")
    elif not ID_RE.match(conjecture_id):
        result.error(
            path.name, line_no.get("id", 1),
            f"id '{conjecture_id}' does not match ^C-\\d{{3}}$",
        )
    if conjecture_id and ID_RE.match(conjecture_id):
        stem = path.stem  # e.g. C-004-foo
        prefix_m = re.match(r"^(C-\d{3})\b", stem)
        if prefix_m and prefix_m.group(1) != conjecture_id:
            result.error(
                path.name, line_no.get("id", 1),
                f"id '{conjecture_id}' does not match filename prefix "
                f"'{prefix_m.group(1)}'",
            )

    # title
    title = front.get("title", "") if front else ""
    if not title:
        result.error(path.name, line_no.get("title", 1), "title missing")
    elif len(title) < 20:
        result.error(
            path.name, line_no.get("title", 1),
            f"title is {len(title)} chars, shorter than the required 20",
        )

    # branch
    branch = front.get("branch", "") if front else ""
    if branch not in VALID_BRANCHES:
        result.error(
            path.name, line_no.get("branch", 1),
            f"branch '{branch}' is not one of A, B, C",
        )

    # status
    status = front.get("status", "") if front else ""
    if status not in VALID_STATUSES:
        result.error(
            path.name, line_no.get("status", 1),
            f"status '{status}' is not one of {sorted(VALID_STATUSES)}",
        )

    # prior
    prior_raw = front.get("prior", "") if front else ""
    prior_val = None
    if not prior_raw:
        result.error(path.name, line_no.get("prior", 1), "prior missing")
    else:
        try:
            prior_val = float(prior_raw)
        except ValueError:
            result.error(
                path.name, line_no.get("prior", 1),
                f"prior '{prior_raw}' is not parseable as a float",
            )
        else:
            if not (0 < prior_val < 1):
                result.error(
                    path.name, line_no.get("prior", 1),
                    f"prior {prior_val} is not a probability strictly "
                    "between 0 and 1 (0 and 1 are certainty, not priors)",
                )
            elif prior_val > 0.5:
                result.warn(
                    path.name, line_no.get("prior", 1),
                    f"prior {prior_val} is above even odds; say in "
                    "'Why this, why now' why a novel conjecture in a hard "
                    "field starts above 0.5",
                )

    # posterior
    posterior_raw = front.get("posterior", "") if front else ""
    if status in STATUSES_REQUIRING_POSTERIOR and not posterior_raw:
        result.error(
            path.name, line_no.get("posterior", line_no.get("status", 1)),
            f"status '{status}' requires a posterior (a panel has run) "
            "but posterior is empty",
        )
    if posterior_raw:
        try:
            posterior_val = float(posterior_raw)
        except ValueError:
            result.error(
                path.name, line_no.get("posterior", 1),
                f"posterior '{posterior_raw}' is not parseable as a float",
            )
        else:
            if not (0 < posterior_val < 1):
                result.error(
                    path.name, line_no.get("posterior", 1),
                    f"posterior {posterior_val} is not strictly between 0 and 1",
                )

    # created
    created = front.get("created", "") if front else ""
    if not created or not DATE_RE.match(created):
        result.error(
            path.name, line_no.get("created", 1),
            f"created '{created}' missing or not in YYYY-MM-DD form",
        )

    # lineage
    lineage = front.get("lineage", "") if front else ""
    if lineage:
        lineage_id_m = re.match(r"^(C-\d{3})", lineage)
        if lineage_id_m:
            lineage_id = lineage_id_m.group(1)
            candidates = list(repo_root.glob(f"conjectures/{lineage_id}*.md"))
            if not candidates:
                result.warn(
                    path.name, line_no.get("lineage", 1),
                    f"lineage names '{lineage_id}' but no corresponding "
                    "file was found",
                )

    # --- required sections ---
    section_bodies = {}
    for heading in REQUIRED_SECTIONS:
        section_text = find_section(text, heading)
        section_bodies[heading] = section_text
        if section_text is None:
            result.error(path.name, 1, f"missing required section '## {heading}'")
        elif visible_text_len(section_text) < 40:
            result.error(
                path.name, 1,
                f"section '## {heading}' has fewer than 40 characters of body text",
            )

    # --- Forbidden observation ---
    fo = section_bodies.get("Forbidden observation")
    if fo:
        sentences = split_sentences(fo)
        if len(sentences) > 3:
            result.error(
                path.name, 1,
                f"'## Forbidden observation' has {len(sentences)} sentences, "
                "more than the 3 allowed (it is meant to be one)",
            )
        if not word_boundary_search(NEGATION_WORDS, strip_html_comments(fo)):
            result.warn(
                path.name, 1,
                "'## Forbidden observation' contains no negation or exclusion "
                "word (not/no/never/cannot/without/fails to/absent/below/"
                "indistinguishable); it may be a prediction, not a prohibition",
            )

    # --- Killer ---
    killer = section_bodies.get("Killer")
    if killer:
        killer_clean = strip_html_comments(killer)
        has_number = bool(re.search(r"\d", killer_clean))
        has_n_eq = bool(re.search(r"\bn\s*=", killer_clean, re.IGNORECASE))
        if not (has_number or has_n_eq):
            result.error(
                path.name, 1,
                "'## Killer' contains no number, unit or 'n=': a killer with "
                "no quantity is not concrete",
            )
        if not word_boundary_search(COST_TIME_WORDS, killer_clean):
            result.warn(
                path.name, 1,
                "'## Killer' lacks any cost or time indicator "
                "(cost/€/$/month/year/week)",
            )

    # --- Rivals ---
    rivals = section_bodies.get("Rivals")
    if rivals:
        n_rivals = count_rivals(rivals)
        if n_rivals < 2:
            result.error(
                path.name, 1,
                f"'## Rivals' lists {n_rivals} item(s); at least 2 are required",
            )

    # --- Severity ---
    severity = section_bodies.get("Severity")
    if severity:
        severity_clean = strip_html_comments(severity)
        matches = SEVERITY_FLOAT_RE.findall(severity_clean)
        found_val = None
        for m in matches:
            try:
                v = float(m)
            except ValueError:
                continue
            if 0 <= v <= 1:
                found_val = v
                break
        if found_val is None:
            result.error(
                path.name, 1,
                "'## Severity' contains no floating point number between 0 and 1",
            )
        elif found_val > 0.3:
            result.warn(
                path.name, 1,
                f"'## Severity' value {found_val} is above 0.3; the test "
                "is then not evidence",
            )

    # --- Claim ---
    claim = section_bodies.get("Claim")
    if claim:
        total_hedges, counts = count_hedges(claim)
        if total_hedges:
            for w, n in counts.items():
                result.warn(
                    path.name, 1,
                    f"'## Claim' contains hedging word '{w}' ({n}x)",
                )
        if total_hedges > 3:
            result.error(
                path.name, 1,
                f"'## Claim' contains {total_hedges} hedging words, more "
                "than 3: the claim has hedged itself into unfalsifiability",
            )

    # --- References ---
    refs = section_bodies.get("References")
    if refs:
        if not REFERENCE_ID_RE.search(strip_html_comments(refs)):
            result.error(
                path.name, 1,
                "'## References' contains no resolvable-looking identifier "
                "(DOI, PMID, arXiv, NCT)",
            )

    # --- Branch C / quantum vocabulary guard ---
    # Fires for every Branch C conjecture, and for A or B only when the quantum
    # vocabulary appears in the MECHANISM. The point of this rule is to stop a
    # conjecture whose mechanism secretly requires Branch C physics from being
    # filed as Branch A, so it is the mechanism that has to be clean. Scanning
    # the whole document instead caught conjectures that merely *mention*
    # quantum technology in order to disclaim it, or that name the branch they
    # are not in, and demanding an energy scale in eV from an array
    # signal-processing proposal is the rule mis-firing rather than working.
    mechanism = section_bodies.get("Mechanism") or ""
    mech_clean = strip_html_comments(mechanism)
    quantum_hit = branch == "C" or bool(
        word_boundary_search(QUANTUM_WORDS, mech_clean)
    )
    if quantum_hit:
        mechanism = section_bodies.get("Mechanism") or ""
        mech_clean = strip_html_comments(mechanism)
        has_time = bool(TIME_UNIT_RE.search(mech_clean))
        has_energy = bool(ENERGY_UNIT_RE.search(mech_clean))
        if not (has_time and has_energy):
            result.error(
                path.name, 1,
                "Branch C or quantum vocabulary present but Mechanism "
                "supplies no timescale and/or no energy scale. See "
                "pipeline/gates/01-physical-plausibility.md — supply them "
                "here rather than spending a panel round.",
            )

        # "frequency" with no units nearby is the signature of a claim like
        # "the characteristic frequency of the tissue", which gate 01 treats as
        # an automatic FATAL. But a hyphenated band name (extremely-low-frequency,
        # high-frequency, kilohertz-frequency) is standard terminology naming a
        # range, not an asserted value, so it is excluded. Narrowing the rule to
        # what it was actually aimed at, rather than deleting it.
        BAND_NAME_RE = re.compile(
            r"\b(?:extremely[- ]low|ultra[- ]low|very[- ]low|low|mid|high|very[- ]high|"
            r"ultra[- ]high|radio|audio|kilohertz|megahertz|gigahertz)[- ]frequency\b",
            re.IGNORECASE,
        )
        body_clean = strip_html_comments(text)
        for sentence in split_sentences_all(body_clean):
            if not re.search(r"\bfrequency\b", sentence, re.IGNORECASE):
                continue
            if NUMBER_WITH_UNIT_RE.search(sentence):
                continue
            # Strip the band names, then see whether a bare "frequency" remains.
            residual = BAND_NAME_RE.sub("", sentence)
            if re.search(r"\bfrequency\b", residual, re.IGNORECASE):
                result.error(
                    path.name, 1, "frequency asserted without units",
                )
                break

    # --- Ledger collision check ---
    if ledger_entries:
        title_text = title or ""
        claim_text = strip_html_comments(claim or "")
        for entry_id, entry_title, entry_body in ledger_entries:
            # A refuted conjecture keeps its file, so once it is written into
            # the graveyard it necessarily resembles its own entry. Warning
            # about that is noise, and noise is how a useful warning gets
            # ignored. Only collisions with OTHER refuted conjectures matter.
            if conjecture_id and entry_id == conjecture_id:
                continue
            title_sim = jaccard(title_text, entry_title) if title_text else 0.0
            claim_sim = jaccard(claim_text, entry_body) if claim_text else 0.0
            sim = max(title_sim, claim_sim)
            if sim > 0.4:
                result.warn(
                    path.name, 1,
                    f"resembles refuted {entry_id}; read the argument that "
                    "killed it and say in 'Why this, why now' how this differs",
                )


def split_sentences_all(text):
    """Sentence splitter across the whole document (not per-section), used
    for the frequency/units check."""
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p for p in parts if p.strip()]


def default_files(repo_root: Path):
    paths = sorted(Path(p) for p in glob.glob(str(repo_root / "conjectures" / "*.md")))
    return [
        p for p in paths
        if p.name not in ("TEMPLATE.md", "README.md")
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Lint conjecture files.")
    parser.add_argument("files", nargs="*", help="Conjecture files to lint")
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-line output")
    parser.add_argument(
        "--ledger", default=None,
        help="Path to ledger/REFUTED.md (default: <repo_root>/ledger/REFUTED.md)",
    )
    args = parser.parse_args(argv)

    repo_root = find_repo_root(Path.cwd())

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = default_files(repo_root)

    ledger_path = Path(args.ledger) if args.ledger else repo_root / "ledger" / "REFUTED.md"
    ledger_entries = parse_ledger(ledger_path)

    result = Result()
    for f in files:
        if not f.exists():
            result.error(str(f), 1, "file not found")
            continue
        lint_file(f, repo_root, ledger_entries, result)

    if args.json:
        payload = {
            "errors": [
                {"file": f, "line": ln, "message": msg}
                for f, ln, msg in result.errors
            ],
            "warnings": [
                {"file": f, "line": ln, "message": msg}
                for f, ln, msg in result.warnings
            ],
            "error_count": len(result.errors),
            "warning_count": len(result.warnings),
        }
        print(json.dumps(payload, indent=2))
    else:
        if not args.quiet:
            for f, ln, msg in result.errors:
                print(f"ERROR {f}:{ln}  {msg}")
            for f, ln, msg in result.warnings:
                print(f"WARN  {f}:{ln}  {msg}")
        print(
            f"\n{len(files)} file(s) checked, "
            f"{len(result.errors)} error(s), {len(result.warnings)} warning(s)"
        )

    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
