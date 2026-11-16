# Smoke run, 2 seeds: carries no verdict

This is a 2-seed, 5-null smoke run of `simulate_c008.py` (config: `seeds: 2`,
`n_null: 5`), kept only as a record that the script ran end to end. The script's
old default output path wrote it to the canonical `results/results.json`, and it
has been moved here so it cannot be mistaken for the result. Two seeds cannot
support a verdict: its grad1:C mean (1.047, 2 of 2 above 1.0) contradicts the
18-seed run, and is the kind of small-sample outlier that
`simulations/verdict.py` now refuses to turn into a verdict. The verdict run is
[`../main/results.json`](../main/results.json) (18 seeds, grad1:C mean 0.638).
