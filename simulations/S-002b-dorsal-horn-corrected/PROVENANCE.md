# Provenance for S-2b

S-2b reuses the S-2 port, mechanisms and data by import and does not copy or edit them:
`../S-002-dorsal-horn/PROVENANCE.md` is the provenance of `mod/` and `data/`, and of the model itself
(Zhang, Janik & Grill 2014, PMID 24790169, ModelDB 168414).

## What S-2b adds

`crosscheck_original_hoc.py` runs the **original** ModelDB 168414 hoc network (the port is not involved) so
that the port can be compared with it. ModelDB code is untrusted data. Handling, as enforced by the script:

- The archive is the same one as in S-2 (`master.zip` of the `ModelDBRepository/168414` mirror, sha256
  `ae2967d49b72243f569541c79b9e7a3c9d3d31b77abcf38c75c4c9ce12fa36cc`); the script refuses to continue on any
  other hash. It is put, with the extracted files, in a **new empty directory outside the repository** that is
  passed as an argument. Only exact member names are read from the zip (no `extractall`).
- Only `CellTemplates.hoc`, `MakeNetwork.hoc` and `RunSim_EP.hoc` of the `A Fiber Inhibition` folder are loaded.
  `mosinit.hoc`, `Shell.hoc`, `Shell_NoEP.hoc` and every save procedure are never loaded or called.
- Before anything is loaded each of the three files is scanned for `system(`, `popen` and `unix` (case
  insensitive) and for `load_file`/`xopen` calls other than the `nrngui` line; any hit stops the script. The
  `load_file("nrngui.hoc")` line is removed in a copy (`CellTemplates_ng.hoc`, `RunSim_EP_ng.hoc`), which is
  scanned again.
- Each simulation runs in a fresh child process (`python -I`, scrubbed environment) with the S-2 compiled
  mechanisms.

## Files the oracle reads, with hashes

The three hoc files and the data files they read, from `A Fiber Inhibition/` (sha256 of the original bytes;
they are also recorded in `results/oracle/original-hoc-crosscheck.json`):

| File | sha256 |
|---|---|
| CellTemplates.hoc | fb5c67adc20471be4c4b91f1ce3cd9f324d74b75220b107f0816978183fc9bbf |
| MakeNetwork.hoc | 3132e114808bf7a8475ad71425639f8cbee983f448f61cf544dd4289b419f1be |
| RunSim_EP.hoc | 5cadd9de0c3f5f10424c1fc159abd92e112575040098dab59b40184c169c0011 |

The remaining 20 data files (cell, coordinate, connectivity, weight, delay, threshold, spike and synapse-count
tables) are listed with their hashes in the script (`FILES`) and in the JSON.

## Checks the script makes and the JSON records

- The 17 `.mod` files in `S-002-dorsal-horn/mod/` equal the originals in `Critical Mod Files/` after CRLF
  normalisation (`mechanisms_all_identical_after_crlf_normalisation`).
- The connectivity, weight, delay and spike tables that the port reads (`S-002-dorsal-horn/data/`) equal the
  originals of the `A Fiber Inhibition` folder after CRLF normalisation (`data_equal_to_port_data`). The
  `A Fiber Inhibition` `WeightVector.txt` has CRLF line endings; its numbers are those of the `Foreman SCS`
  table the port uses.

## Differences between the oracle and the original run, declared

- The scored runs stop at 21 s (the scored cycles end there), not at the shipped 221 s; `--full-length` runs
  two conditions to the shipped length and the committed JSON shows that the per-cycle counts are the same.
- The shipped `loadqueue()` procedure is redefined with the same body plus a skip vector, to leave out the
  events of the dropped fibre classes. The recorders, `init()` and `run()` are the shipped `OutputData()`.
