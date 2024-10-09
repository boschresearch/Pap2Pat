# DESCRIPTION

## FIELD OF THE INVENTION

- relate to machine learning

## BACKGROUND

- motivate semantic segmentation

## DETAILED DESCRIPTION

- define semantic segmentation
- introduce machine learning environment
- describe image/caption pairs
- illustrate flowchart of method 100
- motivate training machine learning environment
- describe machine learning environment components
- retrieve image/caption pairs from databases
- extract nouns from captions
- convert nouns to text prompts
- describe image encoder
- output potential pixel groupings
- describe grouping block
- perform hierarchical spatial grouping
- describe text encoder
- output text representations
- perform contrastive loss operations
- create similarity matrix
- compare similarity matrices
- perform semantic segmentation
- input unlabeled image
- perform vision-text similarity computation
- return extracted feature for category name

### Parallel Processing Architecture

- introduce parallel processing unit (PPU)
- describe PPU as multi-threaded processor
- explain latency hiding architecture
- define thread of execution
- describe PPU as graphics processing unit (GPU)
- explain graphics rendering pipeline
- list applications of PPU
- describe Input/Output (I/O) unit
- explain front end unit
- describe scheduler unit
- explain work distribution unit
- describe hub
- explain crossbar (Xbar)
- describe general processing clusters (GPCs)
- explain partition units
- describe NVLink interconnect
- explain I/O unit functionality
- describe front end unit functionality
- explain scheduler unit functionality
- describe work distribution unit functionality
- explain GPC functionality
- describe partition unit functionality
- explain memory interface
- describe driver kernel
- explain application programming interface (API)
- describe task management
- explain warp
- describe cooperating threads
- introduce GPC architecture
- describe pipeline manager
- explain pre-raster operations unit (PROP)
- describe raster engine
- explain memory partition unit
- introduce parallel processing architecture
- describe error correction code
- implement multi-level memory hierarchy
- support unified memory
- trace memory accesses
- provide address translation services
- transfer data between processors
- generate page faults
- service page faults
- describe memory partition unit
- implement L2 cache
- implement lower level caches
- describe ROP unit
- perform graphics raster operations
- implement depth testing
- track packets
- describe streaming multi-processor
- implement instruction cache
- schedule thread blocks
- dispatch tasks
- describe cooperative groups
- enable synchronization
- describe dispatch unit
- implement register file
- describe processing cores
- implement tensor cores
- describe special function units
- implement load/store units

### Exemplary Computing System

- introduce high-performance GPU-accelerated systems
- motivate need for scalable communication mechanisms
- describe processing system 400 with PPU 200 and CPU 430
- illustrate NVLink 210 high-speed communication links
- describe switch 410 interface between interconnect 202 and CPU 430
- summarize parallel processing module 425
- describe alternative embodiments of NVLink 210 connections
- define single semiconductor platform
- describe NVLink 210 signaling rate and data transfer rate
- motivate direct load/store/atomic access from CPU 430 to PPU 200 memory
- describe coherency operations and Address Translation Services
- illustrate exemplary system 465 with central processing unit 430 and communication bus 475
- describe main memory 440 and input devices 460
- summarize display devices 445 and network interface 435
- describe secondary storage and computer programs
- conclude with scope of preferred embodiment

### Machine Learning

- introduce deep neural networks
- motivate deep learning
- define artificial neuron
- explain perceptron
- describe deep neural network model
- illustrate layers of perceptrons
- explain inference process
- describe training process
- explain forward propagation phase
- explain backward propagation phase
- highlight importance of matrix math operations
- describe PPU 200 capabilities
- introduce semantic segmentation environment
- describe image encoder
- describe text encoder
- explain image multilayer perceptron
- explain text multilayer perceptron
- describe contrastive loss operations
- explain training process of machine learning environment
- describe vision-textual similarity computation operations
- introduce GroupViT architecture
- describe hierarchy of transformer layers
- explain grouping block
- describe zero-shot transfer to semantic segmentation
- motivate bottom-up grouping
- describe limitations of fully convolutional network
- introduce semantic segmentation model
- describe training with text supervision
- explain vision transformer
- describe hierarchical grouping of visual tokens
- explain inference for semantic segmentation
- describe machine learning environment architecture
- explain grouping vision transformer
- describe multi-stage grouping
- define machine learning environment
- introduce hierarchical grouping
- derive grouping block equations
- explain hard assignment strategy
- explain soft assignment strategy
- compute output of grouping block
- introduce image-text contrastive loss
- define image-text contrastive loss equation
- define multi-label image-text contrastive loss
- generate prompted text labels
- define multi-label contrastive loss equation
- compute total image-text contrastive loss
- introduce zero-shot transfer to semantic segmentation
- infer segments of an image
- compute similarity between segment tokens and text embeddings
- assign segments to semantic classes
- transform label names into sentences
- classify spatial regions of the image
- discuss limitations of embodiments
- discuss scope of preferred embodiment
- describe computer code or machine-useable instructions
- discuss distributed computing environments

