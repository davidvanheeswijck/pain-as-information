"""Mutation check for the S-3 tests.

Breaks one line at a time in a temporary copy of this folder (never in place),
runs the matching unit tests against the broken copy, and requires them to
fail by assertion, not by error. Exit 0 only if the untouched code passes and
every mutant is caught.

The `infogain.py` mutants need the standard library only. The verdict-rule
mutants import `simulate_s003.py` and so need numpy:

    simulations/.venv/bin/python simulations/S-003-generator-discrimination/mutation_check.py
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
MI = "terms.append(ph * p * math.log2(p / marginal[y]))"
AGREE = "final = label_t if label_t == label_w else vd.INCONCLUSIVE"
# (source file, test file, name, target line, replacement)
MUTANTS = [
    ("infogain.py", "test_infogain.py", "log base (log2 replaced by the natural log)",
     MI, "terms.append(ph * p * math.log(p / marginal[y]))"),
    ("infogain.py", "test_infogain.py", "normalisation (no division by the marginal)",
     MI, "terms.append(ph * p * math.log2(p))"),
    ("simulate_s003.py", "test_simulate_s003.py",
     "agreement requirement removed (decide alone names the side)",
     AGREE, "final = label_t"),
    ("simulate_s003.py", "test_simulate_s003.py",
     "agreement requirement removed (Wilson alone names the side)",
     AGREE, "final = label_w"),
]
FILES = ["infogain.py", "simulate_s003.py", "test_infogain.py", "test_simulate_s003.py"]


def run_tests(folder: Path, test_file: str):
    # -B: no bytecode cache. Two mutants of the same length written within
    # one second would otherwise share a stale .pyc and the second would
    # silently re-run the first.
    r = subprocess.run([sys.executable, "-B", "-m", "unittest", test_file],
                       cwd=folder, capture_output=True, text=True)
    lines = r.stderr.strip().splitlines()
    failed = [ln.split()[1] for ln in lines if ln.startswith("FAIL:")]
    errors = [ln.split()[1] for ln in lines if ln.startswith("ERROR:")]
    return r.returncode, lines[-1] if lines else "", failed, errors


def main() -> int:
    try:
        import numpy  # noqa: F401
    except ImportError:
        print("numpy is needed for the verdict-rule mutants; run with simulations/.venv/bin/python")
        return 2
    sources = {name: (HERE / name).read_text() for name in FILES}
    for src, _, name, target, _ in MUTANTS:
        if sources[src].count(target) != 1:
            print(f"mutation target for '{name}' not found exactly once; update mutation_check.py")
            return 2
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        # Same layout as the repository: verdict.py one level above the folder.
        work = Path(tmp) / "sim"
        work.mkdir()
        shutil.copy(HERE.parent / "verdict.py", Path(tmp) / "verdict.py")

        def restore():
            for name, text in sources.items():
                (work / name).write_text(text)

        restore()
        for test_file in ("test_infogain.py", "test_simulate_s003.py"):
            code, last, failed, errors = run_tests(work, test_file)
            print(f"unmutated, {test_file}: {last}")
            ok &= code == 0
        for src, test_file, name, target, replacement in MUTANTS:
            restore()
            (work / src).write_text(sources[src].replace(target, replacement))
            code, last, failed, errors = run_tests(work, test_file)
            caught = code != 0 and bool(failed) and not errors
            print(f"mutant, {name}: {last}; {len(failed)} assertion failure(s): "
                  f"{', '.join(failed)}; {len(errors)} error(s) -> "
                  f"{'caught' if caught else 'NOT CAUGHT'}")
            ok &= caught
    print("mutation check " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
