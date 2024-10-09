# DESCRIPTION

## BACKGROUND

- introduce flash memories
- describe market share of flash memories
- discuss applications of flash memories
- describe limitations of flash memories
- discuss problems with flash memories
- identify need for new data storage techniques

## SUMMARY

- introduce rank modulation scheme
- describe goal of rank modulation scheme
- define rank of cell
- explain how rank modulation scheme stores information
- describe how to write data into cells
- explain benefits of rank modulation scheme
- describe encoding process
- explain how encoding can correct errors
- summarize advantages of rank modulation scheme

## DETAILED DESCRIPTION

- outline detailed description

### I. INTRODUCTION TO RANK MODULATION

- introduce rank modulation scheme
- define virtual cell
- explain permutation ordering
- illustrate with example
- describe current technology
- explain flash memory cells
- describe multi-level storage
- explain block erasure
- list limitations of current technology
- motivate rank modulation coding
- define rank modulation coding
- explain partial order of cell levels
- describe rewriting procedure
- illustrate with example

### Example 1

- illustrate rank modulation coding scheme
- mapping from order of cell levels to variable
- procedure for rewriting
- example of rewriting
- limitations of current storage approach
- motivation for rank modulation coding
- features of rank modulation coding
- application to multilevel flash memory devices
- error correction techniques
- joint coding of data
- error-correcting codes
- controlled charge leakage
- research topics relating to rank modulation coding
- optimizing cell-programming speed
- iterative programming process
- modeling cell-level increase
- probability density function
- simulation results
- avoiding over-programming
- final cell level constraint
- average number of rounds
- improving cell-programming speed
- optimizing storage capacity
- asymmetric errors
- simplified model of asymmetric errors
- margin between cell levels
- reduction in gap
- optimizing data modification capability
- rewriting data efficiently
- current flash file systems
- garbage-collection mechanism
- rewriting data locally
- maximizing number of rewrites
- joint coding
- designing rank modulation codes
- rewriting and Gray codes
- Gray code constructions

### II. DEFINITIONS AND BASIC CONSTRUCTION

- define state space and transition functions
- define gray code
- introduce rank modulation scheme
- define push-to-the-top operation
- introduce set of transition functions
- define length-n Rank Modulation Gray Codes (n-RMGC)
- provide example of 3-RMGC
- motivate application of Gray codes
- describe realization of logic multi-level cells
- illustrate RMGC coding scheme
- introduce basic recursive construction for n-RMGCs
- define recursion basis
- assume cyclic and complete (n−1)-RMGC
- construct first block of permutations
- prove lemmas for block construction
- construct remaining blocks and complete n-RMGC
- conclude existence of cyclic and complete n-RMGC

### III. BALANCED n-RMGCs

- define balanced n-RMGC
- construct balanced n-RMGC from (n-1)-RMGC
- prove cyclic and complete properties of Cn
- define jump cost of n-RMGC
- prove lowest jump cost is at least n+1
- call n-RMGC with jump cost n+1 a balanced n-RMGC
- define abstract transition {right arrow over (ti)}
- prove cyclic and complete properties of {right arrow over (ti)}
- define transition tj in p-th programming cycle
- prove Cn is cyclic and complete
- prove Cn is balanced
- define theorem 7
- prove theorem 7
- provide example 8
- define successor function
- describe successor function in pseudocode
- prove theorem 10
- define ranking permutations
- review factoradic numbering system
- define b-factoradic numbering system
- provide equation (1) for rank calculation
- describe permutation with rank 0
- provide example 11
- describe procedure to find b-factoradic representation
- describe procedure to go from b-factoradic to permutation
- describe factoradic-to-bfactoradic procedure
- describe unranking procedure
- provide pseudocode for factoradic-to-bfactoradic
- provide pseudocode for unranking
- describe logic cell as counter
- describe average number of steps in successor function
- describe importance of average number of steps
- conclude balanced n-RMGC construction

### IV. REWRITING WITH RANK-MODULATION CODES

- introduce rank-modulation scheme
- define interpretation function
- define update function
- motivate push-to-the-top operations
- define cost of changing states
- define worst-case rewrite cost
- define average rewrite cost
- present lower bound on worst-case rewrite cost
- define transition graph
- prove properties of transition graph
- present optimal code construction
- define prefix sequence and prefix set
- construct update function
- prove optimality of code construction

### V. OPTIMIZING AVERAGE REWRITE COST

- introduce prefix-free code
- define prefix-free code
- describe tree diagram representation
- introduce full permutation tree T
- define subtree C of T
- define average codeword length
- introduce objective to minimize average codeword length
- discuss limitations of Huffman code
- present dynamic-programming algorithm
- define functions opti(x, m)
- provide recursions for opti(x, m)
- illustrate computation of opt2(4, 3)
- compute opt2(4, 3)
- discuss determination of optimal code tree
- introduce application of prefix-free code for rewriting
- introduce performance analysis
- bound average rewrite cost of any code
- define average rewrite cost of stored symbol i
- lower bound average rewrite cost
- introduce intermediary prefix-free code Z(i)
- define properties of Z(i)
- introduce prefix-free code A
- bound average rewrite cost of A
- prove existence of Z(i)
- state Kraft-McMillan inequality
- define sequence of integers rm
- prove non-negativity of rm
- prove sum of rm is n!/2
- discuss partition of alphabet letters
- state existence of prefix-free code
- conclude performance analysis
- define average rewrite cost
- motivate proof
- derive equation (3)
- calculate values of R(n)
- prove R(n) monotonically decreases
- define Z(i)
- prove properties P.1 and P.2 hold for Z(i)
- state main theorem
- define l' and input alphabet
- set probability distribution
- define A' and prove ξA(i)≦ξA'(i)
- apply inequality (2) and prove theorem
- state corollary
- define sequence of numbers qm
- prove qm are non-negative
- prove equivalent of Lemma 24
- prove Q(n) monotonically decreases

### VI. JOINT CODING FOR LOAD BALANCING

- introduce load balancing challenge
- motivate joint modulation of variables
- illustrate separate coding approach
- analyze performance of separate coding
- introduce joint coding approach
- describe cell arrangement in joint coding
- explain row types in joint coding
- detail variable representation in joint coding
- describe rewriting process in joint coding
- analyze performance of joint coding
- compare joint coding with separate coding
- generalize joint coding to multiple variables
- highlight benefits of joint coding for load balancing
- distinguish joint coding from wear-leveling techniques

### VII. OPERATION AND EMBODIMENTS

- introduce data storage device
- describe device components
- explain data reception and transmission
- illustrate flow diagram of operations
- determine permutation of codeword
- generate permutation A
- provide permutation to data destination
- store ai values in storage elements
- represent virtual cell by signal features
- perform read sequence of operations
- receive permutation and determine data value
- compare stored charge levels
- identify highest charge level
- determine permutation A
- perform program sequence of operations
- increase stored charge level
- perform joint coding operations
- map permutations to data items
- perform partial ordering
- designate index cells and reference cells
- perform uniform stored charge reduction
- decrease stored charge levels
- read operations of data storage device
- determine stored charge levels
- compare stored charge levels
- map permutation to data value
- provide data value over data channel
- implement rank modulation code for signal
- describe rank modulation code
- implement for information channel
- illustrate data device
- describe memory controller
- describe microcontroller
- describe data buffer
- describe ECC block
- describe error correction operations
- describe operations for decoding data
- describe operations for encoding data
- describe data storage device
- describe host device
- describe computer apparatus
- describe processing components
- describe computer system
- describe storage subsystem
- describe user interface output devices
- describe user interface input devices
- describe communications subsystem
- describe tangible media
- describe software for communications
- describe hardware configurations
- describe operating systems
- describe control logic
- describe information storage medium
- describe rank modulation scheme
- describe data flow
- describe RM controller
- describe information values

### VIII. CONCLUSION

- summarize rank modulation
- illustrate embodiments
- claim scope of invention

