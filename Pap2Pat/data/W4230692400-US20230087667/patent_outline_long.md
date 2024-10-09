# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior art

## BACKGROUND

- define machine learning
- explain hyperparameters
- motivate neural networks
- describe neural network architecture
- explain neural network learning
- discuss neural network applications
- introduce canonicalizing using variational autoencoders

## SUMMARY

- outline computer-implemented method

## DETAILED DESCRIPTION

- introduce knowledge graphs
- motivate limitations of existing knowledge graphs
- describe current solutions to adaptability problem
- highlight deficiencies in current solutions
- introduce canonicalizing using variational autoencoders (CUVA)
- describe CUVA architecture
- explain hierarchical agglomerative clustering
- describe training of neural network
- introduce encoder and decoder sections
- describe constraint loss
- explain knowledge graph embedding module
- describe training of neural network in two steps
- introduce constraint-based loss
- describe encoding side information
- explain operational steps for training neural network
- summarize benefits of CUVA

### Example Table 1

- introduce example table
- describe clustering entities, noun phrases, and relation phrases
- introduce variational autoencoder for entities
- introduce variational autoencoder for relations
- describe module for knowledge base completion
- describe training of resulting neural network architecture
- describe building hierarchical agglomerative cluster model
- describe training encoder section
- describe training decoder section
- describe calculating total loss value
- describe FIG. 2A
- describe FIG. 2B
- describe FIG. 2C
- describe core structure of CUVA
- describe encoder block
- describe decoder block
- describe encoding side information
- describe FIG. 3
- describe FIG. 4
- describe FIG. 5
- describe FIG. 6
- describe receiving information
- describe dynamically clustering received information
- describe initializing cluster means and cluster variances
- describe dynamically training neural network
- describe using two loss functions
- describe training neural network in two steps
- describe using additional constraint-based loss
- describe encoding structural knowledge

### Further Comments and/or Embodiments

- describe benefits of CUVA
- describe deficiencies in current state of art
- introduce CANONICNELL dataset

### 1. INTRODUCTION

- introduce knowledge graphs
- motivate limitations of existing knowledge graphs
- describe open information extraction methods
- highlight shortcomings of open knowledge graphs
- introduce canonicalizing using variational autoencoders (CUVA)
- summarize contributions

### 2. RELATED WORK

- introduce OpenIE technique
- summarize rule-based and learning-based approaches
- discuss limitations of existing EL approaches

### 3. OPEN KGS CANONICALIZATION USING VAE

- define CANONICALIZATION task
- introduce CUVA architecture
- describe E-VAE and R-VAE components
- explain Gaussian distribution modeling
- describe KGE module
- introduce Variational AutoEncoder
- explain generative process
- describe Encoder block
- explain Decoder block
- describe cluster assignment
- introduce KGE module
- describe side information
- explain Side Information Loss

### 4. Training Strategy

- describe initializing mixture of Gaussians
- explain HAC clustering method
- describe two-step training strategy
- explain Encoder training
- describe NLL loss calculation
- explain Decoder training
- describe ELBO loss calculation
- explain combined loss function

### 5. Evaluation

- introduce CANONICALIZATION task
- describe ReVerb45K dataset
- introduce CANONICNELL dataset
- describe dataset statistics
- explain data division for test and validation sets
- describe hyper-parameter tuning
- introduce evaluation metrics
- describe CUVA approach
- describe CUVA with Side Information
- compare CUVA with existing methods
- analyze results on ReVerb45K
- analyze results on CANONICNELL
- compare CUVA with pretrained language models
- describe qualitative analysis
- illustrate output of CUVA
- analyze NP clusters
- analyze RP clusters
- describe ablation tests
- analyze importance of KGE Module
- analyze importance of hidden layer
- conclude evaluation

### 6. CONCLUSION AND FUTURE WORK

- summarize CUVA approach
- summarize contributions
- describe future work directions
- introduce Hypernymy Detection
- introduce Link Prediction
- describe computing environment
- describe computer system components
- describe communications fabric
- describe cache
- describe memory
- describe persistent storage
- describe communications unit
- describe I/O interface
- describe external devices
- describe display
- describe computer readable storage medium
- describe computer readable program instructions
- describe network
- describe network adapter card
- describe downloading program instructions
- describe executing program instructions
- describe computer readable program instructions
- describe flowchart illustrations
- describe block diagrams
- conclude description of embodiments

