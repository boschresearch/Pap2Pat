# DESCRIPTION

## TECHNICAL FIELD

- define technical field

## BACKGROUND

- limitations of existing systems
- need for spatial distribution sensing

## SUMMARY

- introduce perturbation-modulated light
- summarize non-imaging color sensors
- explain light transport model
- describe occupancy estimation options
- outline smart lighting system
- summarize method for controlling lighting
- describe lighting control system

## DETAILED DESCRIPTION

- introduce occupancy sensitive smart lighting system
- define occupancy
- describe control strategy module and occupancy sensing module
- illustrate smart lighting system with FIGS. 1 and 2
- describe sensing stage
- describe adjusting stage
- illustrate perturbation modulated light with FIG. 9
- describe flexibility of system design
- illustrate computer system for implementing lighting control system with FIG. 3
- describe control strategy module components
- describe strategy manager
- describe lighting controller
- describe base light manager
- describe perturbation manager
- describe occupancy sensing module components
- describe perturbation strategy
- describe sensor data manager
- describe light transport modeler
- describe occupancy estimation system
- describe light transport model or matrix
- illustrate relationship between x and y
- describe elimination of vector b
- describe solving for A with pseudo-inverse
- describe underdetermined system
- describe sparsity assumption
- describe minimization of difference between A and A0
- describe target functions for E
- describe rank minimization problem
- describe sparse recovery problem

### Rank Minimization

- describe rank minimization problem
- describe solution to rank minimization problem
- describe equivalence to Frobenius norm minimization
- describe sparse recovery problem

### Perturbation-Modulated Lighting

- describe strategies for perturbing base light
- describe requirements for perturbation patterns
- describe choice of perturbation magnitude
- describe arrangement of perturbation patterns
- describe optimization problem for perturbation sequence
- describe graph interpretation and solution

### Analysis of the Light Transport Matrix

- introduce light transport matrix
- describe dependency on room occupancy
- explain classification task
- motivate four-category classification problem
- motivate fifteen-category classification problem
- describe supervised learning approach
- explain feature extraction from matrix E
- describe radial basis function kernel support vector machine
- explain performance measurement using mean average precision
- present experimental results for four-category classification
- present experimental results for fifteen-category classification
- discuss limitations of classification approach

### Volume Rendering

- introduce 3D scene estimation approach
- explain light blockage model
- describe aggregation of matrix E
- define direct path from fixture to sensor
- explain point-to-line distance computation
- define confidence of point being occupied
- describe Gaussian kernel function
- explain normalization term for non-uniform spatial distribution
- discuss isotropic assumption for σ
- describe 3D volume rendering
- explain 3D confidence map
- discuss limitations of 3D scene estimation approach
- motivate occupancy map estimation with light reflection model
- describe physical quantities of fixtures and sensors
- explain luminous intensity and luminous flux
- describe polar luminous intensity distribution function
- explain Lambertian surface assumption
- derive luminous flux arriving at ds1
- derive luminous flux arriving at ds2
- explain reflection kernel computation
- describe confidence map computation
- discuss sensor response modeling
- explain reflection kernel precomputation
- describe weighted sum of reflection kernels
- discuss limitations of occupancy map estimation approach
- introduce flow diagram for smart lighting system
- describe initial base light control values setting
- explain sequence of perturbations introduction
- describe sensor information collection
- explain light transport model storage
- describe estimated occupancy calculation
- explain base light adjustment
- discuss periodic repetition of process
- introduce computing system architecture
- describe processor and memory components
- explain input/output and communications pathway
- discuss computer readable storage medium

