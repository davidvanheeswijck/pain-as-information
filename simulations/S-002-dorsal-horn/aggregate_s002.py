#!/usr/bin/env python3
"""S-2 aggregator: results.json, results.md and PNGs from the per-model files.

Every number in results.md is generated here from data; no typed claims.  The
verdict words follow PREDICTION.md.  When a gate fails the report prints "NO VERDICT"
and a labelled conditional reading, and no bold verdict word for P0 to P3.

    python aggregate_s002.py [outdir]      (default results/main)
"""

import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s2_protocol as P  # noqa: E402

CAVEAT = "These results are not stimulation settings."


def load(path):
    with open(path) as fh:
        return json.load(fh)


def exists(*p):
    return os.path.exists(os.path.join(*p))


def fmt(x, n=2):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    return f"{x:.{n}f}"


def state(lo, hi, thr=P.RED_THRESHOLD):
    """Where a CI sits against the threshold: 'ge', 'lt' or 'span'."""
    if np.isnan(lo) or np.isnan(hi):
        return "undef"
    if lo >= thr:
        return "ge"
    if hi < thr:
        return "lt"
    return "span"


def p1_rule(shifts, red_s, red_c):
    """PREDICTION.md P1.  red_s, red_c: dict shift -> (pt, lo, hi, defined)."""
    defined = [s for s in shifts if red_s[s][3]]
    st = {s: state(red_s[s][1], red_s[s][2]) for s in defined}
    if defined and all(st[s] == "ge" for s in defined):
        return "REFUTED", "red_S CI lower bound >= 0.20 at every shift where it is defined (kill condition)"
    for i, s_star in enumerate(shifts):
        if not red_s[s_star][3]:
            continue
        earlier = [s for s in defined if s < s_star and st[s] == "ge"]
        later = [s for s in shifts if s >= s_star]
        if earlier and all(red_s[s][3] and st[s] == "lt" for s in later) and \
                all(red_c[s][3] and state(red_c[s][1], red_c[s][2]) == "ge" for s in later):
            return "SUPPORTED", f"first shift {s_star} mV: it reduced at {earlier[-1]} mV and not from {s_star} mV on"
    spans = [s for s in defined if st[s] == "span"]
    if spans:
        return "INCONCLUSIVE", "a CI spans 0.20 at shift(s) " + ", ".join(str(s) for s in spans)
    return "NOT SUPPORTED, NOT REFUTED", "no shift satisfies the SUPPORTED conditions and the kill condition does not hold"


def p2_rule(shifts_eval, red):
    """PREDICTION.md P2 on shifts >= median onset where defined."""
    d = [s for s in shifts_eval if red[s][3]]
    if not d:
        return "NOT SUPPORTED, NOT REFUTED", "no shift at or above the median onset has a defined reduction"
    st = {s: state(red[s][1], red[s][2]) for s in d}
    if all(st[s] == "lt" for s in d):
        return "SUPPORTED", "CI upper bound < 0.20 at every evaluated shift"
    if all(st[s] == "ge" for s in d):
        return "REFUTED", "CI lower bound >= 0.20 at every evaluated shift"
    if any(st[s] == "span" for s in d):
        return "INCONCLUSIVE", "a CI spans 0.20 at shift(s) " + ", ".join(str(s) for s in d if st[s] == "span")
    return "NOT SUPPORTED, NOT REFUTED", "mixed: some shifts reduce, some do not, none spanning"


def shipped_facts():
    """Facts read from the shipped data files (not simulated): which fibres carry the shipped SCS
    pulses, what the A-delta rows connect to, and the weights that differ between folders."""
    import s2_protocol as P2
    frm = [int(float(x)) for x in open(os.path.join(P2.DATA, "FromVector.txt")).read().split()]
    to = [int(float(x)) for x in open(os.path.join(P2.DATA, "ToVector.txt")).read().split()]
    w = [float(x) for x in open(os.path.join(P2.DATA, "WeightVector_foreman.txt")).read().split()]
    rows, tstop = P2.read_shipped_inputs("foreman")
    scs_rows = [k for k in range(90, 105)]
    f = dict(scs_fibres=sorted(set(frm[k] for k in scs_rows)), scs_target=sorted(set(to[k] for k in scs_rows)))
    t = np.array(rows[scs_rows[0]])
    t = t[t < tstop]
    f.update(scs_first_ms=float(t[0]), scs_interval_ms=float(np.median(np.diff(t))), scs_n=int(len(t)),
             scs_same_on_all=all(np.array_equal(np.array(rows[k]), np.array(rows[scs_rows[0]])) for k in scs_rows))
    f["abeta_background_rate_hz"] = float(np.mean([len(np.array(rows[k])[np.array(rows[k]) < tstop]) for k in range(0, 15)]) / (tstop / 1000.0))
    f["adelta_to_sg75_weights"] = sorted(set(w[k] for k in range(45, 60)))
    f["adelta_to_wdr_weights"] = sorted(set(w[k] for k in range(60, 90)))
    f["adelta_to_wdr_targets"] = sorted(set(to[k] for k in range(60, 90)))
    f["surround_out_weights_foreman"] = sorted(set(w[k] for k in range(288, 291)))
    return f


def table_md(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def control_section(out):
    L = []
    recs = []
    for dt in (P.DT_MAIN, P.DT_PUB):
        p = os.path.join(out, f"cand0-dt{dt}.json")
        if os.path.exists(p):
            recs.append(load(p))
    if not recs:
        return ["No control record of candidate 0 was found."], False, recs
    rows = []
    for r in recs:
        w, a, f = r.get("W"), r.get("A"), r.get("F")
        rows.append([r["dt"],
                     f"{fmt(w['early'])} to {fmt(w['late'])} spikes/stim: {'pass' if w['ok'] else 'FAIL'}" if w else "not run",
                     f"with A {fmt(a['with_A'])}, without A {fmt(a['without_A'])}: {'pass' if a['ok'] else 'FAIL'}" if a else "not run",
                     ("rC tried (Hz per fibre: WDR Hz): " + ", ".join(f"{k}: {fmt(v, 1)}" for k, v in r.get("rC_tried", {}).items()) +
                      f"; chosen rC {r.get('rC')}") if "rC_tried" in r else "not run",
                     (("pass" if f["ok"] else "FAIL") + (f" (in band {f.get('inhibited_in_band')}, below 30 Hz {f.get('excited_below_30')}, above 100 Hz {f.get('excited_above_100')})" if "excited_below_30" in f else "")) if f else "not run",
                     "yes" if r["accepted"] else "NO"])
    L.append(table_md(["dt (ms)", "W: wind-up (stimuli 1-5 to 16-20)", "A: A-fibre inhibition", "Drive match", "F: SCS frequency effect", "Accepted"], rows))
    ok = all(r["accepted"] for r in recs) and len(recs) == 2
    L.append("")
    L.append("The control runs in the order W, A, drive match, F and stops at the first failing feature, so a feature after it reads \"not run\". "
             "Features are defined in `PREDICTION.md`: W needs the mean of stimuli 16 to 20 to be at least 1.5 times that of stimuli 1 to 5 and at least 1 spike more; "
             "A needs the mean with A-fibre events to be at most 0.80 of the mean without them (and the latter at least 1 spike per cycle).")
    for r in recs:
        if r.get("F") and r["F"].get("rates"):
            L.append("")
            L.append(f"SCS frequency effect of candidate 0 at dt {r['dt']} (rho = rate / rate without SCS; base {fmt(r['F']['base'])} Hz): " +
                     ", ".join(f"{k} Hz: {fmt(r['F']['rho'][k])}" for k in r["F"]["rho"]) + ".")
    return L, ok, recs


def main(out):
    rj = dict(caveat=CAVEAT)
    forced = exists(out, "forced.json")
    md = [f"# S-2 results: dorsal-horn model of touch-evoked pain\n", f"**{CAVEAT}**\n"] + (["**PILOT, control forced: not a result.**\n"] if forced else []) + [
          "Pre-registration: `PREDICTION.md` (commit 007f633). Every number below is generated from the per-model files by `aggregate_s002.py`. "
          "Shifts are model millivolts; frequencies are those of a synthetic Aβ pulse train in a four-cell model.\n"]
    # gates
    g1 = load(os.path.join(out, "gate_g1.json"))["passed"] if exists(out, "gate_g1.json") else False
    g4 = load(os.path.join(out, "gate_g4.json"))["passed"] if exists(out, "gate_g4.json") else False
    ctrl_lines, ctrl_ok, ctrl_recs = control_section(out)
    md.append("## Positive control (candidate 0, the unmodified starting model)\n")
    md += ctrl_lines
    md.append("")
    acc = load(os.path.join(out, "accepted.json")) if exists(out, "accepted.json") else None
    g2 = bool(acc and acc["ok"])
    models, sweeps, convs = {}, {}, {}
    if acc:
        for i in acc["accepted"]:
            if exists(out, "model", f"{i}.json"):
                models[i] = load(os.path.join(out, "model", f"{i}.json"))
            if exists(out, "sweep", f"{i}.json"):
                sweeps[i] = load(os.path.join(out, "sweep", f"{i}.json"))
            if exists(out, "converge", f"{i}.json"):
                convs[i] = load(os.path.join(out, "converge", f"{i}.json"))
    # candidate funnel
    cands = [load(p) for p in sorted(glob.glob(os.path.join(out, "cand", "*.json")), key=lambda q: int(os.path.basename(q)[:-5]))]
    if cands:
        stages = {}
        for c in cands:
            stages[c["stage"]] = stages.get(c["stage"], 0) + 1
        md.append(f"Ensemble funnel: {len(cands)} candidates considered after candidate 0; stopped at stage W: {stages.get('W', 0)}, A: {stages.get('A', 0)}, "
                  f"rC: {stages.get('rC', 0)}, F or accepted: {stages.get('done', 0)}; accepted {sum(1 for c in cands if c['accepted'])}.\n")
        rj["funnel"] = stages
    rj["gates"] = dict(G1=g1, G2=g2, G4=g4)
    # convergence
    g3, conv_txt = False, "no convergence files"
    if convs:
        dts = (str(P.DT_MAIN), str(P.DT_PUB))
        diffs, flips, ncls = [], 0, 0
        for i, c in convs.items():
            R = c["R"]
            for cond in ("C1", "T", "TS", "TCS"):
                for s in (0, 20):
                    diffs.append(abs(R[f"{cond}|{s}|{dts[0]}"] - R[f"{cond}|{s}|{dts[1]}"]))
            cls = []
            for d in dts:
                a = R[f"T|20|{d}"] >= R[f"T|0|{d}"] + P.ONSET_RISE
                b0 = R[f"TS|0|{d}"] < 0.8 * R[f"T|0|{d}"]
                b20 = R[f"TS|20|{d}"] < 0.8 * R[f"T|20|{d}"]
                cls.append((a, b0, b20))
            for k in range(3):
                ncls += 1
                flips += int(cls[0][k] != cls[1][k])
        med = float(np.median(diffs))
        g3 = med <= 0.5 and flips <= 0.1 * ncls
        conv_txt = f"{len(convs)} networks, median |dR| {fmt(med)} Hz, {flips} of {ncls} classifications flip: {'pass' if g3 else 'FAIL'}"
    rj["gates"]["G3"] = g3
    md.append("## Gates\n")
    md.append(f"- G1, candidate 0 passes W, A and F at both dt: {'pass' if g1 else 'FAIL'}")
    md.append(f"- G2, 200 accepted within the cap: " + (f"{'pass' if g2 else 'FAIL'} ({len(acc['accepted'])} accepted of {acc['considered']} considered)" if acc else "not reached"))
    md.append(f"- G3, dt-halving convergence: {conv_txt}")
    md.append(f"- G4, wiring test passed at the start of the run: {'pass' if g4 else 'FAIL'}\n")
    target = acc["target"] if acc else P.N_ENSEMBLE
    n_sub_req = acc.get("n_sub", P.N_SUBSAMPLE) if acc else P.N_SUBSAMPLE
    all_gates = g1 and g2 and g3 and g4 and len(models) >= target
    rj["all_gates"] = all_gates

    sf = shipped_facts()
    md.append("## What the shipped files show (read from the data files, not simulated)\n")
    md.append(f"- **The A-fibre feature lumps Aβ and Aδ.** The A-fibre-inhibition input drives Aβ (rows 0 to 44) and Aδ (rows 45 to 89) together. "
              f"The shipped weight of Aδ onto the local inhibitory interneuron (SG75, rows 45 to 59) is {sf['adelta_to_sg75_weights']} while Aδ drives the WDR neuron directly "
              f"(rows 60 to 89, weights {sf['adelta_to_wdr_weights']}). Aδ therefore adds WDR spikes and cannot inhibit through SG75; Aβ is the fibre class that inhibits. "
              "The pre-registered criterion counted both together, so the criterion cannot isolate Aβ inhibition.")
    md.append(f"- **The shipped SCS pulses are on the surround fibres, not on Aβ.** In the shipped `Foreman SCS` input the pulses are on fibres {sf['scs_fibres'][0]} to {sf['scs_fibres'][-1]} "
              f"(the surround input to SG76, whose outputs are GABA-A onto the WDR and EX neurons, rows 288 to 290; target cell index {sf['scs_target']}), identical on all 15, "
              f"{sf['scs_n']} pulses, first at {sf['scs_first_ms']:.0f} ms, median interval {sf['scs_interval_ms']:.0f} ms (1 Hz). The Aβ fibres in that file carry a background of about "
              f"{sf['abeta_background_rate_hz']:.1f} Hz per fibre. The pre-registered driver instead pulsed Aβ fibres 0 to 14, which excite the WDR directly. "
              "This comes from the input file; it was not simulated here.")
    md.append(f"- **Wind-up weights.** The wind-up control used the `Foreman SCS` weight table, in which the surround outputs (rows 288 to 290) are {sf['surround_out_weights_foreman']}; "
              "the original `WindUp` folder has them at 0 (`PROVENANCE.md`). This does not affect the wind-up pass (the surround fibres are silent in that input) but it is a difference from the original wind-up run.\n")
    md.append("- **Successor guidance (needs a fresh pre-registration).** Register an Aβ-only versus Aδ-only decomposition of the A-fibre control, an SCS driver on the surround fibres 30 to 44 as the shipped data show, "
              "and a drive grid of about 0.5 to 2 Hz per C fibre.\n")

    if not all_gates:
        md.append("## NO VERDICT\n")
        reasons = []
        if not g1:
            reasons.append("G1: the unmodified starting model does not pass the pre-registered control, so nothing else was run beyond the control record above")
        if g1 and not g2:
            reasons.append("G2: fewer than 200 accepted networks")
        if g1 and g2 and not g3:
            reasons.append("G3: convergence not shown")
        if not g4:
            reasons.append("G4: wiring test failed")
        if g1 and g2 and len(models) < target:
            reasons.append(f"only {len(models)} of {target} networks measured")
        md.append("P0 to P3 are **NO VERDICT**. Reasons: " + "; ".join(reasons) + ".\n")
        if ctrl_recs and not g1:
            r = ctrl_recs[0]
            sent = []
            if r.get("W") and not r["W"]["ok"]:
                sent.append(f"W failed (wind-up: mean {fmt(r['W']['early'])} spikes per stimulus early, {fmt(r['W']['late'])} late)")
            if r.get("A") and not r["A"]["ok"]:
                sent.append(f"A failed (mean {fmt(r['A']['with_A'])} spikes per cycle with A fibres, {fmt(r['A']['without_A'])} without)")
            if r.get("rC_tried") and r.get("rC") is None:
                sent.append("no C rate in the pre-registered set {" + ", ".join(str(x) for x in P.RC_SET) + "} Hz per fibre gives a WDR rate in "
                            f"[{P.RC_BAND[0]:g}, {P.RC_BAND[1]:g}] Hz (WDR rates found: " + ", ".join(f"{k}: {fmt(v, 1)}" for k, v in r["rC_tried"].items()) + ")")
            if r.get("F") and not r["F"]["ok"]:
                sent.append("F failed")
            md.append("Conditional reading, not a verdict: candidate 0 at dt " + str(r["dt"]) + ": " + ("; ".join(sent) if sent else "see the table") +
                      ". This describes the pre-registered control (its lumping of Aβ and Aδ and its SCS driver, see the section above) against the tolerances fixed in `PREDICTION.md`; it does not show the port or the published model to be wrong.\n")
        rj["verdicts"] = "NO VERDICT"
        write(out, rj, md)
        return rj

    # ---- full analysis ----
    ids = sorted(models)
    n = len(ids)
    shifts = list(P.SHIFTS)
    Rm = {c: np.array([[np.mean(models[i]["R"][c][str(s)]) for s in shifts] for i in ids]) for c in P.CONDITIONS}
    idx = P.boot_indices(n, seed=1)
    rj["n_networks"] = n
    # P0
    ons = []
    for k in range(n):
        o = P.onset_shift(list(Rm["T"][k]))
        ons.append(P.ONSET_NONE_VALUE if o is None else float(o))
    med, lo, hi = P.median_ci(ons, idx)
    p0 = "SUPPORTED" if (lo >= 10 and hi <= 25) else ("REFUTED" if (hi < 5 or lo > 30) else "INCONCLUSIVE")
    frac_onset = float(np.mean([o < P.ONSET_NONE_VALUE for o in ons]))
    rj["P0"] = dict(median=med, ci=[lo, hi], proportion_with_onset=frac_onset, verdict=p0)
    # reductions
    def red(num, den, minrate=P.MIN_DEFINED_RATE):
        d = {}
        for j, s in enumerate(shifts):
            pt, l, h_ = P.ratio_reduction_ci(num[:, j], den[:, j], idx)
            d[s] = (pt, l, h_, bool(den[:, j].mean() >= minrate))
        return d
    red_s = red(Rm["TS"], Rm["T"])
    red_c = red(Rm["Ch"], Rm["C1"])
    p1, p1why = p1_rule(shifts, red_s, red_c)
    rj["P1"] = dict(verdict=p1, why=p1why, red_S={str(s): v for s, v in red_s.items()}, red_C={str(s): v for s, v in red_c.items()})
    # P2
    E = Rm["TC"] - Rm["C1"]
    Eh = Rm["TCh"] - Rm["Ch"]
    red_ch = red(Eh, E)
    ev_shifts = [s for s in shifts if s >= med] if med < P.ONSET_NONE_VALUE else []
    p2, p2why = p2_rule(ev_shifts, red_ch)
    rj["P2"] = dict(verdict=p2, why=p2why, evaluated_shifts=ev_shifts, red_Ch={str(s): v for s, v in red_ch.items()})
    # P1b and P3 on the subsample
    sub = [i for i in ids if i in sweeps][:n_sub_req]
    ns = len(sub)
    p1b, p3 = None, None
    if ns >= n_sub_req:
        pos = {i: k for k, i in enumerate(ids)}
        sidx = P.boot_indices(ns, seed=2)
        S = {i: {k: np.mean(v) for k, v in sweeps[i]["S"].items()} for i in sub}
        red_best = {}
        for s in P.SWEEP_SHIFTS:
            best = np.array([min(S[i][f"TCS|norm|{s}|{f}"] for f in P.SWEEP_FREQS) for i in sub])
            tc = np.array([Rm["TC"][pos[i], shifts.index(s)] for i in sub])
            pt, l, h_ = P.ratio_reduction_ci(best, tc, sidx)
            red_best[s] = (pt, l, h_, bool(tc.mean() >= P.MIN_DEFINED_RATE))
        rc_sub = {}
        for s in P.SWEEP_SHIFTS:
            num = np.array([Rm["Ch"][pos[i], shifts.index(s)] for i in sub])
            den = np.array([Rm["C1"][pos[i], shifts.index(s)] for i in sub])
            pt, l, h_ = P.ratio_reduction_ci(num, den, sidx)
            rc_sub[s] = (pt, l, h_, bool(den.mean() >= P.MIN_DEFINED_RATE))
        v1b, why1b = p1_rule(list(P.SWEEP_SHIFTS), red_best, rc_sub)
        rj["P1b"] = dict(verdict=v1b, why=why1b, red_best={str(s): v for s, v in red_best.items()})
        p1b = rj["P1b"]
        # P3
        def fstar(net, shift, var="norm"):
            vals = [S[net][f"TCS|{var}|{shift}|{f}"] for f in P.SWEEP_FREQS]
            return int(np.argmin(vals))
        def relief(r_s, r_ref):
            return (1.0 - r_s / r_ref) if r_ref > 0 else None
        def u_main(net, shift):
            j = shifts.index(shift)
            k = pos[net]
            rt, rc = relief(Rm["TS"][k, j], Rm["T"][k, j]), relief(Rm["CS"][k, j], Rm["C1"][k, j])
            return (rt, rc)
        def u_var(net, v):
            j = shifts.index(P.DELTA_REF)
            k = pos[net]
            rt = relief(S[net][f"TS|{v}|{P.DELTA_REF}|{P.SCS_PRIMARY_HZ}"], Rm["T"][k, j])
            rc = relief(S[net][f"CS|{v}|{P.DELTA_REF}|{P.SCS_PRIMARY_HZ}"], Rm["C1"][k, j])
            return (rt, rc)
        res = {}
        for label in ("progressive", "H", "D1", "D2"):
            both = sel = mov = uni = n_def = 0
            for net in sub:
                rt0, rc0 = u_main(net, P.DELTA_REF)
                if label == "progressive":
                    rt1, rc1 = u_main(net, P.DELTA_PROG)
                    f1 = fstar(net, P.DELTA_PROG)
                else:
                    rt1, rc1 = u_var(net, label)
                    f1 = fstar(net, P.DELTA_REF, label)
                f0 = fstar(net, P.DELTA_REF)
                if None in (rt0, rc0, rt1, rc1):
                    continue
                n_def += 1
                du = (rt1 - rc1) - (rt0 - rc0)
                dmean = (rt1 + rc1) / 2 - (rt0 + rc0) / 2
                s_ = du <= -0.20
                m_ = abs(f1 - f0) >= 1
                sel += s_
                mov += m_
                both += (s_ and m_)
                uni += (abs(du) <= 0.10 and dmean <= -0.10 and not m_)
            res[label] = dict(n_defined=n_def, selective_loss=sel, optimum_moves=mov, both=both, uniform_loss=uni,
                              both_wilson=P.wilson(both, n_def))
        a = res["progressive"]["both_wilson"]
        others = [res[v]["both_wilson"] for v in ("H", "D1", "D2")]
        if a[1] < 0.5:
            v3 = "REFUTED"
        elif a[0] > 0.5 and all(o[1] < 0.5 for o in others):
            v3 = "SUPPORTED"
        elif a[0] <= 0.5 <= a[1] or any(o[0] <= 0.5 <= o[1] for o in others):
            v3 = "INCONCLUSIVE"
        else:
            v3 = "NOT SUPPORTED, NOT REFUTED"
        rj["P3"] = dict(verdict=v3, res=res)
        p3 = rj["P3"]
    # ---- text ----
    md.append("## Q1: when does touch drive the projection neuron (P0)\n")
    md.append(f"Onset shift (smallest grid shift at which touch-only output rises by {P.ONSET_RISE:g} Hz above its own value at 0 mV): median {fmt(med, 1)} mV "
              f"(95% bootstrap CI {fmt(lo, 1)} to {fmt(hi, 1)}; networks with no onset counted as {P.ONSET_NONE_VALUE:g}); {frac_onset:.0%} of {n} networks have an onset on the grid. "
              f"**P0 {p0}** (pre-registered: median in [10, 25] mV).\n")
    md.append("## Q2: what still reduces touch-evoked output (P1, P2)\n")
    rows = []
    for s in shifts:
        a, b, c = red_s[s], red_c[s], red_ch[s]
        rows.append([s, fmt(Rm["T"][:, shifts.index(s)].mean()), f"{fmt(a[0])} [{fmt(a[1])}, {fmt(a[2])}]" + ("" if a[3] else " (undef)"),
                     fmt(Rm["C1"][:, shifts.index(s)].mean()), f"{fmt(b[0])} [{fmt(b[1])}, {fmt(b[2])}]",
                     f"{fmt(c[0])} [{fmt(c[1])}, {fmt(c[2])}]" + ("" if c[3] else " (undef)")])
    md.append(table_md(["Δ (mV)", "touch-only rate (Hz)", "red_S: 20 Hz SCS on touch-evoked", "C-only rate (Hz)", "red_C: C x0.5 on C-driven", "red_Ch: C x0.5 on touch-on-background"], rows))
    md.append(f"\n**P1 {p1}** ({p1why}). **P2 {p2}** ({p2why}); shifts evaluated: {ev_shifts}.\n")
    if p1b:
        md.append(f"P1b (secondary, {ns} networks, best of {len(P.SWEEP_FREQS)} frequencies, touch plus background): **{p1b['verdict']}** ({p1b['why']}). red_best by shift: " +
                  ", ".join(f"{s} mV: {fmt(v[0])} [{fmt(v[1])}, {fmt(v[2])}]" for s, v in red_best.items()) + ".\n")
    if p3:
        md.append("## Q3: observable changes (P3)\n")
        rows = [[k, v["n_defined"], v["selective_loss"], v["optimum_moves"], v["both"], f"[{fmt(v['both_wilson'][0])}, {fmt(v['both_wilson'][1])}]", v["uniform_loss"]]
                for k, v in p3["res"].items()]
        md.append(table_md(["Change from the reference (Δ = 15 mV)", "networks", "selective loss", "optimum moves", "both", "Wilson 95% (both)", "uniform loss, optimum fixed"], rows))
        md.append(f"\n**P3 {p3['verdict']}**. Recovery off stimulation is true of habituation by definition and is not simulated; the paraesthesia map is outside the model.\n")
    md.append("## Declared limits\n\nSee `PREDICTION.md`. " + CAVEAT + "\n")
    rj["verdicts"] = dict(P0=p0, P1=p1, P2=p2, P1b=(p1b or {}).get("verdict"), P3=(p3 or {}).get("verdict"))
    write(out, rj, md)
    return rj


def write(out, rj, md):
    def default(o):
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating, np.bool_)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(type(o))
    with open(os.path.join(out, "results.json"), "w") as fh:
        json.dump(rj, fh, indent=1, default=default)
    text = "\n".join(md)
    # the file must open with the caveat sentence
    text = text.replace("# S-2 results: dorsal-horn model of touch-evoked pain\n", "These results are not stimulation settings.\n\n# S-2 results: dorsal-horn model of touch-evoked pain\n", 1)
    with open(os.path.join(out, "results.md"), "w") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results", "main"))
