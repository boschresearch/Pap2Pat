# DESCRIPTION

## FIELD OF INVENTION

- define field of invention

## BACKGROUND

- motivate quantum computers
- describe importance of ground state energy estimation
- limitations of known algorithms

## SUMMARY

- introduce ground state energy estimation
- motivate importance of ground state energy estimation
- describe disclosed technology
- summarize advantages of disclosed technology
- application of disclosed technology
- significance of disclosed technology

## Prior Approaches

- describe quantum phase estimation
- limitations of quantum phase estimation
- describe variational quantum eigensolver
- limitations of variational quantum eigensolver
- describe third known method

## DETAILED DESCRIPTION

- describe ground state energy estimation using present-generation quantum technology

### Overview

- illustrate computer system structure
- describe hybrid quantum-classical computer implementation
- outline method for ground state energy estimation

### Early Fault-Tolerant GSEE Algorithms

- illustrate maximal evolution time vs. total evolution time

### The GSEE Algorithm

- introduce problem formulation
- describe Hadamard test circuit
- formulate ground state energy estimation problem
- discuss limitations of previous methods
- motivate need for low-circuit-depth algorithm
- outline approach for efficiently evaluating convolution

### Previous Early Fault-Tolerant GSEE Methods

- describe approach to estimating ground state energy
- define spectral measure and convolution
- discuss limitations of previous methods
- outline approach to evaluating convolution
- discuss runtime costs of previous methods

### Overcoming the 1/ϵ-Depth Barrier

- motivate need for low-Fourier-degree filter function
- describe properties of desired filter function
- introduce Gaussian filter function
- discuss advantages of Gaussian filter function
- outline approach to estimating convolution
- discuss complexity of algorithm

### A Universal Approach for the Convolution Evaluation

- motivate need for sample-efficient method
- describe approach to evaluating convolution
- outline sampling strategy
- discuss sample complexity

### Reducing tot via Gaussian Derivative Filtering

- motivate need for improved filter function
- introduce Gaussian derivative filter function
- discuss advantages of Gaussian derivative filter function

### Estimating Ground State Energy via Gaussian Derivative Filtering

- define Gaussian derivative function
- derive properties of Gaussian derivative function
- convolve spectral measure with Gaussian derivative filter
- prove desirable property of convolution
- approximate Gaussian derivative function with band-limited function
- apply approximation to efficient evaluation of convolution
- provide lemma for choosing σ

### Part I.

- define mathematical equation
- bound first term in equation
- bound second term in equation
- combine bounds to obtain result
- define another mathematical equation
- bound first term in second equation
- bound second term in second equation
- combine bounds to obtain result
- prove lemma
- introduce strategy for ground state energy estimation
- state lemma 3
- prove lemma 3
- introduce random variables generation
- describe GSEE algorithm
- introduce band-limited version of gσ
- describe data structure ConvEval
- define gσ,T
- prove Lemma 4
- state Claim A
- prove Claim A
- introduce complexity of evaluating convolution
- describe evaluating convolution via Hadamard tests
- define function fT
- define probability density v
- define random variables Xt and Yt
- define random variable Z(x)
- prove coincidence of expressions
- derive sample complexity of convolution evaluation
- define empirical mean of samples
- apply Hoeffding's inequality
- use triangle inequality and union bound
- relate to expectation of Z(xj)
- apply Lemma 1
- redefine j for real fT
- illustrate ConvEval data structure
- illustrate GSEE algorithm
- describe method for estimating ground state energy
- specify quantum computing component
- specify classical computing component
- store computer instructions
- derive outcome samples from Hadamard tests
- evaluate convolution of spectral measure and filter function
- infer estimate of ground state energy
- describe physical system
- specify fault-tolerant quantum computer
- specify low-depth quantum circuit
- select target accuracy
- relate depth to inverse spectral gap and target accuracy
- infer property of Hamiltonian
- describe hybrid quantum-classical computer system
- specify quantum computing component
- specify classical computing component
- store computer instructions
- describe various physical embodiments of a quantum computer
- define quantum circuit
- specify quantum gates
- describe gate sequence
- introduce variational quantum circuit
- parameterize quantum gates
- describe measurement feedback
- introduce error-corrected implementation
- define approximation of target quantum state
- quantify proximity between quantum states
- introduce non-gate model quantum computers
- describe quantum annealing architecture
- illustrate quantum annealing operations
- introduce one-way quantum computing architecture
- describe measurement-based quantum computing
- introduce means for performing functions
- describe system implementation
- illustrate system components
- describe quantum computer components
- specify qubit implementation
- describe control unit functions
- generate control signals
- describe measurement unit functions
- provide measurement signals
- illustrate control unit implementations
- describe feedback signals
- introduce state preparation signals
- describe ansatz circuit
- introduce initialization
- describe gate control signals
- apply gates to qubits
- describe physical state changes
- introduce logical gate operations
- describe quantum gate application
- illustrate system operation
- describe method implementation
- summarize system functionality
- clarify state preparation and gate application
- describe quantum computer components
- explain measurement unit operation
- detail control unit and measurement unit interactions
- describe quantum circuit implementation
- explain shot preparation and measurement
- detail classical computer component
- describe classical computer memory and processor
- explain input and output operations
- describe hybrid quantum classical computer
- detail classical state preparation signals
- explain quantum gate operations
- describe measurement output
- detail classical processor and quantum computer cooperation
- clarify function allocation between classical and quantum computers
- describe technique implementation options
- explain classical computer emulation of quantum computer functions
- detail basis state substitution
- describe computer program implementation
- explain computer-readable medium storage
- detail input and output device interactions
- describe features requiring computer implementation
- clarify claim scope for computer-related elements
- explain product claim scope for computer-related elements
- describe programming language options
- detail computer program product implementation
- explain processor and memory interactions
- describe storage device options
- detail ASIC and FPGA implementation
- explain data structure implementation
- describe data storage and retrieval
- clarify optimization terminology

