# DESCRIPTION

## BACKGROUND

- introduce flash memories
- limitations of flash memories
- need for new data storage techniques

## SUMMARY

- introduce rank modulation scheme
- describe encoding process
- advantages of rank modulation scheme
- summarize benefits of rank modulation scheme

## DETAILED DESCRIPTION

- outline detailed description

### I. INTRODUCTION TO RANK MODULATION

- introduce rank modulation scheme
- motivate rank modulation
- describe memory cell arrangement
- explain current flash memory technology
- limitations of current flash memory technology
- motivate rank modulation coding
- introduce basic concepts of rank modulation coding

### Example 1

- illustrate rank modulation coding scheme
- describe mapping from order of cell levels to variable
- introduce rewriting procedure
- motivate rank modulation scheme
- describe limitations of conventional flash memory devices
- introduce error correction techniques for multilevel flash memory devices
- describe errors in rank modulation data scheme
- propose joint coding of data to improve load balance
- propose error-correcting codes to improve data reliability
- describe controlled charge leakage to lower cell levels
- introduce research topics relating to rank modulation coding
- optimize cell-programming speed
- model cell-level increase by truncated Gaussian distribution
- optimize storage capacity due to tolerance of asymmetric errors
- describe asymmetric errors that change cell levels in one direction
- optimize data modification capability
- describe rewriting data efficiently in terms of rewriting time and storage capacity
- propose rank-modulation scheme to eliminate overshooting and memory endurance problems

### II. DEFINITIONS AND BASIC CONSTRUCTION

- define state space and transition functions
- introduce gray code and its properties
- define rank modulation scheme and state space
- describe basic minimal-cost operation and transition functions
- introduce length-n Rank Modulation Gray Codes (n-RMGC)
- provide example of 3-RMGC and its application
- describe recursive construction for n-RMGCs
- prove existence of cyclic and complete n-RMGC for every integer n≧2

### III. BALANCED n-RMGCs

- define balanced n-RMGC
- construct balanced n-RMGC from (n-1)-RMGC
- prove cyclic and complete properties of Cn
- define jump cost of n-RMGC
- prove lower bound of jump cost
- define balanced n-RMGC
- prove existence of cyclic, complete, and balanced n-RMGC
- illustrate example of balanced 4-RMGC
- define successor function
- describe pseudocode for successor function
- prove asymptotic optimality of successor function
- review factoradic numbering system
- introduce b-factoradic numbering system
- describe ranking permutations in b-factoradic
- illustrate example of b-factoradic representation
- describe factoradic-to-bfactoradic and unranking procedures

### IV. REWRITING WITH RANK-MODULATION CODES

- motivate rank-modulation scheme
- define interpretation and update functions
- define cost of changing states
- define worst-case and average rewrite costs
- present lower bound on worst-case rewrite cost
- construct optimal code
- prove optimality of constructed code

### V. OPTIMIZING AVERAGE REWRITE COST

- introduce prefix-free code
- define prefix-free code
- describe tree diagram representation
- define average codeword length
- motivate dynamic-programming algorithm
- describe algorithm
- provide example of algorithm
- analyze performance of prefix-free code
- bound average rewrite cost
- define intermediary prefix-free code Z(i)
- require properties of Z(i)
- compare Z(i) with optimal prefix-free code A
- prove approximation ratio
- apply Kraft-McMillan inequality
- conclude existence of Z(i)
- define average rewrite cost
- motivate proof of theorem 26
- prove theorem 26
- state corollary 27
- prove theorem 28
- state corollary 29
- define sequence of numbers
- prove lemma 30

### VI. JOINT CODING FOR LOAD BALANCING

- motivate load balancing
- illustrate separate coding approach
- introduce joint coding approach
- describe joint coding method
- analyze joint coding performance
- generalize joint coding to multiple variables
- discuss application of joint coding

### VII. OPERATION AND EMBODIMENTS

- describe data storage device
- illustrate data storage device components
- explain data storage device operation
- determine permutation of codeword
- generate permutation A
- provide permutation to data destination
- store ai values in storage elements
- perform read sequence of operations
- receive permutation and determine data value
- perform program sequence of operations
- receive data and program into device
- describe joint coding operations
- perform uniform stored charge reduction operation
- illustrate reading and programming operations
- describe rank modulation code implementation
- illustrate data device construction
- detail memory controller operation
- describe error correction operations
- illustrate computer system embodiment
- detail system components
- describe user interface components
- illustrate communication subsystem
- describe software and hardware configurations
- illustrate rank modulation scheme implementation
- describe encoding and decoding operations
- illustrate data flow in data device
- describe information values representation
- illustrate source/destination block operation

### VIII. CONCLUSION

- summarize rank modulation scheme

