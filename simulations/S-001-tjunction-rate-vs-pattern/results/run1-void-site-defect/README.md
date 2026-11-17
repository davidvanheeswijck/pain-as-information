# Run 1 of S-1: VOID (recording-site defect)

**Do not cite any number in this directory.** Kept so the history is honest.

In run 1 the recording site `stem_pre` was `stem(0.9)`. In the C-neuron the stem
is connected with `stem(0)` at the T-junction and `stem(1)` at the soma, so
`stem(0.9)` was at the **soma end**, on the far side of the stimulus at
`stem(0.5)`; in the Aβ comparator the connections are the other way round. What
run 1 called "evoked" (and therefore the steady-state drive threshold, the 201
"undrivable" exclusions, the ambiguity exclusion in `score()`, the lost-drive
reading, F and the Chao criterion (b)) tracked invasion of the soma, not drive
toward the junction or central axon. Found in review of PR #3; see Amendment H in
`../../PREDICTION.md`.

Run 1 started at 2026-11-17 00:09:08 and finished at 07:40 (CET). The per-model
files of every stage are in `per-model-files.zip`. The rerun writes to
`../main/`.
