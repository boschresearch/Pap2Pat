# DESCRIPTION

## BACKGROUND

### Technical Field

- introduce quantum computing systems

### Description of Related Art

- limitations of classical binary computers

## SUMMARY

- motivate quantum noise reduction
- introduce quantum computing system
- describe qubit array
- describe quantum computing arrangement
- describe measuring device
- characterize variational quantum amplitude estimation process
- describe advantage of variational quantum amplitude estimation process
- optionally receive input data from physical system
- describe sequence of quantum operations
- describe output data
- optionally implement adaptive variational amplitude estimation process
- describe maximum likelihood process
- optionally implement iterative maximum likelihood process
- introduce method for operating quantum computing system
- arrange for qubit array
- configure quantum computing arrangement
- use measuring device
- characterize variational quantum amplitude estimation process
- optionally receive input data from physical system
- describe sequence of quantum operations
- describe output data
- optionally implement adaptive variational amplitude estimation process
- describe maximum likelihood process
- optionally implement iterative maximum likelihood process
- introduce computer program product
- describe non-transitory computer-readable storage medium
- describe computer-readable instructions
- describe executable method
- introduce third aspect
- describe hybrid quantum computing system
- describe technical solution
- describe advantage of technical solution

## DETAILED DESCRIPTION

### Introduction

- introduce computing hardware
- describe limitations of classical computers
- introduce quantum computers
- describe advantages of quantum computers
- describe challenges of quantum computers
- introduce quantum computing systems
- describe tandem configuration of classical and quantum computers
- describe technical problem of configuring quantum computers
- introduce embodiments of the present disclosure

### Quantum Computation System

- introduce quantum computing system
- describe input and output data
- describe classical computing system
- describe communication between classical and quantum computers
- describe electronic processor of classical computing system
- describe memory of classical computing system
- describe data sources
- describe sensor arrangements
- describe data processing by classical computing system
- describe configuration data
- describe optional data in quantum computer input data
- describe instructions for controller of quantum computer
- describe quantum computer
- describe qubits and quantum gates
- describe quantum circuits
- describe quantum noise reduction
- describe cryogenic temperatures
- describe photonic devices, cryogenic superconducting gates or ion traps
- describe data exchange between classical and quantum computers
- describe computer-executable instructions
- describe electronic hardware processors
- describe quantum amplitude estimation and/or amplification algorithms
- describe variational approximation algorithm
- describe quantum circuits configured based on input data
- describe processing of outputs by quantum computer
- describe sequence of shots
- describe initial states and quantum operations
- describe quantum circuit depth
- describe technical effect of quantum computing system

### Detail Description of Embodiments

- illustrate quantum computing system 10
- describe control system 20
- describe array of qubits 30
- describe configuration device 50
- describe process control device 60
- describe measuring device 70
- describe measurement data 80
- describe classical computing system
- describe quantum computer 130
- describe information representation by qubits
- describe vulnerability to noise and interference
- describe cooling to reduce thermal noise
- describe noise artefacts in qubits
- describe NISQ computer
- describe method for executing quantum computation
- assign initial values to qubits
- describe sequence of operations
- describe measurement phase
- describe depth of quantum circuit
- describe risk of decoherence and errors
- describe processing sensor signals
- describe signal processing using quantum circuit
- describe measurements at measuring device 70
- describe noise reduction in sensed data
- describe granted patent GB2559437B
- describe quantum circuit 120
- describe measuring device 70
- describe controlling quantum noise generation
- describe dividing sequences of quantum operations
- describe approximating quantum state
- describe Variational Quantum Amplitude Estimation (VQAE)
- describe Monte Carlo estimation
- describe beneficial configuration of measuring device 70
- describe quantum amplitude estimation (QAE)
- describe fixed-depth quantum circuits
- describe fine-tuning quantum gates
- describe reducing quantum noise
- describe learning strategy
- describe input data 101
- describe use applications of quantum computing system 10
- describe adaptive variational quantum amplitude estimation (AVQAE)
- describe rescaling algorithm
- describe AVQAE
- motivate noise reduction
- illustrate VQAE quantum circuit
- describe MLAE process
- illustrate amplitude estimation process
- describe VQAE process
- illustrate VQAE iterations
- describe computational task
- define expectation value
- illustrate solution encoding
- describe AVQAE process
- illustrate rescaling function
- describe variational cost reduction
- illustrate flow diagram
- receive input data
- prepare initial quantum state
- configure quantum circuit
- apply sequence of quantum operations
- measure qubit state
- determine amplitude estimation error
- check error threshold
- generate output data
- perform variational approximation
- determine variational state
- configure quantum circuit for next iteration
- repeat VQAE process
- control circuit depth
- describe total number of queries
- describe adaptive VQAE algorithm
- compare AVQAE with classical Monte Carlo method

### Example Implementation of VQAE and AVQAE

- introduce VQAE and AVQAE
- motivate amplitude estimation
- describe applications of amplitude estimation
- explain limitations of traditional amplitude estimation
- propose VQAE and AVQAE
- describe numerical results of VQAE and AVQAE
- compare VQAE and AVQAE with MLAE and classical MC sampling
- show advantage of VQAE and AVQAE
- outline structure of the patent application

### Section I

- define problem of interest
- explain quantum amplitude estimation
- explain classical MC sampling
- define expectation value
- introduce probability distributions
- define parameters for analysis
- encode solution on a quantum computer
- present quantum circuit
- define good state
- explain amplitude estimation algorithm
- discuss limitations of traditional amplitude estimation

### II. Variational Algorithms

- introduce VQAE formalism
- explain maximum likelihood framework
- describe variational step
- define likelihood function
- estimate phase θ
- minimize likelihood function
- define objective function
- describe parameterized quantum circuit
- explain variational update
- introduce gradient-based optimization
- describe Adam optimizer
- calculate gradient
- emulate Hadamard test
- calculate total number of queries
- describe sampling cost
- describe variational approximation cost
- introduce naïve VQAE
- describe initial state of PQC
- perform amplitude amplifications
- calculate infidelity
- show results for different depths
- show results for different m
- present amplitude estimation results
- compare with MLAE and MC sampling
- introduce adaptive VQAE
- describe rescaling of function f
- define new Grover operator
- estimate amplitude a'
- find renormalization factor r
- describe overlap between states
- perform VQAE with adaptive rescaling
- analyze performance of adaptive VQAE

### Section V. Discussion

- discuss quantum advantage of VQAE
- envision future applications
- discuss potential improvements
- conclude on VQAE algorithm

### Other Example Quantum Computing Systems

- illustrate quantum computing system 800
- describe classical computer 802 components
- describe quantum computer 808 components
- illustrate quantum computing system 900
- describe classical computer 908 components
- describe quantum computer 914 components
- illustrate distributed quantum computing system 1000
- describe classical computer 1002 components
- describe quantum computer 1010 components
- mention quantum computer variations

## EXAMPLE EMBODIMENTS

- introduce quantum computing system embodiments

### Group 1

- define quantum computing system with array of qubits and classical computing system
- describe first variational approximation
- describe output data generation
- introduce error threshold
- describe quantum amplitude estimation
- introduce parametrized quantum circuit
- describe adaptive rescaling algorithm
- introduce input data with real valued function and probability distribution
- describe maximum circuit depth independence
- introduce physical system data
- describe gradient based approximation
- describe second sequence of quantum operations
- introduce same number of quantum operations
- describe maximum likelihood amplitude estimation
- introduce iterative process
- describe iteration with MLAE and first variational approximation
- introduce Grover operator
- describe sequence of Grover operators
- introduce control system
- describe non-transitory computer-readable storage medium
- introduce method for operating computing system

### Group 2

- define quantum computing system with control system and quantum computer
- introduce input data representative of physical system
- describe adaptive rescaling algorithm
- introduce maximum likelihood amplitude estimation process
- describe iterative process
- introduce variational quantum approximation process
- describe method for operating computing system
- introduce non-transitory computer-readable storage medium
- describe method implementation

### Group 3

- define quantum computer with array of qubits and measuring device
- introduce input data representative of physical system
- describe adaptive variational amplitude estimation process
- introduce maximum likelihood process
- describe iterative process
- introduce variational quantum amplitude estimation process
- describe method for operating quantum computer
- introduce non-transitory computer-readable storage medium
- describe method implementation

## Terminology

- define including and comprising
- define singular and plural
- define at least one of
- define computer and computing-based device
- describe software execution
- describe storage devices
- describe dedicated circuit
- describe range and device value
- describe conditional language
- describe comprising and including
- describe or and at least one
- describe article usage
- describe at least one of list
- describe conjunctive language
- describe method operation order

