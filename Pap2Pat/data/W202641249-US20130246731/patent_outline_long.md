# DESCRIPTION

## BACKGROUND

- contrast graph and relational storage systems

## DESCRIPTION OF EMBODIMENTS

- introduce graph storage system

### Notation and Nomenclature

- define procedures and logic blocks
- describe symbolic representations of operations
- explain terms and labels

### Overview of Discussion

- outline example techniques and systems

### Example Graph Storage System

- describe graph storage system 100
- introduce servers and global address space
- explain graph allocators and buddy memory allocator
- describe memory block allocation
- introduce fault toleration structure
- describe distributed storage and memory allocation
- explain support for low latency queries
- describe transactional semantics
- introduce distributed storage for updates
- describe server-side event driven processing
- explain scalability and high throughput storage
- describe support for interactive graph queries
- outline example applications

### Example Graph Structure

- describe vertex objects and edge objects
- explain property objects
- introduce internal structure of vertex object
- describe identification and pointers
- explain embedded property
- describe edge object structure
- introduce property object structure
- explain fixed and variable size records

### Example Distributed Storage and Memory Allocation

- describe pre-allocation of memory blocks
- explain buddy memory allocator
- introduce graph allocators and minitransactions
- describe allocation from global address space
- explain meta-data storage
- describe failure handling
- introduce RPC framework
- explain message batching

### Example Online Data Migration

- introduce migrator and online data migration
- describe migrate functions

### Example Fault Toleration Structure

- introduce fault toleration structure
- describe minitransactions and memnodes

### Example Computer System

- introduce computer system 400
- describe address/data bus and processor
- explain multi-processor environment
- introduce volatile memory and non-volatile memory
- describe data storage unit
- introduce alphanumeric input device
- describe cursor control device
- explain display device
- introduce I/O device
- describe operating system and applications

### Example Method of Use

- introduce example method of use
- describe flow diagram 500
- motivate graph storage system
- define graph 200
- store graph 200 on servers/memnodes 110
- provide global address space 130
- allocate global address space 130
- perform parallel server side graph processing
- migrate data across servers/memnodes 110
- introduce second example method of use
- describe flow diagram 600
- motivate graph storage system
- define graph 200
- store graph 200 on servers/memnodes 110
- provide global address space 130
- allocate global address space 130
- perform distributed graph traversals
- employ fault toleration structure 160
- migrate data across servers/memnodes 110
- summarize embodiments
- conclude with claims

