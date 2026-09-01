# The graveyard

Append-only. A refuted conjecture is closed with a reason, never deleted.

This file exists because a research programme without a graveyard is a random
walk: without it the loop rediscovers the same dead idea indefinitely, since
each round starts from the same priors that produced it the first time. It is
also read by gate 05 and gate 09 as context, so an entry here actively prevents
the next round from wasting itself.

It is public, and it includes the author's favourites. A programme built around
a family member's illness has an obvious incentive to report progress that is
not there, and this file is the counterweight. See ETHICS.md, clause 6.

## Format

Each entry:

```
### C-0NN — Title

**Refuted** YYYY-MM-DD by <gate or panel> · run `pipeline/reviews/C-0NN/<stamp>/`
**Prior** 0.NN → **Posterior** 0.NN

The killing argument, in the reviewer's own words where possible, with the
citation that carries it. Long enough that someone can tell whether a later
conjecture answers it or merely rephrases around it.

**Do not re-propose unless:** the specific condition that would revive it.
```

That last line is the useful part. Most refutations are contingent on something
being true of the world today. Saying what would have to change turns a dead
end into a standing bet.

---

### C-001 — Loss of benefit in chronic DRG stimulation is decay of T-junction filtering, not tolerance to charge

**Refuted** 2026-09-01 by five-laboratory panel · run `pipeline/reviews/C-001-drg-habituation-is-filter-fatigue/20260831T234656Z/`
**Prior** 0.25 → **Posterior** 0.15
Vote: 2 of 5 laboratories failed to refute. Median P across laboratories 0.15.

Two independent gates landed the same blow from different directions, and the
author had written the objection into the conjecture himself without noticing
it was fatal.

**The mechanism does not address the disease.** From the biological
plausibility gate, verbatim:

> The T-junction filtering mechanism is real but the conjecture treats C-fibre
> traffic as a labelled line for pain, which the evidence does not support; in
> established neuropathic pain the relevant traffic is on Aβ fibres and the
> relevant pathology is central, so gating C-fibre propagation at the
> T-junction does not address the mechanism of the disease.

This is HC-2's weak point arriving exactly where E-01 §5 said it would. Gating
nociceptor traffic is beside the point if the traffic that hurts is touch.

**The proposed experiment could not have distinguished the conjecture from its
own listed rival.** From the falsifiability gate: false-pass probability **0.5**
against the author's stated 0.15, because the killer measured C-fibre
conduction failure and never measured behavioural allodynia. The Rivals section
had said central compensation would be distinguished by "behavioural allodynia
returns while propagation failure holds steady" — a discriminator the Killer
section never actually measured. **The conjecture proposed a test it did not
specify.**

Not everything failed. Prior art returned PASS, genuinely open with a stated
delta: the idea is novel, the design was wrong. Physical plausibility returned
MINOR, asking for the homeostatic decay time constant and noting that the
entire 28-day crossover is void if filtering has not decayed by then in rat.
Clinical translation returned MINOR, noting that "vary pattern, not amplitude"
cannot be tested in a fully blinded reprogramming trial and would need a
pre-committed open-label design.

**Do not re-propose unless:** a design measures behavioural allodynia and
C-fibre propagation failure **in the same animals**, and a pilot first
establishes that T-junction filtering decays at all under chronic fixed-pattern
stimulation. The premise was never demonstrated; it was assumed. Both gates
that mattered said so independently.

**Caveat on this run, recorded because it affects how much weight the verdict
carries.** Two of eight gates failed on infrastructure (a 900 s timeout with a
retry loop that turned out to be dead for network failures), and the tally's
own gate parser was broken, so the FATAL/MAJOR logic never fired and the
verdict rests on the vote alone. All three bugs are fixed and the tally above
was regenerated with the corrected parser. The vote of 2 of 5 is unaffected.

---

### C-002 — Magnetic field modulation of antinociception is radical-pair mediated and shows a magnetic isotope effect

**Refuted** 2026-09-01 by a cheap-kill literature check ordered at triage · superseded by [C-006](../conjectures/C-006-flavin-13c-magnetic-isotope-effect.md)
**Prior** 0.12 → **Posterior** 0.05

Refuted **as written**. The underlying radical-pair question survives and is
carried forward; the ²⁵Mg implementation is dead.

**The objection that was raised was wrong.** Triage argued that ²⁵Mg is
quadrupolar and that fast relaxation in a distorted site would average the
hyperfine away. On the numbers it does not. The worst measured protein-bound
²⁵Mg relaxation in the literature is T₂ ≈ 31 µs in an enzyme ternary complex
with a deliberately strained coordination sphere, and 472 µs in the binary
complex (Ehrlich & Colman, PMID 7819280), against a radical-pair window of
about 1 µs. That is 30 to 470 times too slow to matter.

**Two better reasons killed it, and the gate missed both.**

*Magnesium has no unpaired spin density, so no hyperfine, so no magnetic
isotope effect is possible in principle.* Closed-shell Mg²⁺ cannot carry the
effect, so the design silently presupposed a Mg⁺• radical. That is precisely
the contested step: the magnesium isotope literature failed independent
replication (Crotty et al., PMID 22198842), with Hore's adjudication noting
"scant evidence that Mg has any biologically relevant redox chemistry"
(PMID 22307585). A null would therefore have been uninformative, which
**destroyed the conjecture's own claim to be decisive in both directions** —
the sole justification for filing a Branch C conjecture at all.

*The field range and the isotope were physically incompatible.* The ²⁵Mg⁺
hyperfine constant is −596.254376(54) MHz, about 21.3 mT, giving an effective
hyperfine field of order 63 mT. The conjecture proposed 10 µT to 1 mT: two to
four orders of magnitude apart. Every claimed magnesium effect in the
literature sits at 3 to 80 mT and none at microtesla, which should have been
the tell.

**Do not re-propose unless:** the isotope carries unpaired electron spin
density at a radical centre, the applied field range matches that isotope's own
hyperfine scale, and a null result would be interpretable. C-006 satisfies all
three by moving to ¹³C on flavin.

**Worth keeping for the method, not just the result.** The gate's objection was
wrong and the check it triggered was still worth running, because it surfaced
two fatal problems nobody had raised. A cheap kill is valuable even when its
stated reason is mistaken.
