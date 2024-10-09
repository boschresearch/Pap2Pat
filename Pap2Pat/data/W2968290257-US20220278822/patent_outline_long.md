# DESCRIPTION

## TECHNICAL FIELD

- relate to AES, SBox, hardware implementation, critical path

## BACKGROUND

### Technical Background/Existing Technology

- introduce AES
- describe AES encryption algorithm
- explain hardware implementations of AES
- motivate need for efficient hardware design of AES SBox
- describe SBox circuit
- define forward AES SBox
- explain non-linear function I(g) and affine function A(g)
- describe circuit for building inversion over GF(2^8)
- introduce Rijmen's idea for small area implementation
- describe Satoh et al's Tower Field construction
- explain Canright's investigation of subfield representation
- introduce Boyar et al's ideas for subfield inverter and minimizing area
- describe Boyar et al's inverter over GF(2^4) with depth 4
- introduce Reyhani et al's implementation of forward SBox and combined SBox
- compare results theoretically
- introduce standard method for evaluating circuit area and depth
- describe negotiation of NOT gates
- introduce technology method for evaluating circuit area and depth
- explain area calculation using Gates Equivalence (GE)
- describe depth calculation using normalized delay-units
- summarize previous work on forward SBox
- summarize previous work on combined SBox
- describe problems with existing solutions
- motivate need for low-depth implementation
- explain importance of area-optimized encryption algorithms
- conclude background

## SUMMARY

- introduce SBox functionality
- describe SBox circuit
- explain first circuit part
- explain second circuit part
- explain third circuit part
- describe calculation in third circuit part
- introduce digital circuits used
- describe forward and inverse SBox operations
- conclude summary

## DETAILED DESCRIPTION

- introduce SBox architecture

### PART A

- define classical SBox architecture
- describe Tower Field construction
- introduce irreducible polynomial
- construct normal base
- express element in GF(2^2)
- build GF(2^4) from GF(2^2)
- build GF(2^8) from GF(2^4)
- summarize irreducible polynomials, roots, and normal bases
- define general element in GF(2^8)
- derive inverse of A
- describe classical architecture of SBox
- introduce new architecture "D"
- remove bottom matrix
- reduce depth of circuit
- describe block diagram of architecture D
- introduce first circuit part
- introduce second circuit part
- introduce third circuit part
- generate 4-bit first output signal
- generate 32-bit second output signal
- produce four preliminary 8-bit results
- produce 8-bit output signal
- compare architecture A and D
- describe conventional SBox architecture A
- describe new SBox architecture D
- redistribute functional aspects
- describe first circuit part
- describe second circuit part
- describe third circuit part
- present gate configuration
- describe shared components
- present advantages of invention
- describe importance of fast SBox
- present synthesis results
- compare with other recent work
- describe technology process
- present synthesis results for forward SBox
- present synthesis results for combined SBox

## PART B OF THE DISCLOSURE

- introduce AES SBox

### 1 Introduction

- motivate efficient AES SBox implementation
- introduce table-lookup implementation
- discuss area and speed trade-offs
- introduce need for inverse cipher
- discuss combining forward and inverse SBox
- define AES SBox mathematically
- summarize prior work on AES SBox implementation
- introduce new techniques for minimizing circuit realization
- preview new architecture for AES SBox

### 2 Preliminaries

- define tower field representation
- derive expression for inverting element in GF(28)
- describe architecture of SBox
- introduce objectives for minimizing linear matrices

### 3 Circuits for Binary Linear System of Equations

- state basic problem statement
- introduce additional input requirement (AIR)
- introduce additional output requirement (AOR)
- describe cancellation-free heuristics
- introduce Paar's greedy approach
- describe Canright's exhaustive search approach
- solve AIR using delay tracking
- solve AOR using CircuitDepth function
- introduce probabilistic heuristic approach
- describe cancellation-allowed heuristics
- introduce Boyar and Peralta's algorithm
- describe basic cancellation-allowed algorithm
- define distance function δi
- describe algorithm for updating set S
- describe tie resolution strategy
- introduce Reyhani et al's improvements
- describe our improvement to algorithm
- discuss solving AIR problem
- discuss solving AOR problem
- describe exhaustive search methods
- introduce notations and data representation
- describe basic idea of exhaustive search
- describe step 1 of exhaustive search
- describe step 2 of exhaustive search
- describe step 3 of exhaustive search
- describe ignored points and optimizations
- describe intersection rule
- describe forward propagation rule
- conclude on searching for minimum solution

### 4.1 Floating Multiplexers

- introduce floating multiplexers
- motivate floating multiplexers
- define floating multiplexers
- describe application of floating multiplexers
- introduce metrics and linear expressions
- define linear matrix ABC
- describe reduction of ABC matrix
- introduce metric for search
- describe algorithm-A(k) for finding Δs
- describe algorithm-B for finding Δs

### 4.2.1 Problem Statement

- introduce problem statement
- define input signal Xn
- define binary matrices Mm+nF and Mm×nI
- define binary vectors AnF, AnI, BmF, BmI
- define vectors of delays DnX and DmY
- define output signal Y
- define YF and YI
- define ZF and ZI
- define A* and B* as constant masking vectors
- define point as tuple of point value and delay
- define signal as MUX gate
- define input points Xk
- define target points Yk
- introduce 4 trivial points
- define 6 possible new points generated by gates
- define Dnew
- describe importance of trivial points
- describe limitation of gate types
- describe implementation of NOT-gate, AND gate, and OR gate

### 5 Architectural Improvements

- introduce two SBox architectures
- describe Area architecture
- describe Depth architecture
- motivate removing bottom matrix
- derive output from Depth architecture
- describe limitations of Depth architecture
- introduce six scenarios of MULN
- describe scenario S0
- describe scenario S1
- describe scenario S2
- describe scenario S3
- describe scenario S4
- describe scenario S5
- motivate computing additional Ys in parallel
- describe inversion over GF(24)
- derive inversion formulae
- motivate using wider range of standard gates
- describe exhaustive search for Boolean expressions
- describe selection of best functions
- provide equations for inversion
- introduce Alpha-Beta approach
- describe application of Alpha-Beta approach
- motivate testing all variants of linear matrices

### 6 Results and Comparisons

- introduce synthesis results
- compare with other academic work
- describe forward SBox results
- compare forward SBox with previous results
- describe combined SBox results
- compare combined SBox with previous results
- show synthesis results for forward SBox
- show synthesis results for combined SBox

### CONCLUSIONS

- summarize contributions

## PART C OF THE DISCLOSURE

- motivate inversion circuit
- present inversion formulae
- adapt algorithm for INV block
- find small solution for INV block
- present alternative set of equations
- organize exhaustive search
- select best Boolean functions

### APPENDIX E

- introduce circuit specifications
- describe shared components
- describe specific components for each circuit

