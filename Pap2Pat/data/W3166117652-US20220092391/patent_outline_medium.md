# DESCRIPTION

## TECHNICAL FIELD

- relate to DNNs

## BACKGROUND

- introduce DNNs

## DETAILED DESCRIPTION

### Overview

- introduce model quantization
- motivate mixed-precision quantization
- describe limitations of equal bit-width precisions
- explain mixed-precision quantization
- illustrate effects of different precisions
- describe challenges of finding effective mixed-precision quantization configurations
- introduce classical multi-objective search
- motivate improved technologies for mixed-precision quantization
- introduce embodiments of the present invention
- describe layer-wise mixed-precision quantization of DNNs
- introduce NEMO search framework

### Example DNN Architecture

- introduce example DNN architecture
- describe convolutional layers
- explain convolution operation
- describe pooling layers
- explain pooling operation
- describe fully connected layers
- explain output vector generation
- illustrate example output vector

### Example DL Environment

- introduce DL environment
- describe DL server components
- explain neural network structure
- describe DL model training process
- explain distributer functionality
- describe client device functionality
- explain network communication
- describe client device types

### Example DNN System

- introduce DNN system
- describe interface module functionality
- explain training module functionality
- describe training dataset formation
- explain hyperparameter determination
- describe DNN architecture definition
- explain training process
- describe compression module functionality
- explain compression process
- describe validation module functionality
- explain validation process
- describe application module functionality
- explain memory storage
- describe memory functionality

### Example Compression Module

- introduce compression module 330
- describe graph generation module 410
- explain sequential graph generation
- describe quantization module 420
- explain GNN 430
- describe NEMO module 440
- explain population generation
- describe NEMO search process
- explain multi-objective optimization

### Example Sequential Graph

- introduce sequential graph 550
- describe node features

### Example Offspring Production

- describe offspring production in NEMO search process

### Example Pareto Frontier

- introduce Pareto frontier 705
- explain Pareto optimal set

### Example Formation of Next Generation Pareto Frontier

- illustrate formation of new generation
- select members of Pareto frontier
- downsize species
- form new generation
- go through offspring production process
- form Pareto frontier
- illustrate mixed-precision quantization
- train GNN
- generate sequential graph
- input sequential graph into GNN
- output bit-width probability distributions
- select bit-width
- illustrate method of compressing DNN
- generate GNNs
- evaluate outputs of GNNs
- select GNN

## SELECT EXAMPLES

- provide various examples of embodiments
- describe method for optimizing multiple objectives
- generate graph neural networks (GNNs)
- generate new GNNs based on existing GNNs
- generate sequential graph for DNN
- input sequential graph into GNNs
- evaluate outputs of GNNs based on conflicting objectives
- select GNN for reducing precisions of quantizable parameters
- provide variations of method with different GNN architectures
- describe apparatus and computer-readable media for optimizing multiple objectives

