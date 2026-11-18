#!/usr/bin/env python3
"""Original-model oracle for S-2b: run the ORIGINAL ModelDB 168414 hoc network, not the Python port.

    simulations/.venv/bin/python -I crosscheck_original_hoc.py WORKDIR [--archive ZIP] [--workers 4]
                                   [--dt 0.025 0.0125] [--full-length] [--out results/oracle/original-hoc-crosscheck.json]

WORKDIR must be a NEW EMPTY directory outside the repository.  The script puts the original files
there (downloaded from the github.com/ModelDBRepository/168414 mirror, or taken from --archive), checks
the archive sha256 against S-2's PROVENANCE.md and every extracted file against the hashes in this script,
and checks that the mechanisms in S-002-dorsal-horn/mod/ are byte-identical to the originals after CRLF
normalisation.  ModelDB code is untrusted data:

  * Only `CellTemplates.hoc`, `MakeNetwork.hoc` and `RunSim_EP.hoc` of the `A Fiber Inhibition` folder are
    ever loaded.  `mosinit.hoc`, `Shell.hoc` and every save procedure are never loaded or called.
  * BEFORE loading anything, each of the three files is scanned for `system(`, `popen` and `unix`
    (case-insensitive); if any occurs the script refuses to run.  Any `load_file`/`xopen` other than the
    `nrngui` line also stops it.
  * The `load_file("nrngui.hoc")` line is stripped in a COPY (`*_ng.hoc`), and the copies are rescanned.
  * The simulations run in a fresh child process per (dt, condition), started with `python -I` and a
    scrubbed environment.

Protocol: the shipped A-fibre-inhibition input, first 10 cycles (21 s); events of the dropped fibre classes
are not delivered.  Score: WDR soma upward crossings of -30 mV (the original `OutputData` recorder) in
[1000 + 2000k, 3000 + 2000k) ms, k = 0..9.  Conditions: C only, C plus A-beta only, C plus A-delta only,
C plus all A.  The mechanisms are the S-2 compiled ones (run `nrnivmodl` in S-002-dorsal-horn/mod first).
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
S2_DIR = os.path.join(os.path.dirname(HERE), "S-002-dorsal-horn")

ARCHIVE_URL = "https://github.com/ModelDBRepository/168414/archive/refs/heads/master.zip"
ARCHIVE_SHA256 = "ae2967d49b72243f569541c79b9e7a3c9d3d31b77abcf38c75c4c9ce12fa36cc"   # S-2 PROVENANCE.md
TOP = "168414-master/"
FOLDER = TOP + "A Fiber Inhibition/"
MODDIR = TOP + "Critical Mod Files/"

HOC = ("CellTemplates.hoc", "MakeNetwork.hoc", "RunSim_EP.hoc")
BANNED = ("system(", "popen", "unix")
FILES = {   # name in the A Fiber Inhibition folder -> sha256 (original bytes)
    "CellTemplates.hoc": "fb5c67adc20471be4c4b91f1ce3cd9f324d74b75220b107f0816978183fc9bbf",
    "MakeNetwork.hoc": "3132e114808bf7a8475ad71425639f8cbee983f448f61cf544dd4289b419f1be",
    "RunSim_EP.hoc": "5cadd9de0c3f5f10424c1fc159abd92e112575040098dab59b40184c169c0011",
    "CellVector.txt": "7a49bece4aee959e991646ab6f15003bbb76322b99df2b563ec3ee52aa867f7b",
    "XVector.txt": "36b7e1d4e0eab633b871cc70db615cd6056bf6b34f9a8fae2c6ac44a858a12b3",
    "YVector.txt": "b4a54804484d4aa92af5d9999db50b2bc98efac3c68c8017ff86e41ae96b54d7",
    "ZVector.txt": "876000f6a6857b4a571a5949abdfac77a8400be898a053fdfdf00eebd32933c4",
    "CellTypeVector.txt": "49e73ced6e5b31dc514225234c0f67e06bbf97ac97615f8a83a8add3ca1aae53",
    "CellTempList.dat": "adbd59e25bbaa37f9ad0a21b92e0523f66067f20239b4dd3f6d376afd5707cf6",
    "FromVector.txt": "3004e62bce84ed9509462c219a24aa53fc252e134654556225303e28fd764f28",
    "ToVector.txt": "3af10451d3a6d249077ea785eeb910870a0b32ad3900d303ebff57b614771cf5",
    "SynapseVector.txt": "3a05511a44d77cb592ed99e31b7d29596327aefe99246f3ce86538395e62ea4b",
    "WeightVector.txt": "515eee3aa0babe73c1986ee21712e198b71f5588e15d3dd137e3819f1efac326",
    "DelayVector.txt": "8b920c4a04cef63743d03797dc62371f07b93990e35ec649a5459693f30e3f13",
    "ThresholdVector.txt": "0250d4a897814835e2fb5f18c28e779ed4d01b109ed4ee383b1841f0b1aaefb0",
    "SpikeStatsVector.txt": "354f929dcee46b769dc78b7a461ff673a618e053fb47197ccd165e85cd7babb5",
    "SpikeTimesVector.txt": "6190ad7f892c3412b4ab286490329c843a6f01f5cbd7dbf20de6defab29a8013",
    # read by the `synapses()` procedures of the three cell templates (synapse counts per type)
    "SG_Cell_SynapseID.dat": "fc1b006047c667c763b2ca8fbb4505cdfcd966b69d456c80798987cf49dc6eb6",
    "IN_Cell_SynapseID.dat": "5804d1b59a6e0b48fb51c0a2fa28c476f627aaf735541b9019b9b218f8a21a8a",
    "T_Cell_SynapseID.dat": "033fb389825e575f3e55ccea192e64b0b1b84652beb2bdd3e657b7eafdfb714a",
    "SG_Cell_Synapses_OneEX_Zone2_SCS.txt": "b8359b225d3f290ec2660cfb753024d38cab97e0741213136a0823a27d6e0336",
    "IN_Cell_Synapses_OneEX_Zone2_SCS.txt": "ac2abe563d9d0754669d1dda76a6421235d59037a8105f2a90042e47f5d2b0bf",
    "T_Cell_Synapses_OneEX_Zone2_SCS.txt": "e9e4c9b3263fda69cc8422887e8feda3af01fcf15286b513ab9652a17b08432e",
}
# original file -> the S-2 copy in data/ that must be equal after CRLF normalisation
DATA_COPIES = {
    "FromVector.txt": "FromVector.txt",
    "ToVector.txt": "ToVector.txt",
    "SynapseVector.txt": "SynapseVector.txt",
    "DelayVector.txt": "DelayVector.txt",
    "WeightVector.txt": "WeightVector_foreman.txt",
    "SpikeStatsVector.txt": "afib_SpikeStatsVector.txt",
    "SpikeTimesVector.txt": "afib_SpikeTimesVector.txt",
}
MODS = ("AMPA_DynSyn B_A B_DR B_NA CaIntraCellDyn GABAa_DynSyn Glycine_DynSyn HH2 KDR KDRI NK1_DynSyn "
        "NMDA_DynSyn SS iCaAN iCaL iKCa iNaP").split()

# condition -> half-open range of fibres whose events are NOT delivered
CONDITIONS = {"C_only": (0, 30), "C_all_A": (-1, -1), "C_abeta": (15, 30), "C_adelta": (0, 15)}
# the reviewer's table (Amendment 2 of S-2's PREDICTION.md), spikes per cycle, dt 0.025
REVIEWER = {"C_only": 11.3, "C_all_A": 19.4, "C_abeta": 8.0, "C_adelta": 23.3}
T_SHORT = 21000.0


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def lf(b):
    return b.replace(b"\r\n", b"\n")


def scan_text(text):
    """Banned tokens found in a hoc text (case-insensitive)."""
    low = text.lower()
    return [t for t in BANNED if t in low]


def loads_other_than_nrngui(text):
    """load_file / xopen calls that are not the nrngui line and are not commented out."""
    bad = []
    for line in text.splitlines():
        code = line.split("//", 1)[0]
        for m in re.finditer(r'\b(load_file|xopen)\s*\(\s*"([^"]*)"', code):
            if m.group(2) != "nrngui.hoc":
                bad.append(m.group(0))
    return bad


def strip_nrngui(text):
    return re.sub(r'^\s*load_file\("nrngui\.hoc"\)', "// (nrngui line stripped in this copy)", text, flags=re.M)


# --- child: one hoc-network run --------------------------------------------------------------------

def child(files_dir, cond, dt, tstop):
    os.chdir(files_dir)
    import numpy as np
    from neuron import h
    lib = None
    for arch in ("arm64", "x86_64", "aarch64"):
        for ext in ("dylib", "so"):
            p = os.path.join(S2_DIR, "mod", arch, "libnrnmech." + ext)
            if os.path.exists(p):
                lib = p
    if lib is None:
        raise SystemExit("compiled S-2 mechanisms not found: run nrnivmodl in S-002-dorsal-horn/mod")
    h.nrn_load_dll(lib)
    h.load_file("stdrun.hoc")
    h.load_file("CellTemplates_ng.hoc")
    h.load_file("MakeNetwork.hoc")
    h.load_file("RunSim_EP_ng.hoc")
    h.dt = dt
    h.tstop = tstop
    lo, hi = CONDITIONS[cond]
    fromv = np.array(h.FromVec)
    skip = h.Vector(len(fromv))
    for k in range(len(fromv)):
        if lo <= fromv[k] < hi:
            skip.x[k] = 1
    h("objref skipk")
    h.skipk = skip
    # same procedure as the shipped loadqueue(), with the events of the dropped fibres skipped
    h("""
proc loadqueue() { local j, kk
    for kk = 0, numspikes.size()-1 {
        if (skipk.x[kk]) continue
        for j = 0, numspikes.x[kk]-1 {
            nclist.object(kk).event(SpikeVector[kk].x[j])
        }
    }
}
""")
    t0 = time.time()
    h.OutputData()          # the shipped recorder set-up, init() and run()
    s = np.array(h.OutputTimesT)
    counts = [int(((s >= 1000 + 2000 * k) & (s < 3000 + 2000 * k)).sum()) for k in range(10)]
    res = dict(cond=cond, dt=dt, tstop=float(h.tstop), counts=counts, mean=float(np.mean(counts)),
               n_cells=int(h.cells.count()), n_netcons=int(h.nclist.count()), n_skipped_rows=int(skip.sum()),
               n_wdr_spikes_total=int(len(s)), seconds=time.time() - t0)
    print("RESULT " + json.dumps(res), flush=True)


# --- parent -----------------------------------------------------------------------------------------------

def child_env():
    env = {k: os.environ[k] for k in ("PATH", "HOME", "TMPDIR", "LD_LIBRARY_PATH", "DYLD_LIBRARY_PATH", "PYTHONHOME")
           if k in os.environ}
    return env


def run_child(files_dir, cond, dt, tstop):
    cmd = [sys.executable, "-I", os.path.abspath(__file__), "--child", files_dir, cond, repr(dt), repr(tstop)]
    r = subprocess.run(cmd, capture_output=True, text=True, env=child_env(), cwd=files_dir)
    for line in r.stdout.splitlines():
        if line.startswith("RESULT "):
            return json.loads(line[7:])
    raise RuntimeError(f"child {cond} dt {dt} failed (rc {r.returncode}): {r.stderr.strip().splitlines()[-3:]}")


def prepare(workdir, archive):
    if os.path.exists(workdir) and os.listdir(workdir):
        raise SystemExit("WORKDIR must be a new empty directory")
    rp = os.path.realpath(workdir)
    repo = os.path.realpath(os.path.join(HERE, "..", ".."))
    if rp == repo or rp.startswith(repo + os.sep):
        raise SystemExit("WORKDIR must be outside the repository")
    os.makedirs(workdir, exist_ok=True)
    files_dir = os.path.join(workdir, "files")
    os.makedirs(files_dir)
    if archive:
        with open(archive, "rb") as fh:
            blob = fh.read()
    else:
        with urllib.request.urlopen(ARCHIVE_URL, timeout=120) as resp:
            blob = resp.read()
    zpath = os.path.join(workdir, "archive.zip")
    with open(zpath, "wb") as fh:
        fh.write(blob)
    got = sha256(blob)
    if got != ARCHIVE_SHA256:
        raise SystemExit(f"archive sha256 {got} differs from PROVENANCE.md ({ARCHIVE_SHA256}); refusing")
    info = dict(url=ARCHIVE_URL, sha256=got, expected_sha256=ARCHIVE_SHA256, sha256_matches=True)
    z = zipfile.ZipFile(zpath)
    names = set(z.namelist())
    files = {}
    for name, want in FILES.items():
        data = z.read(FOLDER + name)             # exact member names only; no extractall
        files[name] = dict(sha256=sha256(data), expected=want, ok=sha256(data) == want)
        with open(os.path.join(files_dir, name), "wb") as fh:
            fh.write(data)
        if sha256(data) != want:
            raise SystemExit(f"{name}: sha256 differs from the one recorded in this script; refusing")
    # the data files the port reads must equal the originals after CRLF normalisation
    data_eq = {}
    for orig, copy in DATA_COPIES.items():
        with open(os.path.join(S2_DIR, "data", copy), "rb") as fh:
            mine = fh.read()
        with open(os.path.join(files_dir, orig), "rb") as fh:
            theirs = fh.read()
        data_eq[f"{orig} == data/{copy} (CRLF-normalised)"] = lf(mine) == lf(theirs)
    # mechanisms
    mods = {}
    for m in MODS:
        assert MODDIR + m + ".mod" in names, m
        theirs = z.read(MODDIR + m + ".mod")
        with open(os.path.join(S2_DIR, "mod", m + ".mod"), "rb") as fh:
            mine = fh.read()
        mods[m + ".mod"] = dict(original_sha256=sha256(theirs), copy_sha256=sha256(mine),
                                identical_after_crlf_normalisation=lf(theirs) == lf(mine),
                                identical_bytes=theirs == mine)
    # scan BEFORE anything is loaded
    scan = {}
    for h in HOC:
        with open(os.path.join(files_dir, h), "r", errors="replace") as fh:
            text = fh.read()
        hits, other = scan_text(text), loads_other_than_nrngui(text)
        scan[h] = dict(banned_hits=hits, other_load_calls=other)
        if hits or other:
            raise SystemExit(f"{h}: refusing to run: banned token(s) {hits} / other load calls {other}")
    # stripped copies, rescanned
    for h in ("CellTemplates.hoc", "RunSim_EP.hoc"):
        with open(os.path.join(files_dir, h), "r", errors="replace") as fh:
            text = strip_nrngui(fh.read())
        ng = h.replace(".hoc", "_ng.hoc")
        if scan_text(text) or loads_other_than_nrngui(text) or re.search(r'^\s*load_file\("nrngui', text, re.M):
            raise SystemExit(f"{ng}: stripped copy still not clean; refusing")
        with open(os.path.join(files_dir, ng), "w") as fh:
            fh.write(text)
        scan[ng] = dict(banned_hits=[], other_load_calls=[], nrngui_stripped=True)
    return files_dir, info, files, data_eq, mods, scan


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("workdir", nargs="?")
    ap.add_argument("--archive", default=None, help="an already downloaded master.zip (sha256 is still checked)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--dt", type=float, nargs="+", default=[0.025, 0.0125])
    ap.add_argument("--full-length", action="store_true",
                    help="also run C only and C plus A-beta at dt 0.025 for the shipped 221 s (truncation check)")
    ap.add_argument("--out", default=os.path.join(HERE, "results", "oracle", "original-hoc-crosscheck.json"))
    ap.add_argument("--child", nargs=4, metavar=("FILES", "COND", "DT", "TSTOP"), help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.child:
        f, c, d, t = args.child
        child(f, c, float(d), float(t))
        return 0
    if not args.workdir:
        ap.error("WORKDIR is required")
    print(time.strftime("%Y-%m-%d %H:%M:%S ") + "oracle start", flush=True)
    files_dir, arch, files, data_eq, mods, scan = prepare(args.workdir, args.archive)
    print("archive sha256 ok; hoc files scanned clean; mods and data checked", flush=True)
    jobs = [(c, dt, T_SHORT) for dt in args.dt for c in CONDITIONS]
    if args.full_length:
        jobs += [(c, 0.025, None) for c in ("C_only", "C_abeta")]

    def go(job):
        c, dt, tstop = job
        if tstop is None:    # shipped tstop
            with open(os.path.join(files_dir, "SpikeStatsVector.txt")) as fh:
                vals = fh.read().split()
            tstop = float(vals[1 + int(float(vals[0]))])
        r = run_child(files_dir, c, dt, tstop)
        print(f"{c} dt {dt} tstop {tstop}: counts {r['counts']} mean {r['mean']:.1f} ({r['seconds']:.0f} s)", flush=True)
        return r

    with ThreadPoolExecutor(args.workers) as ex:
        res = list(ex.map(go, jobs))
    runs, full = {}, {}
    for (c, dt, tstop), r in zip(jobs, res):
        if tstop is None:
            full[c] = r
        else:
            runs.setdefault(repr(dt), {})[c] = r
    out = dict(
        what="ORIGINAL ModelDB 168414 hoc network (A Fiber Inhibition folder), not the Python port",
        loaded_hoc=list(HOC), never_loaded=["mosinit.hoc", "Shell.hoc", "Shell_NoEP.hoc", "all save procedures"],
        scoring="WDR soma upward crossings of -30 mV in [1000+2000k, 3000+2000k) ms, k = 0..9",
        archive=arch, files=files, banned_token_scan=scan, banned_tokens=list(BANNED),
        data_equal_to_port_data=data_eq, mechanisms=mods,
        mechanisms_all_identical_after_crlf_normalisation=all(m["identical_after_crlf_normalisation"] for m in mods.values()),
        tstop_ms=T_SHORT, runs=runs, full_length_check=full,
        reviewer_table_dt_0_025=REVIEWER,
        matches_reviewer_dt_0_025={c: round(runs["0.025"][c]["mean"], 1) == REVIEWER[c] for c in REVIEWER}
        if "0.025" in runs else None)
    try:
        from importlib.metadata import version
        out["neuron_version"] = version("neuron")
    except Exception:
        out["neuron_version"] = None
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print(time.strftime("%Y-%m-%d %H:%M:%S ") + "wrote " + os.path.relpath(args.out, HERE), flush=True)
    if out["matches_reviewer_dt_0_025"] is not None and not all(out["matches_reviewer_dt_0_025"].values()):
        print("MISMATCH with the reviewer's table at dt 0.025: " + json.dumps(out["matches_reviewer_dt_0_025"]), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
