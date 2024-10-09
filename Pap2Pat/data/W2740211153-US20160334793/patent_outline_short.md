# DESCRIPTION

## BACKGROUND OF THE INVENTION

- motivate UUV applications

## SUMMARY OF THE INVENTION

- describe optical detector array capabilities
- outline UUV navigation applications

## DETAILED DESCRIPTION

- introduce underwater communication links
- motivate formation control of UUVs
- summarize formation architectures and strategies
- discuss optical detection for underwater communication
- outline goals and applications of the study

### UUV Modeling, Control and Stability

- introduce UUV kinematics
- derive Euler angles
- formulate UUV dynamics
- apply Newton-Euler formulation
- derive UUV modeling equations
- formulate DOF rigid-body equations of motion
- Analyze hydrodynamic forces on UUV
- Derive added mass and damping matrices
- Calculate restoring forces and moments
- Introduce PID control for UUV stability
- Discuss PID stability for UUVs
- derive UUV modeling equations
- introduce sliding mode controller for UUV
- prove SMC stability for UUVs

### Characterization of Optical Communication in a Leader-Follower UUV Formation

- introduce optical communication in UUV formation
- motivate light field characterization
- describe experimental setup
- derive beam pattern using Gaussian function
- explain inverse square law and Beer-Lambert law
- present experimental results
- discuss implications of results on photo-detector array design
- identify limitations and sources of error
- conclude feasibility of control design for underwater distance detection

### Optical Detector Array Design for Navigational Feedback Between UUVs

- introduce optical detector array design for UUVs
- motivate 5-DOF motion detection
- describe optical design considerations
- discuss environmental considerations
- outline hardware considerations
- introduce simulator for array design evaluation
- define reference frame for simulator
- define detector array geometry
- radiometry calculations
- simulate light field and detector output
- analyze output images using SAM algorithm
- compare planar and curved array designs
- evaluate detector array performance
- experimentally validate simulator results
- discuss and conclude detector array design

### Pose Detection and Control Algorithms for Dynamic Positioning of UUVs Via an Optical Sensor Feedback System

- introduce optical feedback system for UUV dynamic positioning
- motivate two pose detection methods: SAM and image moment variants
- describe phase correlation and log-polar transform algorithm
- explain Spectral Angle Mapper (SAM) algorithm
- calculate image moment invariants for pose detection
- implement PID and SMC for UUV control in regulation and tracking scenarios
- introduce pose detection and control algorithms for dynamic positioning of UUVs
- derive control problem for static-dynamic system
- describe image moments approach for pose detection
- present results for single-DOF SMC control with 21×21 and 5×5 detector arrays
- evaluate PID control for x-axis translation
- present case study for dynamic positioning with multiple concurrent initial pose errors
- present case study for dynamic positioning with multiple concurrent initial pose errors in the presence of added disturbances
- describe dynamic-dynamic system and present results for leader-follower case study
- discuss simulation results and compare performance of pose detection algorithms
- conclude on suitability of image moment invariants algorithm and SMC for UUV dynamic positioning

### Experimental Pose Detection for UUV Control System Using an Optical Detector Array

- introduce UUV docking challenges
- describe existing docking station architectures
- motivate optical communication for docking
- introduce pose detection approach using optical detector array
- describe hardware selection and detector array design
- outline methodology for empirical measurements
- detail calibration procedures for photodiodes and pose estimation
- describe performance evaluation criteria for pose detection and velocity estimation
- outline stochastic assessment of pose uncertainty using Monte Carlo analysis
- present calibration results for photodiode consistency and temperature dependence
- summarize results of pose detection experiments
- Introduce experimental pose detection system for UUV control
- Describe calibration procedure for photodiode response range and temperature effects
- Investigate noise and cross-talk in signal transmission
- Conduct underwater calibration procedure for pose and velocity estimation
- Evaluate performance of pose detection algorithm for stationary and dynamic cases
- Analyze results of two experimental cases with different light source and UUV platform offsets
- Conduct stochastic model simulations to predict system performance under varying environmental conditions
- Evaluate system performance using Monte Carlo simulations with different detector trajectories and hardware noise levels
- Discuss results and limitations of the system, including potential contributors to uncertainty and error
- Suggest hardware improvements and design considerations for future development
- Conclude that the optical detector array provides an accurate and cost-effective positioning system for UUV navigation and docking

### Discussion

- characterize underwater environment
- discuss limitations of single light source
- describe detector array design
- evaluate pose detection algorithms
- discuss control system simulations

### Conclusions

- summarize pose detection capabilities
- identify limitations of system in real-world conditions

### Photodiode Data Collection Procedure Using Beagleboard-XM and Two Arduinos

- describe Arduino setup
- describe BB-XM setup
- outline data collection procedure

### Programs for Experimental Data Collection and Analysis

- list programs for data collection and analysis

