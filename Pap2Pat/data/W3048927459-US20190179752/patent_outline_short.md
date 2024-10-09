# DESCRIPTION

## BACKGROUND

### 1. Field of the Invention

- introduce in-memory caching technology

### 2. Description of the Related Art

- describe graph data and caching techniques

## SUMMARY

- summarize multi-level caching method

### Effect

- describe advantages of multi-level caching

## DETAILED DESCRIPTION

- introduce multi-level caching system
- describe caching of frequently used subgraph and neighboring data
- explain assignment of weight to data based on pattern of frequently used subgraph
- describe loading of data in first cache memory
- explain identification of neighboring vertex with high number of accesses
- describe loading of neighboring vertex in second cache memory
- explain management of data cached in first cache memory
- describe replacement of data in first cache memory when full
- explain management of second cache memory using FIFO scheme
- describe extraction of frequently used query pattern from subgraph used in previous query
- explain assignment of pattern weight to query pattern
- describe management of caching of data based on TTL value and pattern weight
- describe multi-level caching system
- explain TTL distributor and cache manager
- detail 2-level cache memory structure
- illustrate query history table and FP-tree
- describe query pattern extraction and TTL value assignment
- detail caching of neighboring vertices
- illustrate caching process in multi-level caching system
- describe managing first cache memory
- describe managing second cache memory
- outline multi-level caching method
- discuss non-transitory computer-readable media

