# DESCRIPTION

## A. TECHNICAL FIELD

- define technical field

## B. BACKGROUND

- motivate question answering

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- define patent application structure
- describe components and connections
- explain terminology and references

### A. Introduction

- introduce open-domain question answering
- describe simple questions and their challenges
- propose a new system for answering simple questions

### B. Related Work

- discuss knowledge base-supported QA research
- describe entity linking and representation learning approaches

### C. Overview

- formulate simple question answering as a query
- describe the neural pipeline for finding the best match
- outline the system's modules and their interactions

### D. Model Embodiments

- introduce subject labeling
- formulate sequential labeling problem
- review Stacked Bidirectional GRU-RNN
- describe model structure for subject labeling
- train model using Backpropagation
- predict subject chunk
- obtain candidate subjects
- introduce relation ranking
- formulate ranking problem
- describe embedding approach
- compute semantic similarity
- train ranking model using margin ranking loss
- introduce joint disambiguation
- perform joint disambiguation
- predict subject and relation
- generate structured query

### E. Training

- introduce mini-batch negative sampling
- describe AdaGrad with momentum schedule
- apply vertical dropout to S-Bi-GRU
- use pretrained word embedding
- tune model structure and hyperparameters
- train subject labeling model
- train relation ranking model

### F. Knowledge Graph

- describe knowledge graph data source and storage

### G. Some Conclusions

- summarize system and method for simple question answering

### H. System Embodiments

- introduce system diagram
- describe natural language query interface
- describe preprocessor stage
- describe HISQA subject & relation model
- describe query generator
- describe knowledge graph server
- describe answer rendering module
- describe training system
- introduce HISQA subject & relation model diagram
- describe subject labeling model
- describe relation ranking model
- describe joint disambiguation
- describe process for providing answer to input query

