# DESCRIPTION

## A. TECHNICAL FIELD

- define technical field

## B. BACKGROUND

- motivate question answering

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce patent description
- define invention scope
- describe component representation
- explain connection between components
- define embodiment terminology
- incorporate references by reference

### A. Introduction

- introduce open-domain question answering
- describe knowledge graph usage
- formulate core task of QA system
- introduce simple questions
- propose new system for answering simple questions
- outline system components

### B. Related Work

- discuss knowledge base-supported QA
- describe semantic parsing approaches
- introduce continuous embedding approaches
- relate to compositional neural embedding and continuous knowledge base embedding

### C. Overview

- introduce knowledge graph κ
- formulate answering simple question
- describe neural pipeline components
- introduce subject labeling module
- introduce relation ranking module
- introduce joint disambiguation module
- summarize system pipeline

### D. Model Embodiments

- introduce subject labeling
- formulate sequential labeling problem
- review Stacked Bidirectional GRU-RNN
- describe embedding layer
- describe S-Bi-GRU layer
- describe logistic regression layer
- train model by Backpropagation
- predict subject chunk
- obtain candidate subjects
- illustrate process for subject labeling
- parse input query
- input words to subject labeling model
- identify subject chunk
- send query to knowledge base
- get candidate subject entities
- illustrate detailed process of step 244
- transform words to embeddings
- generate tokens and classification features
- predict probability of each token
- concatenate tokens as subject chunk
- introduce relation ranking
- formulate ranking problem
- represent relation as vector
- embed question into vector space
- compute semantic similarity
- illustrate process for relation ranking
- receive query
- generate question vector
- query database for relation vectors
- determine ranking score
- illustrate detailed process of step 344
- transform words to embeddings
- project vector into k-dimensional space

### E. Training

- introduce mini-batch negative sampling
- compute embeddings and dot products
- relieve repeated computation problem
- introduce AdaGrad with momentum schedule
- adjust learning rate element-wise
- combine AdaGrad with momentum
- update parameters using accumulated velocity
- introduce momentum schedule
- disable momentum in early stage
- increase momentum gradually
- apply vertical dropout to S-Bi-GRU
- use pretrained word embedding
- tune model structure and hyperparameters
- fine-tune word embedding layer
- train S-Bi-GRU and logistic regression layer

### F. Knowledge Graph

- introduce knowledge graph data source
- describe graph database usage

### G. Some Conclusions

- summarize system advantages

### H. System Embodiments

- introduce system diagram
- describe natural language query interface
- explain preprocessor stage
- introduce HISQA subject & relation model
- describe query generator
- explain knowledge graph server
- introduce answer rendering module
- describe training system
- introduce HISQA subject & relation model diagram
- explain input question processing
- describe subject labeling model
- explain database query for candidate subjects
- introduce relation ranking model
- describe question vector generation
- explain relation vector generation
- describe ranking score calculation
- introduce joint disambiguation
- explain predicted subject entity and relation selection
- describe answer retrieval
- introduce flowchart for answer provision
- describe input query reception
- explain subject labeling
- describe candidate subject retrieval
- explain relation ranking score generation
- describe disambiguation
- explain predicted subject and relation selection
- describe answer retrieval from database

