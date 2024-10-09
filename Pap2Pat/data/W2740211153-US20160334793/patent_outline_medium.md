# DESCRIPTION

## BACKGROUND OF THE INVENTION

- introduce UUV applications

## SUMMARY OF THE INVENTION

- demonstrate optical detector array capabilities
- predict pose estimation performance
- develop optical detector array for UUV navigation
- evaluate pose detection algorithms

## DETAILED DESCRIPTION

- introduce underwater communication links
- motivate formation control of UUVs
- summarize formation architectures
- describe leader-follower method
- discuss limitations of acoustic communication
- introduce optical detection as alternative
- describe optical communication challenges
- summarize detector array designs
- review previous studies on optical communication
- state goals of this study
- mention additional applications

### UUV Modeling, Control and Stability

- introduce UUV modeling
- define kinematics
- describe Euler angles
- derive velocity transformation matrix
- define UUV dynamics
- formulate Newton-Euler equations
- derive rigid-body dynamics
- define inertia tensor
- describe translational motion
- derive UUV modeling equations
- derive rotational motion equations
- derive DOF rigid-body equations of motion
- simplify rigid-body equations
- introduce hydrodynamic forces and moments
- introduce UUV modeling
- analyze hydrodynamic forces
- define added mass
- apply strip theory
- discuss hydrodynamic damping
- explain restoring forces and moments
- introduce PID control
- describe UUV controllers and stability
- detail PID control law
- discuss PID stability for UUVs
- conclude UUV modeling and control
- derive UUV model equations
- introduce PID control law
- define Lyapunov function candidate
- introduce Sliding Mode Controller (SMC)
- derive SMC equations
- analyze SMC stability
- prove Lyapunov stability for SMC

### Characterization of Optical Communication in a Leader-Follower UUV Formation

- introduce optical communication in UUV formation
- describe light field characterization
- design photo-detector array
- evaluate communication algorithms
- determine optimal spectral range
- measure range between leader and follower vehicles
- modify array design and algorithms
- develop control design for distance detection
- model light field using Gaussian function
- integrate light field model into UUV equations of motion
- construct and test photo-detector array
- discuss limitations of underwater light
- introduce theoretical background
- describe beam pattern
- explain inverse square law
- explain Beer-Lambert law
- describe experimental setup
- present results and discussion

### Optical Detector Array Design for Navigational Feedback Between UUVs

- introduce optical detector array design for UUVs
- motivate 5-DOF motion detection
- describe planar and curved array designs
- introduce simulator for array design evaluation
- define performance criteria for detector array
- discuss environmental considerations for light source
- model light source radiance and beam pattern
- describe beam pattern angular terms
- discuss environmental background noise
- model hardware noise sources
- discuss geometrical design of array
- introduce simulator for array design evaluation
- describe simulator functionality
- define operational distance for underwater communication
- establish reference frame for simulator
- introduce detector array design
- define planar detector array geometry
- define curved detector array geometry
- describe radiometric calculations
- simulate light field and detector signals
- introduce SAM algorithm for image comparison
- analyze simulator output images
- compare planar and curved array performances
- evaluate detector array geometry
- investigate array size effects
- experimentally validate simulator results
- discuss simulator limitations and assumptions
- discuss detector array design criteria
- discuss alternative hardware components
- conclude detector array simulator development
- summarize array design evaluation results
- summarize conclusions

### Pose Detection and Control Algorithms for Dynamic Positioning of UUVs Via an Optical Sensor Feedback System

- introduce optical feedback system for UUV dynamic positioning
- describe two pose detection methods: SAM and image moment variants
- compare pose detection methods to traditional image processing algorithm
- introduce numerical simulator for testing feedback controllers
- describe two simulated control scenarios: static-dynamic and dynamic-dynamic systems
- motivate use of curved optical detector array for pose detection
- design detector array interface and numerical simulator
- develop pose detection algorithms: phase correlation and log-polar transform
- describe SAM algorithm for pose detection
- calculate image moment invariants for pose detection
- implement PID and SMC for UUV control in simulated scenarios
- evaluate performance of optical-based feedback control system
- introduce pose detection and control algorithms for dynamic positioning of UUVs
- define control problem for static-dynamic system
- describe image moments approach for pose detection
- summarize calibration procedure for image moments approach
- outline static-dynamic system algorithm
- present results for single-DOF SMC with 21×21 detector array
- present results for single-DOF SMC with 5×5 detector array
- evaluate PID control for x-axis translation
- describe case study for dynamic positioning with multiple concurrent initial pose errors
- describe case study for dynamic positioning with multiple concurrent initial pose errors and added disturbances
- introduce dynamic-dynamic system scenario
- describe control strategy for dynamic-dynamic system
- present results for dynamic-dynamic system scenario
- discuss simulation results and performance of pose detection algorithms
- compare performance of SMC and PID controllers
- discuss effect of detector array size on dynamic positioning
- summarize conclusions for static-dynamic system scenario
- summarize conclusions for dynamic-dynamic system scenario
- discuss limitations and potential improvements for pose detection and control algorithms
- conclude on the feasibility of UUV pose detection and control algorithms for dynamic positioning

### Experimental Pose Detection for UUV Control System Using an Optical Detector Array

- introduce UUV control system using optical detector array
- motivate UUV docking applications
- describe experimental setup for pose detection
- summarize Monte Carlo simulation results
- introduce introduction to UUVs and docking stations
- describe funnel-docking station architecture
- describe pole-docking station architecture
- motivate optical communication for docking
- introduce pose detection approach
- describe detector module components
- describe detector array geometry and design
- introduce methodology for empirical measurements
- describe wave and tow tank experimental setup
- describe calibration procedure for photodiodes
- describe calibration procedure for pose estimation
- describe temperature calibration procedure
- describe noise and cross-talk calibration procedure
- introduce performance evaluation criteria
- describe positioning accuracy evaluation
- describe velocity estimation accuracy evaluation
- introduce stochastic assessment of pose uncertainty
- summarize results of calibration and Monte Carlo simulations
- Introduce experimental pose detection for UUV control system using an optical detector array.
- Describe temperature compensation for photodiode response.
- Investigate noise and cross-talk in signal transmission.
- Conduct underwater calibration procedure for pose estimation.
- Summarize performance evaluation results.
- Describe pose detection algorithm for x-axis estimation.
- Describe pose detection algorithm for y and z-axis estimation.
- Evaluate system performance for stationary and dynamic cases.
- Present experimental results for case 1: light source and UUV platform aligned.
- Present experimental results for case 2: light source and UUV platform at maximum offset.
- Introduce stochastic model results using Monte Carlo simulations.
- Describe first Monte Carlo simulation scenario: comparing experimental pose estimations to model generated pose estimations.
- Describe second Monte Carlo simulation scenario: conceptual UUV navigating in xy-plane.
- Discuss experimental results and limitations.
- Identify potential contributors to zig-zag behavior and offsets in pose outputs.
- Discuss importance of filtering velocity signal for UUV control system.
- Suggest hardware improvements for pose detection results.
- Discuss design features and limitations of hemispherical detector array.
- Identify factors limiting calibration range.
- Discuss importance of distinguishing between y-axis and yaw motion.
- Present Monte Carlo simulation results for cross-talk between yaw and y-axis motion.
- Discuss potential applications of optical detector array design beyond UUV navigation and pose detection.
- Conclude that optical communication for UUV navigation and docking provides an accurate and cost-effective positioning system.

### Discussion

- characterize underwater environment
- discuss limitations of single light source
- describe detector array dimensions
- discuss pose detection capabilities
- evaluate image processing algorithms
- compare PID and SMC controllers
- discuss accuracy of pose detections
- identify factors affecting pose estimation accuracy
- discuss limitations of system in real-world conditions
- summarize conclusions

### Conclusions

- summarize proof of concept
- discuss pose detection capabilities
- summarize limitations of system
- discuss importance of hardware selection
- conclude on feasibility of optical detection system

### Photodiode Data Collection Procedure Using Beagleboard-XM and Two Arduinos

- describe data collection procedure
- explain Arduino setup
- describe BB-XM setup
- discuss serial communication protocol
- explain data collection code
- summarize data collection procedure

### Programs for Experimental Data Collection and Analysis

- list programs for data collection and analysis

