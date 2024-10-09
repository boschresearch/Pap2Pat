# DESCRIPTION

## BACKGROUND

### Field of the Technology Disclosed

- define field of technology

### Description of Related Art

- motivate quantum computers
- limitations of current quantum algorithms
- introduce VQE and its drawbacks

## SUMMARY

- introduce disclosed technology
- summarize algorithm and quantum circuit
- application of disclosed technology
- embodiment of disclosed technology
- method for estimating ground state property
- advantages of disclosed technology

## DETAILED DESCRIPTION

- introduce quantum computers and their applications
- describe the disclosed technology for ground state property estimation
- overview of the system for ground state property estimation using a hybrid quantum-classical computer system

### Reduced Depth of The Quantum Circuit

- describe the advantage of the disclosed algorithm in terms of quantum circuit depth

### Example Embodiment of The Algorithm

- describe the theorem for estimating ground state properties with high accuracy and low-depth

### Comparison to the Straightforward Method

- compare the disclosed algorithm with the straightforward approach of GSPE

### Ground State Property Estimation Problem

- define the ground state property estimation problem
- describe the search version of APX-SIM and the assumptions made

### An Overview of the Low-Depth Ground State Energy Estimation

- describe the theorem for low-depth ground state energy estimation
- explain the classical post-processing procedure
- describe the Fourier approximation and the estimation of the ground state energy

### Example Algorithm for Commutative Case

- introduce commutative case
- define initial state and Hamiltonian
- describe Step 1: estimate ground state energy
- construct xgood for λ0
- estimate overlap p0 with additive error η/8
- describe Step 2: estimate O-weighted CDF
- define O-weighted density function pO(x)
- estimate O-weighted ACDF with unbiased estimator
- describe variance of estimator G(x;J,Z)
- bound expected total evolution time
- conclude Step 2

### Summarizing the Main Theorem

- state Main Theorem for ground state property estimation

### Thus

- conclude error bound for ground state property estimation

### Algorithm for General Unitary Observables

- state theorem for unitary observables
- introduce 2-d O-weighted density function and CDF
- define 2-d O-weighted approximated CDF
- prove approximation ratio of 2-d O-weighted ACDF
- bound error of 2-d O-weighted ACDF
- define FL,2 and FR,2
- prove first inequality of approximation ratio
- prove second inequality of approximation ratio
- describe parameterized quantum circuit for estimating 2-d O-weighted ACDF
- Introduce algorithm for general unitary observables
- Motivate estimation of 2-d O-weighted ACDF
- Define random variables J, J' with support {-d,..., d}
- Define estimator (x;j,j', Z)
- Show unbiasedness of estimator
- Upper-bound variance of estimator
- Use median-of-means estimator to obtain E-additive error estimate
- Construct 2-d good point for (λ0, λ0)
- Estimate ground state property in general case
- Analyze estimation error of Algorithm 3
- Handle non-unitary observables using block-encoding
- Estimate ϕ0|e−itHOe−itH|ϕ0 for arbitrary non-unitary O
- State main theorem for ground state property estimation with block-encoded observable
- define algorithm for general unitary observables
- motivate estimation of ground state properties
- summarize application of ground state property estimation algorithm
- describe charge density estimation
- introduce quantum linear system solver
- describe Hamiltonian encoding
- outline algorithm for estimating properties of linear system solution
- analyze computation cost of algorithm
- discuss gap amplification technique
- describe application of algorithm to quantum linear system solution
- summarize advantages of disclosed algorithm
- discuss future directions for improvement
- outline hybrid quantum-classical algorithm for estimating ground state property
- describe applications of algorithm
- introduce quantum computing
- describe qubits
- explain quantum gates
- describe quantum circuits
- introduce measurement feedback
- define approximation of quantum states
- describe quantum annealing
- illustrate quantum annealing operations
- introduce one-way quantum computing
- describe system architecture
- illustrate system components
- describe control unit
- explain control signals
- describe measurement unit
- explain measurement signals
- provide examples of qubit implementations
- describe quantum computer components
- explain classical components
- describe control unit functions
- explain measurement unit functions
- provide examples of control signals
- provide examples of measurement signals
- introduce quantum computer architecture
- describe control unit and qubits
- explain state preparation and gate application
- discuss measurement unit and measurement signals
- describe repetition of operations
- introduce hybrid quantum classical computer
- describe classical computer component
- explain interaction between classical and quantum components
- discuss preparation of qubits and application of gates
- describe measurement and output
- explain repetition of process
- discuss flexibility of classical and quantum components
- introduce implementation in hardware, software, or firmware
- explain emulation of quantum computer on classical computer
- discuss replacement of computational basis states
- describe implementation in computer programs
- explain requirement for computer-related elements
- discuss programming languages and computer-readable media
- clarify meaning of "optimize" and "optimal"

