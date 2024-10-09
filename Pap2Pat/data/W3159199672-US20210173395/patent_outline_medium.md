# DESCRIPTION

## BACKGROUND

### Technical Field

- introduce deep reinforcement learning algorithm

### Discussion of the Related Art

- motivate safe reinforcement learning
- limitations of formal verification
- discuss reinforcement learning
- discuss safe reinforcement learning
- limitations of existing approaches
- motivate deep reinforcement learning

## SUMMARY

- introduce system and method
- describe safety constraints
- describe template-based mapping
- describe empirical evaluations
- describe applications
- describe embodiments

## DETAILED DESCRIPTION OF EXEMPLARY EMBODIMENTS

- introduce framework for safe reinforcement learning

### Specifying Safety Controllers

- introduce differential Dynamic Logic (dL)
- define syntax and semantics of hybrid programs (HPs)
- motivate use of dL for specifying safety constraints
- overview of system and method for specifying and enforcing safety constraints
- describe computer vision and reinforcement learning agent system
- illustrate system architecture with block diagram
- explain symbolic mapping process and safe action determination
- integrate safety system with RL agent to enforce safety
- describe end-to-end deep reinforcement learning algorithm for safe RL on visual inputs
- specify safety controllers
- construct symbolic mapping
- introduce QATM algorithm
- describe feature extractor
- explain template matching
- detect objects from score maps
- train symbolic mapping
- create augmented dataset
- train template matching
- create label score map
- define loss function
- enforce constraints
- augment RL algorithm
- extract symbolic features
- evaluate safety constraints
- learn action constraints
- infer object dynamics
- construct constraints on action space

## EXPERIMENTAL EVALUATION

- evaluate systems on two environments

### Descriptions of Evaluation Environments

- describe XO and road runner environments

### Preservation of Safety Constraints

- preserve safety specifications

### Generalization and Internalization

- test penalization hypothesis
- evaluate safety generalization
- compare cumulative reward with and without safety guard

### Optimization

- compare cumulative reward for vanilla PPO and systems according to embodiments
- analyze performance in road runner environment

### System Implementations

- describe cloud computing environment
- define on-demand self-service
- define broad network access
- define resource pooling
- define rapid elasticity
- define measured service
- describe software as a service (SaaS)
- describe platform as a service (PaaS)
- describe infrastructure as a service (IaaS)
- describe private cloud
- describe community cloud
- describe public cloud
- describe hybrid cloud

