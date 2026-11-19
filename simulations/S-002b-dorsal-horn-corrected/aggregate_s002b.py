#!/usr/bin/env python3
"""S-2b aggregator: results.json, results.md, PNGs, visual-traces summary, per-model zip.

All prose in results.md is generated from the data files; every number in a sentence comes from a computed
value.  Verdict words are printed only when the gates of PREDICTION.md hold; otherwise the table says
"NO VERDICT" and prints a plainly labelled conditional reading.

    python aggregate_s002b.py [outdir]        (default results/main)
"""

import itertools
import json
import os
import shutil
import sys
import zipfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
if "--pilot" in sys.argv:
    os.environ["S2B_PILOT"] = "1"

import s2b_protocol as P  # noqa: E402

THR = P.RED_THRESHOLD
MAX_ENUM = 14


def load(path):
    with open(path) as fh:
        return json.load(fh)


def exists(*parts):
    return os.path.exists(os.path.join(*parts))


# --- pure verdict logic (tested in test_s2b_protocol.py) --------------------------------------------

def klass(lo, hi, thr=THR):
    """R: lower bound >= thr; N: upper bound < thr; S: spans thr; '-': undefined."""
    if lo is None or hi is None or not np.isfinite(lo) or not np.isfinite(hi):
        return "-"
    if lo >= thr:
        return "R"
    if hi < thr:
        return "N"
    return "S"


def p1_refuted(cs):
    d = [c for c in cs if c != "-"]
    return len(d) >= 3 and all(c == "R" for c in d)


def p1_supported(cs, cc):
    n = len(cs)
    for j in range(n):
        if cs[j] == "-":
            continue
        before = [cs[i] for i in range(j) if cs[i] != "-"]
        after = [cs[i] for i in range(j, n) if cs[i] != "-"]
        if "R" in before and all(c == "N" for c in after) and after and \
                all(cc[i] == "R" for i in range(j, n)):
            return True
    return False


def _enumerate(cls_lists, decide):
    """Is there an assignment of the S cells to R/N under which `decide` returns a decisive word?"""
    cells = [(k, i) for k, cl in enumerate(cls_lists) for i, c in enumerate(cl) if c == "S"]
    if len(cells) > MAX_ENUM:
        return True
    for assign in itertools.product("RN", repeat=len(cells)):
        cl = [list(c) for c in cls_lists]
        for (k, i), a in zip(cells, assign):
            cl[k][i] = a
        if decide(*cl) in ("SUPPORTED", "REFUTED"):
            return True
    return False


def decide_p1(cs, cc):
    def d(cs_, cc_):
        if p1_refuted(cs_):
            return "REFUTED"
        if p1_supported(cs_, cc_):
            return "SUPPORTED"
        return "NOT SUPPORTED, NOT REFUTED"
    v = d(cs, cc)
    if v != "NOT SUPPORTED, NOT REFUTED":
        return v
    return "INCONCLUSIVE" if _enumerate([cs, cc], d) else v


def decide_p2(ch):
    """`ch`: classes of red_Ch at the shifts at and beyond the population median onset (E defined)."""
    d_ = [c for c in ch if c != "-"]
    if len(d_) < 2:
        return "INCONCLUSIVE"

    def d(cl):
        cl = [c for c in cl if c != "-"]
        if all(c == "N" for c in cl):
            return "SUPPORTED"
        if all(c == "R" for c in cl):
            return "REFUTED"
        return "NOT SUPPORTED, NOT REFUTED"
    v = d(ch)
    if v != "NOT SUPPORTED, NOT REFUTED":
        return v
    return "INCONCLUSIVE" if _enumerate([ch], lambda c: d(c)) else v


def decide_p0(lo, hi, n, limit=P.P0_ONSET_LIMIT):
    if n < P.N_ENSEMBLE:
        return "INCONCLUSIVE"
    if hi <= limit:
        return "SUPPORTED"
    if lo > limit:
        return "REFUTED"
    return "INCONCLUSIVE"


def decide_p3(prog, others, n_floor=P.N_SUBSAMPLE):
    """`prog`, `others['H'|'D1'|'D2']`: (k, n) counts of networks showing the full signature."""
    pw = P.wilson(*prog)
    ow = {k: P.wilson(*v) for k, v in others.items()}
    if prog[1] < n_floor or any(v[1] < n_floor for v in others.values()):
        return "INCONCLUSIVE"
    if pw[1] < 0.5:
        return "REFUTED"
    if pw[0] > 0.5 and all(w[1] < 0.5 for w in ow.values()):
        return "SUPPORTED"
    spans = [pw] + list(ow.values())
    if any(w[0] <= 0.5 <= w[1] for w in spans):
        return "INCONCLUSIVE"
    return "NOT SUPPORTED, NOT REFUTED"


# --- data loading ----------------------------------------------------------------------------------------

def collect(out):
    acc = load(os.path.join(out, "accepted.json")) if exists(out, "accepted.json") else None
    nets = []
    if acc:
        for i in acc["accepted"]:
            p = os.path.join(out, "model", f"{i}.json")
            if os.path.exists(p):
                nets.append(load(p))
    return acc, nets


def mean_by_shift(nets, cond):
    return np.array([[np.mean(n["R"][cond][str(s)]) for s in P.SHIFTS] for n in nets])


def fmt(x, nd=2):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "n/a"
    return f"{x:.{nd}f}"


def ci_str(pt, lo, hi, nd=2):
    return f"{fmt(pt, nd)} [{fmt(lo, nd)}, {fmt(hi, nd)}]"


# --- analysis ----------------------------------------------------------------------------------------------

def analyse(out):
    res = dict(protocol=dict(t_run_ms=P.T_RUN, window_ms=[P.T_SCORE0, P.T_SCORE1], shifts=list(P.SHIFTS),
                             seeds=list(P.SEEDS), touch_hz=P.TOUCH_HZ, scs_primary_hz=P.SCS_PRIMARY_HZ,
                             rc_grid=list(P.RC_GRID)))
    gates = {}
    for g in ("g1", "g4", "g5", "g6"):
        gates[g] = load(os.path.join(out, f"gate_{g}.json"))["passed"] if exists(out, f"gate_{g}.json") else None
    acc, nets = collect(out)
    gates["g2"] = bool(acc and acc.get("ok") and len(nets) >= P.N_ENSEMBLE)
    res["accepted"] = acc
    res["n_networks_measured"] = len(nets)
    # candidate 0
    c0 = {}
    for dt in (P.DT_MAIN, P.DT_PUB):
        if exists(out, f"cand0-dt{dt}.json"):
            c0[str(dt)] = load(os.path.join(out, f"cand0-dt{dt}.json"))
    res["candidate0"] = c0
    oracle_path = os.path.join(HERE, "results", "oracle", "original-hoc-crosscheck.json")
    res["oracle"] = load(oracle_path) if os.path.exists(oracle_path) else None
    # convergence
    conv = [load(os.path.join(out, "converge", f)) for f in sorted(os.listdir(os.path.join(out, "converge")))] \
        if exists(out, "converge") else []
    res["convergence"] = convergence(conv)
    gates["g3"] = res["convergence"]["passed"] if res["convergence"] else None
    res["gates"] = gates
    res["gates_for_p0_p2"] = all(gates[g] is True for g in ("g1", "g2", "g3", "g4", "g6"))
    res["gates_for_p1_p3"] = res["gates_for_p0_p2"] and gates["g5"] is True
    if len(nets) == 0:
        return res
    n = len(nets)
    idx = P.boot_indices(n, P.BOOT_N, seed=1)
    M = {c: mean_by_shift(nets, c) for c in P.MAIN_CONDITIONS}
    sh = list(P.SHIFTS)
    # outputs vs shift
    res["mean_rates"] = {c: M[c].mean(axis=0).tolist() for c in M}
    # P0
    onsets = [P.onset_shift(list(M["T"][i]), P.SHIFTS) for i in range(n)]
    ov = [P.ONSET_NONE_VALUE if o is None else float(o) for o in onsets]
    med, lo, hi = P.median_ci(ov, idx)
    res["P0"] = dict(median=med, ci=[lo, hi], share_with_onset=float(np.mean([o is not None for o in onsets])),
                     onsets=ov, verdict_if_gates=decide_p0(lo, hi, n))
    # P1: red_S, red_C
    red_s, red_c, red_ch = [], [], []
    for j, s in enumerate(sh):
        if M["T"][:, j].mean() >= P.MIN_DEFINED_RATE:
            red_s.append(P.ratio_reduction_ci(M["TS"][:, j], M["T"][:, j], idx))
        else:
            red_s.append((float("nan"),) * 3)
        red_c.append(P.ratio_reduction_ci(M["Ch"][:, j], M["C1"][:, j], idx) if M["C1"][:, j].mean() > 0
                     else (float("nan"),) * 3)
        E = M["TC"][:, j] - M["C1"][:, j]
        Eh = M["TCh"][:, j] - M["Ch"][:, j]
        red_ch.append(P.ratio_reduction_ci(Eh, E, idx) if E.mean() >= P.MIN_DEFINED_RATE else (float("nan"),) * 3)
    cs = [klass(a[1], a[2]) for a in red_s]
    cc = [klass(a[1], a[2]) for a in red_c]
    res["P1"] = dict(red_S=[list(a) for a in red_s], red_C=[list(a) for a in red_c], class_S=cs, class_C=cc,
                     verdict_if_gates=decide_p1(cs, cc) if n >= P.N_ENSEMBLE else "INCONCLUSIVE")
    # P2
    first = [j for j, s in enumerate(sh) if s >= med]
    ch = [klass(red_ch[j][1], red_ch[j][2]) for j in first]
    res["P2"] = dict(red_Ch=[list(a) for a in red_ch], shifts_considered=[sh[j] for j in first], class_Ch=ch,
                     verdict_if_gates=decide_p2(ch) if n >= P.N_ENSEMBLE else "INCONCLUSIVE")
    # readings: A-beta / A-delta decomposition
    res["reading_A"] = reading_a(out, nets, acc)
    # validation F
    res["reading_F"] = reading_f(out, acc)
    # P3
    res["P3"] = p3(out, nets, acc, M)
    return res


def convergence(conv):
    if not conv:
        return None
    cells, flips = [], 0
    ncls = 0
    for r in conv:
        R = r["R"]
        for c in ("C1", "T", "TS"):
            for s in (0, 20):
                cells.append(abs(R[f"{c}|{s}|{P.DT_MAIN}"] - R[f"{c}|{s}|{P.DT_PUB}"]))

        def cl(dt):
            t0, t20 = R[f"T|0|{dt}"], R[f"T|20|{dt}"]
            return (t20 >= t0 + P.ONSET_RISE, R[f"TS|0|{dt}"] < 0.8 * t0, R[f"TS|20|{dt}"] < 0.8 * t20)
        a, b = cl(P.DT_MAIN), cl(P.DT_PUB)
        flips += sum(x != y for x, y in zip(a, b))
        ncls += 3
    med = float(np.median(cells))
    share = flips / ncls if ncls else float("nan")
    return dict(n_networks=len(conv), median_abs_dR=med, flips=flips, classifications=ncls, flip_share=share,
                passed=bool(len(conv) >= P.N_CONVERGE and med <= 1.0 and share <= 0.10))


def reading_a(out, nets, acc):
    ratios = {"C_abeta": [], "C_adelta": [], "C_all_A": []}
    for i in (acc["accepted"] if acc else []):
        p = os.path.join(out, f"cand0-dt{P.DT_MAIN}.json") if i == 0 else os.path.join(out, "cand", f"{i}.json")
        if not os.path.exists(p):
            continue
        a = load(p).get("A")
        if a and a.get("C_only"):
            ratios["C_abeta"].append(a["C_abeta"] / a["C_only"])
    for n in nets:
        base = None
        p = os.path.join(out, f"cand0-dt{P.DT_MAIN}.json") if n["idx"] == 0 else os.path.join(out, "cand", f"{n['idx']}.json")
        if os.path.exists(p):
            a = load(p).get("A")
            base = a["C_only"] if a else None
        if base:
            ratios["C_adelta"].append(float(np.mean(n["A"]["C_adelta"])) / base)
            ratios["C_all_A"].append(float(np.mean(n["A"]["C_all_A"])) / base)
    r = {}
    for k, v in ratios.items():
        if v:
            r[k] = dict(n=len(v), median=float(np.median(v)), q25=float(np.percentile(v, 25)), q75=float(np.percentile(v, 75)))
    if ratios["C_adelta"]:
        k = int(sum(x > 1.0 for x in ratios["C_adelta"]))
        r["share_adelta_excites"] = dict(k=k, n=len(ratios["C_adelta"]), wilson=list(P.wilson(k, len(ratios["C_adelta"]))))
    return r


def reading_f(out, acc):
    recs = []
    for i in (acc["accepted"] if acc else []):
        p = os.path.join(out, "valid", f"{i}.json")
        if os.path.exists(p):
            recs.append(load(p)["F"])
    if not recs:
        return None
    ev = [r for r in recs if r.get("evaluable")]
    ok = [r for r in recs if r.get("ok")]
    rho = {}
    for f in P.CONTROL_FREQS:
        v = [r["rho"][str(f)] for r in ev if str(f) in r["rho"]]
        if v:
            rho[str(f)] = dict(median=float(np.median(v)), q25=float(np.percentile(v, 25)), q75=float(np.percentile(v, 75)))
    return dict(n=len(recs), n_evaluable=len(ev), n_pass=len(ok), wilson_pass_of_all=list(P.wilson(len(ok), len(recs))),
                wilson_pass_of_evaluable=list(P.wilson(len(ok), len(ev))) if ev else None, rho=rho)


def p3(out, nets, acc, M):
    sw = {}
    for i in (acc["accepted"][:P.N_SUBSAMPLE] if acc else []):
        pth = os.path.join(out, "sweep", f"{i}.json")
        if os.path.exists(pth):
            sw[i] = load(pth)["S"]
    if not sw:
        return None
    byid = {n["idx"]: j for j, n in enumerate(nets)}
    sh = list(P.SHIFTS)
    fr = P.SWEEP_FREQS
    prim = P.SCS_PRIMARY_HZ

    def col(cond, s):
        return M[cond][:, sh.index(s)]

    def mean(S, key):
        return float(np.mean(S[key]))

    def fstar(S, v, s):
        vals = [mean(S, f"TCS|{v}|{s}|{f}") for f in fr]
        return int(fr[int(np.argmin(vals))])

    def state(S, j, v, s):
        """u, mean relief, f*, evaluable for variant v at shift s (uses main-grid R_T, R_C1, R_TS)."""
        rt, rc = col("T", s)[j], col("C1", s)[j]
        if v == "norm":
            ts, cs_ = col("TS", s)[j], mean(S, f"CS|norm|{s}|{prim}")
        else:
            ts, cs_ = mean(S, f"TS|{v}|{s}|{prim}"), mean(S, f"CS|{v}|{s}|{prim}")
        ev = rt >= 1.0 and rc >= 1.0
        if not ev:
            return dict(evaluable=False, fstar=fstar(S, v, s))
        rl_t, rl_c = 1 - ts / rt, 1 - cs_ / rc
        return dict(evaluable=True, u=rl_t - rl_c, mean_relief=(rl_t + rl_c) / 2, relief_T=rl_t, relief_C=rl_c,
                    fstar=fstar(S, v, s))

    counts = {k: [0, 0] for k in ("prog", "H", "D1", "D2")}
    detail = []
    uniform_H = [0, 0]
    for i, S in sw.items():
        j = byid.get(i)
        if j is None:
            continue
        ref = state(S, j, "norm", P.DELTA_REF)
        cases = {"prog": state(S, j, "norm", P.DELTA_PROG), "H": state(S, j, "H", P.DELTA_REF),
                 "D1": state(S, j, "D1", P.DELTA_REF), "D2": state(S, j, "D2", P.DELTA_REF)}
        row = dict(idx=i, ref=ref)
        for k, st in cases.items():
            row[k] = st
            if ref["evaluable"] and st["evaluable"]:
                counts[k][1] += 1
                sel = st["u"] <= ref["u"] - 0.20
                mv = st["fstar"] != ref["fstar"]
                counts[k][0] += int(sel and mv)
                row[k]["selective_loss"], row[k]["optimum_moves"] = bool(sel), bool(mv)
                if k == "H":
                    uniform_H[1] += 1
                    uniform_H[0] += int(abs(st["u"] - ref["u"]) <= 0.10 and not mv)
        detail.append(row)
    others = {k: tuple(counts[k]) for k in ("H", "D1", "D2")}
    parts = {k: dict(k=counts[k][0], n=counts[k][1], wilson=list(P.wilson(*counts[k]))) for k in counts}
    # share showing each half separately (readings)
    halves = {}
    for k in counts:
        sel = [r[k].get("selective_loss") for r in detail if "selective_loss" in r[k]]
        mv = [r[k].get("optimum_moves") for r in detail if "optimum_moves" in r[k]]
        halves[k] = dict(selective_loss=[int(sum(sel)), len(sel)], optimum_moves=[int(sum(mv)), len(mv)])
    return dict(n_sweep=len(sw), counts=parts, halves=halves, uniform_H=uniform_H, detail=detail,
                verdict_if_gates=decide_p3(tuple(counts["prog"]), others))


# --- report -----------------------------------------------------------------------------------------------------

def word(res, which, gated_ok):
    v = res[which]["verdict_if_gates"]
    if gated_ok:
        return f"**{v}**"
    return "NO VERDICT (the conditional reading is under \"Conditional readings, not verdicts\" below)"


def gate_line(res):
    g = res["gates"]
    lab = {"g1": "G1 calibration at candidate 0", "g2": "G2 ensemble of 200 accepted", "g3": "G3 dt-halving convergence",
           "g4": "G4 wiring and protocol tests", "g5": "G5 held-out frequency feature at candidate 0 (gates P1, P3)",
           "g6": "G6 oracle equivalence"}
    rows = ["| Gate | Result |", "|---|---|"]
    for k in ("g6", "g1", "g2", "g3", "g4", "g5"):
        v = g.get(k)
        rows.append(f"| {lab[k]} | {'passed' if v is True else ('FAILED' if v is False else 'not evaluated')} |")
    return "\n".join(rows)


def write_report(out, res):
    L = []
    A = L.append
    A("These results are not stimulation settings.")
    A("")
    A("# S-2b results: corrected dorsal-horn run")
    A("")
    A("Every number below is generated from the data files in this directory. Model units: E_anion shifts are in "
      "model millivolts, frequencies are those of a synthetic pulse train in a four-cell model, rates are model "
      "WDR spikes per second. Pre-registration: `PREDICTION.md` (commit #1 of the branch).")
    A("")
    A("## Gates")
    A("")
    A(gate_line(res))
    A("")
    pa = "all of G1-G4 and G6 hold" if res["gates_for_p0_p2"] else "at least one of G1-G4, G6 does not hold"
    pb = "G5 holds as well" if res["gates_for_p1_p3"] else "G5 does not hold or an earlier gate failed"
    A(f"For P0 and P2: {pa}. For P1 and P3: {pb}.")
    A("")
    # control
    A("## The control")
    A("")
    c0 = res.get("candidate0", {})
    A("### Candidate 0 (the unmodified shipped model)")
    A("")
    A("| dt (ms) | W early / late (spikes per stimulus) | W | C only | C+Abeta | C+Adelta | C+all A | ratio Abeta | ratio Adelta | "
      "r_C (Hz per fibre) | C-only rate at r_C (Hz) | A-beta | F |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for dt, r in sorted(c0.items(), key=lambda kv: -float(kv[0])):
        a = r.get("A", {})
        A(f"| {dt} | {fmt(r['W']['early'], 1)} / {fmt(r['W']['late'], 1)} | {'pass' if r['W']['ok'] else 'fail'} | "
          f"{fmt(a.get('C_only'), 1)} | {fmt(a.get('C_abeta'), 1)} | {fmt(a.get('C_adelta'), 1)} | {fmt(a.get('C_all_A'), 1)} | "
          f"{fmt(a.get('ratio_abeta'))} | {fmt(a.get('ratio_adelta'))} | {r.get('rC')} | {fmt(r.get('rC_rate'))} | "
          f"{'pass' if a.get('ok') else 'fail'} | {('pass' if r['F']['ok'] else 'fail') if 'F' in r else 'n/a'} |")
    A("")
    A("Spikes per cycle (A control) in the first 10 cycles of the shipped input.")
    A("")
    if res.get("oracle"):
        o = res["oracle"]
        A("### Port against the original hoc network (oracle)")
        A("")
        A("The original ModelDB 168414 hoc network was executed by NEURON (`crosscheck_original_hoc.py`, "
          f"NEURON {o.get('neuron_version')}); the port is `dh_model.py`. Spikes per cycle, mean of 10 cycles.")
        A("")
        A("| dt (ms) | condition | original (hoc) | port (candidate 0) | reviewer's table |")
        A("|---|---|---|---|---|")
        for dt in ("0.025", "0.0125"):
            for cnd in ("C_only", "C_abeta", "C_adelta", "C_all_A"):
                orig = o["runs"].get(dt, {}).get(cnd, {}).get("mean")
                port = c0.get(dt, {}).get("A", {}).get(cnd)
                rev = o["reviewer_table_dt_0_025"].get(cnd) if dt == "0.025" else None
                A(f"| {dt} | {cnd} | {fmt(orig, 1)} | {fmt(port, 1)} | {fmt(rev, 1) if rev is not None else ''} |")
        A("")
        A(f"All {len(o['mechanisms'])} mechanism files are identical to the originals after CRLF normalisation: "
          f"{o['mechanisms_all_identical_after_crlf_normalisation']}. Archive sha256 matches PROVENANCE.md: "
          f"{o['archive']['sha256_matches']}.")
        A("")
    acc = res.get("accepted")
    if acc:
        st = acc.get("rejected_at_stage", {})
        A("### Ensemble funnel")
        A("")
        A(f"Candidates considered (index order): {acc['considered']}; accepted: {len(acc['accepted'])} of a target of "
          f"{acc['target']}; rejected at W: {st.get('W', 0)}; rejected at A-beta: {st.get('A', 0)}; rejected at the "
          f"drive match: {st.get('rC', 0)} (candidate 0 is counted among the accepted and not among these).")
        A("")
    if "P0" not in res:
        A("## Verdicts")
        A("")
        A("No ensemble was measured. NO VERDICT on P0 to P3; the control records above are the result.")
        return "\n".join(L) + "\n"
    ok02, ok13 = res["gates_for_p0_p2"], res["gates_for_p1_p3"]
    n = res["n_networks_measured"]
    A("## Verdicts")
    A("")
    A(f"Networks measured: {n}. Intervals are bootstrap 95% CIs over networks ({P.BOOT_N} resamples), or Wilson for "
      "proportions.")
    A("")
    p0 = res["P0"]
    A("### P0 (Q1): onset of touch-evoked projection-neuron output")
    A("")
    A(f"Median onset shift {fmt(p0['median'], 1)} mV, CI [{fmt(p0['ci'][0], 1)}, {fmt(p0['ci'][1], 1)}]; "
      f"{fmt(100 * p0['share_with_onset'], 0)}% of networks have an onset on the grid (onset = first shift at which "
      f"R_T rises {P.ONSET_RISE} Hz above its value at 0). Threshold: median at most {P.P0_ONSET_LIMIT} mV. "
      f"Registered rule: SUPPORTED iff the CI upper bound is at most {P.P0_ONSET_LIMIT}; REFUTED iff the CI lower bound "
      f"is above {P.P0_ONSET_LIMIT}; otherwise INCONCLUSIVE. The CI lower bound is {fmt(p0['ci'][0], 1)} and the threshold is "
      f"{fmt(P.P0_ONSET_LIMIT, 1)}"
      + (", so the lower bound equals the threshold" if abs(p0['ci'][0] - P.P0_ONSET_LIMIT) < 1e-9 else "") +
      f". Resolution is limited by the shift grid, {', '.join(str(x) for x in P.SHIFTS)} mV: onsets and the "
      f"CI ends can only fall on grid values, and the median of an even-sized sample can fall between two of them. "
      f"Verdict: {word(res, 'P0', ok02)}.")
    A("")
    p1 = res["P1"]
    A(f"### P1 (Q2a): stimulation on the surround input at {P.SCS_PRIMARY_HZ} Hz, touch-evoked output")
    A("")
    A("| shift (mV) | mean R_T (Hz) | mean R_TS (Hz) | red_S [CI] | class | red_C [CI] | class |")
    A("|---|---|---|---|---|---|---|")
    mr = res["mean_rates"]
    for j, s in enumerate(P.SHIFTS):
        A(f"| {s} | {fmt(mr['T'][j])} | {fmt(mr['TS'][j])} | {ci_str(*p1['red_S'][j])} | {p1['class_S'][j]} | "
          f"{ci_str(*p1['red_C'][j])} | {p1['class_C'][j]} |")
    A("")
    A("red_S = 1 - mean(R_TS)/mean(R_T); red_C = 1 - mean(R_Ch)/mean(R_C1). Classes: R lower bound >= "
      f"{THR}; N upper bound < {THR}; S spans {THR}; - undefined. Verdict: {word(res, 'P1', ok13)}.")
    A("")
    p2 = res["P2"]
    A("### P2 (Q2b): reduced C input, touch-evoked output on background")
    A("")
    A("| shift (mV) | mean R_C1 | mean R_TC | mean E | red_Ch [CI] | class |")
    A("|---|---|---|---|---|---|")
    for j, s in enumerate(P.SHIFTS):
        e = mr["TC"][j] - mr["C1"][j]
        A(f"| {s} | {fmt(mr['C1'][j])} | {fmt(mr['TC'][j])} | {fmt(e)} | {ci_str(*p2['red_Ch'][j])} | "
          f"{klass(p2['red_Ch'][j][1], p2['red_Ch'][j][2])} |")
    A("")
    A(f"Shifts considered (at or above the median onset {fmt(p0['median'], 1)} mV, E defined): "
      f"{p2['shifts_considered']}. Classes there: {p2['class_Ch']}. Registered rule: SUPPORTED iff red_Ch is class N "
      f"(upper bound below {THR}) at every considered shift, with at least two such shifts; REFUTED iff it is class R at "
      f"every one; INCONCLUSIVE if re-classing spanning cells could decide it; otherwise NOT SUPPORTED, NOT REFUTED. "
      f"Verdict: {word(res, 'P2', ok02)}.")
    A("")
    if ok02 and p2["verdict_if_gates"] == "SUPPORTED":
        A(f"In plain terms: at the shifts {p2['shifts_considered']} mV, where touch drives the projection neuron, halving the "
          "C input does not reduce the touch-evoked excess (E, the rate with touch and C minus the rate with C alone); "
          "red_Ch is about "
          + ", ".join(fmt(p2['red_Ch'][list(P.SHIFTS).index(x)][0]) for x in p2['shifts_considered']) +
          " there. This is a property of this four-cell model, not a finding about people. It says nothing about whether "
          "C input matters for touch-evoked pain in a patient, and it is read at shifts where the touch-evoked "
          "rate is already far above the C-driven rate.")
    A("")
    p3r = res.get("P3")
    A("### P3 (Q3): which observable change separates the three causes")
    A("")
    if p3r is None:
        A("The sweep subsample was not measured. NO VERDICT.")
    else:
        A(f"Sweep subsample: {p3r['n_sweep']} networks. Networks showing the full signature (selective loss and a "
          "moved optimum) among the evaluable ones:")
        A("")
        A("| change | full signature k/n | Wilson 95% | selective loss k/n | optimum moves k/n |")
        A("|---|---|---|---|---|")
        names = {"prog": f"progressive disinhibition ({P.DELTA_REF} to {P.DELTA_PROG} mV)", "H": "habituation (H)",
                 "D1": "lead drift D1", "D2": "lead drift D2"}
        for k in ("prog", "H", "D1", "D2"):
            c = p3r["counts"][k]
            h = p3r["halves"][k]
            A(f"| {names[k]} | {c['k']}/{c['n']} | [{fmt(c['wilson'][0])}, {fmt(c['wilson'][1])}] | "
              f"{h['selective_loss'][0]}/{h['selective_loss'][1]} | {h['optimum_moves'][0]}/{h['optimum_moves'][1]} |")
        A("")
        A("The rows are listed in a fixed order and no ordering of the changes is a finding: without a gated verdict "
          "the proportions are a descriptive table of a subsample.")
        A("")
        A(f"Uniform-loss reading for H (|change in u| <= 0.10 and the optimum unchanged): {p3r['uniform_H'][0]} of "
          f"{p3r['uniform_H'][1]} evaluable networks. Verdict: {word(res, 'P3', ok13)}.")
        A("")
        if ok13 and p3r["verdict_if_gates"] == "SUPPORTED":
            A("Candidate observation for a treating team to consider, a hypothesis and never advice: if, over time, "
              "relief of touch-evoked pain falls before relief of background pain does, and the stimulation frequency at "
              "which the combined pain is lowest moves, that is the pattern the model associates with progressive "
              "disinhibition. A change in which region the paraesthesia covers is outside this model.")
        else:
            A("No candidate observation is offered: P3 is not a gated SUPPORTED verdict.")
    A("")
    A("## Conditional readings, not verdicts")
    A("")
    A("These are what the registered rules would print if the gate that failed had held. They are not verdicts and no "
      "verdict word applies to them.")
    A("")
    if not ok13:
        rfx = res.get("reading_F")
        why = (f" The same driver fails the held-out frequency feature (R-F: {rfx['n_pass']} of {rfx['n_evaluable']} evaluable "
               "networks pass, and candidate 0 fails it at both dt), so the reduction it shows cannot be read as the "
               "published stimulation effect.") if rfx else ""
        A(f"- p1, conditional reading, not a verdict: the registered rule applied to the surround-input stimulation data "
          f"would read \"{res['P1']['verdict_if_gates'].lower()}\" (classes of red_S: {res['P1']['class_S']}; of red_C: "
          f"{res['P1']['class_C']}).{why}")
        if p3r is not None:
            A(f"- p3, conditional reading, not a verdict: the registered rule applied to the sweep subsample would read "
              f"\"{p3r['verdict_if_gates'].lower()}\".{why}")
    else:
        A("None: all gates held.")
    A("")
    A("## Registered readings (no verdict word)")
    A("")
    ra = res.get("reading_A", {})
    for k in ("C_abeta", "C_adelta", "C_all_A"):
        if k in ra:
            A(f"- R-A, ratio to C only, {k}: median {fmt(ra[k]['median'])}, IQR [{fmt(ra[k]['q25'])}, {fmt(ra[k]['q75'])}], "
              f"n = {ra[k]['n']}.")
    if "share_adelta_excites" in ra:
        s = ra["share_adelta_excites"]
        A(f"- R-A, share of accepted networks in which C plus A-delta exceeds C only: {s['k']}/{s['n']}, Wilson "
          f"[{fmt(s['wilson'][0])}, {fmt(s['wilson'][1])}].")
    rf = res.get("reading_F")
    if rf:
        A(f"- R-F, held-out frequency feature on {rf['n']} accepted networks: evaluable {rf['n_evaluable']}, pass "
          f"{rf['n_pass']}; Wilson of pass among all [{fmt(rf['wilson_pass_of_all'][0])}, {fmt(rf['wilson_pass_of_all'][1])}].")
        A("- Median rho(f) over evaluable networks: " + "; ".join(f"{f} Hz {fmt(v['median'])}" for f, v in rf["rho"].items()) + ".")
    A("")
    cv = res["convergence"]
    A("## Convergence (dt halving)")
    A("")
    if cv:
        A(f"{cv['n_networks']} networks at dt {P.DT_MAIN} and {P.DT_PUB} ms: median |dR| {fmt(cv['median_abs_dR'])} Hz "
          f"(limit 1.0); classifications flipped {cv['flips']} of {cv['classifications']} ({fmt(100 * cv['flip_share'], 0)}%, limit 10%). "
          f"G3: {'passed' if cv['passed'] else 'FAILED'}.")
    else:
        A("Not measured.")
    A("")
    A("## Visual traces")
    A("")
    A("`visual-traces.json` and `visual-traces.png`: one accepted network, WDR membrane potential at no shift and at a "
      "collapsed shift, touch alone and touch with stimulation on the surround input.")
    A("")
    A("## Disclosures: checks and pilots run before the main run")
    A("")
    cp = os.path.join(HERE, "results", "prereg", "response-curve.json")
    if os.path.exists(cp):
        cv_ = load(cp)
        A("The one unmodified-model response curve allowed before the pre-registration (candidate 0, shift 0, C input only; "
          "`results/prereg/response-curve.json`), used only to place the C-drive grid. WDR rate (Hz, mean of "
          f"{len(cv_['seeds'])} seeds) against the rate per C fibre (Hz):")
        A("")
        A("| rate per C fibre | " + " | ".join(str(c["rC_hz_per_fibre"]) for c in cv_["curve"]) + " |")
        A("|---|" + "---|" * len(cv_["curve"]))
        A("| WDR rate | " + " | ".join(fmt(c["wdr_rate_hz_mean"], 1) for c in cv_["curve"]) + " |")
        A("")
    A("A pipeline pilot with a smaller protocol ran under the gitignored `results/pilot/` after the code was committed; "
      "nothing from it is a result, and `PREDICTION.md` Amendment 1 records what was seen. The oracle "
      "(`results/oracle/original-hoc-crosscheck.json`) and the tests ran before the main run and are logged in `run.log`.")
    A("")
    A("## Declared limits")
    A("")
    A("See `PREDICTION.md`. The weights are under-constrained, so these outputs are discriminating hypotheses about a "
      "four-cell model and say nothing about any patient. The circuit has no descending (brainstem) input "
      "(`evidence/10-descending-modulation.md` §8.2). These results are not stimulation settings.")
    return "\n".join(L) + "\n"


# --- plots ----------------------------------------------------------------------------------------------------------

def plots(out, res):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    sh = list(P.SHIFTS)
    if "mean_rates" in res:
        mr = res["mean_rates"]
        fig, ax = plt.subplots(1, 2, figsize=(10, 4))
        for c, st in (("T", "-o"), ("TS", "--o")):
            ax[0].plot(sh, mr[c], st, label=c)
        ax[0].set_title("touch-evoked output (C off)")
        for c, st in (("C1", "-o"), ("Ch", "--o")):
            ax[1].plot(sh, mr[c], st, label=c)
        ax[1].set_title("C-driven output")
        for a in ax:
            a.set_xlabel("E_anion shift (model mV)")
            a.set_ylabel("mean WDR rate (Hz)")
            a.legend()
        fig.suptitle("Model units; not stimulation settings")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "outputs-vs-shift.png"), dpi=110)
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(6, 4))
        for key, lab in (("P1", "red_S"), ("P1c", "red_C"), ("P2", "red_Ch")):
            if key == "P1":
                d = res["P1"]["red_S"]
            elif key == "P1c":
                d = res["P1"]["red_C"]
            else:
                d = res["P2"]["red_Ch"]
            pt = np.array([x[0] for x in d], float)
            lo = np.array([x[1] for x in d], float)
            hi = np.array([x[2] for x in d], float)
            ax.errorbar(sh, pt, yerr=[np.nan_to_num(pt - lo), np.nan_to_num(hi - pt)], marker="o", capsize=2, label=lab)
        ax.axhline(THR, color="k", lw=0.8, ls=":")
        ax.set_xlabel("E_anion shift (model mV)")
        ax.set_ylabel("reduction")
        ax.legend()
        ax.set_title("Reductions with bootstrap 95% CI")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "reductions.png"), dpi=110)
        plt.close(fig)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(res["P0"]["onsets"], bins=20)
        ax.axvline(P.P0_ONSET_LIMIT, color="k", ls=":")
        ax.set_xlabel("onset shift (model mV; 45 = none on grid)")
        ax.set_ylabel("networks")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "onset-histogram.png"), dpi=110)
        plt.close(fig)
    rf = res.get("reading_F")
    if rf and rf["rho"]:
        fig, ax = plt.subplots(figsize=(6, 4))
        fs = [int(f) for f in rf["rho"]]
        ax.plot(fs, [rf["rho"][str(f)]["median"] for f in fs], "-o", label="median rho")
        ax.fill_between(fs, [rf["rho"][str(f)]["q25"] for f in fs], [rf["rho"][str(f)]["q75"] for f in fs], alpha=0.25)
        ax.axvspan(30, 100, color="g", alpha=0.08)
        ax.axhline(1.0, color="k", lw=0.8, ls=":")
        ax.set_xscale("log")
        ax.set_xlabel("stimulation frequency on the surround input (Hz)")
        ax.set_ylabel("rho = rate / rate without stimulation")
        ax.set_title("Held-out frequency feature (green: published 30-100 Hz window)")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "frequency-window.png"), dpi=110)
        plt.close(fig)
    vp = os.path.join(out, "visual-traces.json")
    if os.path.exists(vp):
        v = load(vp)
        fig, ax = plt.subplots(2, 2, figsize=(11, 6), sharex=True, sharey=True)
        for p in v["panels"]:
            a = ax[0 if p["shift_mV"] == 0 else 1][0 if p["condition"] == "T" else 1]
            a.plot(p["t_ms"], p["wdr_v"], lw=0.5)
            a.set_title(f"shift {p['shift_mV']} mV, {'touch' if p['condition'] == 'T' else 'touch + surround stimulation'}"
                        f" ({len(p['wdr_spikes_ms'])} WDR spikes)", fontsize=9)
        for a in ax[1]:
            a.set_xlabel("ms")
        for a in ax[:, 0]:
            a.set_ylabel("WDR soma V (mV)")
        fig.suptitle(f"Network {v['network_index']}: {v['label']}")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "visual-traces.png"), dpi=110)
        plt.close(fig)


def zip_models(out):
    zp = os.path.join(out, "per-model-files.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for sub in ("cand", "model", "valid", "sweep", "converge"):
            d = os.path.join(out, sub)
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    z.write(os.path.join(d, f), os.path.join(sub, f))
        for f in sorted(os.listdir(out)):
            if f.startswith("cand0-") and f.endswith(".json"):
                z.write(os.path.join(out, f), f)
    return zp


def main(out):
    res = analyse(out)
    with open(os.path.join(out, "results.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    plots(out, res)
    with open(os.path.join(out, "results.md"), "w") as fh:
        fh.write(write_report(out, res))
    zip_models(out)
    print("aggregate written to " + os.path.relpath(out, HERE))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(os.path.abspath(args[0]) if args else os.path.join(HERE, "results", "main"))
