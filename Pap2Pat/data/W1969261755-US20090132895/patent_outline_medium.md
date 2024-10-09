# DESCRIPTION

## BACKGROUND

- introduce flash memories
- limitations of flash memories
- need for new data storage modulation techniques

## SUMMARY

- introduce rank modulation scheme
- describe decoding process
- describe encoding process
- advantages of rank modulation scheme

## DETAILED DESCRIPTION

- introduce rank modulation scheme

### I. INTRODUCTION TO RANK MODULATION

- motivate rank modulation
- describe rank modulation scheme
- illustrate rank modulation scheme with example
- discuss advantages of rank modulation
- introduce error correction in rank modulation

### EXAMPLE 1

- illustrate rank modulation coding scheme
- describe procedure for rewriting data
- show example of rewriting data
- discuss optimization objective of rank modulation coding

### II. DEFINITIONS AND NOTATION

- define notations for flash memory cells
- define rank-modulation scheme
- define adjacent transposition and distance between permutations
- define permutation transition graph

### III. PROPERTIES AND BOUNDS

- study distance between permutations
- study coordinate representation of permutations
- derive upper bound on cardinality of error-correcting rank-modulation codes

### EXAMPLE 2

- illustrate permutation coordinates
- derive coordinates from permutation
- prove theorem on identical permutations
- prove theorem on coordinate existence

### IV. ERROR CORRECTION

- motivate rank modulation coding
- describe error correction concept
- illustrate error correction code example

### V. ERROR-CORRECTING RANK MODULATION CODES

- define permutation adjacency graph
- motivate theorem 7
- prove theorem 7
- define linear array graph
- build bijective map between permutation graph and linear array graph
- state theorem 8
- illustrate permutation adjacency graph for n=3 and n=4
- state proposition 9
- construct single-error-correcting rank-modulation code
- analyze code size of constructed code
- prove error-correcting capability of constructed code

### VI. MORE CODES AND EMBODIMENTS

- report error correcting codes built using ad hoc constructions
- compare ad hoc constructions with sphere-packing upper bound and half-optimal code
- describe ad hoc techniques for generating error correcting codes
- illustrate operations for generating a rank modulation code
- generate n! permutations
- select starting permutation
- generate coordinates of permutations
- test coordinates to determine valid codewords
- retain generated permutations having a distance greater than or equal to (2r+1)
- describe operations for decoding a codeword received over an information channel
- receive rank modulation codeword
- determine if received codeword comprises a valid codeword
- determine corresponding value of valid codeword
- describe decoding process for received codeword
- check valid coordinates for correct codeword
- determine corresponding permutation for valid codeword
- describe encoding process for data value
- generate permutation corresponding to codeword
- provide permutation to data destination
- describe lookup table technique for encoding
- illustrate memory device constructed according to rank modulation scheme
- describe memory controller operations
- describe error correcting code generation
- describe computer apparatus for performing operations
- describe user interface output and input devices
- describe communication subsystem
- describe file storage subsystem
- describe RAM and program product media
- describe software for network communications
- describe various hardware and software configurations
- describe implementation of rank modulation scheme
- illustrate data flow in memory device according to rank modulation scheme

## CONCLUSION

- summarize rank-modulation scheme
- future developments and scope

