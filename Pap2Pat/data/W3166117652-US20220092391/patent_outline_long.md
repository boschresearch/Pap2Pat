# DESCRIPTION

## TECHNICAL FIELD

- relate to DNNs

## BACKGROUND

- introduce DNNs

## DETAILED DESCRIPTION

### Overview

- introduce model quantization
- describe latency, energy, and model size constraints
- motivate mixed-precision quantization
- explain equal bit-width precisions
- describe mixed-precision quantization benefits
- illustrate precision effects using π example
- describe neural network architecture
- explain 32-bit floating-point precision
- describe lower precision values
- motivate finding effective mixed-precision quantization configurations
- describe classical multi-objective search
- introduce graph-based embedding for DNN workloads
- describe GNNs and their application
- introduce NEMO search framework
- describe population generation
- explain species and members
- describe GNN species and internal parameters
- explain NEMO search process
- describe training GNN
- explain utility metrics computation
- describe Pareto optimal set identification
- explain NEMO search process termination

### Example DNN Architecture

- introduce example DNN architecture
- describe VGG-based CNN
- explain input image and objects
- describe convolutional layers
- explain feature extraction
- describe weight matrices and filters
- explain convolution operation
- describe output feature map
- explain pooling layers
- describe downsampling feature maps
- explain average pooling and max pooling
- describe fully connected layers
- explain input vector and output vector
- describe linear combination and activation function
- explain output vector and probabilities
- describe logistic function and softmax function
- explain classification of input image

### Example DL Environment

- introduce DL environment
- describe DL server components
- explain neural network structure
- describe neural network types
- explain neural network training process
- describe DL model applications
- introduce DNN system
- describe database functionality
- explain distributer functionality
- describe client device functionality
- explain client device types
- describe client device interactions
- explain network functionality
- describe network protocols
- explain data representation
- describe encryption methods
- summarize DL environment components

### Example DNN System

- introduce DNN system
- describe interface module functionality
- explain training module functionality
- describe training dataset formation
- explain hyperparameter determination
- describe DNN architecture definition
- explain input layer functionality
- describe output layer functionality
- explain hidden layer functionality
- describe convolutional layer functionality
- explain pooling layer functionality
- describe fully connected layer functionality
- explain training process
- describe cost function usage
- explain compression module functionality
- describe sequential graph generation
- explain GNN functionality
- describe pruning ratio determination
- explain mixed-precision quantization
- describe bit-width determination
- explain quantization process
- describe compressed DNN generation
- explain fine-tuning process
- describe validation module functionality
- explain accuracy score determination
- describe threshold score comparison
- explain application module functionality
- describe memory functionality

### Example Compression Module

- introduce compression module 330
- describe graph generation module 410
- generate sequential graphs of trained DNNs
- identify hidden layers and activations in a trained DNN
- generate graph representation of quantizable operation
- generate nodes representing activation functions
- describe features of a node
- build edges by connecting nodes sequentially
- describe quantization module 420
- quantize weights and activations using GNN 430
- receive sequential graphs from graph generation module 410
- provide sequential graphs to GNN 430
- receive outputs of GNN 430
- quantize weights and activations based on outputs of GNN 430
- describe NEMO module 440
- train GNN 430 using NEMO search framework
- generate population of NEMO search framework
- perform NEMO search process on population

### Example Sequential Graph

- introduce sequential graph 550
- describe nodes in sequential graph 550
- describe features of a node
- connect nodes sequentially

### Example Offspring Production

- introduce offspring production in NEMO search process
- perform mutation and crossover operations on GNNs
- double size of each species

### Example Pareto Frontier

- introduce Pareto frontier 705
- describe criterion space 700
- form Pareto frontier 705 based on population 615
- identify optimal solutions on Pareto frontier 705
- determine utility number for each species

### Example Formation of Next Generation Pareto Frontier

- illustrate formation of new generation
- describe Pareto frontier
- select members of next generation
- downsize species
- form new generation
- describe offspring production process
- describe Pareto frontier formation process
- illustrate process of using GNN for mixed-precision quantization
- describe DNN
- generate sequential graph
- input sequential graph into GNN
- output bit-width probability distributions
- describe probability of optimizing multiple objectives
- select bit-width
- illustrate method of optimizing multiple objectives
- generate plurality of GNNs
- describe GNNs in first species
- describe GNNs in second species
- generate plurality of new GNNs
- form new GNNs based on internal parameters
- generate sequential graph for DNN
- input sequential graph into GNNs
- evaluate outputs of GNNs
- generate Pareto optimal set
- form criterion space
- identify GNNs with best performance
- form Pareto optimal set
- select GNN
- describe computing system
- illustrate components of computing system
- describe processing device
- describe memory

## SELECT EXAMPLES

- provide various examples of embodiments
- introduce method for optimizing multiple objectives
- generate graph neural networks (GNNs)
- generate new GNNs based on plurality of GNNs
- generate sequential graph for first DNN
- input sequential graph into GNNs and new GNNs
- evaluate outputs of GNNs and new GNNs
- select GNN based on evaluation
- specify first species of GNNs
- specify second species of GNNs
- generate new internal parameters
- form new GNNs based on new internal parameters
- generate Pareto optimal set
- configure GNN to receive sequential graph
- output bit-width probability distribution
- select bit-width from probability distribution
- specify quantizable operation as convolution
- specify quantizable operation as activation function
- specify multiple objectives
- provide non-transitory computer-readable media
- provide apparatus for optimizing multiple objectives

