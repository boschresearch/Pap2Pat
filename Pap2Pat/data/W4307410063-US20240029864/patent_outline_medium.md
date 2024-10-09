# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate few-shot learning

## DETAILED DESCRIPTION

- overview of system-on-a-chip (SoC) and its components

### Overview

- illustrate SoC implementation
- describe CPU and its functions
- describe NPU and its functions
- describe GPU and its functions
- describe DSP and its functions
- describe connectivity block and its functions
- describe multimedia processor and its functions
- describe sensor processor and its functions
- describe image signal processors and their functions
- describe navigation module and its functions
- describe machine learning and its applications
- describe neural networks and their types
- describe deep learning and its applications
- describe neural network architecture and its layers
- describe few-shot learning scenario and its applications

### Example Embodiments

- introduce prototypical machine learning networks
- motivate variance-aware prototypical networks
- describe limitations of existing PLM implementations
- introduce meta-learning as a solution
- describe challenges of meta-training for NLP tasks
- introduce three common approaches to meta-learning
- describe prototypical networks and their limitations
- motivate need for systems and techniques that can utilize large labeled datasets
- introduce novel loss function and regularization term
- describe example datasets for training variance-aware prototypical networks
- describe example shoulder dataset and its label space
- describe meta-learning approach for downstream classification tasks
- describe four downstream medical anatomy/pathology classification tasks
- summarize advantages of variance-aware prototypical networks

### Example Workflow

- introduce machine learning architecture and workflow
- receive radiology reports as input
- de-identify input radiology reports according to HIPAA regulations
- split reports into sentences using report segmentation engine
- generate report segments
- implement body-part specific workflow
- use custom data processor to obtain relevant text
- predict pathology severity using classification engine
- illustrate report segmentation for cervical-spine specific input radiology reports
- post-process output to generate concatenated text segments
- illustrate knee-specific implementation of architecture and workflow
- use BERT-based NER model to automatically tag sentences
- group sentences that mention structure of importance
- predict pathology severities using classification engine

### Variance-Aware ProtoNets

- model conditional distribution as Gaussian
- compute Wasserstein distance between Gaussian and query vector
- simplify prototypical network conditional distribution using Gaussian with diagonal covariance matrix

### Experimental Results

- summarize experimental results for BERT-base and Clinical BERT backbones
- compare results against various benchmarks and baselines
- select best model based on meta-validation accuracy
- apply best model to downstream classification tasks

## Deployment

- deploy variance-aware ProtoNet with Adapter-PubMedBERT
- describe pipeline components and inference process

## Monitoring

- describe out-of-distribution detection using Average Variance Indices (AVI)

## CONCLUSION

- summarize extension of Prototypical Networks using Wasserstein distances
- introduce regularization term to encourage class examples clustering
- describe successful downstream performance on various labels
- highlight single model deployment for inference cost savings
- describe use of adapters for tuning small number of parameters
- highlight huge training cost savings
- describe extensive experiments on 13 public datasets
- validate systems and techniques for variance-aware ProtoNets
- outperform strong baselines like ProtoNets and Leopard
- leverage dataset statistics for OOD detection
- define OOD detection metric called Average Variance Indices (AVI)
- illustrate example computing device architecture
- describe components of computing device architecture
- highlight cache performance boost
- describe processor control and service configuration
- enable user interaction with computing device architecture
- describe storage device and services
- provide general description of device and system

