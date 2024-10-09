# DESCRIPTION

## FIELD

- relate semiconductor design

## BACKGROUND OF THE DISCLOSURE

- introduce clock gating

## DETAILED DESCRIPTION

- introduce GPU architecture
- describe clock gating technique

### System Overview

- introduce processing system 100
- describe system components
- motivate various embodiments
- describe processor 102
- detail processor core 107
- explain instruction set 109
- describe cache memory 104
- introduce interface bus 110
- describe memory controller 116
- detail platform controller hub 130
- describe peripherals
- motivate display device 111
- introduce external components
- introduce system overview
- describe processor components
- detail graphics processor core block
- explain function block components
- describe graphics SoC interface
- detail graphics microcontroller
- explain graphics core components
- describe vector engines
- detail matrix acceleration units
- explain sampler and ray tracing units
- introduce GPU architecture
- describe multi-core group components
- detail memory hierarchy
- introduce system overview
- describe I/O circuitry
- detail IOMMU functionality
- explain virtualization support
- describe integrated CPU, GPU, and I/O devices
- introduce tensor cores
- detail matrix operation capabilities
- describe neural network implementation
- introduce ray tracing cores
- detail ray tracing instruction set
- describe ray tracing functionality
- explain hybrid rasterization/ray tracing approach
- introduce GPGPU architecture
- describe compute units and memory hierarchy
- detail command processing and thread dispatch
- introduce additional graphics processor architectures
- describe graphics processor with display controller
- detail video codec engine and media pipeline
- introduce 3D pipeline and media pipeline
- describe thread spawning and execution
- introduce tiled architecture
- describe graphics engine tiles and memory interconnects
- detail fabric interconnect and NUMA system
- introduce compute accelerator architecture
- describe compute engine tiles and network interface

### Graphics Processing Engine

- illustrate GPE 410 block diagram
- describe command streamer 403 functionality
- detail unified return buffer 418 usage
- explain 3D pipeline 312 and media pipeline 316 processing
- describe graphics core cluster 414 architecture
- detail execution resources within graphics core blocks
- explain shared function logic 420 and its resources
- describe scalable graphics core cluster 414
- illustrate graphics core cluster 414 with shared function logic 420
- describe execution logic including array of processing elements
- detail graphics core block 415 architecture
- explain vector engine 502A and matrix engine 503A functionality
- describe memory load/store unit 504A and its operations
- detail instruction cache 505A and data cache/shared local memory 506A
- explain ray tracing unit 508A, sampler 510A, and fixed function logic 512A
- describe graphics processing engine
- detail vector engine architecture
- explain thread execution and register access
- describe message passing and branch instructions
- detail SIMD floating point units
- explain integer computation and extended math capability
- describe machine learning computations
- detail matrix engine architecture
- explain tensor operations and systolic array
- describe input and output data storage
- explain sparsity support and metadata
- detail compressed tensor representations
- describe tile architecture and graphics core clusters
- explain memory hierarchy and cache structure
- detail graphics processor instruction formats
- explain instruction components and execution options
- introduce graphics processing engine
- describe 128-bit instruction format
- explain access/address mode field
- detail opcode grouping
- describe graphics pipeline components
- introduce geometry pipeline
- describe vertex fetcher and vertex shader
- explain thread execution logic
- detail render output pipeline
- describe rasterizer and depth test component
- introduce media pipeline
- describe media engine and video front-end
- explain display engine
- describe graphics pipeline programming
- introduce graphics processor command format
- detail graphics processor command sequence
- explain pipeline flush command
- describe pipeline select command
- detail pipeline control command
- explain return buffer state
- describe 3D pipeline state
- introduce media pipeline state
- describe graphics software architecture

### IP Core Implementations

- implement IP cores on machine-readable medium
- generate software simulation of IP core design
- create RTL design from simulation model
- synthesize RTL design into hardware model
- simulate and test hardware model
- store IP core design for delivery to fabrication facility
- transmit IP core design to fabrication facility
- fabricate integrated circuit based on IP core design
- configure integrated circuit to perform operations
- illustrate IP core implementation in package assembly
- describe interconnection of chiplets in package assembly
- detail active interposer technology in package assembly
- illustrate interchangeable chiplets in package assembly

### Exemplary System on a Chip Integrated Circuit

- describe system on a chip integrated circuit
- illustrate application processor and graphics processor
- detail peripheral or bus logic
- describe display device and interface controllers
- illustrate storage and memory interface
- describe embedded security engine
- illustrate graphics processor with vertex and fragment processors
- detail memory management units and cache
- describe circuit interconnects and shader cores

### Constructing Hierarchical Clock Gating Architectures via Rewriting

- introduce clock gating architectures
- motivate rewriting for clock gating analysis
- describe RTL synthesis tools
- illustrate detection of clock gating opportunities
- describe clock gate circuitry
- motivate mux tree analysis
- introduce e-graph rewriting framework
- describe e-graph data structure
- illustrate e-graph rewriting example
- describe equivalence preserving rewrites
- illustrate flow chart of e-graph rewrites for RTL optimization
- describe using e-graph rewrites for clock gating opportunities
- introduce ASSUME operators
- combine ASSUME operators via rewriting
- apply ASSUME operators to registers
- generate clock gating signals
- evaluate delay and area consequences
- determine profitability of clock gating
- generate complex Boolean enable signals
- apply technique to discover clock gating opportunities
- generate hardware representation of clock gating circuitry
- illustrate method of constructing hierarchical clock gating architectures
- load and analyze RTL code
- generate dataflow graph and initial e-graph
- rewrite expressions in e-graph using equivalence preserving transformations
- assume design with multiplexor-based equivalent expressions
- detect clock gating opportunities within assumed design
- generate RTL code for clock gating circuitry
- provide non-transitory machine-readable medium with instructions

