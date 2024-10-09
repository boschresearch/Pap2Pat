# DESCRIPTION

## FIELD

- relate to photovoltaic array operation

## BACKGROUND

- motivate partial shading in PV systems

## DETAILED DESCRIPTION

- describe PV array connections
- motivate reconfiguring PV arrays
- introduce system for deep neural network-based topology reconfiguration

### Approach

- motivate need for automated methods
- outline system for topology reconfiguration
- describe system components
- highlight scalability of system

### Neural Network Model

- introduce neural network model
- describe input to neural network model
- describe hidden layers of neural network model
- introduce dropout and batchnorm
- describe output layer of neural network model
- describe training framework
- generate synthetic irradiance data
- simulate power generation for different topologies
- determine topology that produces maximum power
- describe simulation setup
- model wiring losses
- describe design of regularized neural network
- describe input layer
- describe hidden layers
- describe output layer

### Results and Discussion

- discuss system performance
- assess merit of PV topology reconfiguration

## Computing Device

- describe device architecture
- detail network interfaces
- outline processor and memory components

## Methods

- introduce photovoltaic topology reconfiguration method
- receive operating data for neural network model
- generate prediction probability for topology configuration
- apply affine transformation and non-linear activation function
- apply dropout policy and batchnorm operation
- generate prediction probabilities for each topology configuration
- determine topology selection based on prediction probabilities
- communicate topology selection to photovoltaic array
- configure linkages of photovoltaic array
- generate labeled synthetic irradiance data for training

