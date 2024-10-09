# DESCRIPTION

## BACKGROUND

- motivate quantization

## SUMMARY

- introduce optimally clipped tensors

## DETAILED DESCRIPTION

- introduce optimally clipped tensors and vectors
- define quantization-aware training (QAT)
- describe clipping scalars and their role in QAT
- motivate dynamic quantization
- introduce max-scaling and its limitations
- define quantization noise and its metricization
- derive analytical expression for MSE
- illustrate quantization MSE as a function of clipping scalar
- observe optimal clipping scalar s* and its properties
- describe limitations of brute force search for s*
- introduce online computation of optimal clipping scalars
- describe neural network architecture for QAT
- detail layer processing unit and quantizing logic
- explain clipping scalar optimization unit
- describe quantization unit and its operation
- derive recursive expression for optimal clipping scalar
- introduce Newton-Raphson algorithm for computing s*
- describe OCTAV algorithm for tensor and vector quantization
- illustrate flowchart of method for quantizing tensors
- compute first clipping scalars for quantizing first tensors
- process input by neural network model using quantized tensors
- adjust first tensors according to mean squared error
- update first clipping scalars based on adjusted first tensors
- illustrate clipping scalars and MSE determined by brute force search and OCTAV

### QAT Gradient Estimation

- introduce QAT with minimal noise
- motivate gradient estimation for quantization
- describe limitations of STE and PWL gradients
- analyze gradient back-propagation using STE
- formulate improved gradient estimator using MAD
- compare MAD with STE and PWL
- apply MAD to weight and activation gradient estimation
- illustrate neural network system for QAT
- conclude OCTAV-enabled QAT for low-precision training

### Parallel Processing Architecture

- introduce parallel processing unit (PPU) 400
- describe PPU 400 components
- illustrate PPU 400 architecture
- define input/output (I/O) unit 405
- describe front end unit 415
- introduce scheduler unit 420
- define work distribution unit 425
- describe hub 430
- introduce crossbar (Xbar) 470
- describe general processing clusters (GPCs) 450
- introduce memory partition units 480
- describe local memory 404
- introduce NVLink 410 interconnect
- describe I/O unit 405 functionality
- describe front end unit 415 functionality
- describe scheduler unit 420 functionality
- describe work distribution unit 425 functionality
- describe GPC 450 functionality
- describe memory partition unit 480 functionality
- introduce cooperative groups
- describe cooperative groups functionality
- introduce tensor cores
- describe tensor core functionality
- summarize PPU 400 applications

### Exemplary Computing System

- introduce high-performance GPU-accelerated systems
- describe processing system 500 with PPU 400
- illustrate NVLink 410 high-speed communication links
- detail switch 510 interfaces
- describe parallel processing module 525
- explain NVLink 410 data transfer rates
- introduce CPU 530 and memory 404
- describe NVLink 410 coherency operations
- detail Address Translation Services (ATS)
- illustrate system 565 with central processing unit 530
- describe communication bus 575
- detail main memory 540
- explain computer-readable media
- describe computer storage media
- introduce CPU(s) 530 and parallel processing module 525
- detail input device(s) 560 and display device(s) 545
- describe network interface 535
- explain natural user interface (NUI)
- detail system 565 in a network environment
- describe cloud-based network environments

### Machine Learning

- introduce deep neural networks
- explain neural learning process
- describe artificial neuron
- illustrate deep neural network model
- explain training process
- describe inference process
- highlight importance of matrix math operations
- introduce PPU 400 for deep neural network-based AI
- illustrate system for training and utilizing machine learning
- describe client device and provider environment
- explain training and inference manager
- describe training module and model repository
- illustrate inference module and user context data repository
- explain use of GPU for deep learning
- describe video data enhancement
- highlight supervised and unsupervised training

### Graphics Processing Pipeline

- introduce graphics processing unit
- describe processing of graphics primitives
- explain rendering and display of frame buffer

### Example Streaming System

- introduce streaming system
- describe server and client device
- explain network communication
- illustrate game streaming system
- describe rendering and encoding of display data
- explain decoding and display of display data
- highlight computer-readable medium for storing executable instructions

