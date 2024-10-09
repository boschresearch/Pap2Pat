# DESCRIPTION

## FIELD OF THE INVENTION

- relate to MLX

## BACKGROUND

- motivate ML and deep learning
- describe complexity of deep learning models
- limitations of interpreting deep learning models
- introduce inherently interpretable models
- motivate MLX
- introduce feature attribution-based explanation
- describe autoencoder architecture
- motivate explainability for autoencoder

## DETAILED DESCRIPTION

- introduce machine learning explanation approach for autoencoder's reconstruction error

### General Overview

- introduce layer-wise relevance propagation (LRP) for feature attribution-based explanation (ABX) for reconstructive autoencoder
- describe LRP computation of input attributions by directly propagating an artificial neural network's (ANN) prediction backward
- discuss LRP propagation rules for various neural layer types
- introduce novel propagation rule for applying LRP to autoencoders using deep Taylor decomposition (DTD)
- describe advantages of the approach, including low algorithmic complexity and straightforward implementation
- summarize novel aspects of the approach

### 1.0 Example Computer

- introduce example computer 100 for machine learning (ML) explainability (MLX)
- describe reconstructive neural network 110 as an artificial neural network (ANN) such as an autoencoder
- discuss various ML tasks that reconstructive neural network 110 can perform
- introduce original tuple 131 and reconstructed tuple 132
- describe reconstruction error 150 as a measured difference between tuples 131-132
- discuss various scenarios for reviewing a tuple, its corresponding inference, and/or reconstructive neural network 110
- introduce MLX functionalities, including explainability, interpretability, and what-if explanations
- describe feature engineering for tuples 131-132
- discuss datatypes of features F1-F3
- introduce categories and their encoding
- describe original tuple 131 as an instance of various objects
- introduce reconstruction error 150 as a measured difference between tuples 131-132
- describe calculation of reconstruction error 150 using a reconstruction error formula
- discuss value ranges of reconstruction error 150
- introduce neural layers in reconstructive neural network 110
- describe feed-forward sequence of neural layers
- discuss input layer and its neurons
- introduce reconstruction layer 180 and its neurons
- describe output of reconstruction layer 180 as reconstructed tuple 132
- discuss time T1, T2, T3, and T4 for inferencing and calculating reconstruction error 150
- introduce element relevance as a measurement of contribution to an output of reconstructive neural network 110
- discuss feature relevances FR1-FR3
- describe ABX based on feature relevances FR1-FR3
- introduce LRP for measuring feature relevances FR1-FR3
- describe LRP as performing arithmetic calculations while backwards traversing the sequence of neural layers
- discuss layer-specific relevance propagation rules 162
- introduce relevance propagation rules for fully-connected layer, convolutional layer, and pooling layer
- describe example layer formula for fully-connected layer
- discuss novel reconstructive relevance propagation rule 161 for reconstruction layers
- describe example relevance formula for reconstructive relevance propagation rule 161
- discuss time T5, T6, T7, and T8 for measuring neuron relevances and generating ABX explanation
- introduce Deep Taylor Decomposition (DTD) for neural layer
- describe arithmetic equalities for DTD
- discuss decomposition of the relevance of a neuron from a previous layer l into relevances of neurons from next layer l+1
- introduce example multi-layer formula for calculating relevances of neurons in neural layer l
- describe DTD 204 that combines the example multi-layer formula with DTD 202
- discuss advantages of using DTD
- introduce explainer as a software component hosted by computer 100
- describe explainer as generating a respective explanation of why reconstructive neural network 110 generated an inference
- summarize the example computer 100 for MLX

### 2.0 Deep Taylor Decomposition (DTD) for Neural Layer

- introduce DTD 202 for decomposing the relevance of a neuron from a previous layer l into relevances of neurons from next layer l+1
- describe arithmetic equalities for DTD 202
- introduce DTD 204 that combines the example multi-layer formula with DTD 202

### 3.0 DTD for Reconstruction Error

- define DTD 300 for reconstruction error formula
- introduce terms and their meanings in DTD 300
- describe Hessian matrix of reconstruction residual cost function
- state layer conservation axiom for neural layers
- state global conservation axiom for reconstructive neural network

### 4.0 Example Reconstruction Relevance Propagation Process

- introduce example process for reconstructive relevance propagation
- describe inference phase: generate reconstructed tuple and reconstruction error
- describe explanation phase: apply novel reconstruction relevance propagation rule
- perform LRP to measure neuron relevance for each neuron
- determine feature relevance of each feature
- generate ABX explanation of why reconstructive neural network regenerated original tuple

### 5.0 Example LRP Process for Database Security

- introduce example process for LRP in database security application
- describe reconstructive neural network accepting original tuple as feature vector
- provide examples of features in tuples representing database statements
- describe generating reconstructed tuple and inference
- describe anomaly detector analyzing dense encoding for anomaly score
- introduce optional ABX explainer using SHAP
- contrast SHAP with LRP for generating ABX explanation
- perform LRP to generate ABX explanation
- apply reconstruction relevance propagation rule to reconstruction residual cost function

### 6.0 Example Pseudocode

- provide example pseudocode listings for LRP on reconstructive neural network

## Hardware Overview

- introduce special-purpose computing devices
- describe hardware components of computing devices
- illustrate computer system 600
- describe bus 602
- introduce hardware processor 604
- describe main memory 606
- describe read only memory (ROM) 608
- introduce storage device 610
- describe display 612
- introduce input device 614
- describe cursor control 616
- describe communication interface 618
- introduce network link 620
- describe local network 622
- describe Internet 628
- describe transmission media

## Software Overview

- introduce software system 700
- describe kernel or operating system (OS) 710
- introduce application programs 702
- describe graphical user interface (GUI) 715
- introduce hypervisor or virtual machine monitor (VMM) 730
- describe virtual machine instances
- describe guest operating systems
- describe VMM 730 functionality

## Cloud Computing

- define cloud computing
- describe public cloud environment
- describe private cloud environment
- describe community cloud environment
- describe hybrid cloud environment
- describe cloud service layers

## Machine Learning Models

- introduce machine learning models
- describe model data representation or model artifact
- describe supervised training
- describe objective function
- describe optimization algorithm
- describe inferencing
- describe classes of problems that machine learning excels at

## Artificial Neural Networks

- introduce artificial neural networks (ANN)
- describe layered feedforward neural network
- describe activation neurons and activation functions
- describe edges and weights in neural networks

## Illustrative Data Structures for Neural Network

- define neural network artifact
- introduce matrices of weights and biases
- describe layered feedforward network
- explain matrix storage
- define input and training data
- describe activation values and matrix storage
- discuss optimization algorithms and derivative values
- explain properties of matrices and neurons
- introduce vectorization and parallelism

### Backpropagation

- introduce backpropagation
- explain error measurement and delta values
- describe edge weight adjustment
- discuss model training and error reduction

### Autoencoder

- introduce autoencoder
- explain unsupervised model training
- describe encoder/decoder functionality
- discuss condensed code and intermediate format

### Principal Component Analysis

- introduce principal component analysis

### Random Forest

- introduce random forest
- explain decision tree construction
- discuss hyper-parameters and prediction calculation

