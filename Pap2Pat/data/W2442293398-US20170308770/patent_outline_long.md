# DESCRIPTION

## BACKGROUND

- introduce visual attention prediction
- motivate saliency map prediction
- summarize traditional saliency detection methods
- describe neural network architectures for saliency prediction
- limitations of deep methods

## BRIEF DESCRIPTION

- describe method for generating prediction system
- describe training system for generating prediction system
- describe method for predicting saliency in an image
- specify processor implementation

## DETAILED DESCRIPTION

- introduce saliency map prediction as probability distribution prediction task
- formulate saliency map as generalized Bernoulli distribution
- describe deep architecture with loss function based on probability distance measures
- describe Bhattacharyya distance for multinomial distributions
- pair loss function with softmax activation function
- describe superior performance with respect to standard regression loss functions
- describe generation of saliency map for large image using existing GPUs
- describe use of trained neural network, specifically Convolutional Network (ConvNet)
- describe adaptation of learned neural network to specific task of saliency detection
- illustrate computer-implemented system for generating saliency map
- describe memory storing instructions for performing method
- describe processor executing instructions
- describe computing devices and input/output devices
- describe attention map generator
- describe neural network training component
- describe prediction component
- describe processing component
- describe output component
- describe optional processing of image based on computed saliency map
- describe output of information based on saliency map
- describe implementation of method in computer program product
- describe non-transitory computer-readable recording medium
- describe alternative implementation in transitory media

### Saliency Maps as Probability Distributions

- introduce optimization and minimization of function
- model saliency map as probability distribution over pixels
- formulate generalized Bernoulli distribution

### Generating Attention Maps (S102)

- obtain eye gaze data for set of observers for each training image
- combine eye gaze data to generate set of fixation coordinates
- generate binary fixation map from ground-truth eye-fixations
- convolve binary map to approximate general region fixated on
- normalize smoothed map to generate normalized attention map
- convert normalized attention map to attention map probability distribution
- apply softmax function to obtain probability distribution

### The Neural Network

- describe example network architecture for saliency map extraction
- use pre-trained convolutional layers of existing neural network
- add additional convolutional layers to pre-trained layers
- describe each convolutional layer as 4D tensor of weights
- apply non-linear function to neuron response
- describe input to neural network as 3D tensor
- describe filters of respective layer as sliding window across output
- describe output of final fully-convolutional network as down-sampled saliency map
- describe optional max-pooling layers

### Learning to Predict the Probability of Fixation (S104)

- adopt end-to-end learning method
- train fully-convolutional network on image and ground-truth saliency map pairs
- compute predicted probability distributions
- compute distance between predicted and ground-truth distributions
- construct objective function to minimize distance
- update network weights using backpropagation
- iterate until stopping point reached
- discuss distance measures and loss functions
- initialize network with pre-trained weights

### Predicting Saliency (S108)

- pass new image through pre-trained network to generate saliency map

### Further Processing (S110)

- extract information from salient region of image
- identify pixels with predicted saliency above threshold
- label salient region and extract information
- discuss system output and applications
- provide examples of applications in various fields

## Examples

- introduce neural network architecture
- describe pre-training on ImageNet
- explain fine-tuning on SALICON dataset
- detail training parameters and optimization
- mention implementation in Gaffe

### 1. Datasets

- introduce SALICON dataset
- describe OSIE dataset
- introduce MIT-1003 dataset
- introduce MIT-300 dataset
- explain data collection methods
- mention dataset limitations

## Results

- summarize results of different loss functions

### 1. Loss Functions

- introduce loss functions
- define Euclidean regression loss
- define Huber regression loss
- explain KL-divergence loss
- explain Bhattacharyya distance-based loss
- compare performance of different losses
- show evolution of metrics on SALICON validation set
- highlight robustness of KL-divergence and Bhattacharyya distance-based losses
- compare with standard regression losses
- explain performance on SALICON challenge
- compare with other methods for predicting saliency
- show results of comparison with other methods
- highlight performance of PDP method

