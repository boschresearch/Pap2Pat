# DESCRIPTION

## BACKGROUND

- motivate IR drop prediction

## BRIEF SUMMARY

- summarize IR drop solution

## DETAILED DESCRIPTION

- introduce IR drop prediction techniques
- describe convolutional neural networks (CNNs)
- motivate use of CNNs for IR drop prediction
- define cell power consumption
- describe cell power characteristics
- explain toggle-rate-scaled cell power
- define cell in a circuit structure
- describe grid-level granularity for IR drop prediction
- explain power map formation
- describe power map input to CNN
- illustrate power map formation with FIG. 1
- describe timing diagram for cells
- explain power contribution of cells to grid tiles
- describe power map generation for each sub-interval
- illustrate power map generation with FIG. 2
- describe CNN architecture for IR drop prediction
- illustrate CNN architecture with FIG. 3
- describe MAX operator for selecting maximum IR drop prediction
- explain backpropagation for training CNN
- describe power map generator for circuit structure
- describe neural network for transforming power maps
- explain appending undecomposed power information to power maps
- illustrate modified machine learning and inference system with FIG. 4
- describe deep neural network architecture
- illustrate deep neural network architecture with FIG. 5
- describe process for repairing excessive IR drop in a circuit
- illustrate process for repairing excessive IR drop with FIG. 6
- describe training neural network on learning set of circuit partitions
- explain generating power maps for training set
- describe applying power maps to neural network for training
- explain IR drop threshold test
- describe remediation of IR drop hotspots
- explain adjusting cell layout or power grid distribution
- describe continuing to routing phase after IR drop remediation
- explain enhancing power maps with sub-interval-independent values
- describe applying machine inference at various points in circuit design
- explain implementation of techniques using general purpose processors and/or GPUs
- describe system for implementing machine learning and inference system
- explain data processing cluster (DPC)
- describe general processing cluster (GPC)
- explain input/output (I/O) components
- describe level one cache (L1 cache) and level two cache (L2 cache)
- explain load/store unit (LSU) and memory management unit (MMU)
- describe parallel processing unit (PPU) and other system components

### Parallel Processing Unit

- introduce parallel processing unit
- describe multi-threaded processor
- explain latency hiding architecture
- define thread of execution
- describe graphics processing unit (GPU)
- explain graphics rendering pipeline
- list applications of parallel processing unit
- describe I/O unit
- explain interconnect
- describe local memory
- explain high-bandwidth memory (HBM) subsystem
- describe NVLink interconnect
- explain data transmission
- describe I/O unit functionality
- explain command decoding
- describe front-end unit
- explain command stream management
- describe scheduler unit
- explain task management
- describe work distribution unit
- explain task dispatching
- describe crossbar interconnect
- explain general processing cluster
- describe task processing
- explain result management
- describe memory partition unit
- explain memory interface
- describe FIG. 8
- introduce general processing cluster
- describe pipeline manager
- explain data processing cluster
- describe raster engine
- explain pre-raster operations unit
- describe streaming multiprocessor
- explain memory management unit
- describe FIG. 9
- explain memory partition unit components
- introduce parallel processing unit
- describe memory hierarchy
- describe unified memory
- describe address translation services
- describe copy engines
- describe page faulting
- describe level two cache
- describe lower level caches
- describe raster operations unit
- describe depth testing
- describe raster engine
- describe memory partition unit
- describe streaming multiprocessor
- describe instruction cache
- describe scheduler unit
- describe register file
- describe processing core
- describe special function unit
- describe load/store unit
- describe interconnect network
- describe shared memory/L1 cache
- describe cooperative groups
- describe dispatch unit
- describe tensor cores
- describe matrix operations
- describe API for tensor cores
- describe texture unit
- describe load and store operations
- describe interconnect network
- describe shared memory/L1 cache
- describe general purpose parallel computation
- describe applications of parallel processing unit

### Exemplary Computing System

- describe high-performance GPU-accelerated systems
- motivate parallel processing unit 700
- introduce processing system 1100
- describe central processing unit 1106
- describe switch 1102
- describe parallel processing unit 700 modules
- describe memory 704 modules
- describe NVLink 708 connections
- describe interconnect 702
- describe parallel processing module 1104
- describe various embodiments of NVLink 708
- describe signaling rate of NVLink 708
- describe data transfer rate of NVLink 708
- introduce processing system 1200
- describe communication bus 1210
- describe main memory 1204
- describe various applications of exemplary processing system 1200

### Graphics Processing Pipeline

- introduce graphics processing pipeline
- describe parallel processing unit
- explain processing of graphics primitives
- detail vertex shader program
- describe pixel shader program
- explain concurrent execution of shader programs
- introduce graphics processing pipeline stages
- describe data assembly stage
- detail vertex shading stage
- explain primitive assembly stage
- describe geometry shading stage
- detail viewport SCC stage
- explain rasterization stage
- describe fragment shading stage
- detail raster operations stage
- explain data assembly stage operations
- describe vertex shading stage operations
- detail primitive assembly stage operations
- explain geometry shading stage operations
- describe viewport SCC stage operations
- detail rasterization stage operations
- explain fragment shading stage operations
- describe raster operations stage operations
- introduce graphics processing pipeline implementation
- describe device driver role
- explain API call processing
- detail kernel launching on parallel processing unit
- describe fixed function hardware units
- explain logic functional operations
- define logic
- describe configured to perform tasks
- explain based on phrase
- describe in response to phrase
- explain first, second, etc. labels
- describe or phrase in claims
- introduce graphics processing pipeline variations
- describe additional stages
- explain excluded stages
- detail dedicated hardware units
- describe programmable hardware units

