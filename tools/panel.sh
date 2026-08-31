#!/usr/bin/env bash
# Run one conjecture through the full pipeline: gates, then a panel vote,
# then a tally.
#
#   panel.sh <conjecture.md> [--size N] [--gates "00 01 02"] [--out DIR]
#            [--rivals FILE]... [--exclude-lab LAB] [--dry-run]
#
# Two phases, for two different reasons.
#
#   Phase 1, gates. Each gate is a different kind of attack, so each is run
#   once, and each on a DIFFERENT laboratory's model, rotating through the
#   panel. Cost is one call per gate rather than gates x models, and no single
#   lab's blind spot can shape the whole gate record.
#
#   Phase 2, panel vote. The conjecture and its gate verdicts go to N models
#   from N laboratories, each voting independently. Refutation is the default:
#   see EPISTEMICS.md rule 1 for the scoring, which is applied by tally.py.
#
# The conjecture is presented to the panel alongside rival candidates, in an
# order derived from a hash rather than from authorship, and with no indication
# of which a human wrote. Sycophancy is a measured property of RLHF-trained
# models (arXiv:2310.13548), so the fix is to remove the preference signal
# rather than to ask the model not to act on it.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"

SUBJECT=""; SIZE=5; OUTDIR=""; DRY=0; RIVALS=(); EXCLUDE=()
GATES="00-triage 01-physical-plausibility 02-biological-plausibility \
03-evidence-integrity 04-falsifiability 05-prior-art 06-hostile-referee \
07-clinical-translation"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --size)        SIZE="$2"; shift 2 ;;
    --gates)       GATES="$2"; shift 2 ;;
    --out)         OUTDIR="$2"; shift 2 ;;
    --rivals)      RIVALS+=("$2"); shift 2 ;;
    --exclude-lab) EXCLUDE+=(--exclude-lab "$2"); shift 2 ;;
    --dry-run)     DRY=1; shift ;;
    -h|--help)     sed -n '2,30p' "$0"; exit 0 ;;
    -*)            echo "unknown flag: $1" >&2; exit 2 ;;
    *)             SUBJECT="$1"; shift ;;
  esac
done
[[ -n "$SUBJECT" && -f "$SUBJECT" ]] || { echo "usage: panel.sh <conjecture.md> [flags]" >&2; exit 2; }

CID="$(basename "$SUBJECT" .md)"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="${OUTDIR:-$ROOT/pipeline/reviews/$CID/$STAMP}"

# --- lint before spending anything -------------------------------------
# A conjecture that fails structure or citations does not deserve a panel, and
# finding that out after thirteen model calls is the expensive way to learn it.
echo "== lint ==" >&2
"$HERE/lint-conjecture.py" "$SUBJECT" || { echo "conjecture fails lint; fix it before spending a panel round" >&2; exit 1; }
"$HERE/verify-citations.py" "$SUBJECT" || { echo "citations do not resolve; fix them before spending a panel round" >&2; exit 1; }

# --- assemble the panel ------------------------------------------------
mapfile -t PANEL < <("$HERE/panel.py" --size "$SIZE" "${EXCLUDE[@]+"${EXCLUDE[@]}"}")
(( ${#PANEL[@]} == SIZE )) || { echo "panel.py returned ${#PANEL[@]} models, wanted $SIZE" >&2; exit 1; }
printf 'panel:\n'; printf '  %s\n' "${PANEL[@]}"

# A dry run must leave no trace. It previously wrote panel.json.md into a fresh
# timestamped directory before exiting, which the dashboard then counted as a
# review run that never happened. Nothing is created until a model is actually
# about to be called.
if (( DRY )); then echo "(dry run: stopping before any model call, nothing written)"; exit 0; fi

mkdir -p "$OUTDIR"
{
  echo "# Panel record: $CID"
  echo
  echo "> Assembled $STAMP. Distinct laboratories enforced by tools/panel.py."
  echo
  "$HERE/panel.py" --size "$SIZE" "${EXCLUDE[@]+"${EXCLUDE[@]}"}" --json
} > "$OUTDIR/panel.json.md"

# --- phase 1: gates, rotated across laboratories -----------------------
# The ledger and the programme are context for every gate. Gate 05 in
# particular is useless without the refuted ledger.
export REVIEW_CONTEXT="$ROOT/PROGRAMME.md:$ROOT/ledger/REFUTED.md"
i=0
: > "$OUTDIR/verdicts.txt"
for g in $GATES; do
  gate="$ROOT/pipeline/gates/$g.md"
  [[ -f "$gate" ]] || { echo "no such gate: $gate" >&2; exit 1; }
  model="${PANEL[$(( i % ${#PANEL[@]} ))]}"
  i=$(( i + 1 ))
  echo "== gate $g  ->  $model ==" >&2
  if v=$("$HERE/review.sh" "$SUBJECT" "$OUTDIR/gate-$g.md" "$gate" "$model"); then
    printf '%-34s %-46s %s\n' "$g" "$model" "$v" | tee -a "$OUTDIR/verdicts.txt"
  else
    # A gate that errors is recorded as a gap, never silently skipped: a
    # missing verdict must not read as a passing one.
    printf '%-34s %-46s %s\n' "$g" "$model" "VERDICT: GATE FAILED TO RUN" \
      | tee -a "$OUTDIR/verdicts.txt"
  fi
done

# --- phase 2: the panel vote -------------------------------------------
# Build the ballot: the conjecture plus any rivals, unattributed, in an order
# fixed by a hash of the content so it is deterministic and reproducible but
# carries no authorship information.
BALLOT="$OUTDIR/ballot.md"
python3 - "$BALLOT" "$SUBJECT" "$OUTDIR/verdicts.txt" "${RIVALS[@]+"${RIVALS[@]}"}" <<'PY'
import hashlib, os, sys
out, subject, verdicts, *rivals = sys.argv[1:]
docs = [subject] + rivals
# Deterministic, content-derived order. Not authorship order, not the order
# they were passed on the command line.
docs.sort(key=lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest())
parts = ["# Candidates\n\nPresented in an order carrying no information about "
         "authorship or origin.\n"]
for n, p in enumerate(docs, 1):
    parts.append(f"\n\n---\n\n## CANDIDATE {n}\n\n" + open(p).read())
parts.append("\n\n---\n\n## Gate verdicts returned against CANDIDATE "
             f"{docs.index(subject) + 1}\n\n```\n" + open(verdicts).read() + "```\n")
open(out, 'w').write("".join(parts))
print(f"ballot: {len(docs)} candidate(s)", file=sys.stderr)
PY

vote_gate="$ROOT/pipeline/gates/10-panel-vote.md"
unset REVIEW_CONTEXT   # the panel votes on the ballot alone
: > "$OUTDIR/votes.txt"
for model in "${PANEL[@]}"; do
  slug="$(printf '%s' "$model" | tr '/@' '__')"
  echo "== vote  ->  $model ==" >&2
  if v=$("$HERE/review.sh" "$BALLOT" "$OUTDIR/vote-$slug.md" "$vote_gate" "$model"); then
    printf '%-46s %s\n' "$model" "$v" | tee -a "$OUTDIR/votes.txt"
  else
    printf '%-46s %s\n' "$model" "VERDICT: VOTE FAILED TO RUN" | tee -a "$OUTDIR/votes.txt"
  fi
done

# --- tally -------------------------------------------------------------
"$HERE/tally.py" "$OUTDIR" | tee "$OUTDIR/SUMMARY.md"
echo >&2
echo "record: $OUTDIR" >&2
