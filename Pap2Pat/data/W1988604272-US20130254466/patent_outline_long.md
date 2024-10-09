# DESCRIPTION

## BACKGROUND

- introduce flash memories
- describe applications of flash memories
- discuss limitations of flash memories
- describe problems with flash memories
- discuss need for improvement

## SUMMARY

- introduce minimum push-up scheme
- describe data values and rank modulation coding scheme
- define n and S
- program rank locations according to scheme
- describe cell differentiation amount
- introduce multi-cells scheme
- describe NAND flash memory
- replace transistors with multi-cells
- increase read precision
- introduce processes for manufacturing and operating data device
- form connections between transistors
- store data in transistors
- introduce multi-permutations scheme
- generalize permutation-based scheme
- introduce new data representation and rewrite model
- describe construction of rank modulation codes

## DETAILED DESCRIPTION

- outline detailed description

### I. INTRODUCTION TO RANK MODULATION

- introduce flash memory cells
- motivate rank modulation
- describe rank modulation scheme
- explain programming process
- introduce rewriting codes
- motivate rewriting codes
- illustrate rewriting example
- explain consequence of rewriting
- introduce push-to-the-top operations
- discuss limitations of push-to-the-top
- summarize related work on error-correcting codes
- summarize related work on variations of rank modulation
- conclude introduction to rank modulation

### II. PERMUTATION “MINIMUM PUSH UP”

- introduce permutation "minimum push up"
- motivate reducing cell level increment
- describe example of "push-to-top" operation
- illustrate limitations of "push-to-top" operation
- introduce "minimal-push-up" operation
- describe "minimal-push-up" operation
- define rewrite model and transition graph
- introduce virtual levels
- describe discrete model for rewriting
- illustrate example of rewriting process
- describe cost of rewriting process
- illustrate example of rewriting cost
- discuss robustness of discrete model
- describe codes based on state transitions
- define cost of changing state
- compute cost of changing state
- illustrate example of rewriting cost
- state theorem 1
- prove theorem 1
- discuss equivalent definition of cost
- describe codes for rewriting data
- define decoding scheme
- define transition graph
- state theorem 2
- prove theorem 2
- discuss size of ball under infinity norm
- note out-degree of each vertex in transition graph
- introduce permutation "minimum push up"
- define cost of rewrite operation
- discuss case of n≦4
- present construction 1 for n=4
- prove theorem 3
- define prefk(B)
- provide lower bound for dominating set's size
- prove theorem 4
- discuss rate of full assignment code
- discuss case of n=5
- present construction 2 for n=5
- prove theorem 5
- discuss rate of code
- discuss case of r≦2
- generalize constructions for r=n−4
- illustrate method 600 of operating a data device
- receive data values to be stored
- define v as an element of S
- program group of n rank locations
- continue process

### III. MULTI-CELLS

- introduce multi-cell flash memory
- describe NAND flash memory
- propose replacing transistors with multi-cells
- explain read operations in multi-cells
- explain write operations in multi-cells
- discuss error rates in multi-cells
- calculate instantaneous and total capacity with trivial scheme
- discuss update schemes with relative cell levels
- introduce notations and model properties
- define discrete levels for cell charge values
- define permutation of cell levels
- explain how to change permutation
- define cost of changing cell state
- provide example of cost calculation
- define update scheme and update code
- define decoding function and update function
- define instantaneous capacity
- define worst-case total capacity per level
- define average total capacity per level
- define Bn,r(σ) and kn,r
- derive upper bound for Cw and Cα
- derive bound for Ci in worst case
- prove Kr/r is strictly decreasing
- derive upper bound for Cα in average case
- prove limq/n,n→∞Cα()≦K1
- prove limn→∞Ci()≦K1 if Cα()→K1
- motivate multi-cells
- construct code for average case
- define instantaneous capacity
- derive instantaneous capacity
- describe permutation based update code
- define decoding function
- describe update function
- provide example of decoding and update
- analyze update cost
- calculate probability of update cost
- show expected cost of update algorithm
- prove existence of code for worst case
- define instantaneous capacity of code
- show worst-case update cost is 1
- use random coding method
- calculate probability of no good sequence
- describe process for manufacturing and operating data device
- dispose transistors on device
- form connections between sources and drains
- store data in transistors
- describe process for operating data device
- generate and store code word

### IV. MULTI-PERMUTATIONS

- generalize paradigm of representing information with permutations
- introduce multi-permutations with relative levels
- define multi-permutations with equal multiplicities
- prove upper bound on total capacity
- prove existence of construction approaching bound
- note limitations of update scheme without relative levels
- introduce Compressed Rank Modulation scheme
- review original rank modulation scheme
- define Compressed Rank Modulation scheme
- illustrate Compressed Rank Modulation scheme
- highlight advantage of Compressed Rank Modulation
- provide example of Compressed Rank Modulation
- compare Compressed Rank Modulation with original rank modulation
- discuss advantages of Compressed Rank Modulation
- introduce initial write process
- describe programming method for initial write
- introduce subsequent rewrites process
- describe programming method for subsequent rewrites
- discuss programming symmetric cells
- introduce rebalancing permutations
- describe method for rebalancing permutations
- provide example of rebalancing permutations
- discuss storing metadata for rebalancing
- introduce record weights approach
- describe method for record weights approach
- discuss storing weight distribution as metadata
- discuss storing vector as compressed rank modulation permutation
- note extension of compressed rank modulation scheme
- conclude discussion of Compressed Rank Modulation scheme

## EXAMPLES

- depict process for operating data device
- depict process for reading data device
- depict process for writing to data device
- define operations within each process

## VI. RANK-MODULATION REWRITING CODES

- introduce rank-modulation rewriting codes
- motivate polar codes
- define rewrite model
- introduce discrete model
- define cell-state vector
- define multiplicity vector
- define multipermutation
- derive multipermutation
- define valid multipermutations
- introduce programming method
- minimize cell charge levels
- define initial state
- define rewriting codes
- define encoding function
- define decoding function
- state constraints
- define instantaneous rate
- define sum-rate
- state goals
- describe construction
- constrain maximum level increase
- avoid overshooting
- encode value of c'
- define sequence of functions
- relate to binary write-once memory problem
- introduce WOM codes
- use polar WOM codes
- bound deviation of non-programmed cells
- describe storage of flipped cells
- introduce rank-modulation rewriting codes
- limitations of polar WOM codes
- construction of rank-modulation rewriting codes
- define encoding function f
- define decoding function g
- encoding of k-th rank
- update information cells vector
- update redundancy cells vector
- decoding of k-th rank
- alternative trade-off between rate and number of writes
- prove correctness of Construction 1
- lemma 1: multipermutation property of redundancy cells
- lemma 2: multipermutation property of information cells
- lemma 3: correctness of encoding and decoding functions
- theorem 1: Construction 1 is an (N',q,T,D,Z) rank-modulation rewriting code
- prove theorem 1
- discuss WOM codes satisfying Assumption 1
- sketch modifications to adjust WOM codes to Construction 1
- conclude Construction 1

### C. Polar WOM Codes

- introduce polar WOM codes
- motivate use for WOM implementation
- describe construction of polar WOM codes
- define polar codes and their usage
- introduce Arikan's channel polarization
- define sub-channels and Bhattacharyya parameter
- describe frozen set and encoding process
- explain successive cancellation scheme
- show reliability of polar codes
- apply polar codes to lossy source coding
- define frozen set for lossy source coding
- describe compression and decompression process
- introduce multiple writes WOM codes
- define test channel and probability transition function
- design polar code for t-th test channel
- describe encoding and decoding process
- state theorem on reliability of polar WOM codes
- introduce lemma on WOM property
- propose construction for code p,∈ of Assumption 1
- prove properties of code p,s
- conclude proof of Lemma 5
- prove lemma 4
- verify property
- analyze sum-rate of construction 1
- derive instantaneous rate
- discuss limitations of instantaneous rate
- introduce lemma 6
- define typical distortion
- describe strong typical sequences
- prove lemma 6
- describe properties of construction 1
- state theorem 3
- prove theorem 3
- discuss encoding and decoding complexities
- describe error handling strategies
- introduce process 1520
- describe block 1527
- describe block 1529
- describe block 1531
- describe block 1533
- describe block 1535
- describe block 1537
- describe block 1539
- introduce process 1545
- describe block 1549
- describe block 1551
- describe block 1553
- describe block 1555

## VI. EXAMPLE EMBODIMENTS

- illustrate data device constructed in accordance with the present disclosure
- describe memory and memory controller
- describe microcontroller and memory interface
- describe host interface and data buffer
- describe error correcting code (ECC) block
- describe operations of decoding data and encoding data
- illustrate operations of FIGS. 6, 8A, 8B, 14 and 15
- describe implementation of rank modulation coding scheme in a USB thumb drive
- describe processing components such as controller and microcontroller
- describe host device
- illustrate computer apparatus sufficient to perform as a host device
- describe computer system
- describe system bus and storage subsystem
- describe memory subsystem and file storage subsystem
- describe user interface output devices and user interface input devices
- describe communications subsystem
- describe file storage subsystem and direct access storage devices
- describe user interface input devices
- describe communications subsystem and external systems
- describe RAM and file storage subsystem
- describe software that enables communications over a network
- describe computer system configurations
- describe microprocessors and operating systems
- describe implementation of techniques
- describe control logic in software or hardware
- describe information storage medium

## VII. CONCLUSION

- summarize disclosure
- describe programming method
- describe flash cell structure
- describe update codes
- describe modifications and variations
- describe appended claims
- describe use of plural and singular terms
- describe introductory phrases
- describe definite articles
- describe convention analogous to "at least one of A, B, and C, etc."
- describe Markush groups
- describe ranges and subranges

