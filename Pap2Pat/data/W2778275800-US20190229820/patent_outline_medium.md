# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define RF receivers

## BACKGROUND

- motivate spectrum sensing

## SUMMARY

- introduce active sequential xampling receiver
- describe dynamic modulator
- explain controller adjustment

## DETAILED DESCRIPTION

- introduce cognitive radio scenario
- describe RF spectrum and channels
- introduce active sequential xampling receiver
- motivate sub-Nyquist energy sensing
- describe optimization problem
- introduce dynamic modulator and controller
- discuss hardware limitations and considerations

### A. Cognitive Radio Scenario

- describe cognitive radio scenario

### B. Spectrum Sensing Architecture

- introduce receiver architecture
- describe analog front end
- introduce dynamic modulator
- describe energy detector
- introduce controller
- describe sensing matrix
- discuss sequential non-coherent tests

### C. Hardware Considerations

- discuss VCO settling time
- discuss alternative oscillator configurations

### II. Optimization Framework

- model receiver as optimization problem
- define utility function and state variables
- formulate optimization problem for optimal policy
- specify observation model and assumptions

### III. Dynamic Design of Sensing Matrices

- define direct inspection case
- formulate hypothesis testing
- derive energy detection
- define test threshold
- introduce assumption 1
- express optimization problem
- introduce group testing approach
- formulate binary group test
- discuss application of group testing
- introduce dynamic design of sensing matrices
- formulate optimization problem
- derive equations for error probabilities
- introduce constraints on sensing matrix
- discuss pairwise tests case
- formulate utility function for pairwise tests
- introduce max-cut problem
- rewrite optimization problem with penalty term
- prove sub-modularity of objective function
- extend results to L>2
- discuss factor approximation of greedy algorithm
- mention additional applications of stochastic optimization

### IV. Approximate Maximum Likelihood Estimate for Mixed Tests

- derive log-likelihood function
- propose LASSO problem solution

### V. Simulation Results

- introduce simulation setup
- define utility function for spectrum sensing
- define utility function for RADAR application
- explain time dependency in optimization objective
- present simulation results for spectrum sensing vs. RADAR
- analyze utility for different optimization approaches
- discuss effect of penalty-to-reward ratio on GT approach
- present simulation results for different N values
- analyze utility for different optimization approaches vs. K/N ratio
- discuss effect of horizon K on GT approach
- present simulation results for different SNRmin values
- analyze utility for different optimization approaches vs. SNRmin
- compare performance with belief propagation and LDPC matrix

