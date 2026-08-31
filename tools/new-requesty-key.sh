#!/usr/bin/env bash
# Mint a project-scoped Requesty key with its own monthly budget.
#
#   new-requesty-key.sh "pain-as-information" 50
#
# Why a separate key rather than reusing an existing one: a runaway loop in this
# repository should exhaust this project's budget and stop, not another
# project's. The monthly limit is the stop, and it is set at creation.
#
# This needs a key with `manage` permission, which is not the same as a key that
# can call completions. Check what the key in your .env can do:
#
#   curl -sS -H "Authorization: Bearer $REQUESTY_API_KEY" \
#        https://api-v2.requesty.ai/v1/manage/apikey/self
#
# If that returns "permissions": {"manage": "none", ...} then this script cannot
# work and there is one manual step: create the key at
# https://app.requesty.ai/api-keys, or grant an existing key manage permission
# there and re-run this. Key management is an Enterprise feature.
#
# The API returns the key string exactly once. This script writes it straight
# into ../.env, which is gitignored, and never echoes it to the terminal, so it
# does not end up in scrollback or in a shell history file.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
API="${REQUESTY_MANAGE_URL:-https://api-v2.requesty.ai/v1/manage/apikey}"

NAME="${1:-pain-as-information}"
LIMIT="${2:-25}"          # monthly limit in USD; 0 means unlimited, avoid that

# The management key is deliberately a DIFFERENT variable from the routing key.
# Reusing one key for both means a leaked review key can mint more keys.
KEY="${REQUESTY_MANAGE_KEY:-}"
if [[ -z "$KEY" && -f "$ROOT/.env" ]]; then
  # shellcheck disable=SC1091
  set -a && . "$ROOT/.env" && set +a
  KEY="${REQUESTY_MANAGE_KEY:-${REQUESTY_API_KEY:-}}"
fi
[[ -n "$KEY" ]] || { echo "no key: set REQUESTY_MANAGE_KEY in $ROOT/.env" >&2; exit 1; }

CFG="$(mktemp)"; RESP="$(mktemp)"
trap 'rm -f "$CFG" "$RESP"' EXIT
chmod 600 "$CFG"; printf 'header = "Authorization: Bearer %s"\n' "$KEY" > "$CFG"

echo "checking whether this key may manage keys..." >&2
SELF=$(curl -sS --max-time 30 -K "$CFG" "$API/self" || true)
if printf '%s' "$SELF" | grep -q '"manage"[[:space:]]*:[[:space:]]*"none"'; then
  cat >&2 <<'MSG'

  The key in .env can call completions but cannot mint keys
  ("permissions": {"manage": "none"}).

  One manual step, then this script works:
    1. https://app.requesty.ai/api-keys
    2. Create a key, or edit an existing one, and grant it manage read/write.
    3. Put it in .env as REQUESTY_MANAGE_KEY (a separate line from
       REQUESTY_API_KEY, so the routing key stays unable to mint keys).
    4. Re-run this script.

  Or simply create the project key in that dashboard by hand and paste it into
  .env as REQUESTY_API_KEY. The harness does not care which route was used.

MSG
  exit 3
fi

HTTP=$(curl -sS --max-time 60 -K "$CFG" -H "Content-Type: application/json" \
  -o "$RESP" -w '%{http_code}' -X POST "$API" \
  -d "$(python3 -c 'import json,sys; print(json.dumps({"name": sys.argv[1], "monthly_limit": float(sys.argv[2])}))' "$NAME" "$LIMIT")")

[[ "$HTTP" == "200" || "$HTTP" == "201" ]] || {
  echo "key creation returned HTTP $HTTP" >&2; head -c 400 "$RESP" >&2; echo >&2; exit 1; }

python3 - "$RESP" "$ROOT/.env" "$NAME" "$LIMIT" <<'PY'
import json, os, re, sys
resp, envpath, name, limit = sys.argv[1:5]
d = json.load(open(resp))
key = d.get("api_key") or d.get("key")
kid = d.get("api_key_id") or d.get("id") or "?"
if not key:
    sys.exit(f"no key string in the response; got fields: {sorted(d)}")
lines, seen = [], False
if os.path.exists(envpath):
    for line in open(envpath):
        if line.startswith("REQUESTY_API_KEY="):
            lines.append(f"REQUESTY_API_KEY={key}\n"); seen = True
        else:
            lines.append(line)
if not seen:
    lines.append(f"REQUESTY_API_KEY={key}\n")
open(envpath, "w").write("".join(lines))
os.chmod(envpath, 0o600)
# The id is safe to print. The key never is.
print(f"created key {name!r} id={kid} monthly_limit={limit} USD", file=sys.stderr)
print(f"written to {envpath} (mode 600, gitignored). The key string was not "
      f"printed; Requesty will not show it again.", file=sys.stderr)
PY
