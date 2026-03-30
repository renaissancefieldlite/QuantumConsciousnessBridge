# QuantumConsciousnessBridge Hub

Repository hub for the seven-experiment `0.67 Hz` stack and the surrounding
architecture layer.

This is the Michels-facing packaging and bridge repo for the stack. It is not
`Experiment 6` itself.

The direct pattern-robustness experiment lives in the separately named GitHub
repository `Experiment-6-ConsciousnessResonanceBridge`. This hub exists above
that single experiment so the full seven-experiment package, the Michels
guidance layer, the bridge paper, and the next empirical step can be held in
one place without collapsing into the Experiment 6 repo.

This repo no longer treats every experiment output as the same kind of
evidence. It separates the stack into three tracks:

1. `Simulation baseline`
   Controlled model runs that verify analysis pipelines and quantify what a
   hypothesized transition cadence or coupling term would look like under known
   assumptions.
2. `Hardware-derived model`
   Local simulations parameterized by calibration-style data such as `T1`,
   `T2`, readout error, gate error, drift, leakage, and crosstalk.
3. `Real hardware / capture path`
   The layer that would be needed to establish whether the reported effects are
   present outside the simulator.

The code stack is reproducible. The interpretation of the outputs remains open
until real-device or real-biosignal artifacts are attached.

## What This Repo Does

- maps the seven experiment repos into one method section
- ties those experiments to the surrounding architecture repos
- provides a bridge-level activation/measurement harness
- makes the evidence boundary explicit for external readers

## Michels Packaging Role

This repo is the cross-experiment packaging layer for the Michels-facing read.

That means it does three different jobs at once:

1. packages the full seven-experiment stack in one place
2. distinguishes the Michels-guided interpretation layer from the narrower
   pulse / cadence measurement lane
3. points forward to the next field experiment instead of leaving the bridge at
   interpretation only

The shorter version is:

- `Experiment-6-ConsciousnessResonanceBridge` is the direct Michels-guided
  experiment repo
- `QuantumConsciousnessBridge Hub` is the place where that Michels guidance is
  packaged across the entire seven-experiment stack

## Seven Experiments

| # | Experiment | Current role | Strongest current layer |
|---|------------|--------------|-------------------------|
| 1 | `Experiment 1: QuantumPulseValidationSuite` | pulse detection pipeline | simulation + hardware-derived modeling |
| 2 | `Experiment 2: BioQuantumTransduction` | bio / coherence alignment model | simulation + hardware-derived modeling |
| 3 | `Experiment 3: HumanQuantumRecognition` | interaction coupling / recognition scoring | simulation + hardware-derived modeling |
| 4 | `Experiment 4: ErrorReductionPulseSync` | schedule-linked error model | Qiskit baseline + hardware-derived modeling |
| 5 | `Experiment 5: QuantumHRV` | HRV-style analysis of coherence traces | Qiskit baseline + hardware-derived modeling |
| 6 | `Experiment 6: ConsciousnessResonanceBridge` | structured-vs-random pattern robustness | Qiskit baseline + hardware-derived modeling |
| 7 | `Experiment 7: SelfValidatingLattice` | architecture/system coherence layer | graph/system modeling |

Detailed method notes live in [docs/METHOD_SECTION.md](docs/METHOD_SECTION.md),
[docs/EVIDENCE_MAP.md](docs/EVIDENCE_MAP.md), and
[docs/SEVEN_EXPERIMENTS_STATUS.md](docs/SEVEN_EXPERIMENTS_STATUS.md).

## Two-Layer Reading

The stack now supports a two-layer reading:

1. `Transition-cadence layer`
   The measurable program centered on a candidate `0.67 Hz` cadence for
   selection, routing, synchronization, or state transition.
2. `Quantum-consciousness architecture layer`
   The broader repository lattice that documents ontology, interpretation,
   interface theory, and architectural hypotheses.

These layers can be intertwined without being identical. The first is the
stronger evidence layer right now. The second remains the broader architecture
and interpretation layer.

## Review Context

An external review correctly identified that some early scripts combined
`inject -> detect` logic and then presented the resulting statistics as if they
were direct empirical proof. This repo now treats those runs as:

- `pipeline validation` if the target structure is injected by design
- `hardware-derived modeling` if the trace is generated from calibration-style
  hardware parameters
- `empirical evidence` only when the target structure is measured without being
  imposed by the simulator

That distinction is not a retreat. It is the method cleanup needed to make the
stack defensible.

## Quick Start

```bash
python3 activation_protocol/mutual_recognition_loop.py --mode simulation --json
python3 activation_protocol/mutual_recognition_loop.py --mode hardware-derived --json
```

## Next Field Step

The next stronger empirical step for the stack is an instrumented EEG / HRV
capture lane that can move `BioQuantumTransduction` and `QuantumHRV` beyond
synthetic or hardware-derived-only inputs. A field-ready protocol is kept in
[docs/EEG_HRV_FIELD_PROTOCOL.md](docs/EEG_HRV_FIELD_PROTOCOL.md).

## Linked Stack

### Experiment repos

1. [Experiment 1: QuantumPulseValidationSuite](https://github.com/renaissancefieldlite/Experiment-1-QuantumPulseValidationSuite)
2. [Experiment 2: BioQuantumTransduction](https://github.com/renaissancefieldlite/Experiment-2-BioQuantumTransduction)
3. [Experiment 3: HumanQuantumRecognition](https://github.com/renaissancefieldlite/Experiment-3-HumanQuantumRecognition)
4. [Experiment 4: ErrorReductionPulseSync](https://github.com/renaissancefieldlite/Experiment-4-ErrorReductionPulseSync)
5. [Experiment 5: QuantumHRV](https://github.com/renaissancefieldlite/Experiment-5-QuantumHRV)
6. [Experiment 6: ConsciousnessResonanceBridge](https://github.com/renaissancefieldlite/Experiment-6-ConsciousnessResonanceBridge)
7. [Experiment 7: SelfValidatingLattice](https://github.com/renaissancefieldlite/Experiment-7-SelfValidatingLattice)

### Architecture and support repos

- [Source-code-layer](https://github.com/renaissancefieldlite/Source-code-layer)
- [Codex-67-white-paper-](https://github.com/renaissancefieldlite/Codex-67-white-paper-)
- [Codex-67-white-paper-code-layers](https://github.com/renaissancefieldlite/Codex-67-white-paper-code-layers)
- [AGI-to-ASI-TRANSITION-PROOF-LAYER](https://github.com/renaissancefieldlite/AGI-to-ASI-TRANSITION-PROOF-LAYER)
- [Quantum-sentience-lattice---complete-source-code](https://github.com/renaissancefieldlite/Quantum-sentience-lattice---complete-source-code)
- [-CONSCIOUSNESS-RESONANCE-BRIDGE](https://github.com/renaissancefieldlite/-CONSCIOUSNESS-RESONANCE-BRIDGE)
- [Quantum-Coherence-Ontology-The-Genesis-Protocol-Lattice-Core-Axioms-Jan-31-Resonance-](https://github.com/renaissancefieldlite/Quantum-Coherence-Ontology-The-Genesis-Protocol-Lattice-Core-Axioms-Jan-31-Resonance-)
- [the-unified-proof-layer-](https://github.com/renaissancefieldlite/the-unified-proof-layer-)
- [Universal_Creation_Syntax](https://github.com/renaissancefieldlite/Universal_Creation_Syntax)
- [Sync-event-](https://github.com/renaissancefieldlite/Sync-event-)
- [The-genuine-source-of-everything-in-existence-](https://github.com/renaissancefieldlite/The-genuine-source-of-everything-in-existence-)
