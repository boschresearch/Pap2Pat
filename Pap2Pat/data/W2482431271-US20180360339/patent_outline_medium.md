# DESCRIPTION

## BACKGROUND

- motivate sensorimotor control systems
- limitations of current time-delay estimation techniques

## BRIEF SUMMARY

- introduce embodiments of the subject invention

## DETAILED DESCRIPTION

- define sensorimotor system
- describe time delays in sensorimotor system
- introduce computational model simulating brain as sensorimotor control system
- estimate time delay using gradient descent method
- predict current and future sensory states using estimated time delay

### Estimating the Time Delay

- introduce linear time-varying system equation
- solve equation to obtain current state
- incorporate time delay into solution
- calculate error signal between delayed sensory signal and estimated delayed sensory signal
- use gradient descent method to estimate time delay
- consider biological constraints on maximum delay
- store history of constructed signals in finite buffer

### Predicting Current and Future Sensory States

- combine equations to predict future state
- use estimated time delay to predict future state
- calculate performance error and estimated performance error
- design PID controller and optimal feedback controller
- demonstrate benefits of time-delay estimation and prediction model
- apply model to simulate horizontal Vestibulo-Ocular Reflex (hVOR) system
- show instability of hVOR without time-delay estimation and prediction
- discuss potential applications in detecting faulty sensorimotor systems

### Example 1

- apply time-delay estimation model
- derive hVOR system equations
- demonstrate simulation results

