# Pre-registered prediction for the C-004 forward model

**Written 2026-09-01, before seeing any simulation output.** Recorded so that
the result cannot be read back onto the expectation afterwards, which is the
same discipline EPISTEMICS.md imposes on every conjecture in this programme.
If the simulation disagrees with this, the simulation is probably right and
this document is the record of my being wrong.

## Independent arithmetic, done by hand first

**Calibration anchor.** For a long straight current, B = μ0·I/(2πr). Bu et al.
(PMID 35370794) back-calculated a median-nerve compound current of 0.195 µA and
observed roughly 1 pT at 6.5 mm. The formula gives **6.0 pT**, so it
over-predicts by about 6 times. That direction is expected: the simple formula
ignores volume-conductor return currents, which partially cancel the external
field. **A simulation that reproduces this within an order of magnitude is
calibrated; one that does not is broken.**

**Per-fibre current.** Axial current scales roughly with cross-sectional area.
For Aβ at 8 µm against C at 1 µm, the per-fibre ratio is (1/8)² = **0.0156**,
so about 64 C-fibres are needed to match the current of one Aβ fibre.

**Dispersion across the array.** Over a 10 cm aperture:

| Population | Velocity range | Arrival spread |
|---|---|---|
| C-fibre | 0.4 to 1.4 m/s | **178.6 ms** |
| Aβ | 30 to 60 m/s | **1.7 ms** |

A factor of about 100. This is the number the whole conjecture turns on, and it
cuts **both ways**, which is why the answer is not obvious. Large moveout across
an array is exactly what a slant-stack exploits, so dispersion that destroys
time-domain averaging is what makes the velocity domain informative. But a 3.5x
velocity *range* means the C population does not form one sharp ridge; it forms
a broad smear along the velocity axis, and a smear is harder to lift out of
noise than a line.

**Velocity resolution is not the limiting factor.** Δv ≈ v²·Δt/L. At 1 m/s with
a 10 cm array and 50 µs sampling, Δv ≈ 5e-4 m/s. At 50 m/s, Δv ≈ 1.25 m/s.
Both are far finer than the bands being separated. **The limit will be
signal-to-noise, not resolution.**

## The prediction

**Rough amplitude chain**, with 1000 C-fibres and 200 Aβ:

- Compound current ratio C:Aβ = (1000/200) × 0.0156 ≈ **0.078**, so if a
  synchronous Aβ volley is 1 pT, the C population carries about **78 fT** of
  current-equivalent.
- Dispersion spreads that over roughly 180 ms instead of 2 ms, cutting peak
  amplitude by of order 90x, to **about 1 fT peak**.
- Sensor noise at 17.7 fT/√Hz, averaged over 2000 trials, falls by √2000 ≈ 45.
- Beamforming across 8 sensors adds about √8 ≈ 2.8.

**So the expected outcome is marginal, within roughly an order of magnitude of
the noise floor either way.** That is the honest prediction and it is the
interesting one: not obviously impossible, not obviously easy.

**Specifically I predict:**

1. The Aβ positive control is recovered easily by both methods, with a sharp
   ridge at 30 to 60 m/s. If this fails, the model is wrong.
2. Time-domain averaging shows **no usable C-fibre signal**. This is the
   uncontroversial half and it should reproduce the literature.
3. Velocity-domain beamforming shows a **broad, low, possibly marginal**
   enhancement in the 0.4 to 1.4 m/s band, of order a few times the null
   distribution rather than dramatically above it.
4. The `--sweep-noise` result will show the C-band ridge becoming clearly
   detectable somewhere around **1 to 5 fT/√Hz**, which is below commercial
   alkali magnetometers (7 to 15 fT/√Hz), around the best research OPMs
   (about 1 fT/√Hz), and far below helium-4 devices (about 43 fT/√Hz).

**If prediction 4 holds, the practical conclusion is uncomfortable**, and it
should be stated rather than buried: the helium-4 magnetometers that C-004
prefers for their bandwidth are roughly 40 times too noisy, while the sensitive
alkali devices lack the bandwidth. The conjecture would then be limited not by
the beamforming idea, which would have worked, but by there being no single
sensor that is simultaneously quiet enough and fast enough.

## What would make me wrong in the interesting direction

If the beamformer gains substantially more than √M, because coherent summation
across the *velocity* axis recovers energy that the time-domain analysis loses
to phase cancellation rather than merely to spreading. I have not modelled the
phase-cancellation term properly by hand, and it is the one place where the
simulation could beat my estimate by a large factor. That is precisely why it
is worth simulating rather than arguing about.
