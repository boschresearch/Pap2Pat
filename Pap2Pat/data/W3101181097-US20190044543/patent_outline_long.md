# DESCRIPTION

## SUMMARY

- motivate fault-tolerant error correction
- introduce flag circuits
- describe general constructions
- summarize example flag EC protocol
- describe embodiments of fault-tolerant error correction
- mention software implementation

## DETAILED DESCRIPTION

### I. General Considerations

- define singular and plural forms
- introduce notation conventions

### II. Introduction and Formalism

- motivate quantum computing
- introduce fault-tolerant error correction
- describe Shor EC
- describe Steane EC
- describe Knill EC
- introduce surface code
- discuss limitations of surface code
- introduce LDPC codes
- discuss flag error correction
- introduce recent work on flag error correction
- outline disclosed technology
- discuss applications of flag error correction
- introduce FTEC schemes
- discuss properties of FTEC schemes
- introduce flag FTEC
- outline sections III and IV
- introduce numerical analysis
- introduce noise model
- define weight-t Pauli operators
- define fault-tolerant error correction
- discuss first condition of FTEC
- discuss second condition of FTEC
- illustrate FTEC conditions
- discuss importance of second condition
- introduce depolarizing noise model
- describe two-qubit gate errors
- describe single-qubit errors
- describe idle qubit errors
- introduce logical failure rate
- describe Monte Carlo simulation
- define pseudo-threshold

### III. Flag Error Correction for Small Distance Codes

- introduce flag error correction protocol
- review Chao and Reichardt's approach for distance-three codes
- present protocol for distance-five CSS codes
- provide general remarks
- apply protocol to 19, 1, 5 color code
- apply protocol to 17, 1, 5 color code
- comment on circuit requirements for measuring stabilizer generators
- define flag 1-FTEC with distance-3 codes
- illustrate circuits for measuring operator ZZZZ
- define bad locations
- define flags and measurements
- define t-flag circuit
- define υ-bad errors
- define stabilizer error correction
- outline flag 1-FTEC protocol
- illustrate tree diagram for flag 1-FTEC protocol
- prove flag 1-FTEC protocol satisfies criteria
- discuss Steane code example
- specify stabilizer measurement circuits for Steane code
- verify flag 1-FTEC condition for Steane code
- introduce flag 2-FTEC with distance-5 codes
- discuss complications for codes with d>3
- illustrate tree diagram for flag 2-FTEC protocol
- define flag error set
- define correction set
- state flag 2-FTEC condition
- define update rules for counters ndiff and nsame
- outline flag 2-FTEC protocol
- illustrate examples of flag 2-FTEC applied to d=5 codes
- show 2-flag circuits with minimal number of flag qubits and CNOT's
- apply flag 2-FTEC protocol to 19, 1, 5 color code
- apply flag 2-FTEC protocol to 17, 1, 5 color code
- verify flag 2-FTEC condition for 19-qubit and 17-qubit color codes
- discuss sufficient condition for flag 2-FTEC condition
- provide numerical verification of flag 2-FTEC condition
- discuss errors in sets {tilde over (E)}22 and {tilde over (E)}12
- illustrate sets {tilde over (E)}m2 for 19-qubit code
- implement flag 2-FTEC protocol following Section III B and FIG. 5

### IV. Flag Error Correction Protocol for Arbitrary Distance Codes

- introduce flag t-FTEC protocol
- define t-flag circuit
- define υ-bad errors
- define flag error set
- provide correction set
- motivate flag t-FTEC condition
- state flag t-FTEC protocol update rules
- describe flag t-FTEC protocol corrections
- introduce circuits
- describe 1-flag circuit construction
- describe 2-flag circuit construction
- use flag information
- define correction set with flag information
- introduce sufficient condition
- state sufficient flag t-FTEC condition
- prove sufficient condition implies flag t-FTEC condition
- introduce surface codes
- show surface codes satisfy sufficient condition
- introduce color codes
- show color codes satisfy sufficient condition
- introduce quantum Reed-Muller codes
- show quantum Reed-Muller codes satisfy sufficient condition
- discuss Hamming codes
- discuss codes that satisfy flag t-FTEC condition but not sufficient condition
- provide example of 5, 1, 3 code
- provide example of Hamming codes
- discuss application of flag t-FTEC protocol
- discuss fault-tolerant preparation and measurement of logical states
- discuss use of flag t-FTEC protocol in Section VIII
- discuss general 1-flag circuit construction
- discuss general 2-flag circuit construction
- discuss use of extra flag qubits
- discuss reduction of correction sets
- discuss sufficient condition for surface codes
- discuss sufficient condition for color codes
- discuss sufficient condition for quantum Reed-Muller codes
- discuss limitations of sufficient condition
- discuss examples of codes that satisfy flag t-FTEC condition
- conclude section on flag error correction protocol

### V. Circuit Level Noise Analysis

- introduce flag 2-FTEC protocol
- analyze logical failure rates of 19, 1, 5 color code
- compute pseudo-threshold for three noise models
- describe full circuit-level noise analysis
- detail stabilizer measurement circuits
- compare logical failure rates of various FTEC schemes
- show results for 5, 1, 3 code and Steane code
- discuss pseudo-thresholds and required time-steps
- analyze flag-FTEC methods applied to 5, 1, 3 code
- compare flag-FTEC with d=3 surface code and Steane-EC
- discuss impact of idle qubit errors on pseudo-threshold
- describe circuits for measuring stabilizers of 5-qubit code
- compare flag-FTEC with d=5 surface code and Steane-EC
- analyze logical failure rates for distance-five codes
- discuss differences in slopes of logical failure rate curves
- explain non-zero (p2) contributions to logical failure rates
- detail fault-tolerant properties of Steane-EC
- compare flag-2 FTEC with Steane-EC applied to 19, 1, 5 code
- discuss regime where flag-2 FTEC achieves lower logical failure rates
- analyze pseudo-threshold of flag-EC applied to 19, 1, 5 color code
- compare 19, 1, 5 color code with d=3 schemes
- discuss time steps involved in flag error correction
- highlight advantages of flag-FTEC methods

### VI. Review

- summarize flag t-FTEC protocol
- highlight usefulness of flag t-FTEC for near-term quantum devices

### VII. Proof that the Flag t-FTEC Protocol Satisfies the Fault-Tolerant Criteria of Definition (2)

- state claim and assumptions
- define benign fault
- describe Case 1: same syndrome measured t+1 times with no flags
- describe Case 2: no flags and ndiff=t
- describe Case 3: set of t circuits flagged
- describe Case 4: m circuits flagged with nsame=t−m+1
- describe Case 5: m circuits flagged with ndiff=t−m
- describe Case 6: m circuits flagged with ndiff=k and nsame=t−m−k+1
- summarize correction process
- conclude that flag t-FTEC protocol satisfies fault-tolerant criteria

### VIII. Fault-Tolerant State Preparation and Measurement using Flag t-FTEC

- introduce fault-tolerant state preparation
- motivate flag t-FTEC condition
- define stabilizer code C
- prepare encoded | state
- apply flag t-FTEC protocol
- measure eigenvalue of logical operator
- describe fault-tolerant measurement procedure
- correct errors during measurement

### IX. Quantum Reed-Muller Codes

- define Reed-Muller codes
- describe generator matrices
- derive dual of RM(1, m+1)
- define higher-order Reed-Muller codes
- derive X stabilizer generators of QRM(m)
- derive Z stabilizer generators of QRM(m)
- show rows(m)⊂rows(m−2,m)
- show weight of rows
- show support of Z-type stabilizer generators
- describe Steane error correction
- introduce CSS codes
- describe syndrome extraction
- describe X stabilizer generators measurement
- describe Z stabilizer generators measurement
- explain fault-tolerant properties
- describe ancilla states verification
- describe X errors detection
- describe Z errors detection
- compare Steane error correction with flag FTEC
- describe logical failure rates computation
- describe full Steane error correction protocol
- describe flag FTEC scheme
- compare pseudo-thresholds
- describe implementation of Steane error correction
- describe implementation of flag FTEC
- describe rotated surface code
- describe idealized noise model
- describe X-type error correction
- describe graph G2D
- describe minimum weight decoder
- describe circuit noise model
- describe measurement qubits
- describe implementation of decoder
- describe graph G3D
- describe simulation of surface code
- describe compact implementation of flag error correction
- describe flag-EC protocol using two ancilla qubits
- describe flag-EC protocol using four ancilla qubits
- introduce quantum Reed-Muller codes
- describe flag fault-tolerant error correction methods
- illustrate flowchart for error correction protocol
- enumerate logical operators of stabilizer code
- determine joint support of stabilizers
- apply standard circuits for error correction
- try t-flagged circuits for each stabilizer
- determine flagged t-FTEC conditions
- apply error correction protocol
- repeat t-flagged circuits for each stabilizer
- track consecutive measurements
- modify counters for consecutive measurements
- repeat syndrome measurements using flag circuits
- apply correction based on syndrome measurements
- illustrate flowchart for error correction protocol
- perform fault-tolerant error correction protocol
- track consecutive measurements
- modify counters for consecutive measurements
- repeat syndrome measurements using flag circuits
- apply correction based on syndrome measurements
- illustrate flowchart for error correction protocol
- perform fault-tolerant error correction protocol
- track consecutive measurements
- modify counters for consecutive measurements
- repeat syndrome measurements using flag circuits
- apply correction based on syndrome measurements
- describe example computing environments
- illustrate computing environment
- describe processing device and memory
- describe storage and input/output devices
- describe communication connections
- describe software for synthesizing circuits
- illustrate network topology for client-server network
- describe computing device and network
- illustrate network topology for distributed computing environment
- describe computing device and network
- describe distributed computing environment
- illustrate system for implementing quantum computing
- describe quantum processing unit and readout device
- describe quantum processor controller and subcontrollers
- describe compilation of quantum computer circuit description
- describe remote computer and communication connections
- describe cloud computing environment
- describe modification of illustrated embodiments
- describe combination of technologies
- describe implementation of procedures and functions
- describe particular arrangements
- describe other arrangements
- conclude remarks

