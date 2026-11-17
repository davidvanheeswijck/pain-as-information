# Provenance of the mechanisms and data in `mod/` and `data/`

## Source

- Model: Zhang TC, Janik JJ, Grill WM (2014) Modeling effects of spinal cord
  stimulation on wide-dynamic range dorsal horn neurons: influence of stimulation
  frequency and GABAergic inhibition. *J Neurophysiol* 112(3):552-67, PMID
  24790169, doi 10.1152/jn.00254.2014.
- ModelDB accession 168414, https://modeldb.science/168414 (submitter Tianhe
  Zhang; model last updated 2023-02-16 per ModelDB's metadata, "Updated 2/16/23 to
  include B_Adapt.mod" in the shipped README).
- The code was taken from the ModelDB mirror
  `https://github.com/ModelDBRepository/168414`, fetched as
  `https://github.com/ModelDBRepository/168414/archive/refs/heads/master.zip`
  (the ModelDB `/download/168414` route was not used; the first-choice rule was the
  mirror because `/download/<id>` can return an HTML 404 page).
- Downloaded 2026-11-17 (UTC) into a new empty directory outside this repository.
  `file` reported "Zip archive data"; 174 files; sha256 of the archive:
  `ae2967d49b72243f569541c79b9e7a3c9d3d31b77abcf38c75c4c9ce12fa36cc`.

## Terms

No LICENSE or terms file is in the mirror (searched the 174 files for `*license*`
and `*terms*`: none). The files are ModelDB-hosted research code, publicly
distributed by the model's authors through ModelDB. They are reproduced here as
unmodified mechanism and data files (apart from the line-ending conversion below)
for non-commercial research on a public programme, with attribution to the paper
above; no claim of ownership. If the authors or ModelDB ask for their removal,
remove them and the dependent code. I did not find a more specific statement of
terms and I am not stating one.

## Handling

The archive was unzipped and **every** `.mod` file this study uses and **every**
`.hoc` file of the three experiment folders (`WindUp`, `A Fiber Inhibition`,
`Foreman SCS`) was read before anything was compiled or run, together with the
data tables listed below. **No shipped `.hoc` script was executed and none is
used**: the four-cell network is rebuilt in Python (`dh_model.py`) from the
`CellTemplates.hoc` geometry and parameters, as read, and the data tables
below are read as plain numbers. The only `VERBATIM` blocks in the mechanisms are
`return 0;`; there is no `system`, `popen` or file call in any of them.

## What was copied, with hashes

`mod/` (the 17 mechanisms the three cell templates insert; `B_Adapt`, `HH2new` and
`vsource` are not used and were not copied). Line endings were converted from CRLF
to LF on the files marked "converted"; content is otherwise byte-identical. Hash
of the copy / hash of the original file in the archive.

| File | sha256 of the copy | sha256 of the original | Note |
|---|---|---|---|
| AMPA_DynSyn.mod | f4e7939cb1b4c1820c048e2f82f1bd5b2761bb3f6711aad197c52c0546e0cf3e | d91aa61d798d8a5cd2423f244fae15651792009c9e19d0be85d806e22412c148 | converted |
| NMDA_DynSyn.mod | 2b181d07360305e7eb1173b5fdc231181005d21349bf27b37e0cf0c9f3b16d2c | same | |
| GABAa_DynSyn.mod | 97e54fcc306e636f9e01c765cbe6667e1fd7e8f3d39001163d928fa89cde9ad3 | same | |
| Glycine_DynSyn.mod | 4f0046b5adcd53e56e2bdec0685aa812e33a5a1c45a324ac310be7a23db09603 | 5bd41347728ba63d131d8da5dc6061da2ea1cdfe04483a6334ef16ea071bfc29 | converted |
| NK1_DynSyn.mod | 37a9dc0024dc4d9fa4da5f4c5fc3436cc84b25aba287b906a6dada7246a7aa1b | same | |
| B_NA.mod | 473facaf00e8e2c867bf0b0746c3803c5bad11f2bc1001fccd9e86498841cb4c | b1dece3f95e6ec601669820e65f052b06ae5f7d09d321b05c6eeb71adf609a6d | converted |
| B_A.mod | 5f2d4cb7a752d9fcf23570eeb2e639238cc10b66632de672c2dce859246f7130 | 91df6814574a85fbbf1184e6f936ac4e22f546c38caa14ff637eb205d746f31c | converted |
| B_DR.mod | 1f342440efb1d7c9da804686405de9fd4e7ebb0f2e66ba7314b0ea92a1161efe | 55c204b1d587998198b81573a53a4256609de6231090bcdc6368f3c928064458 | converted |
| KDR.mod | d1df4cc3ea70979829056188f4df1d3862459a059e8cb25635d2fc024618434d | f5ee2d416b68b04019b88a43684373d1f51e00866c7a122602a64a520c4c92ad | converted |
| KDRI.mod | 87c5b8aaec13d38283f9fdbb94ac962ffd6785e6377f0cc5404c682a01594fc9 | e2f179c6bee86a1bcbe2368cc26b3fddc3196809bff927e9532aad06199c299f | converted |
| SS.mod | c762017426baf8b886e859203bb9d08db4710c3eefab3627d74bc25a03d30aea | 210ebd45d402872ab2c5880cd2d07a9e03ec6fdab4e2520aeef2ffa4344c6f8e | converted |
| HH2.mod | 8610826d2f69d7bae61780022490db020d5a5beeffbecb8caa396a404e1e27ba | same | |
| CaIntraCellDyn.mod | 60de5d5bd37460f7b3f40e8b42c54709ac4a654664dd8d2b7e179fe3e24e49f5 | same | |
| iKCa.mod | 7ef01e9f2129281b83aa4f3080c06203d1096c45f041eadf5b7221c105ec61c8 | same | |
| iCaL.mod | a75ea0dc85471bf2915b73a84b4a408b3349128d133484feb73077bbaada0ae1 | 9932e9ed633b8e77936c3e60a1f97984f756edd1d993016f0005b4ddae1930e2 | converted |
| iNaP.mod | a98b1c999960e9bf28ba7a8052cdcfca3c3ea2ad4532c14c5f803bad42b1f991 | same | |
| iCaAN.mod | f73d62a3795a60c55f6c0f82655a491d12b20eb14002901e8301bb3bc72f3115 | same | |

`data/` (plain-number tables; the originals were LF already, so each copy is
byte-identical to its original):

| File | Original path in the archive | sha256 |
|---|---|---|
| FromVector.txt | Foreman SCS/FromVector.txt (identical in the other two folders) | 3004e62bce84ed9509462c219a24aa53fc252e134654556225303e28fd764f28 |
| ToVector.txt | Foreman SCS/ToVector.txt | 3af10451d3a6d249077ea785eeb910870a0b32ad3900d303ebff57b614771cf5 |
| SynapseVector.txt | Foreman SCS/SynapseVector.txt | 3a05511a44d77cb592ed99e31b7d29596327aefe99246f3ce86538395e62ea4b |
| DelayVector.txt | Foreman SCS/DelayVector.txt | 8b920c4a04cef63743d03797dc62371f07b93990e35ec649a5459693f30e3f13 |
| WeightVector_foreman.txt | Foreman SCS/WeightVector.txt | 99902315b228a00159ad63f8650b3ecdb68fe68ebc57ee247d4d0b3fc4f4b7f4 |
| windup_SpikeTimesVector.txt | WindUp/SpikeTimesVector.txt | 4750899c8fdb914e032509475e190c5a1cdc03d556efacc5d51c6827b45c0c90 |
| windup_SpikeStatsVector.txt | WindUp/SpikeStatsVector.txt | 95edb3dff24abf1c9b54e2aae25bd95b0b11ac8a03753e710407fdffa3ea1467 |
| afib_SpikeTimesVector.txt | A Fiber Inhibition/SpikeTimesVector.txt | 6190ad7f892c3412b4ab286490329c843a6f01f5cbd7dbf20de6defab29a8013 |
| afib_SpikeStatsVector.txt | A Fiber Inhibition/SpikeStatsVector.txt | 354f929dcee46b769dc78b7a461ff673a618e053fb47197ccd165e85cd7babb5 |

The iCaL mechanism of the original is copied as-is; the note in the table on
`iCaL.mod` is the CRLF conversion only.

## Differences to be aware of

- The connectivity tables are the same in the three experiment folders; the
  weight tables differ only in rows 288 to 290 (the surround inhibition from SG
  cell 76, zero in `WindUp`, 0.007315 in the other two). This study uses the
  `Foreman SCS` weights (surround inhibition present).
- `ERevVector.txt` (six inhibitory connections at -70 mV, the rest 0 mV) exists
  in `Foreman SCS` but the loader for it is commented out in the shipped
  `MakeNetwork.hoc`; reversal potentials in the shipped network come from the
  templates (`e = -70` on the GABA-A synapses; glycine default -70).
- `README.txt` says each synapse has its own dummy `S_NetStim` source and that
  synapses with the same index on a cell correspond to one input fibre; here the
  fibre is the "From" index of the connection table (0 to 74), with the same
  spike train on every connection of a fibre.
