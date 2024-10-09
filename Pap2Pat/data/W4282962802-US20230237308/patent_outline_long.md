# DESCRIPTION

## BACKGROUND

- motivate quantization

## SUMMARY

- introduce quantization systems
- describe optimal clipping
- outline method for quantizing tensors

## DETAILED DESCRIPTION

- introduce optimally clipped tensors and vectors
- define quantization-aware training (QAT)
- describe dynamic quantization
- describe static quantization
- motivate use cases for QAT
- describe limitations of conventional techniques
- introduce max-scaling
- describe advantages of max-scaling
- describe limitations of max-scaling
- introduce data clipping
- describe calibration strategy
- define B-bit quantization
- derive quantization noise metric
- describe Lloyd-Max algorithm
- describe max-scaled quantization operation
- derive MSE for max-scaled quantizer
- introduce data clipping for improved accuracy
- describe clipping scalar optimization
- derive analytical expression for MSE
- describe empirical evaluation of MSE
- illustrate quantization MSE as a function of clipping scalar
- describe observations from graphs
- introduce neural network architecture
- describe layer processing unit
- describe quantizing logic
- describe clipping scalar optimization unit
- describe quantization unit
- describe optimal clipping scalar computation
- describe Newton-Raphson algorithm
- describe convergence of clipping scalars
- describe initialization of clipping scalars
- describe MSE minimization
- derive recursive expression for optimal clipping scalar
- describe application to tensor and vector quantization
- describe OCTAV algorithm
- describe convergence of OCTAV algorithm
- describe computational efficiency of OCTAV
- illustrate flowchart of method for quantizing tensors
- compute first clipping scalars
- process input by neural network model
- adjust first tensors according to mean squared error
- update first clipping scalars
- repeat for additional inputs
- adjust intermediate tensors according to mean squared error
- update second clipping scalars
- illustrate clipping scalars determined by brute force search
- illustrate clipping quantization MSE determined by brute force search
- summarize benefits of OCTAV algorithm

### QAT Gradient Estimation

- introduce QAT with minimal noise
- motivate gradient estimation
- define gradient for a layer
- illustrate gradient estimation functions
- describe limitations of STE
- describe limitations of PWL
- introduce MAD
- analyze gradient back-propagation using STE
- derive equation (7)
- highlight exponential explosion of STE gradients
- describe PWL estimator
- derive equation (8)
- introduce magnitude-aware derivative (MAD)
- formulate MAD
- compare MAD with PWL
- describe application of MAD to activations
- illustrate block diagram of neural network system
- summarize benefits of OCTAV-enabled QAT

### Parallel Processing Architecture

- introduce parallel processing unit (PPU) 400
- describe PPU 400 as neural network implementation
- explain software and hardware implementation of neural network model
- describe multi-threaded processor architecture
- introduce graphics processing unit (GPU) for graphics rendering
- describe general-purpose computation capabilities
- list various applications of PPU 400
- describe I/O unit 405
- explain command decoding and routing
- describe front end unit 415
- explain command stream management
- describe scheduler unit 420
- explain task management and tracking
- describe work distribution unit 425
- explain task dispatching
- describe XBar 470
- explain interconnect network
- describe general processing clusters (GPCs) 450
- explain task processing and result generation
- describe memory partition units 480
- explain memory interface and access
- describe memory management unit
- explain translation lookaside buffers (TLBs)
- describe Raster Operations (ROP) unit
- explain level two (L2) cache
- describe memory interface and data buses
- explain high bandwidth memory (HBM) interface
- describe Single-Error Correcting Double-Error Detecting (SECDED) Error Correction Code (ECC)
- explain multi-level memory hierarchy
- describe unified memory and address translation
- explain page fault handling and memory mapping
- describe copy engines and data transfer
- explain hardware page faulting
- describe L2 cache and memory partition unit interaction
- explain level one (L1) cache and processing unit interaction
- describe SIMD and SIMT architectures
- explain program counter, call stack, and execution state management
- describe Cooperative Groups programming model
- explain collective operations and synchronization
- describe tensor cores and matrix operations
- explain floating point and integer arithmetic logic units
- describe special function units (SFUs) and tree traversal unit
- explain texture unit and texture map filtering operations
- describe load store units (LSUs) and register file interaction
- explain interconnect network and crossbar
- describe shared memory and data storage
- explain cache and shared memory functionality
- describe general purpose parallel computation configuration
- explain PPU 400 applications and embodiments

### Exemplary Computing System

- introduce high-performance GPU-accelerated systems
- describe multiple GPUs and CPUs in various industries
- motivate parallelism in applications
- illustrate processing system 500 with PPU 400
- describe CPU 530, switch 510, and multiple PPUs 400
- detail NVLink 410 high-speed communication links
- explain interconnect 402 connections
- describe switch 510 interfaces
- illustrate parallel processing module 525
- describe NVLink 410 and interconnect 402 variations
- detail NVLink 410 and CPU 530 interfaces
- explain NVLink 410 and switch 510 interfaces
- describe NVLink 410 and interconnect 402 direct connections
- illustrate NVLink 410 and CPU 530 direct connections
- describe NVLink 410 and switch 510 direct connections
- explain NVLink 410 and interconnect 402 indirect connections
- detail NVLink 410 and CPU 530 indirect connections
- describe NVLink 410 and switch 510 indirect connections
- illustrate NVLink 410 and interconnect 402 combinations
- describe NVLink 410 and CPU 530 combinations
- explain NVLink 410 and switch 510 combinations
- detail NVLink 410 signaling rate and data transfer rate
- describe NVLink 410 and CPU 530 direct load/store/atomic access
- explain NVLink 410 coherency operations
- describe NVLink 410 Address Translation Services (ATS)
- illustrate NVLink 410 low-power mode
- describe system 565 with CPU 530 and communication bus 575
- detail main memory 540 and computer-readable media
- explain computer storage media and modulated data signal
- describe CPU 530 and parallel processing module 525 execution
- illustrate input device(s) 560 and display device(s) 545
- describe network interface 535 and communication purposes
- explain distributed network and cloud computing environment
- detail secondary storage and power supply
- describe system 565 components and functionality
- illustrate example network environments
- describe client devices, servers, and network attached storage (NAS)
- explain network communication and wireless connectivity
- detail peer-to-peer network environments and client-server network environments
- describe cloud-based network environments and distributed computing
- illustrate client devices and cloud computing functionality

### Machine Learning

- introduce deep neural networks
- describe human brain learning process
- explain artificial neuron model
- define deep neural network model
- illustrate neural network layers
- describe training process
- explain inference process
- highlight importance of matrix math operations
- describe PPU 400 capabilities
- illustrate system 555 components
- describe client device 502 functionality
- explain provider environment 506 functionality
- describe training and inference manager 532 functionality
- illustrate interface layer 508 functionality
- describe training module 512 functionality
- explain model repository 516 functionality
- describe inference module 518 functionality
- illustrate user context data repository 522 functionality
- describe local database 534 functionality
- explain machine learning application 526 functionality
- describe processor 528 functionality
- highlight GPU usage for deep learning
- describe video data enhancement
- explain supervised and unsupervised training
- describe training data 514 functionality
- illustrate training module 512 functionality
- describe model selection process
- explain machine learning algorithm functionality
- describe target attribute prediction
- highlight model output
- describe training and inference manager 532 functionality
- explain model type selection process

### Graphics Processing Pipeline

- introduce PPU 400 functionality
- describe graphics data processing
- explain shader program execution
- illustrate vertex shader program functionality
- describe pixel shader program functionality
- explain frame buffer generation
- describe display device functionality

### Example Streaming System

- introduce streaming system 605
- describe server 603 functionality
- explain client device 604 functionality
- illustrate network 606 functionality
- describe game streaming system functionality
- explain game session processing
- describe input data transmission
- illustrate server-side rendering
- describe ray or path-traced lighting
- explain display data encoding
- describe encoded display data transmission
- illustrate client-side decoding
- describe display data display
- explain computer-readable medium functionality
- highlight arrangement of components

