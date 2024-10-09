# DESCRIPTION

## BACKGROUND

- motivate visual attention prediction

## BRIEF DESCRIPTION

- outline neural network training for saliency prediction

## DETAILED DESCRIPTION

- formulate saliency map prediction as probability distribution prediction task
- describe deep architecture with loss function based on probability distance measures
- illustrate system for generating saliency map with trained neural network
- describe components of system, including attention map generator and output component
- outline method for generating saliency map using trained neural network

### Saliency Maps as Probability Distributions

- model saliency map as generalized Bernoulli distribution over pixels

### Generating Attention Maps (S102)

- generate attention maps from aggregated fixations of multiple observers

### The Neural Network

- describe pre-trained convolutional neural network architecture
- outline additional convolutional layers and non-linear functions

### Learning to Predict the Probability of Fixation (S104)

- train fully-convolutional network on image and ground-truth saliency map pairs
- compute and minimize distance between predicted and ground-truth probability distributions

### Predicting Saliency (S108)

- generate saliency map for new image using pre-trained neural network

### Further Processing (S110)

- extract information from salient region of image based on saliency map

## Examples

- describe neural network architecture for saliency map extraction

### 1. Datasets

- introduce saliency datasets

## Results

- present results of neural network models trained with different loss functions

### 1. Loss Functions

- define Euclidean and Huber regression loss
- evaluate performance of neural network models trained with different loss functions
- compare results of different loss functions

