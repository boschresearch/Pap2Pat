# DESCRIPTION

## TECHNICAL FIELD

- relate to multiparty computation

## RELATED ART

- introduce multiparty computation
- motivate Yao's Millionaires' problem
- limitations of previous methods

## SUMMARY

- introduce secure integer comparison
- summarize first embodiment
- summarize second embodiment
- summarize third embodiment
- application of homomorphic encryption
- advantage of non-interactive protocol
- disclaimer on summary
- disclaimer on drawings

## DETAILED DESCRIPTION

- introduce secure integer comparison
- describe branching program implementation
- outline client-server interaction
- explain goal of computation
- discuss non-interactive protocol
- describe output expressiveness
- mention encrypted server input
- discuss third-party server evaluation
- outline statutory requirements
- describe claimed subject matter
- discuss minor variations
- introduce accompanying drawings
- describe embodiments
- outline HE scheme algorithms
- describe key generation
- explain encryption algorithm
- outline evaluation algorithm
- describe decryption algorithm
- discuss IND-CPA security
- outline correctness conditions
- describe FHE operations
- explain addition operation
- describe constant addition
- outline multiplication operation
- describe constant multiplication
- discuss SHE and leveled FHE
- introduce AHE schemes
- describe AHE properties
- outline protocol 100
- describe client-server interaction
- explain binary tree construction
- outline evaluation process
- describe result encryption
- discuss non-interactive protocol
- outline method 200
- describe key generation
- explain binary tree construction
- outline evaluation process
- describe result encryption
- outline method 300
- describe binary tree pruning
- create normal comparison binary tree
- build tree based on input size
- label leftmost path with server input bits
- create inner nodes with right child leaf nodes
- label inner nodes with Fβ(b)
- create normal comparison binary tree for AHE scheme
- create inverse normal comparison binary tree
- evaluate client input on binary tree
- compute decision bits
- return comparison results
- aggregate comparison bits
- store aggregation result at leaf nodes
- evaluate leaves for FHE scheme
- aggregate cost attribute at each leaf node
- compute product of cost and label value
- sum results across all leaf nodes
- send result to client
- evaluate leaves for AHE scheme
- randomize ciphertexts
- generate additional random ciphertexts
- permute ciphertexts
- send result to client
- decrypt result in FHE scheme
- parse result to obtain encrypted bit
- decrypt encrypted bit to obtain output
- describe method for decrypting result in AHE scheme
- parse result to obtain list of ciphertexts
- iteratively decrypt list of ciphertexts
- obtain output
- modify protocol for certain use cases
- handle AHE case wherein server input is zero
- modify protocol for shared output
- illustrate binary tree array
- evaluate binary tree array
- parse encrypted client input and server input
- store equality of current bits
- store negation of equality of current bits
- store Fβ(y[i])
- evaluate first row of evaluation array
- evaluate remaining rows of binary tree array
- process for FHE scheme
- process for AHE scheme
- sum third column of binary tree array
- send result to client for decryption
- permute third column for AHE scheme
- optimize implementation for constant case
- describe leveled FHE scheme
- evaluate direct acyclic graph
- compute dependency list table
- evaluate dependency list table
- reduce multiplication depth
- describe applications of protocol
- integrate protocol into larger application
- apply further operations to output
- send result for further applications
- run protocol with multiple clients
- describe secure auction setting
- pair auction participants
- determine highest bidder
- describe hardware platform
- illustrate computer components
- describe system bus
- describe central processing unit
- describe random-access memory
- describe graphics card
- describe network interface card

