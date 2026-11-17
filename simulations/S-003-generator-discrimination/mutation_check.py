"""Mutation check for test_infogain.py. Standard library only.

Breaks `mutual_information` in a temporary copy of this folder (never in
place), runs the unit tests against the broken copy, and requires them to
fail by assertion. Exit 0 only if the untouched code passes and every mutant
is caught.

    python3 simulations/S-003-generator-discrimination/mutation_check.py
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = "terms.append(ph * p * math.log2(p / marginal[y]))"
MUTANTS = {
    "log base (log2 replaced by the natural log)":
        "terms.append(ph * p * math.log(p / marginal[y]))",
    "normalisation (no division by the marginal)":
        "terms.append(ph * p * math.log2(p))",
}


def run_tests(folder: Path):
    r = subprocess.run([sys.executable, "-m", "unittest", "test_infogain.py"],
                       cwd=folder, capture_output=True, text=True)
    lines = r.stderr.strip().splitlines()
    failed = [ln.split()[1] for ln in lines if ln.startswith("FAIL:")]
    errors = [ln.split()[1] for ln in lines if ln.startswith("ERROR:")]
    return r.returncode, lines[-1] if lines else "", failed, errors


def main() -> int:
    source = (HERE / "infogain.py").read_text()
    if source.count(TARGET) != 1:
        print("mutation target not found exactly once; update mutation_check.py")
        return 2
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        shutil.copy(HERE / "test_infogain.py", work / "test_infogain.py")
        (work / "infogain.py").write_text(source)
        code, last, failed, errors = run_tests(work)
        print(f"unmutated: {last}")
        ok &= code == 0
        for name, replacement in MUTANTS.items():
            (work / "infogain.py").write_text(source.replace(TARGET, replacement))
            code, last, failed, errors = run_tests(work)
            caught = code != 0 and bool(failed) and not errors
            print(f"mutant, {name}: {last}; {len(failed)} assertion failure(s): "
                  f"{', '.join(failed)}; {len(errors)} error(s) -> "
                  f"{'caught' if caught else 'NOT CAUGHT'}")
            ok &= caught
    print("mutation check " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
