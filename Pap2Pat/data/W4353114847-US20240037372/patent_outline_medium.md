# DESCRIPTION

## FIELD OF THE INVENTION

- relate to MLX

## BACKGROUND

- motivate ML and deep learning
- limitations of deep learning
- motivate MLX
- introduce autoencoder for anomaly detection

## DETAILED DESCRIPTION

- introduce machine learning explanation approach for autoencoder's reconstruction error

### General Overview

- introduce layer-wise relevance propagation (LRP) for feature attribution-based explanation (ABX) for reconstructive autoencoder
- describe LRP's ability to outperform other explanation methods
- introduce novel relevance propagation rule for applying LRP to autoencoders using deep Taylor decomposition (DTD)

### 1.0 Example Computer

- introduce example computer 100 for machine learning (ML) explainability (MLX)
- describe reconstructive neural network 110 as an artificial neural network (ANN) such as an autoencoder
- explain reconstructive neural network 110's ability to generate an inference and reconstructed tuple 132
- introduce reconstruction error 150 as a measured difference between tuples 131-132
- describe explainer component for generating an explanation of why reconstructive neural network 110 generated an inference
- introduce relevance propagation rules 161-162 for LRP explainer
- describe feature engineering for tuples 131-132
- explain datatypes for features F1-F3
- describe categories and their encoding
- introduce original tuple 131 as an instance of various objects
- describe reconstruction error 150 as a measured difference between tuples 131-132
- explain integration of respective reconstruction errors of all features F1-F3
- introduce reconstruction residual cost function 140
- describe example reconstruction error formula
- explain neural layers in reconstructive neural network 110
- describe feed-forward sequence of neural layers
- introduce reconstruction layer 180
- describe output of reconstruction layer 180 as reconstructed tuple 132
- explain element relevance measurement
- introduce LRP for measuring feature relevances FR1-FR3

### 2.0 Deep Taylor Decomposition (DTD) for Neural Layer

- introduce DTD 202 for decomposing the relevance of a neuron from a previous layer l into relevances of neurons from next layer l+1

### 3.0 DTD for Reconstruction Error

- define DTD 300 for reconstruction error formula
- introduce layer conservation axiom and global conservation axiom

### 4.0 Example Reconstruction Relevance Propagation Process

- describe inference phase of reconstructive neural network 110
- describe explanation phase of reconstructive neural network 110
- apply novel reconstruction relevance propagation rule 161

### 5.0 Example LRP Process for Database Security

- describe reconstructive neural network 110 for database security
- introduce features of database statement in tuples
- apply LRP for database security application
- compare with SHAP explainer

### 6.0 Example Pseudocode

- provide example pseudocode listings for LRP on reconstructive neural network 110

## Hardware Overview

- introduce special-purpose computing devices
- describe hardware components of computer system 600
- explain storage media and transmission media
- describe computer system 600 components and their interactions
- introduce communication interface 618 and network link 620
- describe data communication through networks
- explain receiving and executing code through networks
- summarize computer system 600 components and their functions

## Software Overview

- introduce software system 700 and its components
- describe operating system 710 and its functions
- explain graphical user interface 715 and its interactions
- introduce virtual machine monitor 730 and its functions

## Cloud Computing

- define cloud computing and its characteristics
- describe different types of cloud environments
- explain service layers in cloud computing

## Machine Learning Models

- introduce machine learning models and their training
- describe supervised training and its process
- explain inferencing and its process

## Artificial Neural Networks

- introduce artificial neural networks and their components
- describe layered feedforward neural networks and their functions

## Illustrative Data Structures for Neural Network

- define neural network artifact
- describe matrices for weights and biases
- explain storage of matrices and inputs
- discuss advantages of smaller neural networks

### Backpropagation

- motivate backpropagation
- describe error calculation and weight adjustment

### Autoencoder

- introduce autoencoder concept
- explain unsupervised training and condensed code

### Principal Component Analysis

- introduce PCA for dimensionality reduction

### Random Forest

- describe random forest concept and hyper-parameters

