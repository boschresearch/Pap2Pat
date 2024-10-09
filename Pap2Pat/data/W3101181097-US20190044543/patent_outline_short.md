# DESCRIPTION

## SUMMARY

- introduce fault-tolerant error correction

## DETAILED DESCRIPTION

### I. General Considerations

- define conventions and terminology

### II. Introduction and Formalism

- motivate quantum computing and error correction
- summarize recent progress in quantum computing
- introduce fault-tolerant error correction approaches
- describe Shor, Steane, and Knill error correction methods
- discuss surface code and minimum weight matching error correction
- motivate alternative approaches to fault-tolerant error correction
- introduce flag error correction and its advantages

### III. Flag Error Correction for Small Distance Codes

- introduce flag error correction protocol
- define bad locations and flag circuits
- define flags and measurements
- define t-flag circuits and υ-bad errors
- define stabilizer error correction and correction sets
- outline flag 1-FTEC protocol for d=3 codes
- apply flag 1-FTEC protocol to Steane code
- introduce flag 2-FTEC protocol for d>3 codes
- apply flag 2-FTEC protocol to 19, 1, 5 and 17, 1, 5 color codes

### IV. Flag Error Correction Protocol for Arbitrary Distance Codes

- introduce flag t-FTEC protocol
- define t-flag circuit
- define υ-bad errors
- define flag error set
- provide correction set
- describe flag t-FTEC protocol update rules
- describe flag t-FTEC protocol corrections
- provide circuit constructions for 1- and 2-flag circuits
- provide sufficient condition for flag t-FTEC and examples of satisfying code families

### V. Circuit Level Noise Analysis

- analyze 19, 1, 5 color code logical failure rates
- compute pseudo-thresholds for three noise models
- compare flag FTEC schemes with Steane error correction and surface codes
- discuss dependence of scheme performance on idle qubit failure rates
- summarize results and implications for fault-tolerant experiments

### VI. Review

- summarize flag t-FTEC protocol and its applications

### VII. Proof that the Flag t-FTEC Protocol Satisfies the Fault-Tolerant Criteria of Definition (2)

- prove that flag t-FTEC protocol satisfies Definition 2 for various cases
- show that protocol corrects errors and satisfies fault-tolerant criteria

### VIII. Fault-Tolerant State Preparation and Measurement using Flag t-FTEC

- prepare logical | state fault-tolerantly
- perform fault-tolerant measurements

### IX. Quantum Reed-Muller Codes

- define Reed-Muller codes
- derive generator matrices
- describe dual of RM(1, m+1)
- derive X stabilizer generators of QRM(m)
- derive Z stabilizer generators of QRM(m)
- show flag 1-FTEC condition
- describe construction of QRM(m) codes
- discuss properties of QRM(m) codes
- relate to Steane error correction
- introduce quantum Reed-Muller codes
- describe flag fault-tolerant error correction methods
- illustrate error correction protocol in flowcharts
- describe fault-tolerant error correction protocol using single ancilla qubit
- describe fault-tolerant error correction protocol using two ancilla qubits
- describe fault-tolerant error correction protocol using one or more qubits
- illustrate example computing environments
- describe storage and input/output devices
- describe communication connections
- illustrate network topologies
- describe distributed computing environment
- conclude remarks

