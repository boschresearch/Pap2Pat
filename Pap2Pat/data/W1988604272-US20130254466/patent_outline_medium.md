# DESCRIPTION

## BACKGROUND

- introduce flash memories
- limitations of flash memories

## SUMMARY

- introduce minimum push-up scheme
- describe rank modulation coding scheme
- introduce multi-cells for storing data
- describe process for manufacturing and operating data device
- introduce multi-permutations for storing data
- describe computer method of operating data device
- introduce new data representation and rewrite model
- describe computer method of operating data device using WOM code

## DETAILED DESCRIPTION

- outline sections

### I. INTRODUCTION TO RANK MODULATION

- introduce flash memory cells
- motivate rank modulation
- describe rank modulation scheme
- explain rewriting codes
- illustrate rewriting examples
- discuss prior work on rank modulation

### II. PERMUTATION “MINIMUM PUSH UP”

- introduce permutation "minimum push up"
- motivate reducing cell level increment
- describe "push-to-top" operation
- illustrate "push-to-top" operation with example
- introduce "minimal-push-up" operation
- describe "minimal-push-up" operation
- illustrate "minimal-push-up" operation with example
- define rewrite model and transition graph
- describe discrete model for rewriting
- provide example of rewriting cost
- discuss robustness of discrete model
- describe codes based on state transitions
- define decoding scheme and transition graph
- introduce permutation "minimum push up"
- motivate case of n≦4
- describe construction 1 for n=4
- prove theorem 3 for construction 1
- provide lower bound for dominating set size
- motivate case of n=5
- describe construction 2 for n=5
- prove theorem 5 for construction 2
- generalize constructions for r≦2
- describe method 600 of operating a data device

### III. MULTI-CELLS

- introduce multi-cell flash memory
- describe NAND flash memory
- propose replacing transistors with multi-cells
- explain read and write operations in multi-cells
- calculate instantaneous and total capacity with multi-cells
- introduce notations and model properties
- define permutation and cost of update
- provide example of update operation
- define update scheme and decoding function
- derive upper bound for worst-case total capacity
- prove lemma for decreasing Kr/r
- derive upper bound for average total capacity
- prove theorem for optimizing Ci()
- motivate multi-cells
- construct code for average case
- describe decoding function
- describe update function
- provide example of decoding and update
- analyze expected cost of update
- prove existence of code for worst case
- describe random coding method
- illustrate process for manufacturing and operating data device
- illustrate process for operating data device
- conclude with asymptotic optimality of code

### IV. MULTI-PERMUTATIONS

- generalize paradigm of representing information with permutations
- introduce multi-permutations scheme
- describe advantages of rank modulation
- introduce Compressed Rank Modulation scheme
- explain assignment of ranks to cells
- illustrate Compressed Rank Modulation with examples
- compare Compressed Rank Modulation with original rank modulation
- discuss initial write in Compressed Rank Modulation
- describe subsequent rewrites in Compressed Rank Modulation
- explain programming symmetric cells
- discuss rebalancing permutations
- illustrate rebalancing with an example
- discuss record weights approach
- conclude Compressed Rank Modulation scheme

## EXAMPLES

- depict data device operation processes
- illustrate data device read and write processes

## VI. RANK-MODULATION REWRITING CODES

- motivate rank-modulation rewriting codes
- define rewrite model
- introduce multipermutations
- define multiplicity vector
- derive multipermutation from cell-state vector
- describe programming method
- define rewriting codes
- describe goals of code design
- constrain maximum level increase
- choose encoding function
- relate to binary write-once memory problem
- use polar WOM codes
- flip cells to get desired weight
- store flipped cell indices in redundancy cells
- introduce rank-modulation rewriting codes
- define construction 1
- describe encoding function f
- describe decoding function g
- prove correctness of construction 1
- prove lemma 1
- prove lemma 2
- prove lemma 3
- prove theorem 1

### C. Polar WOM Codes

- introduce polar WOM codes
- motivate polar codes for lossy source coding
- define polar codes and their usage
- describe construction of polar WOM codes
- explain usage of polar codes for lossy source coding
- define frozen set and its usage
- describe encoder and decoder for polar WOM codes
- state theorem on reliability of polar WOM codes
- prove lemma on properties of polar WOM codes
- propose construction for code p,∈ of Assumption 1
- prove lemma
- analyze sum-rate of construction
- define typical distortion
- prove lemma 6
- describe properties of construction 1
- state theorem 3
- prove theorem 3
- describe encoding and decoding complexities
- describe error handling strategies
- depict process 1520 for operating a data device
- depict process 1545 for operating a data device
- depict process 1560 for operating a data device
- depict process 1584 for operating a data device

## VI. EXAMPLE EMBODIMENTS

- illustrate data device constructed in accordance with the present disclosure
- describe memory and memory controller components
- detail microcontroller operations
- illustrate data storage device components
- describe computer apparatus sufficient to perform as a host device
- detail computer system components
- describe user interface output and input devices
- illustrate communication subsystem components
- describe file storage subsystem components
- detail RAM and file storage subsystem operations
- illustrate software configurations for communications over a network
- describe various hardware and software configurations
- illustrate implementation of control logic in software or hardware

## VII. CONCLUSION

- summarize programming method for rank modulation
- describe flash cell structure for high number of updates
- summarize update codes based on permutations of relative levels
- describe scope of the disclosure
- clarify terminology and claim language
- provide general statements on ranges and Markush groups

