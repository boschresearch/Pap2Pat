# DESCRIPTION

## BACKGROUND

- motivate IR drop prediction

## BRIEF SUMMARY

- summarize IR drop solution

## DETAILED DESCRIPTION

- introduce IR drop prediction techniques
- motivate use of convolutional neural networks (CNNs)
- describe image classification using CNNs
- apply CNNs to IR drop prediction
- define cell power consumption metrics
- scale power consumption by toggle rate
- reduce computation complexity with grid-level granularity
- map cell power to grid tiles
- form power maps for sub-intervals of clock period
- assign unique time points to power maps
- analyze cell power in each sub-interval
- amortize cell power into grid tiles
- describe CNN architecture for IR drop prediction
- include additional power information in power maps
- depict partitioned circuit structure and grid tiles
- describe timing diagram for cells
- generate power maps for each sub-interval
- transform power maps into IR drop predictions
- select maximum IR drop prediction
- train neural network with power maps and IR drop information
- apply neural network to predict IR drop hotspots
- remediate IR drop hotspots in circuit design

### Parallel Processing Unit

- introduce parallel processing unit
- describe architecture
- specify multi-threaded processor
- describe latency hiding architecture
- define thread
- specify graphics processing unit (GPU) embodiment
- describe general-purpose computation embodiment
- list applications
- describe I/O unit
- specify interconnect
- describe front-end unit
- specify scheduler unit
- describe work distribution unit
- specify crossbar
- describe general processing cluster
- specify memory partition unit
- describe memory interface
- specify HBM2 memory interface
- introduce parallel processing unit
- describe memory hierarchy
- explain memory partition unit
- describe copy engines
- explain level two cache
- describe raster operations unit
- introduce streaming multiprocessor
- describe instruction cache
- explain scheduler unit
- describe register file
- explain processing core modules
- describe special function unit modules
- explain load/store unit modules
- describe interconnect network
- explain shared memory/L1 cache
- describe general purpose parallel computation configuration

### Exemplary Computing System

- describe high-performance GPU-accelerated systems
- illustrate processing system 1100 with parallel processing unit 700
- detail NVLink 708 high-speed communication links
- describe switch 1102 interfaces and interconnect 702 connections
- illustrate parallel processing module 1104 on a single semiconductor platform
- describe NVLink 708 features and capabilities
- illustrate exemplary processing system 1200 with central processing unit 1106
- describe system components and variations

### Graphics Processing Pipeline

- introduce graphics processing pipeline
- describe parallel processing unit
- explain processing of graphics primitives
- detail vertex shader program
- describe pixel shader program
- illustrate pipeline architecture
- define data assembly stage
- explain vertex shading stage
- describe primitive assembly stage
- detail geometry shading stage
- explain viewport SCC stage
- describe rasterization stage
- detail fragment shading stage
- explain raster operations stage
- describe output data
- discuss sequential processing operations
- explain caching of primitive data
- describe viewport scaling, culling, and clipping
- detail rasterization of 3D geometric primitives
- summarize graphics processing pipeline stages

