# DESCRIPTION

## BACKGROUND

### 1. Technical Field

- define technical field

### 2. Description of Related Art

- motivate stochastic process simulation
- describe quantum state representation
- limitations of current simulation methods
- application of stochastic process simulation

## SUMMARY

- introduce new simulation method
- describe key points of simulation method
- application of simulation method

## DETAILED DESCRIPTION

- introduce quantum state representation of stochastic process
- define basis state of quantum computing system
- describe amplitude function of price trajectory
- motivate use of quantum algorithms for financial instruments
- define mixed state of stochastic process
- introduce discrete cosine transform (DCT) of mixed state
- describe DCT as real part of Quantum Fourier Transform
- outline efficient algorithm for DCT on quantum computing system
- describe preparation of state σ using DCT
- note linearity of DCT for stochastic processes
- give example of Brownian motion and its DCT
- describe truncation of DCT series
- introduce probability distribution over DCT coefficients
- describe goal of preparing quantum state σ′
- introduce quantum data loader algorithm
- describe data loader algorithm A
- outline preparation of state σ′ using data loader
- describe inverse map of data loader angles
- give example of Brownian motion and its data loader angles
- describe "data loading the data loader" algorithm
- outline creation of state |D′〉
- describe application of data loader algorithm A to |D′〉
- outline tracing out of first register to obtain σ′
- describe alternative method for Brownian motion
- discuss normalization of vectors involved
- summarize method for simulating stochastic process
- describe FIG. 1 quantum circuit diagram
- describe FIG. 2 flowchart of method for simulating stochastic process

### Example Method

- receive stochastic process with trajectories over time
- determine first quantum circuit to prepare mixed quantum state ρ′
- determine DCT series of stochastic process
- determine probability distribution for coefficients in DCT series
- determine probability distribution of angles D′ for data loader
- execute first quantum circuit to generate mixed quantum state ρ′

### Description of a Computing System

- introduce computing system 400
- describe classical computing system 410
- describe quantum computing system 420
- illustrate classical computing system 410 and quantum computing system 420
- describe qubits 450 and qubit controllers 440
- illustrate qubits 450 in qubit register
- describe qubit controller 440
- illustrate separate qubit controller 440 for each qubit 450
- describe execution of quantum routine on computing system 400
- generate quantum program
- execute quantum program
- compute result
- record result
- illustrate architecture of classical computing system 410
- describe processor 502
- describe chipset 504
- describe memory 506
- describe storage device 508
- describe keyboard 510
- describe graphics adapter 512
- describe pointing device 514
- describe network adapter 516
- describe display 518

### Additional Considerations

- describe embodiments for purposes of illustration
- describe essential features
- describe algorithmic processes
- describe modules
- describe one embodiment
- describe inclusive or
- describe approximate values
- describe alternative embodiments
- describe computer program product
- describe programmable processor
- describe data storage system
- describe modifications and variations

