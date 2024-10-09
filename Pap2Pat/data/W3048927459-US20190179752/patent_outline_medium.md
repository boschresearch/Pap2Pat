# DESCRIPTION

## BACKGROUND

### 1. Field of the Invention

- introduce in-memory caching technology

### 2. Description of the Related Art

- describe graph data and caching techniques

## SUMMARY

- predict and cache frequently accessed graph data
- efficiently search multi-level cache memories

### Effect

- summarize advantages of multi-level caching method

## DETAILED DESCRIPTION

- introduce multi-level caching system
- describe caching of frequently used subgraph and neighboring data
- explain multi-level cache memory hierarchy
- introduce searcher component
- describe searching for graph data in first cache memory
- explain re-searching in second cache memory
- introduce outputter component
- describe outputting graph data
- explain updating TTL values
- introduce memory manager component
- describe moving data between cache memories
- explain managing first cache memory based on TTL values
- describe replacing data in first cache memory
- explain managing second cache memory based on FIFO scheme
- describe deleting data from second cache memory
- introduce pattern extractor component
- describe extracting frequently used query pattern
- explain generating FP-tree
- describe assigning pattern weight
- explain setting TTL value based on pattern weight
- describe adjusting TTL value
- explain updating TTL value based on new query pattern
- describe predicting and caching data
- explain enhancing graph processing performance
- describe multi-level caching system
- introduce TTL distributor and cache manager
- explain used data cache and prefetched cache
- describe cache searching process
- illustrate subgraph for query history
- explain query history table and FP-tree
- describe query pattern extraction
- illustrate TTL value setting
- describe caching neighboring vertices
- illustrate caching process
- describe managing first cache memory
- illustrate managing first cache memory
- describe managing second cache memory
- illustrate managing second cache memory
- introduce multi-level caching method
- describe determining graph query request
- describe searching graph data from first cache memory
- describe searching graph data from second cache memory
- describe searching graph data from disk memory
- describe outputting graph data
- describe loading graph data and neighboring data
- conclude multi-level caching method

