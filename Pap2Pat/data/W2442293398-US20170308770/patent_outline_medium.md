# DESCRIPTION

## BACKGROUND

- motivate visual attention prediction
- summarize applications of saliency map prediction

## BRIEF DESCRIPTION

- describe method for generating prediction system
- describe method for predicting saliency in an image

## DETAILED DESCRIPTION

- formulate saliency map prediction as probability distribution prediction task
- describe deep architecture with loss function based on probability distance measures
- introduce system for generating saliency map of input image
- describe components of system, including memory, processor, and input/output devices
- detail instructions for performing method, including attention map generator and neural network training component
- describe prediction component and processing component
- outline output component and optional processing of image
- describe implementation of method in computer program product
- detail saliency maps as probability distributions
- describe generating attention maps, including obtaining eye gaze data and constructing ground-truth saliency maps
- introduce neural network architecture for saliency map extraction

### Saliency Maps as Probability Distributions

- model saliency map as probability distribution over pixels

### Generating Attention Maps (S102)

- obtain eye gaze data for set of observers for each training image
- generate binary fixation map from ground-truth eye-fixations
- convolve binary map to approximate general region fixated on and normalize to generate attention map probability distribution

### The Neural Network

- describe example network architecture for saliency map extraction
- detail pre-trained layers and additional convolutional layers
- describe non-linear function applied to neuron response
- outline output of neural network, including final down-sampled saliency map

### Learning to Predict the Probability of Fixation (S104)

- train fully-convolutional network on image and ground-truth saliency map pairs
- compute predicted probability distribution using softmax activation function
- calculate distance between predicted and ground-truth distributions using appropriate measure
- update network weights using backpropagation and objective function minimization

### Predicting Saliency (S108)

- generate saliency map for new image using pre-trained neural network

### Further Processing (S110)

- extract information from salient region of image based on saliency map
- apply method to various applications in transportation, retail, and healthcare

## Examples

- describe neural network architecture for saliency map extraction
- train and fine-tune network on SALICON dataset

### 1. Datasets

- introduce SALICON dataset
- describe OSIE, MIT-1003, and MIT-300 datasets
- summarize characteristics of each dataset

## Results

- evaluate performance of neural network models using different loss functions and metrics

### 1. Loss Functions

- define Euclidean and Huber regression loss functions
- evaluate performance of models trained using different loss functions
- compare performance of KL-divergence and Bhattacharyya distance-based loss
- show evolution of metrics on SALICON validation set
- compare performance of Bhattacharyya distance-based loss with other methods
- discuss robustness of KL-divergence and Bhattacharyya distance-based loss to outliers

