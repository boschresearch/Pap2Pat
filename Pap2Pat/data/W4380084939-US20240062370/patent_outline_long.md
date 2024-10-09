# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH

- acknowledge government support

## BACKGROUND

- motivate esophageal disorder diagnosis
- limitations of current diagnosis techniques

## SUMMARY OF THE DISCLOSURE

- introduce method for flow analysis
- compute spatiotemporal parameters
- generate quantitative flow analysis data

## DETAILED DESCRIPTION

- describe systems and methods for quantifying esophageal bolus transport and esophageal mechanics
- introduce machine learning model to process geometric or other spatiotemporal parameters
- estimate quantitative parameters of the bolus and/or esophagus
- compute other parameters from estimated values
- describe advantages of the proposed framework
- enhance resolution of dynamic MRI at specific locations
- adapt to analyze tubular organs in the human body
- provide a more robust analytical framework than current pure physics-based tools
- predict with missing information in the medical images
- describe a hybrid computational framework
- refer to the framework as a mechanics-informed MRI (“MRI-MECH”) framework
- predict esophageal wall properties and motility
- describe the MRI-MECH framework in more detail
- use simple fluids as the swallowed contrast agent for the dynamic MRI
- generate an image sequence as input to the MRI-MECH framework
- model the esophagus as a flexible one-dimensional tube
- solve one-dimensional mass and momentum conservation equations
- use a physics-informed neural network (“PINN”) to minimize differences
- ensure that the physics of the fluid flow problem is always followed
- calculate the fluid velocity and pressure during the esophageal transport
- estimate the mechanical health of the esophagus
- predict missing information about the lower esophageal sphincter (“LES”)
- demonstrate the capability of being to scenarios with missing data or poor image resolution
- describe the difficulty of visualizing the LES cross-sectional area in MRI
- enhance the capability of the dynamic MRI by calculating the LES cross-sectional area
- lead to significantly better prediction of the state of the esophagus
- write the mass and momentum conservation equations in one dimension
- non-dimensionalize the equations
- specify the boundary conditions of the problem
- capture the physiological conditions of normal esophageal transport
- describe the problem of missing data for the LES cross-sectional area
- solve the problem using a physics-informed neural network (“PINN”)
- use the final interpolated volume V(x, t) to calculate A(x, t) and U(x, t)
- calculate p(χr,τr) at the specific time instant when the LES cross-section was visible
- select the point χr near the proximal end of the LES
- calculate the stiffness, kr, at χr
- calculate the pressure pt=p(χr,τ) at other times with the tube-law
- ensure an unique solution for Ales
- describe an example neural network architecture for the PINN
- define the losses for the PINN
- train the network using Tensorflow for 100,000 epochs
- access medical imaging data
- acquire medical imaging data
- describe medical imaging data
- extract bolus model
- construct bolus geometry model
- segment medical imaging data
- describe segmentation approach
- extract cross-sectional areas
- generate center line
- project voxels onto planes
- calculate cross-sectional area
- store bolus geometry model data
- compute spatiotemporal parameter data
- non-dimensionalize spatiotemporal parameters
- access machine learning model
- describe machine learning model architecture
- train machine learning model
- input spatiotemporal parameter data
- generate quantitative flow analysis parameter data
- compute esophageal wall stiffness
- compute active relaxation
- display quantitative parameter data
- describe PINN model
- predict cross-sectional area
- predict fluid velocity
- predict fluid pressure
- describe LES cross-sectional area
- describe bolus fluid velocity
- describe bolus flow rate
- describe fluid pressure variation
- estimate esophageal wall stiffness
- estimate active relaxation
- describe minimum K/θ
- describe active relaxation parameter θ
- compare K/θ and θ
- conclude esophageal function analysis
- introduce 3D U-Net for semantic segmentation
- describe architecture of 3D U-Net
- explain batch normalization
- describe training data preparation
- explain manual segmentation
- describe data augmentation techniques
- specify loss function
- describe hyperparameter tuning
- present results of benchmark trial
- compare results of different annotation sparsity trials
- introduce system for performing mechanics-informed analysis
- describe computing device and server
- explain communication network
- describe data source
- illustrate system architecture
- describe hardware components of computing device
- explain processor and display
- describe inputs and communication systems
- specify memory components
- describe server hardware components
- explain processor and display
- describe inputs and communication systems
- specify memory components
- describe data source hardware components
- explain processor and data acquisition systems
- describe communication systems
- specify memory components
- describe data source inputs and outputs
- explain communication systems
- describe memory components
- note computer-readable media
- define component, system, module, and framework
- describe method of using devices or systems
- describe method of implementing capabilities
- describe method of installing components
- describe method of manufacturing or using devices or systems
- describe method of installing devices or systems
- describe method of using features and implemented capabilities
- describe method of utilizing devices or systems
- describe method of installing disclosed components
- describe method of using disclosed features and implemented capabilities

