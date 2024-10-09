# DESCRIPTION

## BACKGROUND

- motivate exoskeletons

## DETAILED DESCRIPTION

- introduce exoskeleton control problem
- motivate end-to-end continuous controller
- propose deep neural network-based controller
- describe training method using deep reinforcement learning
- introduce three DNNs for training
- validate efficacy of proposed controller experimentally
- illustrate proposed approach and experiment platform
- model human variations using muscle strength randomization
- estimate model uncertainties of exoskeleton
- train hip exoskeleton control policy
- deploy trained policy on physical exoskeleton system
- learn mapping from kinematic state to optimal torques
- overcome limitations of RL-based control research
- train end-to-end controller in offline simulation framework
- design actor-critic deep neural network
- learn optimal continuous torque profile policy
- account for human variability using dynamics randomization
- transfer learned control policy to real hip exoskeleton
- discuss application to other human-machine systems
- present highest metabolic reduction reported to date
- illustrate experiment platform and measurements
- deploy learned control policy on physical system
- evaluate computational efficiency of proposed method
- demonstrate adaptability of learned control policy
- show continuous torque profiles during versatile walking and running

### Systems and Methods

- propose decoupled offline training approach
- introduce musculoskeletal agent training
- introduce exoskeleton control policy training
- describe joint learning of three neural networks
- motivate decoupled offline training structure
- describe modeling exoskeleton dynamics
- describe human musculoskeletal agent
- introduce predictive human muscle-actuated simulations
- describe human musculoskeletal model
- define musculotendon unit
- describe muscle contraction dynamics
- introduce Euler-Lagrangian equations
- describe force-length relationship
- introduce musculoskeletal training framework
- describe motion imitation controller
- define reward function
- describe imitation rewards
- describe CoP reward
- describe smooth action reward
- define loss function
- implement muscle coordination network
- describe deep RL-based hip exoskeleton policy training
- implement exoskeleton control policy network
- process output from control policy network
- calculate PD-based torques
- define objective to learn control policy
- design reward function
- learn with Proximal Policy Optimization (PPO)
- derive PPO objective
- motivate PPO objective
- incorporate sim-to-real transfer
- randomize exoskeleton dynamics
- randomize muscle forces
- modify objective for sim-to-real transfer
- deploy on real hip exoskeleton system
- use joint-level PD controller
- describe dynamics of actuators
- implement low-level torque control architecture
- describe portable exoskeleton
- illustrate exoskeleton design
- describe electronic architecture
- implement high-level microcontroller
- describe power management
- introduce experiment-free versatile optimization
- motivate learning-in-simulation framework
- describe learning-in-simulation framework
- illustrate learning-in-simulation framework
- train neural networks
- describe physics-informed components
- incorporate musculoskeletal model
- describe exoskeleton controller
- demonstrate adaptive versatile control
- illustrate assistive torque profiles
- demonstrate continuous assistive torque profile
- illustrate activity-varying experiment
- demonstrate metabolic rate reduction
- illustrate metabolic rate reduction results

### Study Discussion

- discuss user feedback on exoskeleton
- highlight importance of usability and comfort
- introduce System Usability Scale (SUS)
- describe exoskeleton's performance on SUS
- discuss challenges in sim2real methods
- introduce learning-in-simulation framework
- describe benefits of learning-in-simulation method
- highlight advantages over previous studies
- discuss limitations of the controller
- mention potential applications of the method

### Methods

- model human muscle mechanics
- define musculoskeletal model
- specify muscle activations
- derive muscle force equation
- model human dynamics
- derive Euler-Lagrangian equations
- model human-robot interaction
- define exoskeleton control network
- simulate interaction forces and moments
- design bushing element model
- learn motion imitation neural network
- define imitation policy
- design reward function
- specify sub-rewards
- learn imitation policy
- learn muscle coordination neural network
- define muscle coordination policy
- design loss function
- train neural networks
- introduce exoskeleton control neural network
- describe neural network architecture
- define objective function for learning
- introduce reward function
- define sub-rewards
- introduce action smoothness sub-reward
- filter output of trained controller
- employ PD control loop
- introduce closed-loop simultaneous training
- describe decoupled training scheme
- incorporate sub-rewards in reward function
- introduce domain randomization
- perturb robot dynamics parameters
- randomize musculoskeletal dynamics parameters
- modify optimization objective
- deploy learned controller
- evaluate controller in indoor and outdoor settings
- describe exoskeleton hardware
- introduce processing circuitry
- describe processing circuitry components
- introduce network interfaces
- describe data storage components
- introduce exoskeleton control application
- describe executable programs
- introduce memory components
- describe processor components
- introduce local interface
- describe alternative embodiments
- introduce computer-readable medium
- describe computer-readable medium components
- introduce logic or application embodiments
- describe shared or separate computing devices
- introduce modifications and variations
- describe substantially and range format
- conclude disclosure

