# Ethics and the privacy firewall

This programme is motivated by a real person living with a real disease. That
is a good reason to do the work carefully and a bad reason to relax any of the
following. Everything here is a constraint on the repository, enforced where it
can be enforced.

## 1. No patient data in this repository. Ever.

This repository is public and contains **no** identifiable or re-identifiable
health information. Specifically it must never contain:

- Names, initials, dates of birth, national or patient identifiers, insurance
  or dossier numbers, hospital record numbers, addresses.
- Named clinicians, named institutions treating an individual, appointment
  dates, admission dates, or dates of procedures for an individual.
- Laboratory values, imaging, reports, medication schedules or device serial
  numbers belonging to an individual.
- Any combination of the above sufficient to re-identify someone, which in a
  country the size of Belgium is a small combination.

Clinical motivation enters this repository only as **de-identified phenotype
description at population level**: for example "long-standing post-surgical
CRPS of the foot with a dorsal root ganglion stimulator showing declining
benefit" describes a class of patients found throughout the literature and
identifies nobody.

Any case-specific material lives outside this repository, on a private
machine, and is never committed here. `tools/lint-privacy.py` runs in CI and
fails the build on the obvious patterns. It is a backstop and not a licence to
be careless: the primary control is not writing it down here in the first
place.

## 2. Consent is required before an individual's data is used, even privately

A compilation of someone's medical record assembled from portals, mail and
calendars is a serious act even when done by a family member with good motives
and even when it never leaves a private disk. Before any case-specific material
informs this programme, the person it describes gives informed, specific,
revocable consent, and the consent record notes what was compiled, from where,
who can read it and how it is deleted on request.

If that consent has not been obtained, the correct state of this programme is
the state it is in now: general science only, no case file.

## 3. This is not medical advice and produces none

Nothing in this repository is a diagnosis, a treatment recommendation, a device
protocol or a stimulation parameter for use on a person. Conjectures are
addressed to researchers and to clinical trialists. Where a conjecture implies
something a clinician might do, it says so as a question to bring to a treating
team, never as an instruction.

Nobody should adjust an implanted device, a drug or a therapy on the basis of
anything here. The failure mode this clause exists to prevent is a plausible,
well-cited, wrong idea reaching someone who is desperate enough to try it, and
desperation is the normal state of the population this concerns.

## 4. No n-of-1 experimentation without a clinician and a protocol

Self-experimentation is how patient communities in refractory pain get hurt.
If this programme ever reaches something worth trying on a person, it goes
through a treating physician, a written protocol, an ethics review appropriate
to its risk, pre-registration, and a stopping rule agreed in advance. There is
no informal path.

## 5. Where the compute runs

Model calls default to an EU-hosted, zero-retention endpoint that does not
train on submitted text, and the runner verifies this against the router's own
metadata before spending a token rather than taking it on trust. Since no
patient data is submitted, this is not the main privacy control. It is the
cheap one, so it is on by default, and the verified provenance is stamped into
every verdict.

## 6. Honest failure is the deliverable

Refuted conjectures are committed, including the ones that were the author's
favourites, and `ledger/REFUTED.md` is part of the public record rather than a
private embarrassment. A research programme built around a family member's
illness has an obvious and powerful incentive to report progress that is not
there. The ledger, the pre-registered priors and the default-refute scoring
exist because of that incentive, not in spite of it.

If this programme concludes that the founding intuition was wrong, that
conclusion gets written up and published here with the same care as a success
would have been. That is the outcome the design should make easiest, because it
is the outcome that is most likely.
