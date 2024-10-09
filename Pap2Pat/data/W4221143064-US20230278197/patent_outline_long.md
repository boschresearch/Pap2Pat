# DESCRIPTION

## TECHNICAL FIELD

- relate to robotic manipulation

## BACKGROUND

- introduce contact-based reasoning
- discuss limitations of LCP models
- motivate stochastic dynamics

## SUMMARY

- introduce object of embodiments
- motivate uncertainty in TO
- define SDLCS
- motivate robust optimization
- introduce chance constrained optimization
- formulate MIQPCC
- design SNMPC
- motivate soft constraints
- introduce ERM-based penalty
- divide chance constraints
- optimize SDLCS with hard chance constraints

## DETAILED DESCRIPTION

- introduce patent description conventions
- define terminology and phrasing
- illustrate robotic system block diagram
- describe robotic system components
- explain object manipulation process
- motivate contact model importance
- introduce stochastic discrete-time linear complementarity system
- describe uncertainty in system parameters and dynamics
- explain robust optimization formulation
- describe SDLCS-based robotic system configuration
- explain chance-constrained method for trajectory optimization
- describe joint chance-constraints for robust control problem
- outline control of object manipulation process

### Mathematical Implementation:

- introduce Discrete-Time Linear Complementarity System (DLCS)
- define DLCS with complementarity constraints
- describe DLCS dynamics
- introduce Stochastic Discrete-time Linear Complementarity Systems (SDLCS)
- define SDLCS with uncertainty
- describe SDLCS dynamics
- introduce Robust Trajectory Optimization for SDLCS
- formulate robust TO problem
- impose stochastic dynamics
- impose joint chance-constraints
- describe initial condition and bounds
- introduce Joint Linear Chance Constraints
- impose joint chance constraints
- describe complementarity relationship
- convert joint chance constraints to tractable form
- introduce Chance Complementarity Constraints (CCC) for SDLCS
- decompose stochastic complementarity constraints
- formulate CCC using mixed integer programming
- introduce mathematical implementation
- relax deterministic chance complementarity constraints
- formulate relaxed chance constraints
- decompose two-sided chance constraint
- impose individual constraints for each mode
- provide lower bound for Δ
- formulate mixed-integer quadratic programming with chance constraints
- define objective function and stochastic dynamics evolution
- specify initial condition and bounds
- introduce stochastic non-linear model predictive control
- formulate SNMPC for stochastic nonlinear complementarity system
- linearize stochastic dynamics along reference trajectory
- modify MIQPCC for SNMPC
- specify constraints for SNMPC
- allow deviation from reference discrete mode sequence
- account for stochastic dynamics and complementarity constraint during control

## EXEMPLARY EMBODIMENTS

- illustrate block diagram of robotic system
- describe network interface controller
- explain processor and memory configuration
- detail storage device and its modules
- describe solving robust control problem
- optimize cost function with chance complementarity constraints
- control manipulation of object
- illustrate manipulation system with SDLCS
- describe dynamics of manipulation system
- define state and input of manipulation system
- express complementarity conditions
- modify SNMPC for manipulation system
- relax stochastic complementarity constraints
- add uncertainty to dynamics and friction coefficient
- define chance constraints
- select hyperparameter based on predefined probability
- illustrate method for manipulating object
- collect digital representation of task
- solve robust control problem
- optimize cost function with joint chance-constraints
- control manipulation of object
- illustrate robot system with joints and end effector
- describe robot state and joint commands
- use SDLCS and chance complementarity constraints for robust trajectory optimization
- collect digital representation of task
- solve robust control problem with joint chance-constraints
- compute sequence of control forces
- control manipulation of object

