# DESCRIPTION

## BACKGROUND

- motivate image analysis

## BRIEF SUMMARY

- introduce patch-based multi-scale Transformer
- describe multi-scale representation
- explain spatial embedding
- introduce scale embedding
- describe self-attention mechanism
- outline method for processing imagery
- summarize advantages

## DETAILED DESCRIPTION

### Overview

- introduce patch-based multi-scale Transformer
- describe image representation and Transformer encoder

### Overall Architecture

- illustrate multi-scale image representation
- describe patch encoding and spatial embedding
- introduce Transformer encoder and classification token

### Multi-Scale Patch Embedding

- describe multi-scale input and patch extraction
- introduce patch encoding module and ResNet
- describe sequence of patch embeddings and padding
- discuss advantages of multi-scale representation

### Hash-Based 2D Spatial Embedding

- introduce hash-based spatial embedding
- describe spatial embedding calculation
- discuss advantages of hash-based spatial embedding
- introduce trade-off between expressiveness and trainability

### Scale Embedding

- introduce scale embedding to distinguish scales

### Pre-Training and Fine Tuning

- describe pre-training on large dataset
- discuss fine-tuning on downstream tasks

### The Transformer Encoder

- illustrate Transformer encoder block
- describe multi-head self-attention
- introduce layer normalization and residual connections
- discuss output of Transformer encoder

## EXAMPLE IMPLEMENTATION

- describe example implementation of multi-scale representation
- specify model architecture and hyperparameters
- detail training procedure and hyperparameters
- report results on PaQ-2-PiQ dataset
- visualize attention on original and resized images
- report results on KonIQ-10k dataset
- report results on SPAQ dataset
- report results on AVA dataset
- perform ablation study on spatial embeddings
- visualize learned HSE cosine similarity
- evaluate effect of adding SCE
- compare different patch encoding modules
- evaluate effect of patch size
- describe computing architecture for implementing patch-based multi-scale Transformer

