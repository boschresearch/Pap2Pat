# DESCRIPTION

## BACKGROUND

### Technical Field

- introduce deep reinforcement learning algorithm

### Discussion of the Related Art

- motivate safe reinforcement learning
- discuss formal verification
- introduce reinforcement learning
- explain safe reinforcement learning
- discuss limitations of safe RL
- introduce symbolic reinforcement learning
- discuss limitations of symbolic RL
- introduce deep reinforcement learning
- discuss benefits of deep RL
- discuss limitations of deep RL
- discuss constrained reinforcement learning
- discuss generalization concerns
- summarize related work

## SUMMARY

- introduce system and method
- specify safety constraints
- enforce safety constraints
- learn end-to-end policy
- generalize to complex visual inputs
- demonstrate safe learning
- optimize for objectives
- introduce template-based mapping
- perform template matching
- map objects to planar coordinates
- determine safe actions
- output safe actions
- prevent unsafe actions

## DETAILED DESCRIPTION OF EXEMPLARY EMBODIMENTS

- introduce embodiments
- describe framework
- outline system capabilities

### Specifying Safety Controllers

- introduce differential Dynamic Logic (dL)
- define hybrid programs (HPs)
- specify syntax and informal semantics of HPs
- define formulas of dL
- motivate use of dL for specifying safety constraints
- overview of system and method for specifying and enforcing safety constraints
- describe applicability in complex state spaces
- motivate use of interpretable safety rules
- describe example real-world application in robots in an Amazon-style warehouse
- introduce computer vision and reinforcement learning agent system
- describe input to system
- describe mapping from visual input to symbolic features
- describe checking symbolic constraints
- describe execution of action in environment
- describe output of system
- illustrate system architecture in FIG. 1A
- describe reinforcement learning loop
- describe safety system
- overview of safe RL on visual inputs
- specify safety controllers
- use template matching for object detection
- define symbolic safety constraints
- construct symbolic mapping
- describe QATM algorithm
- modify QATM for symbolic mapping
- detect objects from score maps
- train symbolic mapping
- create augmented dataset
- train template matching
- define label score map
- use focal loss for training
- enforce safety constraints
- augment RL algorithm
- extract symbolic features
- evaluate safety constraints
- prevent unsafe actions
- provide pseudo-code for safe RL
- construct symbolic state
- learn action constraints
- ensure safety specification
- construct state-dependent constraints
- learn dynamics of safety-relevant objects
- automatically construct constraints
- use teach step for initial knowledge
- map differences to actions
- use one-step look ahead
- construct guard on each action
- perform worst-case one-step look-ahead
- construct safety constraint
- discuss limitations of approach
- require less human effort
- sufficient in certain domains
- extend to multi-step planning
- provide example of safety constraint
- discuss importance of safety
- conclude symbolic safety approach

## EXPERIMENTAL EVALUATION

- evaluate systems on two environments

### Descriptions of Evaluation Environments

- introduce XO environment
- describe road runner environment
- specify symbolic state space

### Preservation of Safety Constraints

- preserve safety specifications
- compare safety performance of systems

### Generalization and Internalization

- test penalization hypothesis
- evaluate effect of penalization on performance
- compare cumulative reward with and without safety guard
- test safety generalization to mis-specified environment
- evaluate effect of penalization on safety generalization
- propose alternative embodiment for safety generalization

### Optimization

- evaluate optimization performance in XO environment
- evaluate optimization performance in road runner environment
- analyze causes of performance differences
- discuss importance of safety as a stand-alone concern
- summarize optimization results

### System Implementations

- describe implementation options
- introduce cloud computing model
- define on-demand self-service
- define broad network access
- define resource pooling
- define rapid elasticity
- define measured service
- introduce software as a service (SaaS)
- introduce platform as a service (PaaS)
- introduce infrastructure as a service (IaaS)
- describe private cloud deployment
- describe community cloud deployment
- describe public cloud deployment
- describe hybrid cloud deployment
- describe cloud computing environment
- introduce cloud computing node
- describe computer system/server
- describe system memory
- describe bus
- describe storage system
- describe program/utility
- describe external devices
- describe input/output interfaces
- describe network adapter
- describe cloud computing environment
- describe cloud computing nodes

