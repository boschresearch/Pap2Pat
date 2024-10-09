# DESCRIPTION

## BACKGROUND

- introduce neural networks
- motivate reliability problem
- describe conventional improvement methods
- highlight major disadvantage
- describe ensemble methods
- describe adversarial training
- summarize other methods

## SUMMARY

- introduce compact support neuron
- describe training method
- outline implementation embodiments

## DETAILED DESCRIPTION

- introduce compact support neural networks
- describe advantages over standard neural networks
- motivate use of compact support neurons
- define compact support neuron
- describe radial basis function neuron
- introduce shape parameter α
- describe flexible representation of neuron
- obtain standard ReLU based neuron for α=0
- describe compact support neuron with α>0
- illustrate support for several values of α
- describe convolutional version of compact support neuron
- generate compact support neural network
- describe CSNN with hidden layer and output layer
- illustrate example CSNN
- train CSNN
- describe difficulties in training CSNN
- describe approach to training CSNN
- train regular neural network first
- gradually increase shape parameter α
- describe algorithm for training CSNN
- stop training at α<1 with acceptable errors
- describe advantages of CSNN
- provide normalization
- standardize variables to have zero mean and standard deviation 1
- illustrate histogram of norms of normalized input features
- prune dead neurons
- remove dead neurons during training
- describe generic neuron formulation
- encompass standard projection-based neuron and RBF neuron
- use ReLU as activation function
- obtain compact support neuron
- train CSNN by gradually shrinking support
- describe advantages of CSNN in safety critical applications
- illustrate exemplary computing environment
- describe computing device environment
- illustrate system for implementing aspects
- describe processing unit and memory
- describe additional storage
- describe computer readable media
- describe communication connection and input/output devices
- implement techniques in connection with hardware or software components
- describe program code embodied in tangible media
- provide compact support neural network
- describe first layer of neurons
- describe second layer of neurons with compact support neurons
- describe output layer
- guarantee bounded space of non-zero response
- provide method of generating neural network
- obtain compact support neuron
- train and normalize compact support neural network
- prune dead neurons

