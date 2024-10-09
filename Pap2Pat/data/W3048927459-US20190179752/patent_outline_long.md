# DESCRIPTION

## BACKGROUND

### 1. Field of the Invention

- introduce in-memory caching technology

### 2. Description of the Related Art

- describe graph data representation
- motivate in-memory caching
- limitations of existing in-memory caching schemes

## SUMMARY

- predict and cache frequently accessed data
- efficiently predict and cache data
- enhance graph processing performance
- increase data lifespan
- provide multi-level caching method and system

### Effect

- predict and cache frequently accessed data
- efficiently search multi-level cache memories
- increase data lifespan and prevent frequent replacement

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
- explain replacing data in first cache memory
- describe managing first cache memory
- explain managing second cache memory
- introduce pattern extractor component
- describe extracting query patterns
- explain generating FP-tree
- describe assigning pattern weights
- explain setting TTL values
- describe managing caching based on TTL values
- introduce query history table
- describe recording queries in query history table
- explain managing query history table
- describe generating FP-tree from query history table
- explain extracting query patterns from FP-tree
- describe assigning pattern weights to query patterns
- explain setting TTL values based on pattern weights
- describe managing caching based on TTL values
- introduce disk memory
- describe searching for graph data in disk memory
- explain adding data to first cache memory
- describe managing first cache memory
- explain managing second cache memory
- describe selecting data with high access history
- explain caching neighboring data
- describe managing second cache memory
- explain deleting data from second cache memory
- describe adding new data to second cache memory
- introduce multi-level caching system architecture
- describe cache manager component
- explain graph usage pattern manager component
- describe TTL distributor component
- explain recording queries in query history table
- describe implementing FP-tree
- explain detecting frequently used query patterns
- describe predicting data with high availability
- explain caching predicted data
- describe managing 2-level cache memory
- explain enhancing graph processing performance
- describe multi-level caching system
- introduce TTL distributor
- explain cache manager function
- describe 2-level cache memory
- detail used data cache
- detail prefetched cache
- describe graph query request process
- illustrate subgraph for query history
- describe query history table
- explain FP-tree generation
- describe query pattern extraction
- illustrate query pattern extraction process
- describe TTL value setting
- illustrate TTL value setting process
- describe caching neighboring vertex
- illustrate caching neighboring vertex process
- describe managing first cache memory
- illustrate managing first cache memory process
- describe managing second cache memory
- illustrate managing second cache memory process
- describe multi-level caching method
- determine graph query request
- search graph data in first cache memory
- output graph data
- search graph data in second cache memory
- output graph data
- search graph data in disk memory
- output graph data
- load graph data and neighboring data
- store vertices in first cache memory
- store neighboring vertex in second cache memory
- enhance graph query processing performance
- record multi-level caching method in computer-readable media
- include program instructions
- include data files and data structures
- provide non-transitory computer-readable media
- describe magnetic media
- describe optical media
- describe magneto-optical media
- describe hardware devices
- describe read-only memory
- describe random access memory
- describe flash memory
- claim scope of disclosure

