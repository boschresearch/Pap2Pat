# DESCRIPTION

## BACKGROUND

- introduce quantum error correction codes

## SUMMARY

- motivate virtual quantum state distillation
- describe error-mitigated expectation value method
- outline classical and quantum computer systems
- summarize optional features of the method
- highlight advantages of the error mitigation technique

## DETAILED DESCRIPTION

- describe virtual distillation technique for mitigating errors in noisy quantum computation

### Example Operating Environment

- introduce example system performing virtual distillation
- describe quantum computing system obtaining multiple copies of noisy quantum state
- explain need for correcting expectation value in noisy quantum computation
- describe collective measurements on M copies of noisy quantum state
- derive equality for computing numerator and denominator of corrected expectation value
- describe quantum circuits for computing numerator and denominator
- outline post-processing of measurement outcomes to obtain error-mitigated estimation of expectation value

### Programming the Hardware: Virtual Distillation

- obtain multiple copies of noisy quantum state
- perform measurements on tensor products to compute expectation value
- compute error-mitigated expectation value of target observable
- describe general application of virtual distillation
- outline variations of virtual distillation process
- introduce virtual distillation with measurement by diagonalization

### Programming the Hardware: Selecting Different Virtual Distillation Protocols

- determine feasibility of ancilla-assisted measurement
- select virtual distillation protocol for single qubit observables
- describe limitations of symmetrized observables
- introduce non-symmetrized form for multi-qubit observables
- outline virtual distillation with serial measurements
- describe virtual distillation with ancilla-assisted measurement

### Mitigating Algorithmic Errors

- motivate randomized evolution methods
- describe qDRIFT method
- analyze error mitigation using virtual distillation
- present results of numerical investigation
- discuss implementation of digital and/or quantum subject matter
- define quantum information and data processing apparatus
- describe digital and/or quantum computer programs
- discuss control and implementation of systems

