"""Aggregate S-1b files into results.json / results.md / PNGs.

The P1 and P2 statistics and rules are S-1's, imported unchanged from
aggregate_s001 (wilson, boot_mean, p1_cell, verdict_p1, p2_cell, verdict_p2).
New here: the tuning summary, the gates G1 to G3 (PREDICTION.md), the held-out
validation V1 and V2, and gated reporting.  Every number in the prose is computed
from the files; sentences are chosen by the data.
"""

import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
S1 = os.path.join(os.path.dirname(HERE), "S-001-tjunction-rate-vs-pattern")
sys.path.insert(0, S1)
sys.path.insert(0, HERE)

from aggregate_s001 import (  # noqa: E402
    AMPS, PATTERNS, _load, boot_mean, f2, fval, p1_cell, p2_cell, verdict_p1, verdict_p2, wilson,
)
import tuning as TU  # noqa: E402

FREQS = (2, 4, 20, 40, 60, 80)
NO_TUNING = "No tuning of this model class within the declared space produces progressive block with Sundt following frequencies."


def jload(p):
    with open(p) as f:
        return json.load(f)


# --- tuning summary -----------------------------------------------------------

def funnel(rs):
    cal = [r for r in rs if r.get("calibrated")]
    onsets = [r["flags"]["onset_s"] for r in cal]
    ff = lambda r, n: r["ff"].get(n)
    out = dict(
        n=len(rs),
        n_na_k_band=sum(1 for r in rs if TU.in_band("na_k", ff(r, "na_k"))),
        n_kcnq_band=sum(1 for r in rs if ff(r, "kcnq") is not None and TU.in_band("kcnq", ff(r, "kcnq"))),
        n_sk_band=sum(1 for r in rs if r.get("sk_in_band")),
        n_sk_2_40=sum(1 for r in rs if ff(r, "sk") is not None and TU.SK_ACCEPT_RANGE[0] <= ff(r, "sk") <= TU.SK_ACCEPT_RANGE[1]),
        n_undrivable=sum(1 for r in rs if r.get("stage") == "undrivable"),
        n_calibrated=len(cal),
        n_B1=sum(1 for r in cal if r["flags"]["B1"]),
        n_B2=sum(1 for r in cal if r["flags"]["B2"]),
        n_B3=sum(1 for r in cal if r["flags"]["B3"]),
        n_B1_and_B3=sum(1 for r in cal if r["flags"]["B1"] and r["flags"]["B3"]),
        n_block_all=sum(1 for r in cal if r["flags"]["B1"] and r["flags"]["B2"] and r["flags"]["B3"]),
        n_sundt_all_of_calibrated=sum(1 for r in cal if r.get("sk_in_band")),
        n_onset_none=sum(1 for o in onsets if o is None),
        n_onset_under_2s=sum(1 for o in onsets if o is not None and o < TU.B3_ONSET_S[0]),
        n_onset_over_20s=sum(1 for o in onsets if o is not None and o > TU.B3_ONSET_S[1]),
        onset_median_defined_s=float(np.median([o for o in onsets if o is not None])) if any(o is not None for o in onsets) else None,
        F_early_median=float(np.median([r["run"]["F_early"] for r in cal if r["run"].get("F_early") is not None])) if any(r["run"].get("F_early") is not None for r in cal) else None,
        F_late_median=float(np.median([r["run"]["F_late"] for r in cal if r["run"].get("F_late") is not None])) if any(r["run"].get("F_late") is not None for r in cal) else None,
        n_meets=sum(1 for r in rs if r.get("meets")),
    )
    return out


def tuning_summary(out):
    tdir = os.path.join(out, "tuning")
    sel = jload(os.path.join(tdir, "selected.json")) if os.path.exists(os.path.join(tdir, "selected.json")) else {}
    r1 = list(_load(os.path.join(tdir, "r1"), "c*.json").values())
    r2 = list(_load(os.path.join(tdir, "r2"), "c*.json").values())
    allr = r1 + r2
    cal = sorted((r for r in allr if r.get("calibrated")), key=lambda r: r["J"])
    return dict(
        selected_present=bool(sel), sets=sel.get("sets", []), checks=sel.get("checks", []),
        round2_ran=sel.get("round2_ran", False), centres=sel.get("centres", []),
        n_meeting_targets=sel.get("n_meeting_targets", 0), T=sel.get("T"),
        funnel_all=funnel(allr), funnel_r1=funnel(r1), funnel_r2=funnel(r2),
        best=[dict(id=r["id"], J=r["J"], d=r["d"], ff=r["ff"], flags=r["flags"], params=r["params"],
                   F_early=r["run"].get("F_early"), F_late=r["run"].get("F_late"),
                   n_scored=r["run"].get("n_scored"), meets=r["meets"]) for r in cal[:5]],
        points=[dict(id=r["id"], ff_sk=r["ff"]["sk"], onset_s=r["flags"]["onset_s"], meets=r["meets"],
                     sk_in_band=bool(r.get("sk_in_band"))) for r in cal],
    )


# --- gates and decision (pure; unit-tested) -------------------------------------

def prop_state(k, n):
    """One V1 proportion: pass if > 0.50 with Wilson lower bound > 0.50; fail if the upper bound < 0.50."""
    if n == 0:
        return "inconclusive"
    lo, hi = wilson(k, n)
    return "pass" if (k / n > 0.5 and lo > 0.5) else "fail" if hi < 0.5 else "inconclusive"


def v1_state(k4, n4, k2, n2):
    """V1 (PREDICTION.md): proportion with dF(4 Hz) >= 0.20 and proportion with dF(2 Hz) <= 0.10,
    each judged by prop_state; fails if either fails, passes only if both pass."""
    s = [prop_state(k4, n4), prop_state(k2, n2)]
    if "fail" in s:
        return "fail"
    return "pass" if s == ["pass", "pass"] else "inconclusive"


def v2_state(k, n):
    """V2: pass if proportion >= 0.90 with Wilson lower bound >= 0.85; fail if the upper bound < 0.85."""
    if n == 0:
        return "inconclusive"
    lo, hi = wilson(k, n)
    return "pass" if (k / n >= 0.90 and lo >= 0.85) else "fail" if hi < 0.85 else "inconclusive"


def decide(g1, g2, g3, n_ok, p1_rule, p2_rule, conv_pass):
    """Gate P1 and P2.  Any failed gate gives NO VERDICT; a failed dt-halving check gives
    INCONCLUSIVE; otherwise the pre-registered rule's verdict."""
    bad = []
    if not g1:
        bad.append("G1 calibration not reproduced")
    if not g2:
        bad.append("G2 population progressive block not reproduced")
    if g3 != "pass":
        bad.append(f"G3 held-out validation {g3}")
    if not n_ok:
        bad.append("fewer than 200 accepted variants")
    if bad:
        txt = "NO VERDICT (" + "; ".join(bad) + ")"
        return dict(P1=txt, P2=txt, gates_ok=False, reasons=bad)
    if not conv_pass:
        txt = "INCONCLUSIVE (dt-halving check failed)"
        return dict(P1=txt, P2=txt, gates_ok=True, reasons=["dt-halving failed"])
    return dict(P1=p1_rule, P2=p2_rule, gates_ok=True, reasons=[])


# --- main ------------------------------------------------------------------------

def rate_row(models, key):
    runs = [m["runs"][key] for m in models.values() if key in m["runs"]]
    vals = [fval(r) for r in runs]
    ev = [r["n_evoked"] / max(1, r["n_pulses"]) for r in runs]
    b = boot_mean(vals)
    nt, na, ns = (float(np.mean([r[k] for r in runs])) for k in ("n_test", "n_arrived", "n_scored"))
    fa = boot_mean([fval(r, "F_all") for r in runs])
    n_exc = sum(r["n_arrived"] - r["n_scored"] for r in runs)
    fail_all = sum(r["n_arrived"] * r["F_all"] for r in runs if r.get("F_all") is not None)
    fail_sc = sum(r["n_scored"] * r["F"] for r in runs if r.get("F") is not None)
    n_sc = sum(r["n_scored"] for r in runs if r.get("F") is not None)
    return dict(F_mean=b["mean"], F_ci=[b["lo"], b["hi"]], n=b["n"],
                evoked_fraction_median=float(np.median(ev)) if ev else None,
                n_test_mean=nt, n_arrived_mean=na, n_scored_mean=ns, scored_over_test=ns / nt if nt else None,
                F_all_mean=fa["mean"], F_all_ci=[fa["lo"], fa["hi"]], n_excluded_total=n_exc,
                excluded_fail_rate=(fail_all - fail_sc) / n_exc if n_exc else None,
                scored_fail_rate_pooled=fail_sc / n_sc if n_sc else None)


def held_out(models, valf, amp=1.5):
    base = {k: fval(m["runs"].get("none")) for k, m in models.items()}
    d4, d2 = [], []
    for k, m in models.items():
        b = base[k]
        f4, f2_ = fval(m["runs"].get(f"reg4@{amp}")), fval(m["runs"].get(f"reg2@{amp}"))
        if np.isfinite(b) and np.isfinite(f4):
            d4.append(f4 - b)
        if np.isfinite(b) and np.isfinite(f2_):
            d2.append(f2_ - b)
    d4, d2 = np.array(d4), np.array(d2)
    n4, n2 = len(d4), len(d2)
    k4, k2 = int((d4 >= 0.20).sum()), int((d2 <= 0.10).sum())
    v1 = dict(amp=amp, n_4hz=n4, n_2hz=n2, k_4hz_ge_0_20=k4, prop_4hz=k4 / n4 if n4 else float("nan"),
              wilson_4hz=wilson(k4, n4), k_2hz_le_0_10=k2, prop_2hz=k2 / n2 if n2 else float("nan"),
              wilson_2hz=wilson(k2, n2), mean_dF_4hz=boot_mean(d4), mean_dF_2hz=boot_mean(d2),
              state=v1_state(k4, n4, k2, n2))
    pairs = [(v["ff2"], v["ff21"]) for v in valf.values() if v.get("ff2") is not None and v.get("ff21") is not None]
    nv = len(pairs)
    kv = int(sum(1 for a, b in pairs if a >= 1.12 * b))
    v2 = dict(n=nv, k=kv, prop=kv / nv if nv else float("nan"), wilson=wilson(kv, nv) if nv else [float("nan")] * 2,
              state=v2_state(kv, nv),
              ff2_median=float(np.median([a for a, _ in pairs])) if pairs else None,
              ff21_median=float(np.median([b for _, b in pairs])) if pairs else None)
    g3 = "pass" if (v1["state"] == "pass" and v2["state"] == "pass") else ("fail" if "fail" in (v1["state"], v2["state"]) else "inconclusive")
    return dict(V1=v1, V2=v2, G3=g3)


def main(out, pilot=False):
    TS = tuning_summary(out)
    tdir = os.path.join(out, "tuning")
    stand_in = os.path.exists(os.path.join(tdir, "stand_in.json"))
    R = dict(pilot=pilot, tuning=TS, stand_in=stand_in, verdict_module="S-1's rules, imported from aggregate_s001 (PREDICTION.md)")
    if not TS["sets"] and not stand_in:
        R["outcome"] = "no_tuning"
        R["verdicts"] = dict(P1="NOT RUN: no parameter set met the calibration targets",
                             P2="NOT RUN: no parameter set met the calibration targets")
        with open(os.path.join(out, "results.json"), "w") as f:
            json.dump(R, f, indent=1, default=_default)
        write_md_no_tuning(R, out, pilot)
        try:
            plot_tuning(R, out)
        except Exception as e:
            print("plot failed:", e)
        return

    R["outcome"] = "ensemble"
    models = {os.path.basename(p): jload(p) for p in sorted(glob.glob(os.path.join(out, "model", "m*.json")))}
    models = {k: v for k, v in models.items() if not v.get("undrivable")}
    stoch = _load(os.path.join(out, "stoch"), "m*.json")
    tests = _load(os.path.join(out, "tests"), "m*.json")
    abm = {k: v for k, v in _load(os.path.join(out, "ab"), "a*.json").items() if not v.get("undrivable")}
    valf = _load(os.path.join(out, "val"), "m*.json")
    summ = jload(os.path.join(out, "accept_summary.json"))
    conv = _load(os.path.join(out, "converge"), "m*.json")
    R.update(n_models=len(models), n_stoch_models=len(stoch), n_ab=len(abm))
    min_n = 30 if not pilot else 3

    ffall = np.array(summ["ff_all_candidates"])
    sets_of = summ.get("set_of_accepted", [])
    R["acceptance"] = dict(
        n_candidates=len(ffall), n_accepted=summ["n_accepted"], n_target=summ["n_target"], max_candidates=summ["max_candidates"],
        rate=summ["n_accepted"] / len(ffall) if len(ffall) else float("nan"), range_hz=summ["range_hz"],
        n_in_range=summ["n_in_range"], n_in_range_undrivable=summ["n_in_range_undrivable"],
        ff_median_accepted=float(np.median(summ["ff"])) if summ["ff"] else None,
        n_tight_2_15=int(sum(1 for f in summ["ff"] if f <= 15.0)),
        accepted_per_set=[int(sum(1 for s in sets_of if s == j)) for j in range(max(1, len(TS["sets"])))])

    R["F_by_regular_rate"] = {f"reg{fr}@{amp}": rate_row(models, f"reg{fr}@{amp}") for amp in AMPS for fr in FREQS}
    base = [fval(m["runs"].get("none")) for m in models.values()]
    R["F_probe_only_baseline"] = boot_mean(base)
    R["F_probe_only_baseline"]["max"] = float(np.nanmax(base)) if len(base) else float("nan")

    cells = [p1_cell(models, stoch, p, a, min_n) for p in PATTERNS for a in AMPS]
    R["P1"] = dict(cells=cells, verdict_if_gates_pass=verdict_p1(cells))
    p2 = [p2_cell(models, a) for a in AMPS]
    R["P2"] = dict(cells=p2, verdict_if_gates_pass=verdict_p2(p2))
    sub = {k: v for k, v in models.items() if k in stoch}
    R["P1_burst_on_subsample"] = [p1_cell(sub, stoch, "burst", a, min_n) for a in AMPS]
    tight = {k: v for k, v in models.items() if v["k"] is not None and summ["ff"][v["k"]] <= 15.0}
    R["P2_tight_range_2_15Hz"] = [p2_cell(tight, a) for a in AMPS]

    T10 = {}
    for key in ("none@probe10", "reg20@probe10", "reg80@probe10", "burst@probe10", "none@probe5", "reg20@probe5", "reg80@probe5"):
        T10[key] = boot_mean([fval(t["runs"].get(key)) for t in tests.values()])
    for pat in ("poisson", "jitter"):
        per = []
        for t in tests.values():
            v = [fval(r) for kk, r in t["runs"].items() if kk.startswith(f"{pat}@probe10#")]
            v = [x for x in v if np.isfinite(x)]
            if v:
                per.append(float(np.mean(v)))
        T10[f"{pat}@probe10"] = boot_mean(per)
    T10["reg80_minus_reg20_probe10"] = boot_mean([fval(t["runs"].get("reg80@probe10")) - fval(t["runs"].get("reg20@probe10")) for t in tests.values()])
    R["test_trains_subsample"] = T10
    R["drive_matched_diagnostic"] = dict(
        note="post hoc: reg80 at 1.5x its own steady-state drive threshold, 2 Hz probes",
        n_subsample=len(tests), n_with_d80_found=sum(1 for t in tests.values() if t.get("d80")),
        F_reg80_driven=boot_mean([fval(t["runs"].get("reg80@drive80")) for t in tests.values()]),
        F_reg20=boot_mean([fval(models[k]["runs"].get("reg20@1.5")) for k in tests if k in models]))

    abF = {}
    for amp in AMPS:
        for pat in ("reg4", "reg20", "reg40", "reg60", "reg80", "burst", "poisson", "jitter"):
            abF[f"{pat}@{amp}"] = boot_mean([fval(m["runs"].get(f"{pat}@{amp}")) for m in abm.values()])
    R["abeta_F"] = abF

    # G2: population progressive block at regular 20 Hz, 1.5x (S-1's Chao criteria + onset floor)
    r20 = [m["runs"].get("reg20@1.5", {}) for m in models.values()]
    tb = [r.get("t_block_ms") for r in r20]
    onsets = [(t - TU.STIM_START_MS) / 1000.0 if t is not None else float("inf") for t in tb]
    defined = [o for o in onsets if np.isfinite(o)]
    early = [fval(r, "F_early") for r in r20]
    late = [fval(r, "F_late") for r in r20]
    prog = [l - e for l, e in zip(late, early) if np.isfinite(l) and np.isfinite(e)]
    chao = dict(
        n=len(r20),
        frac_block_defined_within_20s=(sum(1 for o in onsets if o <= 20.0) / len(onsets)) if onsets else float("nan"),
        onset_s_median_all=float(np.median(onsets)) if onsets else float("nan"),
        onset_s_median_defined=float(np.median(defined)) if defined else None,
        n_onset_defined=len(defined),
        F_early_median=float(np.nanmedian(early)) if early else float("nan"),
        F_late_median=float(np.nanmedian(late)) if late else float("nan"),
        F_late_minus_F_early_median=float(np.median(prog)) if prog else float("nan"),
        abeta_F_reg20_1_5=abF["reg20@1.5"])
    chao["a_pass"] = bool(chao["frac_block_defined_within_20s"] >= 0.5)
    chao["a2_pass"] = bool(np.isfinite(chao["onset_s_median_all"]) and chao["onset_s_median_all"] >= TU.B3_ONSET_S[0])
    chao["b_pass"] = bool(np.isfinite(chao["F_late_minus_F_early_median"]) and chao["F_late_minus_F_early_median"] >= 0.20)
    chao["c_pass"] = bool(abF["reg20@1.5"]["n"] > 0 and abF["reg20@1.5"]["hi"] < 0.05)
    g2 = bool(chao["a_pass"] and chao["a2_pass"] and chao["b_pass"] and chao["c_pass"])
    g1 = bool((not stand_in) and TS["sets"] and all(s["check"]["pass"] for s in TS["sets"]))
    ho = held_out(models, valf)
    ho["info_1_0x"] = held_out(models, valf, amp=1.0)["V1"]
    R["held_out"] = ho
    R["gates"] = dict(G1=g1, G2=g2, G3=ho["G3"], chao=chao)

    # convergence
    cv = {}
    for k, c in conv.items():
        cv.setdefault(c["k"], {})[c["dt"]] = c
    diffs, flips = [], 0
    for k, d in cv.items():
        if 0.025 in d and 0.0125 in d:
            v = {dt: {p: fval(d[dt]["runs"][p]) for p in ("reg20", "reg80", "burst")} for dt in (0.025, 0.0125)}
            for pat in ("reg20", "reg80", "burst"):
                a_, b_ = v[0.025][pat], v[0.0125][pat]
                if np.isfinite(a_) and np.isfinite(b_):
                    diffs.append(abs(a_ - b_))
            for fn in (lambda x: abs(x["burst"] - x["reg20"]) <= 0.10, lambda x: x["reg80"] >= x["reg20"] - 0.01):
                try:
                    if fn(v[0.025]) != fn(v[0.0125]):
                        flips += 1
                except Exception:
                    pass
    R["convergence"] = dict(n_models=len(cv), median_abs_dF=float(np.median(diffs)) if diffs else None,
                            max_abs_dF=float(np.max(diffs)) if diffs else None,
                            n_abs_dF_gt_0_05=int(sum(1 for x in diffs if x > 0.05)), n_comparisons=len(diffs),
                            classification_flips=flips,
                            pass_=bool(diffs and np.median(diffs) <= 0.02 and flips == 0))
    n_ok = bool(summ["n_accepted"] >= summ["n_target"])
    dec = decide(g1, g2, ho["G3"], n_ok if not pilot else True, R["P1"]["verdict_if_gates_pass"],
                 R["P2"]["verdict_if_gates_pass"], R["convergence"]["pass_"])
    R["verdicts"] = dict(P1=dec["P1"], P2=dec["P2"], gates_ok=dec["gates_ok"], reasons=dec["reasons"],
                         G1="PASS" if g1 else "FAIL", G2="PASS" if g2 else "FAIL", G3=ho["G3"].upper())

    with open(os.path.join(out, "results.json"), "w") as f:
        json.dump(R, f, indent=1, default=_default)
    write_md(R, out, pilot)
    try:
        write_plots(R, out)
        plot_tuning(R, out)
    except Exception as e:  # plotting must never lose the numbers
        print("plot failed:", e)


def _default(o):
    if isinstance(o, float) and not np.isfinite(o):
        return None
    if isinstance(o, np.floating):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    return None


# --- markdown ------------------------------------------------------------------------

def pr(p):
    return ", ".join(f"{k}={v:.4g}" if isinstance(v, float) else f"{k}={v}" for k, v in p.items())


def tuning_md(R, A):
    T = R["tuning"]
    F = T["funnel_all"]
    A("## Tuning")
    A("")
    A(f"Search space, method and selection criterion: `PREDICTION.md` ('Tuning search space'). Round 1: {T['funnel_r1']['n']} Latin-hypercube candidates"
      + (f"; round 2 ran ({T['funnel_r2']['n']} local candidates around candidates {', '.join(str(c) for c in T['centres'])}), because fewer than 3 round-1 candidates met the targets." if T["round2_ran"] else "; round 2 did not run (at least 3 round-1 candidates met the targets, or none had a calibration run to centre on)."))
    A("")
    A("Calibration targets: Na+Kdr 82.5-137.5 Hz, +KCNQ/M 22.5-37.5 Hz, +Ca-dependent K 4.5-7.5 Hz (Sundt 2015); and, at regular 20 Hz, 1.5x, B1 F(first 5 s) <= 0.50, B2 F(last 10 s) >= 0.80, B3 block onset between 2 and 20 s after stimulation starts (Chao 2020).")
    A("")
    A("| Stage of the funnel (all search candidates) | Rounds 1 + 2 | Round 1 | Round 2 |")
    A("|---|---|---|---|")
    rows = (("candidates", "n"), ("Na+Kdr following frequency in band", "n_na_k_band"), ("+KCNQ/M in band (of those that passed the first)", "n_kcnq_band"),
            ("+SK following frequency in 2-40 Hz (calibration run done)", "n_sk_2_40"), ("of which in the 4.5-7.5 Hz band", "n_sk_band"),
            ("undrivable (no calibration run)", "n_undrivable"), ("calibration runs completed", "n_calibrated"),
            ("B1 holds (of calibrated)", "n_B1"), ("B2 holds", "n_B2"), ("B3 holds (onset 2-20 s)", "n_B3"),
            ("B1, B2 and B3 all hold, counting only the calibration-run candidates and ignoring whether their Sundt bands hold", "n_block_all"), ("**meet every calibration target**", "n_meets"))
    for lab, key in rows:
        A(f"| {lab} | {F[key]} | {T['funnel_r1'][key]} | {T['funnel_r2'][key]} |")
    A("")
    if F["n_calibrated"]:
        A(f"Among the {F['n_calibrated']} calibrated candidates: median F in the first 5 s = {f2(F['F_early_median'])}, median F in the last 10 s = {f2(F['F_late_median'])}; "
          f"block onset is under 2 s in {F['n_onset_under_2s']}, between 2 and 20 s in {F['n_B3']}, over 20 s in {F['n_onset_over_20s']} and absent in {F['n_onset_none']}"
          + (f"; median onset where defined {f2(F['onset_median_defined_s'])} s." if F["onset_median_defined_s"] is not None else "."))
        A("")
        A("Best five calibrated candidates by J (calibration targets only; d = ln(ff/target)/ln(1.25) for the three following frequencies; the bands are ±25% linear, so the band edges are at d = +1.00 and d = -1.29, and the 'in Sundt bands' column states directly whether each following frequency is inside its band):")
        A("")
        A("| id | J | ff Na+Kdr / +KCNQ / +SK (Hz) | d | in Sundt bands (Na+Kdr / +KCNQ / +SK) | F early / late | onset (s) | SK in stem | meets |")
        A("|---|---|---|---|---|---|---|---|---|")
        for b in T["best"]:
            A(f"| {b['id']} | {b['J']:.3f} | {b['ff']['na_k']:.1f} / {b['ff']['kcnq']:.1f} / {b['ff']['sk']:.1f} | {b['d']['na_k']:.2f} / {b['d']['kcnq']:.2f} / {b['d']['sk']:.2f} | {' / '.join('yes' if TU.in_band(n, b['ff'][n]) else 'NO' for n in ('na_k', 'kcnq', 'sk'))} | {f2(b['F_early'])} / {f2(b['F_late'])} | {f2(b['flags']['onset_s'])} | {b['params']['sk_stem']} | {'yes' if b['meets'] else 'no'} |")
        A("")
    A(f"**{F['n_meets']} of {F['n']} candidates met every calibration target; {len(T['sets'])} set(s) selected** (selected sets must also reproduce the three bands at dt/2 and break the third band when SK is removed).")
    A("")
    if T["sets"]:
        A("| id | J | parameters | ff dt/2 (Hz) | SK-removed ff (Hz) | passes dt/2 | passes mutation |")
        A("|---|---|---|---|---|---|---|")
        for s in T["sets"]:
            c = s["check"]
            A(f"| {s['id']} | {s['J']:.3f} | {pr(s['params'])} | {c['ff_half']['na_k']:.1f} / {c['ff_half']['kcnq']:.1f} / {c['ff_half']['sk']:.1f} | {c['mutation_ff']:.1f} | {c['pass_dt_half']} | {c['pass_mutation']} |")
        A("")
    if R.get("stand_in"):
        A("**PILOT ONLY: no candidate met the targets, so S-1's SK configuration was used as a stand-in set to exercise the later stages. It is not a selected set.**")
        A("")


def write_md_no_tuning(R, out, pilot):
    L = []
    A = L.append
    A("# S-1b results: re-tuned T-junction model, rate versus pattern" + (" (PILOT, not a result)" if pilot else ""))
    A("")
    A("**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.")
    A("")
    A("Pre-registration: `PREDICTION.md` (commit #1). Rules for P1 and P2 are S-1's, imported unchanged; they were not applied because the search found no set to apply them to.")
    A("")
    A("## Verdicts")
    A("")
    A("| Item | Result |")
    A("|---|---|")
    A(f"| Tuning | **{NO_TUNING}** |")
    A(f"| P1 pattern is approximately rate | {R['verdicts']['P1']} |")
    A(f"| P2 no human ordering | {R['verdicts']['P2']} |")
    A("")
    F = R["tuning"]["funnel_all"]
    if F["n_calibrated"]:
        A(f"**What this rules out, and what it points to.** Of the {F['n_calibrated']} calibrated candidates, {F['n_onset_under_2s']} block in under 2 s and B1 (F in the first 5 s at most 0.50) holds in {F['n_B1']}; B2 holds in {F['n_B2']} and B3 (onset 2 to 20 s) in {F['n_B3']}. Of the {F['n_B3']} with onset between 2 and 20 s, {F['n_B1_and_B3']} also meet B1 (the rest have F above 0.50 in the first 5 s). Within this declared space and channel set, then, a block that builds progressively by the B1 to B3 definition is not found: the Ca-dependent K block arrives within seconds. That points to a slower process, for example the ion-gradient run-down mechanism of Ladez, Liu, Chen and Feng (EMBC 2024, PMID 40039770), as a candidate for a next pre-registered run. This is a pointer, not a conclusion; nothing here tests that mechanism.")
        A("")
    A(f"This statement is about the declared space and model class only (nine parameters, ranges in `PREDICTION.md`; Sundt-type channels). It is a search result, not an exhaustive scan: {F['n']} sampled candidates, of which {F['n_calibrated']} reached the calibration run (the funnel is in the table below). It does not say that no model could do both, and it is not a result about patients.")
    A("")
    tuning_md(R, A)
    A("## Visual traces")
    A("")
    A("`visual-traces.json` holds 30 s voltage traces (soma, T-junction, central axon) of the best-scoring calibrated candidate under no stimulation, regular 20 Hz, regular 80 Hz and burst, so that the failure can be inspected. It is labelled in the file as not meeting the calibration targets.")
    A("")
    with open(os.path.join(out, "results.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def cond_line(name, R):
    v = R[name]["verdict_if_gates_pass"]
    if R["verdicts"]["gates_ok"]:
        return f"{name}: **{R['verdicts'][name]}**."
    return (f"*Conditional reading, NOT a verdict ({'; '.join(R['verdicts']['reasons'])}): the rule applied to these numbers "
            f"would give {v.lower()}. See 'Conditional readings, NOT verdicts' below.*")


def write_md(R, out, pilot):
    L = []
    A = L.append
    A("# S-1b results: re-tuned T-junction model, rate versus pattern" + (" (PILOT, not a result)" if pilot else ""))
    A("")
    A("**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.")
    A("")
    A(f"Pre-registration: `PREDICTION.md` (commit #1; amendments appended below it). Verdict logic: {R['verdict_module']}. `simulations/verdict.py` is not used (t-interval of one mean against one threshold; no Wilson or composite P1/P2 rule), as in S-1.")
    A("")
    for line in run_notes(out):
        A(line)
    v = R["verdicts"]
    A("## Verdicts")
    A("")
    A("| Item | Verdict |")
    A("|---|---|")
    A(f"| G1 calibration reproduced (selected sets: Sundt bands at dt and dt/2, SK-removed mutation) | **{v['G1']}** |")
    A(f"| G2 population progressive block (calibration reproduction, not independent) | **{v['G2']}** |")
    A(f"| G3 held-out validation (V1 and V2, independent) | **{v['G3']}** |")
    A(f"| P1 pattern is approximately rate | {'**' + v['P1'] + '**' if v['gates_ok'] else v['P1']} |")
    A(f"| P2 no human ordering | {'**' + v['P2'] + '**' if v['gates_ok'] else v['P2']} |")
    A("")
    a = R["acceptance"]
    A(f"Population: {R['n_models']} accepted C-neuron variants (target {a['n_target']}; accepted per selected set: {a['accepted_per_set']}); {R['n_stoch_models']} in the stochastic subsample; {R['n_ab']} Aβ comparators.")
    A(f"Acceptance: {a['n_accepted']}/{a['n_candidates']} candidates ({a['rate']:.0%}; {a['n_in_range']} were in range, {a['n_in_range_undrivable']} of those were dropped as undrivable), following frequency {a['range_hz'][0]}-{a['range_hz'][1]} Hz, median {f2(a['ff_median_accepted'])} Hz; {a['n_tight_2_15']} in the tight 2-15 Hz cut.")
    A("")
    tuning_md(R, A)
    g = R["gates"]
    c = g["chao"]
    A("## G2: population progressive block at regular 20 Hz, 1.5x (calibration reproduction, not independent evidence)")
    A("")
    A(f"- (a) block onset within 20 s in {f2(c['frac_block_defined_within_20s'])} of {c['n']} models (need ≥0.5): {'pass' if c['a_pass'] else 'FAIL'}")
    A(f"- (a') median onset (undefined counted as never) {f2(c['onset_s_median_all'])} s (need ≥2 s): {'pass' if c['a2_pass'] else 'FAIL'}; onset defined in {c['n_onset_defined']} models, median {f2(c['onset_s_median_defined'])} s where defined")
    A(f"- (b) median F(late) - F(early) = {f2(c['F_late_minus_F_early_median'])} (need ≥0.20; median F early {f2(c['F_early_median'])}, late {f2(c['F_late_median'])}): {'pass' if c['b_pass'] else 'FAIL'}")
    ab = c["abeta_F_reg20_1_5"]
    A(f"- (c) Aβ F = {f2(ab['mean'])} [{f2(ab['lo'])}, {f2(ab['hi'])}] (need CI upper < 0.05): {'pass' if c['c_pass'] else 'FAIL'}")
    A("")
    ho = R["held_out"]
    v1, v2 = ho["V1"], ho["V2"]
    A("## Held-out validation (never used in tuning)")
    A("")
    A("V1 (Kent et al. 2018, PMID 29377442: filtering amplified with stimulation at frequencies above 2 Hz): per model, dF(f) = F(regular f Hz, 1.5x) - F(probe-only baseline).")
    A("")
    A("| Quantity | n | proportion | Wilson 95% | mean dF [95% CI] |")
    A("|---|---|---|---|---|")
    A(f"| dF(4 Hz) ≥ 0.20 | {v1['n_4hz']} | {f2(v1['prop_4hz'])} | [{f2(v1['wilson_4hz'][0])}, {f2(v1['wilson_4hz'][1])}] | {f2(v1['mean_dF_4hz']['mean'])} [{f2(v1['mean_dF_4hz']['lo'])}, {f2(v1['mean_dF_4hz']['hi'])}] |")
    A(f"| dF(2 Hz) ≤ 0.10 | {v1['n_2hz']} | {f2(v1['prop_2hz'])} | [{f2(v1['wilson_2hz'][0])}, {f2(v1['wilson_2hz'][1])}] | {f2(v1['mean_dF_2hz']['mean'])} [{f2(v1['mean_dF_2hz']['lo'])}, {f2(v1['mean_dF_2hz']['hi'])}] |")
    A("")
    i1 = ho["info_1_0x"]
    A(f"V1 result: **{v1['state'].upper()}**. (Information only, 1.0x: proportion with dF(4 Hz) ≥ 0.20 is {f2(i1['prop_4hz'])}, with dF(2 Hz) ≤ 0.10 is {f2(i1['prop_2hz'])}.) Amplitude and SK-dependence are not used as held-out features (`PREDICTION.md`).")
    A("")
    A(f"V2 (Gemes et al. 2013, PMID 23148321: following frequency slower for 20 APs than for two): ff(2 pulses) ≥ 1.12 x ff(21 pulses) in {v2['k']}/{v2['n']} models, proportion {f2(v2['prop'])}, Wilson 95% [{f2(v2['wilson'][0])}, {f2(v2['wilson'][1])}] (need ≥0.90 with lower bound ≥0.85). Median ff2 {f2(v2['ff2_median'])} Hz against median ff21 {f2(v2['ff21_median'])} Hz. V2 result: **{v2['state'].upper()}**.")
    A("")
    A(f"G3 (V1 and V2 both pass): **{ho['G3'].upper()}**.")
    A("")
    A("## F by regular rate (probe-only baseline: " + f"mean {f2(R['F_probe_only_baseline']['mean'])}, max over models {f2(R['F_probe_only_baseline']['max'])})")
    A("")
    A("F is computed on *scored* probes only: probes that reach the pre-junction site and are not ambiguous with a stimulus spike. `F_all` keeps the ambiguous probes. The two differ, in a direction and size that depend on the rate; the last column reports the failure rate of the scored and of the excluded probes pooled over models. Where the scored fraction is small, F is a statement about the gaps between stimulus volleys.")
    A("")
    A("| Rate | Amp | F mean | 95% CI | F_all mean | n models | mean probes (test / arrived / scored) | scored / test | median fraction of pulses evoking a spike | failure rate: scored / excluded probes |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for key, t in R["F_by_regular_rate"].items():
        rate, amp = key[3:].split("@")
        A(f"| {rate} Hz | {amp}x | {f2(t['F_mean'])} | [{f2(t['F_ci'][0])}, {f2(t['F_ci'][1])}] | {f2(t['F_all_mean'])} | {t['n']} | {t['n_test_mean']:.1f} / {t['n_arrived_mean']:.1f} / {t['n_scored_mean']:.1f} | {f2(t['scored_over_test'])} | {f2(t['evoked_fraction_median'])} | {f2(t['scored_fail_rate_pooled'])} / {f2(t['excluded_fail_rate'])} |")
    A("")
    A("## P1: pattern versus rate (difference from regular 20 Hz, matched pulse count)")
    A("")
    A("| Pattern | Amp | n | within 10 pts | Wilson 95% | mean diff | 95% CI |")
    A("|---|---|---|---|---|---|---|")
    for c in R["P1"]["cells"]:
        A(f"| {c['pattern']} | {c['amp']}x | {c['n']} | {f2(c['prop_within_10pts'])} | [{f2(c['wilson'][0])}, {f2(c['wilson'][1])}] | {f2(c['mean_diff'])} | [{f2(c['diff_ci'][0])}, {f2(c['diff_ci'][1])}] |")
    A("")
    A(cond_line("P1", R))
    A("")
    A("## P2: F(80 Hz) versus F(20 Hz)")
    A("")
    A("| Amp | n | F20 | F80 | F80≥F20 (1-pt tol) | Wilson 95% | literal | models with ≥20% relative fall | Wilson 95% | evoked frac 20 / 80 Hz |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for c in R["P2"]["cells"]:
        if c.get("n"):
            A(f"| {c['amp']}x | {c['n']} | {f2(c['mean_F20'])} | {f2(c['mean_F80'])} | {f2(c['prop_f80_ge_f20_tol'])} | [{f2(c['wilson'][0])}, {f2(c['wilson'][1])}] | {f2(c['prop_literal'])} | {f2(c['prop_fall_ge_20pct'])} (of {c['n_with_F20_ge_0_05']}) | [{f2(c['wilson_fall'][0])}, {f2(c['wilson_fall'][1])}] | {f2(c['evoked_fraction_median_20Hz'])} / {f2(c['evoked_fraction_median_80Hz'])} |")
    A("")
    A(cond_line("P2", R))
    A("")
    d = R["drive_matched_diagnostic"]
    t = R["test_trains_subsample"]
    cv = R["convergence"]
    A("## Diagnostics (not pre-registered thresholds)")
    A("")
    if d["n_with_d80_found"] == 0:
        A(f"- Drive-matched 80 Hz, post hoc: unavailable (no multiple up to 12x drove 90% of late pulses in {d['n_subsample']} subsample models).")
    else:
        A(f"- Drive-matched, post hoc: 80 Hz at 1.5x its own drive threshold (found in {d['n_with_d80_found']}/{d['n_subsample']} models) gives F = {f2(d['F_reg80_driven']['mean'])} [{f2(d['F_reg80_driven']['lo'])}, {f2(d['F_reg80_driven']['hi'])}] against regular 20 Hz F = {f2(d['F_reg20']['mean'])} on the same subsample.")
    A(f"- Pre-registered 10 Hz test train, subsample: F(none)={f2(t['none@probe10']['mean'])}, F(20 Hz)={f2(t['reg20@probe10']['mean'])}, F(80 Hz)={f2(t['reg80@probe10']['mean'])}, F(burst)={f2(t['burst@probe10']['mean'])}, F(Poisson)={f2(t['poisson@probe10']['mean'])}, F(jitter)={f2(t['jitter@probe10']['mean'])}; F(80)-F(20) = {f2(t['reg80_minus_reg20_probe10']['mean'])} [{f2(t['reg80_minus_reg20_probe10']['lo'])}, {f2(t['reg80_minus_reg20_probe10']['hi'])}].")
    A(f"- 5 Hz test train: F(none)={f2(t['none@probe5']['mean'])}, F(20 Hz)={f2(t['reg20@probe5']['mean'])}, F(80 Hz)={f2(t['reg80@probe5']['mean'])}.")
    A(f"- dt-halving (0.025 vs 0.0125 ms), {cv['n_models']} models: median |dF| = {f2(cv['median_abs_dF'])}, max {f2(cv['max_abs_dF'])}; {cv['n_abs_dF_gt_0_05']}/{cv['n_comparisons']} comparisons with |dF| > 0.05; classification flips: {cv['classification_flips']}; {'pass' if cv['pass_'] else 'FAIL, INCONCLUSIVE'}.")
    A("")
    if not pilot:
        for line in shows(R):
            A(line)
    A("## Aβ comparator F")
    A("")
    A("| Condition | mean F | 95% CI |")
    A("|---|---|---|")
    for key, b in R["abeta_F"].items():
        A(f"| {key} | {f2(b['mean'])} | [{f2(b['lo'])}, {f2(b['hi'])}] |")
    A("")
    with open(os.path.join(out, "results.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def run_notes(out):
    """Resumes, read from the start lines in run.log."""
    p = os.path.join(out, "run.log")
    if not os.path.exists(p):
        return []
    starts = [" ".join(ln.split()[:2]) for ln in open(p) if " start main" in ln or " start pilot" in ln]
    if len(starts) < 2:
        return []
    return ["## Run notes", "",
            f"`run.log` has {len(starts)} start lines ({'; '.join(starts)}): the run was resumed after the process stopped (the cause is not recorded in the log). "
            "A resume reuses every per-model file already present and recomputes only the missing ones; results are deterministic given the per-model seeds.", ""]


def shows(R):
    """'What this run shows': every number computed from R, sentences chosen by data."""
    T = R["F_by_regular_rate"]
    f2h, f4, f20, f80 = (T[f"reg{r}@1.5"] for r in (2, 4, 20, 80))
    g, v = R["gates"], R["verdicts"]
    c = g["chao"]
    ho = R["held_out"]
    base = R["F_probe_only_baseline"]
    L = ["## What this run shows", ""]
    if v["gates_ok"]:
        L += ["All three gates passed; the P1 and P2 entries in the verdict table are the pre-registered rules' outputs.", ""]
    else:
        L += [f"P1 and P2 are **NO VERDICT** as pre-registered: {'; '.join(v['reasons'])}.", ""]
    L += [f"**(a) Time course at regular 20 Hz, 1.5x.** Median F in the first 5 s is {f2(c['F_early_median'])} and in the last 10 s {f2(c['F_late_median'])} "
          f"(difference {f2(c['F_late_minus_F_early_median'])}); block onset is within 20 s in {f2(c['frac_block_defined_within_20s'])} of models, with median onset {f2(c['onset_s_median_defined'])} s where defined. "
          f"The probe-only baseline is F = {f2(base['mean'])} (max over models {f2(base['max'])}). "
          "This is the property that was tuned; it is not independent evidence.", ""]
    L += [f"**(b) Held-out V1.** F(2 Hz) = {f2(f2h['F_mean'])}, F(4 Hz) = {f2(f4['F_mean'])}, F(20 Hz) = {f2(f20['F_mean'])} at 1.5x against the probe-only {f2(base['mean'])}; "
          f"{f2(ho['V1']['prop_4hz'])} of models show dF(4 Hz) ≥ 0.20 and {f2(ho['V1']['prop_2hz'])} show dF(2 Hz) ≤ 0.10. V1 is **{ho['V1']['state']}**. "
          f"V2 is **{ho['V2']['state']}** ({ho['V2']['k']}/{ho['V2']['n']} models with ff(2 pulses) at least one grid step above ff(21 pulses)).", ""]
    ev20, ev80 = f20["evoked_fraction_median"], f80["evoked_fraction_median"]
    s = (f"**(c) What high rates do.** At the junction-side stem site, the median fraction of pulses that evoke a spike is {f2(ev20)} at 20 Hz and {f2(ev80)} at 80 Hz (1.5x); "
         f"F(80 Hz) = {f2(f80['F_mean'])} against F(20 Hz) = {f2(f20['F_mean'])}. "
         f"F(80 Hz) is computed on {f2(f80['n_scored_mean'])} of {f2(f80['n_test_mean'])} probes per model ({f2(f80['scored_over_test'])}) against {f2(f20['n_scored_mean'])} of {f2(f20['n_test_mean'])} at 20 Hz ({f2(f20['scored_over_test'])}); "
         f"F_all is {f2(f80['F_all_mean'])} at 80 Hz and {f2(f20['F_all_mean'])} at 20 Hz; the failure rate of excluded probes at 80 Hz is {f2(f80['excluded_fail_rate'])} against {f2(f80['scored_fail_rate_pooled'])} for scored probes. ")
    if f80["F_all_mean"] is not None and f80["F_mean"] is not None and abs(f80["F_all_mean"] - f80["F_mean"]) > 0.10:
        s += "F and F_all differ by more than 0.10 at 80 Hz, so the size of any rate effect depends on the exclusion rule. "
    if ev80 is not None and ev20 and ev80 < 0.5 * ev20:
        s += "The stimulus largely stops evoking spikes at 80 Hz, so an F change with rate cannot be read as filtering. "
    L += [s, ""]
    if not v["gates_ok"]:
        L += ["## Conditional readings, NOT verdicts", "",
              f"Applying the pre-registered rules to these numbers anyway: P1 would read {R['P1']['verdict_if_gates_pass'].lower()}; P2 would read {R['P2']['verdict_if_gates_pass'].lower()}. "
              "They carry no evidential weight because a gate failed.", ""]
        cvr = R["convergence"]
        if not cvr["pass_"]:
            L += [f"The dt-halving check also failed ({cvr['classification_flips']} flip(s); {cvr['n_abs_dF_gt_0_05']} of {cvr['n_comparisons']} comparisons with |dF| > 0.05).", ""]
    return L


# --- plots ------------------------------------------------------------------------------

def write_plots(R, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for i, amp in enumerate(AMPS):
        xs = list(FREQS)
        t = R["F_by_regular_rate"]
        ys = [t[f"reg{f}@{amp}"]["F_mean"] for f in xs]
        lo = [t[f"reg{f}@{amp}"]["F_ci"][0] for f in xs]
        hi = [t[f"reg{f}@{amp}"]["F_ci"][1] for f in xs]
        ax[i].errorbar(xs, ys, yerr=[np.array(ys) - np.array(lo), np.array(hi) - np.array(ys)], marker="o", capsize=3)
        ax[i].set_ylim(0, 1.05)
        ax[i].set_xlabel("regular stimulation rate (Hz)")
        ax[i].set_ylabel("filtering index F (2 Hz probe)")
        ax[i].set_title(f"{amp}x drive threshold")
    fig.suptitle("S-1b: F against rate (mean and bootstrap 95% CI across models)")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "F-vs-rate.png"), dpi=110)
    plt.close(fig)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for i, amp in enumerate(AMPS):
        cells = [c for c in R["P1"]["cells"] if c["amp"] == amp]
        xs = np.arange(len(cells))
        m = [c["mean_diff"] for c in cells]
        lo = [c["diff_ci"][0] for c in cells]
        hi = [c["diff_ci"][1] for c in cells]
        ax[i].errorbar(xs, m, yerr=[np.array(m) - np.array(lo), np.array(hi) - np.array(m)], fmt="o", capsize=4)
        for y, ls, col in ((0.10, "--", "k"), (-0.10, "--", "k"), (0.20, ":", "r")):
            ax[i].axhline(y, ls=ls, c=col, lw=0.8)
        ax[i].set_xticks(xs)
        ax[i].set_xticklabels([c["pattern"] for c in cells])
        ax[i].set_ylabel("F(pattern) - F(regular 20 Hz)")
        ax[i].set_title(f"{amp}x drive threshold")
    fig.suptitle("S-1b P1: matched-rate patterns against regular 20 Hz (dashed: ±10 pts; dotted: refutation bar)")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "P1-pattern-minus-rate.png"), dpi=110)
    plt.close(fig)


def plot_tuning(R, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    pts = R["tuning"]["points"]
    fig, ax = plt.subplots(figsize=(6, 4.5))
    lo, hi = TU.band(TU.TARGET_HZ["sk"])
    ax.axvspan(lo, hi, color="0.9", label="Sundt 6 Hz band")
    ax.axhspan(TU.B3_ONSET_S[0], TU.B3_ONSET_S[1], color="0.93", label="onset 2-20 s")
    for p in pts:
        y = p["onset_s"] if p["onset_s"] is not None else 0.05
        ax.scatter(p["ff_sk"], y, c="tab:green" if p["meets"] else "tab:blue", s=14)
    ax.set_yscale("log")
    ax.set_xlabel("following frequency, +SK configuration (Hz)")
    ax.set_ylabel("block onset at regular 20 Hz, 1.5x (s; 0.05 = none)")
    ax.set_title("S-1b: calibrated search candidates")
    ax.legend(loc="upper right", fontsize=7)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "tuning-funnel.png"), dpi=110)
    plt.close(fig)
