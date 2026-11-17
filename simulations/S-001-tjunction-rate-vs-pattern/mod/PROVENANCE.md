# Provenance of the mechanisms in this directory

## Source

- Model: Sundt D, Gamper N, Jaffe DB (2015) Spike propagation through the dorsal
  root ganglia in an unmyelinated sensory neuron: a modeling study.
  *J Neurophysiol* 114(6):3140-53, PMID 26334005, doi 10.1152/jn.00226.2015.
- ModelDB accession 187473, https://modeldb.science/187473 (submitter David B. Jaffe).
- The ModelDB direct-download URL (`/download/187473`) returned an HTML "page not
  found" in November 2026; the code is mirrored by ModelDB at
  `https://github.com/ModelDBRepository/187473`, fetched as
  `https://github.com/ModelDBRepository/187473/archive/refs/heads/master.zip`.
- Downloaded 2026-11-16 (UTC) into an empty directory outside this repository.
- sha256 of the archive: `c3aecf727e3cf1f1058a53b589d0fb00fa3ab74d4cba657325b66510d14fb014`
  (`187473.zip`, GitHub-mirror archive; see note below).
- Repository content dated 2024-10-01 ("Updated links and converted readme to markdown").

Note on the hash: the first download attempt (`/download/187473`) was a 10,575-byte
HTML error page with sha256 `877402907e06...`; it was discarded. The hash above is
that of the GitHub-mirror archive that was actually used.

## Handling

The archive was unzipped and **every** .mod, .hoc and .py file was read before
anything was compiled or run (README.md, mosinit.hoc, Figure5d/Figure5d.hoc,
Figure5d/Plot5d.py, Figure8c/Figure8c.hoc, Figure8c/Plot8c.py, and mods/*.mod).
No file does anything beyond defining channels, building the cell, writing a
`.dat` file and plotting; `mosinit.hoc` calls `system("python Plot5d.py")`, which
is why none of the ModelDB scripts were run. None of its .hoc or .py files is
used here: the cell is rebuilt in Python (`../tjmodel.py`) from the geometry and
densities in Figure5d.hoc and Figure8c.hoc.

## Files copied unmodified (byte-identical) from `mods/`

| File | Mechanism | Used for |
|---|---|---|
| nahh.mod | Na (Traub & Miles 1991; Cummins 2007, Sheets 2007) | Na, with the -6/+6 mV Nav1.7/1.8 shifts the hoc applies |
| kdr.mod | Borg-Graham delayed rectifier (`borgkdr`) | Kdr |
| im.mod | Yamada, Koch & Adams M-current (`iM`) | KCNQ/M |
| cal.mod | L-type Ca, Migliore 1995 | Ca entry for SK |
| SK.mod | SK, after Aradi & Holmes 1999 | Ca-dependent K |

Not copied: `fpump.mod`, `kexternal.mod`, `nadifl.mod` (Na/K pump, extracellular K,
Na diffusion). The paper's abstract states that pump and ion-accumulation effects
"had no effect on following frequency", and S-1 asks about following-frequency-type
filtering.

## Licence and terms

The ModelDB repository contains **no LICENSE file**. ModelDB's own terms state that
models are made freely available for research and require citation of the model's
paper; they are used here on that basis, with citation above. If a licence
statement is wanted, it must come from the authors.

## Aβ comparator

Not taken from ModelDB 51022 (Amir & Devor 2003). It is a generic node-and-internode
cell built in `../tjmodel.py` (class `ANeuron`) from the same `nahh` and `borgkdr`
mechanisms; nothing was downloaded for it.

## Compiling

`nrnivmodl` in this directory (with the project virtualenv on PATH) produces
`arm64/` or `x86_64/`, which are gitignored.
