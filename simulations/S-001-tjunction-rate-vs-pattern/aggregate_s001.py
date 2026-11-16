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
             verdict_module=("simulations/verdict.py" if os.path.exists(SHARED_VERDICT) else "local rule (PREDICTION.md)"))
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
            tab[f"reg{fr}@{amp}"] = dict(F_mean=b["mean"], F_ci=[b["lo"], b["hi"]], n=b["n"],
                                         evoked_fraction_median=float(np.median(ev)) if ev else None)
    base = [fval(m["runs"].get("none")) for m in models.values()]
    R["F_by_regular_rate"] = tab
    R["F_probe_only_baseline"] = boot_mean(base)

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
    dd = [fval(t["runs"].get("reg80@drive80")) - fval(models[k]["runs"].get("reg80@1.5")) for k, t in tests.items() if k in models]
    R["drive_matched_diagnostic"] = dict(
        note="post hoc: reg80 at 1.5x its own steady-state drive threshold, 2 Hz probes",
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
            for pat in ("reg20", "reg80", "burst"):
                a, b = fval(d[0.025]["runs"][pat]), fval(d[0.0125]["runs"][pat])
                if np.isfinite(a) and np.isfinite(b):
                    diffs.append(abs(a - b))
    R["convergence"] = dict(n_models=len(cv), median_abs_dF=float(np.median(diffs)) if diffs else None,
                            max_abs_dF=float(np.max(diffs)) if diffs else None,
                            pass_=bool(diffs and np.median(diffs) <= 0.02))

    with open(os.path.join(out, "results.json"), "w") as f:
        json.dump(R, f, indent=1, default=lambda o: None if (isinstance(o, float) and not np.isfinite(o)) else float(o) if isinstance(o, np.floating) else bool(o) if isinstance(o, np.bool_) else int(o))
    write_md(R, out, pilot)
    try:
        write_plots(R, models, stoch, out)
    except Exception as e:  # plotting must never lose the numbers
        print("plot failed:", e)


def f2(x):
    return "n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:.3f}"


def write_md(R, out, pilot):
    L = []
    A = L.append
    A("# S-1 results: DRG T-junction, rate versus pattern" + (" (PILOT, not a result)" if pilot else ""))
    A("")
    A("**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.")
    A("")
    A(f"Verdict logic: {R['verdict_module']}. Pre-registration: `PREDICTION.md` (commit #1); amendments are listed in `PREDICTION.md` under 'Amendments made in the results commit'.")
    A("")
    v = R["verdicts"]
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
    A(f"- (a) block defined within 20 s in {f2(c['frac_models_block_defined_within_20s'])} of models (need ≥0.5): {'pass' if c['a_pass'] else 'FAIL'}; median time-to-block {f2(c['time_to_block_ms_median'])} ms")
    A(f"- (b) median F(late) - F(early) = {f2(c['F_late_minus_F_early_median'])} (need ≥0.20): {'pass' if c['b_pass'] else 'FAIL'}")
    ab = c["abeta_F_reg20_1_5"]
    A(f"- (c) Aβ F = {f2(ab['mean'])} [{f2(ab['lo'])}, {f2(ab['hi'])}] (need CI upper < 0.05): {'pass' if c['c_pass'] else 'FAIL'}")
    A("")
    A("## F by regular rate (probe-only baseline: " + f"{f2(R['F_probe_only_baseline']['mean'])})")
    A("")
    A("| Rate | Amp | F mean | 95% CI | n | median fraction of pulses evoking a spike |")
    A("|---|---|---|---|---|---|")
    for key, t in R["F_by_regular_rate"].items():
        rate, amp = key[3:].split("@")
        A(f"| {rate} Hz | {amp}x | {f2(t['F_mean'])} | [{f2(t['F_ci'][0])}, {f2(t['F_ci'][1])}] | {t['n']} | {f2(t['evoked_fraction_median'])} |")
    A("")
    A("## P1: pattern versus rate (difference from regular 20 Hz, matched pulse count)")
    A("")
    A("| Pattern | Amp | n | within 10 pts | Wilson 95% | mean diff | 95% CI |")
    A("|---|---|---|---|---|---|---|")
    for c in R["P1"]["cells"]:
        A(f"| {c['pattern']} | {c['amp']}x | {c['n']} | {f2(c['prop_within_10pts'])} | [{f2(c['wilson'][0])}, {f2(c['wilson'][1])}] | {f2(c['mean_diff'])} | [{f2(c['diff_ci'][0])}, {f2(c['diff_ci'][1])}] |")
    A("")
    A(f"P1 if the control passes: **{R['P1']['verdict_if_control_passes']}**.")
    A("")
    A("## P2: F(80 Hz) versus F(20 Hz)")
    A("")
    A("| Amp | n | F20 | F80 | F80≥F20 (1-pt tol) | Wilson 95% | literal | models with ≥20% relative fall | Wilson 95% | evoked frac 20 / 80 Hz |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for c in R["P2"]["cells"]:
        if c.get("n"):
            A(f"| {c['amp']}x | {c['n']} | {f2(c['mean_F20'])} | {f2(c['mean_F80'])} | {f2(c['prop_f80_ge_f20_tol'])} | [{f2(c['wilson'][0])}, {f2(c['wilson'][1])}] | {f2(c['prop_literal'])} | {f2(c['prop_fall_ge_20pct'])} (of {c['n_with_F20_ge_0_05']}) | [{f2(c['wilson_fall'][0])}, {f2(c['wilson_fall'][1])}] | {f2(c['evoked_fraction_median_20Hz'])} / {f2(c['evoked_fraction_median_80Hz'])} |")
    A("")
    A(f"P2 if the control passes: **{R['P2']['verdict_if_control_passes']}**.")
    A("")
    d = R["drive_matched_diagnostic"]
    A("## Diagnostics (not pre-registered thresholds)")
    A("")
    A(f"- Drive-matched, post hoc: regular 80 Hz at 1.5x its own steady-state drive threshold gives F = {f2(d['F_reg80_driven']['mean'])} [{f2(d['F_reg80_driven']['lo'])}, {f2(d['F_reg80_driven']['hi'])}] against regular 20 Hz F = {f2(d['F_reg20']['mean'])} on the same subsample; the 80 Hz drive amplitude is {f2(d['d80_over_d20']['mean'])}x the 20 Hz one.")
    t = R["test_trains_subsample"]
    A(f"- Pre-registered 10 Hz test train, subsample: F(none)={f2(t['none@probe10']['mean'])}, F(20 Hz)={f2(t['reg20@probe10']['mean'])}, F(80 Hz)={f2(t['reg80@probe10']['mean'])}, F(burst)={f2(t['burst@probe10']['mean'])}, F(Poisson)={f2(t['poisson@probe10']['mean'])}, F(jitter)={f2(t['jitter@probe10']['mean'])}; F(80)-F(20) = {f2(t['reg80_minus_reg20_probe10']['mean'])} [{f2(t['reg80_minus_reg20_probe10']['lo'])}, {f2(t['reg80_minus_reg20_probe10']['hi'])}].")
    A(f"- 5 Hz test train: F(none)={f2(t['none@probe5']['mean'])}, F(20 Hz)={f2(t['reg20@probe5']['mean'])}, F(80 Hz)={f2(t['reg80@probe5']['mean'])}.")
    cv = R["convergence"]
    A(f"- dt-halving (0.025 vs 0.0125 ms), {cv['n_models']} models: median |dF| = {f2(cv['median_abs_dF'])}, max {f2(cv['max_abs_dF'])}; {'pass' if cv['pass_'] else 'FAIL, INCONCLUSIVE'}.")
    A("")
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
