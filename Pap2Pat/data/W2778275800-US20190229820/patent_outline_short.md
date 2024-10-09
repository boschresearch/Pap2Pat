# DESCRIPTION

## FIELD OF THE DISCLOSURE

- define RF receivers

## BACKGROUND

- motivate spectrum sensing

## SUMMARY

- introduce active sequential xampling receiver

## DETAILED DESCRIPTION

- introduce cognitive radio scenario and RF spectrum sensing
- describe active sequential xampling receiver for spectrum sensing
- discuss limitations of Nyquist sampling and advantages of sub-Nyquist energy sensing

### A. Cognitive Radio Scenario

- describe cognitive radio scenario and RF spectrum 18

### B. Spectrum Sensing Architecture

- describe receiver 16 and analog front end 22
- explain dynamic modulator 26 and controller 28
- illustrate components of analog front end 22 and energy detector 24

### C. Hardware Considerations

- discuss hardware limitations and considerations for implementation

### II. Optimization Framework

- formulate optimization problem for receiver utility
- define observation model and utility function

### III. Dynamic Design of Sensing Matrices

- derive direct inspection case
- formulate optimization problem for direct inspection case
- introduce group testing approach
- define binary group test for group testing approach
- motivate dynamic design of sensing matrices
- derive equations for probabilities of declaring 1 in a group-test
- introduce optimization problem for sensing matrix B and threshold γ
- consider pairwise tests case and derive utility obtainable after decision
- formulate max-cut problem and prove sub-modularity of objective function
- discuss extension to L>2 and factor approximation of greedy algorithm

### IV. Approximate Maximum Likelihood Estimate for Mixed Tests

- derive approximate maximum likelihood estimate for mixed tests

### V. Simulation Results

- introduce simulation setup for spectrum sensing and RADAR applications
- compare utility for different optimization approaches for spectrum sensing
- compare utility for different optimization approaches for RADAR
- analyze utility for different N
- analyze utility for different SNRmin
- compare with other approaches, including compressive sensing and belief propagation

