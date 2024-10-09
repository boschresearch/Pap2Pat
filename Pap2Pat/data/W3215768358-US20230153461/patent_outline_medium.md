# DESCRIPTION

## BACKGROUND

- motivate large-scale datasets
- limitations of data sharing
- limitations of model parameter sharing

## SUMMARY

- introduce proxy model and private model
- describe training process
- describe objective function
- describe differentially private algorithm
- describe mixing step
- describe benefits of approach

## DETAILED DESCRIPTION

### Architecture Overview

- introduce model training systems
- describe private data and its sensitivity
- motivate proxy model and private model
- describe proxy model and private model architecture
- explain data instances and output predictions
- describe training module and its functionality
- explain communication module and its functionality
- describe inference module and its functionality
- illustrate training and inference process
- describe private model training process
- describe proxy model training process
- explain distillation loss and its calculation
- describe private loss and its calculation
- explain total loss for private model and proxy model
- describe differentially private algorithm for proxy model
- explain gradient generation for proxy model and private model
- introduce architecture overview
- define proxy model parameters
- motivate clipping gradients
- describe differential privacy cost
- summarize training process
- illustrate training iteration
- explain mixing proxy models
- describe bias correction
- illustrate exponential communication protocol
- conclude private model training

### Experimental Results

- introduce experiment setup
- describe dataset preparation
- outline experiment procedure
- present results for ProxyFL embodiment
- compare ProxyFL with other federated models
- show communication time for parameter exchange
- evaluate robustness to non-IID dataset skew
- present example results for multi-origin real-world dataset
- describe experiment setup for WSI data
- present performance results for WSI data
- discuss limitations and variations of the invention

