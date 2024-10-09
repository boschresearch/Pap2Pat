# DESCRIPTION

## BACKGROUND

- motivate graph analytics

## SUMMARY

- introduce mutable multilevel data structure
- describe variants of data structure
- application of data structure

## DETAILED DESCRIPTION OF EMBODIMENTS

- introduce mutable multilevel data structures

### Compressed Sparse Row Representation

- introduce CSR representation
- describe CSR components (vertex table and edge table)
- illustrate CSR representation with example graph
- discuss limitations of CSR representation (immutability)
- propose mutable CSR variants (delta map and log-based CSR)
- describe log-based CSR representation with example modifications
- introduce mutable multilevel data structures for graph representation
- introduce compressed sparse row representation
- describe method for accessing mutable multilevel data structure
- motivate performance-optimized variant
- describe edge table representation
- illustrate two-level representation of graph
- compare performance to existing data structures
- describe space-optimized variant
- motivate concurrent computations on different levels
- describe method for reconstructing adjacency list

### Creating a New Read-Only Level

- motivate creating new read-only level
- describe triggering conditions for creating new read-only level
- outline method for creating new read-only level
- discuss concurrent updates during creation of new read-only level

### Merging Read-Only Levels

- describe method for merging read-only levels

### Space-Optimized Design

- introduce space-optimized variant
- motivate low memory overhead
- describe edge set representation
- illustrate deletion vector usage
- depict two-level representation of graph
- reconstruct adjacency list example
- describe query-level reconstruction
- illustrate flow diagram for reconstruction
- describe next pointer usage
- illustrate flow diagram with next pointers

### Parameterized Design

- introduce hybrid representation
- describe performance-optimized variant
- describe space-optimized variant
- describe hybrid variant with copy-large policy
- describe hybrid variant with copy-small policy

### Copy-on-Write Arrays

- introduce copy-on-write arrays
- describe indirection table and data pages
- illustrate copy-on-write array with example

### Persistent Representations of the Mutable Multilevel Data Structures

- introduce persistent representations
- describe on-disk representation of copy-on-write arrays
- describe invariants and usage in graph analytics

### The Writable Level

- implement writable level data structure
- coordinate concurrent updates using latching scheme
- manage vertex objects and growable arrays
- illustrate method for managing changes to writable level

### Sliding Window

- introduce sliding window concept
- describe benefits of sliding window
- explain how to advance sliding window
- discuss deleting old read-only levels
- provide example of sliding window usage
- explain level identifier management
- describe evaluation of different variants
- categorize algorithms by computation vs traversal
- compare performance of different variants
- discuss memory usage of different variants
- evaluate hybrid variants
- discuss insights on persistence and performance
- describe flexibility of mutable multilevel data structures

