# DESCRIPTION

## STATEMENT OF FEDERALLY SPONSORED RESEARCH

- acknowledge government support

## BACKGROUND

- motivate esophageal disorder diagnosis

## SUMMARY OF THE DISCLOSURE

- outline quantitative flow analysis method

## DETAILED DESCRIPTION

- introduce esophageal bolus transport and mechanics analysis
- describe machine learning model for processing medical imaging data
- outline advantages of proposed framework over current tools
- motivate application to esophageal disorders diagnosis
- introduce MRI-MECH framework for esophageal transport analysis
- describe one-dimensional fluid flow model through flexible tube
- derive mass and momentum conservation equations
- define pressure tube-law for esophageal wall properties
- specify boundary conditions for normal esophageal transport
- describe limitations of low spatial resolution dynamic MRI
- motivate need for accurate LES cross-sectional area measurement
- introduce physics-informed neural network (PINN) for solving problem
- describe PINN architecture and training process
- define measurement losses for α, u, and p
- define residual losses for mass and momentum conservation equations
- enforce Dirichlet pressure boundary condition
- describe constraint for LES cross-sectional area
- define total loss for PINN training
- normalize χ and τ for PINN training
- outline example implementation details for PINN training
- access medical imaging data
- extract bolus model from medical imaging data
- compute spatiotemporal parameter data
- access machine learning model
- input spatiotemporal parameter data to machine learning model
- generate quantitative flow analysis parameter data
- compute esophageal wall stiffness and active relaxation
- display or store quantitative flow analysis parameter data
- motivate use of physics-informed neural networks
- describe training of machine learning model
- describe architecture of machine learning model
- motivate use of non-dimensionalized parameters
- describe computation of cross-sectional area
- describe computation of esophageal wall stiffness
- describe computation of active relaxation
- describe prediction of cross-sectional area, fluid velocity, and fluid pressure
- describe variation of LES cross-sectional area
- describe variation of bolus fluid velocity, flow rate, and fluid pressure
- introduce 3D U-Net for semantic segmentation
- describe architecture of 3D U-Net
- detail batch normalization and training parameters
- explain data preparation and annotation
- describe data augmentation techniques
- specify loss function and optimization algorithm
- report hyperparameter tuning and results
- compare performance with varying annotation sparsity
- introduce system for performing mechanics-informed analysis
- describe computing device and server components
- detail communication network and data source
- illustrate hardware components of computing device and server
- describe memory and storage components
- detail communication systems and input/output devices
- explain data acquisition systems and medical imaging systems
- describe memory and storage components of data source
- detail communication systems of data source
- note transitory and non-transitory computer-readable media
- define components, systems, and modules in computer implementation
- provide general disclosure and scope of the invention

