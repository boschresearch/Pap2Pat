# DESCRIPTION

## BACKGROUND

### 1. Technical Field

- define technical field

### 2. Description of Related Art

- limitations of prior art

## SUMMARY

- motivate quantum gradient algorithms
- introduce SFQG methods
- application of SFQG methods

## DETAILED DESCRIPTION

- introduce quantum algorithms for market risk computation
- describe quantum amplitude estimation for derivative pricing
- outline alternative embodiments of quantum algorithms for computing market risk

### 1. INTRODUCTION

- introduce quantum algorithms for accelerating financial derivative pricing
- describe classical Monte Carlo methods for pricing
- motivate quantum amplitude estimation for pricing
- introduce greeks and their importance in financial risk management
- describe classical finite difference methods for computing greeks
- introduce quantum gradient estimation algorithms
- describe GAW quantum gradient algorithm
- outline application of GAW algorithm to financial derivatives
- introduce Simulation-Free Quantum Gradient (SFQG) method
- describe maximum likelihood estimation (MLE) for gradient estimation
- outline comparison of quantum, classical, and semi-classical gradient estimation algorithms
- highlight new contributions of the disclosure
- describe numerically studying quantum gradient estimation algorithms
- introduce second-order accurate oracle for quantum gradient estimation
- describe improving gradient estimation using classical MLE
- provide resource estimates for quantum advantage in financial derivative pricing
- describe employing automatic differentiation (AD) methods on quantum computers

### 2. GRADIENT METHODS FOR FINANCIAL DERIVATIVES

- introduce classical finite difference methods for computing greeks
- describe forward finite difference scheme
- describe central finite difference scheme
- analyze error of finite difference formulas
- introduce classical finite difference with common random numbers (CFD-CRN)
- describe semi-classical quantum gradient (SQG) method
- analyze complexity of SQG method
- introduce correlated sampling for SQG method
- describe quantum gradient estimation algorithms
- introduce fractional phase oracle for target function
- describe quantum Fourier transform for gradient estimation
- analyze complexity of quantum gradient estimation algorithms
- describe dependence of complexity on oracle construction
- describe dependence of complexity on region of function evaluation
- introduce example of high probability for gradient estimation
- describe importance of non-linearity of function in region of evaluation
- outline application of quantum gradient estimation to financial derivatives
- describe advantages of quantum gradient estimation over classical methods
- summarize complexities of different gradient estimation methods

### 3. HIGHER-ORDER METHODS FOR QUANTUM GRADIENTS

- introduce higher-order methods for quantum gradients
- motivate central-difference schemes
- define 2m-point central-difference approximation
- construct phase oracle for general 2m-point scheme
- describe application to Gevrey class G1/2 functions
- state Theorem 1 for gradient estimation
- introduce block encoding technique
- define block encoding of probability oracle
- describe Hamiltonian simulation method
- provide formula for number of oracle calls
- discuss optimal value of β
- describe application to financial domain
- summarize scaling in k and c of algorithms

### 4. RESOURCE ESTIMATION OF QUANTUM GRADIENT METHODS

- introduce resource estimation for quantum gradient methods
- describe representative parameters from financial domain
- assume smoothness conditions of Theorem 1
- set phase error ϵphase
- set finite-difference approximation degree m
- set spacing parameter l
- estimate number of oracle calls
- compare to classical finite difference and semi-classical methods
- introduce GAW numerical estimates
- describe numerical simulation of GAW algorithm
- examine central-difference approximation order m
- examine spacing l
- describe practical method for emulating algorithm's performance
- account for phase error ϵphase
- describe vanilla options example
- provide closed-form solution for European call option
- describe numerical simulation for increasing k
- search for optimal values of m and l
- compare to theoretical estimates from Theorem 1
- show results of numerical simulation
- describe path-dependent basket options example
- provide definition of option contract's price V
- describe classical Monte Carlo pricing
- simulate GAW algorithm for path-dependent basket option
- compare query complexity to SQG method
- compare query complexity to CFD and CFD-CRN methods
- summarize results of numerical simulation

### 5. SIMULATION-FREE QUANTUM GRADIENT (SFQG) METHOD

- introduce SFQG method
- describe construction of second-order accurate quantum gradient algorithm
- define phase oracle OS
- construct first-order pricing phase oracle
- evaluate operator on superposition of points x
- apply Grover operator πS times
- get estimate of derivatives of θ(x) at x0
- compute gradients of ƒ using chain rule
- distinguish positive and negative cases
- introduce second-order pricing phase oracle
- construct oracle OSθ1|x
- define operators + and -
- generate state with correct phases
- add dummy variable to function
- distinguish eigenstates
- illustrate quantum circuit diagram
- apply Hadamard gates
- create copy of each |x
- evaluate oracles OSθ+ and OSθ-
- uncompute copies
- apply inverse Quantum Fourier Transform
- measure to estimate gradients
- simulate SFQG algorithm
- compute greeks of basket option
- discuss query complexity

### 6. QUANTUM GRADIENT ESTIMATION USING MAXIMUM LIKELIHOOD ESTIMATION

- introduce maximum likelihood estimation
- describe issues with previous methods
- define log-likelihood function
- maximize log-likelihood function
- derive confidence intervals
- illustrate probability distribution
- fit to theoretical distribution
- plot log-likelihood function
- get MLE estimate
- discuss advantages of MLE method
- discuss classical compute cost

### 7. UPDATED ESTIMATES FOR QUANTUM ADVANTAGE

- update resource estimation for quantum advantage
- motivate reparameterization technique
- estimate T-depth of SFQG circuit
- calculate greeks of basket option
- compare classical and quantum pricing times
- discuss potential advantages of SFQG method
- analyze limitations of SFQG method
- discuss applicability to GAW method

### 8. PHASE KICKBACK

- introduce phase kickback in SFQG method
- define state after application of operator
- apply inverse Quantum Fourier Transform
- calculate probability of measuring value |z
- discuss implementation of re-parameterization method
- define operator
- load standard normal distributions
- compute payoff using quantum arithmetic
- rotate payoff into amplitude of ancilla qubit
- uncompute register |g(i)
- write overall effect of operator
- evaluate in superposition over register |x
- define states |ψ±(x)
- discuss linearity of θ(x) near x=0
- calculate probability of measuring value |z
- discuss application of operator
- illustrate simulated measurement outcomes
- discuss results of simulation

### 9. AUTOMATIC DIFFERENTIATION AND MULTI-OBJECTIVE QAE

- introduce automatic differentiation
- advantage of automatic differentiation
- construct probability oracle
- apply quantum arithmetic
- compute payoff function
- compute gradient
- use reversible implementation
- result in state
- use QAE to read out multiple objectives
- estimate expectation values
- construct state
- use quantum arithmetic to compute sum
- construct operator
- apply rotation controlled by register
- construct probability oracle
- use quantum gradient algorithm
- result in read out of all k expectation values
- discuss complexity of algorithm
- apply multi-objective QAE to evaluate gradient
- combine AD and QAE
- result in gradient algorithm with runtime
- discuss advantage over finite difference schemes
- conclude AD as promising approach
- introduce automatic differentiation and multi-objective QAE
- describe function ƒ(x) and its properties
- determine gradient of function ƒ(x) using quantum gradient algorithm
- describe phase oracle OSƒm
- execute quantum circuit to determine gradient
- transmit instructions based on gradient
- introduce computing system
- describe classical computing system
- describe quantum computing system
- illustrate block diagram of computing system
- describe qubits and qubit controllers
- execute quantum routine on computing system
- generate quantum program
- execute quantum program
- compute result
- record result
- determine quantity based on result
- describe quantum computing system
- describe qubits
- describe quantum circuit
- describe gates and unitary operations
- describe depth and layers of quantum circuit
- execute quantum circuit on quantum computing system
- store description of quantum circuit
- describe classical computing system architecture
- describe processor and chipset
- describe memory and storage device
- describe keyboard and pointing device
- describe graphics adapter and display
- describe network adapter
- describe storage device as non-transitory computer-readable storage medium
- describe memory as non-persistent memory
- describe computer program modules
- describe algorithmic processes and operations
- describe modules and functional operations
- describe use of "one embodiment" and "an embodiment"
- describe use of "comprises", "comprising", "includes", and "including"
- describe use of "or" and "a" or "an"
- describe approximate values
- describe alternative embodiments
- describe computer program product
- describe method steps
- describe programmable processor
- describe data storage system
- describe input and output devices
- describe scope of disclosure

