# DESCRIPTION

## BACKGROUND

- introduce graph analytics
- limitations of CSR representation
- motivate mutable CSR-based representations
- describe delta maps and log-based representations
- summarize alternative data structures
- describe existing systems for graph representation

## SUMMARY

- introduce mutable multilevel data structure
- describe read-only levels and writable level
- define vertex table and edge table
- describe edge table contents
- motivate level 0 representation
- introduce performance-optimized variant
- introduce space-optimized variant
- describe hybrid variant
- motivate copy policies
- describe copy-on-write arrays
- summarize computation options
- describe graph processing module

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce mutable multilevel data structures
- describe variants and applications

### Compressed Sparse Row Representation

- introduce compressed sparse row representation
- describe limitation of CSR representation
- define graph structure
- represent graph structure as sparse matrix
- describe CSR representation
- illustrate CSR representation with example
- describe vertex table
- describe edge table
- calculate length of adjacency list
- store node properties
- store edge properties
- add mutability to CSR representation
- describe delta map
- implement delta map as hash table
- run graph analytics on CSR representation and delta map
- describe log-based variant of CSR representation
- modify CSR representation to add mutability
- treat edge table as log
- append updated adjacency list to edge table
- update vertex table
- describe performance of log-based CSR representation
- create holes in edge table
- perform compaction operation
- add delta map to log-based CSR representation
- illustrate changes to graph in log-based CSR representation
- describe mutable multilevel data structures
- design mutable multilevel data structures for various workloads
- implement read-only levels of mutable multilevel data structures
- implement single writable level of mutable multilevel data structures
- illustrate example implementation of mutable multilevel data structure
- introduce compressed sparse row representation
- describe mutable multilevel data structure
- illustrate method for accessing mutable multilevel data structure
- describe read access with fresh data
- describe read access without fresh data
- describe write access
- introduce edge table array
- describe optimization for graph processing algorithms
- introduce three approaches for representing edge tables
- describe software copy-on-write approach
- introduce vertex table
- describe vertex table implementation
- introduce performance-optimized variant
- describe delta map
- describe creation of new CSR-like data structure
- describe copy-on-write approach for vertex table
- illustrate two-level representation of graph
- describe level 0 CSR representation
- describe level 1 CSR representation
- describe differences between level 0 and level 1 CSR representations
- describe adjacency list lengths
- compare performance-optimized variant with existing data structures
- introduce space-optimized variant
- describe splitting adjacency lists over multiple edge tables
- describe indirection table
- describe log-based data structures
- describe concurrent computations on different levels
- describe traversing multiple levels to reconstruct adjacency lists
- describe graph processing module
- describe operations performed by graph processing module
- describe request to perform computations on graph structure
- illustrate method for reconstructing adjacency list
- describe checking vertex table entry
- describe traversing multiple levels to reconstruct adjacency list
- describe locating first element of adjacency list
- describe adding elements to adjacency list
- describe completing construction of adjacency list
- describe feedback loop for adding elements
- conclude method for reconstructing adjacency list

### Creating a New Read-Only Level

- create new read-only level
- trigger creation by time or modifications
- create from single writable level
- use delta map or other representation
- create periodically or by size of delta map
- create by explicit call or function
- create for fresher data or speedup
- provide explicit command or API
- invoke by administrator or operating system
- merge two read-only levels
- compact mutable multilevel data structure
- illustrate method in flow diagram
- create copy-on-write enabled clone
- allocate new array for edge table
- write updated adjacency list
- update vertex table
- clear single writable level
- execute concurrently with graph analytics

### Merging Read-Only Levels

- merge read-only levels to consolidate space
- iterate over edge tables to produce merged edge table
- compute merge-translation map
- merge vertex table and update accordingly
- merge vertex and edge properties
- merge all read-only levels to build new level 0

### Space-Optimized Design

- introduce space-optimized variant
- trade performance for low memory overhead
- describe merging of read-only levels
- add new outgoing edges to edge set
- store only newly added edges
- reconstruct adjacency list
- examine multiple levels
- add pre-computed node degree
- speed up graph processing algorithms
- add deletion vector
- store indication of edge deletion
- use logical timestamps
- facilitate multi-version access
- examine deletion vectors
- determine whether edge has been deleted
- describe FIG. 8
- illustrate two-level representation
- describe level 0 CSR representation
- describe level 1 CSR representation
- illustrate changes to graph structure
- describe deletion of edge
- describe addition of new edge
- reconstruct adjacency list
- examine level 1
- examine level 0
- ignore deleted edge
- add edge to adjacency list
- describe pseudo-code
- reconstruct adjacency list
- examine levels
- skip levels without adjacency list fragments
- describe property of approach
- examine levels with adjacency list fragments
- describe space-optimized variant
- suit workloads with busy nodes
- describe social media network example
- describe duplication of data
- describe reconstruction operation
- describe flow diagram in FIG. 9A
- begin at query level
- check vertex table entry
- reconstruct adjacency list

### Parameterized Design

- introduce hybrid representation
- describe performance-optimized variant
- describe space-optimized variant
- introduce copy-large policy
- introduce copy-small policy
- describe hybrid design
- describe decision-making process for copying adjacency lists
- introduce degree cutoff
- describe copy-on-delete policy
- introduce additional bit for vertex table
- describe reconstruction of adjacency lists
- introduce two-parameter hybrid variant
- describe creation of new read-only level
- evaluate vertex for copying adjacency list
- determine copy mode configuration
- compare degree to threshold
- copy entire adjacency list
- copy modified edges only
- repeat for additional vertices
- complete creation of new read-only level
- describe configurability of parameters
- describe dynamic adjustment of parameters

### Copy-on-Write Arrays

- introduce copy-on-write arrays
- describe split into fixed-size pages
- introduce indirection table
- describe access to elements
- illustrate copy-on-write array
- describe indirection table at each level
- describe data pages at each level
- describe edge table array
- describe vertex table array
- describe traversal of copy-on-write vertex table
- locate target data page
- locate element on target page
- evaluate performance of copy-on-write design
- describe limitations of hardware-assisted implementation

### Persistent Representations of the Mutable Multilevel Data Structures

- introduce persistent representations
- describe in-memory representation
- describe memory mapping and demand paging
- describe storage of mutable multilevel data structures
- introduce default number of consecutive levels per file
- describe on-disk representation of copy-on-write array
- describe header with metadata
- describe indirection table
- describe data pages
- describe loading data into memory
- describe accessing elements
- describe allocation of copy-on-write array
- describe invariants of copy-on-write array

### The Writable Level

- introduce writable level
- motivate delta map implementation
- describe log of modifications
- summarize data structure options
- motivate batch application of modifications
- describe creation of new read-only level
- introduce copy-on-write arrays
- describe indirection table and data pages
- motivate demand allocation of data pages
- describe vertex table and vertex objects
- introduce fine-grained latching scheme
- describe compare-and-swap operation
- motivate spin-lock mechanism
- describe coordination of concurrent writes
- introduce growable arrays of edges
- describe method for managing changes
- illustrate method with flow diagram

### Sliding Window

- introduce sliding window concept
- describe benefits of sliding window
- explain how to maintain sliding window
- introduce space-optimized variant
- describe how to advance sliding window
- explain how to delete old read-only levels
- provide example of sliding window usage
- describe how to create new read-only level
- explain how to set lowest level
- discuss level identifier values
- describe how to reuse level identifiers
- introduce evaluation section
- describe evaluation methodology
- introduce graph analytics algorithms
- describe triangle counting algorithm
- describe page ranking algorithm
- describe Markov chain algorithm
- describe single-source shortest path algorithm
- categorize algorithms into structure-light and structure-heavy
- describe performance-optimized variant
- describe space-optimized variant
- describe hybrid variant
- evaluate performance-optimized variant
- evaluate space-optimized variant
- evaluate hybrid variant
- compare performance of variants
- discuss memory usage of variants
- describe delta map implementation
- evaluate delta map implementation
- discuss benefits of hybrid variant
- describe policy for copying adjacency lists
- evaluate policy for copying adjacency lists
- discuss trade-offs between memory and performance
- describe use of mutable multilevel data structures
- discuss flexibility of mutable multilevel data structures
- describe use of mutable multilevel data structures for graph processing
- discuss benefits of mutable multilevel data structures
- describe computing system for implementing mutable multilevel data structures
- describe computer program product for implementing mutable multilevel data structures
- describe machine-readable storage medium for storing program instructions
- describe processor for executing program instructions
- describe cache hierarchy for processor
- describe persistent storage devices for storing graph structure
- describe system memory for storing program instructions
- describe program instructions for creating and using mutable multilevel data structures
- describe application for processing graph structure
- describe shared libraries for implementing graph processing
- describe operating system for managing computer system
- describe compiler for compiling program instructions
- describe graph processing module for performing operations on mutable multilevel data structures
- describe contention manager for managing concurrent access
- describe transaction support library for implementing atomic transactions
- describe private and shared memory locations for storing data

