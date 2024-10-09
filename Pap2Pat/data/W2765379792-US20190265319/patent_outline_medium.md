# DESCRIPTION

## STATEMENT OF GOVERNMENT INTEREST

- acknowledge government support

## FIELD

- define field of drug discovery

## BACKGROUND

- introduce natural products research
- describe limitations of traditional NMR practices
- motivate need for new approaches

## SUMMARY

- introduce systems and methods for rapid dereplication
- describe integration of fast 2D NMR and deep learning
- motivate advantages over prior art techniques
- outline method for determining data about natural products
- describe various implementations of the invention
- highlight advantages of the invention

## DETAILED DESCRIPTION

- introduce deep learning for 2D NMR spectra analysis
- motivate use of deep learning for small training samples
- describe HSQC spectra as fingerprints for natural product molecules
- contrast HSQC with other techniques (HMBC, COSY)
- highlight advantages of HSQC (clean experiment, few artifacts)
- introduce SMART system for integrating Fast 2D NMR with Neural Network
- describe Fast 2D NMR program for HSQC with Non Uniform Sampling (NUS)
- explain data reconstruction with combined Poisson Gap and Maximum Entropy Method
- describe Siamese DCNN applying Energy-Base Model (EBM) for spectral detection and ranking
- highlight benefits of using Fast 2D NMR (time-saving, high-quality spectra)
- contrast with conventional 2D NMR comparison methods
- describe limitations of computer-aided structure elucidation (CASE)
- introduce DCNN as image recognition-based analysis technique
- describe creation of SMART prototype with database of 2D HSQC spectra
- explain Training Embedding Map (TEM) and its application
- describe testing of SMART with NUS HSQC spectra of nonribosomal peptide synthetase (NRPS) derived NPs
- highlight user-friendly and unbiased nature of SMART
- describe SMART workflow (2D NMR data acquisition, spectral analysis, molecular structure output)
- illustrate SMART workflow with viequeamide NPs example
- describe alternative implementation of SMART method
- explain use of deep learning technique for structure identification
- highlight advantages of using convolutional neural network (CNN)
- describe application of Siamese network architecture for clustering HSQC spectra

### Network Training and Results Mapping

- train neural network using stochastic gradient descent
- speed up training with batch normalization
- divide datasets into training, validation, and test sets
- monitor error on validation set and embed test results in clustering map
- measure top N error and report accuracy results
- visualize training and test results in two-dimensional map
- analyze clustering results and quantify structural similarity

### SMART Characterization of Viequeamides of NRPS Origin

- characterize viequeamides

## EXAMPLES

### NUS 2D NMR Data Generation

- outline experimental setup

### Deep Convolutional Neural Network

- compile HSQC spectra dataset
- process HSQC spectra images
- describe dataset distribution
- introduce 10-fold validation scheme
- define DCNN architecture
- specify energy loss function
- apply dropout regularization
- experiment with embedding layer dimensions
- illustrate precision curves for different dimensions
- describe Siamese network mapping
- compare with conventional machine learning methods
- generate precision-recall curves
- describe feature extraction by deep network
- introduce loss function design
- define deep convolutional neural network
- introduce contrastive loss function
- motivate softmax layer
- describe final loss function
- introduce SMART system
- describe applications of SMART
- illustrate precision recall curves
- describe training process
- introduce robustness testing
- describe noise addition process
- illustrate distance vs. noise power plots
- describe clustering map visualization
- motivate novel compound discovery
- describe natural products discovery workflow
- introduce Fast NMR technique
- describe deep learning system
- illustrate benefits of SMART system
- describe implementation of SMART system

