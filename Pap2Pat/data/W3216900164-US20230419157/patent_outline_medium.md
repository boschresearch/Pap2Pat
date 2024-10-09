# DESCRIPTION

## FIELD OF THE INVENTION

- relate to quantum computation

## BACKGROUND OF THE INVENTION

- introduce experimental progress in quantum computing
- discuss limitations of current approaches

## BRIEF SUMMARY OF THE INVENTION

- introduce novel approach to fault-tolerant quantum computation
- describe advantages of the approach
- motivate the need for a new approach
- introduce the concept of a well-protected logical qubit
- describe the fault-tolerant protocol
- discuss the use of a special ancilla qubit
- explain the interaction between the ancilla qubit and data qubits
- describe the implementation of the protocol
- analyze the robustness of the protocol
- discuss the threshold for circuit error rate
- describe the advantages of the scheme
- summarize the benefits of the invention

## DETAILED DESCRIPTION OF THE INVENTION

- introduce fault-tolerant measurement-based quantum computation using cluster states

### BACKGROUND

- define cluster states
- motivate importance of cluster states in fault-tolerant quantum computation
- describe preparation of cluster states
- discuss limitations of existing approaches

### Main Results

- motivate low component overhead
- introduce abstract protocols for fault-tolerant quantum computation
- describe experimental proposals for realizing protocols
- illustrate physical device for implementing protocols
- describe procedure for implementing fault-tolerant quantum computation
- discuss potential sources of noise
- analyze error propagation
- discuss thresholds for circuit error rate
- mitigate effect of memory error

### Cluster State Preparation

- introduce cluster state preparation algorithm
- motivate bypassing calibration of multiple gates
- define algorithm for arbitrary graphs
- explain main idea of algorithm
- define graphs G[k]' and explain their role
- illustrate algorithm with example
- introduce 3D cluster states
- describe Protocol A for preparing cluster states on bcc lattice
- explain Protocol A's two main steps
- describe Protocol B for preparing cluster states on bcc lattice
- explain Protocol B's application of Algorithm 1 to Gbcc

### Error Analysis

- introduce error analysis
- define error propagation
- motivate geometrically local errors
- introduce effective errors
- define effective error equation
- analyze single-qubit Pauli errors
- show effective error is geometrically local
- analyze multiple Pauli errors
- show joint effect of multiple errors
- introduce effective errors for Protocols A and B
- analyze single-qubit errors in Protocol A
- show effective error is geometrically local in Protocol A
- analyze single-qubit errors in Protocol B
- show effective error is geometrically local in Protocol B
- discuss role of intermediate measurements
- introduce thresholds
- describe error models
- estimate threshold circuit error rates

### Experimental Realization

- describe experimental realizations of protocols and devices
- introduce quantum nanophotonic and acoustic systems
- describe deterministic generation of single photons and phonons
- describe coherent interactions with a single quantum emitter
- implement modified versions of the circuit in Ref. [35]
- prepare a three-dimensional cluster state on a cubic lattice
- perform universal fault-tolerant quantum computation
- implement elementary operations in protocols A and B
- coordinate interactions between the emitter and data qubits
- perform error correction when the loss rate is significant
- describe encoding schemes and elementary gates
- introduce single-rail and dual-rail encoding schemes
- implement controlled-X and controlled-Z gates
- describe implementation details for protocols A and B

### Analysis

- describe effect of delay line errors
- introduce error models 3a and 3b
- parameterize delay line error per time step
- assume equal time steps for operations
- describe dephasing and loss errors in delay lines
- estimate logical error rate for generating a cluster state
- infer effect of physical errors on final state
- discuss optimal logical error rate and scaling

### Experimental Prospects

- introduce experimental platforms
- discuss limitations of optical domain
- discuss microwave photonics and quantum acoustic systems

### Discussion

- summarize method for preparing cluster state
- compare with standard protocols
- discuss error rates and component overhead
- compare with GKP code
- discuss fault-tolerance property
- envision variations and alternate instantiations

### Alternative Algorithm

- introduce alternative algorithm
- define cluster state |ψG[k]′
- derive circuit for |ψG[n]′
- simplify circuit using Eq. (20)
- prove correctness of Algorithm 2
- prove Eq. (22) by induction
- prove correctness of Algorithm 1
- prove correctness of Algorithm 1 by induction
- conclude correctness of Algorithms 1 and 2
- analyze error propagation in Algorithms 1 and 2
- motivate geometric locality of effective errors
- define geometric locality for arbitrary graphs
- introduce error analysis for Algorithm 1
- prove Claim 1 for Algorithm 1
- analyze Z errors in Algorithm 1
- analyze X errors in Algorithm 1
- analyze Xi errors in Algorithm 1
- summarize error analysis for Algorithm 1
- introduce error analysis for Algorithm 2
- prove Claim 2 for Algorithm 2
- discuss limitations of Algorithm 2
- discuss special cases of Algorithm 2
- conclude error analysis for Algorithms 1 and 2

