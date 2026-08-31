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

**Why.** This was a real question and the evidence base was assembled partly to
answer it. It came back negative on all three plausible uses.

*For chemistry and ligand design.* Only two systems anywhere have rigorous
fault-tolerant resource estimates, and both are metalloenzyme active sites:
nitrogenase FeMoco and cytochrome P450. The cheapest published costs are
**1,000 to 3,700 logical qubits, around 2 to 8 billion Toffoli gates, and about
5 million physical qubits**. Against that, the best hardware in 2026 has **one**
genuinely below-threshold logical qubit and has executed at most **nine logical
T gates** in a fault-tolerant circuit. The gap is **four to seven orders of
magnitude** depending on the axis, and it is confirmed independently from the
hardware side: getting from a 1.4e-3 logical error rate to the 1e-10 these
algorithms need implies surface code distance around 50, so about 5,000
physical qubits per logical qubit, so about 10 million physical qubits.

Worse, and this is the part that does not improve with hardware: **there are
zero credible fault-tolerant resource estimates for any ion channel, membrane
protein, neurotransmitter receptor or binding free energy.** Not few. Zero. The
absence is structural. Phase estimation prices one energy at one geometry in a
fixed active space. The quantities that matter pharmacologically are
conformational and thermodynamic, needing 10⁴ to 10⁶ such energies over a
sampling problem where quantum computers have **no known advantage**.

That connects to a specific failure in this field's history. The Nav1.7 drugs
failed on **state dependence**: the sulfonamides bind the depolarised
conformation of voltage-sensing domain IV, while resting-state channels
dominate in uninjured tissue. That is a conformational sampling problem, which
is exactly the class a quantum computer does not help with.

And the field's flagship benchmark fell. In 2026, FeMoco was solved to chemical
accuracy **classically**, with the originating commentary noting the benchmark
model was "unrepresentatively easy to solve".

*For machine learning on biosignals.* No demonstrated advantage exists on real
hardware against a strong classical baseline. In the one properly controlled
head-to-head, using a Riemannian pipeline as comparator, the quantum classifier
scored **83% on training and 50.25% balanced accuracy on held-out data with an
F1 of 2.84%**, which on a binary task means it assigned every epoch to one
class. It ran roughly 14,000 times slower than the classical model that beat
it. Separately, dequantisation results prove that any regime in which a quantum
kernel on dimensionally reduced data would be exponentially fast is a regime a
classical sampling algorithm handles equally fast.

Full argument and citations: `evidence/04-quantum-audit.md` §3.2 and §3.3.

**What this decision does not say.** It does not say quantum technology is
irrelevant to the programme. Branch B remains open and is where Tier 3 money
should go: **optically pumped magnetometry** of nerve traffic. That is quantum
technology, it works today, and the benefit is geometric rather than
computational.

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
