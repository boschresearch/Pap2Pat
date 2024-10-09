# DESCRIPTION

## FIELD

- relate semiconductor design

## BACKGROUND OF THE DISCLOSURE

- introduce clock gating

## DETAILED DESCRIPTION

- introduce GPU architecture and clock gating technique

### System Overview

- introduce processing system
- describe system components
- detail processor architecture
- explain memory hierarchy
- describe peripherals and interfaces
- illustrate system variations
- describe system overview
- introduce graphics processor core block
- detail function block components
- describe graphics microcontroller functionality
- outline graphics core components
- illustrate GPU architecture
- introduce system overview
- describe I/O circuitry and memory management
- detail tensor cores and matrix operations
- describe ray tracing cores and operations
- outline ray tracing instruction set
- describe GPGPU architecture
- detail compute units and memory hierarchy
- describe command processing and thread dispatch
- introduce additional graphics processor architectures
- describe graphics processor with tiled architecture
- detail compute accelerator architecture
- outline integrated network interface

### Graphics Processing Engine

- describe graphics processing engine architecture
- illustrate 3D pipeline and media pipeline
- detail command streamer and unified return buffer
- explain graphics core cluster and execution resources
- describe shared function logic and cache
- illustrate graphics core block and vector engine
- detail memory load/store unit and instruction cache
- describe graphics processing engine
- detail vector engine architecture
- explain matrix engine architecture
- illustrate tile architecture of multi-tile processor
- describe memory hierarchy and interconnects
- illustrate graphics processor instruction formats
- detail instruction components and formats
- explain instruction execution and control
- introduce graphics processing engine
- describe instruction format and access modes
- explain opcode grouping and decode
- outline graphics pipeline components
- describe geometry pipeline and tessellation
- explain render output pipeline and pixel operations
- introduce media pipeline and command streamer
- describe graphics processor command format
- outline graphics processor command sequence
- explain 3D pipeline and media pipeline states
- describe graphics software architecture

### IP Core Implementations

- define IP core development system
- generate software simulation of IP core design
- create RTL design from simulation model
- synthesize RTL design into hardware model
- store IP core design for delivery to fabrication facility
- fabricate integrated circuit based on IP core design

### Exemplary System on a Chip Integrated Circuit

- illustrate system on a chip integrated circuit with application processor, graphics processor, and peripheral logic
- describe graphics processor with vertex processor and fragment processor
- illustrate additional graphics processor with unified shader core architecture
- describe programmable network interface for accelerating network-based compute tasks

### Constructing Hierarchical Clock Gating Architectures via Rewriting

- introduce clock gating analysis
- motivate rewriting technique
- describe e-graph rewriting framework
- illustrate e-graph rewriting example
- outline flow chart of RTL optimization
- summarize rewrites for clock gating opportunities
- introduce clock gating via rewriting
- motivate ASSUME operators
- describe e-graph generation
- illustrate method of constructing hierarchical clock gating architectures
- detail ASSUME operator propagation
- describe clock gating opportunity detection
- outline RTL code generation
- provide embodiment variations

