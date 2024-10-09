# DESCRIPTION

## STATEMENT REGARDING PRIOR DISCLOSURES BY THE INVENTOR OR A JOINT INVENTOR

- disclose prior art

## BACKGROUND

- define machine learning
- explain hyperparameters
- introduce neural networks

## SUMMARY

- outline computer-implemented method

## DETAILED DESCRIPTION

- introduce knowledge graphs
- motivate limitations of existing knowledge graphs
- describe canonicalizing using variational autoencoders (CUVA)
- introduce functional block diagram of computing environment
- describe client computing device and server computer
- describe canonicalization program
- describe database
- describe network

### Example Table 1

- introduce example table
- describe clustering entities, noun phrases, and relation phrases
- describe variational auto encoder for entities
- describe variational auto encoder for relation mentions
- describe module for knowledge base completion
- describe training neural network architecture
- describe encoder block
- describe decoder block
- describe encoding side information
- describe loss measure
- describe mean squared error value
- describe side information loss
- describe training neural network
- describe operational steps for training neural network

### Further Comments and/or Embodiments

- describe benefits and improvements of CUVA

### 1. INTRODUCTION

- introduce knowledge graphs
- motivate limitations of existing knowledge graphs
- introduce canonicalizing using variational autoencoders (CUVA)

### 2. RELATED WORK

- summarize related work on Open KGs canonicalization

### 3. OPEN KGS CANONICALIZATION USING VAE

- define canonicalization task
- introduce CUVA architecture
- describe variational autoencoder
- explain encoder and decoder blocks
- describe KGE module
- explain side information usage

### 4. Training Strategy

- initialize mixture of Gaussians
- describe two-step training strategy
- explain encoder training
- explain decoder training

### 5. Evaluation

- introduce evaluation task
- describe ReVerb45K dataset
- describe CANONICNELL dataset
- explain evaluation metrics
- describe CUVA approach
- describe CESI approach
- compare CUVA and CESI results on ReVerb45K
- compare CUVA and CESI results on CANONICNELL
- evaluate CUVA with varying strategies
- evaluate CUVA against pretrained language models

### 6. CONCLUSION AND FUTURE WORK

- summarize CUVA approach
- summarize results
- introduce CANONICNELL dataset
- discuss future work on improving cluster quality
- discuss future work on link prediction
- describe computing environment
- describe computer system components
- describe cache and memory
- describe persistent storage
- describe communications unit
- describe I/O interface
- discuss computer readable storage medium

