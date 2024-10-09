# DESCRIPTION

## BACKGROUND

- introduce graph analytics
- limitations of CSR representation
- overview of existing graph representations

## SUMMARY

- introduce mutable multilevel data structure
- describe read-only levels and writable level
- explain edge table and vertex table
- discuss variants of mutable multilevel data structure
- describe hybrid variant and copy policies
- outline usage and implementation of mutable multilevel data structure

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce mutable multilevel data structures

### Compressed Sparse Row Representation

- introduce CSR representation
- describe limitations of CSR representation
- define CSR representation components
- illustrate CSR representation example
- describe vertex table functionality
- describe edge table functionality
- discuss node properties storage
- discuss edge properties storage
- introduce delta map for mutability
- describe log-based CSR representation
- illustrate log-based CSR representation example
- discuss log-based CSR representation limitations
- introduce mutable multilevel data structures
- describe design considerations for mutable multilevel data structures
- illustrate example implementation of mutable multilevel data structure
- introduce compressed sparse row representation
- describe mutable multilevel data structure
- illustrate method for accessing mutable multilevel data structure
- describe read-only levels of mutable multilevel data structure
- describe writable level of mutable multilevel data structure
- describe edge table array in read-only levels
- describe vertex table in read-only levels
- describe performance-optimized variant of mutable multilevel data structure
- describe delta map in performance-optimized variant
- illustrate two-level representation of graph
- describe differences between level 0 and level 1 CSR representations
- describe software copy-on-write approach for vertex tables
- compare performance of mutable multilevel data structures to existing data structures
- describe space-optimized variant of mutable multilevel data structure
- describe log-based data structures in performance-optimized variant
- describe concurrent computations on different levels of mutable multilevel data structure
- describe graph processing module and its operations
- illustrate method for reconstructing adjacency list for given vertex
- describe reconstructing adjacency list from performance-optimized mutable multilevel data structure

### Creating a New Read-Only Level

- motivate creating new read-only level
- describe triggering conditions for creating new read-only level
- explain creating new read-only level periodically
- explain creating new read-only level based on delta map size
- describe creating new read-only level through explicit function call
- illustrate method for creating new read-only level
- describe handling concurrent updates during creation
- discuss supporting bidirectional edge traversal
- explain storing vertex and edge properties

### Merging Read-Only Levels

- describe merging read-only levels to consolidate space
- illustrate step-by-step process for merging read-only levels
- discuss merging all read-only levels to build new level 0 data structure

### Space-Optimized Design

- introduce space-optimized variant
- trade performance for low memory overhead
- describe edge set representation
- add new outgoing edges to edge set
- store only newly added edges
- reconstruct adjacency list
- examine multiple levels of data structure
- describe vertex table
- add pre-computed node degree
- describe deletion vector
- store indication of edge deletion
- use logical timestamps
- describe deletion vector elements
- illustrate two-level representation
- describe level 0 CSR representation
- describe level 1 CSR representation
- reconstruct adjacency list example
- describe pseudo-code for reconstruction
- illustrate flow diagram for reconstruction
- describe method for reconstructing adjacency list
- describe next pointer entry

### Parameterized Design

- introduce hybrid representation
- describe performance-optimized variant
- describe space-optimized variant
- introduce copy-large policy
- introduce copy-small policy
- describe hybrid variant with two values
- describe method for creating new read-only level
- evaluate conditions for copying adjacency list
- describe copying entire adjacency list
- describe copying modified edges
- illustrate method for creating new read-only level

### Copy-on-Write Arrays

- introduce copy-on-write arrays
- describe splitting arrays into equal-sized data pages
- describe indirection array
- illustrate copy-on-write array
- describe accessing elements in copy-on-write array
- describe traversing copy-on-write vertex table
- evaluate performance of copy-on-write vertex table

### Persistent Representations of the Mutable Multilevel Data Structures

- introduce persistent representations
- describe using memory mapping and demand paging
- describe on-disk representation of copy-on-write array
- describe loading data into memory
- describe maintaining invariants
- describe building persistent representation of mutable multilevel data structure

### The Writable Level

- implement writable level data structure
- collect modifications in batches
- create new read-only level
- describe vertex table implementation
- coordinate concurrent updates
- manage concurrent writes to data pages
- illustrate method for managing changes
- update adjacency lists and counters

### Sliding Window

- introduce sliding window concept
- describe benefits of sliding window
- explain how to advance sliding window
- describe deletion vector for edge deletion
- provide example of one hour long sliding window
- explain level identifier management
- describe level identifier wrapping
- introduce evaluation section
- describe graph analytics algorithms used
- describe graph structure used for evaluation
- categorize algorithms into structure-light and structure-heavy
- evaluate performance-optimized variant
- evaluate space-optimized variant
- evaluate hybrid variants
- compare performance to original CSR representation
- describe memory usage of variants
- discuss merging levels
- evaluate impact of deletions on performance
- describe policy for copying adjacency lists
- evaluate performance of hybrid variants
- discuss trade-offs between memory and performance
- describe use cases for mutable multilevel data structures
- discuss persistence and performance for large graphs
- describe flexibility of mutable multilevel data structures
- introduce computing system for implementing mutable multilevel data structures
- describe program instructions for creating and using mutable multilevel data structures

