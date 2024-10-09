# DESCRIPTION

## RELATED APPLICATION INFORMATION

- claim priority

## BACKGROUND

### Technical Field

- define technical field

### Description of the Related Art

- motivate self-supervised learning
- limitations of current methods

## SUMMARY

- introduce model training method
- train model with self-supervised contrastive loss
- update model with cascade k-nearest neighbor mining
- fine-tune model for downstream task
- deploy model for target application
- introduce computer program product
- describe program instructions
- introduce computer processing system

## DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS

- introduce self-supervised multimodal representation learning
- motivate cascade positive example mining
- describe limitations of previous works
- propose cascade K-Nearest Neighbor Mining
- propose Progressive Training
- summarize self-supervised representation learning technique
- describe computing device 100
- introduce processor 110
- introduce input/output subsystem 120
- introduce memory 130
- introduce data storage device 140
- introduce communication subsystem 150
- introduce peripheral devices 160
- describe hardware processor subsystem
- describe video classification application
- introduce video classification system 200
- describe model inference 220
- describe feature extraction 220A
- describe feature classification 220B
- introduce self-supervised contrastive learning 300
- describe 3D convolutional layers 330
- describe memory banks 350
- describe video feature extraction 340
- describe similarity score computation
- describe cascade k-nearest neighbor mining 500
- describe progressive training regime 700
- describe contrastive learning 800
- describe instance-level discrimination
- describe action-level discrimination
- describe learning from multiple modalities
- describe method 900 for self-supervised multimodal representation learning
- describe model training with self-supervised contrastive loss
- introduce progressive training in phases
- inherit model weights from previous training phase
- describe block 910A: pull together positive feature pairs
- describe block 910B: repel apart negative feature pairs
- describe block 920: update trained model with self-supervised contrastive loss
- describe Cascade K-Nearest Neighbor mining
- describe block 930: fine-tuning trained model for downstream task
- describe block 930A: use downstream task labels to fine-tune model
- describe block 940: deploy trained model for target application inference
- describe block 940A: transform input video to output textual label
- discuss concept of contrastive learning
- discuss instance discrimination
- introduce InfoNCE loss
- discuss limitations of InfoNCE loss
- introduce Multi-Instance InfoNCE loss
- discuss CoCLR approach
- discuss limitations of CoCLR approach
- introduce Cascade Mining approach
- describe overview of Cascade Mining
- describe training RGB and Flow models with InfoNCE loss
- describe using RGB model as oracle to mine positive examples
- describe using Flow model as oracle to improve RGB model
- describe maintaining RGB and Flow memory queues
- describe calculating similarity between query and key features
- describe selecting potential positive examples
- discuss computer program product
- describe computer readable storage medium
- describe downloading computer readable program instructions
- describe executing computer readable program instructions
- discuss flowchart and block diagram illustrations
- describe implementing functions/acts specified in flowchart and/or block diagram
- discuss one embodiment of the present invention
- discuss scope of the invention

