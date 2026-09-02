#!/usr/bin/env python3
"""Backstop for the privacy firewall described in ETHICS.md.

This repository is PUBLIC and must never contain patient-identifiable
material. This tool is a safety net, not the primary control: the primary
control is not writing the material down here in the first place.

IMPORTANT FOR FUTURE CONTRIBUTORS: findings are redacted in the output on
purpose. A privacy linter that prints the private data it found into CI logs
has defeated itself — do not "fix" this by printing the raw match to make
debugging easier.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SKIP_NAMES = {".citation-cache.json"}

# --- Belgian national register number (rijksregisternummer) -----------------

# The optional "." separator means this pattern happily matches a slice out of
# the middle of a floating-point number: 172317.13142657682 in a simulation
# results file was reported as a national register number. The guards below
# reject a match that is part of a longer numeric literal (a digit immediately
# before, or a digit or ".digit" immediately after) while still allowing a
# genuine number followed by sentence-final punctuation. Allowlisting the
# offending files was the alternative and was rejected: the list would grow
# with every simulation run, and a privacy linter that people routinely add
# exceptions to stops being read.
NRN_RE = re.compile(
    r"(?<!\d)(?<!\d\.)"
    r"\b\d{2}[.\-\s]?\d{2}[.\-\s]?\d{2}[.\-\s]?\d{3}[.\-\s]?\d{2}\b"
    r"(?!\d)(?!\.\d)"
)


def nrn_checksum_valid(digits):
    """digits: an 11-character string of digits, no separators."""
    if len(digits) != 11 or not digits.isdigit():
        return False
    first9 = int(digits[:9])
    check = int(digits[9:11])
    candidates = []
    remainder = first9 % 97
    candidates.append(97 - remainder if remainder != 0 else 97)
    remainder2000 = (2000000000 + first9) % 97
    candidates.append(97 - remainder2000 if remainder2000 != 0 else 97)
    return check in candidates


# --- Belgian KBO / enterprise number (WARN only) -----------------------------

KBO_RE = re.compile(r"\bBE ?0\d{9}\b")

# --- Dates of birth -----------------------------------------------------------

DOB_DATE_RE = re.compile(
    r"\b\d{2}[/\-:]\d{2}[/\-:]\d{4}\b|\b\d{4}-\d{2}-\d{2}\b"
)
# A bare year in parentheses, "(19.." or "(20..", was originally in this list to
# catch "Name (1978)" birth-year notation. In a repository whose evidence base is
# mostly citations it matches a publication year on nearly every line, and a
# detector that fires constantly is a detector everyone learns to ignore. The
# explicit words below are the real signal; a date is only a date of birth if
# something nearby says so.
DOB_KEYWORDS = ["born", "DOB", "geboren", "birth", "date of birth", "geboortedatum", "°"]
DOB_WINDOW = 60

# --- Clinical identifier keywords ---------------------------------------------

CLINICAL_KEYWORDS = [
    "patient id", "patiënt", "dossiernummer", "rijksregister", "mutualiteit",
    "ziekenfonds", "NISS", "INSZ", "EMD", "nexuzhealth", "mynexuzhealth",
    "cozo", "vitalink", "sumehr", "medicatieschema",
]

# --- Hospital and insurer names -----------------------------------------------
# Small, deliberately narrow list of institutions that would identify a
# treating institution for an individual. Population-level phenotype
# description is fine; a named treating institution is not. Extend with
# care, not enthusiasm.

INSTITUTION_NAMES = [
    "jessa", "ziekenhuis oost-limburg", "ZOL", "virga jesse", "salvator",
    "UZ Leuven", "AZ", "DKV", "De Voorzorg", "VDAB", "mutualiteit",
]

# --- Local filesystem paths that leak a username ------------------------------

LEAKY_PATH_RE = re.compile(r"/Users/[a-z]+/|/home/[a-z]+/|C:\\Users\\")

# --- Credentials ---------------------------------------------------------------

CREDENTIAL_PATTERNS = [
    ("rqsty-key", re.compile(r"rqsty-[A-Za-z0-9]+")),
    ("openai-key", re.compile(r"sk-[A-Za-z0-9]{16,}")),
    ("github-token", re.compile(r"gh[pous]_[A-Za-z0-9]{20,}")),
    ("aws-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]

# --- Medication schedule shape --------------------------------------------------

MED_DOSE_RE = re.compile(r"\b\w+ \d+ ?mg\b", re.IGNORECASE)


def word_boundary_pattern(term):
    return re.compile(r"\b" + re.escape(term.strip()) + r"\b", re.IGNORECASE)


def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".git").exists():
            return candidate
    return start.resolve()


def is_binary(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            chunk = f.read(8000)
    except OSError:
        return True
    return b"\x00" in chunk


def read_text(path: Path):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def mask(match_text):
    """Redact a matched string for display: first 2 and last 2 chars kept,
    middle replaced with '*'. See module docstring for why this exists —
    do not change this to print the raw match."""
    n = len(match_text)
    if n <= 4:
        return "*" * n
    return match_text[:2] + ("*" * (n - 4)) + match_text[-2:]


def list_git_files(repo_root: Path, staged: bool):
    args = ["git", "diff", "--cached", "--name-only"] if staged else ["git", "ls-files"]
    try:
        out = subprocess.run(
            args, cwd=repo_root, capture_output=True, text=True, check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    files = [line.strip() for line in out.stdout.splitlines() if line.strip()]
    return [repo_root / f for f in files]


def walk_files(repo_root: Path):
    files = []
    for p in repo_root.rglob("*"):
        if not p.is_file():
            continue
        if ".git" in p.relative_to(repo_root).parts:
            continue
        files.append(p)
    return files


def load_allowlist(repo_root: Path):
    """.privacy-allow: lines of 'path:pattern-name' or 'path:*', # comments."""
    allow_path = repo_root / ".privacy-allow"
    allowed = {}
    if not allow_path.exists():
        return allowed
    for raw in allow_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        path_part, _, pattern_part = line.partition(":")
        path_part = path_part.strip()
        pattern_part = pattern_part.strip()
        allowed.setdefault(path_part, set()).add(pattern_part)
    return allowed


def load_names(repo_root: Path):
    names_path = repo_root / "tools" / ".privacy-names"
    if not names_path.exists():
        return None
    names = []
    for raw in names_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(line.lower())
    return names


class Finding:
    def __init__(self, path, line, pattern_name, matched_text, message, severity):
        self.path = path
        self.line = line
        self.pattern_name = pattern_name
        self.matched_text = matched_text
        self.message = message
        self.severity = severity


def line_number(text, index):
    return text.count("\n", 0, index) + 1


def scan_file(path: Path, rel_path: str, text: str, names, findings: list):
    # Belgian national register number
    for m in NRN_RE.finditer(text):
        digits = re.sub(r"\D", "", m.group(0))
        if len(digits) == 11 and nrn_checksum_valid(digits):
            findings.append(Finding(
                rel_path, line_number(text, m.start()), "belgian-nrn",
                m.group(0),
                f'matched "{mask(m.group(0))}"',
                "ERROR",
            ))

    # Belgian KBO / enterprise number
    for m in KBO_RE.finditer(text):
        findings.append(Finding(
            rel_path, line_number(text, m.start()), "belgian-kbo",
            m.group(0),
            f'matched "{mask(m.group(0))}"',
            "WARN",
        ))

    # Dates of birth
    for m in DOB_DATE_RE.finditer(text):
        window_start = max(0, m.start() - DOB_WINDOW)
        window_end = min(len(text), m.end() + DOB_WINDOW)
        window = text[window_start:window_end]
        window_lower = window.lower()
        if any(kw.lower() in window_lower for kw in DOB_KEYWORDS):
            findings.append(Finding(
                rel_path, line_number(text, m.start()), "date-of-birth",
                m.group(0),
                f'matched "{mask(m.group(0))}" near a birth-date keyword',
                "ERROR",
            ))

    # Clinical identifier keywords (per line)
    for lineno, line in enumerate(text.splitlines(), start=1):
        for kw in CLINICAL_KEYWORDS:
            if word_boundary_pattern(kw).search(line):
                findings.append(Finding(
                    rel_path, lineno, "clinical-keyword",
                    kw,
                    f'matched "{mask(kw)}"',
                    "ERROR",
                ))

    # Hospital and insurer names
    for lineno, line in enumerate(text.splitlines(), start=1):
        for name in INSTITUTION_NAMES:
            if word_boundary_pattern(name).search(line):
                findings.append(Finding(
                    rel_path, lineno, "institution-name",
                    name,
                    f'matched "{mask(name)}" — population-level phenotype '
                    "description is fine, a named treating institution is not",
                    "ERROR",
                ))

    # Personal names
    if names:
        for lineno, line in enumerate(text.splitlines(), start=1):
            for name in names:
                if word_boundary_pattern(name).search(line):
                    findings.append(Finding(
                        rel_path, lineno, "personal-name",
                        name,
                        f'matched "{mask(name)}"',
                        "ERROR",
                    ))

    # Local filesystem paths leaking a username
    for m in LEAKY_PATH_RE.finditer(text):
        findings.append(Finding(
            rel_path, line_number(text, m.start()), "leaky-path",
            m.group(0),
            f'matched "{mask(m.group(0))}"',
            "ERROR",
        ))

    # Credentials
    for pattern_name, regex in CREDENTIAL_PATTERNS:
        for m in regex.finditer(text):
            findings.append(Finding(
                rel_path, line_number(text, m.start()), f"credential:{pattern_name}",
                m.group(0),
                f'matched "{mask(m.group(0))}"',
                "ERROR",
            ))

    # Medication schedule shape
    med_matches = set(m.group(0) for m in MED_DOSE_RE.finditer(text))
    if len(med_matches) >= 3:
        findings.append(Finding(
            rel_path, 1, "medication-list",
            ", ".join(sorted(med_matches)),
            "reads like an individual medication list; population-level "
            "statements should not enumerate a personal regimen "
            f"({len(med_matches)} distinct drug-dose patterns found)",
            "WARN",
        ))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Lint the repository for private/identifiable material.")
    parser.add_argument("paths", nargs="*", help="Files to lint (default: all tracked files)")
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-finding output")
    parser.add_argument("--staged", action="store_true", help="Lint only git-staged files")
    args = parser.parse_args(argv)

    repo_root = find_repo_root(Path.cwd())

    if args.paths:
        files = [Path(p) for p in args.paths]
    elif args.staged:
        files = list_git_files(repo_root, staged=True) or []
    else:
        files = list_git_files(repo_root, staged=False)
        if files is None:
            files = walk_files(repo_root)

    allowlist = load_allowlist(repo_root)
    names = load_names(repo_root)
    names_file_present = names is not None

    all_findings = []
    suppressed_count = 0

    for f in files:
        if not f.exists() or not f.is_file():
            continue
        if f.name in SKIP_NAMES:
            continue
        try:
            rel_path = str(f.resolve().relative_to(repo_root))
        except ValueError:
            rel_path = str(f)
        if ".git" in Path(rel_path).parts:
            continue
        if is_binary(f):
            continue
        text = read_text(f)
        if text is None:
            continue

        file_allow = allowlist.get(rel_path, set())
        if "*" in file_allow:
            # whole file skipped, but every finding it would have produced
            # is not counted since we never scan it. That is intentional:
            # a whole-file allow is a deliberate, visible decision, not a
            # silent one, and it is recorded by name in .privacy-allow.
            continue

        file_findings = []
        scan_file(f, rel_path, text, names, file_findings)

        for finding in file_findings:
            if finding.pattern_name in file_allow:
                suppressed_count += 1
                continue
            all_findings.append(finding)

    errors = [fnd for fnd in all_findings if fnd.severity == "ERROR"]
    warnings = [fnd for fnd in all_findings if fnd.severity == "WARN"]

    if args.json:
        payload = {
            "findings": [
                {
                    "path": fnd.path,
                    "line": fnd.line,
                    "pattern": fnd.pattern_name,
                    "severity": fnd.severity,
                    "message": fnd.message,
                }
                for fnd in all_findings
            ],
            "error_count": len(errors),
            "warning_count": len(warnings),
            "suppressed_count": suppressed_count,
            "names_file_checked": names_file_present,
        }
        print(json.dumps(payload, indent=2))
    else:
        if not args.quiet:
            for fnd in all_findings:
                print(f"{fnd.severity} {fnd.path}:{fnd.line}  {fnd.pattern_name}  {fnd.message}")
        print(
            f"\n{len(files)} file(s) checked, {len(errors)} error(s), "
            f"{len(warnings)} warning(s), {suppressed_count} suppressed by "
            ".privacy-allow"
        )
        if not names_file_present:
            print(
                "NOTE: tools/.privacy-names not found; personal-name "
                "detection did not run."
            )

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
