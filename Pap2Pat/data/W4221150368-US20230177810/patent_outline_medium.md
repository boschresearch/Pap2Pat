# DESCRIPTION

## FIELD OF THE INVENTION

- relate to machine learning

## BACKGROUND

- motivate semantic segmentation

## DETAILED DESCRIPTION

- define semantic segmentation
- motivate machine learning environment
- illustrate method 100 for semantic segmentation training
- train machine learning environment with image/caption pairs
- describe image encoder architecture
- extract nouns from captions and convert to text prompts
- perform contrastive loss operations during training
- perform semantic segmentation with trained machine learning environment
- input unlabeled image and category names into trained machine learning environment
- perform vision-text similarity computation operations during inference
- describe optional architectures and features

### Parallel Processing Architecture

- introduce parallel processing unit (PPU)
- describe PPU as multi-threaded processor
- motivate latency hiding architecture
- define thread of execution
- describe PPU as graphics processing unit (GPU)
- list applications of PPU
- describe input/output (I/O) unit
- describe front end unit
- describe scheduler unit
- describe work distribution unit
- describe hub and crossbar (Xbar)
- describe general processing clusters (GPCs)
- describe partition units
- describe memory interface
- describe GPC components
- describe memory partition unit
- introduce parallel processing architecture
- describe memory hierarchy
- explain data transfer between processors
- detail memory partition unit
- describe data caching
- introduce streaming multi-processor
- describe instruction scheduling
- explain cooperative groups
- detail functional units
- describe register file
- introduce tensor cores
- describe special function units
- explain load and store operations
- describe shared memory and cache

### Exemplary Computing System

- describe high-performance GPU-accelerated systems
- illustrate processing system 400 with PPU 200 and CPU 430
- detail NVLink 210 high-speed communication links
- describe various embodiments of parallel processing module 425
- specify signaling rate and data transfer rate of NVLink 210
- illustrate exemplary system 465 with CPU 430 and parallel processing system 425
- describe system 465 components and functionality
- discuss applicability of architecture and functionality to various systems

### Machine Learning

- introduce deep neural networks
- motivate neural networks
- define artificial neuron
- describe deep neural network model
- explain training process
- describe inference process
- highlight importance of matrix math operations
- introduce PPU 200 computing platform
- introduce exemplary semantic segmentation environment
- describe image encoder
- describe text encoder
- explain contrastive loss operations
- describe vision-textual similarity computation operations
- introduce GroupViT architecture and training pipeline
- describe hierarchical grouping mechanism
- explain zero-shot transfer to semantic segmentation
- summarize machine learning environment architecture
- define machine learning environment
- introduce hierarchical grouping
- derive grouping block equations
- describe image-text contrastive loss
- introduce multi-label image-text contrastive loss
- define total image-text contrastive loss
- describe zero-shot transfer to semantic segmentation
- explain prompting engineering mechanism
- discuss limitations of embodiments
- describe computer code and machine-useable instructions
- provide clarification on terminology and scope

