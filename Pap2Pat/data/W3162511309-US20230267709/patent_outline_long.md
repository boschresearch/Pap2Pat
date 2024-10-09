# DESCRIPTION

## TECHNICAL FIELD

- introduce face recognition

## BACKGROUND

- define face recognition
- describe applications
- limitations of facial recognition
- motivate dataset-aware learning

## DETAILED DESCRIPTION

- introduce facial recognition system
- describe conventional models
- discuss loss functions in conventional models
- discuss architecture of conventional models
- discuss importance of training data
- discuss challenges of dataset fusion
- illustrate overlapping identity issue
- introduce label cleaning process
- discuss limitations of label cleaning
- introduce dataset-aware loss approach
- discuss advantages of dataset-aware loss
- discuss domain adaptation for multi-dataset training
- introduce gradient reversal layers for domain adaptation
- illustrate framework of dataset-aware approach
- describe embedding network, classification network, and dataset classifier network
- discuss backpropagation algorithm
- discuss supervised learning with class label and dataset index

### Terminology

- define "an embodiment" and "some embodiments"
- define "comprise", "comprising", and "comprised of"
- define "based on"
- define "connected", "coupled", and variants

### Related Work in Machine Learning

- introduce loss functions
- discuss classification losses
- discuss contrastive losses
- discuss combining classification and contrastive losses
- introduce data processing
- discuss label cleaning
- discuss noise-resistant learning
- introduce domain adaptation
- discuss transfer learning
- discuss domain-specific architectures
- discuss direct image transformation
- discuss latent space adaptation

### Overview of Dataset-Aware Approach to Training

- introduce dataset-aware loss
- discuss overlapping identity issue
- discuss conventional approaches to addressing overlapping identity issue
- introduce dataset-aware loss approach
- discuss advantages of dataset-aware loss
- illustrate framework of dataset-aware approach
- describe embedding network, classification network, and dataset classifier network
- discuss backpropagation algorithm
- discuss supervised learning with class label and dataset index
- define dataset-aware loss
- discuss softmax loss
- define dataset indicator
- discuss dataset-aware loss with softmax loss
- discuss combining dataset-aware loss with variations of softmax-based losses
- discuss dataset-invariant learning by domain adaptation
- introduce domain adaptation with gradient reversal layers
- discuss optimization of network parameters
- discuss two-stage optimization approach

### Experiments and Results

- introduce experiment settings
- describe datasets used
- define embedding subnetworks
- set embedding dimensions
- set parameter A from Eq. 7
- set batch sizes
- adopt pre-trained model
- set initial learning rate
- decay learning rate
- set maximum steps for training
- compare to conventional methods
- show results in Table I of FIG. 5
- analyze results
- conduct ablation study
- evaluate baseline method
- show results in Table III of FIG. 5
- analyze ablation study results
- conclude effectiveness of dataset-aware loss

### Overview of Training Platform

- introduce training platform
- describe modules of training platform
- explain interfaces of training platform
- describe dataset management
- explain network environment
- describe connections to networks
- explain accessibility of interfaces
- describe hosting of training platform
- conclude overview of training platform

### Methodologies for Training a Model in a Dataset-Aware Manner

- obtain datasets
- compute embeddings
- determine loss metrics
- describe neural network architecture
- explain embedding network
- explain classification network
- explain dataset classifier network
- optimize network parameters
- store loss metrics
- form training set
- generate feature vectors
- determine loss within datasets
- propagate losses to model
- train model
- store trained model
- describe dataset-aware training
- address overlapping identities
- generate feature vectors
- determine loss within datasets
- propagate losses to model
- conclude dataset-aware training

### Processing System

- illustrate processing system 900
- describe components of processing system 900
- detail bus 916 architecture
- compare processing system 900 to other electronic devices
- define machine-readable medium and storage medium
- explain execution of computer programs
- discuss distribution of program products
- list examples of machine- and computer-readable media
- describe network adapter 912 functionality
- detail firewall capabilities

## REMARKS

- disclaim limitation
- emphasize scope flexibility
- clarify terminology usage
- emphasize claim-based scope

