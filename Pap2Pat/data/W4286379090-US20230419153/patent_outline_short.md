# DESCRIPTION

## BACKGROUND

### 1. Technical Field

- define technical field

### 2. Description of Related Art

- limitations of prior art

## SUMMARY

- introduce SFQG methods

## DETAILED DESCRIPTION

- introduce quantum algorithms for financial derivatives

### 1. INTRODUCTION

- motivate quantum acceleration of financial derivative pricing
- introduce quantum amplitude estimation for derivative pricing
- introduce greeks and their importance in financial risk analysis
- overview of disclosed approaches for computing greeks

### 2. GRADIENT METHODS FOR FINANCIAL DERIVATIVES

- introduce classical finite difference method for computing greeks
- introduce semi-classical quantum gradient method
- introduce quantum gradient methods using quantum Fourier transform
- compare complexities of different gradient estimation methods

### 3. HIGHER-ORDER METHODS FOR QUANTUM GRADIENTS

- motivate higher-order methods
- describe 2m-point central-difference approximation
- construct phase oracle for general 2m-point scheme

### 4. RESOURCE ESTIMATION OF QUANTUM GRADIENT METHODS

- introduce resource estimation
- describe asymptotic resource estimation for GAW method
- estimate number of oracle calls for target error
- compare to classical finite difference and semi-classical quantum finite difference
- numerically estimate GAW method for vanilla European call option
- numerically estimate GAW method for path-dependent basket option

### 5. SIMULATION-FREE QUANTUM GRADIENT (SFQG) METHOD

- construct second-order accurate quantum gradient algorithm
- define first-order phase oracle
- apply Grover operator to estimate derivatives of θ(x)
- construct second-order pricing phase oracle
- apply inverse Quantum Fourier Transform to estimate gradients of ƒ
- discuss post-processing to distinguish positive and negative cases

### 6. QUANTUM GRADIENT ESTIMATION USING MAXIMUM LIKELIHOOD ESTIMATION

- describe maximum likelihood estimation method
- apply MLE to quantum gradient estimation algorithms

### 7. UPDATED ESTIMATES FOR QUANTUM ADVANTAGE

- estimate quantum advantage for derivative pricing
- discuss potential speedup for SFQG method

### 8. PHASE KICKBACK

- describe phase kickback in SFQG method
- derive probability of measuring a value |z
- implement re-parameterization method
- discuss application of phase kickback to derivative pricing

### 9. AUTOMATIC DIFFERENTIATION AND MULTI-OBJECTIVE QAE

- introduce automatic differentiation
- construct probability oracle using automatic differentiation
- extend to multi-objective QAE
- compute gradients using multi-objective QAE
- discuss advantages of multi-objective QAE
- describe automatic differentiation and multi-objective QAE
- introduce computing system
- describe classical computing system
- describe quantum computing system
- describe execution of quantum routine
- describe quantum circuit
- describe parameters of parameterized quantum circuit
- describe storage of quantum circuit
- describe classical computing system architecture
- provide additional considerations
- provide general statements on embodiments

