# DESCRIPTION

## FIELD OF THE INVENTION

- relate to segmenting images into background and foreground

## BACKGROUND OF THE INVENTION

- introduce video surveillance applications
- describe background subtraction methods
- discuss multimodal backgrounds and Gaussian distributions
- motivate Bayesian update procedure
- discuss mixture of model background approaches
- describe non-parametric kernel density estimation
- introduce 3D geometry-based method
- discuss frequency-based techniques
- describe adapting to color composition of foreground objects
- highlight limitations of conventional methods

## SUMMARY OF THE INVENTION

- introduce method for detecting left-behind objects
- highlight advantages of the method
- describe method's functionality

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

- introduce left-behind object detection method
- describe camera acquiring image sequence
- model pixel color evolution over time
- define background and foreground models
- update background model parameters
- analyze temporal evolution of pixel intensities
- maintain parameters at multiple time scales
- describe short-term and long-term background models
- define foreground model with long-term and short-term masks
- apply evidence rules to foreground masks
- describe four hypotheses from foreground masks
- update motion image with evidence values
- increment evidence values for left-behind objects
- decrement evidence values for non-left-behind objects
- set evidence values to zero if less than zero
- define evidence threshold for left-behind object detection
- describe decay constant for removing left-behind objects
- introduce sequential Bayesian update procedure
- describe Bayesian update for long-term and short-term models
- maintain multimodality of background model
- update at most one layer per pixel
- determine number of layers for each pixel
- use embedded confidence score for layer selection
- describe layer model with 3D multivariate Gaussian distributions
- estimate probability distributions of mean and variance
- extract statistical information from probability distributions
- use expectation of mean and variance for change detection
- use variance of mean as confidence measure
- describe normal-inverse-Wishart distribution
- update parameters with new observations
- integrate joint posterior density with respect to covariance
- obtain marginal posterior density for mean
- use expectations of marginal posterior distributions
- describe confidence measure for layer
- separate RGB color channels for processing
- generate diagonal covariance matrix
- initialize background model with multiple layers
- update background model parameters with new samples
- use confidence scores to determine number of layers
- detect changed regions of the scene
- apply connected component analysis to motion image
- verify method with publicly available datasets

## EFFECTS OF THE INVENTION

- summarize advantages over tracking approaches
- highlight detection capabilities
- claim scope and variations

