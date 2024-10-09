# DESCRIPTION

## BACKGROUND

- motivate sensorimotor cortex
- limitations of current time-delay estimation techniques
- application of time-delay estimation in biological systems
- need for comprehensive computational model

## BRIEF SUMMARY

- introduce embodiments of subject invention
- summarize tasks of computational model
- distinguish from prior art methods

## DETAILED DESCRIPTION

- introduce sensorimotor system
- define sensorimotor system components
- describe sensorimotor system processes
- motivate predictive control
- describe limitations of standard feedback control
- introduce time delay estimation
- derive time delay estimation equation
- describe biological constraints
- introduce predicting current and future sensory states
- describe application of model to simulate hVOR system

### Estimating the Time Delay

- introduce linear time-varying system
- define state vector and control vector
- describe Jacobian matrices
- derive solution to differential equation
- introduce time delay vector
- describe error signal calculation
- introduce gradient descent method
- derive time delay estimation equation
- describe biological constraints
- introduce finite buffer for hardware implantation
- describe storage of history of signals
- introduce assumption of bounded time delay
- describe limitations of Equation (6)
- introduce condition for stability
- describe application to hardware implantation

### Predicting Current and Future Sensory States

- introduce predictive nature of sensorimotor system
- describe smooth pursuit system
- introduce model for predicting future state
- derive equation for predicting future state
- describe importance of time delay estimation
- introduce PID controller
- describe PID controller gains
- introduce optimal feedback controller
- describe optimal feedback controller gain
- introduce simulation experiments
- describe benefits of time-delay estimation and prediction model
- introduce application to hVOR system
- describe poor response of traditional controller
- introduce oscillatory behavior
- describe similarity to sensorimotor diseases
- introduce detection of faulty sensorimotor systems
- describe application to neurological disorders

### Example 1

- introduce vestibulo-ocular reflex model
- define system equations
- derive time-delay estimator
- derive state predictor
- demonstrate unstable hVOR without time-delay estimation
- demonstrate stable hVOR with time-delay estimator and state predictor
- generalize to other embodiments

