# DESCRIPTION

## TECHNICAL FIELD

- relate to video anomaly detection

## BACKGROUND

- introduce unsupervised video anomaly detection
- limitations of cross-domain video anomaly detection
- motivate zero-shot cross domain video anomaly detection
- identify need for improved xVAD systems

## SUMMARY

- introduce zero-shot cross-domain video anomaly detection system
- collect video from source domain
- obtain images of foreground objects
- train first neural network for frame prediction
- train second neural network for anomaly classification
- utilize normalcy classifier module
- perform video anomaly detection

## DETAILED DESCRIPTION

- set context for description
- define terminology and phrasing
- clarify representation of systems
- establish level of detail

### System Overview

- introduce training system
- describe system components
- explain memory storage
- detail processor functionality
- introduce source domain data
- describe normal events in source domain
- explain foreground object extraction
- detail training of first neural network
- introduce future frame prediction module
- describe generator and discriminator components
- explain reconstruction loss and discriminative loss
- detail training of second neural network
- introduce normalcy classifier module
- describe object-aware anomaly synthesis module
- explain pseudo abnormal frame generation
- detail normalcy loss function
- explain relative normalcy loss function
- introduce attention affirmation loss function
- detail relative attention affirmation loss function
- explain joint training of neural networks
- describe video anomaly detection process
- introduce FIG. 2A
- describe future frame prediction module
- detail generator architecture
- explain memory module functionality
- describe decoder architecture
- introduce FIG. 2B
- describe normalcy classifier module
- detail object-aware anomaly synthesis module
- explain randomly initialized CNN
- describe object-aware cut mix operation
- introduce FIG. 2C
- describe normalcy classifier architecture
- detail normalcy loss function
- explain relative normalcy loss function
- introduce attention affirmation loss function
- detail relative attention affirmation loss function
- explain attention map extraction
- describe attention affirmation loss function
- introduce FIG. 3
- describe pseudo abnormal frame representation
- detail object localization process
- explain ground truth mask generation
- introduce FIG. 4
- describe training system workflow
- detail future frame prediction process
- explain normalcy classification process
- describe video anomaly detection output

