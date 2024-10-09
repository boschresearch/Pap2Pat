# DESCRIPTION

## FIELD

- define field

## BACKGROUND

- motivate quantum computing

## SUMMARY

- summarize system

## DETAILED DESCRIPTION

- introduce photonic quantum computing
- limitations of known systems
- embodiment of system configuration

### INTRODUCTION

- motivate photonic quantum computing
- advantages of photonic quantum computing
- two main classes of photonic quantum computing system configurations
- first class: continuous variable cluster states with encoded qubits
- limitations of first class
- second class: direct generation of encoded qubit clusters
- limitations of second class
- hybrid scheme leveraging advantages of both classes
- desirable features for scalability
- fully on-chip implementation
- modular system configuration
- theoretical features: planar system configuration and hybrid resource state
- overview of system configuration

### Overview of the System Configuration

- system configuration includes three modules
- state preparation module generates bosonic qubits and magic states
- multiplexing module performs multiplexing of bosonic qubits
- main computational module stitches together hybrid resource state
- example system 100 for generating hybrid cluster state
- state factory generates GKP states
- time stitch implements delay line loops and chains qubits together
- space stitch multiplexes outputs in spatial domain
- photonic QPU entangles hybrid resource states into higher-dimensional cluster state

### Generation of Bosonic Qubits Using Multiplexed Gaussian Boson Sampling (“GBS”) Devices

- generation of non-Gaussian states of light
- multiplexing of GBS devices to obtain high rates and fidelities
- example of multiplexed state generation

### Time Domain Generation of 1D Clusters

- generation of 1D cluster states using optical delay lines and GKP qubits
- setup for generation of 1D cluster state
- operation of interferometer
- CZ gate implemented by interferometer
- generation of 1D GKP cluster state
- equivalent spatial representation
- complete example device for generating 1D cluster

### GKP Cluster in 2+1 Dimensions

- stitching together 1D hybrid temporal cluster states
- generation of higher-dimensional hybrid lattices
- example 2D chip layout for (2+1)D cluster generator
- 3D cubic lattice generated using 2D chip

### Generation of a Hybrid Raussendorf-Harrington-Goyal (“RHG”) Lattice

- generation of Raussendorf lattice
- example representations of two layers of Raussendorf lattice
- combined representation of two layers
- chip layout for generating Raussendorf lattices
- operation of chip layout
- generation of Raussendorf lattice as resource for fault-tolerant quantum computation

### Passive Version of System Configuration

- introduce hybrid CV-DV architecture
- motivate limitations of existing architectures
- propose novel architecture without inline squeezing
- describe generation circuit for fault-tolerant resource states
- explain symmetry of generation circuit
- calculate logical error rates for different levels of finite squeezing and photon loss
- define GKP encoding for optical bosonic modes
- introduce single-mode states within GKP code space
- model effects of finite squeezing via additive Gaussian bosonic channel
- define beamsplitter and phase shifter operations
- describe homodyne detectors and GKP Pauli measurements
- define CV CZ and CX gates for GKP qubits

### 3D Hybrid Macronode Architecture

- introduce 3D hybrid macronode architecture
- describe primal unit cell of 3D hybrid pair cluster state
- explain generation of 3D hybrid pair cluster state
- define two-mode entangled state
- derive two-mode entangled state from GKP or momentum squeezed vacuum
- show identities for two-mode cluster states
- obtain state diagram from identities
- create magic states by inserting into architecture
- arrange entangled pairs in 3D configuration
- specify 2D array of sources with probabilities
- apply beamsplitters, delay lines, and phase delays
- create fully connected 3D resource state
- apply homodyne detection
- prove equivalence to canonical hybrid cluster state
- show circuit representation of beamsplitter network
- apply circuit identities to migrate CZ gates
- commute CX gates and squeezers
- replace beamsplitters with CX gates and squeezers
- economize description of post-measurement state
- choose central mode from wires with GKP states
- describe noise model for single-mode Gaussian bosonic channel
- commute photon loss and finite squeezing noise
- rescale homodyne outcomes to account for loss
- describe threshold calculations using Monte Carlo simulations
- estimate conditional qubit-level error probabilities
- discuss improvement in swap-out tolerance
- introduce 3D hybrid macronode architecture
- motivate CZ gates elimination
- describe inline squeezing degradation
- explain circuit identities
- consolidate finite squeezing noise and photon losses
- reveal built-in redundancy
- describe GKP error correction
- motivate macronode with multiple GKP states
- describe entanglement structure
- illustrate 2D mode layout
- show 3D arrangement of four-mode macronodes
- describe macronode graph edges
- explain CZ gates replacement
- describe passive system configuration
- illustrate Raussendorf lattice generation
- modify node configuration
- describe beamsplitter interactions
- illustrate passive system configuration chip layout
- describe mode pairs and links/edges
- explain entangled states implementation
- describe dumbbell-shaped entangled states
- illustrate time delayed nodes
- describe different types of entangled states
- generalize passive architecture
- describe graph transformation
- motivate interferometer construction
- describe unitary matrix construction
- explain beam splitter network construction
- describe Fourier transform
- explain beamsplitter operation
- describe phase shifter operation
- conclude passive architecture generalization
- introduce 3D Hybrid Macronode Architecture
- describe quantum error correction
- outline Method 1: Procedure for Performing Fault-Tolerant Quantum Computation
- compile logical circuit
- state initialization
- implement logical circuit
- process measurement outcomes
- outline Method 2: Procedure for Performing Quantum Error Correction
- run decoder
- perform error correction
- outline Method 3: Example Inner Decoder
- identify noisy directions
- perform change of basis
- apply binning
- undo change of basis
- obtain binary string
- outline Method 4: Example Outer Decoder
- syndrome identification
- matching graph construction
- find minimum-weight perfect matching
- recovery operation
- correction
- describe noise model
- model state initialization error
- describe Gaussian white noise channel
- outline cluster state initialization
- prepare momentum-squeezed state
- apply CZ gates
- evolve noise matrix
- measure momentum values
- describe inner decoder
- outline importance of translator
- describe example of momentum-squeezed state
- outline outer decoder
- describe error correction problem
- outline numerical example
- describe heuristic translator
- outline Method 5: Example Inner Decoder for One p-Squeezed State Surrounded by GKP States

## Technological Advantages

### Modularity

- facilitate modular design

### Minimal Cryogenic Requirements

- reduce cryogenic requirements

### Homodyne Detection Sets Timescales

- set timescales for cluster generation
- set timescales for cluster manipulation
- describe homodyne detection
- compare homodyne detection with PNR detection
- compare homodyne detection with threshold detectors
- describe advantages of faster timescales
- describe shorter delay lines
- describe lower losses
- reference FIGS. 2A, 2C, and 4C
- describe delay lines in FIGS. 2A and 2C
- introduce method for generating hybrid cluster state
- receive input vector of homodyne measurements
- identify directions with noise levels above threshold
- perform change-of-basis
- apply transformation
- undo change-of-basis
- generate binary string
- describe alternative method for generating hybrid cluster state

