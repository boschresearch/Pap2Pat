# DESCRIPTION

## BACKGROUND

- introduce neural networks
- describe DNNs and their applications
- discuss limitations of DNNs with rules

## BRIEF SUMMARY

- introduce DNN-CRR system
- describe joint learning from data and rules
- explain controllable rule representations
- discuss model-agnostic, task-agnostic, and rule-agnostic system
- describe system for training machine learning model
- explain receiving input data and control parameter value
- discuss generating output data using input data, control parameter value, and rules
- describe technical advantages of system
- discuss reducing computational costs
- describe method for training machine learning model
- explain receiving input data and control parameter value
- discuss generating output data using input data, control parameter value, and rules
- describe non-transitory computer-readable storage media
- discuss optional features of system
- explain processing input data with different control parameter values
- describe updating model parameter values
- discuss training machine learning model with rule encoder, data encoder, and decision block

## DETAILED DESCRIPTION

### Overview

- introduce DNN-CRR system
- define rule encoder
- define task encoder
- explain latent representation
- describe rule latent representation
- describe data latent representation
- explain control parameter value
- define rules
- provide examples of rules
- explain rule strength
- define rule verification ratio
- explain adjusting rule strength
- describe training process
- explain model parameter updates
- describe generating different latent representations
- explain technical advantages
- describe controllable rule representations
- explain searching for control parameter values
- describe efficient use of computing resources
- explain strict adherence to rules
- describe flexibility of DNN-CRR system
- explain model-, rule-, and data-agnostic nature
- describe versatility of DNN-CRR system

### Example Systems

- introduce DNN-CRR system
- describe data processing flow
- introduce physical system
- describe training data
- describe DNN training
- illustrate energy levels of predicted states
- describe adjustment of rule strength
- introduce block diagram of DNN-CRR system
- describe rule encoder
- describe data encoder
- describe decision block
- describe two-passage approach for training data
- describe implementation on processors and memory devices
- describe implementation in medical diagnosis
- describe example rule for medical diagnosis
- describe adjustment of rule strength in medical diagnosis
- describe implementation in material simulation
- describe implementation in financial analysis
- describe example rule for financial analysis
- describe adjustment of rule strength in financial analysis
- describe implementation in computer network monitoring
- describe example rule for computer network monitoring
- describe adjustment of rule strength in computer network monitoring
- describe training data for DNN
- describe compound objective function
- describe task-based objective
- describe rule-based objective
- describe first passage of data
- describe second passage of data
- describe concatenation of latent representations
- describe decision block
- describe model architectures
- describe optimization methods
- describe training process
- describe convergence criteria
- describe advantages of DNN-CRR system
- describe example training process
- define DNN-CRR system
- introduce control parameter value
- describe probability distribution
- motivate beta distribution
- describe concatenated latent representation
- compute compound objective
- update model parameter values
- describe automatic scaling
- compute scale parameter value
- update model parameter values
- describe flow diagram for training
- receive input training data
- generate data latent representation
- generate rule latent representation
- concatenate latent representations
- generate output data
- update model parameter values
- describe process for processing input
- receive control parameter value and input data
- process input data
- describe incorporating rules using input perturbation
- describe perturbation-based objective function
- describe flow diagram for training with perturbation

### Hypothesis Testing and Control Parameter Searching Using DNN-CRR

- introduce trade-off between rule strength and network accuracy
- describe DNN-CRR system receiving data and control parameter value
- specify received data components
- define rule verification ratio threshold and maximum error rate threshold
- describe searching for target control parameter value
- sample control parameter values from range [0,1]
- generate network outputs on validation set
- compare error rate and rule verification ratio
- iteratively adjust control parameter value
- stop search upon meeting termination criteria
- process input data using target control parameter value
- repeat process for different datasets or distribution shifts
- generate statistics for network quality and rule adherence
- provide insight for hypothesized rules
- verify or reject hypothesized rules
- illustrate experimental results for DNN-CRR system
- compare DNN-CRR system with other models
- show mean absolute error for various models
- compare rule verification ratios for various models
- illustrate average model errors for DNN-CRR system
- show average error for different rules
- apply input perturbation to train models
- illustrate average model error on unseen test data sets
- adapt DNN-CRR system for different datasets
- illustrate cross-entropy loss on different input datasets
- adapt DNN-CRR system to distribution shifts
- train models with fixed control parameter values
- show cross-entropy losses for different models
- illustrate trade-off between rule strength and cross-entropy loss
- compare network accuracy versus rule strength

### Example Computing Environment

- illustrate DNN-CRR system
- describe computing device architecture
- define processor components
- explain memory storage
- describe data retrieval and modification
- discuss data structure and format
- introduce processor types
- describe specialized hardware components
- explain parallel processing
- discuss distributed system architecture
- describe network communication
- illustrate network topology
- explain short- and long-range connections
- discuss communication standards
- describe web server functionality
- explain client-server architecture
- describe client computing device components
- explain user input and output devices
- define "configured to" phrase
- discuss operation ordering and integration

