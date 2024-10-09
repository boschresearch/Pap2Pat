# DESCRIPTION

## BACKGROUND

### Field of the Technology Disclosed

- define field of technology

### Description of Related Art

- introduce quantum computers
- motivate quantum chemistry applications
- describe ground state energy estimation
- limitations of current quantum circuits
- introduce variational quantum eigensolver
- limitations of VQE

## SUMMARY

- introduce disclosed technology
- describe quantum-classical algorithm
- estimate ψ0|O|ψ0 with high accuracy
- describe low-depth quantum circuit
- maximal Hamiltonian evolution time
- total evolution time
- number of times to run quantum circuit
- algorithm works for any observable
- quantum circuit variant of Hadamard test
- applications in quantum chemistry
- estimating transport properties
- extracting quantities from linear system
- combining with other methods

## DETAILED DESCRIPTION

- introduce quantum computers
- motivate need for solving problems with current quantum computer architecture
- describe algorithm for calculating ground state energy and properties
- illustrate system for ground state property estimation using hybrid quantum-classical computer system
- describe method for estimating ground state property of an observable
- highlight advantage of disclosed algorithm in high-accuracy estimation
- provide overview of disclosed technology

### Reduced Depth of The Quantum Circuit

- describe advantage of disclosed algorithm in reducing quantum circuit depth

### Example Embodiment of The Algorithm

- state theorem for estimating ground state property with high accuracy and low-depth
- describe implementation of algorithm using Hamiltonian simulation methods

### Comparison to the Straightforward Method

- describe straightforward approach of GSPE
- compare circuit depth of disclosed algorithm with straightforward approach

### Ground State Property Estimation Problem

- define ground state property estimation problem
- describe decision version of problem
- define search version of problem
- motivate need for prior information about Hamiltonian and its ground state
- define ground state property estimation problem with assumptions

### An Overview of the Low-Depth Ground State Energy Estimation

- state theorem for low-depth ground state energy estimation
- describe initial state preparation
- define density function and cumulative distribution function
- approximate cumulative distribution function using Fourier approximation
- estimate ACDF using parameterized quantum circuit
- describe method for estimating ground state energy using ACDF

### Example Algorithm for Commutative Case

- introduce commutative case
- define initial state
- define eigenbasis of O and H
- define Step 1: estimate ground state energy
- run procedure EstimateGSE
- define x* and p0
- construct xgood using spectral gap of H
- prove xgood is good for λ0
- estimate {tilde over (C)}(xgood) with additive error η/8
- define unbiased estimator for {tilde over (C)}(xgood)
- show variance of estimator
- reduce sample complexity using median-of-means trick
- define Step 2: estimate O-weighted CDF
- define quantum circuit for estimating O-weighted ACDF
- define unbiased estimator for O-weighted ACDF
- show variance of estimator
- define O-weighted "density function"
- define O-weighted CDF and ACDF
- prove O-weighted CDF can be approximated by O-weighted ACDF
- estimate p0O0 with multiplicative error
- estimate ground state property ψ0|O|ψ0
- summarize main theorem

### Summarizing the Main Theorem

- summarize main theorem

### Thus

- bound error of estimating ground state property
- choose ϵ0 and ϵ1
- conclude theorem

### Algorithm for General Unitary Observables

- state theorem for unitary observables
- introduce 2-d O-weighted density function
- define 2-d O-weighted CDF function
- justify definition of C0,2
- define 2-d O-weighted approximated CDF
- state lemma for approximation ratio of 2-d O-weighted ACDF
- prove lemma using F2 and H2
- bound error in F2 and H2
- define FL,2 and bound error
- define  and bound error
- prove first inequality of lemma
- define FR,2 and bound error
- prove second inequality of lemma
- describe parameterized quantum circuit
- introduce Hadamard gate H
- introduce phase gate S
- parameterize quantum circuit with t1, t2
- use quantum circuit to estimate 2-d O-weighted ACDF
- introduce algorithm for general unitary observables
- motivate estimation of ground state property
- define block-encoding of observable
- introduce Hadamard test for block-encoded observable
- estimate expectation value of observable
- define quantum circuit for estimation
- apply Hadamard gate
- apply controlled-unitary operation
- measure second register
- apply controlled-unitary operation again
- apply phase gate or identity
- apply Hadamard gate again
- measure first register
- define random variables X and Y
- show X is unbiased estimator of real part
- show Y is unbiased estimator of imaginary part
- introduce lemma for estimating 2-d O-weighted ACDF
- prove lemma
- introduce claim for constructing good point
- prove claim
- introduce algorithm for ground state property estimation
- analyze estimation error of algorithm
- maximize probability of success
- discuss handling non-unitary observables
- introduce theorem for ground state property estimation with block-encoded observable
- sketch proof of theorem
- define algorithm for general unitary observables
- derive unbiased estimator of ϕ0|e−iHtOe−iHt|ϕ0
- estimate (x, y) using modified algorithm
- analyze modified algorithm
- discuss applications of ground state property estimation algorithm
- introduce charge density application
- define one-particle reduced density matrix
- express 1RDM in terms of unitary operators
- estimate each entry of 1RDM using prior method
- obtain charge density function of ground state
- introduce quantum linear system solver application
- propose quantum algorithm to generate quantum state
- discuss shortcomings of existing quantum linear system solvers
- combine disclosed ground state property estimation algorithm with quantum linear system solver
- estimate properties of linear system solution
- analyze computation cost of second step
- discuss gap amplification technique
- define family of Hamiltonians
- analyze eigenvalues of Hamiltonians
- prepare state with Ω(1) overlap with |0|x(1)
- estimate x|M|x using Algorithm 3
- discuss advantages of disclosed algorithm
- discuss future directions for improvement
- discuss trade-off between maximal evolution time and total evolution time
- propose using amplitude estimation to reduce total evolution time
- discuss impact of error on algorithm performance
- introduce method for estimating ground state property of observable
- discuss initializing quantum component to initial state
- discuss various applications of method
- introduce quantum computing
- describe qubits
- explain qubit properties
- describe qudit
- introduce quantum gates
- explain single-qubit gates
- explain multi-qubit gates
- describe quantum circuits
- explain gate sequence
- introduce measurement feedback
- describe error correction
- introduce quantum annealing
- describe quantum annealing process
- explain initial and final Hamiltonians
- describe annealing schedule
- explain time-dependent Schrodinger equation
- describe final state measurement
- introduce postprocessing
- describe one-way quantum computing
- explain measurement-based quantum computing
- describe cluster state
- explain single-qubit measurements
- describe outcome of measurements
- introduce system architecture
- describe quantum computer components
- explain control unit
- describe control signals
- introduce measurement unit
- describe measurement signals
- explain qubit interconnections
- describe linear chain connection
- describe two-dimensional grid connection
- describe all-to-all connection
- introduce classical components
- describe beam splitter
- explain photodetector
- describe circuit QED implementation
- explain bus resonator
- describe superconducting circuits
- introduce trapped ions
- describe laser control
- explain NMR implementation
- describe RF antenna
- introduce anyons
- introduce quantum computer architecture
- describe control unit and qubits
- explain state preparation and gate application
- discuss measurement unit and measurement signals
- describe feedback signals and fault-tolerant quantum computing
- introduce initialization and reset operation
- explain gate control signals and quantum gate operations
- discuss application of gates and measurement operations
- describe repetition of measurement operations
- introduce hybrid quantum classical computer architecture
- describe classical computer component and memory
- explain classical processor and bus
- discuss input and output data
- describe quantum computer component and qubits
- explain classical state preparation signals
- discuss application of gate operations
- describe measurement output and classical state
- explain cooperation between classical and quantum computers
- discuss flexibility in function allocation
- introduce implementation in hardware and software
- describe emulation of quantum computer functions
- explain reference to states and basis states
- discuss implementation in computer programs
- describe features requiring computer implementation
- explain claims requiring computer-related elements
- discuss product claims and computer-related elements
- introduce programming languages and computer program products
- describe machine-readable storage devices
- explain processors and memory
- discuss storage devices and ASICs
- describe data structures and computer-readable medium
- explain optimization and approximation
- discuss limitations of optimization
- introduce algorithm for general unitary observables
- describe quantum circuits and shots
- explain state preparation and gate application
- discuss measurement operations and output
- describe repetition of operations

