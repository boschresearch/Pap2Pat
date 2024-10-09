# DESCRIPTION

## BACKGROUND

- introduce quantum error correction codes

## SUMMARY

- motivate virtual quantum state distillation
- describe error-mitigated expectation value method
- summarize classical and quantum computer systems
- describe optional features of error-mitigated expectation value method
- specify noise experienced by each copy of noisy quantum state
- define entangled quantum state
- describe measurement process for error-mitigated expectation value
- describe normalization of expectation value
- specify parallel measurements
- describe application of cyclic shift operator
- describe advantages of error mitigation technique

## DETAILED DESCRIPTION

- introduce virtual distillation for mitigating errors in noisy quantum computation
- describe mathematical formulation of virtual distillation
- explain benefits of virtual distillation over other approaches

### Example Operating Environment

- introduce example system for performing virtual distillation
- describe quantum computing system obtaining multiple copies of noisy quantum state
- explain need for correcting expectation value in noisy quantum computation
- describe collective measurements on M copies of noisy quantum state
- introduce Equation (2) for corrected expectation value
- derive Equation (3) for computing numerator and denominator of Equation (2)
- prove identity of Equation (3) using cyclic shift operator
- describe quantum circuit for computing numerator and denominator of Equation (2)
- explain post-processing of measurement outcomes
- obtain error-mitigated estimation of expectation value
- describe variations of virtual distillation
- introduce example quantum computing system for performing virtual distillation
- describe qubit assembly and control and measurement system
- explain operation of qubit assembly and control and measurement system
- describe classical processor for performing classical computation operations

### Programming the Hardware: Virtual Distillation

- introduce process 300 for error-mitigated expectation value
- obtain multiple copies of noisy quantum state
- perform measurements on tensor products of M copies
- compute expectation value of target observable
- use computed expectation value to determine error-mitigated expectation value
- describe general application of virtual distillation
- introduce process 400 for virtual distillation with measurement by diagonalization
- obtain multiple copies of noisy quantum state
- define symmetrized version of target observable
- perform measurements on tensor products of 2 copies
- compute expectation values using measurement outcomes
- determine error-mitigated expectation value using computed expectation values

### Programming the Hardware: Selecting Different Virtual Distillation Protocols

- introduce process for selecting virtual distillation protocol
- determine feasibility of ancilla-assisted measurement
- determine if target observable is single qubit observable
- perform virtual distillation with serial measurements on two or more copies of noisy quantum state
- decompose target observable into tensor products of single-qubit operators
- perform serial measurements on tensor products of M copies of noisy quantum state
- apply diagonalization operators and measure outcomes
- compute error-mitigated expectation value of target observable
- perform virtual distillation with parallel measurements on two or more copies of noisy quantum state
- generalize protocol to higher powers of ρ
- perform virtual distillation with ancilla-assisted measurement on M=2 copies of noisy quantum state
- approximate numerator and denominator of Equation 8 using non-destructive measurement of swap operator
- generalize protocol to M>2 copies of noisy quantum state

### Mitigating Algorithmic Errors

- introduce error mitigation methods
- describe qDRIFT method
- explain randomized selection rule
- define Hamiltonian decomposition
- bound diamond norm distance
- describe virtual distillation technique
- apply virtual distillation to qDRIFT
- analyze Heisenberg Hamiltonian model
- show qDRIFT coherent cost reduction
- discuss implementation of digital and/or quantum subject matter
- define quantum computational systems
- describe digital and/or quantum computer programs
- explain data processing apparatus
- discuss digital and/or quantum computer-readable media
- describe control of systems
- provide general implementation details

