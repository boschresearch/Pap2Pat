# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- introduce nlp models
- limitations of fine tuning
- introduce few-shot learning

## DETAILED DESCRIPTION

- overview of patent application

### Overview

- illustrate system-on-a-chip (SoC) architecture
- describe components of SoC
- explain memory storage and processing
- introduce machine learning (ML) and artificial intelligence (AI)
- define neural networks and their applications
- explain individual nodes in a neural network
- describe weight values and their role
- introduce different types of neural networks
- describe convolutional neural networks (CNNs)
- describe recurrent neural networks (RNNs)
- describe generative adversarial networks (GANs)
- describe multilayer perceptron (MLP) neural networks
- introduce deep learning (DL) and its relation to ML
- describe layers in a deep neural network
- explain hidden layers and their role
- describe output of a deep neural network
- illustrate fully connected neural network
- illustrate locally connected neural network
- describe few-shot learning (FSL) scenario
- introduce prototypical machine learning network
- describe attention mechanism in FSL
- explain query-by-example process
- describe N-way M-shot episode
- illustrate 3-way 5-shot FSL scenario
- describe prototypical network for FSL
- explain embedding space in prototypical network
- describe determining prototype representation
- explain classification using prototypical network
- describe distance metrics for classification
- provide example of classification using prototypical network
- conclude overview of patent application

### Example Embodiments

- introduce prototypical machine learning networks
- describe variance-aware prototypical network
- motivate few-shot text classification
- describe limitations of pre-trained language models
- introduce meta-learning for few-shot learning
- describe challenges of meta-training for NLP tasks
- introduce three common approaches to meta-learning
- describe model agnostic meta-learning (MAML)
- describe prototypical networks
- motivate need for systems and techniques
- introduce novel loss function for prototypical networks
- describe regularization term for tight clustering
- describe meta-training on large labeled dataset
- describe deployment on diverse downstream tasks
- describe superior performance on public benchmarks
- describe simplicity of training and deployment
- describe use of dataset statistics for out-of-distribution cases
- describe variance-aware prototypical network using Wasserstein distance
- describe additional regularization term for covariance matrices
- describe use of Gaussians for conditional distributions
- introduce example datasets for training
- describe MRI radiology reports dataset
- describe label space for shoulder dataset
- describe split of dataset labels across training and validation subsets
- describe meta-learning for different downstream classification tasks
- describe four downstream medical anatomy/pathology classification tasks
- describe each task as a downstream classification task
- conclude example embodiments

### Example Workflow

- introduce machine learning architecture and workflow
- receive radiology reports as input
- de-identify input radiology report according to HIPAA regulations
- split report into sentences using report segmentation engine
- generate report segments
- implement body part-specific workflow
- use body-part specific custom data processor
- obtain relevant text from body-part specific radiology report
- predict pathology severity
- use rule-based regex to extract 'Impression' section
- extract text of 'Impression' section
- use extracted text for final classification task
- implement cervical spine-specific segmentation engine
- associate with downstream task of predicting severity of neural foraminal stenosis
- break information down at motion segment level
- correlate pathological findings with clinical exam findings
- inform future treatment interventions
- use BERT-based NER model to identify motion segments
- concatenate sentences referring to same motion segment
- include concatenated text in output features
- provide output features to variance-aware prototypical network-based classification engine
- predict pathology severities
- use knee-specific segmentation engine
- use BERT-based NER model to tag sentences mentioning structure of importance
- group sentences mentioning structure of importance
- predict pathologies of importance
- implement classification engine for predicting anatomical pathology severity
- use variance-aware prototypical networks
- predict labels for anatomical pathology severity

### Variance-Aware ProtoNets

- model conditional distribution as Gaussian
- treat query example as Dirac distribution
- compute Wasserstein distance between Gaussian and query vector
- simplify prototypical network conditional distribution
- reduce space complexity to store covariance matrix
- train variance-aware prototypical networks
- regularize negative log likelihood loss

### Experimental Results

- run experiments on V100 16 GB GPU using PyTorch and HuggingFace libraries
- use BERT-base, Clinical BERT, and PubMed-BERT as backbone models
- apply adapters to each backbone model
- freeze BERT weights and update adapter weights
- compare and analyze against various benchmarks and baselines
- select best model based on meta-validation accuracy
- apply best model to downstream classification tasks
- validate variance-aware prototypical networks on 13 public benchmark datasets

## Deployment

- deploy regularized variance-aware ProtoNet with Adapter-PubMedBERT
- describe pipeline components
- explain inference process
- detail pipeline metadata and output

## Monitoring

- describe BERT embeddings anisotropy
- introduce Average Variance Indices (AVI) for OOD detection
- explain AVI calculation and thresholding

## CONCLUSION

- summarize Wasserstein distance-based Prototypical Networks
- describe regularization term for class prototype clustering
- highlight successful downstream performance on various labels
- emphasize single model deployment for inference cost savings
- describe adapter usage for parameter tuning
- highlight training cost savings
- summarize extensive experiments on 13 public datasets
- describe outperformance of strong baselines
- introduce Average Variance Indices (AVI) for OOD detection
- describe leveraging dataset statistics for OOD detection
- illustrate example computing device architecture
- describe processing unit and computing device connection
- detail computing device memory and storage
- explain cache usage for performance boost
- describe processor and service configuration
- highlight multi-core processor capabilities
- describe input and output devices
- explain communication interface and user interaction
- detail storage device and services
- describe hardware and software modules
- clarify device and system terminology
- explain functional blocks and components
- describe process and method representation
- highlight computer-executable instructions and data
- explain computer-readable medium and storage
- describe non-transitory medium and signal exclusion
- highlight code segment and hardware circuit coupling
- explain device implementation and form factors
- describe peripherals and add-in cards
- highlight instructions and media for conveying instructions
- explain computing resources and supporting structures
- describe means for providing functions
- highlight variations and embodiments
- explain less than and greater than symbols
- describe component configuration and coupling
- explain claim language and set satisfaction
- highlight electronic hardware, software, and firmware implementation

