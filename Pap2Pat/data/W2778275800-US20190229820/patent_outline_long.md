# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define RF receivers

## BACKGROUND

- motivate spectrum sensing
- limitations of Nyquist rate
- introduce xampling architectures

## SUMMARY

- introduce active sequential xampling receiver
- describe dynamic modulator
- explain energy detection
- motivate utility function
- describe optimization
- introduce exemplary embodiments

## DETAILED DESCRIPTION

- introduce cognitive radio scenario
- describe RF spectrum and channels
- explain need for timely decision in spectrum sensing
- introduce active sequential xampling receiver
- describe analog front end and dynamic modulator
- explain optimization problem for spectrum sensing
- discuss limitations of Nyquist sampling
- introduce utility function for spectrum sensing
- explain structure of utility function
- discuss relation to stochastic optimization schemes
- summarize performance analysis of sensing matrix designs
- outline organization of disclosure
- introduce notation for vectors, matrices, and sets
- define marginal increment for set function
- conclude introduction to detailed description

### A. Cognitive Radio Scenario

- describe cognitive radio scenario
- illustrate RF spectrum and channels
- explain need for timely decision in spectrum sensing

### B. Spectrum Sensing Architecture

- introduce receiver architecture
- describe analog front end and energy detector
- explain dynamic modulator and controller
- illustrate receiver architecture
- describe components of analog front end
- explain dynamic modulator and sensing matrix
- describe energy detector and sampling circuit
- introduce received signal model
- explain modulation and demodulation
- describe energy detector output
- introduce orthogonal projections
- explain approximation errors due to windowing
- discuss mitigation of side lobes
- conclude description of spectrum sensing architecture

### C. Hardware Considerations

- discuss settling time for VCOs
- explain use of low-pass filter and slower sampling rate
- discuss use of N oscillators at constant frequencies
- conclude hardware considerations

### II. Optimization Framework

- model receiver as dividing time between sensing and exploiting sub-bands
- define utility function of receiver as function of state vector
- describe sensing process and measurement design
- introduce decision rules for unknown states of resources
- define total utility for receiver
- formulate optimization problem to maximize utility
- specify example form for function θ
- describe observation model and exponential distribution
- motivate application to RF spectrum sensing

### III. Dynamic Design of Sensing Matrices

- define direct inspection case
- formulate hypothesis testing
- derive energy detection
- set test threshold
- define utility
- introduce assumption 1
- express optimization in terms of B
- define test error probabilities
- show independence of false alarm probability
- guarantee detection performance
- introduce generalized likelihood ratio test
- rewrite optimization problem
- define sub-modular function
- introduce lemma 1
- sort resources
- find best set size
- introduce group testing approach
- define sets k and i
- formulate binary group test
- highlight hypotheses
- note GT approach
- write test equation
- derive alpha and beta
- define decision rule
- derive pi functions
- define alpha and beta GT
- note optimization complexity
- introduce additional constraints
- consider pairwise tests case
- set bi=bj
- define binary coefficients
- establish upper-bound for miss detection probability
- define utility uijGT
- set threshold gammaij
- translate problem to max-cut problem
- define UGT
- add penalty for constraint violation
- define upsilon function
- state Lemma 2
- extend result to L>2
- discuss factor approximation of greedy algorithm
- state Lemma 3
- discuss complexity of Algorithm 1
- note additional applications of stochastic optimization

### IV. Approximate Maximum Likelihood Estimate for Mixed Tests

- propose alternative approach for any measurement matrix B
- derive log-likelihood function
- formulate LASSO problem
- incorporate prior beliefs ωi

### V. Simulation Results

- introduce simulation setup
- define parameters for spectrum sensing and RADAR applications
- explain reward and penalty for spectrum sensing
- explain reward and penalty for RADAR application
- motivate expected utility increasing linearly with time
- highlight time dependency in optimization objective
- introduce greedy solution and its limitations
- present simulation results for spectrum sensing vs. RADAR
- describe FIG. 4A
- describe FIG. 4B
- explain experiment setup
- analyze utility for different optimization approaches
- discuss gain for GT approach over DI approach
- present simulation results for different N
- describe FIG. 5A
- describe FIG. 5B
- analyze utility for different horizons K
- discuss benefit of mixing resources
- present simulation results for different SNRmin
- describe FIG. 6A
- describe FIG. 6B
- analyze utility for different minimum SNR
- compare with approximate ML estimate via compressive sensing
- compare with belief propagation in a loopy network
- discuss benefit of active sub-Nyquist receiver
- conclude simulation results

