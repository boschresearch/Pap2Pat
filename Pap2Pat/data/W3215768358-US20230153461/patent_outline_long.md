# DESCRIPTION

## BACKGROUND

- introduce machine learning
- limitations of data sharing
- motivate model parameter sharing
- limitations of model parameter sharing
- introduce federated learning
- limitations of federated learning
- need for improvements

## SUMMARY

- introduce proxy model
- train proxy model with private model
- define training loss
- introduce differentially private algorithm
- calculate privacy cost
- stop training based on privacy cost
- introduce mixing step
- share proxy models with peers
- update model with received proxy models
- introduce adjacency matrix
- debias proxy models with bias matrix
- outperform existing alternatives

## DETAILED DESCRIPTION

### Architecture Overview

- introduce model training systems
- describe private data
- motivate proxy model
- describe proxy model architecture
- describe private model architecture
- introduce training module
- describe training process
- introduce communications module
- describe parameter sharing
- introduce inference module
- describe prediction process
- illustrate training and inference process
- introduce multiple model training systems
- describe private model training
- describe proxy model training
- introduce distillation loss
- describe private loss calculation
- describe distillation loss calculation
- introduce total loss for private model
- introduce total loss for proxy model
- describe differentially private algorithm
- introduce privacy cost measurement
- describe privacy cost calculation
- introduce differentially private stochastic gradient descent
- describe gradient generation for proxy model
- describe gradient generation for private model
- introduce stochastic gradient descent steps
- describe gradient calculation for private model
- describe gradient calculation for proxy model
- introduce batch sampling
- describe contribution of each training item
- conclude architecture overview
- introduce architecture overview
- define proxy model parameters
- motivate KL-divergence
- derive per-item gradient
- clip gradients
- add Gaussian noise
- bound individual item contributions
- update model parameters
- describe proxy model architecture
- motivate different architecture
- train proxy model
- mix proxy models
- describe training iteration
- select training data
- update private model parameters
- generate updated proxy model
- mix proxy models with adjacency matrix
- correct bias
- determine next proxy model parameters
- update bias matrix
- debias proxy model parameters

### Experimental Results

- introduce experiment setup
- describe dataset splitting
- explain data distribution
- introduce non-IID data
- describe client data
- introduce models for comparison
- describe model architectures
- outline training parameters
- introduce mutual learning parameter
- present results of experiment 1
- show performance on test datasets
- compare ProxyFL with other models
- present communication time results
- show communication cost comparison
- present results of experiment 2
- show performance on non-IID data
- compare ProxyFL with other models on non-IID data
- introduce real-world dataset
- describe data preprocessing
- outline experiment setup for real-world dataset
- present results of experiment 3
- show performance on internal and external test data
- compare communication efficiency of models

