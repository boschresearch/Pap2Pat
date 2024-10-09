# DESCRIPTION

## BACKGROUND

- motivate quantization

## SUMMARY

- introduce optimally clipped tensors

## DETAILED DESCRIPTION

- introduce optimally clipped tensors and vectors
- motivate quantization-aware training (QAT)
- describe limitations of conventional techniques
- define quantization and clipping
- derive analytical expression for mean squared error (MSE)
- illustrate quantization MSE as a function of clipping scalar
- describe neural network architecture for QAT
- compute optimal clipping scalars using Newton-Raphson algorithm
- illustrate flowchart for quantizing tensors of a neural network model
- describe advantages of OCTAV algorithm
- compare OCTAV with brute force search
- summarize benefits of QAT using MSE-optimal clipping scalars

### QAT Gradient Estimation

- motivate QAT with minimal noise
- analyze limitations of STE and PWL gradients
- introduce magnitude-aware derivative (MAD) for improved gradient estimation
- evaluate OCTAV-enabled QAT for neural network training

### Parallel Processing Architecture

- introduce parallel processing unit (PPU) 400
- describe PPU 400 components
- detail input/output (I/O) unit 405
- explain front end unit 415
- describe scheduler unit 420
- detail work distribution unit 425
- explain general processing clusters (GPCs) 450
- describe memory partition units 480
- detail XBar 470 interconnect network
- explain task management and execution
- describe memory hierarchy and caching
- summarize PPU 400 applications and configurations

### Exemplary Computing System

- describe high-performance GPU-accelerated systems
- illustrate processing system 500 with PPU 400 and CPU 530
- detail NVLink 410 high-speed communication links
- describe switch 510 interfaces and interconnect 402
- illustrate parallel processing module 525 on a single semiconductor platform
- describe NVLink 410 features, including coherency operations and Address Translation Services
- illustrate system 565 with CPU 530, switch 510, and parallel processing module 525
- describe main memory 540 and computer-readable media
- detail CPU(s) 530 and parallel processing module 525 execution of computer-readable instructions
- describe system 565 components, including input device(s) 560, display device(s) 545, and network interface 535

### Machine Learning

- introduce deep neural networks
- describe neural network architecture
- explain training process
- discuss inference process
- illustrate system components for machine learning
- describe request and response flow
- discuss training data and model selection
- explain supervised and unsupervised training

### Graphics Processing Pipeline

- describe graphics processing pipeline

### Example Streaming System

- introduce streaming system architecture
- describe client-server interaction
- explain rendering and display process

