# DESCRIPTION

## TECHNICAL FIELD

- introduce AES and SBox

## BACKGROUND

### Technical Background/Existing Technology

- describe AES algorithm
- explain hardware implementations of AES
- introduce SBox and its importance
- discuss previous work on SBox implementation
- describe the need for efficient SBox implementation
- summarize previous research on SBox

## SUMMARY

- motivate low-depth SBox implementation
- introduce invention for SBox functionality

## DETAILED DESCRIPTION

- introduce SBox architecture

### PART A

- define classical SBox architecture
- describe Tower Field construction
- derive element inversion in GF(2^8)
- introduce Architecture D
- describe Architecture D block diagram
- explain first circuit part
- explain second circuit part
- explain third circuit part
- compare Architecture D with conventional architecture

## PART B OF THE DISCLOSURE

- introduce AES SBox and its importance in cryptographic systems

### 1 Introduction

- motivate need for efficient hardware design of AES SBox
- discuss previous work on AES SBox implementation

### 2 Preliminaries

- define mathematical notation and representation for AES SBox

### 3 Circuits for Binary Linear System of Equations

- state basic problem of linear circuit minimization
- introduce cancellation-free heuristics for linear circuit minimization
- discuss solving additional input requirement (AIR) and additional output requirement (AOR)
- introduce probabilistic heuristic approach for linear circuit minimization
- discuss cancellation-allowed heuristics for linear circuit minimization
- introduce exhaustive search methods for linear circuit minimization
- discuss optimizations and conclusions for linear circuit minimization

### 4.1 Floating Multiplexers

- motivate floating multiplexers
- describe metrics and linear expressions to solve

### 4.2.1 Problem Statement

- define problem statement
- introduce input and output signals
- define delay constraints
- introduce masking vectors

### 5 Architectural Improvements

- propose two SBox architectures
- describe six scenarios for MULN block
- present inversion formulae over GF(24)
- introduce alpha-beta approach for top and bottom linear matrices
- discuss Q-zero points for top matrices in combined SBox

### 6 Results and Comparisons

- present synthesis results for forward SBoxes
- present synthesis results for combined SBoxes

### CONCLUSIONS

- summarize contributions to minimizing AES SBox circuit realization

## PART C OF THE DISCLOSURE

- extend inversion circuit

### APPENDIX E

- present improved inversion circuits

