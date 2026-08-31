#!/usr/bin/env python3
"""Build the programme dashboard, `docs/index.html`, from the repository.

Every number on the dashboard is derived from a file that already exists:
conjecture front matter, the ledgers, `pipeline/reviews/`, the evidence base
and `PROGRAMME.md`. Nothing here is hand-maintained, on the same principle as
`ledger/REFUTED.md` rule 6 and EPISTEMICS.md rule 11: a number that is not
read from its source is a number someone will eventually have to retract.

Standard library only, so this runs on a bare CI runner exactly like the
other tools/ scripts. The output is a single self-contained HTML file: inline
CSS, inline SVG, no CDN, no JavaScript framework, so it works offline and
from `file://`.

    tools/build-dashboard.py                 # write docs/index.html
    tools/build-dashboard.py --check         # exit 1 if docs/index.html is stale

`--check` is meant for CI: it regenerates into a temp file and diffs against
the committed output, ignoring only the "generated at" wall-clock stamp,
which is the one field that is expected to differ between two runs of an
identical repository state.
"""

from __future__ import annotations

import argparse
import datetime
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# --------------------------------------------------------------------------
# repo discovery
# --------------------------------------------------------------------------


def find_repo_root(start: Path) -> Path:
    cur = start.resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / ".git").exists():
            return candidate
    return start.resolve()


# --------------------------------------------------------------------------
# small text helpers, shared by every parser below
# --------------------------------------------------------------------------

MD_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
MD_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")
MD_CODE_RE = re.compile(r"`([^`]+)`")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def strip_md(text: str) -> str:
    """Remove the handful of markdown constructs this repository actually
    uses, for display as plain inline text. Not a general markdown parser;
    it does not need to be one."""
    text = HTML_COMMENT_RE.sub("", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = MD_BOLD_RE.sub(r"\1", text)
    text = MD_ITALIC_RE.sub(r"\1", text)
    text = MD_CODE_RE.sub(r"\1", text)
    return text


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def clean(text: str) -> str:
    """strip markdown, collapse whitespace, then escape for HTML."""
    return esc(" ".join(strip_md(text).split()))


def split_sentences(text: str) -> list[str]:
    stripped = " ".join(strip_md(text).split())
    if not stripped:
        return []
    parts = re.split(r"(?<=[.!?])\s+", stripped)
    return [p for p in parts if p.strip()]


def first_sentence(text: str, default: str = "") -> str:
    sentences = split_sentences(text)
    return sentences[0] if sentences else default


LEADING_BOLD_LABEL_RE = re.compile(r"^\*\*([A-Za-z][A-Za-z ]*)\.\*\*\s*")


def drop_leading_bold_label(text: str) -> str:
    """`ledger/DECISIONS.md` opens paragraphs with a bold label like
    `**Decision.**` or `**Why.**`. Left in place, the naive sentence
    splitter reads the label's own full stop as the end of sentence one.
    Dropping the label before splitting fixes that without a smarter
    (and heavier) sentence splitter."""
    return LEADING_BOLD_LABEL_RE.sub("", text.strip())


def find_section(body: str, heading: str, level: str = "##") -> str | None:
    """Find a `<level> Heading` section's body (up to the next heading of the
    same or higher level). Returns raw text, or None if not found."""
    pattern = re.compile(
        r"^" + re.escape(level) + r"\s+" + re.escape(heading) + r"\s*$",
        re.MULTILINE,
    )
    m = pattern.search(body)
    if not m:
        return None
    start = m.end()
    next_m = re.search(r"^#{1,%d}\s+" % len(level), body[start:], re.MULTILINE)
    end = start + next_m.start() if next_m else len(body)
    return body[start:end]


def truncate(text: str, n: int) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


# --------------------------------------------------------------------------
# A. conjectures
# --------------------------------------------------------------------------

FRONT_MATTER_KEYS = [
    "id", "title", "branch", "status", "prior", "posterior",
    "lineage", "supersedes", "created", "bears_on",
]


def parse_front_matter(text: str) -> dict:
    """The same minimal `key: value` reader as tools/lint-conjecture.py.
    Deliberately not YAML: the front matter here is one line per key with no
    nesting, and a real YAML parser is a dependency this tool does not need."""
    lines = text.splitlines()
    data = {}
    if not lines or lines[0].strip() != "---":
        return data
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return data
    for i in range(1, end_idx):
        stripped = lines[i].strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        data[key.strip()] = value.strip()
    return data


ID_IN_TEXT_RE = re.compile(r"C-\d{3}")


def parse_conjectures(root: Path) -> list[dict]:
    paths = sorted(root.glob("conjectures/C-*.md"))
    out = []
    for path in paths:
        if path.name in ("TEMPLATE.md", "README.md"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = parse_front_matter(text)
        cid = fm.get("id", "") or (
            ID_IN_TEXT_RE.match(path.stem).group(0)
            if ID_IN_TEXT_RE.match(path.stem)
            else path.stem
        )
        claim = find_section(text, "Claim") or ""
        forbidden = find_section(text, "Forbidden observation") or ""
        bears_on = [
            b.strip() for b in fm.get("bears_on", "").split(",") if b.strip()
        ]
        parents = sorted(set(
            ID_IN_TEXT_RE.findall(fm.get("lineage", "") or "")
            + ID_IN_TEXT_RE.findall(fm.get("supersedes", "") or "")
        ))
        out.append({
            "id": cid,
            "title": fm.get("title", "").strip(),
            "branch": fm.get("branch", "").strip(),
            "status": fm.get("status", "").strip(),
            "prior": fm.get("prior", "").strip(),
            "posterior": fm.get("posterior", "").strip(),
            "created": fm.get("created", "").strip(),
            "bears_on": bears_on,
            "parents": parents,
            "claim": first_sentence(claim),
            "forbidden": " ".join(strip_md(forbidden).split()),
            "path": path,
            "relpath": f"../conjectures/{path.name}",
        })
    out.sort(key=lambda c: c["id"])
    return out


# --------------------------------------------------------------------------
# B. ledgers
# --------------------------------------------------------------------------


def parse_refuted(root: Path) -> list[dict]:
    path = root / "ledger" / "REFUTED.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    entries = []
    matches = list(re.finditer(
        r"^###\s+(C-\d{3})\s*[—-]\s*(.+)$", text, re.MULTILINE,
    ))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        entries.append({
            "id": m.group(1),
            "title": m.group(2).strip(),
            "summary": first_sentence(body, "(no summary sentence found)"),
        })
    return entries


DECISION_HEADING_RE = re.compile(
    r"^##\s+(D-\d{3})\.\s*(.+?)\s*$", re.MULTILINE,
)


def parse_decisions(root: Path) -> list[dict]:
    seen = {}
    for name in ("ledger/DECISIONS.md", "ledger/OPEN.md"):
        path = root / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = list(DECISION_HEADING_RE.finditer(text))
        for i, m in enumerate(matches):
            did = m.group(1)
            if did in seen:
                continue
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[start:end]
            # Skip a leading blockquote note (an amendment) and summarise the
            # decision itself, which is the first non-quoted paragraph.
            paragraphs = [
                p for p in re.split(r"\n\s*\n", body)
                if p.strip() and not p.strip().startswith(">")
            ]
            summary = (
                first_sentence(drop_leading_bold_label(paragraphs[0]))
                if paragraphs else ""
            )
            seen[did] = {
                "id": did,
                "title": m.group(2).strip(),
                "summary": summary,
                "source": name,
            }
    return [seen[k] for k in sorted(seen)]


# --------------------------------------------------------------------------
# C. panel runs
# --------------------------------------------------------------------------

VERDICT_RE = re.compile(
    r"VERDICT:\s*([A-Z][A-Z —-]*?)(?:\s*[—–-]\s*(.*))?\s*$",
    re.MULTILINE,
)
REVIEWER_RE = re.compile(r"Reviewer:\s*`([^`]+)`")
LAB_RE = re.compile(r"\blab\s+(\S+)")
TIMESTAMP_RE = re.compile(
    r"^>\s*(\d{4}-\d{2}-\d{2}T[\d:+\-]+)", re.MULTILINE,
)
RUN_STAMP_RE = re.compile(r"^(\d{8}T\d{6}Z)$")


def _verdict_from_text(text: str) -> tuple[str, str]:
    """Last VERDICT: line wins, matching tools/review.sh's own convention."""
    matches = list(VERDICT_RE.finditer(text))
    if not matches:
        return "NO VERDICT LINE", ""
    m = matches[-1]
    return m.group(1).strip(), (m.group(2) or "").strip()


def _parse_verdict_file(path: Path, label: str) -> dict | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    reviewer_m = REVIEWER_RE.search(text)
    lab_m = LAB_RE.search(text)
    ts_m = TIMESTAMP_RE.search(text)
    word, detail = _verdict_from_text(text)
    return {
        "label": label,
        "model": reviewer_m.group(1) if reviewer_m else "?",
        "lab": lab_m.group(1) if lab_m else "?",
        "date": ts_m.group(1) if ts_m else "",
        "word": word,
        "detail": detail,
    }


def parse_panel_runs(root: Path) -> tuple[list[dict], int]:
    """Walk pipeline/reviews/<conjecture-id>/<timestamp>/. Each timestamped
    directory is one review run. Returns (rows, run_count).

    Real runs so far are triage-only: `review.sh` always writes one
    `gate-<gate>.md` or `vote-<model>.md` file per model call, and those
    files carry the reviewer, laboratory and verdict directly, so they are
    read as the source of truth. `verdicts.txt`, `votes.txt` and
    `SUMMARY.md`, when a full panel has actually run, are read too, as a
    fallback for any row a per-file scan would otherwise miss."""
    reviews_dir = root / "pipeline" / "reviews"
    rows = []
    run_count = 0
    if not reviews_dir.is_dir():
        return rows, run_count

    for conj_dir in sorted(reviews_dir.iterdir()):
        if not conj_dir.is_dir():
            continue
        cid_m = ID_IN_TEXT_RE.match(conj_dir.name)
        cid = cid_m.group(0) if cid_m else conj_dir.name
        for run_dir in sorted(conj_dir.iterdir()):
            if not run_dir.is_dir() or not RUN_STAMP_RE.match(run_dir.name):
                continue
            run_count += 1
            fallback_date = (
                f"{run_dir.name[0:4]}-{run_dir.name[4:6]}-{run_dir.name[6:8]}"
            )
            seen_labels = set()

            for gate_file in sorted(run_dir.glob("gate-*.md")):
                label = gate_file.stem[len("gate-"):]
                row = _parse_verdict_file(gate_file, label)
                row.update({
                    "conjecture": cid,
                    "date": row["date"][:10] or fallback_date,
                    "link": f"../pipeline/reviews/{conj_dir.name}/{run_dir.name}/{gate_file.name}",
                })
                rows.append(row)
                seen_labels.add(label)

            for vote_file in sorted(run_dir.glob("vote-*.md")):
                row = _parse_verdict_file(vote_file, "panel vote")
                row.update({
                    "conjecture": cid,
                    "date": row["date"][:10] or fallback_date,
                    "link": f"../pipeline/reviews/{conj_dir.name}/{run_dir.name}/{vote_file.name}",
                })
                rows.append(row)

            # Fallback: an aggregated verdicts.txt/votes.txt line with no
            # matching per-file verdict (e.g. a run recorded only that way).
            for agg_name, agg_label in (("verdicts.txt", None), ("votes.txt", "panel vote")):
                agg_path = run_dir / agg_name
                if not agg_path.exists():
                    continue
                for line in agg_path.read_text(encoding="utf-8", errors="replace").splitlines():
                    if not line.strip():
                        continue
                    parts = line.split()
                    if agg_label is None:
                        gate, model = parts[0], parts[1] if len(parts) > 1 else "?"
                    else:
                        gate, model = agg_label, parts[0]
                    if gate in seen_labels:
                        continue
                    word, detail = _verdict_from_text(line)
                    rows.append({
                        "label": gate, "model": model, "lab": "?",
                        "date": fallback_date, "word": word, "detail": detail,
                        "conjecture": cid,
                        "link": f"../pipeline/reviews/{conj_dir.name}/{run_dir.name}/{agg_name}",
                    })

    rows.sort(key=lambda r: (r["date"], r["conjecture"], r["label"]), reverse=True)
    return rows, run_count


VERDICT_COLOUR = {
    "green": {"PASS", "NOT REFUTED"},
    "amber": {"MAJOR"},
    "red": {"FATAL", "REFUTED", "VACUOUS", "CHEAP KILL", "CHEAP KILL AVAILABLE"},
}


def verdict_colour(word: str) -> str:
    w = word.upper()
    for colour, words in VERDICT_COLOUR.items():
        if any(w == v or w.startswith(v) for v in words):
            return colour
    if w == "MINOR":
        return "neutral"
    return "neutral"


# --------------------------------------------------------------------------
# D. evidence base
# --------------------------------------------------------------------------

IDENTIFIER_RE = re.compile(
    r"10\.\d{4,9}/\S+|PMID\s*:?\s*\d+|arXiv:\S+|NCT\d+", re.IGNORECASE,
)
RETRACTION_HEADING_RE = re.compile(
    r"^>?\s*#{1,6}\s+Retraction\b", re.MULTILINE | re.IGNORECASE,
)


def parse_evidence(root: Path) -> list[dict]:
    paths = sorted((root / "evidence").glob("*.md"))
    out = []
    for path in paths:
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        first_line = text.splitlines()[0].lstrip("#").strip() if text else path.stem
        out.append({
            "id": path.stem.split("-")[0].upper(),
            "title": first_line,
            "established": len(re.findall(r"\bESTABLISHED\b", text)),
            "contested": len(re.findall(r"\bCONTESTED\b", text)),
            "speculative": len(re.findall(r"\bSPECULATIVE\b", text)),
            "identifiers": len(IDENTIFIER_RE.findall(text)),
            "unverified": len(re.findall(r"\[UNVERIFIED\]", text)),
            "retracted": bool(RETRACTION_HEADING_RE.search(text)),
            "relpath": f"../evidence/{path.name}",
        })
    return out


# --------------------------------------------------------------------------
# E. git
# --------------------------------------------------------------------------


def get_git_info(root: Path) -> dict:
    def run(*args):
        return subprocess.run(
            ["git", *args], cwd=root, capture_output=True, text=True, timeout=10,
        )

    info = {"sha": None, "commit_count": None, "last_commit_date": None}
    try:
        r = run("rev-parse", "--short", "HEAD")
        if r.returncode == 0:
            info["sha"] = r.stdout.strip()
        r = run("rev-list", "--count", "HEAD")
        if r.returncode == 0:
            info["commit_count"] = r.stdout.strip()
        r = run("log", "-1", "--format=%cI")
        if r.returncode == 0 and r.stdout.strip():
            dt = datetime.datetime.fromisoformat(r.stdout.strip())
            info["last_commit_date"] = dt.astimezone(datetime.timezone.utc).strftime(
                "%Y-%m-%d",
            )
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    return info


# --------------------------------------------------------------------------
# F. PROGRAMME.md — hard core and protective belt
# --------------------------------------------------------------------------

HC_HEADING_RE = re.compile(r"^###\s+(HC-\d+)\.\s+(.+?)\s*$", re.MULTILINE)
PB_ITEM_RE = re.compile(
    r"^-\s+(PB-\d+)\.\s*(.*?)(?=\n-\s+PB-\d+\.|\Z)", re.MULTILINE | re.DOTALL,
)


def parse_programme(root: Path) -> tuple[list[dict], list[dict]]:
    path = root / "PROGRAMME.md"
    if not path.exists():
        return [], []
    text = path.read_text(encoding="utf-8", errors="replace")

    hard_core = []
    hc_section = find_section(text, "Hard core") or ""
    matches = list(HC_HEADING_RE.finditer(hc_section))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(hc_section)
        body = hc_section[start:end]
        hard_core.append({
            "id": m.group(1),
            "title": m.group(2).strip(),
            "summary": first_sentence(body),
        })

    protective_belt = []
    pb_section = find_section(text, "Protective belt") or ""
    for m in PB_ITEM_RE.finditer(pb_section):
        pid = m.group(1)
        text_block = " ".join(m.group(2).split())
        protective_belt.append({
            "id": pid,
            "summary": first_sentence(text_block, text_block),
        })

    return hard_core, protective_belt


def conjectures_bearing_on(conjectures: list[dict], item_id: str) -> list[dict]:
    return [c for c in conjectures if item_id in c["bears_on"]]


# --------------------------------------------------------------------------
# SVG: conjecture lineage graph
# --------------------------------------------------------------------------

BRANCH_COLOUR = {
    # Three hues, and lightness varied deliberately so the encoding survives
    # a greyscale printout: A is mid-blue, B is light amber, C is dark plum.
    "A": {"fill": "#2b5d8c", "stroke": "#193a58", "text": "#eaf2fb"},
    "B": {"fill": "#c98a1e", "stroke": "#8a5e12", "text": "#241a05"},
    "C": {"fill": "#6e1f4a", "stroke": "#42112c", "text": "#f6e8ef"},
}
BRANCH_FALLBACK = {"fill": "#555b66", "stroke": "#33373d", "text": "#f0f1f3"}

STATUS_DASH = {
    "draft": "6,4",
    "in-panel": "6,4",
    "open": None,
    "promoted": None,
    "wounded": "1.5,3",
    "refuted": None,
}

NODE_W, NODE_H = 168, 60
COL_GAP, ROW_GAP = 72, 22
MARGIN = 32


def build_lineage_svg(conjectures: list[dict]) -> str:
    if not conjectures:
        return (
            '<p class="empty-state">No conjectures yet. This section will '
            "draw itself as soon as one exists.</p>"
        )

    by_id = {c["id"]: c for c in conjectures}
    depth_memo: dict[str, int] = {}

    def depth_of(cid: str, visiting: set) -> int:
        if cid in depth_memo:
            return depth_memo[cid]
        if cid in visiting:
            depth_memo[cid] = 0
            return 0
        visiting.add(cid)
        parents = [p for p in by_id[cid]["parents"] if p in by_id]
        d = 0 if not parents else 1 + max(depth_of(p, visiting) for p in parents)
        visiting.discard(cid)
        depth_memo[cid] = d
        return d

    columns: dict[int, list[dict]] = {}
    for c in conjectures:
        d = depth_of(c["id"], set())
        columns.setdefault(d, []).append(c)
    for col in columns.values():
        col.sort(key=lambda c: c["id"])

    max_col_len = max(len(v) for v in columns.values())
    n_cols = max(columns) + 1
    width = MARGIN * 2 + n_cols * NODE_W + (n_cols - 1) * COL_GAP
    col_height = max_col_len * NODE_H + (max_col_len - 1) * ROW_GAP
    height = MARGIN * 2 + col_height

    positions = {}
    for d, col in columns.items():
        col_h = len(col) * NODE_H + (len(col) - 1) * ROW_GAP
        y0 = MARGIN + (col_height - col_h) / 2
        x = MARGIN + d * (NODE_W + COL_GAP)
        for i, c in enumerate(col):
            y = y0 + i * (NODE_H + ROW_GAP)
            positions[c["id"]] = (x, y)

    parts = [
        f'<svg viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Conjecture lineage graph" class="lineage-svg" '
        f'xmlns="http://www.w3.org/2000/svg">',
        "<defs>",
        '<marker id="lineage-arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="lineage-arrowhead"/></marker>',
        "</defs>",
    ]

    # edges first, so nodes sit on top
    for c in conjectures:
        cx, cy = positions[c["id"]]
        for pid in c["parents"]:
            if pid not in positions:
                continue
            px, py = positions[pid]
            x1, y1 = px + NODE_W, py + NODE_H / 2
            x2, y2 = cx, cy + NODE_H / 2
            mx = (x1 + x2) / 2
            parts.append(
                f'<path d="M{x1:.1f},{y1:.1f} C{mx:.1f},{y1:.1f} '
                f'{mx:.1f},{y2:.1f} {x2:.1f},{y2:.1f}" class="lineage-edge" '
                f'marker-end="url(#lineage-arrow)"/>'
            )

    for c in conjectures:
        x, y = positions[c["id"]]
        colours = BRANCH_COLOUR.get(c["branch"], BRANCH_FALLBACK)
        dash = STATUS_DASH.get(c["status"])
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        refuted = c["status"] == "refuted"
        group_opacity = ' opacity="0.55"' if refuted else ""
        title_line = truncate(c["title"], 24)
        text_deco = ' text-decoration="line-through"' if refuted else ""

        parts.append(f'<a href="{esc(c["relpath"])}">')
        parts.append(f'<g{group_opacity}>')
        parts.append(f"<title>{clean(c['title'] + ' (' + c['status'] + ')')}</title>")
        parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{NODE_W}" height="{NODE_H}" '
            f'rx="9" fill="{colours["fill"]}" stroke="{colours["stroke"]}" '
            f'stroke-width="2"{dash_attr}/>'
        )
        # branch badge, so colour is never the only signal
        parts.append(
            f'<circle cx="{x + NODE_W - 15:.1f}" cy="{y + 15:.1f}" r="10" '
            f'fill="{colours["stroke"]}"/>'
            f'<text x="{x + NODE_W - 15:.1f}" y="{y + 19:.1f}" '
            f'text-anchor="middle" class="lineage-badge">{esc(c["branch"] or "?")}</text>'
        )
        parts.append(
            f'<text x="{x + 12:.1f}" y="{y + 24:.1f}" fill="{colours["text"]}" '
            f'class="lineage-id"{text_deco}>{esc(c["id"])}</text>'
        )
        parts.append(
            f'<text x="{x + 12:.1f}" y="{y + 44:.1f}" fill="{colours["text"]}" '
            f'class="lineage-title"{text_deco}>{clean(title_line)}</text>'
        )
        parts.append("</g></a>")

    parts.append("</svg>")
    return "".join(parts)


# --------------------------------------------------------------------------
# SVG: calibration plot
# --------------------------------------------------------------------------

CAL_SIZE = 480
CAL_MARGIN = 56


def _cal_xy(value: float) -> tuple[float, float]:
    plot = CAL_SIZE - 2 * CAL_MARGIN
    x = CAL_MARGIN + value * plot
    y = CAL_MARGIN + (1 - value) * plot
    return x, y


def build_calibration_svg(conjectures: list[dict]) -> str:
    panelled = []
    unpanelled = []
    for c in conjectures:
        try:
            prior = float(c["prior"])
        except (TypeError, ValueError):
            continue
        if c["posterior"]:
            try:
                posterior = float(c["posterior"])
            except ValueError:
                posterior = None
        else:
            posterior = None
        if posterior is None:
            unpanelled.append((c, prior))
        else:
            panelled.append((c, prior, posterior))

    parts = [
        f'<svg viewBox="0 0 {CAL_SIZE} {CAL_SIZE}" role="img" '
        f'aria-label="Calibration plot: prior against posterior" '
        f'class="cal-svg" xmlns="http://www.w3.org/2000/svg">',
        "<defs>",
        '<marker id="cal-arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" class="cal-arrowhead"/></marker>',
        "</defs>",
    ]

    x0, y0 = _cal_xy(0)
    x1, y1 = _cal_xy(1)
    # axes
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y1}" class="cal-axis"/>')
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y0}" class="cal-axis"/>')
    # diagonal, the honesty line
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" class="cal-diagonal"/>')
    for v, label in ((0.0, "0"), (0.5, "0.5"), (1.0, "1")):
        vx, _ = _cal_xy(v)
        _, vy = _cal_xy(v)
        parts.append(f'<text x="{vx}" y="{y0 + 18}" class="cal-tick">{label}</text>')
        parts.append(f'<text x="{x0 - 10}" y="{vy + 4}" text-anchor="end" class="cal-tick">{label}</text>')
    parts.append(f'<text x="{(x0 + x1) / 2}" y="{CAL_SIZE - 12}" text-anchor="middle" class="cal-axis-label">prior</text>')
    parts.append(
        f'<text x="{16}" y="{(y0 + y1) / 2}" text-anchor="middle" '
        f'transform="rotate(-90 16 {(y0 + y1) / 2})" class="cal-axis-label">posterior</text>'
    )

    for c, prior in unpanelled:
        px, py = _cal_xy(prior)
        parts.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" class="cal-point-hollow">'
            f'<title>{clean(c["id"] + ": prior " + c["prior"] + ", no posterior yet")}</title>'
            f"</circle>"
        )

    for c, prior, posterior in panelled:
        x1a, y1a = _cal_xy(prior)
        x2a, y2a = _cal_xy(posterior)
        moved = posterior > prior
        parts.append(
            f'<line x1="{x1a:.1f}" y1="{y1a:.1f}" x2="{x2a:.1f}" y2="{y2a:.1f}" '
            f'class="{"cal-moved-up" if moved else "cal-moved-down"}" '
            f'marker-end="url(#cal-arrow)"/>'
        )
        parts.append(
            f'<circle cx="{x2a:.1f}" cy="{y2a:.1f}" r="6" class="cal-point">'
            f'<title>{clean(c["id"] + ": prior " + c["prior"] + " -> posterior " + c["posterior"])}</title>'
            f"</circle>"
        )

    parts.append("</svg>")
    svg = "".join(parts)

    if unpanelled and not panelled:
        note = (
            "No conjecture has completed a panel yet. The hollow marks are "
            "priors sitting on the diagonal, waiting to move."
        )
    elif not panelled and not unpanelled:
        note = "No conjectures with a stated prior yet."
    else:
        note = ""
    return svg, note


# --------------------------------------------------------------------------
# SVG: small evidence stacked bar
# --------------------------------------------------------------------------


def build_evidence_bar_svg(established: int, contested: int, speculative: int) -> str:
    total = established + contested + speculative
    bar_w, bar_h = 180, 14
    if total == 0:
        return (
            f'<svg viewBox="0 0 {bar_w} {bar_h}" role="img" '
            f'aria-label="no ESTABLISHED/CONTESTED/SPECULATIVE markers found" '
            f'class="ev-bar" xmlns="http://www.w3.org/2000/svg">'
            f'<rect width="{bar_w}" height="{bar_h}" rx="3" class="ev-bar-empty"/>'
            f"</svg>"
        )
    segs = [
        (established, "ev-bar-established", "established"),
        (contested, "ev-bar-contested", "contested"),
        (speculative, "ev-bar-speculative", "speculative"),
    ]
    parts = [
        f'<svg viewBox="0 0 {bar_w} {bar_h}" role="img" '
        f'aria-label="established {established}, contested {contested}, '
        f'speculative {speculative}" class="ev-bar" '
        f'xmlns="http://www.w3.org/2000/svg">'
    ]
    x = 0.0
    for count, cls, label in segs:
        w = bar_w * count / total
        if w > 0:
            parts.append(
                f'<rect x="{x:.1f}" y="0" width="{w:.1f}" height="{bar_h}" '
                f'class="{cls}"><title>{label}: {count}</title></rect>'
            )
        x += w
    parts.append("</svg>")
    return "".join(parts)


# --------------------------------------------------------------------------
# HTML assembly
# --------------------------------------------------------------------------

STATUS_ORDER = ["draft", "in-panel", "open", "wounded", "refuted", "promoted"]


def status_counts(conjectures: list[dict]) -> dict:
    counts = {s: 0 for s in STATUS_ORDER}
    for c in conjectures:
        if c["status"] in counts:
            counts[c["status"]] += 1
    return counts


def build_html(root: Path, generated_at: datetime.datetime) -> str:
    conjectures = parse_conjectures(root)
    refuted = parse_refuted(root)
    decisions = parse_decisions(root)
    panel_rows, run_count = parse_panel_runs(root)
    evidence = parse_evidence(root)
    hard_core, protective_belt = parse_programme(root)
    git_info = get_git_info(root)

    counts = status_counts(conjectures)
    total_identifiers = sum(e["identifiers"] for e in evidence)

    # ---- A. header --------------------------------------------------
    ts_str = generated_at.strftime("%Y-%m-%d %H:%M UTC")
    sha = git_info["sha"] or "unknown"
    header = f"""
<header class="page-header">
  <h1>Pain as Information — programme dashboard</h1>
  <p class="thesis">Chronic neuropathic pain as a signalling problem, tested by trying to kill the idea, not to confirm it.</p>
  <p class="meta">
    Generated <span id="generated-ts">{ts_str}</span> from repository state
    at commit <code>{esc(sha)}</code>
    ({esc(str(git_info["commit_count"] or "?"))} commits,
    last touched {esc(git_info["last_commit_date"] or "unknown")}).
    This page is built, not written: every number above is read from a file
    in this repository by <code>tools/build-dashboard.py</code>. Editing it
    by hand accomplishes nothing; the next run overwrites it.
  </p>
</header>
"""

    # ---- B. status strip ---------------------------------------------
    status_chips = "".join(
        f'<div class="chip"><span class="chip-n">{counts[s]}</span>'
        f'<span class="chip-label">{esc(s)}</span></div>'
        for s in STATUS_ORDER
    )
    strip = f"""
<section class="status-strip" aria-label="Programme status at a glance">
  <div class="stat"><span class="stat-n">{len(conjectures)}</span><span class="stat-label">conjectures</span></div>
  <div class="status-chips">{status_chips}</div>
  <div class="stat"><span class="stat-n">{run_count}</span><span class="stat-label">review runs recorded</span></div>
  <div class="stat"><span class="stat-n">{len(evidence)}</span><span class="stat-label">evidence briefs</span></div>
  <div class="stat"><span class="stat-n">{total_identifiers}</span><span class="stat-label">citation identifiers found</span></div>
  <div class="stat"><span class="stat-n">{len(decisions)}</span><span class="stat-label">decisions recorded</span></div>
</section>
"""

    # ---- C. lineage graph ---------------------------------------------
    lineage_svg = build_lineage_svg(conjectures)
    lineage_section = f"""
<section id="lineage" aria-labelledby="lineage-h">
  <h2 id="lineage-h">Conjecture lineage</h2>
  <p class="section-note">
    Columns are generation depth (roots on the left); an edge points from a
    conjecture to the one it was rebuilt from (<code>lineage:</code> or
    <code>supersedes:</code>). Colour is branch (A classical, B quantum
    instrument, C quantum-in-tissue) and is repeated as a letter badge so it
    survives greyscale. Border: solid = open/promoted, dashed = draft/in-panel,
    dotted = wounded. A struck-through, faded label is refuted.
  </p>
  <div class="svg-wrap">{lineage_svg}</div>
</section>
"""

    # ---- D. calibration plot -------------------------------------------
    cal_svg, cal_note = build_calibration_svg(conjectures)
    cal_note_html = f'<p class="section-note cal-note">{esc(cal_note)}</p>' if cal_note else ""
    calibration_section = f"""
<section id="calibration" aria-labelledby="cal-h">
  <h2 id="cal-h">Calibration: prior against posterior</h2>
  <p class="section-note cal-honesty">
    EPISTEMICS.md rule 5: <strong>a programme where every posterior exceeds
    every prior is a programme that is not learning.</strong> This plot is
    the honesty check on that rule, and it is meant to be looked at every
    time it changes, not just once.
  </p>
  <p class="section-note">
    Filled points are panelled conjectures: the arrow runs from (prior,
    prior) on the diagonal to (prior, posterior). Hollow points on the
    diagonal have a prior and no posterior yet.
  </p>
  <div class="svg-wrap">{cal_svg}</div>
  {cal_note_html}
</section>
"""

    # ---- E. hard core board ---------------------------------------------
    def board_item(item_id: str, title: str, summary: str) -> str:
        bearers = conjectures_bearing_on(conjectures, item_id)
        if bearers:
            links = ", ".join(
                f'<a href="{esc(c["relpath"])}">{esc(c["id"])}</a>' for c in bearers
            )
            bears_html = f'<p class="bears-on">Bears on this: {links}</p>'
        else:
            bears_html = (
                '<p class="bears-on empty-inline">No conjecture attached yet.</p>'
            )
        title_html = f"<strong>{esc(item_id)}.</strong> {esc(title)}" if title else esc(item_id)
        return f"""
    <li class="board-item">
      <p class="board-title">{title_html}</p>
      <p class="board-summary">{esc(summary)}</p>
      {bears_html}
    </li>"""

    hc_html = "".join(board_item(h["id"], h["title"], h["summary"]) for h in hard_core)
    pb_html = "".join(board_item(p["id"], "", p["summary"]) for p in protective_belt)
    if not hard_core and not protective_belt:
        board_body = '<p class="empty-state">PROGRAMME.md defines no hard core or protective belt yet.</p>'
    else:
        board_body = f"""
  <div class="board-columns">
    <div>
      <h3>Hard core</h3>
      <ul class="board-list">{hc_html or '<li class="empty-state">none found</li>'}</ul>
    </div>
    <div>
      <h3>Protective belt</h3>
      <ul class="board-list">{pb_html or '<li class="empty-state">none found</li>'}</ul>
    </div>
  </div>"""
    hardcore_section = f"""
<section id="hardcore" aria-labelledby="hardcore-h">
  <h2 id="hardcore-h">Hard core and protective belt</h2>
  {board_body}
</section>
"""

    # ---- F. panel history -------------------------------------------
    if panel_rows:
        rows_html = "\n".join(
            f'    <tr>'
            f'<td>{esc(r["date"])}</td>'
            f'<td><a href="{esc(r["link"])}">{esc(r["conjecture"])}</a></td>'
            f'<td>{esc(r["label"])}</td>'
            f'<td>{esc(r["model"])}</td>'
            f'<td>{esc(r["lab"])}</td>'
            f'<td><a href="{esc(r["link"])}" class="verdict verdict-{verdict_colour(r["word"])}">'
            f'{esc(r["word"])}</a></td>'
            f"</tr>"
            for r in panel_rows
        )
        table = f"""
  <table class="data-table">
    <thead><tr><th>Date</th><th>Conjecture</th><th>Gate / vote</th><th>Reviewer</th><th>Laboratory</th><th>Verdict</th></tr></thead>
    <tbody>
{rows_html}
    </tbody>
  </table>"""
    else:
        table = (
            '<p class="empty-state">No panel or gate verdicts recorded yet '
            "under <code>pipeline/reviews/</code>.</p>"
        )
    panel_section = f"""
<section id="panel-history" aria-labelledby="panel-h">
  <h2 id="panel-h">Panel history</h2>
  <p class="section-note">
    Most recent first. Every row links to the verbatim model output; nothing
    here is a paraphrase.
  </p>
  {table}
</section>
"""

    # ---- G. evidence base -------------------------------------------
    if evidence:
        ev_rows = []
        for e in evidence:
            bar = build_evidence_bar_svg(e["established"], e["contested"], e["speculative"])
            retract_badge = (
                '<span class="badge badge-retract">RETRACTION</span>' if e["retracted"] else ""
            )
            ev_rows.append(
                f'    <tr>'
                f'<td><a href="{esc(e["relpath"])}">{esc(e["id"])}</a> {retract_badge}<br>'
                f'<span class="ev-title">{esc(e["title"])}</span></td>'
                f'<td>{e["identifiers"]}</td>'
                f'<td>{e["unverified"]}</td>'
                f'<td>{bar}<span class="ev-counts">E {e["established"]} · C {e["contested"]} · S {e["speculative"]}</span></td>'
                f"</tr>"
            )
        ev_table = f"""
  <table class="data-table">
    <thead><tr><th>Brief</th><th>Identifiers</th><th>[UNVERIFIED]</th><th>Established / contested / speculative</th></tr></thead>
    <tbody>
{''.join(ev_rows)}
    </tbody>
  </table>"""
    else:
        ev_table = '<p class="empty-state">No evidence briefs found under <code>evidence/</code>.</p>'
    evidence_section = f"""
<section id="evidence" aria-labelledby="evidence-h">
  <h2 id="evidence-h">Evidence base</h2>
  <p class="section-note">
    Counts are read directly from each brief; "identifiers" is a pattern
    match (DOI/PMID/arXiv/NCT), not a live resolution against a registry —
    that check is <code>tools/verify-citations.py</code>, which runs in CI
    and needs the network this dashboard deliberately does not use.
  </p>
  {ev_table}
</section>
"""

    # ---- H. decisions -------------------------------------------
    if decisions:
        dec_items = "".join(
            f'<li><a href="../ledger/{"DECISIONS.md" if d["source"].endswith("DECISIONS.md") else "OPEN.md"}">'
            f'<strong>{esc(d["id"])}.</strong> {esc(d["title"])}</a>'
            f'<p class="board-summary">{esc(d["summary"])}</p></li>'
            for d in decisions
        )
        dec_body = f'<ul class="board-list">{dec_items}</ul>'
    else:
        dec_body = '<p class="empty-state">No decisions recorded yet in ledger/DECISIONS.md.</p>'
    decisions_section = f"""
<section id="decisions" aria-labelledby="decisions-h">
  <h2 id="decisions-h">Decisions</h2>
  {dec_body}
</section>
"""

    # ---- refuted, folded into the ledger picture ---------------------
    if refuted:
        ref_items = "".join(
            f'<li><strong>{esc(r["id"])}</strong> — {esc(r["title"])}'
            f'<p class="board-summary">{esc(r["summary"])}</p></li>'
            for r in refuted
        )
        refuted_body = f'<ul class="board-list">{ref_items}</ul>'
    else:
        refuted_body = (
            '<p class="empty-state">No entries yet. The programme has not '
            "refuted a conjecture. That is a fact about how young it is, "
            "not a fact worth hiding.</p>"
        )
    refuted_section = f"""
<section id="refuted" aria-labelledby="refuted-h">
  <h2 id="refuted-h">Refuted, and kept</h2>
  {refuted_body}
</section>
"""

    # ---- footer -------------------------------------------
    footer = """
<footer class="page-footer">
  <p>
    <a href="https://github.com/davidvanheeswijck/pain-as-information">Repository</a>
    · refuted conjectures are kept in <code>ledger/REFUTED.md</code> rather
    than deleted, on purpose: a research programme without a graveyard is a
    random walk.
  </p>
</footer>
"""

    body = (
        header + strip + lineage_section + calibration_section
        + hardcore_section + panel_section + evidence_section
        + decisions_section + refuted_section + footer
    )
    return HTML_SHELL.format(body=body)


HTML_SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pain as Information — programme dashboard</title>
<meta name="generator" content="tools/build-dashboard.py">
<style>
:root {{
  color-scheme: light dark;
  --bg: #f7f7f5;
  --bg-raised: #ffffff;
  --fg: #1a1c1e;
  --fg-muted: #565c63;
  --border: #d8dade;
  --accent: #2b5d8c;
  --green: #1f7a3f;
  --amber: #a6690a;
  --red: #a3271f;
  --neutral: #6b6f75;
  font-size: 16px;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #14161a;
    --bg-raised: #1d2025;
    --fg: #eceef0;
    --fg-muted: #a3a9b0;
    --border: #33373d;
    --accent: #6fa8dc;
    --green: #4fbf72;
    --amber: #e0a53c;
    --red: #e2685f;
    --neutral: #9aa0a8;
  }}
}}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.55;
}}
a {{ color: var(--accent); }}
main, header.page-header, footer.page-footer {{
  max-width: 1180px;
  margin: 0 auto;
  padding: 1.5rem clamp(1rem, 3vw, 2.5rem);
}}
.page-header h1 {{
  font-size: clamp(1.6rem, 2.4vw + 1rem, 2.4rem);
  margin: 0 0 0.4rem;
  letter-spacing: -0.01em;
}}
.thesis {{ font-size: 1.05rem; color: var(--fg-muted); margin: 0 0 0.8rem; max-width: 62ch; }}
.meta {{ font-size: 0.85rem; color: var(--fg-muted); max-width: 72ch; }}
code {{
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  background: var(--bg-raised);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 0.05em 0.35em;
  font-size: 0.9em;
}}
section {{
  max-width: 1180px;
  margin: 0 auto 2.5rem;
  padding: 0 clamp(1rem, 3vw, 2.5rem);
}}
h2 {{
  font-size: 1.4rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.4rem;
  margin-bottom: 0.8rem;
}}
h3 {{ font-size: 1.05rem; margin: 0 0 0.5rem; }}
.section-note {{ color: var(--fg-muted); max-width: 78ch; font-size: 0.94rem; }}
.cal-honesty {{ font-size: 1rem; color: var(--fg); }}
.status-strip {{
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem 2rem;
  align-items: center;
  background: var(--bg-raised);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.2rem 1.5rem;
  margin: 0 auto 2.5rem;
  max-width: 1180px;
}}
.stat {{ display: flex; flex-direction: column; }}
.stat-n {{ font-size: 1.9rem; font-weight: 700; line-height: 1; }}
.stat-label {{ font-size: 0.78rem; color: var(--fg-muted); text-transform: uppercase; letter-spacing: 0.04em; }}
.status-chips {{ display: flex; flex-wrap: wrap; gap: 0.6rem; }}
.chip {{
  display: flex; flex-direction: column; align-items: center;
  border: 1px solid var(--border); border-radius: 8px;
  padding: 0.3rem 0.7rem; min-width: 4.2rem;
}}
.chip-n {{ font-weight: 700; }}
.chip-label {{ font-size: 0.7rem; color: var(--fg-muted); }}
.svg-wrap {{
  background: var(--bg-raised);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem;
  overflow-x: auto;
}}
.lineage-svg, .cal-svg {{ display: block; width: 100%; height: auto; max-width: 100%; }}
.lineage-edge {{ fill: none; stroke: var(--fg-muted); stroke-width: 1.6; opacity: 0.7; }}
.lineage-arrowhead {{ fill: var(--fg-muted); }}
.lineage-id {{ font: 700 13px ui-monospace, monospace; }}
.lineage-title {{ font: 12px -apple-system, sans-serif; }}
.lineage-badge {{ font: 700 11px sans-serif; fill: #fff; }}
a text {{ cursor: pointer; }}
.cal-axis {{ stroke: var(--fg-muted); stroke-width: 1.4; }}
.cal-diagonal {{ stroke: var(--fg-muted); stroke-width: 1.4; stroke-dasharray: 4,4; }}
.cal-tick {{ font: 11px sans-serif; fill: var(--fg-muted); }}
.cal-axis-label {{ font: 12px sans-serif; fill: var(--fg-muted); }}
.cal-point {{ fill: var(--accent); stroke: var(--bg-raised); stroke-width: 1.4; }}
.cal-point-hollow {{ fill: none; stroke: var(--fg-muted); stroke-width: 1.6; }}
.cal-moved-up {{ stroke: var(--red); stroke-width: 2.2; }}
.cal-moved-down {{ stroke: var(--green); stroke-width: 2.2; }}
.cal-arrowhead {{ fill: var(--red); }}
.cal-note {{ font-style: italic; }}
.board-columns {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; }}
.board-list {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0.9rem; }}
.board-item, .board-list > li {{
  background: var(--bg-raised);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 0.8rem 1rem;
}}
.board-title {{ margin: 0 0 0.3rem; font-weight: 600; }}
.board-summary {{ margin: 0 0 0.3rem; color: var(--fg-muted); font-size: 0.92rem; }}
.bears-on {{ margin: 0; font-size: 0.85rem; }}
.empty-inline {{ color: var(--fg-muted); font-style: italic; }}
.empty-state {{
  color: var(--fg-muted);
  font-style: italic;
  border: 1px dashed var(--border);
  border-radius: 10px;
  padding: 1rem 1.2rem;
}}
.data-table {{ width: 100%; border-collapse: collapse; background: var(--bg-raised); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }}
.data-table th, .data-table td {{ text-align: left; padding: 0.55rem 0.8rem; border-bottom: 1px solid var(--border); font-size: 0.92rem; vertical-align: top; }}
.data-table th {{ color: var(--fg-muted); font-weight: 600; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.03em; }}
.data-table tr:last-child td {{ border-bottom: none; }}
.ev-title {{ color: var(--fg-muted); font-size: 0.85rem; }}
.ev-counts {{ font-size: 0.78rem; color: var(--fg-muted); margin-left: 0.5rem; }}
.ev-bar {{ width: 130px; height: 12px; vertical-align: middle; }}
.ev-bar-established {{ fill: var(--green); }}
.ev-bar-contested {{ fill: var(--amber); }}
.ev-bar-speculative {{ fill: var(--neutral); }}
.ev-bar-empty {{ fill: none; stroke: var(--border); stroke-dasharray: 3,3; }}
.badge {{ display: inline-block; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.03em; border-radius: 4px; padding: 0.1em 0.4em; vertical-align: middle; }}
.badge-retract {{ background: var(--red); color: #fff; }}
.verdict {{ font-weight: 700; text-decoration: none; padding: 0.15em 0.5em; border-radius: 5px; display: inline-block; }}
.verdict-green {{ color: var(--green); background: color-mix(in srgb, var(--green) 16%, transparent); }}
.verdict-amber {{ color: var(--amber); background: color-mix(in srgb, var(--amber) 16%, transparent); }}
.verdict-red {{ color: var(--red); background: color-mix(in srgb, var(--red) 16%, transparent); }}
.verdict-neutral {{ color: var(--fg); background: color-mix(in srgb, var(--neutral) 16%, transparent); }}
.page-footer {{ color: var(--fg-muted); font-size: 0.85rem; border-top: 1px solid var(--border); margin-top: 1rem; }}
@media (max-width: 640px) {{
  .status-strip {{ flex-direction: column; align-items: stretch; }}
  .data-table {{ display: block; overflow-x: auto; }}
}}
</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


# --------------------------------------------------------------------------
# --check
# --------------------------------------------------------------------------

GENERATED_TS_RE = re.compile(r'(id="generated-ts">)[^<]*(<)')


def normalise_for_diff(text: str) -> str:
    """Strip the one field that legitimately differs between two runs of an
    unchanged repository: the wall-clock generation stamp."""
    return GENERATED_TS_RE.sub(r"\1GENERATED\2", text)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out", default=None,
        help="output path (default: <repo_root>/docs/index.html)",
    )
    parser.add_argument(
        "--root", default=None,
        help="repository root (default: found by walking up for .git)",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="regenerate into a temp file and exit 1 if it differs from --out",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve() if args.root else find_repo_root(Path.cwd())
    out_path = Path(args.out) if args.out else root / "docs" / "index.html"
    if not out_path.is_absolute():
        out_path = root / out_path

    now = datetime.datetime.now(datetime.timezone.utc)
    html_text = build_html(root, now)

    if args.check:
        if not out_path.exists():
            print(f"stale: {out_path} does not exist; run without --check to generate it")
            return 1
        current = out_path.read_text(encoding="utf-8")
        if normalise_for_diff(current) != normalise_for_diff(html_text):
            print(
                f"stale: {out_path} does not match what tools/build-dashboard.py "
                "would generate from the current repository state. "
                "Run it without --check and commit the result."
            )
            return 1
        print(f"{out_path} is up to date")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_text, encoding="utf-8")
    print(f"wrote {out_path} ({len(html_text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
