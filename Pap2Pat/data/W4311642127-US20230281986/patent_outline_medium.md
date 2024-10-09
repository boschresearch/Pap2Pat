# DESCRIPTION

## TECHNICAL FIELD

- relate to video anomaly detection

## BACKGROUND

- introduce unsupervised video anomaly detection
- limitations of cross-domain video anomaly detection

## SUMMARY

- motivate zero-shot cross domain video anomaly detection
- introduce zVAD system
- summarize zVAD system components

## DETAILED DESCRIPTION

- set forth explanation approach
- define terminology and scope

### System Overview

- introduce training system for video anomaly detection
- describe system components: memory, first neural network, second neural network, processor
- explain memory functionality
- describe source domain data collection
- define source domain
- describe target domain
- explain task relevance
- describe foreground object extraction
- train first neural network for future frame prediction
- introduce future frame prediction module
- describe generator and discriminator components
- explain reconstruction loss and discriminative loss
- describe encoder, memory module, and decoder components
- associate future frame prediction module with object-aware anomaly synthesis module
- generate pseudo abnormal frames
- train second neural network for normalcy classification
- introduce normalcy classifier module
- generate plurality of loss functions
- describe normalcy loss, relative normalcy loss, attention affirmation loss, and relative attention affirmation loss
- utilize predicted frames and pseudo abnormal frames for normalcy classification
- train second neural network with predicted normal and pseudo abnormal video frames
- perform video anomaly detection
- illustrate example of video anomaly detection
- describe use case for detecting anomaly

