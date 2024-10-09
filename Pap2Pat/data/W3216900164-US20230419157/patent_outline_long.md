# DESCRIPTION

## FIELD OF THE INVENTION

- relate to quantum computation

## BACKGROUND OF THE INVENTION

- introduce experimental progress in quantum computing
- discuss limitations of current approaches
- highlight challenges in manufacturing and calibrating qubits
- motivate need for new approach

## BRIEF SUMMARY OF THE INVENTION

- introduce novel approach to fault-tolerant quantum computation
- describe advantages of approach
- motivate shedding limitations of traditional assumptions
- introduce fault-tolerant protocol for generating cluster state
- describe compatibility with simpler physical realization
- compare to existing proposals for building cluster states
- discuss limitations of two-dimensional cluster states
- introduce special ancilla qubit and data qubits
- describe interactions between ancilla qubit and data qubits
- highlight fixed and periodic interactions
- discuss implementation using existing technologies
- analyze robustness against circuit errors and memory errors
- describe depolarizing model for circuit errors
- discuss effect of dephasing and qubit loss
- introduce threshold for circuit error rate
- describe logical error rate in absence of memory errors
- discuss logical error rate in presence of memory errors
- highlight separation between T and
- discuss advantages of hybrid system
- illustrate advantages of scheme
- discuss counterintuitive feature of protocol
- describe deliberate approach of interacting one qubit with many
- highlight fault-tolerance of protocol
- summarize features of scheme

## DETAILED DESCRIPTION OF THE INVENTION

- introduce fault-tolerant measurement-based quantum computation using cluster states

### BACKGROUND

- define cluster state
- introduce stabilizers of cluster state
- motivate importance of cluster states in fault-tolerant quantum computation
- describe Raussendorf, Harrington, and Goyal's scheme
- explain preparation of cluster state
- discuss fault-tolerant quantum computation using cluster state
- introduce space overhead and its limitations
- motivate need for low component overhead
- introduce surface code and its relation to cluster state

### Main Results

- introduce component overhead as a figure of merit
- motivate need for low component overhead
- construct abstract protocols for fault-tolerant quantum computation
- present concrete experimental proposals
- describe device for implementing protocols
- introduce control qubit and data qubits
- explain interactions between control qubit and data qubits
- describe measurement of data qubits
- introduce routers and their role
- describe detector implementations
- explain procedure for implementing fault-tolerant quantum computation
- discuss potential sources of noise
- address concern of error propagation
- discuss effect of time delays on memory error
- introduce error analysis section
- discuss threshold values for circuit error rate
- study effect of delay line errors
- argue for exponential suppression of logical error rate
- compare with other fault-tolerant quantum computing schemes

### Cluster State Preparation

- introduce cluster state preparation algorithm
- motivate bypassing calibration of multiple gates
- describe single ancilla interacting with data qubits
- define notation for Hadamard gate and Pauli operators
- explain Algorithm 1 for preparing cluster states
- define graphs G[k]' and their relation to subgraphs of G
- illustrate Algorithm 1 with example graph G
- explain generation of cluster states |ψG[k]' via Algorithm 1
- describe role of ancilla in generating cluster states
- explain application of Zj corrections
- discuss different orderings of qubits and their effects
- introduce 3D cluster states
- describe Protocol A for preparing cluster states on bcc lattice
- explain use of Algorithm 1 to prepare cluster state on cubic lattice
- describe measurement of qubits to obtain |ψG
- illustrate Protocol A with example circuit
- introduce Protocol B for preparing cluster states on bcc lattice
- describe application of Algorithm 1 to Gbcc
- explain labelling convention for bcc lattice
- illustrate Protocol B with example circuit
- describe nearest neighbors of qubits in bcc lattice
- divide qubits into groups Vxy, Vyz, and Vzx
- define Nbcc(i) and its relation to nearest neighbors

### Error Analysis

- introduce error analysis
- define noisy operations
- describe error propagation
- introduce effective errors
- define effective error
- analyze single-qubit errors
- analyze multi-qubit errors
- discuss error analysis for Algorithm 1
- prove geometric locality of effective errors
- discuss error analysis for Protocol A
- analyze X and Z errors in Protocol A
- discuss error analysis for Protocol B
- analyze X and Z errors in Protocol B
- discuss geometric locality of effective errors
- discuss error thresholds
- introduce Error Model 1
- describe depolarizing channels
- simulate error thresholds
- fit data to Eq. (12)
- estimate threshold circuit error rate
- compare to Ref. [14]
- discuss reasons for lower threshold in Protocol A
- introduce Error Model 2
- add detectable loss errors
- simulate error thresholds with loss
- fit data to quadratic curve
- estimate loss threshold
- compare to Ref. [28]
- discuss lower loss threshold in Protocol A
- discuss limitations of Error Model 2
- motivate revisiting delay line errors
- discuss experimental implementations
- discuss effect of delay line errors
- summarize error analysis results
- discuss implications for fault-tolerant quantum computing
- discuss open problems
- conclude error analysis

### Experimental Realization

- describe experimental realizations of protocols and devices
- focus on implementations in quantum nanophotonic and acoustic systems
- introduce single and double chains of one-dimensional cluster states
- adapt techniques to create cluster states on different graphs
- implement first step of Protocol A
- perform universal fault-tolerant quantum computation
- implement elementary operations in protocols
- coordinate interactions between emitter and data qubits
- perform error correction when loss rate is significant
- use device with single quantum emitter and photonic or phononic waveguide
- encode qubit degrees of freedom for emitter
- realize certain gates between emitter and photon or phonon
- introduce single-rail encoding scheme
- describe operation of single-rail encoding
- implement controlled-X gate in single-rail scheme
- implement controlled-Z gate in single-rail scheme
- introduce dual-rail encoding scheme
- describe operation of dual-rail encoding
- implement controlled-X gate in dual-rail scheme
- implement controlled-Z gate in dual-rail scheme
- explain implementation details for Protocols A and B
- control ordering of sequential interactions between emitter and data qubits
- perform intermediate measurements on emitter for Protocol B
- implement projective measurements on emitter
- re-initialize emitter in predetermined state
- discuss effect of delay line errors
- study two phenomenological models for delay line errors
- determine optimal logical error rate depending on delay line error rate

### Analysis

- study effect of delay line errors on logical error rate
- define Error Models 3a and 3b
- parameterize models using delay line error per time step
- assume time steps are equal
- define dephasing error and loss per time step
- comment on how delay line errors change analysis
- use depolarizing noise model with modification
- omit depolarizing channel after initialization of each data qubit
- define Error Models 3a and 3b
- estimate logical error rate for generating cluster state on LxLxL bcc lattice
- plot logical error rate vs. delay line error rate
- find optimal value L* of L that minimizes logical error rate
- make educated guess about scaling of logical error rate
- observe agreement with scaling
- fit data to equation
- determine break-even point for using delay lines

### Experimental Prospects

- introduce three experimental platforms
- describe optical domain
- discuss limitations of optical domain
- describe microwave photonics
- describe quantum acoustic systems
- discuss feasibility of quantum acoustic systems
- conclude experimental prospects

### Discussion

- summarize method for preparing cluster state
- compare with standard protocols
- discuss memory errors
- discuss logical error rate
- compare with anyon-based quantum computation
- compare with Gottesman-Kitaev-Preskill code
- discuss fault-tolerance property
- explain effect of single-qubit circuit-level error
- explain effect of m-qubit circuit-level error
- discuss general algorithm for preparing cluster states
- envision variations of the protocol
- discuss using flag techniques
- discuss trade-offs for improved error tolerance

### Alternative Algorithm

- introduce alternative algorithm
- structure of Algorithm 2
- define cluster state |ψG[k]′
- prove correctness of Algorithm 2
- define A_DD_j
- prove base case k=1
- prove inductive step
- apply A_DD_j to |ψG[k-1]′
- simplify expression
- prove correctness of Algorithm 2
- introduce correctness of Algorithm 1
- prove base case k=1
- prove inductive step
- consider two cases (k-1,k)∈E and (k-1,k)∉E
- apply HX, Z gates
- measure in Z-basis
- apply Z, if necessary
- obtain desired state |ψG
- conclude correctness of Algorithm 1
- analyze error propagation in Algorithms 1 and 2
- show effective error scales with maximum degree of G
- define geometric locality of effective error
- motivate error analysis for Algorithm 1
- prove Claim 1 for Algorithm 1
- define block of gates in Algorithm 1
- consider Z errors in Algorithm 1
- consider X errors in Algorithm 1
- consider X errors between gates in Algorithm 1
- consider X errors after re-initialization in Algorithm 1
- consider Xi errors in Algorithm 1
- summarize error analysis for Algorithm 1
- motivate error analysis for Algorithm 2
- prove Claim 2 for Algorithm 2
- define block of gates in Algorithm 2
- modify index sets for Algorithm 2
- consider X and Z errors in Algorithm 2
- summarize error analysis for Algorithm 2
- note limitations of Algorithm 2
- discuss Hamiltonian path in graph G
- discuss ordering of qubits in Algorithm 2
- note effective errors are geometrically local for certain graphs
- discuss maximum degree of graph G
- discuss error correction in quantum computing
- discuss application of Algorithms 1 and 2
- discuss thresholds for error correction
- discuss simulations for error correction
- discuss analysis of error correction
- conclude error analysis for Algorithms 1 and 2

