# DESCRIPTION

## BACKGROUND

- motivate image analysis

## BRIEF SUMMARY

- introduce patch-based multi-scale Transformer
- motivate native resolution image
- describe multi-scale representation
- explain self-attention mechanism
- introduce hash-based 2D spatial embedding
- describe scale embedding
- summarize technical problems
- describe method for processing imagery
- construct multi-scale representation
- encode spatial embedding
- apply scale embeddings
- perform self-attention
- describe final image representation
- provide implementation details
- describe image processing system

## DETAILED DESCRIPTION

### Overview

- introduce patch-based multi-scale Transformer
- construct multi-scale image representation
- split images into fixed-size patches
- encode spatial and scale information
- perform multi-head self-attention

### Overall Architecture

- construct multi-scale image representation
- split images into fixed-size patches
- encode spatial and scale information
- perform multi-head self-attention
- add classification token to sequence
- predict image quality score or classification

### Multi-Scale Patch Embedding

- capture local and global information
- construct multi-scale input
- resize images using Gaussian kernel
- calculate number of patches
- encode patches using patch encoding module
- concatenate patch embeddings
- zero-pad or cut to fixed length
- attach input mask for masked self-attention
- ignore padding tokens during training

### Hash-Based 2D Spatial Embedding

- encode patch spatial information
- map patches to G×G grid
- define hash-based spatial embedding
- calculate ti and tj
- add spatial embedding to patch embedding
- align patches across scales
- choose suitable grid size G
- trade-off between expressiveness and trainability

### Scale Embedding

- introduce scale embedding
- mark input scale for each patch

### Pre-Training and Fine Tuning

- pre-train on large dataset
- fine-tune on downstream tasks
- use random cropping and augmentations
- fine-tune on IQA tasks
- use regression losses for IQA tasks

### The Transformer Encoder

- input embedded multi-scale representation
- define Transformer encoder block
- perform layer normalization
- perform multi-head self-attention
- perform multi-layer perceptron
- add residual connections
- formulate Transformer encoder
- choose suitable sequence length l

## EXAMPLE IMPLEMENTATION

- introduce multi-scale representation
- specify parameters for Transformer input tokens
- describe training process for MST-IQA models
- specify hyperparameters for training
- describe fine-tuning process
- specify hyperparameters for fine-tuning
- report results on PaQ-2-PiQ dataset
- visualize attention on original and resized images
- report results on KonIQ-10k dataset
- report results on SPAQ dataset
- report results on AVA dataset
- evaluate effectiveness of hash-based spatial embedding
- describe ablation study for spatial embeddings
- visualize learned HSE cosine similarity
- evaluate effectiveness of scale embedding
- describe different designs for encoding patches
- evaluate effect of patch size
- visualize attention from output tokens to multi-scale representation
- describe computing architecture for patch-based multi-scale Transformer
- illustrate example system for implementing patch-based multi-scale Transformer
- describe components of computing devices
- describe user interface subsystem
- describe communication between computing devices
- illustrate method for processing imagery
- construct multi-scale representation of native resolution image
- encode spatial embedding for each patch
- apply scale embeddings to capture scale information
- perform self-attention on input tokens to create final image representation

