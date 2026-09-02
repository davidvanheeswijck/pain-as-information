#!/usr/bin/env bash
# One gate, one model, one verdict.
#
#   review.sh <input.md> <output.md> <gate.md> [model]
#
# Routing. The gate runs on an EU-hosted, zero-retention endpoint by default,
# and the runner verifies that against the router's own model metadata before
# spending a token rather than taking it on trust. What the router actually
# said is stamped into the verdict, so a relaxed run is visible in every
# artefact it produced. Inherited from the sibling legislation project; see
# EPISTEMICS.md rule 9 for why it is kept here.
#
# Env:
#   REQUESTY_API_KEY   (or REVIEW_API_KEY)
#   REVIEW_BASE_URL    default https://router.eu.requesty.ai/v1
#   REVIEW_MODEL       default vertex/gemini-3.7-flash@eu (overridden by $4)
#   REVIEW_CONTEXT     colon-separated extra files appended as context, e.g.
#                      "PROGRAMME.md:ledger/REFUTED.md". Gates that need the
#                      ledger will not work without it.
#   REVIEW_VERIFY      default 1. Refuse to run unless the router reports the
#                      guarantees below. 0 skips verification entirely, and the
#                      verdict then claims nothing about jurisdiction.
#   REVIEW_REQUIRE_EU          default 1  geolocation must be eu
#   REVIEW_REQUIRE_ZDR         default 1  retention must be 0 days
#   REVIEW_REQUIRE_NO_TRAINING default 1  text must not be trained on
#   REVIEW_TEMPERATURE default 0.3; "off" to never send it
#   REVIEW_MAX_TOKENS  default unset (router decides)
#
# A .env at the repository root is loaded if present, so the key stays out of
# shell history and out of the repository.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && . "$ROOT/.env" && set +a

IN="${1:?usage: review.sh <input.md> <output.md> <gate.md> [model]}"
OUT="${2:?}"; PROMPT="${3:?}"
BASE="${REVIEW_BASE_URL:-https://router.eu.requesty.ai/v1}"
MODEL="${4:-${REVIEW_MODEL:-vertex/gemini-3.7-flash@eu}}"
VERIFY="${REVIEW_VERIFY:-1}"
KEY="${REVIEW_API_KEY:-${REQUESTY_API_KEY:-}}"
[[ -f "$IN"     ]] || { echo "no such input: $IN" >&2; exit 1; }
[[ -f "$PROMPT" ]] || { echo "no such gate: $PROMPT" >&2; exit 1; }
[[ -n "$KEY"    ]] || { echo "no API key: set REQUESTY_API_KEY (see tools/README.md)" >&2; exit 1; }
mkdir -p "$(dirname "$OUT")"
TMP="$(mktemp)"; RESP="$(mktemp)"; CFG="$(mktemp)"; META="$(mktemp)"
trap 'rm -f "$TMP" "$RESP" "$CFG" "$META"' EXIT
chmod 600 "$CFG"; printf 'header = "Authorization: Bearer %s"\n' "$KEY" > "$CFG"

# ---- provenance, verified rather than asserted -------------------------
PROV="router $(printf '%s' "$BASE" | sed -E 's#https?://([^/]+).*#\1#') (unverified)"
if [[ "$VERIFY" == "1" ]]; then
  curl -sS --max-time 120 -K "$CFG" -o "$META" "$BASE/models" || {
    echo "could not read $BASE/models to verify routing" >&2; exit 1; }
  PROV=$(python3 - "$META" "$MODEL" "$BASE" <<'PY'
import json, os, sys
meta, model, base = json.load(open(sys.argv[1])), sys.argv[2], sys.argv[3]
rows = meta.get('data', meta if isinstance(meta, list) else [])
m = next((r for r in rows if r.get('id') == model), None)
if m is None:
    sys.exit(f"model {model!r} is not offered by {base}. Pick one it lists "
             "(tools/panel.py --list), or set REVIEW_REQUIRE_EU=0 deliberately.")
geo, days, trained = (str(m.get('geolocation', '')).lower(),
                      m.get('data_retention_days'), m.get('data_used_for_training'))
want = lambda k: os.environ.get(k, '1') == '1'
bad = []
if want('REVIEW_REQUIRE_EU') and geo != 'eu':
    bad.append(f"geolocation={geo or 'unknown'}")
if want('REVIEW_REQUIRE_ZDR') and days not in (0, '0'):
    bad.append(f"retention_days={days}")
# Unknown is not a pass. A router that does not say must not be read as a
# quiet yes.
if want('REVIEW_REQUIRE_NO_TRAINING') and trained not in (False, 'false'):
    bad.append(f"trained_on={'unknown' if trained is None else trained}")
if bad:
    sys.exit("refusing to run: " + ", ".join(bad) + ". The verdict would claim "
             "a guarantee this model does not offer. Relax the specific "
             "requirement deliberately rather than all of them.")
host = base.split('//')[-1].split('/')[0]
# Reports what the router said, never what was required.
print(f"router {host} · geolocation {geo} · retention {days}d · "
      f"trained-on {str(trained).lower()} · lab {m.get('model_lab', '?')}")
PY
  ) || exit 1
fi

build_body() {  # $1 = "with" | "without" temperature
  python3 - "$PROMPT" "$IN" "$MODEL" "${REVIEW_TEMPERATURE:-0.3}" "$1" \
           "${REVIEW_CONTEXT:-}" "${REVIEW_MAX_TOKENS:-}" > "$TMP" <<'PY'
import json, os, sys
prompt, doc, model, temp, mode, ctx, maxtok = sys.argv[1:8]
parts = [open(prompt).read()]
for p in filter(None, ctx.split(':')):
    if os.path.exists(p):
        parts.append(f"\n\n--- CONTEXT: {p} ---\n\n" + open(p).read())
    else:
        sys.exit(f"REVIEW_CONTEXT names a missing file: {p}")
parts.append("\n\n--- DOCUMENT UNDER REVIEW ---\n\n" + open(doc).read())
body = {"model": model, "messages": [{"role": "user", "content": "".join(parts)}]}
# Reasoning-tier models reject temperature outright, so the runner must be
# able to drop it.
if mode == "with" and temp not in ("off", ""):
    body["temperature"] = float(temp)
if maxtok:
    body["max_tokens"] = int(maxtok)
print(json.dumps(body))
PY
}
# Emit exactly one three-digit code, whatever happens.
#
# This used to be `curl ... -w '%{http_code}' || echo 000`. On a network
# failure curl writes "000" via -w AND the fallback appends another, giving
# "000000", which matches none of the retry conditions below. The retry loop
# was therefore dead for exactly the failures it existed to handle: timeouts
# and connection errors. 429 and 5xx retried fine, because curl exits zero and
# writes a single real code, which is why this survived unnoticed.
call() {
  local code
  code=$(curl -sS --max-time "${REVIEW_TIMEOUT:-1800}" --connect-timeout 30 \
    -K "$CFG" -H "Content-Type: application/json" \
    -o "$RESP" -w '%{http_code}' -d @"$TMP" "$BASE/chat/completions" 2>/dev/null) || true
  [[ "$code" =~ ^[0-9]{3}$ ]] || code="000"
  printf '%s' "$code"
}
build_body with
HTTP=$(call)
if [[ "$HTTP" == "400" ]] && grep -qi 'temperature' "$RESP"; then
  echo "note: $MODEL rejects temperature; retrying without it" >&2
  build_body without; HTTP=$(call)
fi
for backoff in 20 60; do
  [[ "$HTTP" == "429" || "$HTTP" =~ ^5 || "$HTTP" == "000" ]] || break
  echo "note: HTTP $HTTP from $MODEL, retrying in ${backoff}s" >&2
  sleep "$backoff"; HTTP=$(call)
done

# A reasoning model can burn its entire completion budget on hidden thinking
# and return HTTP 200 with an EMPTY content string. That is not a review. It
# was previously written to disk as a headed but bodiless file and scored
# "NO VERDICT LINE - treat as MAJOR", which invented an objection no reviewer
# had made and counted it against the conjecture. Two of C-003's five negative
# gates were this artefact.
#
# Detect it and retry once with a much larger budget before giving up.
truncated() {
  python3 - "$RESP" <<'PY2'
import json, sys
try:
    r = json.load(open(sys.argv[1]))
    c = r["choices"][0]
    m = c.get("message", {}) or {}
    txt = (m.get("content") or "") + (m.get("reasoning_content") or "") + (m.get("reasoning") or "")
    sys.exit(0 if not txt.strip() else 1)
except Exception:
    sys.exit(0)
PY2
}
if [[ "$HTTP" == "200" ]] && truncated; then
  echo "note: $MODEL returned empty or truncated content; retrying at ${REVIEW_MAX_TOKENS_RETRY:-32000} output tokens" >&2
  REVIEW_MAX_TOKENS="${REVIEW_MAX_TOKENS_RETRY:-32000}" build_body with
  HTTP=$(call)
fi
if [[ "$HTTP" == "200" ]] && truncated; then
  echo "GATE TRUNCATED: $MODEL produced no reviewable text for $(basename "$PROMPT") even at ${REVIEW_MAX_TOKENS_RETRY:-32000} tokens." >&2
  echo "This is a harness failure, not a verdict. Do not score it." >&2
  exit 3
fi
[[ "$HTTP" == "200" ]] || { echo "review HTTP $HTTP from $BASE for $MODEL" >&2
                            head -c 400 "$RESP" >&2; echo >&2; exit 1; }

python3 - "$RESP" "$OUT" "$MODEL" "$PROMPT" "$PROV" "$IN" <<'PY'
import datetime, json, os, sys
r = json.load(open(sys.argv[1]))
_msg = r["choices"][0].get("message") or {}
txt = _msg.get("content") or ""
u = r.get("usage", {})

# Reasoning-tier models on some providers return their analysis in a separate
# "reasoning_content" field and leave "content" empty when the answer budget is
# exhausted. Discarding that was throwing away a real review: nebius/kimi-k3
# failed gates 01 and 06 on two consecutive C-003 panels while voting normally
# in the same runs, because the vote prompt is short enough to leave room for a
# reply and the gate prompts are not.
#
# Recover the verdict from the reasoning field rather than losing the gate, and
# STAMP the file so the record shows where the text came from. This is not the
# model's polished answer and must not be passed off as one.
_recovered = False
if not txt.strip():
    _r = _msg.get("reasoning_content") or _msg.get("reasoning") or ""
    if _r.strip():
        txt = _r
        _recovered = True
hdr = (f"# Gate verdict\n\n"
       f"> Reviewer: `{sys.argv[3]}` · {sys.argv[5]}\n"
       f"> Gate: `{os.path.basename(sys.argv[4])}` · "
       f"Subject: `{os.path.basename(sys.argv[6])}`\n"
       f"> {datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')} · "
       f"tokens in={u.get('prompt_tokens','?')} out={u.get('completion_tokens','?')}\n"
       f"> Verbatim model output below. Do not edit it. If it is wrong, that is\n"
       f"> a fact about the panel and belongs in the record.\n"
       + ("> **RECOVERED FROM `reasoning_content`.** The model returned an empty\n"
          "> answer field, so this is its reasoning trace rather than a composed\n"
          "> review. Weigh it accordingly.\n" if _recovered else "")
       + "\n")
open(sys.argv[2], "w").write(hdr + txt + "\n")
# Models routinely bold the verdict, so the line arrives as "**VERDICT: ...**"
# rather than "VERDICT: ...". Anchoring on startswith() recorded a perfectly
# good MINOR as a missing verdict, and a missing verdict scores as MAJOR, so
# markdown formatting was silently changing the result of a review. Strip
# leading and trailing emphasis before matching.
import re as _re
v = []
for line in txt.splitlines():
    s = _re.sub(r"^[\s>*_#`-]+", "", line).strip()
    if s.upper().startswith("VERDICT:"):
        v.append(_re.sub(r"[\s*_`]+$", "", s))
print(v[-1] if v else "VERDICT: NO VERDICT LINE — treat as MAJOR")
PY
echo "written: $OUT" >&2
