"""Port-versus-original equivalence for S-2b: the non-circular check.

The committed file results/oracle/original-hoc-crosscheck.json holds spike counts produced by NEURON
executing the ORIGINAL ModelDB 168414 hoc network (crosscheck_original_hoc.py), not by this code.  This test
runs the Python port (dh_model.py) on the same four A-fibre conditions at dt 0.025 and compares.

    simulations/.venv/bin/python -B -m unittest test_s2b_oracle    (from this directory, ~40 s)

The last test is the mutation check: the same comparison on a deliberately wrong port (the A-beta input to
the local inhibitory interneuron SG75 removed) must FAIL it.
"""

import gc
import json
import os
import re
import subprocess
import sys
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import crosscheck_original_hoc as oracle  # noqa: E402
import s2b_protocol as P  # noqa: E402

ORACLE_JSON = os.path.join(HERE, "results", "oracle", "original-hoc-crosscheck.json")
CONDS = ("C_only", "C_abeta", "C_adelta", "C_all_A")
MEAN_TOL = 0.1       # spikes per cycle: the pre-registered G6 tolerance on the cycle mean
CYCLE_TOL = 1        # spikes: tolerance per cycle (fixed-step integration, event-queue details)


def equivalent(port_counts, oracle_counts):
    """True iff the port reproduces the original: cycle mean within MEAN_TOL, every cycle within CYCLE_TOL."""
    p, o = np.asarray(port_counts, float), np.asarray(oracle_counts, float)
    return bool(abs(p.mean() - o.mean()) <= MEAN_TOL + 1e-9 and np.max(np.abs(p - o)) <= CYCLE_TOL)


def port_counts(weight_factors=None, conds=None):
    import dh_model as dm
    model = dm.DorsalHorn(weight_factors=weight_factors, dt=0.025)
    out = {}
    for name, (keep_b, keep_d) in P.A_CONDITIONS.items():
        if conds and name not in conds:
            continue
        ev = P.afib_events(model, keep_b, keep_d)
        model.set_shift(0)
        wdr = model.run(ev, P.A_TSTOP, 0.025)["WDR"]
        out[name] = P.afib_counts(wdr).tolist()
    del model
    gc.collect()
    return out


def port_counts_isolated(weight_factors=None, conds=None):
    """The port in a fresh process: two networks built one after the other in one process can crash NEURON."""
    r = subprocess.run([sys.executable, "-B", os.path.abspath(__file__), "--port-counts", json.dumps(weight_factors or {}),
                        json.dumps(conds or [])],
                       capture_output=True, text=True, cwd=HERE)
    for line in r.stdout.splitlines():
        if line.startswith("COUNTS "):
            return json.loads(line[7:])
    raise RuntimeError(f"port run failed (rc {r.returncode}): {r.stderr.strip().splitlines()[-3:]}")


_CACHE = {}


def port_normal():
    if "normal" not in _CACHE:
        _CACHE["normal"] = port_counts_isolated()
    return _CACHE["normal"]


class OracleRecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ORACLE_JSON) as fh:
            cls.o = json.load(fh)

    def test_archive_hash_is_the_one_in_provenance(self):
        with open(os.path.join(P.S2_DIR, "PROVENANCE.md")) as fh:
            prov = fh.read()
        self.assertIn(self.o["archive"]["sha256"], prov)
        self.assertTrue(self.o["archive"]["sha256_matches"])

    def test_every_file_matches_its_recorded_hash(self):
        self.assertTrue(all(f["ok"] for f in self.o["files"].values()))
        for h in oracle.HOC:
            self.assertIn(h, self.o["files"])

    def test_banned_tokens_scan_was_clean_before_loading(self):
        self.assertEqual(self.o["banned_tokens"], list(oracle.BANNED))
        self.assertEqual(sorted(self.o["loaded_hoc"]), sorted(oracle.HOC))
        for name, s in self.o["banned_token_scan"].items():
            self.assertEqual(s["banned_hits"], [], name)
            self.assertEqual(s["other_load_calls"], [], name)

    def test_mechanisms_identical_to_originals_after_crlf_normalisation(self):
        self.assertTrue(self.o["mechanisms_all_identical_after_crlf_normalisation"])
        self.assertEqual(len(self.o["mechanisms"]), 17)

    def test_port_data_equal_to_original_data(self):
        self.assertTrue(all(self.o["data_equal_to_port_data"].values()), self.o["data_equal_to_port_data"])

    def test_oracle_reproduces_the_reviewers_table_at_dt_0_025(self):
        runs = self.o["runs"]["0.025"]
        for c, want in oracle.REVIEWER.items():
            self.assertEqual(round(runs[c]["mean"], 1), want, c)
        self.assertTrue(all(self.o["matches_reviewer_dt_0_025"].values()))

    def test_oracle_runs_were_to_21_s_and_truncation_is_harmless(self):
        self.assertEqual(self.o["tstop_ms"], 21000.0)
        for c, r in self.o["full_length_check"].items():
            self.assertGreater(r["tstop"], 200000.0)
            self.assertEqual(r["counts"], self.o["runs"]["0.025"][c]["counts"], c)


class Scanner(unittest.TestCase):
    """The pre-load scan refuses a file that contains a banned token."""

    def test_scan_flags_each_banned_token(self):
        for tok in ("system(", "popen", "unix"):
            self.assertEqual(oracle.scan_text(f"// harmless\nx = 1 {tok.upper()} y"), [tok])
        self.assertEqual(oracle.scan_text("proc f() { print 1 }"), [])

    def test_other_load_calls_are_flagged_but_nrngui_and_comments_are_not(self):
        self.assertEqual(oracle.loads_other_than_nrngui('load_file("nrngui.hoc")\n//load_file("x.hoc")\n'), [])
        self.assertEqual(len(oracle.loads_other_than_nrngui('load_file("mosinit.hoc")')), 1)

    def test_strip_nrngui_removes_only_that_line(self):
        txt = 'load_file("nrngui.hoc")\nobjref a\n'
        out = oracle.strip_nrngui(txt)
        self.assertNotIn("nrngui", out.replace("(nrngui line stripped in this copy)", ""))
        self.assertIn("objref a", out)

    def test_original_hoc_hashes_are_the_ones_the_script_pins(self):
        for h in oracle.HOC:
            self.assertTrue(re.fullmatch(r"[0-9a-f]{64}", oracle.FILES[h]))


class PortEquivalence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ORACLE_JSON) as fh:
            cls.o = json.load(fh)
        cls.port = port_normal()

    def test_port_matches_original_on_every_condition(self):
        for c in CONDS:
            o = self.o["runs"]["0.025"][c]["counts"]
            self.assertTrue(equivalent(self.port[c], o), f"{c}: port {self.port[c]} original {o}")

    def test_port_reproduces_the_reviewers_four_numbers(self):
        for c, want in oracle.REVIEWER.items():
            self.assertEqual(round(float(np.mean(self.port[c])), 1), want, c)

    def test_abeta_only_reduces_and_adelta_only_excites(self):
        m = {c: float(np.mean(self.port[c])) for c in CONDS}
        self.assertLessEqual(m["C_abeta"], 0.8 * m["C_only"])
        self.assertGreater(m["C_adelta"], m["C_only"])


class Mutation(unittest.TestCase):
    """The comparison must FAIL on a wrong port (run with python -B)."""

    def test_removing_abeta_to_sg75_fails_the_equivalence(self):
        with open(ORACLE_JSON) as fh:
            o = json.load(fh)
        wrong = port_counts_isolated({"abeta_sg": 0.0}, ["C_abeta"])
        failed = [c for c in wrong if not equivalent(wrong[c], o["runs"]["0.025"][c]["counts"])]
        self.assertIn("C_abeta", failed)

    def test_equivalent_rejects_a_shifted_count(self):
        self.assertFalse(equivalent([8] * 10, [11] * 10))
        self.assertTrue(equivalent([8] * 10, [8] * 10))


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--port-counts":
        print("COUNTS " + json.dumps(port_counts(json.loads(sys.argv[2]) or None, json.loads(sys.argv[3]) or None)))
    else:
        unittest.main()
