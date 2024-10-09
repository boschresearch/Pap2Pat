# DESCRIPTION

## FIELD OF INVENTION

- define field of invention

## BACKGROUND

- motivate quantum computing

## SUMMARY

- summarize quantum computing
- motivate ground state energy estimation
- introduce disclosed technology

## Prior Approaches

- summarize prior methods
- limitations of prior methods

## DETAILED DESCRIPTION

- describe ground state energy estimation algorithm using low-depth quantum circuits

### Overview

- illustrate basic structure of computer system implementing method and system

### Early Fault-Tolerant GSEE Algorithms

- illustrate maximal evolution time vs. total evolution time of early fault-tolerant GSEE algorithms

### The GSEE Algorithm

- formulate GSEE problem
- discuss limitations of previous algorithms
- introduce approach for efficiently evaluating convolution

### Previous Early Fault-Tolerant GSEE Methods

- describe main idea of reducing GSEE problem to locating first non-zero point of function
- discuss limitations of previous methods

### Overcoming the 1/ϵ-Depth Barrier

- discuss bottleneck of maximal evolution time in previous methods
- introduce Gaussian filter function
- discuss properties of Gaussian filter function

### A Universal Approach for the Convolution Evaluation

- propose sample-efficient method to evaluate convolution
- discuss general approach for evaluating convolution for large family of filter functions

### Reducing tot via Gaussian Derivative Filtering

- introduce Gaussian derivative filter and its advantages

### Estimating Ground State Energy via Gaussian Derivative Filtering

- define Gaussian derivative function
- prove desirable property of convolution
- apply property to strategy for GSEE

### Part I.

- derive upper bound for convolution
- bound first term in Eq. (13)
- bound second term in Eq. (13)
- combine bounds to obtain Eq. (23)
- derive lower bound for convolution
- combine bounds to obtain Eq. (35)
- generate random variables
- introduce band-limited version of gσ
- define gσ,T and prove L∞-approximation
- prove L∞-approximation for gσ*p
- evaluate convolution via Hadamard tests
- define probability density v and random variables Xt and Yt
- define random variable Z(x) and prove unbiased estimation
- prove coincidence of expressions
- establish lemma 1
- analyze sample complexity
- establish lemma 2
- define empirical mean
- apply Hoeffding's inequality
- derive probability bounds
- illustrate convolution evaluation
- illustrate low-depth GSEE algorithm
- describe method for estimating ground state energy
- describe hybrid quantum-classical computer system
- discuss physical embodiments of quantum computers
- explain qubits and qudits
- describe gate model quantum computers
- define quantum circuit
- specify quantum gates
- describe quantum circuit design
- introduce variational quantum circuit
- describe measurement feedback
- define approximation of target quantum state
- introduce quantum annealing architecture
- describe quantum annealing process
- introduce one-way quantum computing architecture
- describe one-way quantum computing process
- introduce system architecture
- describe quantum computer components
- specify qubit interconnections
- describe control unit functions
- specify control signal forms
- describe measurement unit functions
- specify measurement signal forms
- describe feedback signals
- define quantum computer architecture
- describe state preparation and measurement
- explain gate application and control signals
- discuss measurement operations and results
- introduce hybrid quantum classical computer
- describe classical computer component
- explain quantum computer component interaction
- discuss classical control signals and state preparation
- describe gate operations and measurement output
- explain cooperation between classical and quantum computers
- discuss flexibility of function allocation
- introduce implementation options
- explain computer program execution
- discuss computer-readable storage media
- clarify claims and scope
- provide disclaimer on optimization

