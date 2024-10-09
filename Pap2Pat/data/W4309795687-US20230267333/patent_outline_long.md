# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- motivate model uncertainty
- limitations of prior approaches
- importance of abstention policy
- prior approaches to abstention policy
- limitations of prior approaches
- integrate abstention into model training
- overview of selective networks

## SUMMARY

- summarize method of training selective network
- embodiment of method

## DETAILED DESCRIPTION

- introduce selective networks
- motivate selective networks
- define selective neural network
- derive empirical coverage and selective risk
- formulate training objective
- discuss limitations of existing approaches

### Gumbel-Softmax Selective Networks

- introduce Gumbel-softmax reparameterization
- motivate Gumbel-softmax reparameterization
- redefine selection function
- apply Gumbel-softmax reparameterization
- derive Gumbel-softmax distribution
- approximate argmax with softmax
- discuss temperature annealing
- combine Gumbel-softmax with selective networks
- illustrate proposed approach
- describe forward pass
- describe backward pass
- summarize Gumbel-softmax selective networks

### Experimental Results

- describe experimental setup
- introduce baselines
- categorize baselines
- describe general purpose selective networks
- introduce SelectiveNet
- introduce MC-dropout
- describe specialized selective networks
- introduce Deep Gamblers
- introduce Softmax Response
- describe datasets
- introduce CIFAR-10
- describe CIFAR-10 dataset
- introduce Cats vs. Dogs
- describe Cats vs. Dogs dataset
- introduce ImageNet-100
- describe ImageNet-100 dataset
- introduce Concrete Compressive Strength
- describe Concrete Compressive Strength dataset
- introduce California Housing
- describe California Housing dataset
- introduce Ames Housing
- describe Ames Housing dataset
- describe implementation details
- introduce auxiliary prediction head
- describe architecture adjustments
- describe data augmentation
- describe optimization
- describe Gumbel-softmax temperature
- describe coverage calibration
- introduce coverage calibration
- describe evaluation protocol
- describe selective classification results
- introduce Table 1
- describe results on CIFAR-10
- describe results on Cats vs. Dogs
- introduce Table 2
- describe results on ImageNet-100
- describe selective regression results
- introduce Tables 3-7
- describe results on Concrete Compressive Strength
- describe results on California Housing
- describe results on Ames Housing
- discuss importance of abstention
- discuss integration with existing infrastructure
- discuss significance of selective network training
- describe computer program product
- describe computer readable storage medium
- describe network adapter card
- describe computer readable program instructions
- describe electronic circuitry
- describe flowchart illustrations
- describe block diagrams
- describe computer system

