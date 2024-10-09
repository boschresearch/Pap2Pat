# DESCRIPTION

## A. TECHNICAL FIELD

- define technical field

## B. BACKGROUND

- motivate question answering

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- define patent application structure

### A. Introduction

- motivate open-domain question answering

### B. Related Work

- summarize existing knowledge base-supported QA approaches

### C. Overview

- introduce neural pipeline for simple question answering

### D. Model Embodiments

- define subject labeling model
- formulate subject labeling as sequential labeling problem
- describe Stacked Bidirectional GRU-RNN architecture
- illustrate subject labeling process with flowchart
- define relation ranking model
- formulate relation ranking as ranking problem
- describe S-Bi-GRU based model for relation ranking
- illustrate relation ranking process with flowchart

### E. Training

- describe mini-batch negative sampling technique
- explain AdaGrad with momentum schedule optimization algorithm
- discuss additional training techniques: dropout, pretrained word embedding, and hyperparameter tuning

### F. Knowledge Graph

- describe knowledge graph data source and storage

### G. Some Conclusions

- summarize system and method for simple question answering

### H. System Embodiments

- describe system diagram and components
- detail HISQA subject & relation model
- explain query generator and knowledge graph server
- describe answer rendering module
- illustrate HISQA subject & relation model diagram
- outline process for providing answer to input query

