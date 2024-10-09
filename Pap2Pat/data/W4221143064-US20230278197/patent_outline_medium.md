# DESCRIPTION

## TECHNICAL FIELD

- relate to robotic manipulation

## BACKGROUND

- motivate contact modeling

## SUMMARY

- introduce trajectory optimization
- motivate stochastic dynamics
- propose chance constrained optimization
- formulate MIQPCC
- design SNMPC

## DETAILED DESCRIPTION

- introduce patent description conventions
- describe robotic system block diagram
- motivate stochastic discrete-time linear complementarity system
- describe contact model and trajectory optimization
- formulate robust control problem with chance constraints
- solve control problem and compute control forces

### Mathematical Implementation:

- define DLCS
- derive DLCS equations
- introduce SDLCS
- formulate robust TO for SDLCS
- impose joint chance-constraints
- derive joint linear chance constraints
- apply Boole's inequality
- define chance complementarity constraints
- decompose stochastic complementarity constraints
- introduce mathematical implementation
- relax deterministic chance complementarity constraints
- formulate mixed-integer quadratic programming with chance constraints
- describe stochastic non-linear model predictive control
- formulate modified mixed-integer quadratic programming with chance constraints for SNMPC
- linearize stochastic dynamics along reference trajectory
- describe uncertainty propagation
- allow deviation from reference discrete mode sequence

## EXEMPLARY EMBODIMENTS

- illustrate robotic system 101 block diagram
- describe network interface controller and connections
- outline processor and memory components
- detail storage device and modules
- explain solving robust control problem and optimizing sequence of control forces
- describe output interface and controller
- illustrate manipulation system 801 block diagram
- derive dynamics of manipulation system 801
- formulate stochastic complementarity constraints
- modify SNMPC equations for manipulation system 801
- illustrate method 900 for manipulating an object
- describe steps of method 900
- illustrate robot system 1000 and components
- outline robot controller 1031 and tasks

