# DESCRIPTION

## BACKGROUND

### 1. Technical Field

- define technical field

### 2. Description of Related Art

- limitations of prior art

## SUMMARY

- introduce SFQG methods

## DETAILED DESCRIPTION

- introduce quantum algorithms for market risk computation

### 1. INTRODUCTION

- introduce quantum algorithms for financial derivatives
- motivate quadratic advantage in market risk computation
- describe classical Monte Carlo methods for pricing
- introduce quantum amplitude estimation for pricing
- motivate gradient computation for financial derivatives
- introduce classical finite difference methods for greeks
- introduce quantum gradient estimation algorithms
- outline the structure of the disclosure

### 2. GRADIENT METHODS FOR FINANCIAL DERIVATIVES

- introduce greeks and their importance
- describe classical finite difference methods
- introduce classical finite difference with common random numbers
- introduce semi-classical quantum gradients
- describe the complexity of classical finite difference methods
- describe the complexity of semi-classical quantum gradients
- introduce quantum gradients using quantum Fourier transform
- describe the oracle for quantum gradient estimation
- outline the complexity of quantum gradient estimation algorithms

### 3. HIGHER-ORDER METHODS FOR QUANTUM GRADIENTS

- motivate higher-order methods
- introduce 2m-point central-difference approximation
- construct phase oracle for general 2m-point scheme
- estimate gradients of smooth functions
- create phase oracles from probability oracles
- implement quantum gradient method using block encoding

### 4. RESOURCE ESTIMATION OF QUANTUM GRADIENT METHODS

- describe resource estimation for gradient methods
- set parameters for gradient estimation problems
- estimate number of oracle calls for GAW method
- compare to classical finite difference and semi-classical methods
- introduce GAW numerical estimates
- describe numerical simulation of GAW method
- examine central-difference approximation order and spacing
- compare to theoretical values
- describe vanilla options example
- numerically simulate GAW algorithm for vanilla options
- describe path-dependent basket options example
- numerically simulate GAW algorithm for path-dependent basket options
- compare query complexity to other methods

### 5. SIMULATION-FREE QUANTUM GRADIENT (SFQG) METHOD

- introduce SFQG method
- construct first-order phase oracle
- apply Grover operator to phase oracle
- estimate derivatives of θ(x) at x0
- compute gradients of ƒ using chain rule
- distinguish positive and negative cases
- construct second-order phase oracle
- apply product of oracles to generate state
- measure gradients and distinguish cases
- illustrate SFQG method in quantum circuit diagram
- simulate SFQG algorithm to compute greeks
- discuss complexity of SFQG algorithm

### 6. QUANTUM GRADIENT ESTIMATION USING MAXIMUM LIKELIHOOD ESTIMATION

- introduce maximum likelihood estimation
- apply MLE to quantum gradient estimation
- illustrate MLE for Vega estimation
- discuss advantages of MLE method
- analyze complexity of MLE post-processing

### 7. UPDATED ESTIMATES FOR QUANTUM ADVANTAGE

- update resource estimation for quantum advantage
- estimate T-depth of SFQG circuit
- compare classical and quantum runtime
- discuss potential advantages of SFQG method

### 8. PHASE KICKBACK

- introduce phase kickback in SFQG method
- derive state after applying operator
- apply inverse Quantum Fourier Transform
- calculate probability of measuring value |z
- implement re-parameterization method
- load standard normal distributions
- compute payoff using quantum arithmetic
- rotate into amplitude of ancilla qubit
- discuss phase kickback failure conditions

### 9. AUTOMATIC DIFFERENTIATION AND MULTI-OBJECTIVE QAE

- introduce automatic differentiation
- describe gradient computation using automatic differentiation
- construct probability oracle for QAE
- apply quantum arithmetic to compute payoff
- compute gradient using automatic differentiation and quantum arithmetic
- describe multi-objective QAE for estimating expectation values
- construct state for multi-objective QAE
- estimate values using multi-objective QAE
- compute gradient using multi-objective QAE
- discuss complexity of multi-objective QAE
- combine automatic differentiation and multi-objective QAE for gradient algorithm
- introduce automatic differentiation and multi-objective QAE
- describe function ƒ(x) and its properties
- determine gradient of function ƒ(x) using quantum gradient algorithm
- describe phase oracle OSƒm
- execute quantum circuit to determine gradient
- transmit instructions based on gradient
- introduce computing system
- describe classical computing system
- describe quantum computing system
- execute quantum routine on computing system
- generate quantum program
- execute quantum program
- record result
- determine quantity based on result
- describe qubits and qubit controllers
- describe quantum circuit
- describe gates and unitary operations
- describe parameters of parameterized quantum circuit
- store description of quantum circuit
- describe classical computing system architecture
- describe communication buses
- describe storage device
- provide additional considerations

