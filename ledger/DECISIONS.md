# Decisions

Programme-level decisions with their reasons, so they can be revisited when the
reason changes rather than re-argued from scratch. Each one names the evidence
that would reverse it.

---

## D-001. Do not buy quantum computing capacity. 2026-09-01

**Decision.** The programme does not rent quantum hardware or quantum
simulation capacity, for chemistry, for ligand design, or for machine learning
on biosignals. Money that would go there goes to Branch A and to
instrumentation instead.

> **Note, 2026-09-01.** This decision was first written on material that was
> partly retracted hours later, after the reporting agent disclosed that it had
> asserted numbers from recall and had described a database search it never
> ran. **The decision has been rewritten to rest only on the verified subset,
> and it survives that rewrite comfortably.** The specific figures that were
> withdrawn are marked in `evidence/04-quantum-audit.md`. Recording this rather
> than quietly reissuing the file, because a decision record whose evidence
> changed without trace is worth less than no record.

**Why.** This was a real question and the evidence base was assembled partly to
answer it. It came back negative on the two plausible uses.

*For chemistry and ligand design.* The two rigorous fault-tolerant resource
estimates in this space are both metalloenzyme active sites, and both were
verified from the primary papers:

- Nitrogenase FeMoco (Reiher et al., *PNAS* 114:7555-7560, 2017): about
  **10¹⁵ T gates, 111 logical qubits, and 1.8 × 10⁸ physical qubits** at a
  10⁻³ error rate. The paper calls this "reasonable time on **small** quantum
  computers". A small quantum computer here is 180 million physical qubits.
- Cytochrome P450 (Goings et al., *PNAS* 119:e2203533119, 2022): about
  **2,158 logical qubits, 4.9 million physical qubits, 135 hours**.

Against that, the current hardware milestone is a surface code operating
**below threshold** with, in headline terms, **one** logical qubit. One against
one to four thousand is the whole argument, and it needs no further arithmetic.

The part that does not improve with hardware is the mismatch between what the
method prices and what pharmacology needs. Phase estimation gives **one energy
at one geometry in a fixed active space**. The quantities that matter here are
conformational and thermodynamic, requiring very many such energies over a
sampling problem where quantum computers have **no known advantage**.

That connects to a specific failure in this field's history. The Nav1.7 drugs
failed on **state dependence**: the sulfonamides bind the depolarised
conformation of voltage-sensing domain IV, while resting-state channels
dominate in uninjured tissue. That is a conformational sampling problem, which
is exactly the class a quantum computer does not help with. This point is from
E-03 and is independently sourced.

*For machine learning on biosignals.* The load-bearing argument is theoretical
rather than empirical, which is fortunate given what had to be withdrawn.
**Dequantisation results** (Tang, STOC 2019, arXiv:1807.04271; Chia et al.,
*JACM* 69(5), 2022) show that support vector machines and principal component
analysis admit classical sampling algorithms of comparable asymptotic cost.
Any regime in which a quantum kernel on dimensionally reduced biosignal data
would be exponentially fast is a regime a classical algorithm handles equally
fast. Separately, a 160-dataset benchmark across 12 quantum models found
out-of-the-box classical models systematically ahead (Bowles, Ahmed, Schuld,
arXiv:2403.07059, still an unrefereed preprint).

Full argument, with the retracted passages marked inline:
`evidence/04-quantum-audit.md` §3.2 and §3.3.

**What this decision does not say.** It does not say quantum technology is
irrelevant to the programme. Branch B remains open and is where Tier 3 money
should go: **optically pumped magnetometry** of nerve traffic. That is quantum
technology, it works today, and the benefit is geometric rather than
computational.

**Where simulation compute would actually help, since the question was asked in
the form of an offer.** The programme does have real compute needs. They are
all classical, and all of them are cheap by comparison:

1. **Biophysical modelling of the T-junction**, in NEURON or a comparable cable
   simulator. C-001 claims that ganglion stimulation works by amplifying
   T-junction filtering and that the effect decays under an unvarying stimulus.
   That is a multi-compartment model with Ca2+ and SK conductances, and it can
   be run to the point of making a quantitative, falsifiable prediction about
   which stimulus patterns restore filtering, **before** anyone spends the
   180,000 to 250,000 euro the animal experiment costs. This is the highest
   value compute in the programme by a wide margin, and it runs on a laptop
   overnight or a small cluster in an hour.
2. **Molecular dynamics on state-dependent sodium channel binding.** The
   Nav1.7 failure is a conformational sampling problem, which is exactly what
   ordinary MD is for and exactly what quantum computers do not help with. If
   the programme ever wants a view on subtype selectivity, this is the tool, and
   GPU hours are the resource.
3. **Forward magnetic modelling for Branch B.** Before buying a single
   magnetometer, model the expected field at a realistic standoff from a
   dispersed C-fibre volley, and find out whether phase cancellation kills the
   signal. That is a finite-element calculation, it costs almost nothing, and
   it could close the whole branch cheaply. It should be done first.
4. **Panel compute**, which is the harness itself and is the one recurring cost.
   Roughly thirteen model calls per conjecture on an EU-hosted router.

The ordering matters. Item 3 is a potential cheap kill on an entire branch and
should be run before any hardware is bought, in the same way triage should be
run before any panel is spent.

**What would reverse it.** Any one of:

- A published fault-tolerant resource estimate for a voltage-gated sodium
  channel binding free energy, end to end, landing under about 10⁵ physical
  qubits.
- A demonstrated quantum advantage on a conformational sampling or free-energy
  problem, as opposed to a ground-state energy.
- A replicated quantum machine learning result on real hardware beating a
  properly tuned classical baseline on a real biosignal dataset.
- Logical qubit counts above about 1,000 with sustained real-time error
  correction and no post-selection.

None of these is absurd. None is close.

---

## D-002. Branch B spends on helium-4 OPMs, not NV-diamond, and on superficial nerve, not the cord. 2026-09-01

**Decision.** Within Branch B, instrumentation effort targets **optically
pumped magnetometry of a superficial limb nerve**.

**Why.** Three numbers.

NV-diamond is about **1 pT/√Hz** in the biomagnetic band against a commercial
OPM's 7 to 15 fT/√Hz, so roughly **300 times worse** where it matters. Its only
femtotesla result is at 350 kHz, two to three orders above the band neural
signals live in. It has produced **no new single-neuron recording since 2016**,
and in 2026 still needs thousands of averaged heartbeats to recover a human
magnetocardiogram an OPM gets in one beat.

The peripheral nerve signal is **bimodal, and conflating the two modes is the
commonest error in this area**. A superficial nerve at 6.5 mm gives about
**1 pT** and has been recovered in humans with three sensors. A deep source
such as the cervical cord gives **5 to 50 fT** and needs 1,000 to 8,000
averages on a 132-channel sub-2 fT/√Hz SQUID array. Those are two problems a
factor of 100 apart.

And for the deep case a better sensor does not help, because **the averaging
requirement is set by biological and environmental interference, not by sensor
noise**. Anyone selling a quieter magnetometer as the fix for magnetospinography
is selling the wrong bottleneck.

Helium-4 OPMs are preferred over alkali despite costing about 13 times in
sensitivity, because they are the only class whose bandwidth (DC to 2 kHz)
clears the roughly 1 ms width of a compound action potential. Alkali OPMs run
150 to 350 Hz and hit exactly that wall.

**What would reverse it.** An NV sensitivity below about 100 fT/√Hz sustained
near DC, or an alkali OPM with usable gain above 1 kHz.

**The open risk this decision carries.** It is not established that
unmyelinated C-fibre traffic is reachable by magnetometry at all.
Magnetospinography has never detected even Aδ fibres, because conduction
velocity dispersion phase-cancels the compound volley, and C-fibres are ten
times slower again. That is the conjecture this branch turns on and it has not
yet been written.
