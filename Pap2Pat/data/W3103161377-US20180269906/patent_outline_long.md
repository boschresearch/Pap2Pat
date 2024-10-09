# DESCRIPTION

## FIELD

- relate to quantum computing

## SUMMARY

- introduce magic state distillation protocols
- summarize protocol performance
- outline protocol embodiments

## DETAILED DESCRIPTION

### I. General Considerations

- introduce magic state distillation
- describe system components
- discuss method variations
- clarify terminology
- explain figure simplicity

### II. Introduction to Disclosed Technology

- motivate quantum computing
- describe fault-tolerant architectures
- introduce magic states
- discuss distillation protocols
- summarize prior art
- introduce disclosed protocol
- describe error suppression
- discuss asymptotic performance
- introduce other gate applications
- describe small instance performance
- discuss transversal gate implementation
- outline disclosure organization
- define notation conventions
- introduce Hadamard operator

### III. Basic Distillation Protocols

- introduce magic state distillation
- classify distillation protocols
- describe first class of protocols
- describe second class of protocols
- introduce example schemes
- describe stochastic error model
- introduce trivial outer code
- describe [[7,1,3]] inner code
- implement control-Hadamard
- describe Hadamard measurement routine
- analyze error patterns
- introduce [[17,1,5]] inner code
- describe H-measurement routine
- pipeline H-measurement routines
- introduce repetition outer code
- describe [[4,2,2]] inner code
- implement control-H⊗2
- describe quadratic distillation protocol
- introduce [[16,6,4]] inner code
- describe H-measurement routine
- pipeline H-measurement routines
- analyze error suppression
- describe modified distillation protocol
- simulate modified protocol
- describe circuit for modified protocol
- conclude repetition outer code

### IV. Third Level of Clifford Hierarchy

- introduce third level of Clifford hierarchy
- describe magic state for CCZ gate
- identify stabilizer operators
- define W operators
- describe example protocol for CCZ state distillation
- implement control-Swaps
- analyze error model
- conclude CCZ state distillation

### V. Inner Codes

- introduce inner codes
- define symmetric dot product
- define null subspace S
- prove lemma 1
- define symmetric matrix Λ
- state lemma 2
- prove lemma 2
- define (p,q)-magic basis
- state theorem 1
- introduce CSS codes from self-orthogonal matrices
- define X-stabilizer and Z-stabilizer
- choose magic basis for logical operators
- define logical operators
- state theorem 2
- define odd and even codes

### VI. Coding Theory and Asymptotic Performance

- introduce asymptotic properties of protocols
- define two limits of asymptotic performance
- state Theorem 3
- prove Theorem 3
- state Theorem 4
- prove Theorem 4
- define γ for concatenated protocols
- discuss triorthogonal codes and multilevel protocols
- conjecture γ<1
- discuss T-count efficiency of Theorem 3
- define error reduction degree d
- discuss initial distillation of magic states
- derive nT/nouter scaling
- discuss Theorem 4 using odd codes
- define inner code properties
- discuss effect of errors in T gates
- define measurement error
- introduce outer code properties
- define sensitivity of outer code
- prove Lemma 3
- define good rate and distance of codes
- define good sensitivity and check rate of outer codes
- prove Theorem 3 using inner and outer codes
- prove Theorem 4 using inner and outer codes
- discuss existence of inner codes with good rate and distance
- discuss existence of outer codes with good check rate and sensitivity
- define puncturing procedure for even codes
- discuss randomized construction of weakly self-dual CSS codes
- introduce Majorana fermion codes
- derive weakly self-dual CSS codes from Majorana codes
- discuss randomized construction of stabilizer codes
- define random ensemble of weakly self-orthogonal matrices
- state Lemma 4 for random self-orthogonal matrices
- introduce coding theory
- define asymptotic performance
- prove lemma 4
- prove lemma 5
- prove lemma 6
- introduce outer codes
- prove lemma 7
- define classical error correcting codes
- prove lemma 8
- construct explicit families of codes
- prove lemma 9
- discuss Tanner graphs
- discuss small Tanner graphs
- discuss numerical searches
- describe iterative randomized procedure
- describe additional random search
- test for distance 7
- discuss results of searches
- discuss outer codes with smaller values of m
- describe method for adding checks
- discuss results of searches
- discuss table I
- conclude coding theory
- conclude asymptotic performance
- conclude outer codes
- conclude overall

### VII. Numerical Simulation

- explain error model used for simulations
- introduce magic state fidelity
- define twirled state
- express error in terms of squared fidelity
- introduce stochastic error model
- explain difficulty of enumerating error patterns
- introduce alternative error model with random angles
- show equivalence of alternative model to stochastic error model
- discuss advantages of alternative model
- introduce [[16,2,4]] inner code
- explain modification of inner code to implement H-measurements
- discuss pipelining of [[16,2,4]] inner code
- introduce [[21,3,5]] inner code
- explain pipelining of [[21,3,5]] inner code
- discuss reduction of noisy T gate count
- introduce [[23,1,7]] inner code
- discuss pipelining of [[23,1,7]] inner code
- present results of simulations
- discuss asymptotic behavior of results
- emphasize importance of nouter in error probability

### VIII. Protocols at Intermediate Size

- introduce family of protocols for intermediate sizes
- discuss use of quantum BCH codes as inner codes
- explain construction of outer code
- discuss row and column checks of outer code
- introduce error correction scheme
- explain re-initialization of qubits in error-corrected rows
- discuss discarding of qubits in error-detected columns
- analyze output error rate
- discuss conditioning on detected errors
- show that output error is O(∈⁴)
- discuss success rate of protocol
- generalize protocol to three-dimensional grid
- introduce error correction in three-dimensional grid
- discuss application of error correction in columns
- explain discarding of qubits in error-detected vertical planes
- analyze output error rate in three-dimensional grid
- discuss success rate of three-dimensional grid protocol
- introduce modification of two-dimensional grid with diagonal checks
- discuss error correction in modified two-dimensional grid

### IX. Discussion

- discuss distillation protocols
- motivate small number of qubits
- compare with other protocols
- define trivial way to define new protocol
- explain T-gate circuit depth
- summarize space and time efficiency
- introduce example small inner and outer codes
- describe [[4,2,2]] inner code
- describe [[16,6,4]] inner code
- describe [[7,1,3]] inner code
- describe [[17,1,5]] inner code
- describe [[21,3,5]] and [[23,1,7]] inner codes
- explain puncturing of codes
- describe [[20,2,6]] code
- introduce other inner codes
- describe Petersen graph code
- explain proof of Lemma 9
- introduce example circuits
- describe FIG. 6
- describe FIG. 7
- describe FIG. 8
- describe FIG. 9
- discuss coincidence among protocols
- explain recursive formula
- introduce qudits
- define magic states
- use magic states for transformation
- derive transformation equation
- explain phase factor correction
- discuss interconvertibility of T gates
- introduce inner codes
- define stabilizer code
- discuss logical operators
- define transversal gate
- implement measurement of stabilizer
- deduce action of transversal gate
- implement controlled Clifford on logical qudits
- discuss implementation of C(SmX)
- consider equation and solution for C(SmX)
- implement simultaneous C(SmX) on all logical qudits
- discuss generalization to matrices over a field p
- introduce alternative construction from Reed-Muller codes
- discuss rate of resulting weakly self-dual code
- introduce outer codes
- discuss parity check matrix for outer code
- introduce check matrix from adjacency matrix of biregular graph
- introduce symmetric forms over finite fields
- classify quadratic spaces over fields of odd characteristic
- discuss Witt group of the field
- discuss quadratic spaces
- classify quadratic spaces up to hyperbolic planes
- prove diag(1, 1) is not hyperbolic
- show diag(1, 1) is congruent to diag(-1, -1)
- classify quadratic spaces by determinant of form
- state Lemma 10 about isometry of subspaces
- state Lemma 11 about orthogonal sum of null subspace and hyperbolic subspace
- prove Lemma 11
- state Lemma 12 about maximal null subspaces
- prove Lemma 12
- count null vectors in quadratic space
- state Lemma 13 about probability of null vectors
- prove Lemma 13
- estimate probability of Mv=0
- bound probability of v in Vc⊥ and v not in Vc
- bound probability of v in Vc⊥
- bound probability of v in Vc and v in Vc⊥
- conclude proof of Lemma 13
- introduce discussion
- derive probability equation
- bound probability factor
- combine probabilities
- illustrate computing environment
- describe processing device
- describe memory
- describe software
- describe storage
- describe input devices
- describe output devices
- describe communication connections
- describe computer-readable media
- describe program modules
- describe local or distributed computing environment
- illustrate network topology
- describe client-server network
- describe distributed computing environment
- illustrate system for implementing embodiments
- describe quantum processing units
- describe readout devices
- describe quantum processor controller
- describe classical processor
- describe compilation process
- describe remote computer
- describe cloud computing environment
- introduce general embodiments
- describe method for distilling magic states
- apply inner code
- use control-Swap operations
- apply outer code
- suppress errors
- describe inner code properties
- describe outer code properties
- describe error correcting codes
- describe magic state implementation
- describe quantum computing device
- describe concatenated circuit
- describe inputting magic states
- describe controlled-Hadamard operations
- illustrate method for distilling magic states
- apply inner and outer codes
- describe inner code properties
- describe outer code properties
- describe error correcting codes
- describe magic state implementation
- describe quantum computing device
- describe concatenated circuit
- conclude remarks

