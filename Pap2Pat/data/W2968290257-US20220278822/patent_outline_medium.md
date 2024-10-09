# DESCRIPTION

## TECHNICAL FIELD

- relate to AES, SBox, hardware implementation, critical path

## BACKGROUND

### Technical Background/Existing Technology

- introduce AES
- describe hardware implementations of AES
- explain AES encryption algorithm
- describe SBox circuit
- motivate minimizing gates and critical path
- discuss table-lookup implementation
- introduce need for inverse cipher
- describe forward AES SBox
- explain non-linear function I(g) and affine function A(g)
- discuss minimizing inversion over GF(2^8)
- summarize previous work on SBox implementation
- introduce notation for gate names
- explain standard method and technology method for evaluating circuits

## SUMMARY

- motivate low depth SBox implementation
- introduce SBox circuit with three parts
- describe first and second circuit parts
- describe third circuit part and its calculation

## DETAILED DESCRIPTION

- introduce SBox architecture

### PART A

- build GF(2⁸) using Tower Field construction
- define irreducible polynomial f(x)
- construct normal base from conjugates of W
- express elements in GF(2²) using normal base
- build GF(2⁴) from GF(2²)
- build GF(2⁸) from GF(2⁴)
- summarize irreducible polynomials, roots, and normal bases
- define general element in GF(2⁸)
- derive inverse of A
- describe classical SBox architecture
- introduce new architecture D
- describe motivation for architecture D
- derive result R in architecture D
- describe block diagram of architecture D
- detail first circuit part of architecture D
- detail second circuit part of architecture D
- detail third circuit part of architecture D
- compare architecture D with conventional architecture A
- describe gate configuration of architecture D

## PART B OF THE DISCLOSURE

- introduce AES SBox and its importance in cryptographic systems

### 1 Introduction

- motivate efficient hardware design of AES SBox
- discuss limitations of table-lookup implementation
- introduce need for combined SBox and inverse cipher
- summarize previous work on AES SBox implementation

### 2 Preliminaries

- define tower field representation and irreducible polynomials
- derive expression for inverting a general element in GF(28)

### 3 Circuits for Binary Linear System of Equations

- state basic problem statement for linear circuit minimization
- introduce additional input requirement (AIR) and additional output requirement (AOR)
- describe cancellation-free heuristics for linear circuit minimization
- solve AIR using input delay vector
- solve AOR using circuit depth function
- describe probabilistic heuristic approach for cancellation-free heuristics
- introduce cancellation-allowed heuristics for linear circuit minimization
- describe basic cancellation-allowed algorithm
- improve cancellation-allowed algorithm using faster evaluation of distance function
- discuss limitations of cancellation-allowed heuristics with maxD constraint
- introduce exhaustive search methods for linear circuit minimization
- describe notations and data representation for exhaustive search
- explain steps of exhaustive search algorithm
- discuss ignored points and other optimizations for exhaustive search

### 4.1 Floating Multiplexers

- motivate floating multiplexers
- define metrics and linear expressions to solve
- introduce iterative algorithms to find Δs
- describe algorithm-A(k) and algorithm-B
- discuss limitations of the algorithms

### 4.2.1 Problem Statement

- introduce problem statement
- define input signal Xn and binary matrices Mm+nF and Mm×nI
- define binary vectors AnF, AnI, BmF, BmI, and vectors of delays DnX and DmY
- define output signal Y
- introduce masking vectors A* and B*
- define ZF and ZI
- define point and signal
- represent input points Xk
- represent target points Yk

### 5 Architectural Improvements

- introduce two SBox architectures
- describe Area architecture
- describe Depth architecture
- motivate six scenarios of MULN
- describe scenario S0
- describe scenarios S1-S5
- motivate inversion over GF(24)
- derive Boolean expressions for inversion
- describe alpha-beta approach for top and bottom linear matrices
- apply alpha-beta approach to combined SBox
- utilize Q-Zero points for top matrices in combined SBox

### 6 Results and Comparisons

- present synthesis results
- compare forward SBoxes
- compare combined SBoxes
- conclude results

### CONCLUSIONS

- summarize contributions

## PART C OF THE DISCLOSURE

- motivate inversion over GF(24)
- derive improved inversion formulae
- present alternative equations for INV block

### APPENDIX E

- describe circuits using improved inversion formula

