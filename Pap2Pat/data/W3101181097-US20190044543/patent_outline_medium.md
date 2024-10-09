# DESCRIPTION

## SUMMARY

- motivate fault-tolerant error correction
- introduce flag EC protocols
- describe embodiments

## DETAILED DESCRIPTION

### I. General Considerations

- define conventions for singular and plural forms

### II. Introduction and Formalism

- motivate quantum computing
- introduce fault-tolerant error correction
- describe Shor EC
- describe Steane EC
- describe Knill EC
- introduce surface code
- discuss limitations of existing approaches
- introduce flag error correction
- discuss applications of flag EC
- outline structure of disclosure
- introduce flag FTEC for distance-three and -five codes
- introduce general flag FTEC protocol
- discuss flag circuit constructions
- provide examples of codes for flag FTEC
- outline numerical analysis of flag EC schemes

### III. Flag Error Correction for Small Distance Codes

- introduce flag error correction protocol
- motivate distance-(2t+1) codes
- define bad locations
- introduce flag qubit and extra CNOT gates
- define flags and measurements
- define t-flag circuit
- define υ-bad errors
- define stabilizer error correction
- introduce correction set
- outline flag 1-FTEC protocol
- illustrate tree diagram for flag 1-FTEC protocol
- apply flag 1-FTEC to Steane code
- introduce flag 2-FTEC with distance-5 codes
- define flag error set
- define flag 2-FTEC condition
- outline flag 2-FTEC protocol
- illustrate tree diagram for flag 2-FTEC protocol
- apply flag 2-FTEC to 19, 1, 5 and 17, 1, 5 color codes
- verify flag 2-FTEC condition for color codes

### IV. Flag Error Correction Protocol for Arbitrary Distance Codes

- introduce flag t-FTEC protocol
- define t-flag circuit
- define υ-bad errors
- define flag error set
- provide correction set
- motivate flag t-FTEC condition
- state flag t-FTEC protocol update rules
- state flag t-FTEC protocol corrections
- describe 1-flag circuit construction
- describe 2-flag circuit construction
- explain use of flag information
- define correction set with flag information
- state sufficient flag t-FTEC condition
- prove sufficient condition implies flag t-FTEC condition
- show surface codes satisfy sufficient condition
- show color codes satisfy sufficient condition
- show quantum Reed-Muller codes satisfy sufficient condition
- discuss codes that satisfy flag t-FTEC condition but not sufficient condition
- conclude section

### V. Circuit Level Noise Analysis

- demonstrate flag 2-FTEC protocol
- analyze logical failure rates of 19, 1, 5 color code
- compute pseudo-thresholds for three noise models
- compare flag FTEC schemes with Steane error correction
- analyze logical failure rates for various error correction methods
- compare flag FTEC with d=3 and d=5 surface codes
- discuss circuit depths and qubit overhead
- analyze pseudo-thresholds for flag FTEC and Steane EC
- discuss advantages of flag FTEC for early fault-tolerant experiments
- compute number of time steps for flag FTEC protocols
- discuss trade-offs between logical error rate and time steps

### VI. Review

- summarize flag t-FTEC protocol and its applications

### VII. Proof that the Flag t-FTEC Protocol Satisfies the Fault-Tolerant Criteria of Definition (2)

- prove Claim 1: flag t-FTEC protocol satisfies Definition 2
- analyze Case 1: same syndrome measured t+1 times with no flags
- analyze Case 2: no flags with ndiff=t
- analyze Case 3: t circuits flagged
- analyze Cases 4-6: various combinations of flags and faults

### VIII. Fault-Tolerant State Preparation and Measurement using Flag t-FTEC

- introduce fault-tolerant state preparation
- derive fault-tolerant measurement procedure
- describe flag t-FTEC protocol
- outline measurement repetition process

### IX. Quantum Reed-Muller Codes

- define Reed-Muller codes
- describe generator matrices
- derive dual of RM(1, m+1)
- define higher-order Reed-Muller codes
- derive X stabilizer generators of QRM(m)
- derive Z stabilizer generators of QRM(m)
- show rows(m)⊂rows(m−2,m)
- show every weight 2m−2 row has support within some weight 2m−1 row
- conclude every Z-type stabilizer generator has support within X generator
- describe implementation of Steane error correction
- describe fault-tolerant properties of Steane error correction
- compare Steane error correction with flag FTEC protocol
- describe logical failure rate of Steane error correction
- describe implementation of full Steane error correction protocol
- compare logical failure rates of full Steane error correction and flag FTEC protocol
- describe implementation of Surface Code Error Correction
- describe idealized noise model for Surface Code Error Correction
- describe minimum weight X-type correction for Surface Code Error Correction
- describe implementation of decoder for Surface Code Error Correction
- introduce quantum Reed-Muller codes
- describe flag fault-tolerant error correction methods
- illustrate flowchart for error correction protocol
- enumerate logical operators of stabilizer code
- determine joint support of stabilizers
- apply standard circuits for error correction
- try t-flagged circuits for each stabilizer
- determine flagged t-FTEC conditions
- apply error correction protocol
- repeat syndrome measurements
- track consecutive measurements
- modify counters for consecutive measurements
- repeat syndrome measurements using flag circuits
- apply correction based on syndrome measurements
- illustrate flowchart for error correction protocol
- perform fault-tolerant error correction using two ancilla qubits
- track consecutive measurements
- modify counters for consecutive measurements
- repeat syndrome measurements using flag circuits
- apply correction based on syndrome measurements
- illustrate flowchart for error correction protocol
- perform fault-tolerant error correction using one or more qubits
- describe example computing environments
- conclude remarks

