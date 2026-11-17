"""Aggregate S-1 per-model files into results.json / results.md / PNGs.

Verdict logic: simulations/verdict.py (the shared module) is used if it exists;
otherwise the local rule below, which implements the rules fixed in PREDICTION.md:
bootstrap 95% CI (10000 resamples, percentile) for means, Wilson 95% interval
for proportions, INCONCLUSIVE whenever an interval spans its threshold.
"""

import glob
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED_VERDICT = os.path.join(os.path.dirname(HERE), "verdict.py")
AMPS = (1.0, 1.5)
PATTERNS = ("poisson", "burst", "jitter")
FREQS = (4, 20, 40, 60, 80)
RNG = np.random.default_rng(12345)


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (float(c - h), float(c + h))


def boot_mean(x, n=10000):
    x = np.asarray([v for v in x if v is not None and np.isfinite(v)], dtype=float)
    if len(x) == 0:
        return dict(mean=float("nan"), lo=float("nan"), hi=float("nan"), n=0)
    idx = RNG.integers(0, len(x), (n, len(x)))
    m = x[idx].mean(axis=1)
    return dict(mean=float(x.mean()), lo=float(np.percentile(m, 2.5)), hi=float(np.percentile(m, 97.5)), n=int(len(x)))


def _load(d, pat):
    out = {}
    for p in sorted(glob.glob(os.path.join(d, pat))):
        with open(p) as f:
            out[os.path.basename(p)] = json.load(f)
    return out


def fval(run, key="F"):
    v = run.get(key) if run else None
    return float("nan") if v is None else float(v)


def p1_cell(models, stoch, pattern, amp, min_n):
    """Per-model difference F_pattern - F_reg20 and the P1 statistics."""
    diffs = []
    for k, m in models.items():
        r20 = fval(m["runs"].get(f"reg20@{amp}"))
        if pattern == "burst":
            fx = fval(m["runs"].get(f"burst@{amp}"))
        else:
            s = stoch.get(k)
            if not s:
                continue
            vals = [fval(v) for kk, v in s["runs"].items() if kk.startswith(f"{pattern}@{amp}#")]
            vals = [v for v in vals if np.isfinite(v)]
            fx = float(np.mean(vals)) if vals else float("nan")
        if np.isfinite(r20) and np.isfinite(fx):
            diffs.append(fx - r20)
    d = np.array(diffs)
    n = len(d)
    k_in = int((np.abs(d) <= 0.10).sum()) if n else 0
    w = wilson(k_in, n)
    b = boot_mean(d)
    return dict(pattern=pattern, amp=amp, n=n, prop_within_10pts=k_in / n if n else float("nan"),
                wilson=w, mean_diff=b["mean"], diff_ci=[b["lo"], b["hi"]],
                refute_hit=bool(n and b["mean"] >= 0.20 and b["lo"] > 0.10),
                refute_unresolved=bool(n and b["mean"] >= 0.20 and b["lo"] <= 0.10),
                support_ok=bool(n >= min_n and w[0] >= 0.80), support_unresolved=bool(n and w[0] < 0.80 <= w[1]))


def verdict_p1(cells):
    if any(c["refute_hit"] for c in cells):
        return "REFUTED"
    if all(c["support_ok"] for c in cells):
        return "SUPPORTED"
    if any(c["refute_unresolved"] or c["support_unresolved"] for c in cells):
        return "INCONCLUSIVE"
    return "NOT SUPPORTED, NOT REFUTED"


def p2_cell(models, amp, hi="reg80", lo="reg20"):
    pairs = []
    for k, m in models.items():
        a, b = fval(m["runs"].get(f"{lo}@{amp}")), fval(m["runs"].get(f"{hi}@{amp}"))
        if np.isfinite(a) and np.isfinite(b):
            pairs.append((a, b, m["runs"][f"{lo}@{amp}"].get("n_evoked"), m["runs"][f"{hi}@{amp}"].get("n_evoked"),
                          m["runs"][f"{lo}@{amp}"].get("n_pulses"), m["runs"][f"{hi}@{amp}"].get("n_pulses")))
    arr = np.array([(p[0], p[1]) for p in pairs])
    n = len(arr)
    if n == 0:
        return dict(amp=amp, n=0)
    f20, f80 = arr[:, 0], arr[:, 1]
    k_tol = int((f80 >= f20 - 0.01).sum())
    k_lit = int((f80 >= f20).sum())
    w = wilson(k_tol, n)
    mask = f20 >= 0.05
    nm = int(mask.sum())
    k_fall = int(((f20[mask] - f80[mask]) / f20[mask] >= 0.20).sum()) if nm else 0
    wf = wilson(k_fall, nm)
    ev = np.array([(p[2] / p[4] if p[4] else np.nan, p[3] / p[5] if p[5] else np.nan) for p in pairs], dtype=float)
    return dict(amp=amp, n=n, prop_f80_ge_f20_tol=k_tol / n, wilson=w, prop_literal=k_lit / n,
                mean_F20=float(f20.mean()), mean_F80=float(f80.mean()),
                n_with_F20_ge_0_05=nm, prop_fall_ge_20pct=(k_fall / nm if nm else float("nan")), wilson_fall=wf,
                support_ok=bool(w[0] >= 0.90), support_unresolved=bool(w[0] < 0.90 <= w[1]),
                refute_hit=bool(nm and k_fall / nm > 0.5 and wf[0] > 0.5),
                refute_unresolved=bool(nm and wf[0] <= 0.5 < wf[1]),
                evoked_fraction_median_20Hz=float(np.nanmedian(ev[:, 0])), evoked_fraction_median_80Hz=float(np.nanmedian(ev[:, 1])))


def verdict_p2(cells):
    if any(c.get("refute_hit") for c in cells):
        return "REFUTED"
    if all(c.get("support_ok") for c in cells):
        return "SUPPORTED"
    if any(c.get("support_unresolved") or c.get("refute_unresolved") for c in cells):
        return "INCONCLUSIVE"
    return "NOT SUPPORTED, NOT REFUTED"


def main(out, pilot=False):
    ctl = json.load(open(os.path.join(out, "control.json"))) if os.path.exists(os.path.join(out, "control.json")) else {}
    models = {os.path.basename(p)[:-5]: json.load(open(p)) for p in sorted(glob.glob(os.path.join(out, "model", "m*.json")))}
    models = {k + ".json": v for k, v in models.items() if not v.get("undrivable")}
    stoch = _load(os.path.join(out, "stoch"), "m*.json")
    tests = _load(os.path.join(out, "tests"), "m*.json")
    abm = {k: v for k, v in _load(os.path.join(out, "ab"), "a*.json").items() if not v.get("undrivable")}
    summ = json.load(open(os.path.join(out, "accept_summary.json"))) if os.path.exists(os.path.join(out, "accept_summary.json")) else {}
    conv = _load(os.path.join(out, "converge"), "m*.json")
    R = dict(pilot=pilot, n_models=len(models), n_stoch_models=len(stoch), n_ab=len(abm),
             verdict_module="local rule (PREDICTION.md)")
    min_n = 30 if not pilot else 3

    # acceptance
    if summ:
        ffall = np.array(summ["ff_all_candidates"])
        R["acceptance"] = dict(n_candidates=len(ffall), n_accepted=summ["n_accepted"],
                               rate=summ["n_accepted"] / len(ffall), range_hz=summ["range_hz"],
                               n_in_range=summ.get("n_in_range"), n_in_range_undrivable=summ.get("n_in_range_undrivable"),
                               ff_median_accepted=float(np.median(summ["ff"])),
                               n_tight_2_15=int(sum(1 for f in summ["ff"] if f <= 15.0)))

    # per-frequency tables
    tab = {}
    for amp in AMPS:
        for fr in FREQS:
            vals = [fval(m["runs"].get(f"reg{fr}@{amp}")) for m in models.values()]
            ev = [m["runs"][f"reg{fr}@{amp}"]["n_evoked"] / max(1, m["runs"][f"reg{fr}@{amp}"]["n_pulses"])
                  for m in models.values() if f"reg{fr}@{amp}" in m["runs"]]
            b = boot_mean(vals)
            runs = [m["runs"][f"reg{fr}@{amp}"] for m in models.values() if f"reg{fr}@{amp}" in m["runs"]]
            nt = float(np.mean([r["n_test"] for r in runs]))
            na = float(np.mean([r["n_arrived"] for r in runs]))
            ns = float(np.mean([r["n_scored"] for r in runs]))
            fa = boot_mean([fval(r, "F_all") for r in runs])
            tab[f"reg{fr}@{amp}"] = dict(F_mean=b["mean"], F_ci=[b["lo"], b["hi"]], n=b["n"],
                                         evoked_fraction_median=float(np.median(ev)) if ev else None,
                                         n_test_mean=nt, n_arrived_mean=na, n_scored_mean=ns,
                                         scored_over_test=ns / nt if nt else None,
                                         F_all_mean=fa["mean"], F_all_ci=[fa["lo"], fa["hi"]])
    base = [fval(m["runs"].get("none")) for m in models.values()]
    R["F_by_regular_rate"] = tab
    R["F_probe_only_baseline"] = boot_mean(base)
    R["F_probe_only_baseline"]["max"] = float(np.nanmax(base)) if len(base) else float("nan")

    # P1, P2
    cells = [p1_cell(models, stoch, p, a, min_n) for p in PATTERNS for a in AMPS]
    R["P1"] = dict(cells=cells, verdict_if_control_passes=verdict_p1(cells))
    p2 = [p2_cell(models, a) for a in AMPS]
    R["P2"] = dict(cells=p2, verdict_if_control_passes=verdict_p2(p2))
    # burst on the subsample only, for like-for-like with the stochastic cells
    sub = {k: v for k, v in models.items() if k in stoch}
    R["P1_burst_on_subsample"] = [p1_cell(sub, stoch, "burst", a, min_n) for a in AMPS]
    # tight-range sensitivity
    tight = {k: v for k, v in models.items() if summ and v["k"] is not None and summ["ff"][v["k"]] <= 15.0}
    R["P2_tight_range_2_15Hz"] = [p2_cell(tight, a) for a in AMPS]
    R["P1_burst_tight_range"] = [p1_cell(tight, {}, "burst", a, min_n) for a in AMPS]

    # pre-registered 10 Hz / 5 Hz test trains (subsample only)
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
    R["test_trains_subsample"] = T10
    d10 = [fval(t["runs"].get("reg80@probe10")) - fval(t["runs"].get("reg20@probe10")) for t in tests.values()]
    R["test_trains_subsample"]["reg80_minus_reg20_probe10"] = boot_mean(d10)
    n_d80 = sum(1 for t in tests.values() if t.get("d80"))
    R["drive_matched_diagnostic"] = dict(
        note="post hoc: reg80 at 1.5x its own steady-state drive threshold, 2 Hz probes",
        n_subsample=len(tests), n_with_d80_found=n_d80,
        F_reg80_driven=boot_mean([fval(t["runs"].get("reg80@drive80")) for t in tests.values()]),
        F_reg20=boot_mean([fval(models[k]["runs"].get("reg20@1.5")) for k in tests if k in models]),
        d80_over_d20=boot_mean([t["d80"] / models[k]["drive_thr"] for k, t in tests.items() if k in models and t.get("d80")]))

    # Abeta
    abF = {}
    for amp in AMPS:
        for pat in ("reg4", "reg20", "reg40", "reg60", "reg80", "burst", "poisson", "jitter"):
            abF[f"{pat}@{amp}"] = boot_mean([fval(m["runs"].get(f"{pat}@{amp}")) for m in abm.values()])
    R["abeta_F"] = abF

    # time to block and progression (positive control Chao qualitative)
    tb = [m["runs"].get("reg20@1.5", {}).get("t_block_ms") for m in models.values()]
    tb_def = [t for t in tb if t is not None]
    early = [fval(m["runs"].get("reg20@1.5"), "F_early") for m in models.values()]
    late = [fval(m["runs"].get("reg20@1.5"), "F_late") for m in models.values()]
    prog = [l - e for l, e in zip(late, early) if np.isfinite(l) and np.isfinite(e)]
    Tm = [m["T"] for m in models.values()][:1]
    tb_lim = 20000.0
    chao = dict(
        frac_models_block_defined_within_20s=(sum(1 for t in tb_def if t <= tb_lim) / len(tb)) if tb else float("nan"),
        time_to_block_ms_median=float(np.median(tb_def)) if tb_def else None,
        F_late_minus_F_early_median=float(np.median(prog)) if prog else float("nan"),
        abeta_F_reg20_1_5=abF["reg20@1.5"])
    chao["a_pass"] = bool(chao["frac_models_block_defined_within_20s"] >= 0.5)
    chao["b_pass"] = bool(np.isfinite(chao["F_late_minus_F_early_median"]) and chao["F_late_minus_F_early_median"] >= 0.20)
    chao["c_pass"] = bool(abF["reg20@1.5"]["n"] > 0 and abF["reg20@1.5"]["hi"] < 0.05)
    sundt_pass = bool(ctl and all(ctl[n]["pass"] for n in ("na_k", "kcnq", "sk")))
    R["positive_control"] = dict(sundt=ctl, sundt_pass=sundt_pass, mutation_pass=bool(ctl.get("sk_removed_mutation", {}).get("pass")),
                                 chao_qualitative=chao,
                                 PASS=bool(sundt_pass and chao["a_pass"] and chao["b_pass"] and chao["c_pass"]))
    R["verdicts"] = dict(
        positive_control="PASS" if R["positive_control"]["PASS"] else "FAIL",
        P1=R["P1"]["verdict_if_control_passes"] if R["positive_control"]["PASS"] else "NO VERDICT (positive control failed)",
        P2=R["P2"]["verdict_if_control_passes"] if R["positive_control"]["PASS"] else "NO VERDICT (positive control failed)")

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
            # classification flips (the pre-registered check): burst within 10 pts of
            # reg20, and F80 >= F20 - 0.01, each classified at both dt
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

    with open(os.path.join(out, "results.json"), "w") as f:
        json.dump(R, f, indent=1, default=lambda o: None if (isinstance(o, float) and not np.isfinite(o)) else float(o) if isinstance(o, np.floating) else bool(o) if isinstance(o, np.bool_) else int(o))
    write_md(R, out, pilot)
    try:
        write_plots(R, models, stoch, out)
    except Exception as e:  # plotting must never lose the numbers
        print("plot failed:", e)


def f2(x):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:.3f}"


def shows(R):
    """'What this run shows', every number computed from R; sentences chosen by data."""
    pc, c = R["positive_control"], R["positive_control"]["chao_qualitative"]
    T = R["F_by_regular_rate"]
    f4, f20, f80 = (T[f"reg{r}@1.5"] for r in (4, 20, 80))
    ev20, ev80 = f20["evoked_fraction_median"], f80["evoked_fraction_median"]
    tb = c["time_to_block_ms_median"]
    base = R["F_probe_only_baseline"]
    d = R["drive_matched_diagnostic"]
    cells = R["P1"]["cells"]
    maxdiff = max(abs(x["mean_diff"]) for x in cells)
    minprop = min(x["prop_within_10pts"] for x in cells)
    L = ["## What this run shows", ""]
    if not pc["PASS"]:
        L += ["Nothing here rescues the verdicts: the positive control failed, so P1 and P2 are **NO VERDICT** as pre-registered.", ""]
    else:
        L += ["The positive control passed; the verdicts in the table above are the pre-registered ones.", ""]
    s = (f"**(a) Time course.** F at 1.5x is {f2(f4['F_mean'])} at 4 Hz, {f2(f20['F_mean'])} at 20 Hz and {f2(f80['F_mean'])} at 80 Hz; "
         f"median time-to-block at regular 20 Hz is {f2(tb)} ms; median F(late) - F(early) is {f2(c['F_late_minus_F_early_median'])}. "
         f"The probe-only baseline is F = {f2(base['mean'])} (max over models {f2(base['max'])}), so any block is caused by the stimulation, not by the 2 Hz probe. ")
    if tb is not None and tb < 2000:
        s += "Criterion (a) (block within 20 s) is **vacuous** here: the block is essentially immediate, so passing it says nothing about Chao's *progressive* block. "
    if c["b_pass"]:
        s += "Criterion (b) (progression) passes."
    else:
        s += ("Criterion (b) (progression) fails, so this model does not reproduce a progressive block. "
              "Candidate causes, by what the data can say: the 2 Hz probe is not one (baseline above); the 'threshold' definition is not one if the evoked fraction at 4 Hz is about 1 "
              f"(it is {f2(f4['evoked_fraction_median'])}); the remaining candidate is the tuning amendment (A in `PREDICTION.md`: Ca decay and SK conductance set against Sundt's 6 Hz following frequency). "
              "That last point is a hypothesis; it was not tested by re-tuning, which would need a new pre-registration.")
    L += [s, ""]
    s = (f"**(b) Pattern against rate, in this model.** The largest mean difference from regular 20 Hz across the six cells is {f2(maxdiff)}, and the smallest proportion of models within 10 points is {f2(minprop)}. ")
    if f20["F_mean"] > 0.9:
        s += "F at regular 20 Hz is above 0.9, so there is little room for any pattern to raise it: this is partly a ceiling effect and is weak evidence about pattern in a model that blocks progressively. "
    L += [s, ""]
    s = (f"**(c) What high rates do.** At the junction-side stem site, the median fraction of pulses that evoke a spike is {f2(ev20)} at 20 Hz and {f2(ev80)} at 80 Hz (1.5x); F(80) = {f2(f80['F_mean'])} against F(20) = {f2(f20['F_mean'])}. ")
    if ev80 is not None and ev20 and ev80 < 0.5 * ev20:
        s += "F changes with rate in a regime where the stimulus has largely stopped evoking spikes, so a rate effect on F cannot be read as filtering. "
    else:
        s += "The stimulus keeps evoking spikes at 80 Hz, so the F change is not explained by lost drive. "
    s += (f"F(80 Hz) is computed on probes that cross between stimulus volleys: {f2(f80['n_scored_mean'])} of {f2(f80['n_test_mean'])} probes per model are scored at 80 Hz "
          f"({f2(f80['scored_over_test'])}) against {f2(f20['n_scored_mean'])} of {f2(f20['n_test_mean'])} at 20 Hz ({f2(f20['scored_over_test'])}), and F_all is {f2(f80['F_all_mean'])} at 80 Hz against {f2(f20['F_all_mean'])} at 20 Hz. "
          "So a low F(80) means \"drive intact, and gap probes rarely fail\", not \"a high rate passes the junction\". ")
    if d["n_with_d80_found"] == 0:
        s += f"The post hoc drive-matched 80 Hz run could not be made: no amplitude up to 12x found a drive in {d['n_subsample']}/{d['n_subsample']} models."
    L += [s, ""]
    L += ["**Context, not a result.** A model that could pass this control would have to reproduce Sundt's 6 Hz following frequency *and* a block that builds over tens of seconds, and keep the stem drivable at the high rates. "
          "A rival mechanism exists: Ladez, Liu, Chen and Feng (EMBC 2024, PMID 40039770, NEURON, Markov Nav models) report that DRG stimulation raises intra-axonal Na and lowers K, disrupting transaxonal gradients, "
          "with activity-dependent conduction slowing and eventual block in Aδ and C fibres. That is worth a separate pre-registered run; it is not built here.", ""]
    if not pc["PASS"]:
        L += ["## Conditional readings, NOT verdicts (control failed)", "",
              f"Applying the pre-registered rules to these numbers anyway: P1 would read {R['P1']['verdict_if_control_passes'].lower()}; P2 would read {R['P2']['verdict_if_control_passes'].lower()}. "
              "These are shown only so the reasons are visible. They carry no evidential weight because the model failed its own control.", ""]
        cvr = R["convergence"]
        if not cvr["pass_"]:
            L += [f"**The dt-halving check also FAILED** ({cvr['classification_flips']} pattern-versus-rate classification flip(s) and {cvr['n_abs_dF_gt_0_05']} of {cvr['n_comparisons']} comparisons with |dF| > 0.05, max |dF| {f2(cvr['max_abs_dF'])}), "
                  "so even the conditional readings above are not numerically converged in the time step. This further weakens them; it is not a rounding detail.", ""]
    return L


def run_notes(out):
    """Interruptions and resumes, read from run.log and file times."""
    p = os.path.join(out, "run.log")
    if not os.path.exists(p):
        return []
    starts = [ln.split()[0] for ln in open(p) if "start main" in ln or "start pilot" in ln]
    if len(starts) < 2:
        return []
    import time as _t
    last_model = max((os.path.getmtime(f) for f in glob.glob(os.path.join(out, "model", "m*.json"))), default=0)
    last_cand = max((os.path.getmtime(f) for f in glob.glob(os.path.join(out, "cand", "c*.json"))), default=0)
    fmt = lambda t: _t.strftime("%H:%M", _t.localtime(t))
    return ["## Run notes", "",
            f"The run was started at {starts[0]} and **resumed at {starts[-1]}** ({len(starts)} start lines in `run.log`) after the process was killed (machine restart). "
            f"The resume reused cached per-model files and did not recompute them: the last candidate file was written at {fmt(last_cand)} and the last det model file at {fmt(last_model)}, both before the resume; "
            "the control stage (not cached) was recomputed, and the later stages (stochastic, tests, Aβ, convergence, visual) were run in the resumed process, computing only files not already present. Results are deterministic given the per-model seeds.", ""]


def cond_line(name, R):
    v = R[name]["verdict_if_control_passes"]
    if R["positive_control"]["PASS"]:
        return f"{name}: **{v}**."
    return (f"*Conditional reading, NOT a verdict (positive control failed): the rule applied to these numbers "
            f"would give {v.lower()}. See 'Conditional readings, NOT verdicts' below.*")


def write_md(R, out, pilot):
    L = []
    A = L.append
    A("# S-1 results: DRG T-junction, rate versus pattern" + (" (PILOT, not a result)" if pilot else ""))
    A("")
    A("**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.")
    A("")
    A(f"Verdict logic: {R['verdict_module']} (`simulations/verdict.py` exists on main and gives a t-interval of a mean against one threshold; it has no proportion/Wilson rule and no composite P1/P2 logic, so it is not used here and the local rule stays; `aggregate_s001.py` could cross-check the mean-difference cells with it). Pre-registration: `PREDICTION.md` (commit #1); amendments are listed in `PREDICTION.md` under 'Amendments made in the results commit'.")
    A("")
    v = R["verdicts"]
    for line in run_notes(out):
        A(line)
    A("## Verdicts")
    A("")
    A("| Item | Verdict |")
    A("|---|---|")
    for k, lab in (("positive_control", "Positive control"), ("P1", "P1 pattern is approximately rate"), ("P2", "P2 no human ordering")):
        A(f"| {lab} | **{v[k]}** |")
    A("")
    A(f"Population: {R['n_models']} accepted C-neuron variants; {R['n_stoch_models']} in the stochastic subsample; {R['n_ab']} Aβ comparators.")
    if "acceptance" in R:
        a = R["acceptance"]
        A(f"Acceptance: {a['n_accepted']}/{a['n_candidates']} candidates ({a['rate']:.0%}; {a['n_in_range']} were in range, {a['n_in_range_undrivable']} of those were dropped because no stimulus up to 12x the from-rest threshold drove 90% of 20 Hz pulses), following frequency {a['range_hz'][0]}-{a['range_hz'][1]} Hz, median {a['ff_median_accepted']:.1f} Hz; {a['n_tight_2_15']} in the tight 2-15 Hz cut.")
    A("")
    pc = R["positive_control"]
    A("## Positive control")
    A("")
    A("| Configuration | Sundt 2015 | Band (±25%) | Model | dt/2 check | Pass |")
    A("|---|---|---|---|---|---|")
    for n, lab in (("na_k", "Na + Kdr"), ("kcnq", "+ KCNQ/M"), ("sk", "+ Ca-dependent K")):
        r = pc["sundt"].get(n, {})
        r2 = pc["sundt"].get(n + "_dt0.0125", {})
        if r:
            A(f"| {lab} | {r['target_hz']} Hz | {r['band'][0]:.1f}-{r['band'][1]:.1f} | {r['ff']:.1f} Hz | {f2(r2.get('ff'))} Hz | {'yes' if r['pass'] else 'NO'} |")
    m = pc["sundt"].get("sk_removed_mutation")
    if m:
        A(f"| SK removed (mutation) | must leave 4.5-7.5 Hz | | {m['ff']:.1f} Hz | | {'control correctly fails' if m['pass'] else 'MUTATION DID NOT BREAK THE CONTROL'} |")
    c = pc["chao_qualitative"]
    A("")
    A("Chao 2020 qualitative control at regular 20 Hz, 1.5x:")
    A("")
    A(f"- (a) block defined within 20 s in {f2(c['frac_models_block_defined_within_20s'])} of models (need ≥0.5): {'pass' if c['a_pass'] else 'FAIL'}; median time-to-block {f2(c['time_to_block_ms_median'])} ms" + (" (vacuous: block is immediate)" if (c['time_to_block_ms_median'] or 1e9) < 2000 else ""))
    A(f"- (b) median F(late) - F(early) = {f2(c['F_late_minus_F_early_median'])} (need ≥0.20): {'pass' if c['b_pass'] else 'FAIL'}")
    ab = c["abeta_F_reg20_1_5"]
    A(f"- (c) Aβ F = {f2(ab['mean'])} [{f2(ab['lo'])}, {f2(ab['hi'])}] (need CI upper < 0.05): {'pass' if c['c_pass'] else 'FAIL'}")
    A("")
    A("## F by regular rate (probe-only baseline: " + f"mean {f2(R['F_probe_only_baseline']['mean'])}, max over models {f2(R['F_probe_only_baseline']['max'])})")
    A("")
    A("F is computed on *scored* probes only: probes that reach the pre-junction site and are not ambiguous with a stimulus spike (see `PREDICTION.md`, amendment E). `F_all` counts every arrived probe and treats any central crossing in the window as success, so it is a lower bound on F that includes stimulus spikes. Where the scored fraction is small, F is a statement about the gaps between stimulus volleys.")
    A("")
    A("| Rate | Amp | F mean | 95% CI | F_all mean | n models | mean probes (test / arrived / scored) | scored / test | median fraction of pulses evoking a spike |")
    A("|---|---|---|---|---|---|---|---|---|")
    for key, t in R["F_by_regular_rate"].items():
        rate, amp = key[3:].split("@")
        A(f"| {rate} Hz | {amp}x | {f2(t['F_mean'])} | [{f2(t['F_ci'][0])}, {f2(t['F_ci'][1])}] | {f2(t['F_all_mean'])} | {t['n']} | {t['n_test_mean']:.1f} / {t['n_arrived_mean']:.1f} / {t['n_scored_mean']:.1f} | {f2(t['scored_over_test'])} | {f2(t['evoked_fraction_median'])} |")
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
    A("## Diagnostics (not pre-registered thresholds)")
    A("")
    if d["n_with_d80_found"] == 0:
        A(f"- Drive-matched 80 Hz, post hoc: **unavailable.** The search tries multiples of the from-rest threshold up to 12x and accepts the first at which at least 90% of the late pulses of a 4 s regular 80 Hz train evoke a stem spike. It found none in {d['n_subsample']}/{d['n_subsample']} subsample models, so no 'drive-matched' run exists (the earlier 'n/a' was this, not a missing stage). Within a 12x amplitude range the stem cannot be driven at 80 Hz in these models; that is itself the lost-drive result, and is why P2 cannot be read as filtering.")
    else:
        A(f"- Drive-matched, post hoc: 80 Hz at 1.5x its own drive threshold (found in {d['n_with_d80_found']}/{d['n_subsample']} models) gives F = {f2(d['F_reg80_driven']['mean'])} [{f2(d['F_reg80_driven']['lo'])}, {f2(d['F_reg80_driven']['hi'])}] against regular 20 Hz F = {f2(d['F_reg20']['mean'])} on the same subsample.")
    t = R["test_trains_subsample"]
    A(f"- Pre-registered 10 Hz test train, subsample: F(none)={f2(t['none@probe10']['mean'])}, F(20 Hz)={f2(t['reg20@probe10']['mean'])}, F(80 Hz)={f2(t['reg80@probe10']['mean'])}, F(burst)={f2(t['burst@probe10']['mean'])}, F(Poisson)={f2(t['poisson@probe10']['mean'])}, F(jitter)={f2(t['jitter@probe10']['mean'])}; F(80)-F(20) = {f2(t['reg80_minus_reg20_probe10']['mean'])} [{f2(t['reg80_minus_reg20_probe10']['lo'])}, {f2(t['reg80_minus_reg20_probe10']['hi'])}].")
    A(f"- 5 Hz test train: F(none)={f2(t['none@probe5']['mean'])}, F(20 Hz)={f2(t['reg20@probe5']['mean'])}, F(80 Hz)={f2(t['reg80@probe5']['mean'])}.")
    cv = R["convergence"]
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


def write_plots(R, models, stoch, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    for i, amp in enumerate(AMPS):
        xs = list(FREQS)
        ys = [R["F_by_regular_rate"][f"reg{f}@{amp}"]["F_mean"] for f in xs]
        lo = [R["F_by_regular_rate"][f"reg{f}@{amp}"]["F_ci"][0] for f in xs]
        hi = [R["F_by_regular_rate"][f"reg{f}@{amp}"]["F_ci"][1] for f in xs]
        ax[i].errorbar(xs, ys, yerr=[np.array(ys) - np.array(lo), np.array(hi) - np.array(ys)], marker="o", capsize=3)
        ax[i].set_ylim(0, 1.05)
        ax[i].set_xlabel("regular stimulation rate (Hz)")
        ax[i].set_ylabel("filtering index F (2 Hz probe)")
        ax[i].set_title(f"{amp}x drive threshold")
    fig.suptitle("S-1: F against rate (mean and bootstrap 95% CI across models)")
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
        ax[i].axhline(0.10, ls="--", c="k", lw=0.8)
        ax[i].axhline(-0.10, ls="--", c="k", lw=0.8)
        ax[i].axhline(0.20, ls=":", c="r", lw=0.8)
        ax[i].set_xticks(xs)
        ax[i].set_xticklabels([c["pattern"] for c in cells])
        ax[i].set_ylabel("F(pattern) - F(regular 20 Hz)")
        ax[i].set_title(f"{amp}x drive threshold")
    fig.suptitle("S-1 P1: matched-rate patterns against regular 20 Hz (dashed: ±10 pts; dotted: refutation bar)")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "P1-pattern-minus-rate.png"), dpi=110)
    plt.close(fig)
