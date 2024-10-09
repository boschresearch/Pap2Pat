# DESCRIPTION

## FIELD OF THE DISCLOSURE

- introduce neuromorphic systems

## BACKGROUND

- motivate tinyML systems
- describe energy efficiency of neuromorphic systems
- discuss limitations of traditional ML approaches
- introduce spike-based learning and training
- describe backpropagation for training spiking neural networks
- discuss transfer techniques for mapping deep neural nets
- introduce local learning rules for spiking neural networks
- describe supervised synaptic learning rules
- discuss limitations of backpropagation
- introduce feedback alignment and random backpropagation
- describe equilibrium propagation
- introduce predictive coding frameworks
- discuss shortcomings of prior art solutions
- motivate need for backpropagation-less learning
- motivate need for sparsity in network spiking activity

## BRIEF SUMMARY

- introduce learning framework for neuromorphic systems
- describe use of spiking growth transform neurons
- discuss design of neuromorphic tinyML systems
- introduce backpropagation-less learning approach
- highlight features of learning framework

## DETAILED DESCRIPTION OF THE DRAWINGS

- describe Growth Transform computing system
- introduce GT network systems
- describe user computing devices and client device

### Exemplary Computer System

- introduce Growth Transform computing device
- describe database server
- discuss user computing devices
- introduce client device
- describe GT network systems
- discuss tinyML systems
- introduce machine learning processes
- describe user computing devices and GT systems
- discuss database server and database
- describe rules engine computing device

### Exemplary Client Computing Device

- introduce client computing device
- describe processor and memory area
- discuss modules for implementing systems and methods
- introduce media output component
- describe input device
- discuss communication interface
- describe stored instructions
- introduce user interface
- discuss memory area

### Exemplary Server Computing System

- introduce server system
- describe processor and memory area
- discuss communication interface
- introduce storage device
- describe storage interface
- discuss memory area

## Growth Transform Neural Networks

- introduce energy-efficient neuromorphic machine learning
- equalize training and sparsity losses
- provide framework for designing neuromorphic tinyML systems
- build upon spiking neuron and population model
- incorporate learning and synaptic adaptation
- exploit inherent dynamics for optimal network configuration
- implement energy-based learning using neural variables
- describe GTNN architecture and applications

## Learning Framework

- illustrate circuit model for single neuron
- define instantaneous power
- introduce biophysical constraints
- formulate optimization problem
- derive first-order condition
- extend to time-varying input
- define barrier function
- rewrite optimization problem
- describe GT neuron model
- illustrate oscillatory dynamics
- describe modulation function
- derive ReLU encoding
- illustrate plot for different values of Q
- describe quantization effects
- illustrate error introduced by approximation
- describe response of single GT neuron
- introduce ON-OFF GT neuron model
- describe optimization problem for ON-OFF neuron
- derive first-order conditions
- describe properties of ON-OFF variables
- illustrate orthogonal property
- describe sparsity-driven learning framework
- generalize differential stimuli
- derive first-order conditions for i-th ON-OFF neuron pair
- describe linear constraint
- formulate L1 optimization
- describe gradient descent approach
- derive spike-based local update rule
- illustrate sparsest solution
- describe linear projection using sparse GT network
- formulate modified L1 optimization
- derive synaptic update rule
- describe inference using network sparsity

### Application of Learning Framework Machine Learning

- introduce application of learning framework
- describe weight adaptation and sparsity
- illustrate sparsity-driven weight adaptation using FIGS. 7A and 7B
- show weight adaptation results in FIGS. 4C and 4D
- describe unsupervised learning using template projection
- formulate template projection problem
- minimize network-level spiking activity
- describe domain description problem
- train GT network to evolve towards data points
- show equivalence between firing rate minimization and loss minimization
- illustrate example with single data point in FIG. 8A
- plot loss function in FIG. 8B
- plot L1 norm of mean membrane potentials in FIG. 8C
- plot L1 loss in FIG. 8D
- describe anomaly detection
- train GT network with unlabeled training set
- determine mean firing rates for each data point
- set maximum mean firing rate as threshold
- classify data points as members or outliers
- describe supervised learning
- design network to solve linear classification problems
- describe linear feed-forward network
- describe linear recurrent network
- compare properties of two architectures
- verify linear classification framework with feed-forward architecture
- introduce learning framework machine learning
- describe network architecture
- motivate random projection-based classification
- derive transformation matrix
- compute L1 distance
- describe centroid computation
- illustrate XOR dataset classification
- plot training data points and classification boundary
- describe layer-wise training
- derive equation for layer 1
- describe fully-connected network in layer 2
- illustrate XOR dataset classification
- plot evolution of sparsity metric
- describe target information in layer-wise training
- illustrate network architecture
- describe training process
- illustrate XOR dataset classification
- plot evolution of training accuracy and sparsity metric
- describe incremental few-shot learning
- describe machine olfaction dataset
- describe network testing
- plot evolution of training accuracy and sparsity metric
- compare with standard backpropagation
- describe performance comparison
- plot batch-wise test accuracies
- plot sparsity metrics on test data
- describe reduced shot learning
- plot test accuracy and sparsity metrics
- describe inherent regularizing effect
- describe parallels with biological neural networks
- illustrate population activity evolution
- plot PCA trajectories
- describe stimulus representation
- describe implications for neuromorphic hardware
- describe energy efficiency
- describe flexibility and functional diversity
- illustrate GTNN diagram
- describe short-term and long-term dynamics
- illustrate GT neuron diagram
- describe local energy balance and ON-OFF dynamics
- plot performance on short and long time scales
- describe experimental test data results
- illustrate flow diagram of GTNN architecture
- describe spike-response model building
- describe GT neural network design
- describe network optimization
- describe relation with balanced spiking networks
- describe network design and learning framework

## Machine Learning & Other Matters

- introduce computer-implemented methods
- discuss machine learning programs
- motivate supervised machine learning
- motivate unsupervised machine learning
- discuss machine learning applications

### Additional Considerations

- discuss computer programming techniques
- define computer-readable media
- discuss computer programs
- define machine-readable medium
- define processor
- discuss software and firmware
- discuss system embodiments
- discuss system environments
- discuss system flexibility
- discuss system components
- discuss system functionality
- discuss patent claims and scope

