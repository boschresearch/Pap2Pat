# DESCRIPTION

## BACKGROUND

- introduce flash memories
- describe market share
- discuss applications
- describe limitations
- explain block erasures
- discuss writing speed constraints
- motivate new modulation techniques

## SUMMARY

- introduce rank modulation scheme
- describe cell programming
- explain permutation-based data storage
- describe decoding process
- describe encoding process
- explain benefits of rank modulation
- describe error correction capabilities
- discuss modulation code generation
- preview other features and advantages

## DETAILED DESCRIPTION

- introduce rank modulation scheme

### I. INTRODUCTION TO RANK MODULATION

- motivate rank modulation
- describe rank modulation scheme
- explain virtual cell concept
- illustrate permutation ordering
- describe error correction challenges
- introduce concepts and motivation for rank modulation
- illustrate rank modulation coding scheme
- describe rewriting procedure
- highlight advantages of rank modulation coding
- discuss error correction and joint coding
- introduce error-correcting codes for rank modulation

### EXAMPLE 1

- illustrate rank modulation coding scheme
- show mapping from order to variable
- describe rewriting procedure
- illustrate rewriting example
- highlight single cell change
- illustrate charge levels
- describe rewriting process
- show variable change
- illustrate final charge levels

### II. DEFINITIONS AND NOTATION

- define flash memory cells
- define charge levels
- define ranks of cells
- define permutation
- define adjacent transposition
- define distance between permutations
- define Kendall Tau Distance
- define size of errors

### III. PROPERTIES AND BOUNDS

- study distance between permutations
- study coordinate representation
- study sizes of balls
- derive upper bound on error-correcting codes
- prove theorem on distance between permutations
- illustrate recursive algorithm for computing distance

### EXAMPLE 2

- introduce permutation examples
- calculate coordinates from permutations
- explain theorem 4
- prove theorem 4
- explain theorem 5
- prove theorem 5
- introduce theorem 6
- prove theorem 6

### IV. ERROR CORRECTION

- motivate rank modulation coding
- explain error tolerance
- discuss error correction necessity
- introduce error correction concept
- illustrate error correction example
- discuss error-correcting code properties
- present error-correcting code results

### V. ERROR-CORRECTING RANK MODULATION CODES

- define permutation adjacency graph
- study topology of permutations
- derive general construction for error-correcting rank-modulation codes
- present family of one-error-correcting codes
- define adjacency graph of permutations
- prove theorem 7
- prove other direction of theorem 7
- define linear array graph
- build bijective map between permutation vertices and linear array vertices
- prove theorem 8
- illustrate permutation adjacency graph for n=3 and n=4
- prove proposition 9
- show approach to designing error-correcting rank-modulation codes
- prove theorem 10
- generate error-correcting codes for rank modulation schemes
- present single-error-correcting rank-modulation code
- construct code C1
- construct code C2
- analyze code size of construction 11
- prove lemma 12
- prove lemma 13
- prove theorem 14

### VI. MORE CODES AND EMBODIMENTS

- report error correcting codes built using ad hoc constructions
- compare ad hoc constructions with sphere-packing upper bound and half-optimal code
- describe single-error-correcting code with two codewords for n=3
- describe ad hoc construction for single-error-correcting code with five codewords for n=4
- compare ad hoc construction with Construction 10 for n=4
- describe ad hoc constructions for single-error-correcting codes for n=5, 6, 7
- compare ad hoc constructions with Construction 11 for n=5, 6, 7
- describe two-error-correcting codes for n=5, 6, 7
- describe three-error-correcting codes for n=5, 6, 7
- describe four-error-correcting codes for n=5, 6, 7
- implement ad hoc techniques as operations
- generate and test permutations for suitability as error correcting codes
- retain permutations that correct a desired number of errors
- use conventional desktop or laptop computers for generating permutations
- compare efficiency of ad hoc techniques with Construction 11
- show operations for generating a rank modulation code
- generate n! permutations
- select a starting permutation
- generate coordinates of permutations
- test coordinates to determine if they satisfy conditions for indicating a valid codeword
- retain generated permutations having a distance greater than or equal to (2r+1)
- perform operations using a conventional desktop, server, or laptop computer
- show operations for decoding a codeword received over an information channel
- receive a rank modulation codeword
- determine if the received codeword comprises a valid codeword
- verify that a received codeword permutation comprises a valid codeword
- determine a valid codeword by checking against permutations that differ from the received codeword by a value r
- introduce rank modulation scheme
- describe decoding process
- determine valid codeword
- illustrate decoding process with example
- describe encoding process
- generate permutation corresponding to codeword
- provide permutation to data destination
- describe lookup table techniques for encoding
- illustrate memory device constructed according to rank modulation scheme
- describe memory controller operations
- describe error correcting code generation
- illustrate computer apparatus for performing operations
- describe computer system components
- describe user interface output devices
- describe user interface input devices
- describe communication subsystem
- describe file storage subsystem
- describe RAM and file storage subsystem
- describe software for communications over network
- describe various hardware and software configurations
- describe implementation of rank modulation scheme
- describe control logic in software or hardware
- describe information storage medium
- describe implementation in various systems
- illustrate data flow in memory device
- describe rank modulation controller operations
- describe interfaces for receiving and providing data values and codewords
- describe information values for physically representing data values and codewords
- describe memory cells for storing codewords
- describe transmitter/receiver for transmitting and receiving encoded signals
- describe modulation of signal components to define rank modulation code permutations
- describe error correction operations
- describe decoding operations
- describe encoding operations
- describe lookup table techniques
- describe memory device construction
- describe memory controller operations
- describe error correcting code generation
- describe implementation of rank modulation scheme

## CONCLUSION

- propose rank-modulation scheme
- discuss error-correcting codes
- suggest future developments
- claim scope of invention

