# DESCRIPTION

## FIELD

- relate to photovoltaic array operation

## BACKGROUND

- describe limitations of power production from PV systems

## DETAILED DESCRIPTION

- motivate reconfiguring PV array connections
- describe conventional approaches to mitigate shading
- introduce system for deep neural network-based topology reconfiguration
- describe key contributions of the system
- outline system architecture and components
- describe system operation and functionality

### Approach

- motivate need for automated methods for topology reconfiguration
- describe limitations of conventional approaches
- outline system for reconfiguring PV array to maximize power output
- describe system components and architecture
- describe system operation and functionality
- highlight scalability and deployability of the system
- describe importance of not requiring additional panels for reconfiguration
- describe system's ability to handle static reconfiguration scenarios

### Neural Network Model

- introduce neural network model
- describe neural network model architecture
- describe input to neural network model
- describe hidden layers of neural network model
- describe output layer of neural network model
- describe softmax activation function
- describe regularization techniques used
- describe dropout policy
- describe batchnorm
- describe training framework
- describe simulation module
- describe training module
- describe synthetic data generation
- describe binary mapping scheme
- describe irradiance distributions
- describe dataset construction
- describe supervised classification problem
- describe label assignment
- describe simulation setup
- describe PV array simulation model
- describe wiring losses modeling
- describe re-configurable links
- describe string connections
- describe resistance values used
- describe activation and deactivation of simulated linkages
- describe topology configurations
- describe wire loss modeling
- describe adaptability of the system
- describe design of regularized neural network
- describe neural network architecture
- describe training and optimization of neural network model

### Results and Discussion

- describe system performance
- describe confusion matrix
- describe merit of PV topology reconfiguration
- describe power improvement results

## Computing Device

- introduce device 500
- describe network interfaces 510
- describe processor 520
- describe memory 540
- describe power supply 560
- describe photovoltaic topology reconfiguration processes/services 590
- discuss alternative embodiments

## Methods

- introduce method 600 for photovoltaic topology reconfiguration
- receive operating data as input to neural network model
- generate prediction probability of topology configuration
- provide neural network model and train
- receive operating data at first input layer
- receive output of previous layer at hidden layer
- apply affine transformation and non-linear activation function
- apply dropout policy
- apply batchnorm operation
- receive output of final hidden layer at output layer
- apply softmax activation function
- generate prediction probabilities for each topology configuration
- determine topology selection
- communicate topology selection to photovoltaic array
- configure linkages of photovoltaic array
- introduce method 700 for generating labeled synthetic irradiance data
- generate synthetic irradiance data
- apply synthetic irradiance data to PV array simulation model
- identify simulated topology configuration with maximum power output
- assign label to synthetic irradiance data
- introduce method 800 for training neural network

