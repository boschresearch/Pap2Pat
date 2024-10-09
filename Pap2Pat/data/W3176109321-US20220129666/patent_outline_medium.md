# DESCRIPTION

## TECHNICAL FIELD

- relate to anomaly detection

## BACKGROUND

- introduce human poses
- motivate anomaly detection

## SUMMARY

- introduce anomaly detector
- motivate one-class classifier
- describe pair of complementary classifiers
- address non-convex optimization problem
- introduce Hilbert space
- describe kernel embedding
- summarize anomaly detection

## DETAILED DESCRIPTION

- establish disclosure framework

### Overview

- introduce anomaly detector for human poses
- describe objective of anomaly detector
- explain discriminative one-class classifier
- illustrate anomaly detection in sequence of poses using FIG. 1
- describe sequence of poses and normal data
- explain complexity and non-linearity of sequence of poses
- introduce arbitrarily shaped boundaries of discriminative classes
- describe anomaly detector components using FIG. 2
- explain input interface and memory
- describe processor and output interface
- explain embedding input data into reproducing kernel Hilbert space (RKHS)
- describe pair of complementary classifiers
- illustrate pair of complementary classifiers using FIGS. 3A, 3B, and 3C
- describe training of discriminative one-class classifier using FIG. 4
- explain pre-processing sequence of poses
- describe extracting pose features
- explain training pair of complementary classifiers
- describe min-max optimization technique
- formulate optimization problem
- introduce orthonormal frames
- derive alternative formulations
- introduce Euclidean distance measure
- define discriminative one-class classifier
- address non-convex optimization problem
- train pair of hyperspheres
- define one-class classifier
- derive parameters of one-class classifier
- describe anomaly detection pipeline
- embed input data into kernel space
- classify embedded data using one-class classifier
- render classification result
- describe vehicle driver assistance system
- capture sequence of image frames with poses
- detect anomaly poses in sequence of image frames
- filter and preprocess image frames
- overview of anomaly detector
- normalize pose sequences
- generate vector representation
- embed into sequence representation
- map to normalized histogram
- detect anomaly in sequence of poses
- embed input data into RKHS
- classify using discriminative one-class classifier
- render classification result
- implement in vehicle driver assistance system
- implement in security surveillance system
- detect anomaly poses in different activities
- notify operators of security surveillance system
- implement in different applications
- overall block diagram of anomaly detector
- execute stored instructions
- output classification result

