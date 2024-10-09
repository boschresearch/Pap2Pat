# DESCRIPTION

## CROSS REFERENCE

- claim benefit of german patent application

## FIELD

- relate to computer-implemented method

## BACKGROUND INFORMATION

- describe possibilities of predicting behavior

## SUMMARY

- achieve precise prediction of behavior
- determine value of first moment of first distribution
- determine value of second moment of first distribution
- determine expected value for first moment of second distribution
- determine second moment of third distribution
- determine sum of third distributions
- determine prediction of behavior
- recursively determine value of first moment
- recursively determine value of second moment
- efficiently determine expected value
- determine covariance of first moment of second distribution
- determine expected value for second moment of second distribution
- determine second moment of third distribution
- consider context variable
- determine history of dynamic system
- consider neighborhood of agents
- model latent states of agents
- control agent depending on prediction

## DETAILED DESCRIPTION OF EXAMPLE EMBODIMENTS

- introduce device for predicting behavior of agents
- describe device components
- describe interface and sensor system
- describe sensor system capabilities
- describe actuator and control command
- describe computer program
- introduce dynamic system example
- describe agents in dynamic system
- describe roundabout example
- describe observed trajectories
- describe predicted trajectories
- describe Gaussian mixture distribution
- describe confidence intervals
- describe prediction of distance, velocity, or acceleration
- describe autonomous vehicle example
- describe machine learning model
- introduce latent variable X
- describe observed variable Y
- describe initial value for latent state
- describe deterministic change in latent state
- describe stochastic change in latent state
- describe context variable I
- describe normal distribution for observed variable
- describe neural network for deterministic change
- describe neural network for stochastic change
- describe neural network for observed variable
- describe update to deterministic change
- describe update to stochastic change
- describe message for agent
- describe operation AGG
- describe edges of graph
- describe prediction for prediction time point T
- describe marginal probability p(yT|I)
- describe kernel p(xT|x0,I)
- describe Gaussian mixture model p(x0|I)
- describe mean value and covariance
- describe expected value and covariance
- describe cross-covariance
- describe Jacobi matrix
- describe method for prediction p(yT|I)
- describe inner loop and outer loop
- describe neural network for moments
- describe context variable I and association Nm
- define trajectories
- describe operation AGG
- motivate graph neural network
- describe step 404
- determine first moment recursively
- describe tool for expected value and covariance
- implement operation AGG
- calculate expected value and covariance
- determine Jacobi matrix
- describe affine transformation
- calculate expected value and covariance recursively
- determine value of first moment
- describe step 406
- determine second moment recursively
- calculate covariance of deterministic change
- calculate expected value of stochastic change
- determine value of second moment
- describe step 408
- determine expected value of first moment
- determine covariance of first moment
- describe step 410
- determine first moment of normal distribution
- describe step 412
- determine expected value of second moment
- describe step 414
- determine second moment of normal distribution
- describe outer loop and prediction

