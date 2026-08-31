#!/usr/bin/env python3
"""Select a review panel from the router, under a hard lab-diversity constraint.

Why this file exists. Models from one laboratory share pretraining data,
post-training recipe and failure modes, so their agreement is correlated. Five
verdicts from one lab's family look like a consensus and are not independent
evidence. Every selection this tool returns has distinct `model_lab` values,
and it fails loudly rather than quietly returning a smaller or duplicated panel.

It also enforces the routing guarantees before a model is eligible at all, so
a panel can never silently include a model that would fail review.sh's check.

Standard library only, so it runs on a bare CI runner.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any, Iterable

DEFAULT_BASE = "https://router.eu.requesty.ai/v1"

# Labs excluded from a panel by default. Not a quality judgement: these are
# tiers whose members are small enough that a MAJOR finding from them is more
# often a comprehension failure than a real objection, which costs the
# programme a round to discover. Override with --allow-lab.
LOW_TIER_LABS = {"nvidia", "sference"}


def fetch_models(base: str, key: str, timeout: int = 60) -> list[dict[str, Any]]:
    req = urllib.request.Request(
        f"{base}/models",
        headers={"Authorization": f"Bearer {key}",
                 "User-Agent": "pain-as-information/panel.py"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"router returned HTTP {e.code} for {base}/models")
    except (urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"could not reach {base}/models: {e}")
    rows = payload.get("data", payload if isinstance(payload, list) else [])
    if not rows:
        sys.exit(f"{base}/models returned no models")
    return rows


def compliant(m: dict[str, Any], require_eu: bool, require_zdr: bool,
              require_no_training: bool) -> bool:
    """Same three separable guarantees review.sh enforces. Unknown fails."""
    if require_eu and str(m.get("geolocation", "")).lower() != "eu":
        return False
    if require_zdr and m.get("data_retention_days") not in (0, "0"):
        return False
    if require_no_training and m.get("data_used_for_training") not in (False, "false"):
        return False
    return True


def _price(m: dict[str, Any]) -> float:
    try:
        return float(m.get("input_price") or 0.0)
    except (TypeError, ValueError):
        return 0.0


def _tier_key(m: dict[str, Any]) -> tuple:
    """Rank within a lab, best first.

    There is no capability field in the router metadata, so this uses the
    proxies that are there: whether the model reasons, how much context it
    holds, and what it costs. Price as a capability proxy is crude and is
    occasionally wrong, which is why --pin exists.
    """
    return (
        1 if m.get("supports_reasoning") else 0,
        int(m.get("context_window") or 0),
        _price(m),
    )


def choose(rows: Iterable[dict[str, Any]], size: int, *, exclude_labs: set[str],
           pins: list[str]) -> list[dict[str, Any]]:
    by_lab: dict[str, list[dict[str, Any]]] = {}
    for m in rows:
        lab = (m.get("model_lab") or "unknown").lower()
        by_lab.setdefault(lab, []).append(m)

    chosen: list[dict[str, Any]] = []
    used_labs: set[str] = set()

    # Pinned ids come first and still consume their lab's slot, so pinning
    # cannot be used to smuggle two models from the same lab onto a panel.
    index = {m["id"]: m for m in rows}
    for pid in pins:
        m = index.get(pid)
        if m is None:
            sys.exit(f"--pin {pid} is not an eligible model. "
                     "Run --list to see what is.")
        lab = (m.get("model_lab") or "unknown").lower()
        if lab in used_labs:
            sys.exit(f"--pin {pid} is from lab {lab!r}, which is already on the "
                     "panel. A panel of five is five laboratories.")
        chosen.append(m)
        used_labs.add(lab)

    # Take the best model each lab offers, then rank the LABS by that model.
    # Sorting labs alphabetically would be deterministic but arbitrary, and it
    # quietly biases every panel towards whichever laboratories sort early.
    # Ties break on lab name so the result stays reproducible.
    candidates = [(max(ms, key=_tier_key), lab) for lab, ms in by_lab.items()
                  if lab not in used_labs and lab not in exclude_labs]
    candidates.sort(key=lambda t: (_tier_key(t[0]), t[1]), reverse=True)
    for model, lab in candidates:
        if len(chosen) >= size:
            break
        chosen.append(model)
        used_labs.add(lab)

    if len(chosen) < size:
        sys.exit(
            f"could only assemble {len(chosen)} distinct laboratories, needed "
            f"{size}. Available after filtering: {sorted(set(by_lab) - exclude_labs)}. "
            "Lower --size deliberately rather than allowing a duplicate lab: a "
            "panel with two models from one lab is not a panel of that size."
        )
    return chosen[:size]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", default=os.environ.get("REVIEW_BASE_URL", DEFAULT_BASE))
    p.add_argument("--size", type=int, default=5, help="panel size, one lab each")
    p.add_argument("--list", action="store_true",
                   help="show every eligible model grouped by laboratory")
    p.add_argument("--pin", action="append", default=[], metavar="MODEL_ID",
                   help="force this model onto the panel; consumes its lab's slot")
    p.add_argument("--exclude-lab", action="append", default=[], metavar="LAB",
                   help="drop a laboratory entirely, e.g. to avoid self-review")
    p.add_argument("--allow-lab", action="append", default=[], metavar="LAB",
                   help="re-admit a lab excluded by default")
    p.add_argument("--json", action="store_true")
    p.add_argument("--allow-non-eu", action="store_true",
                   help="drop the routing guarantees. The panel record then "
                        "claims nothing about jurisdiction.")
    a = p.parse_args()

    key = os.environ.get("REVIEW_API_KEY") or os.environ.get("REQUESTY_API_KEY")
    if not key:
        # Read the repo .env the same way review.sh does, so the two tools
        # never disagree about which key is in play.
        env = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
        if os.path.exists(env):
            for line in open(env):
                line = line.strip()
                if line.startswith("REQUESTY_API_KEY=") or line.startswith("REVIEW_API_KEY="):
                    key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        sys.exit("no API key: set REQUESTY_API_KEY (see tools/README.md)")

    strict = not a.allow_non_eu
    rows = [m for m in fetch_models(a.base, key)
            if compliant(m, strict, strict, strict)]
    if not rows:
        sys.exit(f"no model at {a.base} satisfies the routing guarantees. "
                 "Check the endpoint, or pass --allow-non-eu deliberately.")

    excluded = {l.lower() for l in a.exclude_lab} | (
        LOW_TIER_LABS - {l.lower() for l in a.allow_lab})

    if a.list:
        by_lab: dict[str, list[dict[str, Any]]] = {}
        for m in rows:
            by_lab.setdefault((m.get("model_lab") or "unknown").lower(), []).append(m)
        for lab in sorted(by_lab):
            mark = "  (excluded by default)" if lab in excluded else ""
            print(f"\n## {lab} ({len(by_lab[lab])}){mark}")
            for m in sorted(by_lab[lab], key=_tier_key, reverse=True):
                flags = "reasoning" if m.get("supports_reasoning") else "-"
                print(f"   {m['id']:<52} ctx={m.get('context_window','?'):>9}  {flags}")
        return 0

    panel = choose(rows, a.size, exclude_labs=excluded, pins=a.pin)
    if a.json:
        print(json.dumps([{"id": m["id"], "lab": m.get("model_lab"),
                           "geolocation": m.get("geolocation"),
                           "retention_days": m.get("data_retention_days"),
                           "trained_on": m.get("data_used_for_training")}
                          for m in panel], indent=2))
    else:
        for m in panel:
            print(m["id"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
